from rest_framework.routers import DefaultRouter

from .views import ReminderViewSet

app_name = "todo"

router = DefaultRouter()

router.register(r"todo", ReminderViewSet, basename="todo")

urlpatterns = router.urls
