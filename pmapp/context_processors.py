from .models import Category

def all_category(request):
    category_list = Category.objects.all()

    params = {
        # context_proccersを読み込んだら必ず取得できる。
        'category_list': category_list,
    }

    return params