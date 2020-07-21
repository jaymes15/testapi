from . import views
from django.conf.urls import url
from django.urls import path
from  .views import DetailsListView,DetailView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings



app_name= 'customapi'
urlpatterns = [
	path('', views.homepage,name='homepage'),
	path('getalldetails/',DetailsListView.as_view()),
	path('getdetail/<int:id>',DetailView.as_view())
	
	]

urlpatterns += staticfiles_urlpatterns()

urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
