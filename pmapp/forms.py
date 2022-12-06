from django import forms
from .models import Post, Tags, Comment
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
# UserはあらかじめDjangoが準備している
from django.contrib.auth.models import User
# 登録フォームを定義するファイル

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        # forms.pyでは、HTML側で入力可能にする項目を指定する。
        fields = ('title', 'content', 'category', 'genre', 'tag', 'thumbnail', 'spot', 'music_title', 'artist', 'music', 'music_phrase', 'youtube_url')

# 継承
# bootstrapのCSSをpost_form.htmlのformのレイアウトに対して適用されるように設定
# このクラスが呼び出された時に最初に実行される処理
    def __init__(self, *args, **kwargs):
        # super　継承
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            # 各fieldに対してform-controlというクラスを与える
            # 定型文のようなもの
            # fieldのすべてのclass属性に'form-control'と指定したい場合
            field.widget.attrs['class'] = 'form-control'

# ログインフォーム
class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

# サインアップフォーム UserCreationFormはDjangoが持っているもの
class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        # password2 確認用パスワード
        fields = ('username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

# 検索するためのForm
class SearchForm(forms.Form):
    # required=Falseにより、入力は必須ではなく任意
    freeword = forms.CharField(min_length=1, max_length=30,
    label='', required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

#tag作成フォーム
class TagsForm(forms.ModelForm):
    class Meta:
        model = Tags
        # forms.pyでは、HTML側で入力可能にする項目を指定する。
        fields = ('name',)

    # 継承
    def __init__(self, *args, **kwargs):
        # super　継承
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            # 各fieldに対してform-controlというクラスを与える
            field.widget.attrs['class'] = 'form-control'

# コメント投稿フォーム
class CommentCreateForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)

    def __init__(self, *args, **kwargs):
        # super　継承
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            # 各fieldに対してform-controlというクラスを与える
            field.widget.attrs['class'] = 'form-control'