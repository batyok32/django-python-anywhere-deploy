# Models
from .models import Order, OrderItem
from shop.models import Coupon, Product, Size
from authentication.models import UserAccount
# Filters
from rest_framework.filters import  OrderingFilter

# Serializers
from .serializers import OrderSerializer, OrderItemSerializer, SecondOrderItemSerializer


# RESTFRAMEWORK stuff
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

# Pagination
from shop.views import MyOffsetPagination

# List and create orders
class OrderListCreateView(generics.ListCreateAPIView):
    """
    Creating Order and Order Items
    """
    pagination_class = MyOffsetPagination
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class=OrderSerializer
    filter_backends = (OrderingFilter,)
    ordering_fields = ['id', 'created', 'total_shop', 'city']

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user, is_active=True)

    def post(self, request, *args, **kwargs):
        order=None
        if (not request.data['cartItems'] or len(request.data['cartItems']) < 1):
            return Response("No Cart Items", status.HTTP_404_NOT_FOUND)
        cart_items = request.data['cartItems']
        # Initialize serializer and validate
        serializer = OrderSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        # Trying to get field
        code = request.data.get('code', None)
        if code:
            try:
                coupon = Coupon.objects.get(code=code)
                order = serializer.save(user=request.user, coupon=coupon, discount=coupon.discount)
            except:
                return Response("Coupon is not valid", status=status.HTTP_404_NOT_FOUND)
        else:
            order = serializer.save(user=request.user)
        # Saving serializer
        
        # Another serializer
        for item in cart_items: 
            print("TRYING TO ORDER")
            product = Product.objects.get(id=item['product_id'])
            quantity = item['product_quantity']
            size_id = item['size']
            size = Size.objects.get(id=size_id)
            size.amount -= quantity
            total = product.new_price * int(quantity)
            product.sold += quantity
            product.amount -= quantity
            size.save()
            product.save()
            orderItem = OrderItemSerializer(data={"size":size.size_name,"price": total, "quantity":quantity})
            orderItem.is_valid(raise_exception=True)
            print("EVERYTHING IS GOOD OrderItem", orderItem)
            print("EVERYTHING IS GOOD SIze >>>", size)
            print("EVERYTHING IS GOOD SIze NAme >>>", size.size_name)
            print("EVERYTHING IS GOOD Product >>>", product)
            orderItem.save(order=order, product=product)
        order.save()
        # Response
        return Response(serializer.data, status=status.HTTP_201_CREATED)

# Making not valid order
class OrderDeleteView(APIView):
    """
    'Delete' Order
    """
    permission_classes = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs):
        orders = request.data.get('orders', None)
        # Loop and delete orders
        if orders:
            try:
                for order in orders:
                    choosedOrder=Order.objects.get(id=order, user=request.user)
                    choosedOrder.is_active = False
                    choosedOrder.save()
            except:
                return Response('Error 404', status=status.HTTP_404_NOT_FOUND)
    
        # Response
        return Response("Everything Ok", status=status.HTTP_200_OK)


class OrderProducts(APIView):
    # permission_classes = (permissions.IsAuthenticated,)

    def get_order(self, request, *args, **kwargs):
        try:
            pk = self.kwargs['pk']
            user = UserAccount.objects.get(username='admin')
            order = Order.objects.get(id=pk, user=user, is_active=True)
            return order
        except:
            return Response("Not Found", status=status.HTTP_404_NOT_FOUND)


    def get(self, request, *args, **kwargs):
        order = self.get_order(request)
        orderItems = OrderItem.objects.filter(order=order)
        serializer = SecondOrderItemSerializer(orderItems, many=True, context={'request':request})
        # print("Response", serializer.data)
        return Response(serializer.data, status=status.HTTP_200_OK)