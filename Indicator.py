# System libraries
import os

# Graphic libraries
from gi.repository import AppIndicator3
from gi.repository import Notify
from gi.repository import Gtk

# Controller
from IndicatorController import IndicatorController

# Settings window
from Settings import Settings

class Indicator(object):
    """Contains method to generate the indicator and the menu"""

    def __init__(self):
        """Initialize the indicator and build the menu"""
        self.APPID = "Study Timer Indicator"
        self.ICON = os.path.abspath('stopwatch2.png')
        self.view = AppIndicator3.Indicator.new(self.APPID, self.ICON, AppIndicator3.IndicatorCategory.SYSTEM_SERVICES)
        self.view.set_status(AppIndicator3.IndicatorStatus.ACTIVE)
        self.controller = IndicatorController(self)
        self.settings = None
        self.menu = Gtk.Menu()
        self.generateMenu()
        self.view.set_menu(self.menu)
        Notify.init(self.APPID)
        Gtk.main()

    # Return the indicator View (AppIndicator3.Indicator)
    def getView(self):
        return self.view

    # Generate the indicator menu
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
        start_phase.connect('activate', self.controller.startPhase)
        start_break.connect('activate', self.controller.startBreak)
        #start_long_break.connect('activate', self.controller.startBreak, self)
        start_session.connect('activate', self.controller.startSession)
        start_settings.connect('activate', self.startSettings)
        quit.connect('activate', self.quit)

        # Append all to the menu and show
        self.menu.append(start_phase)
        self.menu.append(start_break)
        #self.menu.append(start_long_break)
        self.menu.append(start_session)
        self.menu.append(start_settings)
        self.menu.append(quit)
        self.menu.show_all()

    def enableMenuItem(self, item):
        item.set_sensitive(True)

    def disableMenuItem(self, item):
        item.set_sensitive(False)

    # Disable all indicator menu items apart from the selected one
    def disableMenuItems(self, item):
        for e in self.menu.get_children():
            if (e != item and e.get_label() != 'Quit'):
                e.set_sensitive(False)

    # Enable all menu items
    def enableMenuItems(self):
        for e in self.menu.get_children():
            e.set_sensitive(True)

    def startSettings(self, trigger):
        self.settings = Settings(self.controller)

    def playSound(self, sound):
        pass

    # Change the indicator label (only for timer)
    def changeLabel(self, minute, seconds):
        self.view.set_label(minute+":"+seconds, "")

    # Throw a Notification
    def throwNotification(self, text):
        Notify.Notification.new("<b>Study Indicator</b>", text ,self.ICON).show()

    def quit(self, trigger):
        """Quit the application and close everything"""
        Notify.uninit()
        Gtk.main_quit()
