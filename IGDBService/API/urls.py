from django.urls import include, path
from .views import GamesNameListView, GamesSteamListView


urlpatterns = [
    path('get_igdb_games_list/name', GamesNameListView.as_view(), name="get_igdb_games_Name_list"), # retorna uma lista com o nome de todos os games salvos no banco de dados
    path('get_igdb_games_list/id_steam', GamesSteamListView.as_view(), name="get_igdb_games_id_steam_list"), # retorna uma lista com o id da steam de todos os games salvos no banco de dados
]