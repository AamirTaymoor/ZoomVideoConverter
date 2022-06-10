from django.urls import path
from . import views
urlpatterns = [
    path('',views.home, name = 'home-page'),
    path('convert',views.con_video, name = 'con-video'),
    path('testing',views.testing, name = 'testing-page'),
    path('upload',views.upload_vid, name = 'uploading-page'),
    #path('store',views.store, name = 'store-page'),
    path('records',views.get_records, name = 'records-page'),
    #path('media',views.play_video, name = 'play-page'),
    path('media/videofiles/',views.play_video, name = 'play-page'),

] 