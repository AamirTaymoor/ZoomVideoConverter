from datetime import datetime
from django.db import models

# Create your models here.
class Video(models.Model):
    recording_id = models.CharField(max_length=100, default='None')
    meeting_id = models.CharField(max_length=100, default='None')
    play_url = models.FileField(upload_to='videofiles', null= True, verbose_name='')
    recording_start = models.DateTimeField(default=datetime.now, blank=True)
    recording_end = models.DateTimeField(default=datetime.now, blank=True)
    
    class Meta:
        unique_together = ['recording_id', 'meeting_id']                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 

