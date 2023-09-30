from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *


@api_view(['GET'])
def get_all_products(request):
    products = Product.objects.all()
    ser = ProductSerializers(products, many=True)
    return Response(ser.data)


@api_view(["GET"])
def get_subcategories_by_category(request, pk):
    category = Category.objects.get(pk=pk)
    subcategories = Sub_Category.objects.filter(category=category)
    ser = Sub_CategorySerializers(subcategories, many=True)
    return Response(ser.data)


@api_view(["GET"])
def get_product_by_subcategory(request, pk):
    sub_category = Sub_Category.objects.get(pk=pk)
    products = Product.objects.filter(sub_category=sub_category)
    ser = ProductSerializers(products, many=True)
    return Response(ser.data)


@api_view(['GET'])
def filter_products_by_name(request):
    name = request.GET.get('name')
    products = Product.objects.filter(name__icontains=name)
    ser = ProductSerializers(products, many=True)
    return Response(ser.data)


@api_view(['GET'])
def search_brand_by_name(request):
    name = request.GET.get('name')
    brands = Brand.objects.filter(name__icontains=name)
    ser = BrandSerializers(brands, many=True)
    return Response(ser.data)


@api_view(['GET'])
def get_products_by_sale(request):
    products = Product.objects.filter(is_sale=True)
    ser = ProductSerializers(products, many=True)
    return Response(ser.data)



@api_view(['POST'])
def add_product_card(request, pk):
    product = Product.objects.get(pk=pk)
    card = Card.objects.create(
        user=request.user,
        products=product
    )
    ser = CardSerializers(card)
    return Response(ser.data)


@api_view(['POST'])
def add_saved_product(request, pk):
    product = Product.objects.get(pk=pk)

    saved_product = Saved.objects.create(
        user=request.user,
        product=product
    )
    ser = SavedSerializers(saved_product)
    return Response(ser.data)


@api_view(['POST'])
def create_comment(request, pk):
    product = Product.objects.get(pk=pk)
    if request.method == "POST":
        text = request.POST['text']
        comment = Comment.objects.create(
            text=text,
            user=request.user,
            product=product
        )
        ser = ProductSerializers(comment)
        return Response(ser.data)



@api_view(['POST'])
def reply_comment(request, pk):
    product = Product.objects.get(pk=pk)
    comment_id = request.POST.get('comment_id')
    text = request.POST['text']
    user = request.user
    new_comment = Comment.objects.create(
        user=user,
        product_id=product,
        text=text,
        comment_id=comment_id,
    )
    ser = CommentSerializers(new_comment)
    return Response(ser.data)




@api_view(['PUT'])
def update_products_like(request, pk):
    product = Product.objects.get(pk=pk)
    product.like_number += 1
    product.save()
    ser = ProductSerializers(product)
    return Response(ser.data)

















