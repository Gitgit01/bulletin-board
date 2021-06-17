# chat/urls.py
from django.urls import path

from . import views

urlpatterns = [
    # ホーム画面
    path(r'', views.home, name='home'),
    # 掲示板一覧画面
    path(r'bulletin_board_list', views.bulletin_board_list, name='bbl'),
    #掲示板画面
    path(r'bulletin_board/<int:article_id>', views.bulletin_board, name='bb')
]