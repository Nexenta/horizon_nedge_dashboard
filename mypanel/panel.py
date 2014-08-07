from django.utils.translation import ugettext_lazy as _

import horizon

from openstack_dashboard.dashboards.mydashboard import dashboard


class Mypanel(horizon.Panel):
    name = _("Nedge Admin")
    slug = "mypanel"


dashboard.NedgeDashboard.register(Mypanel)
