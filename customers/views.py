from django.shortcuts import render
from rest_framework import viewsets
from customers.models import Customer


class CustomerViewSet(viewsets.ModelViewSet):
    ...
