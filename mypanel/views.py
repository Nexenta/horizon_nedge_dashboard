from horizon import tabs
from horizon import views

from openstack_dashboard.dashboards.mydashboard.mypanel import tabs as mydashboard_tabs

import sys
sys.path.append("/usr/lib/python2.7/dist-packages")
# import pycurl 
import requests

class IndexView(views.APIView):
    tab_group_class = mydashboard_tabs.MypanelTabs
    template_name = 'mydashboard/mypanel/index.html'

    def get_data(self, request, context, *args, **kwargs):
        
#        c = pycurl.Curl()
#        c.setopt(c.URL, 'http://172.31.98.28:8081/')
#        clusters = c.perform()
#        context['clusters'] = clusters

        r = requests.get("http://172.31.98.28:8081/")
        context['clusters'] = r.text


        context['python_version'] = sys.version

        # Add data to the context here...
        return context
