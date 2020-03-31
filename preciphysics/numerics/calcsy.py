#!/usr/bin/env python
# coding: utf-8




import numpy as np
import matplotlib.pyplot as plt


#====================================================================*
#CALCULATIONS FOR THE USE OF METEOROLOGICAL STUDY AND NUMERICAL MODELS
#____________________________________________________________________*

#Constants for Calculations. 
aT  = 4.0 * 10**-5 # Constant for calculation of 'molecular speed of molecule' using temperature (K.(m^-2).(s^2).mole.(g^-1))
aP  = 0.0342       # Constant for calculation of pressure in an isothermal atmosphere (K.(m'-1))
p0  = 101.325      # Average pressure at surface (kPa)
ro0 = 1.225        # Initial density (kg.(m^-3))
aro = 0.040        # Constant for calculation of density in an isothermal atmosphere (K.(m^-1))
Cp  = 1004.67      # The heat capacity constant for dry air (J.(kg^-1).(K^-1))
Lv  = 2.5 * 10**6  # Laten heating amount for condensation, vapoprization, etc. (K.(kg^-1))
Rd  = 287.0        #
Rv  = 461.0        #
Cp  = 1005.0       #
lapseD = 9.8       # Dry adiabiatic lapse rate (C/km)

#_____________________________________________________________________*
#                        STATE VARIABLES
#_____________________________________________________________________*

#Compute molecular speed using temperature and molecular weight of the specified molecule
def molecular_speed(tmp, molweight):
    """ Returns average random speed of the specified molecules (Vmol)
        tmp  = Temperature of molecules (K) (can be given as array)
        molweight   = Molecular weight of molecules (g/mol)
        Vmol = Average random speed of molecules at specified temperature (m/s)
        aT   = Constant
        
        NOTE : Insert temperature as Degree Celcius(C) ! It will be returned to Kelvin(K) automatically
        """
    Vmol = np.sqrt([np.add(tmp, 273.15) / (np.multiply(aT, molweight))])
    return Vmol


#_____________________________________________________________________*

#Compute pressure in an isothermal atmosphere using temperature  and specified altitude
def pressure_isothermal(tmp, Z):
    """ Returns pressure in kPa  in an isothermal atmosphere on specified altitude (p_isot)
        p_isot = Pressure at specified altitude in an isothermal atmosphere (kPa)
        tmp = Average temperature for the Isothermal Atosphere (K)
        Z   = Altitude at which pressure is to be calculated (meters(m))
        aP  = Constant
        p0  = Average pressure at surface
        
        NOTE : Insert temperature as Degree Celcius(C) ! It will be returned to Kelvin(K) automatically
        NOTE : Insert Z altitude(Z) in kilometers(km) ! 
        
        
    """
    p_isot = p0 * np.exp((aP * -1) / (np.add(tmp, 273.15)) * np.multiply(Z, 10**3))
    return p_isot


#_____________________________________________________________________*

#Compute density in an isothermal atmosphere using temperature and specified altitude
def density_isothermal(tmp, Z):
    """ Returns density in kg.(m^-3) in an isothermal atmosphere on specified altitude (ro_isot)
        ro_isot = Density at specified altitude in ac isothermal atmosphere (kg.(m^-3))
        tmp = Average temperature for the Isothermal Atosphere (K)
        Z   = Altitude at which pressure is to be calculated (meters(m))
        aro = Constant 
        ro0 = Average density initially

        NOTE : Insert temperature as Degree Celcius(C) ! It will be returned to Kelvin(K) automatically
        NOTE : Insert Z altitude(Z) in kilometers(km) ! 


    """
    ro_isot = ro0 * np.exp((aro * -1) / (np.add(tmp, 273.15)) * np.multiply(Z, 10**3))
    return ro_isot


#_____________________________________________________________________*

#Compute virtual temperature using temperature and mixin ratio approximately
def virt_temp(tmp, rv):
    """ Returns Virtual Temperature in K (tmpv)
        virt_tmp = Virtual temperature (K)
        tmp = Temperature (K)
        rv   = Mixing ratio of air approximately (gvapor/gdry)
    
        NOTE : Insert temperature as Degree Celcius(C) ! It will be returned to Kelvin(K) automatically
    
    """
    tmpv = np.add(tmp,273.15) * np.add(1,(np.multiply(0.61, rv)))
    return tmpv


#_____________________________________________________________________*

#Compute sensible heat using density and volume
def sens_heat(tmpi, tmpf, M):
    """ Returns calculated sensible heat in Joule(J) (Qh)
        Qh = Sensible heat (J)
        tmpi = Initial Temperature (K)
        tmpf = Final Temperature (K)
        M    = Mass (kg)
        
        NOTE : Insert temperature as Degree Celcius(C) ! It will be returned to Kelvin(K) automatically
        
    """
    Qh = np.multiply([M * Cp], (np.subtract(np.add(tmpf, 273.15), np.add(tmpi, 273.15))))
    return Qh


#_____________________________________________________________________*

#Compute the heat capacity for moist air using Cp
def heatcap_moist(rv): 
    """ Returns the heat capacity of moist air in (J.(kg^-1).(K^-1)) (Cpv)
        Cpv = The heat capacity for moist air (J.(kg^-1).(K^-1))
        rv  = Mixing ratio of air (gvapor / gdry)
        
        """
    Cpv = np.multiply(Cp, np.add(1, np.multiply(0.84, rv)))
    return Cpv


#_____________________________________________________________________*

#Compute the latent heating
def latent_heat(M):
    """ Returns Latent heat in (J) (Qe)
        Qe  = Laten heating for (Vaporization, Sublimation, Condensation, Fusion, Deposition)  (J)
        M   = Mass of water (kg)
        
    """
    Qe = np.multiply(Lv, M)
    return Qe


#_____________________________________________________________________*

#Compute the potential temperature using temperature and pressure
def theta(tmp, press):
    """ Returns Potential Temperature in (K) (theta)
        theta  = Potential Temperature (K)
        press  = Pressure (Pa)
        tmp    = Temperature (K)
        
        NOTE : Insert temperature as Degree Celcius(C) ! It will be returned to Kelvin(K) automatically
        NOTE : Insert pressure in Pascal(Pa)! 
        
       """
    part1 = np.divide(1000.0, press)
    part2 = part1 ** (np.divide(Rd, Cp))
    theta = np.multiply((tmp + 273.15), part2)
    return theta


#_____________________________________________________________________*

#Compute the potential temperature at a specified altitude using temperature at that altitude
def theta_z(tmpZ, Z):
    """ Returns Potential Temperature in (K) (thetaZ)
        thetaZ = Potential Temperature (K)
        tmpZ   = Temperature at specified altitude (K)
        Z      = Specified altitude (m)
        lapseD = The dry air adiabatic lapse rate (C/km) (K/km)
        
        NOTE : Insert temperature as Degree Celcius(C) ! It will be returned to Kelvin(K) automatically
        NOTE : Insert Z altitude(Z) in kilometers(km) ! 
        
    """
    thetaZ = np.add(tmpZ + 273.15, np.multiply((lapseD * -1), Z ))
    return thetaZ


#_____________________________________________________________________*
#                        HUMIDITY VARIABLES
#_____________________________________________________________________*
