from horizon import tabs
from horizon import views

from openstack_dashboard.dashboards.mydashboard.mypanel import tabs as mydashboard_tabs


class IndexView(views.APIView):
    tab_group_class = mydashboard_tabs.MypanelTabs
    template_name = 'mydashboard/mypanel/index.html'
    clusters = "clusters123"

    def get_data(self, request, context, *args, **kwargs):
        context['clusters'] = 'These are my clusters'

        # Add data to the context here...
        return context
