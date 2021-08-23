from rest_framework.pagination import LimitOffsetPagination

# Custom pagination class
class MyOffsetPagination(LimitOffsetPagination):
    default_limit = 20
    max_limit = 1000
