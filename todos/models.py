from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=200, null=True)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=False)

    def __str__(self):
        return self.title
