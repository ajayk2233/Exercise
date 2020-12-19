from django.db import models

class School(models.Model):
    gender_choices = (
        ('Male', 'Male'),
        ('Female', 'Female')
    )
    std_choices = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
    )
    name = models.CharField(max_length=30)
    roll_no = models.CharField(max_length=10)
    gender = models.CharField(max_length=6,choices=gender_choices)
    phone = models.CharField(max_length=20)
    std = models.IntegerField(null=True,blank=True,choices=std_choices)
    def __str__(self):
        return(self.name)