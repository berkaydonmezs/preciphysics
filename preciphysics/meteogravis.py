#!/usr/bin/env python
# coding: utf-8
#                               HEY THERE! WELCOME                                     #
#______________________________________________________________________________________*
#  Preciphysics's meteogravis module offers you to plot the meteogram of the variables #
#                 metegravis contains one Class and its methods                        #
#                      -There are two built-in functions-                              #
#             Given the Dataset, desired Latitude, Longitude and Days                  #
#        Function meteogram_TMSLP plots the Temperature and MSLP variables             #
#    Function meteogram_PRCVS plots the Surface Total Precipitation and Visibility     #
#!                                IMPORTANT NOTES                                     !#
#   Meteogravis currently accept only GFS Dataset to be able to perform the plotting   #
#                          IT IS STILL UNDER DEVELOPMENT                               #
#   Therefore in the near future it will be possible to perform it with any Dataset    #
#______________________________________________________________________________________*


import xarray as xr
import cartopy
import numpy as np
import matplotlib.pyplot as plt

#_____________________________________________________*
#            Defining Class and Functions             #
#_____________________________________________________*
#         Assigning to the dataset variables          #
#_____________________________________________________*

class Meteogravis():
    
    def __init__(self, lat, lon, data):
        """ Expected ; 
        data : GFS Dataset(NetCDF)
        lat  : Latitude in interest
        lon  : Longitude in interest
        """
        self.data = data
        self.lat  = lat
        self.lon  = lon
    
    def meteogram_TMSLP(self, days):
        """ Returns temperature and MSLP meteogram plot.
        Given the data, specified latitude and longitude 
        days : Count of days to plot
        

        NOTE : Temperature given in K, changed to degreeC in the function! 
               Pressure is given in Pa, changed to hPa in the function!
               It may take several seconds to plot the meteogram.
        """
        #_____________________________________________________*
        #                Dataset Mungling Part                #
        #_____________________________________________________*
        self.days = days

        #Assign requested hour counts to a variable 
        day_count = int(self.days)
        try:
            if day_count > 0 and day_count<6 :
                if day_count == 1:
                    sliced = 9
                elif day_count == 2:
                    sliced = 17
                elif day_count == 3:
                    sliced = 25
                elif day_count == 4:
                    sliced = 33
                elif day_count == 5:
                    sliced = 38    
        except: 
            raise ValueError("Please enter days in between 1 and 5")


        # Extract Temperature and MSLP values from the dataset and Specify time range in interest
        temp = self.data['tmpsfc'].sel(time=self.data['tmpsfc']['time'].isel(time=slice(0,sliced)))
        pres = self.data['prmslmsl'].sel(time=self.data['prmslmsl']['time'].isel(time=slice(0,sliced)))
        time = self.data['acpcpsfc']['time'].isel(time=slice(0,sliced))
        initialization = self.data['acpcpsfc']['time'].isel(time=slice(0,sliced))[0].values
        init = str(initialization)[0:-16] + 'Z'

        #Set the Latitude and Longitude given as input 
        pres1 = pres.sel(lon = self.lon, lat = self.lat ).values/100
        temp1 = temp.sel(lon = self.lon, lat = self.lat ).values - 273.15
        time1 = time.values  

        #_____________________________________________________*
        #             Dataset Visualization Part              #
        #_____________________________________________________*

        number_gp = 7
        #_____________________________________________________*
        #Create fig and set ax and customize the plot
        fig = plt.figure(figsize=(13,6))
        ax  = plt.subplot(2,1,1)
        ax.text(0.83, 1.03, 'INIT : {}'.format(init), fontsize=12, transform=ax.transAxes)
        ax.plot(time1, pres1,'bs',color='k')
        ax.plot(time1, pres1,color='green')
        ax.set_ylim(np.min(pres1)-2,np.max(pres1)+2)
        ax.legend(['pressure(mb)'], facecolor='w')
        ax.spines['left'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['bottom'].set_edgecolor('#444444')
        ax.spines['bottom'].set_linewidth(4)
        ax.spines['top'].set_edgecolor('#444444')
        ax.spines['top'].set_linewidth(1)
        ax.grid(linestyle=':', linewidth=0.5)
        ax.set_facecolor('#ebebeb')
        fig.tight_layout()
        plt.title('Mean Sea Level Pressure(MSLP)',fontweight="bold")
        plt.xlabel('Date(month-day-UTC)')
        plt.ylabel('Pressure(mb-hPa)')
    
        #_____________________________________________________*
        #Set ax1 and customize the plot
        ax1 = plt.subplot(2,1,2)
        #ax1.plot(time_smooth, tempp_smooth(hours),'bs')
        ax1.plot(time1, temp1,'o',color='k')
        ax1.plot(time1, temp1,color='red')
        ax1.set_ylim(np.min(temp1)-5,np.max(temp1)+5)
        ax1.legend(['temperature(C)'], facecolor='w')
        ax1.spines['left'].set_visible(False)
        ax1.spines['right'].set_visible(False)
        ax1.spines['bottom'].set_edgecolor('#444444')
        ax1.spines['bottom'].set_linewidth(4)
        ax1.spines['top'].set_edgecolor('#444444')
        ax1.spines['top'].set_linewidth(1)
        ax1.grid(linestyle=':', linewidth=0.5)
        ax1.set_facecolor('#ebebeb')
        plt.title('Temperature(2m)',fontweight="bold")
        plt.xlabel('Date(month-day-UTC)')
        plt.ylabel('Temperature(C)')
        fig.tight_layout()
    
    
    def meteogram_PRCVS(self, days):
        """ Returns Surface Total Precipitation and Visibility meteogram plot.
        Given the data, specified latitude and longitude 
        days : Count of days to plot


        NOTE : Visibility given in m, changed to km in the function! 
               It may take several seconds to plot the meteogram.

        """
        #_____________________________________________________*
        #                Dataset Mungling Part                #
        #_____________________________________________________*

        #Assign requested hour counts to a variable 
        self.days = days
        day_count = int(days)
        try:
            if day_count > 0 and day_count<6 :
                if day_count == 1:
                    sliced = 9
                elif day_count == 2:
                    sliced = 17
                elif day_count == 3:
                    sliced = 25
                elif day_count == 4:
                    sliced = 33
                elif day_count == 5:
                    sliced = 38    
        except: 
            raise ValueError("Please enter days in between 1 and 5")

        # Extract Visibility and Surface Total Precipitation values from the dataset and Specify time range in interest
        vis = self.data['vissfc'].sel(time=self.data['vissfc']['time'].isel(time=slice(0,sliced)))
        prec = self.data['apcpsfc'].sel(time=self.data['apcpsfc']['time'].isel(time=slice(0,sliced)))
        time = self.data['apcpsfc']['time'].isel(time=slice(0,sliced))
        initialization = self.data['apcpsfc']['time'].isel(time=slice(0,sliced))[0].values
        init = str(initialization)[0:-16] + 'Z'

        #Set the Latitude and Longitude given as input 
        vis1 = vis.sel(lon = self.lon, lat = self.lat ).values * (10**-3)
        prec1 = prec.sel(lon = self.lon, lat = self.lat ).values
        time1 = time.values  
        prec1 = np.nan_to_num(prec1)

        #_____________________________________________________*
        #             Dataset Visualization Part              #
        #_____________________________________________________*
        number_gp = 7
        #_____________________________________________________*
        #Create fig and set ax and customize the plot
        fig = plt.figure(figsize=(13,6))
        ax = plt.subplot(2,1,1)
        ax.text(0.83, 1.03, 'INIT : {}'.format(init), fontsize=12, transform=ax.transAxes)
        ax.plot(time1, prec1,'bs',color='k')
        ax.plot(time1, prec1,color='blue')
        ax.set_ylim(np.min(prec1)-2,np.max(prec1)+2)
        ax.legend(['precipitation accumulation(mm)'], facecolor='w')
        ax.spines['left'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['bottom'].set_edgecolor('#444444')
        ax.spines['bottom'].set_linewidth(4)
        ax.spines['top'].set_edgecolor('#444444')
        ax.spines['top'].set_linewidth(1)
        ax.grid(linestyle=':', linewidth=0.5)
        ax.set_facecolor('#ebebeb')
        fig.tight_layout()
        plt.title('Precipitation Accumulation in mm',fontweight="bold")
        plt.xlabel('Date')
        plt.xlabel('Date(month-day-UTC)')
        plt.ylabel('Precipitation(mm)')

        #_____________________________________________________*
        #Set ax1 and customize the plot
        ax1 = plt.subplot(2,1,2)
        ax1.plot(time1, vis1,'o',color='k')
        ax1.plot(time1, vis1,color='pink')
        ax1.set_ylim(np.min(vis1)-1,np.max(vis1)+5)
        ax1.legend(['Visibility(km)'], facecolor='w')
        ax1.spines['left'].set_visible(False)
        ax1.spines['right'].set_visible(False)
        ax1.spines['bottom'].set_edgecolor('#444444')
        ax1.spines['bottom'].set_linewidth(4)
        ax1.spines['top'].set_edgecolor('#444444')
        ax1.spines['top'].set_linewidth(1)
        ax1.grid(linestyle=':', linewidth=0.5)
        ax1.set_facecolor('#ebebeb')
        plt.title('Visibility Surface',fontweight="bold")
        plt.xlabel('Date(month-day-UTC)')
        plt.ylabel('Visibility(km)')
        fig.tight_layout()     

