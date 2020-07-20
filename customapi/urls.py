from . import views
from django.conf.urls import url
from django.urls import path
from  .views import DetailsListView



app_name= 'customapi'
urlpatterns = [
	path('', views.homepage,name='homepage'),
	path('getalldetails/',DetailsListView.as_view())
	]