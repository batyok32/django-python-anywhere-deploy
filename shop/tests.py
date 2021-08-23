from django.test import TestCase

# Create your tests here.
# @api_view(['GET', "POST"])
# def comments_list(request, pk):
#     try:
#         product = Product.objects.get(id=pk)
#     except Product.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#     if request.method == 'GET':
#         comments = Comment.objects.filter(product=product).order_by('created')
#         serializer = CommentSerializer(
#             comments, context={'request': request}, many=True)
#         return Response({"data": serializer.data})

#     elif request.method == "POST":
#         if request.user.is_authenticated():
#             request.data['user'] = request.user
#             serializer = CommentSerializer(data=request.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(status=status.HTTP_201_CREATED)
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#         return Response({"Error": "NO"})

# {
#     "body": "Thi sis",
#     "product":"3"
# }


# @api_view(['GET'])
# def product_list(request,category=None, filter_word=None):
#     """
#     List  products.
#     """
#     prev="http://127.0.0.1:8000/api/v1/products"

#     products = Product.objects.filter(available=True)
#     # FIlter by category if category
#     if category:
#         choosen_category=Category.objects.filter(name=category)
#         prev=f"{prev}/{category}"
#         if not choosen_category:
#             return Response({"error":"No category"}, status=status.HTTP_404_NOT_FOUND)
#         products = products.filter(category__in=choosen_category)

#     # Filtering
#     if filter_word in filter_list:
#         filter_w = filter_list[filter_word]
#         if category:
#             prev = f"{prev}/{filter_word}"
#         else:
#             prev = f"{prev}/filter/{filter_word}"
#         products = products.order_by(f"{filter_w}")

#     # Paginating
#     result = Paginate(request=request).get_data(queryset=products)
#     serializer = ProductSerializer(result['data'], many=True, context={'request': request})
#     # filter = ProductFilter(request.GET, queryset=Product.objects.all())
#     return Response({'data': serializer.data ,
#         'count': result['count'],
#         'numpages' : result['numpages'],
#         'nextlink': f'{prev}/?page=' + str(result['nextPage']),
#         'prevlink': f'{prev}/?page=' + str(result['previousPage'])
#     })

