from distutils.command.upload import upload
from ftplib import MAXLINE
from django.db import models
from django.contrib.auth.models import User

# カテゴリーテーブル
class Category(models.Model):
    name = models.CharField('カテゴリー名', max_length=50)
    # カテゴリーの英語名をURLに使用
    name_en = models.CharField('カテゴリー名英語', max_length=10)
    created_at = models.DateTimeField(auto_now_add = True)
    update_at = models.DateTimeField(auto_now = True)

    def post_count(self):
        n = Post.objects.filter(category = self).count()
        return n

    def __str__(self):
        return self.name

# データベース内のテーブルを定義するファイル
# Postモデルを定義
# Postはテーブル
class Post(models.Model):
    # ForeignKey ＝　　外部キー（他のモデルと紐づいていることを意味する）
    # Djangoでは、model Userを定義していなくても元々持っている。
    # on_delete=models.PROTECT  もしUserに紐づいたPostがあればデータベースから削除できない
    author = models.ForeignKey(User, on_delete=models.PROTECT, blank=False) 
    # 文字列のField　　１行の時に使う
    # max_lengthを書かないと必ずエラーになる。
    # 半角全角関係なく50文字まで入るようになっている。
    title = models.CharField('タイトル', max_length = 50)
    # TextFieldは複数行　※max_lengthはなくても良い。
    content = models.TextField('内容', max_length = 1000)
    # 'Category'はCategoryモデルの名前と紐づいている
    category = models.ForeignKey('Category', on_delete=models.PROTECT)
    # サムネイル
    thumbnail = models.ImageField(upload_to='images/', blank=True)
    # 日付タイムスタンプ　自動的に今の時間を追加
    # 更新された時は何も入らない
    created_at = models.DateTimeField(auto_now_add = True)
    # 更新された時に今の時刻を設定
    update_at = models.DateTimeField(auto_now = True)

# Postを参照する時にタイトルを使って参照する。
# strはstring文字列の略
# self.idの時は__int__
    def __str__(self):
        return self.title

# お気に入り用のモデル
class Like(models.Model):
    post = models.ForeignKey(Post, verbose_name="投稿", on_delete=models.PROTECT)
    user = models.ForeignKey(User, verbose_name="Likeしたユーザー", on_delete=models.PROTECT)