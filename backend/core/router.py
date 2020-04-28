from rest_framework.routers import SimpleRouter

from backend.core import views

router = SimpleRouter()

router.register(r"breeds", views.BreedViewSet, basename="breed")
router.register(r"categories", views.CategoryViewSet, basename="category")
router.register(r"groups", views.GroupViewSet, basename="group")
router.register(r"pregnancy-diagnosis", views.PregnancyDiagnosisViewSet, basename="pregnancy-diagnosis")
router.register(r"sheeps", views.SheepViewSet, basename="sheep")
router.register(r"users", views.UserViewSet, basename="user")
