from horizon import tabs
from horizon import views

from openstack_dashboard.dashboards.mydashboard.mypanel import tabs as mydashboard_tabs

import sys
sys.path.append("/usr/lib/python2.7/dist-packages")
import requests
import json

class IndexView(views.APIView):
    tab_group_class = mydashboard_tabs.MypanelTabs
    template_name = 'mydashboard/mypanel/index.html'

    def get_data(self, request, context, *args, **kwargs):

        clusters_endpoint = requests.get("http://192.168.100.1:8081/clusters")
        context['clusters'] = json.loads(clusters_endpoint.text)['clusters']

        context['python_version'] = sys.version

        # Add data to the context here...
        return context
