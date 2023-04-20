from .views import *
from django.urls import path

urlpatterns = [
    path('generalUser/all', GeneralUserCreateUpdateListRetrieveDeleteView.as_view({'get': 'list'}),
         name='generalUserList'),
    path('generalUser/retrieve/<int:pk>', GeneralUserCreateUpdateListRetrieveDeleteView.as_view({'get': 'retrieve'}),
         name='generalUserRetrieve'),
    path('generalUser/update/<int:pk>', GeneralUserCreateUpdateListRetrieveDeleteView.as_view({'put': 'update'}),
         name='generalUserUpdate'),
    path('generalUser/create', GeneralUserCreateUpdateListRetrieveDeleteView.as_view({'post': 'create'}),
         name='generalUserCreate'),
    path('generalUser/delete/<int:pk>', GeneralUserCreateUpdateListRetrieveDeleteView.as_view({'delete': 'destroy'}),
         name='generalUserDestroy'),


    path('subUser/all', SubUserCreateUpdateListRetrieveDeleteView.as_view({'get': 'list'}),
         name='subUserList'),
    path('subUser/retrieve/<int:pk>', SubUserCreateUpdateListRetrieveDeleteView.as_view({'get': 'retrieve'}),
         name='subUserRetrieve'),
    path('subUser/update/<int:pk>', SubUserCreateUpdateListRetrieveDeleteView.as_view({'put': 'update'}),
         name='subUserUpdate'),
    path('subUser/create', SubUserCreateUpdateListRetrieveDeleteView.as_view({'post': 'create'}),
         name='subUserCreate'),
    path('subUser/delete/<int:pk>', SubUserCreateUpdateListRetrieveDeleteView.as_view({'delete': 'destroy'}),
         name='subUserDestroy'),


    path('editImage/all', EditImageCreateUpdateListRetrieveDeleteView.as_view({'get': 'list'}),
         name='editImageList'),
    path('editImage/retrieve/<int:pk>', EditImageCreateUpdateListRetrieveDeleteView.as_view({'get': 'retrieve'}),
         name='editImageRetrieve'),
    path('editImage/update/<int:pk>', EditImageCreateUpdateListRetrieveDeleteView.as_view({'put': 'update'}),
         name='editImageUpdate'),
    path('editImage/create', EditImageCreateUpdateListRetrieveDeleteView.as_view({'post': 'create'}),
         name='editImageCreate'),
    path('editImage/delete/<int:pk>', EditImageCreateUpdateListRetrieveDeleteView.as_view({'delete': 'destroy'}),
         name='editImageDestroy'),
    path('editImage/processingImage/<int:pk>', ProcessingEditImage.as_view({'get': 'retrieve'}),
         name='editImageProcessing'),
    path('editImage/put/<int:pk>', ProcessingImage.as_view(), name='editImagePut'),


    path('categoriesNews/all', CategoriesNewsCreateUpdateListRetrieveDeleteView.as_view({'get': 'list'}),
         name='categoriesNewsList'),
    path('categoriesNews/retrieve/<int:pk>', CategoriesNewsCreateUpdateListRetrieveDeleteView.as_view({'get': 'retrieve'}),
         name='categoriesNewsRetrieve'),
    path('categoriesNews/update/<int:pk>', CategoriesNewsCreateUpdateListRetrieveDeleteView.as_view({'put': 'update'}),
         name='categoriesNewsUpdate'),
    path('categoriesNews/create', CategoriesNewsCreateUpdateListRetrieveDeleteView.as_view({'post': 'create'}),
         name='categoriesNewsCreate'),
    path('categoriesNews/delete/<int:pk>', CategoriesNewsCreateUpdateListRetrieveDeleteView.as_view({'delete': 'destroy'}),
         name='categoriesNewsDestroy'),


    path('news/all', NewsCreateUpdateListRetrieveDeleteView.as_view({'get': 'list'}),
         name='newsList'),
    path('news/retrieve/<int:pk>', NewsCreateUpdateListRetrieveDeleteView.as_view({'get': 'retrieve'}),
         name='newsRetrieve'),
    path('news/update/<int:pk>', NewsCreateUpdateListRetrieveDeleteView.as_view({'put': 'update'}),
         name='newsUpdate'),
    path('news/create', NewsCreateUpdateListRetrieveDeleteView.as_view({'post': 'create'}),
         name='newsCreate'),
    path('news/delete/<int:pk>', NewsCreateUpdateListRetrieveDeleteView.as_view({'delete': 'destroy'}),
         name='newsDestroy'),

    path('testModel/update/<int:pk>', UpdateTestModel.as_view(), name='TestModelUpdate'),

    path('testImage', TestViews.as_view({'post': 'create'}), name='TestView')

]