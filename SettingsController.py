class SettingsController(object):
    """docstring for """

    def __init__(self, window):
        self.window = window

    # Save the data inside the model
    def saveData(self, trigger):
        counter = 0
        for row in self.window.getListBox().get_children():
            for box in row.get_children():
                for e in box.get_children():
                    if e.__class__.__name__ == 'SpinButton':
                        self.saveInto(e.get_value(), counter)
                        counter +=1

    # Reset the previous data
    def resetData(self, trigger):
        counter = 0
        for row in self.window.getListBox().get_children():
            for box in row.get_children():
                for e in box.get_children():
                    if e.__class__.__name__ == 'SpinButton':
                        print(counter + self.getFrom(counter))
                        counter += 1


    def saveInto(self, value, id):
        if (id==0):
            self.window.getModel().timer.setPhaseDuration(value)
        elif (id==1):
            self.window.getModel().timer.setBreakDuration(value)
        elif (id==2):
            self.window.getModel().timer.setSessionDuration(value)

    def getFrom(self, id):
        if (id==0):
            self.window.getModel().timer.getPhaseDuration()
        elif (id==1):
            self.window.getModel().timer.getBreakDuration()
        elif (id==2):
            self.window.getModel().timer.getSessionDuration()
