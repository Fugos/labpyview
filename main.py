import pyview2 as pv
import numpy as np
import serial
import time

## use pythonw main.py command to run on macOS

# Create a model
class WindowModel:
    def __init__(self):
        self.want_to_abort = False
        self.countA = 0
        self.countB = 0
        self.countC = 0  # A'
        self.countD = 0  # B'
        self.indA = []
        self.indB = []
        self.indC = []
        self.indD = []
        self.resultA = []
        self.resultB = []
        self.resultC = []
        self.resultD = []
        #self.ser = serial.Serial('COM2', 9600, timeout=0)
        #print(self.ser.is_open)
        #print(self.ser.name)

    def start(self):
        self.want_to_abort = False

        while True:
            self.countA += 1
            self.indA.append(self.countA)
            self.resultA.append(np.random.randn(1))
            print('about to read')
            #allbytes = self.ser.read(48)
            #print(allbytes)
            print('done reading')
            pv.update()

            time.sleep(0.1)
            if self.want_to_abort:
                break

    def readall(self):
        print("Reading all bytes!")
        #print(self.ser.read_all())
        print("Done reading all bytes!")

    def stop(self):
        self.want_to_abort = True


# Create a view
axes_params = dict(ylabel='Count Rate',
                   xlabel='time',
                   title='Count')
plotA = pv.Plot(x='indA', y='resultA', plot_type='plot', axes_params=dict(ylabel='Count Rate',
                                                                          xlabel='time',
                                                                          title='A Counter'))
plotB = pv.Plot(x='indB', y='resultB', plot_type='plot', axes_params=dict(ylabel='Count Rate',
                                                                          xlabel='time',
                                                                          title='B Counter'))
plotC = pv.Plot(x='indC', y='resultC', plot_type='plot', axes_params=dict(ylabel='Count Rate',
                                                                          xlabel='time',
                                                                          title='A\' Counter'))
plotD = pv.Plot(x='indD', y='resultD', plot_type='plot', axes_params=dict(ylabel='Count Rate',
                                                                          xlabel='time',
                                                                          title='B\' Counter'))
text_A = pv.TextCtrl('countA', label='A Counts', dtype=float)
text_B = pv.TextCtrl('countB', label='B Counts', dtype=float)
text_C = pv.TextCtrl('countC', label='C Counts', dtype=float)
text_D = pv.TextCtrl('countD', label='D Counts', dtype=float)

button_start = pv.Button('start', label='Start!')
button_stop = pv.Button('stop', label='Stop', single_threaded=False)
button_readall = pv.Button('readall', label='ReadAll')

WindowView = pv.View([[plotA, plotB],
                      [text_A, text_B],
                      [button_start, button_stop, button_readall]], title='CCU Data')

# Run the program
pv.run(WindowModel, WindowView)


