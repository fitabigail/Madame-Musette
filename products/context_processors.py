from .models import Category


def categories_sort(request):
    list = Category.objects.all()
    return dict(list=list)
