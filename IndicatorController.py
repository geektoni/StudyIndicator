# Library to manage time
import time
import sys

# Graphic libraries and auxiliaries
from gi.repository import GObject
from Settings import Settings

# Model class
from Timer import Timer

class IndicatorController(object):
    """Indicator Controller class, all the actions are here"""

    def __init__(self, indicator):
        self.timer = Timer()
        self.indicator = indicator
        self.eventSource = None

    # Function that start a study phase. It changes the label of
    # the trigger and deactivate all the other indicator menu entries.
    def startPhase(self, trigger):
        trigger.set_label("Stop Phase")
        trigger.disconnect_by_func(self.startPhase)
        trigger.connect('activate', self.stopPhase)
        self.indicator.disableMenuItems(trigger)
        self.timer.setStartTime()
        self.eventSource = GObject.timeout_add(1000, self.labelChanger, self.timer.getPhaseDuration())

    # Stop the phase and reset the indicator label. It also
    # enable all the indicator menu items
    def stopPhase(self, trigger):
        trigger.set_label("Start Phase")
        trigger.disconnect_by_func(self.stopPhase)
        trigger.connect('activate', self.startPhase)
        self.indicator.enableMenuItems()
        if (self.eventSource != None):
            self.indicator.getView().set_label("", "")
            GObject.source_remove(self.eventSource)

    # Start break phase. It is the same of startPhase
    def startBreak(self, trigger):
        trigger.set_label("Stop Break")
        trigger.disconnect_by_func(self.startBreak)
        trigger.connect('activate', self.stopBreak)
        self.indicator.disableMenuItems(trigger)
        self.timer.setStartTime()
        self.eventSource = GObject.timeout_add(1000, self.labelChanger, self.timer.getBreakDuration())

    # Stop break phase. It is the same of stopPhase
    def stopBreak(self, trigger):
        trigger.set_label("Start Break")
        trigger.disconnect_by_func(self.stopBreak)
        trigger.connect('activate', self.startBreak)
        self.indicator.enableMenuItems()
        if (self.eventSource != None):
            self.indicator.getView().set_label("", "")
            GObject.source_remove(self.eventSource)

    # Start a work session, it is composed of some working phases
    # an some break phases. For example, 3 working phases and 3
    # break phases.
    def startSession(self, trigger):
        trigger.set_label("Stop Session")
        trigger.disconnect_by_func(self.startSession)
        trigger.connect('activate', self.stopSession)
        self.indicator.disableMenuItems(trigger)
        self.timer.setStartTime()
        self.eventSource = GObject.timeout_add(1000, self.labelChangerSession, self.timer.getPhaseDuration(), 0, self.timer.getSessionDuration())

    def stopSession(self, trigger):
        trigger.set_label("Start Session")
        trigger.disconnect_by_func(self.stopSession)
        trigger.connect('activate', self.startSession)
        self.indicator.enableMenuItems()
        if (self.eventSource != None):
            self.indicator.getView().set_label("", "")
            GObject.source_remove(self.eventSource)

    # This function change the label of the indicator, and it is used
    # inside a GObject loop. When the time arrive to a max, it will
    # return False instead of True
    def labelChanger(self, max):
        clock = self.timer.getElapsedTime()
        if (clock[0] == max):
            return False
        self.indicator.changeLabel(str(clock[0]), str(clock[1]%60))
        return True

    # This function is similar to labelChanger, but it is design specifically
    # for the session operation. It will call continuously the same function
    # as long as the counter is less than sessionDuration
    def labelChangerSession(self, max, counter, maxCounter):
        clock = self.timer.getElapsedTime()
        if (counter==maxCounter):
            return False
        if (clock[0] == max and max == self.timer.getPhaseDuration()):
            self.timer.setStartTime()
            self.eventSource = GObject.timeout_add(1000, self.labelChangerSession, self.timer.getBreakDuration(), counter+1, maxCounter)
            return False
        elif (clock[0] == max and max == self.timer.getBreakDuration()):
            self.timer.setStartTime()
            self.eventSource = GObject.timeout_add(1000, self.labelChangerSession, self.timer.getPhaseDuration(), counter+1, maxCounter)
            return False
        self.indicator.changeLabel(str(clock[0]), str(clock[1]%60))
        return True
