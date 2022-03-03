from django.db import models
from django.utils import timezone


class Data(models.Model):
    title = models.CharField(max_length=30, null=True)
    date = models.DateTimeField(default=timezone.now)
    critical = models.IntegerField()
    deaths = models.IntegerField()
    today_new_deaths = models.IntegerField()
    today_new_confirmed = models.IntegerField()
    confirmed = models.IntegerField(null=True)
    recovered = models.IntegerField(null=True)

    def __str__(self):
        return str(self.date.strftime("%Y/%m/%d"))
