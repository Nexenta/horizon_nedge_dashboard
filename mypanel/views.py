from horizon import tabs
from horizon import views

from openstack_dashboard.dashboards.mydashboard.mypanel import tabs as mydashboard_tabs

import sys
sys.path.append("/usr/lib/python2.7/dist-packages")
from hurry.filesize import size
import requests
import json

class IndexView(views.APIView):
    tab_group_class = mydashboard_tabs.MypanelTabs
    template_name = 'mydashboard/mypanel/index.html'

    def get_data(self, request, context, *args, **kwargs):

        # clusters_endpoint = requests.get("http://10.3.30.230:8080/clusters")
        # context['clusters'] = json.loads(clusters_endpoint.text)['clusters']

        stats_endpoint = requests.get("http://10.3.30.230:8080/stats")

        context['nodes'] = []
        stats = json.loads(stats_endpoint.text)['response']['stats']
        nodes = stats['servers']
        for n in nodes:
            context['nodes'].append(n)
        context['nodes'] = nodes
        nodes_good = {x:nodes[x] for x in nodes if 100 == nodes[x]['health']}
        context['n_nodes_good'] = len(nodes_good)
        context['n_nodes_bad'] = len(nodes) - context['n_nodes_good']
        context['python_version'] = sys.version
        context['n_objects'] = stats['summary']['total_num_objects']
        context['capacity_total'] = size(stats['summary']['total_capacity'])
        context['capacity_used'] = size(stats['summary']['total_used'])
        context['capacity_available'] = size(stats['summary']['total_available'])

        return context
