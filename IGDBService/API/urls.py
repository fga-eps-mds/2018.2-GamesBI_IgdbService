from django.urls import include, path
from .views import IgDBView

urlpatterns = [
    path('get_igdb_games_list/', IgDBView.as_view(), name="get_igdb_games"),
]