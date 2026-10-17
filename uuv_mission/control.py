#this is a PD controller that takes and error and calculates an output u to be passed into ClosedLoop

class Controller:
    def __init__(self):
        self.previous_error = 0
        #this initialises theerror as zero
    def calculate(self, error):

        Kp = 0.15
        Kd = 0.6
        e = error
        u = Kp * e + Kd * (e-self.previous_error)
        #here we have calculated the output u

        self.previous_error = e
        #here we have updated the previous error

        return u
    

