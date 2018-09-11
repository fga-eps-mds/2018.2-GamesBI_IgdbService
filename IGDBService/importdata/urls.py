from django.urls import include, path
from .views import IgDBView

urlpatterns = [
    path('get_igdb_games_list_request/', IgDBView.as_view(), name="get_igdb_games"),# faz a requisiçao na api da igdb e salva no banco
]
