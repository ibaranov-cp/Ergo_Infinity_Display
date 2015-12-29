#!/usr/bin/env python

# Author: Ilia Baranov

import wmi
import os 

w = wmi.WMI(namespace='root\\wmi')
print (w.MSAcpi_ThermalZoneTemperature()[0].CurrentTemperature/10.0)-273.15

