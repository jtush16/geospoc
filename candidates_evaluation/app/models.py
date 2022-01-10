from django.db import models


# Create your models here.


class Candidate(models.Model):     # Candidate(name,email,web,cover_letter,cv,like)

    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    web = models.CharField(max_length=60)
    cover_letter = models.FileField(upload_to='cover_letter/',null=True)
    cv = models.FileField(upload_to='cv/', null=True)
    like = (
            ('Yes', 'Yes'),
            ('No','No'),
            )
    like = models.CharField(max_length=200, choices=like)

    @classmethod
    def dummy_candidate(cls):
        return Candidate(id = '', name = ' ', email = ' ',
                         web = ' ', cover_letter = None, cv = None,
                         like = ' ')


class Registration(models.Model):       # Registration(name,email,password,confirm_password)
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=150)
    confirm_password = models.CharField(max_length=150)

class Ratings(models.Model):
    like = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5')
    )
    like = models.CharField(max_length=200, choices=like)









