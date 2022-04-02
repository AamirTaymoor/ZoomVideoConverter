import json
f = open('/home/aamir/Desktop/zoom/zoom/vid_con/meeting_info.json', 'r')
info = json.load(f)
recording_files = info['recording_files']
f.close
id = []
urls = []
meeting_id = []
recording_start = []
recording_end = []

for u in recording_files:
    urls.append(u['download_url'])
    meeting_id.append(u['meeting_id'])
    recording_start.append(u['recording_start'])
    recording_end.append(u['recording_end'])
print(recording_start)                                                                                                                                                                                                                                                                                                 