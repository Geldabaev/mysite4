from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name='home'),
    path("test/", views.test, name='test'),
    path("categ/<int:catid>/", views.categ, name="categ")
]
