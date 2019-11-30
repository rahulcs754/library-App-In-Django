from django.db import models

class Book(models.Model):
    name = models.CharField(max_length = 50)
    picture = models.ImageField()
    author = models.CharField(max_length = 30, default='this is author')
    email = models.EmailField(blank = True)
    describe = models.TextField(default = 'this is a book crud operation')

    def __str__(self):
        return self.name