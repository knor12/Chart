__author__ = "Noreddine Kessa "
__license__ = "GPL"

from chart import *
from random import randint
from threading import Timer
from perpetualTimer import perpetualTimer

#this is a test bench for the chart module

class MainForm(Frame):

    def __init__(self, title, master=None):
        Frame.__init__(self, master )
        self.grid(row = 50, column = 50, sticky = W)
        self.master.title(title)
        self.label = Label(self, text='Hello')
        #self.label.grid(row=0, column=0)
        self.createWidgets()
        self.Measurment_number =0




    def createWidgets(self):
        padding =5
        self.chrtTemperature = Chart(self,bg="white" , width=1000, height=200)
        self.chrtTemperature.set_title("Temp chart")
        self.chrtTemperature.set_number_of_data_point(100)
        self.chrtTemperature.add_point(1,1)
        self.chrtTemperature.grid(row=1, column=1, columnspan=5 ,padx=padding , pady=padding)
        self.chrtTemperature.draw()

        self.chrtHumidity = Chart(self, bg="white", width=1000, height=200)
        self.chrtHumidity.set_title("Humidity chart")
        self.chrtHumidity.set_number_of_data_point(100)
        self.chrtHumidity.add_point(1, 1)
        self.chrtHumidity.grid(row=3, column=1,columnspan=5 ,padx=padding , pady=padding)
        self.chrtHumidity.draw()

        self.chrtPressure = Chart(self, bg="white", width=1000, height=200)
        self.chrtPressure.set_title("Pressure chart")
        self.chrtPressure.set_number_of_data_point(100)
        self.chrtPressure.add_point(1, 1)
        self.chrtPressure.grid(row=5, column=1 , columnspan=5 ,padx=padding , pady=padding)
        self.chrtPressure.draw()

        self.btnStartStop = Button(self , text="Start" , command=self.__btnStartStop_clicked)
        self.btnStartStop.grid(row=0, column=1)

        self.btnExit = Button(self, text="Exit" )
        self.btnExit.bind("<Button-1>", self.__btnExit_clicked)
        self.btnExit.grid(row=0, column=2)

        self.btnClear = Button(self, text="Clear" )
        self.btnClear.bind("<Button-1>", self.__btnClear_clicked)
        self.btnClear.grid(row=0, column=3)
        #self.pack()

    def __btnClear_clicked(self , event):

        #clear all the chart from data
        self.chrtTemperature.clear_data()
        self.chrtHumidity.clear_data()
        self.chrtPressure.clear_data()

        # update user interfaces
        self.chrtTemperature.draw()
        self.chrtHumidity.draw()
        self.chrtPressure.draw()

    def __btnStartStop_clicked(self):
        if self.btnStartStop['text']=="Start":
            self.btnStartStop['text']="Stop"
            #self.t = Timer(0.1, self.timer_call_back)
            self.__t = perpetualTimer(1, self.timer_call_back)
            self.__t.start()
            self.__t.run()

        else:
            self.btnStartStop['text']="Start"
            self.__t.cancel()



    def __btnExit_clicked(self , event):
        print("exiting")
        self.__t.cancel()
        self.destroy()
        exit()




    def timer_call_back(self):

        #incremenat the index
        self.Measurment_number+=1
        x=self.Measurment_number

        #get the data and pass it to the chart
        self.chrtTemperature.add_point(x,randint(27, 31) )
        self.chrtHumidity.add_point(x, randint(31, 42))
        self.chrtPressure.add_point(x, randint(31, 32))

        #update user interfaces
        self.chrtTemperature.draw()
        self.chrtHumidity.draw()
        self.chrtPressure.draw()

        #rearm the timerself.t.run()









if __name__ == '__main__':
    root = MainForm(title="Main Form" )
    root.createWidgets()
    root.mainloop()