from django.urls import path
from .views import ItemCreate, ItemDetail

urlpatterns = [
    # Endpoint to create a new item
    path('items/create/', ItemCreate.as_view(), name='item-create'),

    # Endpoints for retrieving, updating, and deleting an item by ID
    path('items/<int:item_id>/', ItemDetail.as_view(), name='item-detail'),
]
