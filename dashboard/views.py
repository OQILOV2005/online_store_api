from main.models import Order, Product
from main.serializers import *
from rest_framework.decorators import api_view
from  rest_framework.response import Response


@api_view(['POST'])
def create_product(request):
    if request.method == "POST":
        name = request.POST.get('name')
        photo = request.POST.getlist('photo')
        price = request.POST.get('price')
        barnd = request.POST.get('barnd')
        sub_category = request.POST.get('sub_category')
        quantity = request.POST.get('quantity')
        is_active = request.POST.get('is_active')
        is_sale = request.POST.get('is_sale')
        sale = request.POST.get('sale')
        description = request.POST.get('description')
        addition = request.POST.get('addition')
        tags = request.POST.getlist('tags')
        is_credit = request.POST.get('is_credit')
        rating = request.POST.get('rating')
        like_number = request.POST.get('like_number')
        status_size = request.POST.get('status_size')
        new_poduct = Product.objects.create(
            name=name,
            price=price,
            barnd_id=barnd,
            sub_category_id=sub_category,
            quantity=quantity,
            is_active=is_active,
            is_sale=is_sale,
            sale=sale,
            description=description,
            addition=addition,
            is_credit=is_credit,
            rating=rating,
            like_number=like_number,
            status_size=status_size,
        )
        for i in tags:
            new_poduct.tags.add(i)
            new_poduct.save()
        for i in photo:
            img = ProductImage.objects.create(
                image = i
            )
            new_poduct.photo.add(img)
            new_poduct.save()
        ser = ProductSerializers(new_poduct)
        return Response(ser.data)




@api_view(['PUT'])
def update_product(request, pk):
    product = Product.objects.get(pk=pk)
    name = request.POST.get('name')
    photo = request.FILES.getlist('photo')
    price = request.POST.get('price')
    barnd = request.POST.get('barnd')
    sub_category = request.POST.get('sub_category')
    quantity = request.POST.get('quantity')
    is_active = request.POST.get('is_active')
    is_sale = request.POST.get('is_sale')
    sale = request.POST.get('sale')
    description = request.POST.get('description')
    addition = request.POST.get('addition')
    tags = request.POST.getlist('tags')
    is_credit = request.POST.get('is_credit')
    rating = request.POST.get('rating')
    like_number = request.POST.get('like_number')
    status_size = request.POST.get('status_size')
    product.product=product
    product.name=name
    product.price=price
    product.barnd=barnd
    product.sub_category=sub_category
    product.quantity=quantity
    product.is_active=is_active
    product.is_sale=is_sale
    product.sale=sale
    product.description=description
    product.addition=addition
    product.tags=tags
    product.is_credit=is_credit
    product.rating=rating
    product.like_number=like_number
    product.status_size=status_size
    if photo is not None:
        for i in photo:
            photo = ProductImage.objects.create(
                image = i
            )
            product.photo.add(photo)
    product.save()
    ser=ProductSerializers(product)
    return Response(ser.data)




@api_view(['POST'])
def create_order(request):
    user = request.user
    user= request.POST.get('user')
    phone= request.POST.get('phone')
    quantity = request.POST.get('quantity')
    address= request.POST.get('address')
    is_delivery= request.POST.get('is_delivery')
    total_price= request.POST.get('total_price')
    is_credit= request.POST.get('is_credit')
    period= request.POST.get('period')
    cards = Card.objects.get(user=user)
    total_price=0
    for i in cards:
        if i.product.quantity >= quantity:
            total_price += i.product.price * quantity
            new_order = Order.objects.create(
                user=user,
                phone=phone,
                address=address,
                quantity=quantity,
                is_delivery=is_delivery,
                total_price=total_price,
                is_credit=is_credit,
                period=period,
            )
            for i in cards:
                new_order.produc.add(i.product)
                new_order.save()
            ser = OrderSerializers(new_order)
            return Response(ser.data)




@api_view(["DELETE"])
def delete_product(request, pk):
    product = Product.objects.get(pk=pk)
    product.delete()
    return Response({'message' : "Deleted"})


@api_view(["DELETE"])
def delete_product(request, pk):
    order = Order.objects.get(pk=pk)
    order.delete()
    return Response({'message' : "Deleted"})













