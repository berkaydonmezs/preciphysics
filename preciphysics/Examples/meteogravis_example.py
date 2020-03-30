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

  #_________________________________________________________________________________*
  #      SO LET'S MAKE AN EXAMPLE TO SHOW HOW METEOGRAVIS PERFORMS THE PLOTTING     #
  #          In this Example we will plot the meteogram for the variables;          #
  #           MSLP, Temperature, Surface Total Precipitation, Visibility            #
  #                     For Latitude 45; Longitude 20;                              #
  #                      For the Time Range of 1 Days                               #
  #_________________________________________________________________________________*

#              PROCESS 1                    #
#FIRST WE SHOULD IMPORT THE NECESSARY MODULES
from .visjobs.visjobs.datas import get_data
from preciphysics.preciphysics import meteogravis

#                                PROCESS 2                                        #
#_________________________________________________________________________________*
#   Getting the GFS data using visjobs's get_data module's pick_data function     #
#_________________________________________________________________________________*

# Function exports the GFS dataset initialized at 2020-03-24-12 UTC extending forward 5 days.
# Go to https://github.com/donmezk/visjobs for further explanation about getting the data
data = get_data.pick_data(year = '2020', month = '03', day = '24', hour = '12', latest = False, model = 'GFS')

#                                 PROCESS 3                                        #
#__________________________________________________________________________________*
#Assigning meteogravis module's class Meteogravis to an object to be able to use it#
#__________________________________________________________________________________*

# Expected parameters are entered into class Meteogravis
mtg = Meteogravis(lat = 45, lon = 20, data = data)

#                                PROCESS 4                                        #
#_________________________________________________________________________________*
#          Now its time to use Meteogravis's built-in Functions to plot           #
#_________________________________________________________________________________*

# meteogram_TMSLP() function extracts temperature and MSLP variables from the dataset
# There is only one expected parameter which is: days
# days parameter corresponds to the count of days to be plotted in meteogram
mtg.meteogram_TMSLP(days = 1)

#   PROCESS 5   #
# meteogram_PRCVS() function extracts Surface total Precipitation and Visibility variables from the dataset
# There is also one expected parameter which is: days
# days parameter corresponds to the count of days to be plotted in meteogram
mtg.meteogram_PRCVS(days = 1)

