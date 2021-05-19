from django.db import models

# Create your models here.
class museum(models.Model):
    mu_id = models.AutoField(primary_key=True)

    mu_name = models.CharField(max_length=50)
    mu_location = models.CharField(max_length=100)
    mu_intro = models.TextField()
    mu_open = models.DateField()
    mu_link = models.TextField()
    mu_level = models.TextField()
    mu_tele = models.CharField(max_length=50)
    mu_grade = models.FloatField()
    mu_fee = models.TextField()
    mu_bulid = models.CharField(max_length=50)
    mu_num = models.IntegerField()
    mu_city = models.TextField()
    mu_look = models.IntegerField()
    mu_status = models.IntegerField()


class collection(models.Model):
    co_id = models.AutoField(primary_key=True)
    mu_id = models.IntegerField()
    co_name = models.CharField(max_length=50)
    co_intro = models.TextField()
    co_age = models.CharField(max_length=50)
    co_image = models.CharField(max_length=50)
    co_status = models.IntegerField()


class exhibition(models.Model):
    ex_id = models.AutoField(primary_key=True)
    mu_id = models.IntegerField()
    ex_location = models.TextField()
    ex_time = models.CharField(max_length=128)
    ex_theme = models.CharField(max_length=128)
    ex_intro = models.TextField()
    ex_tele = models.TextField()
    ex_list = models.TextField()
    ex_pic = models.CharField(max_length=128)
    ex_status = models.IntegerField()

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

class userInfo(models.Model):
    userID = models.AutoField(unique=True,primary_key=True)
    username = models.CharField(max_length=45)
    nickname = models.CharField(max_length=45)
    telephone = models.CharField(max_length=45)
    idcard = models.CharField(max_length=45)
    password = models.TextField()
    userRole = models.CharField(max_length=20)
    userCreateDate = models.DateTimeField(auto_now_add=True)

class UploadExplanation(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    name = models.CharField(max_length=200)
    audio = models.FileField()
    visible = models.NullBooleanField(default=True)