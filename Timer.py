# Main library
import time

class Timer(object):
    """ Timer class """

    def __init__(self):
        self.startTime = 0
        self.phaseDuration = 2
        self.breakDuration = 1
        self.sessionDuration = 4

    def setPhaseDuration(self, duration):
        self.phaseDuration = duration

    def getPhaseDuration(self):
        return self.phaseDuration

    def setBreakDuration(self, duration):
        self.breakDuration = duration

    def getBreakDuration(self):
        return self.breakDuration

    def setSessionDuration(self, duration):
        self.sessionDuration = duration

    def getSessionDuration(self):
        return self.sessionDuration

    def setStartTime(self):
        self.startTime = time.mktime(time.localtime(time.time()))

    def getElapsedTime(self):
        seconds = int(time.mktime(time.localtime(time.time())) - self.startTime)
        minutes = int(seconds/60)
        return (minutes, seconds)
