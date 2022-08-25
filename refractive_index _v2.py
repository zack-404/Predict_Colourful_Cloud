import csv
import numpy as np


def Cauchy_equation(air_pressure,air_temperature,wavelength,relative_humidity):

    T = air_temperature
    w = wavelength
    a = air_pressure
    RH= relative_humidity

    es=6.112*np.exp(17.67*T/(T+243.5))  # saturated vapor

    e = RH*es/100                         # actual vapor pressure

    Mp = 0.662*e/(a-e)                    # mixing ratio at the pressure level, p

    v = -1/986.665*Mp


    return 1+(0.0000776/T)*(1+(0.00752)/w/w)*(a+4810*v/T)


temperature      = []
pressure         = []
refractive_index = []

with open ('csv_file/Pres.csv','r') as csv_file:

    csv_reader=csv.reader(csv_file)

    for line in csv_reader:
        
        for i in line:
            pressure.append(i)


with open ('csv_file/Temp.csv','r') as csv_file:

    csv_reader=csv.reader(csv_file)

    for line in csv_reader:
        
        for i in line:
            temperature.append(i)


for i in range(3899):

    if 'NaN' == temperature[i]:
        temperature[i]  = '-25'

for i in range(3899):

    if 'NaN' == pressure[i]:
        pressure[i]     = '0.17'

for i in range(0,3899):

    air_pressure        =float(pressure[i])
    air_temperature     =float(temperature[i])+273.0
    wavelength          =700*1000.0
    relative_humidity   =0.7

    refractive_index.append(Cauchy_equation(
        air_pressure        = air_pressure,
        air_temperature     = air_temperature,
        relative_humidity   = relative_humidity,
        wavelength          = wavelength
        )
    )


with open ('csv_file/refractivity2.csv','w') as csv_file:
    
    csv_writer=csv.writer(csv_file,delimiter='\n')

    csv_writer.writerow(refractive_index)
