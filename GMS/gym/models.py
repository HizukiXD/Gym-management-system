from django.db import models
from django.core.validators import MinLengthValidator, EmailValidator, MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError
from datetime import date

# Enquiry Model
class Enquiry(models.Model):
    name = models.CharField(max_length=60)
    contact = models.CharField(
        max_length=10,
        validators=[
            MinLengthValidator(10, "Contact number must be 10 digits."),
        ],
    )
    emailid = models.CharField(
        max_length=60,
        validators=[EmailValidator("Enter a valid email address.")],
    )
    age = models.CharField(
        max_length=40,
        validators=[
            MinValueValidator(1, "Age must be greater than  0."),
        ],
    )
    gender = models.CharField(max_length=10, choices=[("Male", "Male"), ("Female", "Female")])

    def clean(self):
        if not self.contact.isdigit():
            raise ValidationError("Contact number must contain only digits.")
        if int(self.age) <= 1:
            raise ValidationError("Age must be a positive number.")

    def __str__(self):
        return self.name


# Equipment Model
class Equipment(models.Model):
    name = models.CharField(max_length=100)
    price = models.CharField(
        max_length=10,
        validators=[
            MinValueValidator(1, "Price must be greater than 0."),
        ],
    )
    unit = models.CharField(max_length=10)
    date = models.CharField(max_length=40)
    description = models.CharField(max_length=500)

    def clean(self):
        if not self.price.isdigit():
            raise ValidationError("Price must be a valid number.")

    def __str__(self):
        return self.name


# Plan Model
class Plan(models.Model):
    name = models.CharField(max_length=50)
    amount = models.CharField(
        max_length=10,
        validators=[
            MinValueValidator(1, "Amount must be greater than 0."),
        ],
    )
    duration = models.CharField(max_length=10)

    def clean(self):
        if not self.amount.isdigit():
            raise ValidationError("Amount must be a valid number.")

    def __str__(self):
        return self.name


# Member Model
class Member(models.Model):
    name = models.CharField(max_length=50)
    contact = models.CharField(
        max_length=10,
        validators=[
            MinLengthValidator(10, "Contact number must be 10 digits."),
        ],
    )
    emailid = models.CharField(
        max_length=50,
        validators=[EmailValidator("Enter a valid email address.")],
    )
    age = models.CharField(
        max_length=40,
        validators=[
            MinValueValidator(1, "Age must be greater than 0."),
        ],
    )
    gender = models.CharField(
        max_length=10,
        choices=[("Male", "Male"), ("Female", "Female")],
        default="",
    )
    plan = models.CharField(max_length=50)
    joindate = models.DateField()
    expiredate = models.DateField()
    initialamount = models.CharField(
        max_length=10,
        validators=[
            MinValueValidator(1, "Initial amount must be greater than 0."),
        ],
    )

    def clean(self):
        if not self.contact.isdigit():
            raise ValidationError("Contact number must contain only digits.")
        if int(self.age) <= 0:
            raise ValidationError("Age must be a positive number.")
        if self.expiredate <= self.joindate:
            raise ValidationError("Expire date must be after join date.")
        if not self.initialamount.isdigit():
            raise ValidationError("Initial amount must be a valid number.")

    def __str__(self):
        return self.name