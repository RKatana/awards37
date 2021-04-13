from . import views
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path("", views.index, name = "projects"),
    path("project/post/", views.post, name = "post"),
    path("profile/", views.profile, name = 'profile'),
    path("project/<int:project_id>/", views.project_detail, name = "details"),
    path("search/projects/results/", views.search, name = "search"),
    path("logout/", views.logout, name = "logout"),
    path("api/projects/", views.ProjectList.as_view()),
    path("api/profile/", views.ProfileList.as_view()),
    path("token/", obtain_auth_token),
    path("developer/api/", views.apiView, name = "api"),
]