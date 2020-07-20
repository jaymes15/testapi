from . import views
from django.conf.urls import url
from django.urls import path
from  .views import DetailsListView,DetailView



app_name= 'customapi'
urlpatterns = [
	path('', views.homepage,name='homepage'),
	path('getalldetails/',DetailsListView.as_view()),
	path('getdetail/<int:id>',DetailView.as_view())
	

	]