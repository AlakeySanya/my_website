from django.db import models

class PersonalInfo(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    biography = models.TextField()
    profile_picture = models.ImageField(upload_to='profile_pics/')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Hobby(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='hobbies/')

    def __str__(self):
        return self.title
