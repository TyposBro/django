from . import views
from django.urls import path


urlpatterns = [
    path("<int:index>", views.monthly_challenge_by_index),
    path("<str:month>", views.monthly_challenge_by_string),

]
