# System libraries
import os

# Graphic libraries
from gi.repository import AppIndicator3
from gi.repository import Notify
from gi.repository import Gtk

# Controller
from IndicatorController import IndicatorController

class Indicator(object):
    """Contains method to generate the indicator and the menu"""

    def __init__(self):
        """Initialize the indicator and build the menu"""
        self.APPID = "Study Timer Indicator"
        self.ICON = os.path.abspath('stopwatch2.svg')
        self.view = AppIndicator3.Indicator.new(self.APPID, self.ICON, AppIndicator3.IndicatorCategory.SYSTEM_SERVICES)
        self.view.set_status(AppIndicator3.IndicatorStatus.ACTIVE)
        self.controller = IndicatorController()
        self.menu = Gtk.Menu()
        self.generateMenu()
        self.view.set_menu(self.menu)
        Notify.init(self.APPID)
        Gtk.main()

    def generateMenu(self):
        """Build the indicator menu and connect it to the application controller"""

        # Initialize all menu entries
        start_phase= Gtk.MenuItem("Start Phase")
        start_break = Gtk.MenuItem("Start Break")
        start_long_break = Gtk.MenuItem("Start Long Break")
        start_session = Gtk.MenuItem("Start Session")
        start_settings = Gtk.MenuItem("Settings")
        quit = Gtk.MenuItem("Quit")

        # Connect everything to the controller
        start_phase.connect('activate', self.controller.startPhase, self)
        start_break.connect('activate', self.controller.startBreak, self)
        start_long_break.connect('activate', self.controller.startBreak, self)
        #start_session.connect('activate', None)
        #start_settings.connect('activate', None)
        quit.connect('activate', self.quit)

        # Append all to the menu and show
        self.menu.append(start_phase)
        self.menu.append(start_break)
        self.menu.append(start_long_break)
        self.menu.append(start_session)
        self.menu.append(start_settings)
        self.menu.append(quit)
        self.menu.show_all()

    def enableMenuItem(self, item):
        item.set_sensitive(True)

    def disableMenuItem(self, item):
        item.set_sensitive(False)

    def startSettings(self):
        pass

    def playSound(self, sound):
        pass

    def quit(self, trigger):
        """Quit the application and close everything"""
        Notify.uninit()
        Gtk.main_quit()
