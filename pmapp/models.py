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

# 音楽ジャンルテーブル
class Genre(models.Model):
    name = models.CharField('音楽ジャンル名', max_length=50)
    # 音楽ジャンルの英語名をURLに使用
    name_en = models.CharField('音楽ジャンル名英語', max_length=10)
    created_at = models.DateTimeField(auto_now_add = True)
    update_at = models.DateTimeField(auto_now = True)

    def post_count(self):
        n = Post.objects.filter(genre = self).count()
        return n

    def __str__(self):
        return self.name

# タグテーブル
class Tags(models.Model):
    name = models.CharField('Tag名', max_length = 50, blank=True)
    # タグ名の英語名をURLに使用
    name_en = models.CharField('Tag名英語', max_length=10)
    created_at = models.DateTimeField(auto_now_add = True)
    update_at = models.DateTimeField(auto_now = True)

    def post_count(self):
        n = Post.objects.filter(tag = self).count()
        return n

    def __str__(self):
        return self.name

# データベース内のテーブルを定義するファイル
# Postモデルを定義
# Postテーブル
class Post(models.Model):
    # ForeignKey ＝ 外部キー（他のモデルと紐づいていることを意味する）
    # Djangoでは、model Userを定義していなくても元々持っている。
    # on_delete=models.PROTECT  もしUserに紐づいたPostがあればデータベースから削除できない
    author = models.ForeignKey(User, on_delete=models.PROTECT, blank=False)
    # 文字列のField １行の時に使う
    # max_lengthを書かないと必ずエラーになる。
    # 半角全角関係なく50文字まで入るようになっている。
    title = models.CharField('タイトル', max_length = 50, blank=False)
    # TextFieldは複数行　※max_lengthはなくても良い。
    content = models.TextField('内容', max_length = 1000, blank=False)
    # 'Category'はCategoryモデルクラスと紐づいている
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    # 'Genre'はGenreモデルクラスと名前と紐づいている
    genre = models.ForeignKey(Genre, on_delete=models.PROTECT)
    # 'Tags'はTagsモデルクラスと紐づいている
    tag = models.ForeignKey(Tags, on_delete=models.PROTECT, blank=True, null=True)
    # サムネイル
    thumbnail = models.ImageField(upload_to='images/', blank=True)
    # 写真を撮ったスポット
    spot = models.CharField('写真スポット', max_length = 50, blank=True)
    #曲名
    music_title = models.CharField('曲名', max_length = 50, default='', blank=True)
    #アーティスト名
    artist = models.CharField('アーティスト名', max_length = 50, default='', blank=True)
    # 音楽ファイル
    music = models.FileField(upload_to='music/', blank=True)
    # 曲ワンフレーズ どこまでが著作権になるかわからないので文字数は１５文字で制限
    music_phrase = models.CharField('歌詞ワンフレーズ', max_length = 15, blank=True)
    # YouTubeのMVリンクURL
    youtube_url = models.URLField('YouTubeのURL', max_length = 30, blank=True)
    # 日付タイムスタンプ　自動的に今の時間を追加
    created_at = models.DateTimeField(auto_now_add = True)
    # 更新された時に今の時刻を設定
    # 更新された時以外は何も入らない
    update_at = models.DateTimeField(auto_now = True)
    # 更新された時以外は何も入らない
    date_at = models.DateField(auto_now_add = True)

    def like_count(self):
        n = Like.objects.filter(post = self).count()
        return n

    # Postを参照する時にタイトルを使って参照する。
    # strはstring文字列の略
    # self.idの時は__int__
    def __str__(self):
        return self.title

# お気に入り用のモデル
class Like(models.Model):
    # related_name="posted_user"
    post = models.ForeignKey(Post, verbose_name="投稿", on_delete=models.CASCADE)
    post_pk = models.IntegerField(verbose_name="投稿ID", blank=True)
    user = models.ForeignKey(User, verbose_name="Likeしたユーザー", on_delete=models.PROTECT)

#1対多のリレーションを実現するコメントモデル
class Comment(models.Model):
    text = models.TextField('本文')
    target = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='対象記事')