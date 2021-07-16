from django.urls import path
from .views.resource_views import Resources, ResourceDetail
from .views.user_views import SignUp, SignIn, SignOut, ChangePassword


urlpatterns = [
  	# Restful routing
    path('resources/', Resources.as_view(), name='resources'),
    path('resources/<int:pk>/', ResourceDetail.as_view(), name='resource_detail'),
    path('sign-up/', SignUp.as_view(), name='sign-up'),
    path('sign-in/', SignIn.as_view(), name='sign-in'),
    path('sign-out/', SignOut.as_view(), name='sign-out'),
    path('change-pw/', ChangePassword.as_view(), name='change-pw')
]
