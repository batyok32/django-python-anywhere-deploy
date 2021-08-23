from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

class Paginate(object):
    def __init__(self, request):
        self.request = request

    def get_data(self, queryset):
        data = []
        nextPage = 1
        previousPage = 1
        page = self.request.GET.get('page', 1)
        paginator = Paginator(queryset, 1)
        try:
            data = paginator.page(page)
        except PageNotAnInteger:
            data = paginator.page(1)
        except EmptyPage:
            data = paginator.page(paginator.num_pages)
        if data.has_next():
            nextPage = data.next_page_number()
        if data.has_previous():
            previousPage = data.previous_page_number()
        count = paginator.count
        numpages = paginator.num_pages
        result = {
            "data":data, 
            "nextPage":nextPage, 
            "previousPage":previousPage,
            'numpages' : numpages,
            'count':count
        }
        # result = [
        #     data, 
        #     nextPage, 
        #     previousPage,
        #     numpages,
        #     count
        # ]
        return result
