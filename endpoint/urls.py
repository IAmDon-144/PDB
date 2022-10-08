from django.urls import path
from .views import endPointsPBS


urlpatterns = [
    path("", endPointsPBS, name="end-points"),

]
