from django.db import models
from django.utils import timezone
# from jsonfield import JSONField


class WaterQuantity(models.Model):
    date = models.DateField()

    pressure_difference = models.FloatField()
    pressure_absolute = models.FloatField()
    temperature = models.FloatField()
    water_level = models.FloatField()
    pressure_baro = models.FloatField()
    reference_water_level = models.FloatField()
    water_density = models.FloatField()

    #def __str__(self):
        #return self.question_text

        # to implement a return on self.json data.


class WaterQuality(models.Model):
    # it seems like we should make this a "type" for downn the line queries

    #collection process
    site_id = models.CharField(max_length=50)
    collector_initials = models.CharField(max_length=3)  
    jar_number = models.IntegerField()
    collection_time = models.DateTimeField() 


    '''parameter = models.CharField(max_length=50) 
    pval_one = models.FloatField() #do we want these to have a bound?
    pval_two = models.FloatField()
    pval_three = models.FloatField()

    
    analyst_initials = models.CharField(max_length=3)
    enterer_intials = models.CharField(max_length=3)
    notes = models.TextField()''' #previous information

    
