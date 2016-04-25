from django.db import models

class Signin(models.Model):
	uname=models.CharField(max_length=200)
	mnunber=models.IntegerField()
	mailid=models.CharField(max_length=200)
	address=models.CharField(max_length=200)
	password=models.IntegerField()
	cofirmpassword=models.IntegerField()


class Login(models.Model):
	uname=models.CharField(max_length=200)
	password=models.IntegerField()
	

