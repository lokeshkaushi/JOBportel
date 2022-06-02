from django.db import models
class Job(models.Model):
    jobtitle = models.CharField(max_length=50)
    jobdiscription = models.CharField(max_length=50)

class Candidate(models.Model):
    email= models.CharField(max_length=50)
    jobid = models.CharField(max_length=50)
    applydate = models.CharField(max_length=50)
    cname = models.CharField(max_length=50)


class Registration(models.Model):
    email =models.CharField(max_length=100)
    password =models.CharField(max_length=100)
    mobileno =models.CharField(max_length=100)
    technology =models.CharField(max_length=100)
    candidatetype =models.CharField(max_length=100)
    higherquli =models.CharField(max_length=100)

class HrReg(models.Model):
    email =models.CharField(max_length=100)
    password =models.CharField(max_length=100)
    mobileno =models.CharField(max_length=100)
    companyname =models.CharField(max_length=100)
    
class Jobinfo(models.Model):
    jobtitle =models.CharField(max_length=100)
    experience =models.CharField(max_length=100)
    jobdescription =models.CharField(max_length=100)
    uploadimage =models.CharField(max_length=100)
    technology =models.CharField(max_length=100)
    postdate =models.CharField(max_length=100)
    duedate =models.CharField(max_length=100)






