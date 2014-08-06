from django.utils.translation import ugettext_lazy as _

import horizon


# discard this comment.

class MyGroup(horizon.PanelGroup):
    slug = 'mygroup'
    name = _('My Group')
    panels = ('mypanel',)


class Mydashboard(horizon.Dashboard):
    name = _("My Dashboard (^)")
    slug = "mydashboard"
    panels = ('Mygroup', 'mypanel', )
    default_panel = 'mypanel'



horizon.register(Mydashboard)
