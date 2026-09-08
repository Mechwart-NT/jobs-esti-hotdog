from django.db import models

ROLE_CHOICES = [
    ('Frontend', 'Frontend'),
    ('Backend', 'Backend'),
    ('Fullstack', 'Fullstack'),
]

LEVEL_CHOICES = [
    ('Junior','Junior'),
    ('Midweight','Midweight'),
    ('Senior','Senior'),
    ('Rocket Science','Rocket Science'),
]

CONTRACT_CHOICES = [
    ("Full Time","Full Time"),
    ("Part Time","Part Time"),
    ("Contract","Contract")
]

class Language(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Tool(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Job(models.Model):
    company = models.CharField(max_length=255)
    #logo = models.ImageField()
    new = models.BooleanField(default=True)
    featured = models.BooleanField(default=False)
    position = models.CharField(max_length=255)
    role = models.CharField(max_length=255, choices=ROLE_CHOICES)
    level = models.CharField(max_length=255, choices=LEVEL_CHOICES)
    postedAt = models.DateTimeField(auto_now_add=True)
    contract = models.CharField(max_length=255, choices=CONTRACT_CHOICES)
    location = models.CharField(max_length=255)
    languages = models.ManyToManyField(Language)
    tools = models.ManyToManyField(Tool)

    def __str__(self):
        return f"{self.position} at {self.company}"