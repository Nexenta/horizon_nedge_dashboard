
from django.utils.translation import ugettext_lazy as _

import horizon


class MyGroup(horizon.PanelGroup):
    slug = 'mygroup'
    name = _('My Group')
    # panels = ( 'mypanel', 'config_panel', 'overview_panel', )
    panels = ( 'mypanel', )

class HorizonNedgeDashboard(horizon.Dashboard):
    name = _("NexentaEdge")
    slug = "nedge_dashboard"
    # panels = ('Mygroup', 'mypanel', 'config_panel', 'overview_panel', )
    panels = ( 'mypanel', )
    default_panel = 'mypanel'

horizon.register(HorizonNedgeDashboard)
