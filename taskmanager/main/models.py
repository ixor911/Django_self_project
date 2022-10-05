from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Role(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField('Name', max_length=20)
    description = models.TextField('Description', null=True, blank=True)


class Employee(models.Model):
    def __str__(self):
        return self.name

    login = models.CharField('Login', max_length=30)
    password = models.CharField('Password', max_length=30)
    name = models.CharField('Name', max_length=50)

    email = models.EmailField('Mail', max_length=50, null=True, blank=True)
    age = models.PositiveSmallIntegerField('Age', blank=True, null=True)
    phone = models.CharField('Phone', max_length=20, blank=True)
    imagePath = models.FilePathField('ImagePath', path='main/images', blank=True)

    role = models.ForeignKey(
        Role,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )


class Chat(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField('Name', max_length=20)


class Task(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField('Name', max_length=50)
    date = models.DateField('Date', auto_now=True)

    description = models.TextField('Description', blank=True)

    employees = models.ManyToManyField(
        Employee,
        blank=True
    )

    chat = models.ForeignKey(
        Chat,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )


class Message(models.Model):
    def __str__(self):
        return self.text

    text = models.TextField('Text')
    date = models.DateField('Date', auto_now=True)

    writer = models.ForeignKey(
        Employee,
        on_delete=models.SET('Deleted employee'),
        blank=True
    )

    chat = models.ForeignKey(
        Chat,
        on_delete=models.CASCADE
    )




