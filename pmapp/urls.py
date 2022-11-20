from django.urls import path, include
from . import views

# vies.pyと表示のURLを紐づけるファイル

app_name = 'pmapp'

urlpatterns = [
    # これがないと最多尾が表示されない　vies.pyとHTNLの関係が定義されていないから
    # ’’がHTMLを示す
    # views.クラス名(views.pyで定義したもの)
    # as_viewはクラスベースの汎用ビューを使う時に書く。
    path('', views.Index.as_view(), name='index'),
    # 一つ目の引数はURL  nameはリンクを使う時の名称
    path('post_create', views.PostCreate.as_view(), name='post_create'),
    # <int:pk> int・・・整数値　pk・・・primary key 1から順にカウントアップされているID
    path('post_detail/<int:pk>', views.PostDetail.as_view(), name='post_detail'),
    # PostUpdate用
    path('post_update/<int:pk>', views.PostUpdate.as_view(), name='post_update'),
    # Djangoでは削除の場合、一旦確認が入る。　（本当に削除してもよろしいですか？）
    path('post_delete/<int:pk>', views.PostDelete.as_view(), name='post_delete'),
    # PostList用
    path('post_list', views.PostList.as_view(), name='post_list'),
    # Login用
    path('login', views.Login.as_view(), name='login'),
    # Login用
    path('logout', views.Logout.as_view(), name='logout'),
    # SignUp用
    path('signup', views.SignUp.as_view(), name='signup'),
    # Like  defで作った関数は、as_view()なくていい  like_addのURLが呼び出された時に
    # vies.pyのLike_addが動き出す  ex)like/6
    path('like/<int:post_id>', views.Like_add, name='like_add'),
    # カテゴリー
    path('category_list', views.CategoryList.as_view(), name='category_list'),
    # カテゴリー詳細ページ  ex)category_detail/news
    path('category_detail/<str:name_en>', views.CategoryDetail.as_view(), name='category_detail'),
    path('search', views.Search, name='search'),
]
