import datetime

from django.db import models
from django.utils import timezone

class DataField(models.Model):
    field_text = models.CharField(max_length=50)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.field_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class DataInput(models.Model):
    field = models.ForeignKey(DataField, on_delete=models.CASCADE)
    data_text = models.CharField(max_length=200)
    data_nums = models.IntegerField(default=0)

    def __str__(self):
        return self.data_text
