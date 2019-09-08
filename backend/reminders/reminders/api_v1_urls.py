from django.urls import path, include

app_name = "api-v1"

urlpatterns = [
    path("auth/", include("rest_framework.urls", namespace="drf-auth")),
    path("", include("todo.urls", namespace="todo"))
]
