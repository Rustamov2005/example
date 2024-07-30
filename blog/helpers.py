

class Paginator():
    @staticmethod
    def page_pagination(queryset: list, page: int, page_size: int):
        return queryset[page_size*(page-1):page_size * page]
