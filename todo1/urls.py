from django.conf.urls import url

from .views import todo_list,todo_detail,fuck,todo_create


app_names = 'todos'

urlpatterns = [
    url(r'', todo_list),
     url(r'^create/', todo_create),
     url(r'^<id:int>/', todo_detail),
    url(r'^fuck/', fuck),
]