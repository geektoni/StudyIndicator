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

    def __init__(self):
        timer = Timer()

    def startPhase(self, trigger, duration):
        pass

    def stopPhase(self, trigger):
        pass

    def startBreak(self, trigger, duration):
        pass

    def stopBreak(self, trigger):
        pass

    def startSession(self, trigger, duration):
        pass

    def stopSession(self, trigger):
        pass
