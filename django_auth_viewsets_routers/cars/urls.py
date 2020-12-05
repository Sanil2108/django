from cars.views import HelloWorldView, CarViewSet, EngineViewSet
from rest_framework.routers import DefaultRouter
from django.urls import path, include

car_view = CarViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

router = DefaultRouter()
router.register(r'car', CarViewSet)
router.register(r'engine', EngineViewSet)

urlpatterns = [
    path('helloworld/', HelloWorldView.as_view()),
    path('', include(router.urls))
    # path('car/', car_view),
]
