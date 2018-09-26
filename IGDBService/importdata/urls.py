from django.urls import include, path
from .views import IgDBView

urlpatterns = [
    # faz a requisiçao na api da igdb e salva no banco
    path('get_igdb_games_list_request/',
         IgDBView.as_view(), name="get_igdb_games"),
]
