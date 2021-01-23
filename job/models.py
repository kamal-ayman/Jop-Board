from django.db import models
from datetime import datetime

JOPTYPES = (
    ('computer since', 'computer since'),
    ('artificial intelligence', 'artificial intelligence'),
    ('CC', 'CC'),
)


class Job(models.Model):
    title = models.CharField(max_length=25, default='', null=True)
    jop_type = models.CharField(max_length=50, choices=JOPTYPES, null=True)
    description = models.TextField(max_length=1000, default='', null=True)
    published_at = models.DateTimeField(default=datetime.now, null=True)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experience = models.IntegerField(default=1)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, default=1, null=True)

    def __str__(self):
        return 'Name User: ' + self.title


class Category(models.Model):
    name = models.CharField(max_length=25, default='')

    def __str__(self):
        return self.name
