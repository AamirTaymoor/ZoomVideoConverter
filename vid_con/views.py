
from urllib import response
from wsgiref.util import request_uri
from django.shortcuts import render, HttpResponse
from converter import Converter
import urllib.request
import os
import pyrebase
from pathlib import Path
import vid_con
from .models import Video
from django.core.files import File
import json
BASE_DIR = Path(__file__).resolve().parent.parent

id = []
urls = []
meeting_id = []
recording_start = []
recording_end = []

# Create your views here.
def testing(request):
    s = request.get_full_path()
    return HttpResponse(s)
    #return render(request, 'vid_con/loading.html')
def home(request):
    return render(request, 'vid_con/home.html')
def con_video(request):
    recording_id = []
    urls = []
    meeting_id = []
    recording_start = []
    recording_end = []
    with open('/home/aamir/Desktop/zoom/zoom/meeting_info.json', 'r') as f:
        zoom_res = json.load(f)
    #recording_files = zoom_res['recording_files']
    recording_files = zoom_res['meetings'][0]['recording_files']
    print(recording_files)
    for u in recording_files:
        urls.append(u['download_url'])
        recording_id.append(u['id'])
        meeting_id.append(u['meeting_id'])
        recording_start.append(u['recording_start'])
        recording_end.append(u['recording_end'])
    path = "/home/aamir/Desktop/zoom/zoom/out_vid_container/"
    in_file_path = '/home/aamir/Desktop/zoom/zoom/in_vid_container/video.mp4'
    out_file_path = "/home/aamir/Desktop/zoom/zoom/out_vid_container/con_video.mp4"
    for i in range(len(urls)):
        urllib.request.urlretrieve(urls[i], in_file_path)
        
        c = Converter()

        info = c.probe(in_file_path)

        conv = c.convert(in_file_path, out_file_path, {
            'format': 'mp4',
            'audio': {
                'codec': 'aac',
                'samplerate': 11025,
                'channels': 2
            },
            'video': {
                'codec': 'h264',
                'width': 720,
                'height': 400,
                'fps': 15
            }})
        #flag = 0
        for timecode in conv:
            if timecode >= 100:
                print("Converting (%f) ...\r" % timecode)
                #flag = 1
        
            #print('selected file removed')
        #else:
        
            #print('file not found')
        os.remove(in_file_path)

        fname = os.path.join(path, os.listdir(path)[0])
        #file_name = os.path.basename(fname)
        obj,created1 = Video.objects.get_or_create(meeting_id=meeting_id[i], recording_id= recording_id[i])
        if created1 == True:
            #obj = Video()
            obj.recording_id= recording_id[i]
            obj.meeting_id= meeting_id[i]
            p = Path(fname)
            #f = open(fname,'wb+')
            f = p.open(mode='rb')
            obj.play_url = File(f, name=p.name )
                

            #f = 
            #f.write()
            #myfile = File(f)
            #obj.play_url = p_url
            obj.recording_start = recording_start[i]
            obj.recording_end = recording_end[i]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
            obj.save()
            f.close()   
        else:
            return render(request, 'vid_con/file_exists.html')
           
        if os.path.exists(out_file_path):
            os.remove(out_file_path)

        
    return render(request, 'vid_con/convert.html')

def upload_vid(request):
    firebase = pyrebase.initialize_app(config)
    storage = firebase.storage()
    file_name = ''
    local_path = '/home/aamir/Desktop/zoom/zoom/vid_container/'
    if os.path.isdir(local_path):
        if not os.listdir(local_path):
            file_name =''
        else:
            for f in os.listdir(local_path):
                filename = f

    #if os.path.exists(local_path):
        #os.remove(local_path)
    
    path_on_cloud = "videoconverter-92860.appspot.com/"
    #path_local = "/home/aamir/Desktop/zoom/zoom/vid_container/video.mp4"
    
    if os.path.isdir(local_path):
        if not os.listdir(local_path):
            return HttpResponse('Path directory is empty!!')
        else:
            for f in os.listdir(local_path):
                file_name = f
                path_on_cloud = path_on_cloud+file_name
                path_local = local_path+file_name
                res = storage.child(path_on_cloud).put(path_local)
                os.remove(path_local)
                file_token = res['downloadTokens']
                file_url = storage.child(path_on_cloud).get_url(file_token)
                return HttpResponse("file uploaded at url :" +file_url)   
            
    else:
        return HttpResponse('Directory does not exists')


def get_records(request):
    return render(request, 'vid_con/records.html', { 'event_list' : Video.objects.all()})

def play_video(request):
    #src= request.get_full_path()
    #return HttpResponse(request.build_absolute_uri(location=None))

    return render(request, 'vid_con/vid_play.html')