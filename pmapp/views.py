from ast import Delete
from re import template
from django.shortcuts import render, resolve_url, redirect
from django.http import HttpResponse, HttpResponseRedirect
# Djangoで準備されているViewをインポート
from django.views.generic import TemplateView, CreateView, DetailView, UpdateView, DeleteView, ListView
from .models import Post, Like, Category
from django.urls import reverse_lazy
from .forms import PostForm, LoginForm, SignUpForm, SearchForm
# Djangoが用意したライブラリmessages
from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.db.models import Q  #QはOR条件
from django.core.paginator import Paginator

# UserPassesTestMixinを継承してオリジナルのクラスを作成
class OnlyMyPostMixin(UserPassesTestMixin):
    # 例外処理を行うかどうか = True
    # 判定はUser
    raise_exception = True

    def test_func(self):
        # 今開いている記事をpostに入れる
        post = Post.objects.get(id = self.kwargs['pk'])
        # その開いている記事を作った人が今ログインしている人かどうかの判別
        return post.author == self.request.user


#Djangoは大文字と小文字を区別
#defではなくclass
# views.pyで作ったクラス名はurls.pyでも使うのでクラス名に注意！
# クラスベース汎用ビュー 他にCreateView（作成）, UpdateView（更新）, DetailView（削除）, ListView（一覧）がある。
class Index(TemplateView):
    # templatesフォルダにあるHTMLを指定。
    template_name = 'pmapp/index.html'

    # テンプレートに辞書を渡すメソッド
    # argsはなくても良い。
    def get_context_data(self, *args, **kwargs):
        # 自分の内容をそのままcontextとして取得
        # 一旦TemplateViewの中で記述するのが決まり事
        # 継承元のメソッドを呼び出すおまじない
        context = super().get_context_data(**kwargs)
        # postというテーブルの中から全て取得
        # Post.objects  テーブル名.objectsは決まり事
        post_list = Post.objects.all().order_by('-created_at')
        # 辞書　key： value
        context = {
            'post_list': post_list,
        }
        # HTMLに渡すパラメータ
        return context
# Djangoが標準で用意しているクラスベースビューを使えばCRUDは簡単に実装できる

# それぞれのViewが持つ機能を引き継ぐ（継承）ので、記述がシンプルになる
# ログイン時のみ作成できるようにする
# 　→ ログインしていないと、新規投稿ボタンを押してもログイン画面に飛ばされる（　LoginRequiredMixinにより実装　＊クラスベースビュー）
# 注意！　 LoginRequiredMixinは、 CreateViewよりも前に書く。　Mixinというのは多重継承
class PostCreate(LoginRequiredMixin, CreateView):
    # Postのモデルを作る
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('pmapp:index')

    # formの内容が正しい時　（タイトルに何も入っていない場合などはエラー）
    def form_valid(self, form):
        # ログイン中のユーザーをセットするための記述
        form.instance.author_id = self.request.user.id
        # PostCreateの内容を上書き formそのものを返す記述
        return super(PostCreate, self).form_valid(form)

    #Postを作成できたら、メッセージを表示
    def get_success_url(self):
        messages.success(self.request, 'Postを登録しました。')
        return resolve_url('pmapp:index')

# 投稿詳細
class PostDetail(DetailView):
    # 取得した内容はHTMLでobjectとして渡される。　（Django では、DetailViewを使った場合このような処理になる）
    model = Post

    def get_context_data(self, *args, **kwargs):
        # 自分自身のデータを取得  一つ以上必ずデータを取得
        detail_data = Post.objects.get(id = self.kwargs['pk'])
        # 同じカテゴリに属する記事をとってくる処理  最新５件だけとってくる
        # Postの中にcategoryは存在する。detail_data.category
        category_posts = Post.objects.filter(category = detail_data.category).order_by('-created_at')[:5]
        params = {
            'object': detail_data,  #Post
            'category_posts': category_posts,
        }
        return params


# 更新
class PostUpdate(OnlyMyPostMixin, UpdateView):
    # テーブル名
    model = Post
    # forms.pyで書いたクラス名
    form_class = PostForm

    # 更新ボタンを押した後の処理
    def get_success_url(self):
        # ここでメッセージの色を変えることができる。　infoが青
        messages.info(self.request, 'Postを更新しました。')
        # 更新した後に遷移するURL
        return resolve_url('pmapp:post_detail', pk=self.kwargs['pk'])

# 削除
# DeleteView Django特有の機能　Djangoのメリット　簡単に記述できる
# 本当に削除しますか？　という確認画面を作ってくれる
class PostDelete(OnlyMyPostMixin, DeleteView):
    model = Post

    # 削除ボタンを押した後の処理
    def get_success_url(self):
        # infoはbootstrapと連動
        messages.info(self.request, 'Postを削除しました。')
        # 削除した後に遷移するURL
        return resolve_url('pmapp:index')

# 投稿一覧クラス
class PostList(ListView):
    model = Post
    paginate_by = 5

# Djangoが用意してくれている関数
    def get_queryset(self):
        return Post.objects.all().order_by('-created_at')

class Login(LoginView):
    form_class = LoginForm
    # ログイン画面指定
    template_name = 'pmapp/login.html'

class Logout(LogoutView):
    template_name = 'pmapp/logout.html'

# Userを作るためCreateViewを使う
class SignUp(CreateView):
    form_class = SignUpForm
    template_name = 'pmapp/signup.html'
    success_url = reverse_lazy('pmapp:index')

    # formの内容にエラーがない場合に実行
    def form_valid(self, form):
        # formの内容を保存
        user = form.save()
        # 上で作ったユーザーを使ってログイン
        login(self.request, user)
        self.object = user
        messages.info(self.request, 'ユーザー登録をしました。')
        return HttpResponseRedirect(self.get_success_url())

@login_required   
def Like_add(request, post_id):
    # クラスベースでは、勝手にこのidを取ってきてくれるが、関数ベースなので明示する必要あり
    post = Post.objects.get(id = post_id)
    # お気に入り登録した投稿の数をカウント  filterの中に抽出条件を入れる
    is_liked = Like.objects.filter(user = request.user, post = post_id).count()
    # １回でもお気に入りに追加していたら追加済みメッセージを表示
    if is_liked > 0:
        messages.info(request, 'すでにお気に入りに追加済みです。')
        # ページ遷移先
        return redirect ('pmapp:post_detail', post_id)

    like = Like()
    # request.userはログイン中のユーザー
    like.user = request.user
    like.post = post
    like.save()  #Likeにデータ保存

    messages.success(request, 'お気に入りに追加しました!')
    # 詳細ページでは、post.idを記載しないと、どの投稿の詳細ページかわからなくなるのでid指定
    return redirect('pmapp:post_detail', post.id)

# カテゴリ一覧クラス
class CategoryList(ListView):
    model = Category

# カテゴリ詳細ページ
class CategoryDetail(DetailView):
    model = Category
    # この二つを記述しないとURLにすることはできない
    slug_field = 'name_en'
    slug_url_kwarg = 'name_en'

    def get_context_data(self, *args, **kwargs):
        detail_data = Category.objects.get(name_en = self.kwargs['name_en'])
        category_posts = Post.objects.filter(category = detail_data.id).order_by('-created_at')

        params = {
            'object': detail_data,
            'category_posts': category_posts,
        }

        return params

# 検索関数
def Search(request):
    if request.method == 'POST':
        # freewordという空の箱を持った変数
        searchform = SearchForm(request.POST)

        if searchform.is_valid():
            # cleaned_data → エラーがないかチェック済みのデータ
            freeword = searchform.cleaned_data['freeword']
            #QはOR条件　　A OR B （　Q()｜Q ()）
            # title または contentsにfreewordがはいっているかどうか
            search_list = Post.objects.filter(Q(title__icontains = freeword) |Q(content__icontains = freeword))

        params = {
            # Search.HTMLに渡す
            'search_list': search_list,
        }

        return render (request, 'pmapp/search.html', params)