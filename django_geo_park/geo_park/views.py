# from ..ML_model.ml_model import ml
from .serializers import *
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
import os

from ultralytics import YOLO
from PIL import Image
import cv2
from keras.models import load_model


def ml(img_path):
    cur_dir = os.path.dirname(os.path.abspath(__file__))
    path_model = '{}/best.pt'.format(cur_dir)
    path_img = img_path
    model = YOLO(path_model)
    im1 = Image.open(path_img)
    result = model.predict(source=im1, save=True, name=img_path[28:])
    print(result)
    return result




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
        query = EditImage.objects.all()

        if self.action == 'list' or self.action == 'retrieve':
            return EditImageSerializer

        elif self.action == 'create' or self.action == 'update' or self.action == 'destroy':
            return CreateEditImageSerializer


class ProcessingEditImage(viewsets.ModelViewSet):
    queryset = EditImage.objects.all()

    def get_serializer_class(self):
        if self.action == 'retrieve':
            obj = self.get_object()
            if obj.user_general:
                obj.user_general.is_active -= 1
                obj.user_general.save()
                print(obj.user_general.is_active)
            else:
                obj.user_sub.is_active -= 1
                obj.user_sub.save()

            desc = ml(img_path=f'{obj.image_user}')
            obj.image_neural = f'runs/detect/{str(obj.image_user)[28:]}/{str(obj.image_user)[28:]}'
            obj.desc = desc
            obj.is_done = True
            obj.save()
            return CreateEditImageSerializer

        if self.action == 'update':
            model = self.get_object()
            print(model.user_sub)
            return CreateEditImageSerializer


class ProcessingImage(APIView):
    queryset = EditImage.objects.all()

    def post(self, req):
        serializer = UpdateImageSerializer(data=req.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'post': serializer.data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method PUT not allowed"})

        try:
            instance = EditImage.objects.get(pk=pk)
        except:
            return Response({"error": "Object does not exists"})

        serializer = EditImageSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({"post": serializer.data})


class UpdateTestModel(APIView):

    def post(self, req):
        serializer = UpdateTestModelSerializer(data=req.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'post': serializer.data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method PUT not allowed"})

        try:
            instance = TestModel.objects.get(pk=pk)
        except:
            return Response({"error": "Object does not exists"})

        serializer = UpdateTestModelSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        TestModel.objects.create(name='newName', is_active=True)

        return Response({"post": serializer.data})


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


