from django.db import models


# Create your models here.

class Person(models.Model):
    SHIRT_SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large')
    )

    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES, help_text='셔츠 사이즈 선택')
    first_name = models.CharField('이름', max_length=30)
    last_name = models.CharField('성', max_length=30)

    def __str__(self):
        return f'{self.last_name}{self.first_name}'
