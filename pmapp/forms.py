from django import forms
from .models import Post
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
# UserはあらかじめDjangoが準備している
from django.contrib.auth.models import User
# 登録フォームを定義するファイル


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        # forms.pyでは、HTML側で入力可能にする項目を指定する。
        fields = ('title', 'content', 'category', 'thumbnail')

# 継承
# bootstrapのCSSをpost_form.htmlのformのレイアウトに対して適用されるように設定
# このクラスが呼び出された時に最初に実行される処理
    def __init__(self, *args, **kwargs):
        # super　継承
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            # 各fieldに対してform-controlというクラスを与える
            # 定型文のようなもの
            field.widget.attrs['class'] = 'form-control'

# ログインフォーム
class LoginForm(AuthenticationForm):
    # レイアウトをきれいにするための記述　（書き方共通）
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
        # レイアウトをきれいにするための記述
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

# 検索するためのForm
class SearchForm(forms.Form):
    freeword = forms.CharField(min_length=1, max_length=30,
    label='', required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)