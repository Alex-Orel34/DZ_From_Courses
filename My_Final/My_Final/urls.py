from django.contrib import admin
from django.urls import path
from Farm.views.authorization import *
from Farm.views.checkout import *
from Farm.views.db_info import *
from Farm.views.edit_basket import *
from Farm.views.home_page import *
from Farm.views.product_page import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page, name='home_page'),
    path('sign_in/', sign_in, name='sign_in'),
    path('registration/', registration, name='registration'),
    path('<str:product_type>', product_page, name='product_page'),
    path('add_sw/<str:product_id>', add_to_basket, name='add_to_basket'),
    path('del_sw/<str:product_id>', delete_from_basket, name='del_from_basket'),
    path('checkout/', checkout, name='checkout'),
    path('db/', db_info, name='bd_info'),
    path('del_or/<str:order_id>', delete_from_order, name='del_from_order'),
    path('del_us/<str:user_id>', delete_from_user, name='del_from_user'),
]
