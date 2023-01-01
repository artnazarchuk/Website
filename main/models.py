from django.db import models

class Main_model(models.Model):
    title = models.CharField('Title', max_length=50)
    description = models.TextField('description')
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    image = models.FileField(upload_to='img/')

    def __str__(self):
        return self.title
