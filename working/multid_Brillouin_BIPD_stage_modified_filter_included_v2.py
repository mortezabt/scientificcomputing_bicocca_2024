# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 09:01:24 2024

@author: VIBRA SR
"""

from pycromanager import *
import matplotlib.pyplot as plt
import numpy as np
import time
from scipy.optimize import curve_fit
from scipy import optimize
import os
import shutil
import datetime
from lmfit.models import SkewedGaussianModel
import clr


calibrate = 1
if calibrate ==1:
    import spectolib
    bipd = spectolib.SpectoBIPD("COM9")    #Verify BIPD's COM port
    bipd.heater_set_enabled(True)
    # ang_init = bipd.rotator_get_position() 
    # vol_init

    # bipd.rotator_set_position(ang_home)
    # bipd.lc_set_level(vol_min)
    
    def cal_ang(plot, correct, ang_range, ang_step):     
        """optimizing the angle"""
        global ang_min  
        mmc.set_exposure(expo1)
        pos = bipd.rotator_get_position()
        f = pos           
        print("Optimizing Angle...")            
        k=0
        span = np.arange(f - ang_range, f + ang_range, ang_step)
        
        acql = Acquisition(directory=pathl, name=namel, show_display= False)
        
        k=0
        for i in span:
            f = i
            d = f
                
            #print(f'Moving to position {f}')
            bipd.rotator_set_position(d)
            time.sleep(0.2)
            #time.sleep(0.1)      # add this in case the plots are not good
            eventl = { 'axes': {'time': k} }
            acql.acquire(eventl)
            dl = acql.get_dataset()
            k+=1
        acql.mark_finished() 
        # with Acquisition(directory = pathl, name = namel, show_display= False) as acql:
        #     k=0
        #     for i in span:
        #         f = i
        #         d = f
                
        #         #print(f'Moving to position {f}')
        #         bipd.rotator_set_position(d)
        #         time.sleep(0.2)
        #         #time.sleep(0.1)      # add this in case the plots are not good
        #         eventl = { 'axes': {'time': k} }
        #         acql.acquire(eventl)
        #         dl = acql.get_dataset()
        #         k+=1
                    
        dask_arrayl = dl.as_array()
        x1l = dask_arrayl.compute()
        x1l= x1l[0,:,:,:]
                 
        
        Msl = (x1l.mean(axis=1)).mean(axis=1)
        if correct == True:
            Msl[1]=Msl[0]
            Msl[2]=Msl[3]
        Ms_bl =[]
        Ms_bl = Msl
        
        
        
        mn = min(Ms_bl)
        
        
        x_model = span  
        if plot == True:
            plt.figure()       
            plt.scatter(span, Ms_bl)
            plt.show()
            plt.title("Angle")
            plt.xlabel("Degrees")
            plt.ylabel("Intensity")
        lst_Ms_bl = Ms_bl.tolist()
        index_mn = lst_Ms_bl.index(mn)
        ang_min = x_model[index_mn]
            
             
             
        ang_min =round(ang_min, 4)
        f = ang_min
        d = f
        
        #print(f'Moving to position {f}')
        bipd.rotator_set_position(d)
        time.sleep(0.1)    
        
        print("Angle set to %sdeg by single point" % ang_min)


    # def cal_vol(plot=True, correct=True,vol_range = 0.02, vol_step = 0.001, expo2 = 30):
    def cal_vol(plot, correct,vol_range , vol_step , expo2 ):
        """Optimizing the voltage"""
        
        global vol_min
        vol1 = vol_min
         
        print("Optimizing Voltage...")      
        k=0
        span = np.arange(vol1 - vol_range, vol1 + vol_range, vol_step)
        mmc.set_exposure(expo2)
        
        
        acql = Acquisition(directory=pathl, name=namel, show_display= False)
        k=0
        for i in span:
            bipd.lc_set_level(i)
            time.sleep(0.1)      # add this in case the plots are not good
            eventl = { 'axes': {'time': k} }
            acql.acquire(eventl)
            dl = acql.get_dataset()
            k+=1
        acql.mark_finished()
        # with Acquisition(directory = pathl, name = namel, show_display= False) as acql:
        #     k=0
        #     for i in span:
        #         bipd.lc_set_level(i)
        #         time.sleep(0.1)      # add this in case the plots are not good
        #         eventl = { 'axes': {'time': k} }
        #         acql.acquire(eventl)
        #         dl = acql.get_dataset()
        #         k+=1
          
    
        dask_arrayl = dl.as_array()
        x1l = dask_arrayl.compute()
        x1l= x1l[0,:,:,:]
            
        ### create a variable with the mean value of the pixels related to the rayleigh name "M"###
        Msl = (x1l.mean(axis=1)).mean(axis=1)
        if correct == True:
            Msl[1]=Msl[0]
            Msl[2]=Msl[3]
           #plt.plot(span,Msl,label='plot')
        Ms_bl =[]
        Ms_bl = Msl
        # for l in Msl:
        #     minimum = min(Msl)
        #     Ms_bl.append(l - minimum)
        xz=vol1
        #try:
        mn = min(Ms_bl)
        
        
        """section until the "if" is to pick the min value without fitting""" 
        x_model = span
        if plot == True:     
            plt.figure()       
            plt.scatter(span, Ms_bl)
            plt.show()
            plt.title("Voltage")
            plt.xlabel("Voltage")
            plt.ylabel("Intensity")
        lst_Ms_bl = Ms_bl.tolist()
        index_mn = lst_Ms_bl.index(mn)
        vol_min = x_model[index_mn]
        
        
        
        
        vol_min =round(vol_min, 3)
        bipd.lc_set_level(vol_min)        
        time.sleep(0.1) 
        print("Voltage is set to %sV by single point" % vol_min)
        return vol_min

#%%

if calibrate ==1:
    
    ang_home =-15.37
    vol_min = 1680
    bipd.rotator_set_position(ang_home)
    bipd.lc_set_level(vol_min)


#%%
"""Set the following parameters before you start the acquisition"""
"""Run this section to preview the acquisition details"""

name = 'Delete_me'     # Set the name of the current acquisition
step = 2  # Stage maovement step size (um)
sampling = 200     # Optimization ocurring per this number of datapoints (number) 
freq = 2           # optimize angle for every "freq" voltage optimization  
bridge = Bridge()
mmc = bridge.get_core()
expo1 = mmc.get_exposure()  # Gets the exposure time in Micromanager for mapping, to set manually use the line below
#expo1 = 300       # Exposure time of camera for mapping (ms)

"""Creating Today's Directory"""

current_date = datetime.date.today()
year = current_date.strftime("%Y%m%d")
path = r'D:\OneDrive - CNR\_Spontaneous Raman (Vibra)\Brillouin\_Data\%s %s' %(year, name)
try:
    os.mkdir(path)
    print("Today's Directory Created")
except OSError as error:
    print("Today's Directory Already Exists")
namel = 'Delete_me'    
pathl = r'D:\Delete_me'     # Remove all the "Delete_me" files in this directory
shutil.rmtree(pathl, ignore_errors = True)      # remove the existing dump folder
try:
    os.mkdir(pathl)
    print("A New Dump Directory Created")
except OSError as error:
    print("Dump Directory Already Exists")    
    
  
"""Creating the acqusition events based on the stage positions"""

mm = bridge.get_studio()
pm = mm.positions()
pos_list = pm.get_position_list()
x_range = np.zeros((2))
y_range = np.zeros((2))
i = 0

for idx in range(2):
    pos = pos_list.get_position(idx)
    # pos.go_to_position(pos, mmc)
    print(pos.get_label())
    
    # for ipos in range(1, 2):
    # stage_pos = pos.get(ipos)
    # x_range[i] = stage_pos.x
    # y_range[i] = stage_pos.y
    x_range[i] = pos.get_x()
    y_range[i] = pos.get_y()
    
    
    #print("x: ", stage_pos.x, ", y: ", stage_pos.y, "z: ", stage_pos.z)
    print("x: ", x_range[i], ", y: ", y_range[i])
    i = i+1

# pos = pos_list.get_position(2)
# pos.go_to_position(pos, mmc)
# stage_pos = pos.get(0)

#zz = stage_pos.x

nx = abs(round((x_range[1] - x_range[0])/step))
ny = abs(round((y_range[1] - y_range[0])/step))
x = np.zeros((nx*ny))
y = np.zeros((nx*ny))
#z = np.ones((nx*ny))*zz

print("Dx: ", abs(round((x_range[1] - x_range[0]))),
      ", Dy: ", abs(round((y_range[1] - y_range[0]))))
print("nx: ", nx, ", ny: ", ny)
print("N: ", nx*ny, ", ExpTime (min): ", (expo1+200)*nx*ny/60000)

if x_range[1] < x_range[0]:
    ax = np.linspace(x_range[0], x_range[1], num=nx)
else:
    ax = np.linspace(x_range[0], x_range[1], num=nx)

if y_range[1] < y_range[0]:
    ay = np.linspace(y_range[0], y_range[1], num=ny)
else:
    ay = np.linspace(y_range[0], y_range[1], num=ny)


for i in range(ny):
    x[i*nx:(i+1)*nx] = ax
    y[i*nx:(i+1)*nx] = ay[i]


#xyz = np.hstack([x[:, None], y[:, None], z[:, None]])
xy = np.hstack([x[:, None], y[:, None]])
#events = multi_d_acquisition_events(xyz_positions=xyz)
events = multi_d_acquisition_events(xy_positions=xy)

#%%
"""optimizing the angle and voltage"""

if calibrate == 1:    
    cal_ang(plot=True, correct=True, ang_range=1, ang_step = 0.05)
    cal_vol(plot=True, correct=True,vol_range = 20, vol_step = 1, expo2 = 30)

subevents =[events[i:i+sampling] for i in range(0, len(events),sampling)]
flag= False
flag_ang = False



check = []
def hook_fn(image, metadata,bridge, event_queue) :    
    axes=metadata["Axes"] 
    done = (int(axes["position"]) * 100)/(nx * ny)
    done_r = round(done)
    if done_r % 5 == 0:     # Prints progress percentage every 5%
        if done_r not in check:
            check.append(done_r)
            print(round(done, 2), "% Acquired" )
            
        
    if ((int(axes["position"])+1) % sampling)  == 0 or (int(axes["position"]))== (nx * ny)-1:
        global flag
        flag = True
        
    if ((int(axes["position"])+1) % (freq*sampling))  == 0 or (int(axes["position"]))== (nx * ny)-1:
        global flag_ang
        flag_ang = True
        
    return image, metadata

"""Define two acquisition events"""

acq = Acquisition(directory=path, name=name,image_process_fn=hook_fn, show_display= True)
#span = np.arange(vol1[0] - vol_range, vol1[0] + vol_range, vol_step)
flag2 = False       
for item in subevents:
    mmc.set_exposure(expo1)
    acq.acquire(item)
    
    """waiting untill the acquisition batch is finished"""
    
    while not flag:
        time.sleep(0.01)
    
        """Initiate the optimization process"""
        
        
    if flag_ang == True:
        if calibrate == 1:
            cal_ang(plot=False, correct=True, ang_range=1, ang_step = 0.05)
            # cal_vol(plot=False, correct=True,vol_range = 20, vol_step = 1, expo2 = 30)
      
    flag_ang = False     
        
    if flag == True:
        if calibrate == 1:
            # cal_ang(plot=False, correct=True, ang_range=1, ang_step = 0.05)
            cal_vol(plot=False, correct=True,vol_range = 20, vol_step = 1, expo2 = 30)
      
    flag = False  
    
    
      
acq.mark_finished()

"""Save .txt file with the acquisition details"""

direc = name + "_1"
path_note = os.path.join(path, direc, "Full resolution")
f = open("%s/nx=%s ny=%s %sum %sms %s.txt"%(path_note, nx, ny, step, expo1, name), "w")



    
