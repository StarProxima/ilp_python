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
    id = models.IntegerField(primary_key=True)
    fio = models.CharField(max_length=100)
    work_experience = models.IntegerField()


class Guard(models.Model):
    id = models.IntegerField(primary_key=True)
    chief = models.ForeignKey(Chief, models.DO_NOTHING, db_column='ChiefID')
    fio = models.CharField(max_length=100)
    work_experience = models.IntegerField()


class Post(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)


class OnDuty(models.Model):
    id = models.IntegerField(primary_key=True)
    guard = models.ForeignKey(Guard, models.DO_NOTHING, db_column='GuardID')
    post = models.ForeignKey(Post, models.DO_NOTHING, db_column='PostID')
    chief = models.ForeignKey(Chief, models.DO_NOTHING, db_column='ChiefID')
    exit_time = models.DateTimeField()


class Remark(models.Model):
    id = models.IntegerField(primary_key=True)
    guard = models.ForeignKey(Guard, models.DO_NOTHING, db_column='GuardID')
    post = models.ForeignKey(Post, models.DO_NOTHING, db_column='PostID')
    chief = models.ForeignKey(Chief, models.DO_NOTHING, db_column='ChiefID')
    remark = models.CharField(max_length=100)
