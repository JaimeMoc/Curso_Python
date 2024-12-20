# We import the libraries.
from django.contrib import admin
from django.urls import path
from .views import ReviewView

# We define the URLs of the applications.
urlpatterns = [
    path('', ReviewView.as_view(), name='movie'), # We declare the Movie app in general.
    path('<int:pk_movie>', ReviewView.as_view(), name='get_review_by_movie'), # We declare a filter to return one movie per pk.
    path('review/<int:pk_review>', ReviewView.as_view(), name='update_and_delete_review'), # We declare the app review.
]