from django.utils.translation import ugettext_lazy as _

import horizon


class MyGroup(horizon.PanelGroup):
    slug = 'mygroup'
    name = _('My Group')
    panels = ('mypanel',)


class NedgeDashboard(horizon.Dashboard):
    name = _("NexentaEdge")
    slug = "nedge_dashboard"
    panels = ('Mygroup', 'mypanel', )
    default_panel = 'mypanel'



horizon.register(NedgeDashboard)
