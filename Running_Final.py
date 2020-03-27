from tkinter import *


class Running_app(Frame):

    def __init__(self, master = None):
        Frame.__init__(self,master)
        self.master = master
        self.init_window()
        self.init_widgets()
        #self.calculate_stats()
        self.stats_old()
        

    def init_window(self):
        self.master.title("Running App")

    def init_widgets(self):#
        # Lables for Inputs
        Label(text="Input Running Stats").grid(row=0, column=1)
        # Lables for Inputs
        Label(text="Distance in Km").grid(row=1, column=0)
        Label(text="Average Hart Rate").grid(row=2, column=0)
        Label(text="Average steps per minuet").grid(row=3, column=0)
        Label(text="Total Time of run(mins)").grid(row=4, column=0)

        # Text - "Stats From Run"
        Label(text="Run Stats").grid(row=6, column=1)
        # Labels for Run Outputs
        Label(text="% of Total Distance").grid(row=7, column=0)
        Label(text="Total Heart Beats in Run").grid(row=8, column=0)
        Label(text="Total Steps in Run").grid(row=9, column=0)
        Label(text="Heart Beats per Step").grid(row=10, column=0)
        # Labels for Totals outputs
        Label(text="Total Distance of Runs").grid(row=12, column=0)
        Label(text="Total Heart Beats").grid(row=13, column=0)
        Label(text="Total Steps").grid(row=14, column=0)
        Label(text="Total Time of Runs(mins)").grid(row=15, column=0)

        self.distance_kmVar = IntVar()
        Entry(textvariable = self.distance_kmVar, justify = RIGHT).grid(row=1, column=1)
        self.av_hrVar = IntVar()
        Entry(textvariable = self.av_hrVar, justify = RIGHT).grid(row=2, column=1)
        self.av_stepsVar = IntVar()
        Entry(textvariable = self.av_stepsVar, justify = RIGHT).grid(row=3, column=1)
        self.time_runVar = IntVar()
        Entry(textvariable = self.time_runVar, justify = RIGHT).grid(row=4, column=1)

        # Showing Stats fields - From run
        self.percent_totalVar = IntVar()
        lblPercenttotal = Label(textvariable = self.percent_totalVar).grid(row=7, column=1)
        self.total_beats_runVar = IntVar()
        lblTotal_beats_run = Label(textvariable = self.total_beats_runVar).grid(row=8, column=1)
        self.total_steps_runVar = IntVar()
        lblTotal_steps_run = Label(textvariable = self.total_steps_runVar).grid(row=9, column = 1)
        self.heart_beats_per_step_runVar = IntVar()
        lblHeart_beats_per_step = Label(textvariable = self.heart_beats_per_step_runVar).grid(row=10, column=1)

        # Text - "Total Stats"
        Label(text="Running Totals").grid(row=11, column=1)

        # Showing Running Totals
        self.total_disVar = IntVar()
        lblTotal_dis = Label(textvariable = self.total_disVar).grid(row=12, column=1)
        self.total_hbVar = IntVar()
        lblTotal_hb = Label(textvariable = self.total_hbVar).grid(row=13, column=1)
        self.total_stepsVar = IntVar()
        lblTotal_steps = Label(textvariable = self.total_stepsVar).grid(row=14, column=1)
        self.total_timeVar = IntVar()
        lblTotal_time = Label(textvariable = self.total_timeVar).grid(row=15, column=1)
        
        # Create Buttons
        btCalculateStats = Button(text="Calculate Stats", command= self.calculate_stats).grid(row=5, column=1)
                                                            #    command=lambda: calculate_stats(distance_km, av_hr, av_steps, time_run                                                   #     
        btQuit= Button(text='Save and Quit', command=self.save_exit).grid(row=17,column=1)

        show_stats = Button(text='Show Old', command=self.stats_old).grid(row=18, column=1)


    def stats_old(self):
        f = open('testing_new1.txt','r')
        old_stats = []
        for line in f:
            old_stats.append(line.strip('\n'))
        self.old_distanceVar = IntVar()
        self.old_av_hrVar = IntVar()
        self.old_av_stepsVar = IntVar()
        self.old_timeVar = IntVar()
        self.old_distanceVar = old_stats[0]
        self.old_av_hrVar = old_stats[1]
        self.old_av_stepsVar = old_stats[2] 
        self.old_timeVar = old_stats[3]
        old_stats_list = (self.old_distanceVar, self.old_av_hrVar, self.old_av_stepsVar, self.old_timeVar)
        print(old_stats_list)
        f.close()
##        with open("testing1.txt", "r") as f:
##            old_stats = [e1,e2,e3,e4]
##            f.readlines()
##            e1.get(f.seek(0))
##            e2.get(f.seek(1))
##            e3.get(f.seek(2))
##            e4.get(f.seek(3))
##            print(old_stats
##        

    def calculate_stats(self):
        percent_total = float(self.distance_kmVar.get()) / float(self.old_distanceVar)
        self.percent_totalVar.set(format(percent_total, '10.8f'))

        total_beats_run = float(self.av_hrVar.get()) * float(self.time_runVar.get())
        self.total_beats_runVar.set(format(total_beats_run, '10.2f'))
      
        total_steps_run = float(self.av_stepsVar.get()) * float(self.time_runVar.get())
        self.total_steps_runVar.set(format(total_steps_run, '10.2f'))

        heart_beats_per_step_run = float(self.av_hrVar.get()) / float(self.av_stepsVar.get())
        self.heart_beats_per_step_runVar.set(format(heart_beats_per_step_run, '10f'))


        total_dis = float(self.distance_kmVar.get()) + float(self.old_distanceVar)
        self.total_disVar.set(format(total_dis, '10.2f'))

        total_hb = float(self.total_beats_runVar.get()) + float(self.old_av_hrVar)
        self.total_hbVar.set(format(total_hb, '10.2f'))

        total_steps = float(self.total_steps_runVar.get()) + float(self.old_av_stepsVar)
        self.total_stepsVar.set(format(total_steps, '10.2f'))

        total_time = float(self.time_runVar.get()) + float(self.old_timeVar)
        self.total_timeVar.set(format(total_time, '10.2f'))


        
    def save_exit(self):
        distance = self.total_disVar.get()
        av_hr = self.total_hbVar.get()
        av_steps = self.total_stepsVar.get()
        time = self.total_timeVar.get()
        with open("testing_new1.txt", "w") as file:
            file.write("{}\n".format(distance))
            file.write("{}\n".format(av_hr))
            file.write("{}\n".format(av_steps))
            file.write("{}\n".format(time))        
        exit()


def main():

    root = Tk()

    app = Running_app(root)

    root.mainloop()


if __name__ == '__main__':
    main()

##
##
##from tkinter import *
##
##total_dis = 5000
##
##class Running_app:
##    total_dis = 5000
##    def __init__(self, master = None):
##        self.window = Frame(master)
##        self.master = master
##        self.init_window()
##        self.init_widgets()
##        self.calculate_stats()
##        
##
##    def init_window(self):
##        self.master.title("Running App")
##
##    def init_widgets(self):#
##        # Lables for Inputs
##        Label(text="Input Running Stats").grid(row=0, column=1)
##        # Lables for Inputs
##        Label(text="Distance in Km").grid(row=1, column=0)
##        Label(text="Average Hart Rate").grid(row=2, column=0)
##        Label(text="Average steps per minuet").grid(row=3, column=0)
##        Label(text="Total Time of run(mins)").grid(row=4, column=0)
##
##
##        self.distance_km = IntVar(self.window)
####        self.distance_km.set('00.0')
##        self.distance_input = Entry(self.window, textvariable = self.distance_km)
##        self.distance_input.grid(row=1, column=1)
##
##        self.av_hr = IntVar(self.window)
####        self.av_hr.set('00.0')
##        self.av_hr_input = Entry(self.window, textvariable = self.av_hr)
##        self.av_hr_input.grid(row=2, column=1)
##
##        
##        self.av_steps = IntVar(self.window)
####        self.av_steps.set('00.0')
##        self.av_steps_input = Entry(self.window, textvariable = self.av_steps)
##        self.av_steps_input.grid(row=3, column=1)
##
##        self.time_run = IntVar(self.window)
####        self.time_run.set('00.0')
##        self.time_run_input = Entry(self.window, textvariable = self.time_run)
##        self.time_run_input.grid(row=4, column=1)
##                                    
##
##
##
##        # Entrie fields for Inputs
####        self.distance_kmVar = IntVar()
####        self.distance_km = Entry(textvaribale = self.distance_kmVar, justify = RIGHT).grid(row=1, column=1)
####        self.av_hrVar = IntVar()
####        self.av_hr = Entry(textvariable = self.av_hrVar, justify = RIGHT).grid(row=2, column=1)
####        self.av_stepsVar = IntVar()
####        self.av_steps = Entry(textvariable = self.av_stepsVar, justify = RIGHT).grid(row=3, column=1)
####        self.time_runVar = IntVar()
####        self.time_run = Entry(textvariable = self.time_runVar, justify = RIGHT).grid(row=4, column=1)
##
##        # Text - "Stats From Run"
##        Label(text="Run Stats").grid(row=6, column=1)
##        # Labels for Run Outputs
##        Label(text="% of Total Distance").grid(row=7, column=0)
##        Label(text="Total Heart Beats in Run").grid(row=8, column=0)
##        Label(text="Total Steps in Run").grid(row=9, column=0)
##        Label(text="Heart Beats per Step").grid(row=10, column=0)
##        # Labels for Totals outputs
##        Label(text="Total Distance of Runs").grid(row=12, column=0)
##        Label(text="Total Heart Beats").grid(row=13, column=0)
##        Label(text="Total Steps").grid(row=14, column=0)
##        Label(text="Total Time of Runs(mins)").grid(row=15, column=0)
##
##        # Showing Stats fields - From run
##        self.percent_totalVar = IntVar()
##        lblPercenttotal = Label(textvariable = self.percent_totalVar).grid(row=7, column=1)
##        self.total_beats_runVar = IntVar()
##        lblTotal_beats_run = Label(textvariable = self.total_beats_runVar).grid(row=8, column=1)
##        self.total_steps_runVar = IntVar()
##        lblTotal_steps_run = Label(textvariable = self.total_steps_runVar).grid(row=9, column = 1)
##        self.heart_beats_per_step_runVar = IntVar()
##        lblHeart_beats_per_step = Label(textvariable = self.heart_beats_per_step_runVar).grid(row=10, column=1)
##
##        # Text - "Total Stats"
##        Label(text="Running Totals").grid(row=11, column=1)
##
##        # Showing Running Totals
##        self.total_disVar = IntVar()
##        lblTotal_dis = Label(textvariable = self.total_disVar).grid(row=12, column=1)
##        self.total_hbVar = IntVar()
##        lblTotal_hb = Label(textvariable = self.total_hbVar).grid(row=13, column=1)
##        self.total_stepsVar = IntVar()
##        lblTotal_steps = Label(textvariable = self.total_stepsVar).grid(row=14, column=1)
##        self.total_timeVar = IntVar()
##        lblTotal_time = Label(textvariable = self.total_timeVar).grid(row=15, column=1)
##        
##        # Create Buttons
##        btCalculateStats = Button(text="Calculate Stats", command= self.calculate_stats).grid(row=5, column=1)
##                                                            #    command=lambda: calculate_stats(distance_km, av_hr, av_steps, time_run                                                   #     
##        btQuit= Button(text='Save and Quit', command=self.save_exit).grid(row=17,column=1)
##
##    
##
##    def calculate_stats(self):
##        percent_total = float(self.distance_km.get()) / float(self.total_dis)
##        self.percent_totalVar.set(format(percent_total, '10.8f'))
##
##        total_beats_run = float(self.av_hr.get()) * float(self.time_run.get())
##        self.total_beats_runVar.set(format(total_beats_run, '10.2f'))
##      
##        total_steps_run = float(self.av_steps.get()) * float(self.time_run.get())
##        self.total_steps_runVar.set(format(total_steps_run, '10.2f'))
##
##        heart_beats_per_step_run = int(self.av_hr.get()) / int(self.av_steps.get())
##        self.heart_beats_per_step_runVar.set(format(heart_beats_per_step_run, '10f'))
##
##        
##    def save_exit(self):
##        exit()
##
##
##def main():
##
##    root = Tk()
##
##    app = Running_app(root)
##
##    root.mainloop()
##
##
##if __name__ == '__main__':
##    main()
##
##
