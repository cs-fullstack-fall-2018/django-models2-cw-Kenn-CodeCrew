from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
import random
import string


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
