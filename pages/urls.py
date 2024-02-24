from django.urls import include, path

from pages.utils import ImageLocalStorage 

from .views import AboutPageView, CartRemoveAllView, CartView, ContactView, HomePageView, ImageViewFactory, ImageViewNoDI, ProductCreateView, ProductIndexView, ProductShowView, CreatedView  

urlpatterns = [ 
    path("", HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('contact/', ContactView.as_view(), name='contact'), 
    path('products/', ProductIndexView.as_view(), name='index'), 
    path('products/create', ProductCreateView.as_view(), name='form'), 
    path('products/<str:id>', ProductShowView.as_view(), name='show'), 
    path('products/succesful/created', CreatedView.as_view(), name='created'), 
    path('cart/', CartView.as_view(), name='cart_index'), 
    path('cart/add/<str:product_id>', CartView.as_view(), name='cart_add'), 
    path('cart/removeAll', CartRemoveAllView.as_view(), name='cart_removeAll'),
    path('image/', ImageViewFactory(ImageLocalStorage()).as_view(), name='image_index'), 
    path('image/save', ImageViewFactory(ImageLocalStorage()).as_view(), name='image_save'), 
    path('imagenotdi/', ImageViewNoDI.as_view(), name='imagenodi_index'), 
    path('image/save', ImageViewNoDI.as_view(), name='imagenodi_save'), 
] 