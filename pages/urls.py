from django.urls import path 

from .views import AboutPageView, ContactView, HomePageView, ProductCreateView, ProductIndexView, ProductShowView, CreatedView  

urlpatterns = [ 
    path("", HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('contact/', ContactView.as_view(), name='contact'), 
    path('products/', ProductIndexView.as_view(), name='index'), 
    path('products/create', ProductCreateView.as_view(), name='form'), 
    path('products/<str:id>', ProductShowView.as_view(), name='show'), 
    path('products/succesful/created', CreatedView.as_view(), name='created'), 
] 