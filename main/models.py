from django.db import models

class MainModel(models.Model):
    title = models.CharField('Title', max_length=50)
    description = models.TextField('description')
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    image = models.FileField(upload_to='img/')

    # Для корректного отображения титульника задачи в админке
    def __str__(self):
        return self.title

    # Для корректного отображения полей в админке
    class Meta:
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"
