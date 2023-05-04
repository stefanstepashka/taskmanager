from django.db import models
import datetime
from django.utils import timezone
# Create your models here.


class Tag(models.Model):
    name = models.CharField(unique=True, max_length=50)

    def __str__(self):
        return self.name



def due_date_default():
    return timezone.now() + timezone.timedelta(days=7)



class Task(models.Model):

    STATUS_CHOICES = [
        ('Not Started', 'Not Started'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
    ]
    PRIORITY_CHOICES = [
        (1, 'Low'),
        (2, 'Medium'),
        (3, 'High'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    created_at = models.DateTimeField(
        auto_now_add=True)
    status = models.CharField(
        max_length=12, choices=STATUS_CHOICES, default='Not Started'
    )
    updated_at = models.DateTimeField(auto_now=True)

    start_date = models.DateTimeField(default=timezone.now)
    due_date = models.DateTimeField(default=due_date_default)
    tags = models.ManyToManyField(Tag,  blank=True)
    def __str__(self):
        return self.title


class Subscription(models.Model):
    email = models.EmailField()
    notification_type = models.CharField(max_length=100)
