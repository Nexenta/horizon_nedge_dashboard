
from django.utils.translation import ugettext_lazy as _

import horizon


class MyGroup(horizon.PanelGroup):
    slug = 'mygroup'
    name = _('My Group')
    panels = ('mypanel',)


class HorizonNedgeDashboard(horizon.Dashboard):
    name = _("NexentaEdge")
    slug = "nedge_dashboard"
    panels = ('Mygroup', 'mypanel', 'config', )
    default_panel = 'mypanel'

horizon.register(HorizonNedgeDashboard)
