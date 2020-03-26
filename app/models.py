from django.db import models
import re

EMAIL_REGEX = re.compile(r"^[a-zA-Z0-9.+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]+$")


class UserManager(models.Manager):
    def validator(self, data):
        errors = {}
        if len(data["fname"]) < 2:
            errors["fname"] = "First name has to be 2 chars"
        if len(data["lname"]) < 2:
            errors["lname"] = "Last name has to be 2 chars"
        if not EMAIL_REGEX.match(data["email"]):
            errors["email"] = "Email is invalid"
        if data["password"] != data["cpassword"]:
            errors["password"] = "Passwords do not match"
        if len(data["password"]) < 8:
            errors["password"] = "Password is too short"
        return errors


class User(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=60)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()


class Budget(models.Model):
    account = models.CharField(max_length=100)
    total_amount = models.IntegerField(default=0)
    budget = models.IntegerField(default=0)
    created_by = models.ForeignKey(
        User, related_name="user_budget", on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Tracker(models.Model):
    category = models.CharField(max_length=100)
    item = models.CharField(max_length=100)
    planned_amount = models.IntegerField(default=0)
    created_by = models.ForeignKey(
        User, related_name="user_tracker", on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


# class Work(models.Model):
#     description
#     date_wored_on
#     user_worked
#     created_at
#     updated_at
