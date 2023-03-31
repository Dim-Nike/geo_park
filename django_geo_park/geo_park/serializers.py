from .models import *
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']


class GeneralUserSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = GeneralUser
        fields = '__all__'


class CreateGeneralUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeneralUser
        fields = '__all__'


class SubUserSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    subscription_fields = serializers.CharField(source='get_subscription_display')

    class Meta:
        model = SubUser
        fields = '__all__'


class CreateSubUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubUser
        fields = '__all__'


class EditImageSerializer(serializers.ModelSerializer):
    user_general = GeneralUserSerializer()
    user_sub = SubUserSerializer()

    class Meta:
        model = EditImage
        fields = '__all__'


class CreateEditImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = EditImage
        fields = '__all__'


class CreateCategoriesNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriesNews
        fields = '__all__'


class NewsSerializer(serializers.ModelSerializer):
    categories = CreateCategoriesNewsSerializer()

    class Meta:
        model = News
        fields = '__all__'


class CreateNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'





