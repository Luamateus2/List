from django.db import models
from datetime import timedelta

class Event(models.Model):
    TITLE_MAX_LENGTH = 100

    DAY_OF_WEEK_CHOICES = [
        ('1', 'Monday'),
        ('2', 'Tuesday'),
        ('3', 'Wednesday'),
        ('4', 'Thursday'),
        ('5', 'Friday'),
        ('6', 'Saturday'),
        ('7', 'Sunday'),
    ]

    title = models.CharField(max_length=TITLE_MAX_LENGTH)
    start_date = models.DateField()
    description = models.TextField(blank=True)
    days_of_week = models.CharField(max_length=50, blank=True, default="")
    duration = models.DurationField()  # Example: datetime.timedelta(hours=1, minutes=30)

    def __str__(self):
        return self.title

    def get_days_of_week(self):
        return self.days_of_week.split(',') if self.days_of_week else []

    def set_days_of_week(self, days):
        self.days_of_week = ','.join(days)

