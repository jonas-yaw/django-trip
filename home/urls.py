from django.urls import path
from .views import HomePageView, AboutPageView, SuggestPageView,SuggestDonePageView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("about/", AboutPageView.as_view(), name="about"),
    path("suggest", SuggestPageView.as_view(), name="suggest"),
    path("suggest_success", SuggestDonePageView.as_view(), name="suggest_done"),
]

