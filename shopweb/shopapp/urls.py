"""
URL configuration for shopweb project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.urls import path
from . import views
from .views import UpdatePostView

urlpatterns = [
    #     products
    path("", views.products, name="products"),
    path("product/<str:product_name>/", views.products_comments, name="products_comments"),
    path("add_products/", views.add_products, name="add_products"),
    path("edit_product_post/<str:product_name>/", UpdatePostView.as_view(), name="edit_product_post"),
    path("delete_product_post/<str:product_name>/", views.Delete_product_Post, name="delete_product_post"),
    path("search/", views.search, name="search"),

    
#     profile
    path("profile/", views.Profile, name="profile"),
    path("edit_profile/", views.edit_profile, name="edit_profile"),
    path("user_profile/<int:myid>/", views.user_profile, name="user_profile"),
    
#    user authentication
    path("signup/", views.signup, name="signup"),
    path("login/", views.Login, name="login"),
    path("logout/", views.Logout, name="logout"),

]