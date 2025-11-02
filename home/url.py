from django.urls import path
from . import views

urlpatterns = [
    path('', views.BookList.as_view(), name='book list page'),
    path('book/<slug:slug>/', views.BookDetail.as_view(), name='book_datail_page'),
    path('categories',views.CategoryList.as_view(),name='category_list_page'),
    path('category/<slug:slug>/', views.CategoryBooksView.as_view(), name='category_books'),
    path('author/<slug:slug>/', views.AuthorDetailView.as_view(), name='author_detail')
]