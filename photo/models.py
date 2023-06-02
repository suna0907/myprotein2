from django.db import models
#accountsアプリのmodelsモジュールからCuatomUserをインポート
# Create your models here.
from accounts.models import CustomUser

class Category(models.Model):
    #投稿する写真のカテゴリを管理するモデル

    #カテゴリ名のフィールド
    title = models.CharField(
        verbose_name='カテゴリ'#フィールドのタイトル
        max_length=20)

def __str__(self):
    #オブジェクトを文字列に変換して返す
    #eturns(str):カテゴリ名
    return self.title

class PhotoPost(models.Model):
    # 投稿されたデータを管理するモデル
    # CustomUserモデルのuser_idとPhotoPostモデルを1対多の関係で結びつける
    # CustomUserが親でPhotoPostが子の関係になる
    user = models.ForeignKey(
        CustomUser,
        #フィールドのタイトル
        verbose_name='ユーザー',
        #ユーザーを削除する場合はそのユーザーの投稿データも全て削除する
        on_delete=models.CASCADE
        )
    #categoryモデルのtitleとPhotoPostモデルを1対多の関係で結びつける
    # categoryが親でPhotoPostが子の関係になる
    category = models.ForeignKey(
        Category,
        #フィールドのタイトル
        verbose_name='カテゴリ'
        #カテゴリに関連付けられた投稿データが存在する場合はそのカテゴリを削除できないようにする
        on_delete=models.PROTECT
        )
#タイトル用フィールド
title = models.CharField(
    verbose_name='タイトル', #フィールドのタイトル
    max_length=200           #最大文字数は200
    )
#コメント用のフィールド
comment = models.TextField(
    verbose_name='コメント', #フィールドのタイトル
    )
#イメージのフィールド１
image1 = models.ImageField(
    verbose_name='イメージ１', #フィールドのタイトル
    upload_to = 'photos', #media_poot以下のphotosにファイルを保存
    )
#イメージのフィールド２
image2 = models.ImageField(
    verbose_name='イメージ2', #フィールドのタイトル
    upload_to = 'photos', #media_poot以下のphotosにファイルを保存
    blank = True, #フィールド値の設定は必須ではない
    null = True #データベースにnullが保存されることを許容
    )
#投稿日時のフィールド
posted_at=models.DateTimeField(
    verbose_name='投稿日時'#フィールドのタイトル
    auto_now_add=True     #日時を自動追加
    )

def __str__(self):
    # オブジェクトを文字列に変換して返す
    # returns(str):投稿記事のタイトル
    return self.title