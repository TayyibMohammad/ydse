import math
import matplotlib.pyplot as plt

class ydse:
    
    def __init__(self, wavelength, d, D):
        self.d=d
        self.D=D
        self.wavelength=wavelength
        
    def calcPathDistance(self, x, y):
        return (x**2 + y**2)**0.5
    
    def intensityGen(self):
        yList = []
        phaseDiffList=[]
        for i in range(-10, 10, 1): 
            i*=0.0001
            yList.append(i)
            y1=((self.d)/2 - i)
            path1=self.calcPathDistance(self.D, y1)
            y2=((self.d)/2 + i)
            path2=self.calcPathDistance(self.D, y2)
            pathDiff=path1-path2
            phaseDiffList.append((2*math.pi/self.wavelength)*pathDiff)
        
        iList=[]
        for phaseDiff in phaseDiffList:
            iList.append(4*(math.cos(phaseDiff/2))**2)
    
        plt.plot(yList, iList)
        plt.show()
        
        
YDSE=ydse(4e-8, 0.0005, 4)
YDSE.intensityGen()
        

        
        
            
            