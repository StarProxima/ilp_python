from django.db import models


class Brend(models.Model):
    name_brend = models.CharField(max_length=50)
    country = models.CharField(max_length=50)


class Stock(models.Model):
    name_stock = models.CharField(max_length=50)
    start_stock = models.CharField(max_length=50)
    finish_stock = models.CharField(max_length=50)
    persent_stock = models.CharField(max_length=50)


class Product(models.Model):
    name_product = models.CharField(max_length=50)
    catagory = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    brend = models.ForeignKey(Brend, on_delete=models.CASCADE)
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)


class Chief(models.Model):
    ChiefID = models.IntegerField(primary_key=True)
    FIO = models.CharField(max_length=100)
    WorkExperience = models.IntegerField()


class Guard(models.Model):
    GuardID = models.IntegerField(primary_key=True)
    ChiefID = models.ForeignKey(Chief, models.DO_NOTHING, db_column='ChiefID')
    FIO = models.CharField(max_length=100)
    WorkExperience = models.IntegerField()


class Post(models.Model):
    PostID = models.IntegerField(primary_key=True)
    Name = models.CharField(max_length=100)
    Location = models.CharField(max_length=100)


class OnDuty(models.Model):
    OnDutyID = models.IntegerField(primary_key=True)
    GuardID = models.ForeignKey(Guard, models.DO_NOTHING, db_column='GuardID')
    PostID = models.ForeignKey(Post, models.DO_NOTHING, db_column='PostID')
    ChiefID = models.ForeignKey(Chief, models.DO_NOTHING, db_column='ChiefID')
    ExitTime = models.DateTimeField()


class Remark(models.Model):
    RemarkID = models.IntegerField(primary_key=True)
    GuardID = models.ForeignKey(Guard, models.DO_NOTHING, db_column='GuardID')
    PostID = models.ForeignKey(Post, models.DO_NOTHING, db_column='PostID')
    ChiefID = models.ForeignKey(Chief, models.DO_NOTHING, db_column='ChiefID')
    Remark = models.CharField(max_length=100)
