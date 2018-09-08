from django.urls import include, path
<<<<<<< d587316b453efdffa92b57e922245937701a8e67
from .views import IgDBView, GamesListView, GamesNameListView, GamesSteamListView

urlpatterns = [
    path('get_igdb_games_list_request/', IgDBView.as_view(), name="get_igdb_games"),# faz a requisiçao na api da igdb e salva no banco
    path('get_igdb_games_list/', GamesListView.as_view(), name="get_igdb_games"), #retorna uma lista com os dados dos games
    path('get_igdb_games_list/Name', GamesNameListView.as_view(), name="get_igdb_games_Name_list"), # retorna uma lista com o nome de todos os games salvos no banco de dados
    path('get_igdb_games_list/Id_Steam', GamesSteamListView.as_view(), name="get_igdb_games_id_steam_list"), # retorna uma lista com o id da steam de todos os games salvos no banco de dados
]
=======
from .views import IgDBView

urlpatterns = [
    path('get_igdb_games_list/', IgDBView.as_view(), name="get_igdb_games"),
]
>>>>>>> [ADD] #90 Starting to create igdb games import
