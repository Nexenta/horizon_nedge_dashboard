from django.utils.translation import ugettext_lazy as _

import horizon

from openstack_dashboard.dashboards.horizon_nedge_dashboard import dashboard


class Mypanel(horizon.Panel):
    name = _("Dashboard")
    slug = "mypanel"


dashboard.HorizonNedgeDashboard.register(Mypanel)
