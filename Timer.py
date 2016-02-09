# Main library
import time

class Timer(object):
    """ Timer class """

    def __init__(self):
        self.startTime = 0
        self.MAXPHASEDURATION = 60
        self.MAXBREAKDURATION = 30
        self.MAXSESSIONDURATION = 10
        self.phaseDuration = 25
        self.breakDuration = 5
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

    def getMAXPHASEDURATION(self):
        return self.MAXPHASEDURATION

    def getMAXBREAKDURATION(self):
        return self.MAXBREAKDURATION

    def getMAXSESSIONDURATION(self):
        return self.MAXSESSIONDURATION

    def setStartTime(self):
        self.startTime = time.mktime(time.localtime(time.time()))

    def getElapsedTime(self):
        seconds = int(time.mktime(time.localtime(time.time())) - self.startTime)
        minutes = int(seconds/60)
        return (minutes, seconds)
