from django.db import models

# Create your models here.

class Place(models.Model):
    name = models.CharField(max_length=200)
    visited = models.BooleanField(default=False)

    date_visited = models.DateField(max_length=20, default='not visited')
    review = models.CharField(max_length=300, default='not visited')

    def __str__(self):
        return '%s visited? %s' % (self.name, self.visited)
