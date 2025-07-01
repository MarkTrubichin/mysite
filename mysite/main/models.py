from django.db import models

class Project(models.Model):
    PROJECT_TYPE_CHOICES = [
        ('commercial', 'Commercial'),
        ('personal', 'Personal'),
    ]

    title = models.CharField(max_length=100)
    project_type = models.CharField(max_length=20, choices=PROJECT_TYPE_CHOICES, default='personal')
    category = models.CharField(max_length=20, default='other')
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='projects/', blank=True)

    def __str__(self):
        return self.title
