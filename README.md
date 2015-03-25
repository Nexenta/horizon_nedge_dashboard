An OpenStack Horizon plugin that lists cluster properties and nodes properties (VMworld 2014).

=== Horizon Nedge Dashboard ===

This guide assumes that you have Horizon Dashboard (Icehouse) installed from Ubuntu packages (instructions on install Hozion: http://docs.openstack.org/icehouse/install-guide/install/apt/content/install_dashboard.html).
Installation Instructions

==== Installation ====

Download the tarball and extract it to the appropriate location, as a superuser:

 sudo sh -c "apt-get install tar wget -y && \ 
 cd /usr/share/openstack-dashboard/openstack_dashboard/dashboards && \ 
 wget https://s3.amazonaws.com/ish-archive/2014/Clients/Nexenta/horizon_nedge_dashboard.0-0-0.tar.gz && \ 
 tar -xvf horizon_nedge_dashboard.0-0-0.tar.gz"

Modify the configuration file /usr/share/openstack-dashboard/openstack_dashboard/settings.py to (1) register the new plugin as an installed app, and (2) specify the Nedge statistics endpoint

1. Modify the INSTALLED_APPS list:

  INSTALLED_APPS = [ ... , 'openstack_dashboard.dashboards.horizon_nedge_dashboard', ]

2. Add the NEDGE_URL configuration parameter, for example:

  NEDGE_URL="http://10.3.30.231:8080/" # with final slash

Next, restart apache and memcached and you should be able to see the Nedge Dashboard in the side menu of your Horizon Dashboard:

 sudo sh -c "service apache2 restart && service memcached restart"

==== Installation in Development ====

1. Get the git
2. Modify settings.py
3. Restart apache and memcached
4. Profit

==== Version ====

This is version 0.0.1