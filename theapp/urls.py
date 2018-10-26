from django.conf.urls import url
from . import views
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView,LogoutView

app_name = 'theapp'

urlpatterns = [
	# /theapp/
	url(r'^index/$', views.IndexView.as_view(), name='index'),

    url(r'^register/$',views.register,name='register'),


	url(r'^login/$', LoginView.as_view(template_name='theapp/login.html'), name='login'),

    url(r'^logout/$', LogoutView.as_view(next_page=reverse_lazy('theapp:login')), name='logout'),

	# /theapp/<sport_id>/
	url(r'^(?P<pk>[0-9]+)/$', views.EquipmentView.as_view(), name='equipment'),

	url(r'^(?P<pk>[0-9]+)/(?P<pk_alt>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

	url(r'^sport/add/$', views.AddItem.as_view(), name='item-add'),

	url(r'^sport/(?P<pk>[0-9]+)/$', views.SportUpdate.as_view(), name='sport-update'),

	url(r'^sport/(?P<pk>[0-9]+)/delete/$', views.DeleteItem.as_view(), name='item-delete'),

]