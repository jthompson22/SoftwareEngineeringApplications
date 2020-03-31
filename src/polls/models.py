from django.db import models
from django.utils import timezone
from jsonfield import JSONField


'''class WaterQuantity(models.Model):
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

        # to implement a return on self.json data.'''


class WaterQualityData(models.Model):
    # it seems like we should make this a "type" for downn the line queries
    #collection process
    collection_data = JSONField()
    #previous information

    
