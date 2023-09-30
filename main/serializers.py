from rest_framework import serializers
from .models import *


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        depth = 2
        model = Product
        fields = "__all__"


class BrandSerializers(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = "__all__"



class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class Sub_CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Sub_Category
        fields = "__all__"


class SavedSerializers(serializers.ModelSerializer):
    class Meta:
        model = Saved
        fields = "__all__"


class CommentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"


class OrderSerializers(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"


class TagSerializers(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"


class CommentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"


class ProductImageSerializers(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = "__all__"


class RegionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = "__all__"


class CardSerializers(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = "__all__"


