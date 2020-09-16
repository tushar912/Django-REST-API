from django.db import models


class Todo(models.Model):

    title = model.CharField(max_length=200)
    description= models.TextField()

    def __str__(self):

        return self.title
