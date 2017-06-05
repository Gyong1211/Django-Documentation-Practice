from django.db import models


# Create your models here.
class Person(models.Model):
    SHIRT_SIZE = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )
    PERSON_TYPES = (
        ('students', '학생'),
        ('teacher', '선생')
    )

    person_type = models.CharField(
        '유형',
        max_length=10,
        choices=PERSON_TYPES,
        default=PERSON_TYPES[0][0]
    )
    teacher = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        on_delete=models.CASCADE,
    )
    name = models.CharField('이름', max_length=60)
    shirt_size = models.CharField(
        '셔츠사이즈',
        max_length=1,
        choices=SHIRT_SIZE,
        help_text='남자는 L쓰세요'
    )

    def __str__(self):
        return self.name


class Manufacturer(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Car(models.Model):
    name = models.CharField(max_length=40)
    manufacturer = models.ForeignKey(
        Manufacturer,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name
