from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from .serializer import ProductSerializer, CartSerializer, UserSerializer
from .models import Product, Cart
from django.contrib.auth.models import User
from django.contrib.auth import login as django_login,authenticate
from rest_framework.permissions import IsAuthenticated
from rest_framework import status


# Create your views here.
@api_view(['POST'])
def add_product(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Product added successfully", "product": serializer.data})
    else:
        return Response({"errors": "Invalid data", "details": serializer.errors})


@api_view(['GET'])
def view_product(request):
    product = Product.objects.all()
    serializer = ProductSerializer(product, many=True)
    return Response({"products": serializer.data})


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_cart(request):
    user = request.user
    product_id = request.data.get('product_id')
    quantity = request.data.get('quantity', 1)

    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)

    cart_item, created = Cart.objects.get_or_create(user=user, product=product)

    if not created:
        cart_item.quantity += quantity
        cart_item.save()

    return Response({"message": "Product added to cart"}, status=status.HTTP_201_CREATED)


@api_view(['POST'])
def register(request):
    username = request.data.get("username")
    email = request.data.get('email')
    password = request.data.get('password')
    if User.objects.filter(username=username).exists():
        return Response({"error": "Username already exists"})
    else:
        User.objects.create_user(username=username, email=email, password=password)
        return Response({"message": "Successfully Registered"})


@api_view(['GET'])
def view_users(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        django_login(request, user)
        return Response({"messages": "Successfully logged in"})
    else:
        return Response({"error": "Invalid username or password"})


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def view_cart(request):
    user = request.user
    cart_items = Cart.objects.filter(user=user)

    if not cart_items:
        return Response({"message": "No items in your cart."}, status=status.HTTP_404_NOT_FOUND)

    total_price = 0
    for item in cart_items:
        total_price += item.product.price * item.quantity

    cart_items_data = CartSerializer(cart_items, many=True)

    return Response({
        "cart_items": cart_items_data.data,
        "total_price": total_price
    }, status=status.HTTP_200_OK)
