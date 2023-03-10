"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include, re_path  # noqa
from info import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    re_path(r"^admin/", admin.site.urls),
    # re_path(r"^api/items/", views.TestAPI.as_view()),
    re_path(r"^api-auth/", include("rest_framework.urls")),
    path(
        "api/pages/",
        views.PageModelView.as_view(
            {"get": "list", "post": "create"},
        ),
        name="page_list",
    ),
    path(
        "api/page/<str:slug>/",
        views.PageModelView.as_view(
            {"get": "retrieve", "put": "update", "delete": "destroy"},
        ),
        name="page_detail",
    ),
    path(
        "api/page/<str:slug>/card/<str:name>/image/<int:id>",
        views.ImageView.as_view(
            {"get": "retrieve", "put": "update", "delete": "destroy"},
        ),
    ),
    path(
        "api/imgs/",
        views.SingleImageView.as_view(
            {"get": "list", "post": "create"},
        ),
        name="image_list",
    ),
    path(
        "api/img/<str:name>/",
        views.SingleImageView.as_view(
            {"get": "retrieve", "put": "update", "delete": "destroy"},
        ),
        name="image_detail",
    ),
    path(
        "api/item/<int:id>/",
        views.ItemView.as_view(
            {"get": "retrieve", "put": "update", "delete": "destroy"},
        ),
        name="item_detail",
    ),
    path(
        "api/home/",
        views.HomePageView.as_view({"get": "list"}),
        name="home_list",
    ),
    path(
        "api/home/related_wiki/",
        views.RelatedWikiView.as_view({"get": "list", "post": "create"}),
        name="related_wiki_list",
    ),
    path(
        "api/home/related_wiki/<int:id>/",
        views.RelatedWikiView.as_view(
            {"get": "retrieve", "put": "update", "delete": "destroy"},
        ),
        name="related_wiki_detail",
    ),
    path(
        "api/home/footer/",
        views.FooterView.as_view({"get": "list"}),
        name="footer_list",
    ),
    path(
        "api/home/sections/",
        views.HPSView.as_view({"get": "list"}),
        name="section_list",
    ),
    path(
        "api/home/sections/<int:id>/",
        views.HPSView.as_view(
            {"get": "retrieve", "put": "update", "delete": "destroy"},
        ),
        name="section_list",
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
