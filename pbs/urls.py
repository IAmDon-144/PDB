from django.urls import path
from .views import allPBS, allSubZonal, allZonal, allComplainCenter, allFiders, allReport, getChild

urlpatterns = [


    path("all-pbs/", allPBS.as_view(), name="all-pbs"),
    path("all-zonal/", allZonal.as_view(), name="all-zonal"),
    path("all-sub-zonal/", allSubZonal.as_view(), name="all-sub-zonal"),
    path("all-complain-center/", allComplainCenter.as_view(),
         name="all-complain-center"),
    path("all-fider/", allFiders.as_view(), name="all-fider"),
    path("all-report/", allReport.as_view(), name="all-report"),




    path("get-child/<str:pk>/", getChild.as_view(), name="get-pbs"),

]
