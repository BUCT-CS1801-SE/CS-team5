from django.db import models
# Create your models here.

class newstable(models.Model):
    newsID = models.AutoField(unique=True, primary_key=True)#主键
    museumID = models.IntegerField() #应该是外键,合并的时候再说
    newsTitle = models.TextField()
    newsTime = models.DateField()
    newsmaintext = models.TextField()
    attitude = models.TextField(max_length=45)
    status = models.IntegerField()

class explaintable(models.Model):
    explanationID = models.AutoField(unique=True,primary_key=True)
    explanationName = models.TextField(max_length=45)
    explainerID = models.IntegerField()
    explanationTime = models.IntegerField()
    explanationLanguage = models.TextField(max_length=45)
    recommendedTime = models.FloatField()
    status = models.IntegerField()

class userComments(models.Model):
    commentID = models.AutoField(unique=True,primary_key=True)
    userID = models.IntegerField()
    museumID = models.IntegerField()
    comment = models.TextField(max_length=1000)
    sentiAnalysis_environment = models.IntegerField()
    sentiAnalysis_exhibit = models.IntegerField()
    sentiAnalysis_service = models.IntegerField()
    commentdata = models.DateField()
    status = models.IntegerField()
