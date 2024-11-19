from django.db import models


# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/')
    url = models.URLField()

    class Meta:
        db_table = 'project'

    def __str__(self):
        return self.title


class Link(models.Model):
    title = models.CharField(max_length=250)
    url = models.URLField()

    class Meta:
        db_table = 'link'

    def __str__(self):
        return self.title


class Resume(models.Model):
    file = models.FileField(upload_to='resume')

    class Meta:
        db_table = 'resume'


class Skill(models.Model):
    name = models.CharField(max_length=250)

    class Meta:
        db_table = 'skill'

    def __str__(self):
        return self.name


class About(models.Model):
    text = models.TextField()

    class Meta:
        db_table = 'about'
