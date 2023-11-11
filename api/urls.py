from django.urls import path
from . import views
urlpatterns=[
    path("sponsor-create/",views.SponsorCreateAPIView.as_view()),
    path("sponsor-list/",views.SponsorListAPIView.as_view()),
    path("sponsor-id/<int:pk>/", views.SponsorRetrieveAPIVIEW.as_view()),
    path("sponsor-update/<int:pk>/",views.SponsorUpdateAPIView.as_view()),
    path("student-sponsor/create/",views.StudentSponsorCreateAPIView.as_view()),
    path("student-list/",views.StudentListAPIView.as_view()),
    path("dashboard-statistic/",views.DashboartStatisticAPIView.as_view()),
    path("student-create/",views.StudentCreateAPIView.as_view()),
    path("student-update/<int:pk>/",views.StudentUpdateAPIView.as_view()),
    path("student-sponsor-list/<int:pk>",views.StudentSponsorListAPIView.as_view()),
    path("dashboard-graphic/",views.GraphicAPIView.as_view()),



]


