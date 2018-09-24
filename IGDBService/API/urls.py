from django.urls import include, path
from .views import GamesNameListView, GamesSteamListView, GamesAllListView, GenreListView


urlpatterns = [
    path('get_igdb_games_list/name', GamesNameListView.as_view(), name="get_igdb_games_name_list"), # retorna uma lista com o nome de todos os games salvos no banco de dados
    path('get_igdb_games_list/id_steam', GamesSteamListView.as_view(), name="get_igdb_games_id_steam_list"), # retorna uma lista com o id da steam de todos os games salvos no banco de dados
    path('get_igdb_games_list/all', GamesAllListView.as_view(), name="get_igdb_games_all"), # retorna uma lista com o id da steam de todos os games salvos no banco de dados
    path('get_igdb_games_list/genres', GenreListView.as_view(), name="get_igdb_genres_all"), # retorna uma lista com o id da steam de todos os games salvos no banco de dados

]