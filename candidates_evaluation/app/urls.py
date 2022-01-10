from django.urls import path
from . import views


urlpatterns = [
    path('', views.add_candidates),
    path('candidate/', views.add_candidates),
    path('registration/',views.add_registration),
    path('allcandidates/',views.get_all_candidates),
    path('login/',views.authenticate_user),
    path('logout/',views.log_out)
]
