from django.db import models

# Create your models here.
class Projects(models.Model):
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/', blank=True)
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title