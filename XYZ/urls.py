from XYZ import views
from rest_framework.urls import path
# from django.urls import path

urlpatterns=[
    path('list/',views.Bloglist.as_view()),
    path('<int:id>',views.Bloginterested.as_view()),
    path('category',views.CategoryAPIViews.as_view(),name='category-list')
    ]
