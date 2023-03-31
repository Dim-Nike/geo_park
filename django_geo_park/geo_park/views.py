from django.shortcuts import render
from .serializers import *
from rest_framework import viewsets, generics
from rest_framework.response import Response


class GeneralUserCreateUpdateListRetrieveDeleteView(viewsets.ModelViewSet):
    queryset = GeneralUser.objects.all()

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return GeneralUserSerializer
        elif self.action == 'create' or self.action == 'update' or self.action == 'destroy':
            return CreateGeneralUserSerializer


class SubUserCreateUpdateListRetrieveDeleteView(viewsets.ModelViewSet):
    queryset = SubUser.objects.all()

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return SubUserSerializer
        elif self.action == 'create' or self.action == 'update' or self.action == 'destroy':
            return CreateSubUserSerializer


class EditImageCreateUpdateListRetrieveDeleteView(viewsets.ModelViewSet):
    queryset = EditImage.objects.all()

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return EditImageSerializer
        elif self.action == 'create' or self.action == 'update' or self.action == 'destroy':
            return CreateEditImageSerializer


class CategoriesNewsCreateUpdateListRetrieveDeleteView(viewsets.ModelViewSet):
    queryset = CategoriesNews.objects.all()
    serializer_class = CreateCategoriesNewsSerializer


class NewsCreateUpdateListRetrieveDeleteView(viewsets.ModelViewSet):
    queryset = News.objects.all()

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return NewsSerializer
        elif self.action == 'create' or self.action == 'update' or self.action == 'destroy':
            return CreateNewsSerializer

