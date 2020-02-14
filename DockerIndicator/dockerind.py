#!/usr/bin/python

import appindicator
import pynotify
import gtk

#a = appindicator.Indicator('tubecheck', '/home/paul/scripts/neo.png', appindicator.CATEGORY_APPLICATION_STATUS)
#a = appindicator.Indicator('tubecheck', 'http://a0.twimg.com/profile_images/283061581/neo_reasonably_small.png', appindicator.CATEGORY_APPLICATION_STATUS)
a = appindicator.Indicator('tubecheck', '/usr/share/pixmaps/apple-green.png', appindicator.CATEGORY_APPLICATION_STATUS)
a.set_status( appindicator.STATUS_ACTIVE )
m = gtk.Menu()
ci = gtk.MenuItem( 'Check' )
qi = gtk.MenuItem( 'Quit' )

m.append(ci)
m.append(qi)

a.set_menu(m)
ci.show()
qi.show()

def checkStatus(item):
	
	# show the notification message
	pynotify.init('tubecheck')
	n = pynotify.Notification('<b>Paulgramming Channel</b>',
		'notification-message-im')
	n.show()

ci.connect('activate', checkStatus)

def quit(item):
	gtk.main_quit()

qi.connect('activate', quit)

gtk.main()


