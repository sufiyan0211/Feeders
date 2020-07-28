from django.db import models

# Create your models here.

class Info(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    image = models.ImageField(upload_to='images/')
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title


class Covid(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    image = models.ImageField(upload_to='images/')
    url = models.URLField(blank=True)
    def __str__(self):
        return self.title


class News(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    image = models.ImageField(upload_to='images/')
    url = models.URLField(blank=True)
    def __str__(self):
        return self.title

class Business(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    image = models.ImageField(upload_to='images/')
    url = models.URLField(blank=True)
    def __str__(self):
        return self.title


class Technology(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    image = models.ImageField(upload_to='images/')
    url = models.URLField(blank=True)
    def __str__(self):
        return self.title


class Educations(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    image = models.ImageField(upload_to='images/')
    url = models.URLField(blank=True)
    def __str__(self):
        return self.title


class Fasion(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    image = models.ImageField(upload_to='images/')
    url = models.URLField(blank=True)
    def __str__(self):
        return self.title


class Movies(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    image = models.ImageField(upload_to='images/')
    url = models.URLField(blank=True)
    def __str__(self):
        return self.title


class Series(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    image = models.ImageField(upload_to='images/')
    url = models.URLField(blank=True)
    def __str__(self):
        return self.title


