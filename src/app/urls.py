from django.urls import path
from . import views
urlpatterns = [
   path('', views.HomePageView.as_view(), name='home'),
   path('contacts/home', views.HomePageView.as_view(), name='home'),
   path('detail/<int:pk>', views.ContactDetailView.as_view(), name='detail'),
   path('home', views.HomePageView.as_view(), name='home'),
   path('search/', views.search, name='search'),
   path('contacts/create', views.ContactCreateView.as_view(), name="create"),
   path('contacts/update/<int:pk>', views.ContactUpdateView.as_view(), name="update"),
   path('contacts/delete/<int:pk>', views.ContactDeleteView.as_view(), name="delete"),
   path('signup/', views.SignUpView.as_view(), name="signup"),

]
