from django.urls import path
from . import views

urlpatterns = [path("posts/", views.postlist, name = "postlist"),
            #    path("posts/<int:id>", views.postlist, name = "single_feed")
               path("posts/create", views.create_post, name = "create_post"),
               path("posts/edit/<int:id>", views.edit_post, name = "edit_post"),
               path("posts/delete/<int:id>", views.delete_post, name = "delete_post")
               ]
