from django.db import models

# Create your models here.
class Calendar(models.Model):
    SHIFTTYPES = {
            'ph1': 'Pack Holder #1',
            'nh1': 'Non Holder #1',
            'ph2': 'Pack Holder #2',
            'nh2': 'Non Holder #2',
            'bck': 'Backup'
        }
    dayNum = models.IntegerField()
    staffID = models.IntegerField()
    shiftType = models.CharField(max_length=3, choices=SHIFTTYPES)
    #instance.get_shiftType_display() prints value instead of key of SHIFTTYPES