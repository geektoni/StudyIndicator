# Graphical libraries
from gi.repository import Gtk

# Controller Library
from SettingsController import SettingsController

class Settings(Gtk.Window):
    """ Settings menu class. This generate the view """

    def __init__(self, indicatorController):
        # Initialize the controller and the caller
        self.caller = indicatorController
        self.controller = SettingsController(self)

        # Initialize the window and set the border width
        Gtk.Window.__init__(self, title="Settings")
        self.set_border_width(10)
        self.set_default_icon_from_file("stopwatch2.png")

        # Set up the listbox with all the elements needed
        self.listBox = Gtk.ListBox()
        self.listBox.set_selection_mode(Gtk.SelectionMode.NONE)
        self.buildEntriesSpin("Phase duration:", 1, self.caller.timer.getMAXPHASEDURATION(), self.caller.timer.getPhaseDuration())
        self.buildEntriesSpin("Break duration:", 1, self.caller.timer.getMAXBREAKDURATION(), self.caller.timer.getBreakDuration())
        self.buildEntriesSpin("Session duration:", 1, self.caller.timer.getMAXSESSIONDURATION(), self.caller.timer.getSessionDuration())
        self.buildButtons()

        # Add the listbox to the window e show everything
        self.add(self.listBox)
        self.show_all()

    def buildEntriesSpin(self, title, minvalue, maxvalue, default):
        """Build menu spin entries, useful to change values into Pomodoro"""

        ListRow = Gtk.ListBoxRow()
        Box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        Label = Gtk.Label(title, xalign=0)
        Spin = Gtk.SpinButton()
        adjustment = Gtk.Adjustment(default, minvalue, maxvalue, 1, 10, 0)
        Spin.set_adjustment(adjustment)
        Spin.set_value(default)
        Box.pack_start(Label, True, True, 0)
        Box.pack_start(Spin, True, True, 0)
        ListRow.add(Box)
        self.listBox.add(ListRow)

    def buildButtons(self):
        """Buil buttons to save and clear values in the window"""

        Box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        Save = Gtk.Button("Save")
        Clear = Gtk.Button("Clear")
        Save.connect('clicked', self.controller.saveData)
        Clear.connect('clicked', self.controller.resetData)
        Box.pack_start(Save, True, True, 0)
        Box.pack_start(Clear, True, True, 0)
        self.listBox.add(Box)


    def getListBox(self):
        return self.listBox

    def getModel(self):
        return self.caller
