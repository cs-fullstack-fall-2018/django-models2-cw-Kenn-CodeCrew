# from django.shortcuts import render
from .models import Respondent
from django.http import HttpResponse
import random
import string


# Create your views here.

# Function to generate a random name
def get_random_name():
    return (''.join([random.choice(string.ascii_letters + string.digits) for n in range(32)]))


# Function to generate a random age between 18 - 120
def get_random_age():
    return (random.randint(18, 121))


# Function to generate a random salary 0 - 100000
def get_random_salary():
    return (random.randint(0, 100001))


def index(request):
    return HttpResponse("<h1>Welcome to the Census Application!</h1><h4>" + get_random_name() + "</h4><h4>" + str(
        get_random_age()) + "</h4><h4>" + str(get_random_salary()))


def createRes(request):
    newObject = Respondent(respondent_name = get_random_name(), respondent_age = get_random_age(), respondent_income = get_random_salary())
    newObject.save()
    # return HttpResponse(Respondent.objects.all())
    eachName = ""
    counter = 0
    print(Respondent)
    for eachElement in Respondent.objects.all():
        eachName += "Name "+  str(counter) + ": " + eachElement.respondent_name + "<br>"
        counter+=1
    return HttpResponse(eachName)


def readRes(request):
    eachName = ""
    counter = 0
    print(Respondent)
    for eachElement in Respondent.objects.all():
        eachName += "Name "+  str(counter) + ": " + eachElement.respondent_name + "<br>"
        counter+=1
    return HttpResponse(eachName)


def updateRes(request):
    user = Respondent.objects.get(respondent_name = "Kevin")
    print(user.respondent_income)
    user.respondent_income = get_random_salary()
    user.save()
    return HttpResponse(user.respondent_income)


def deleteRes(request):
    deleteThisUser = Respondent.objects.get(respondent_name = "Kenn")

    eachName = "BEFORE<br>"
    counter = 0
    print(Respondent)
    for eachElement in Respondent.objects.all():
        eachName += "Name "+  str(counter) + ": " + eachElement.respondent_name + "<br>"
        counter+=1

    eachName += "<br><br><br>AFTER<br>"

    deleteThisUser.delete()

    counter = 0
    for eachElement in Respondent.objects.all():
        eachName += "Name "+  str(counter) + ": " + eachElement.respondent_name + "<br>"
        counter+=1

    return HttpResponse(eachName)