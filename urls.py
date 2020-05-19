from django.conf.urls import url
from BRMapp import views


urlpatterns=[
    url ('$^',views.ViewBooks),
    url ('view-books',views.ViewBooks),
    url ('new-book',views.newBook),
    url ('search-book',views.searchBook),
    url ('edit-book',views.editBook ),
    url ('delete-book',views.deleteBook ),
    url ('add',views.add),
    url ('search',views.Search),
    url ('edit',views.edit),
]
