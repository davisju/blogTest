from django.db import models

# Create your models here.
class Ariticle(models.Model):
    DEVELOPMENT = "dv"
    PERSONAL = "ps"
    CATEGORY_CHOICES = {
        (DEVELOPMENT, "development"),
        (PERSONAL, "personal"),
    }
    title = models.CharField(max_length=200)
    content = models.TextField()
    category = models.CharField(max_length=2,
    choices=CATEGORY_CHOICES,
    default=DEVELOPMENT,
    )
class Comment(models.Model):
    article = models.Foreignkey(Ariticle, on_delete=models.CASCADE)
    username = models.CharField(max_length=50)
    content = model.CharField(max_length=200)

class HashTag(models.Model):
    name = models.CharField(max_length=50)
    content = model.CharField(max_length=200)

class Question(models.Model):
    question_text =models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

class Choice(models.Model):
    question = models.Foreignkey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)    
