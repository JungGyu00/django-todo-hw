from django.db import models


class Todo(models.Model):
    class Meta:
        db_table = "todo"

    user = models.ForeignKey('user.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    content = models.TextField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_done = models.BooleanField(default=False)

    def __str__(self):
        return self.title
