# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User


# Create your models here.

class Group(models.Model):
    name = models.CharField(max_length=30)
    date_created = models.DateField(auto_now_add=True)
    last_used = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name 
# TO DO: 
#Subclass  auth user model 
class User(django.contrib.auth.models.User):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    venmo = models.CharField(max_length=30, default="hello")
    email = models.EmailField()
    groups = models.ManyToManyField(Group, through='UserMembership', related_name='people')

    def full_name(self):
        return self.first_name + " " + self.last_name

    def __str__(self):
        return self.first_name + " " + self.last_name

class Receipt(models.Model):
    photo_bucket = models.CharField(max_length=30)
    timestamp = models.DateField(auto_now_add = True)
    total_cost = models.DecimalField(max_digits=5, decimal_places=2)
    tip = models.DecimalField(max_digits=5, decimal_places=2)
    tax = models.DecimalField(max_digits=5, decimal_places=2)
    title = models.CharField(max_length=30)
    is_complete = models.BooleanField()
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    owner = models.ForeignKey(Users, on_delete=models.CASCADE)
    participants = models.ManyToManyField(Users, through='ReceiptMembership',  related_name='participants')

    def __str__(self):
        return self.title


class Item(models.Model):
    name = models.CharField(max_length=30)
    value = models.DecimalField(max_digits=5, decimal_places=2)
    receipt = models.ForeignKey(Receipt, on_delete=models.CASCADE)
    user_owns = models.ForeignKey(Users, on_delete=models.CASCADE)
    # make functions that return cost per user
    def __str__(self):
        return self.name 

class UserMembership(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE,)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    date_joined = models.DateField(auto_now_add=True)
    role = models.CharField(max_length=30)
    def __str__(self):
        return self.user.first_name + " " + self.group.name

class ReceiptMembership(models.Model):
    users = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='users')
    receipt = models.ForeignKey(Receipt, on_delete=models.CASCADE, related_name='receipt')
    outstanding_payment = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.users.first_name + " " + str(self.receipt.timestamp)






