from django.conf.urls import patterns  # noqa
from django.conf.urls import url  # noqa

from .views import IndexView

from openstack_dashboard.dashboards.horizon_nedge_dashboard.mypanel import views

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^\?tab=mypanel_tabs__tab$', views.IndexView.as_view(), name='mypanel_tabs'),
)
