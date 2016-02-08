# Main library
import time

class Timer(object):
    """ Timer class """

    def __init__(self):
        self.startTime = 0
        self.phaseDuration = 25
        self.breakDuration = 5
        self.sessionDuration = self.phaseDuration*4+self.breakDuration*4

    def setPhaseDuration(duration):
        self.phaseDuration = duration

    def getPhaseDuration():
        return self.phaseDuration

    def setBreakDuration(duration):
        self.breakDuration = duration

    def getBreakDuration():
        return self.breakDuration

    def setSessionDuration(duration):
        self.sessionDuration = duration

    def getSessionDuration():
        return self.sessionDuration

    def setStartTime():
        self.startTimer = time.mktime(time.localtime(time.time())

    def getElapsedTime():
        seconds = int(time.mktime(time.localtime(time.time())) - self.startTime)
        minutes = int(seconds/60)
        return (minutes, seconds)
