from django.db import models

# Create your models here.
class Calendar(models.Model):
    dayNum = models.IntegerField(null=True)
    emp = models.ForeignKey('Staff', on_delete=models.CASCADE, related_name="assigned", null=True)
    shiftType = models.CharField(max_length=10)
    def _str__(self):
        return f"{self.staff.stuName} {self.shiftType}"

class Staff(models.Model):
    stuID = models.IntegerField(primary_key=True, unique=True)
    stuName = models.CharField(max_length = 30)
    timeOff = models.ManyToManyField(Calendar)
    numPH1 = models.IntegerField()
    numNH1 = models.IntegerField()
    numPH2 = models.IntegerField()
    numNH2 = models.IntegerField()
    numBackup = models.IntegerField()
    def __str__(self):
        return f"{self.stuID} {self.stuName} PH1 Shift: {self.numPH1} NH1 Shift: {self.numNH1}"