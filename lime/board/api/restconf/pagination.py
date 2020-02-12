from rest_framework.pagination import PageNumberPagination

class BoardAPIPaginator(PageNumberPagination):
	page_size = 10