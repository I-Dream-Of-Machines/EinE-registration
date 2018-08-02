from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator


# AKEB Members (each has different functionality, and different access)


class RegionalMember(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    region = models.CharField(max_length=2)
    role = models.IntegerField()  # 1-Excellence in Education, 2-Monitoring and Evaluation
    status = models.BooleanField()  # 0-Inactive, 1-Active - to allow access to be disabled after the EoT


# class NationalMember(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     role = models.IntegerField()  # 1-Excellence in Education, 2-Monitoring and Evaluation
#     status = models.BooleanField()  # 0-Inactive, 1-Active - to allow access to be disabled
#
#
# class NationalConvener(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     role = models.IntegerField()  # 1-Robotics, 2-iCOMPUTE, 3-Let's Speak
#     status = models.BooleanField()  # 0-Inactive, 1-Active - to allow access to be disabled
#
#
# class Facilitator(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     curriculum_vitae = models.FileField()
#     region = models.CharField(max_length=2)  # Facilitation Region
#
#
# class Guardian(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     phone_regex = RegexValidator(regex=r'^\d{3}\-\d{3}\-\d{4}',
#                                  message="Phone number must be in the format: 999-999-9999")
#     primary_contact_number = models.CharField(validators=[phone_regex])
#     secondary_contact_number = models.CharField(validators=[phone_regex])
#     address = models.TextField()  # Use Canada Post??
#
#
# class Child(models.Model):
#     user = models.OneToOneField(Guardian, on_delete=models.CASCADE)
