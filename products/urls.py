from django.urls import path
from . import views

urlpatterns = [
    path('add-product', views.add_product, name='add-product'),
    path('update-product/<int:p_id>', views.update_product, name='update-product'),
    path('delete-product/<int:p_id>', views.delete_product, name='delete-product'),
    path('rate-product/<int:p_id>', views.rate_product, name='rate-product'),
]
