# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 10:54:56 2023

@author: mahta
"""

#import    
import os    

import pandas as pd    
# specify the current working directory
os.chdir('C:/Users/mahta/OneDrive - University of Stirling/Erken_GOTM_simulations/4models/isimip2b_gotm_erken/gfdl-esm2m')

#%%Reading Netcdf file


import netCDF4 as nc

from scipy.io import netcdf  

#file direction
gfdl_his= 'C:/Users/mahta/OneDrive - University of Stirling/Erken_GOTM_simulations/4models/isimip2b_gotm_erken/gfdl-esm2m/isimip_gotm_erken_gfdl_historical.nc'

#gfdl_pic= 'C:/Users/mahta/OneDrive - University of Stirling/Erken_GOTM_simulations/4models/isimip2b_gotm_erken/gfdl-esm2m/isimip_gotm_erken_gfdl_picontrol.nc'

gfdl_rcp26= 'C:/Users/mahta/OneDrive - University of Stirling/Erken_GOTM_simulations/4models/isimip2b_gotm_erken/gfdl-esm2m/isimip_gotm_erken_gfdl_rcp26.nc'

gfdl_rcp60= 'C:/Users/mahta/OneDrive - University of Stirling/Erken_GOTM_simulations/4models/isimip2b_gotm_erken/gfdl-esm2m/isimip_gotm_erken_gfdl_rcp60.nc'

#gfdl_rcp85= 'C:/Users/mahta/OneDrive - University of Stirling/Erken_GOTM_simulations/4models/isimip2b_gotm_erken/gfdl-esm2m/isimip2b_gotm_erken_gfld_rcp85.nc'

gfdl_rcp85= 'C:/Users/mahta/OneDrive - University of Stirling/Erken_GOTM_simulations/4models/isimip2b_gotm_erken/gfdl-esm2m/isimip2b_gotm_erken_gfdl_rcp85_correct.nc'

#transfering into datasets 

dataset_gfdl_his  = netcdf.netcdf_file(gfdl_his,'r')
#dataset_gfdl_pic = netcdf.netcdf_file(gfdl_pic,'r')
dataset_gfdl_rcp26  = netcdf.netcdf_file(gfdl_rcp26,'r')
dataset_gfdl_rcp60  = netcdf.netcdf_file(gfdl_rcp60,'r')
dataset_gfdl_rcp85  = netcdf.netcdf_file(gfdl_rcp85,'r')

#%%depth variable and geogharphical location 


import numpy as np
from datetime import datetime, timedelta
import netCDF4
netCDF4.num2date



lat=dataset_gfdl_his.variables['lat'][:]
print (lat)#[59.6]

lon=dataset_gfdl_his.variables['lon'][:]
print (lon)#[18.6]


z_bnd_gotm= dataset_gfdl_his.variables['zi'][:]
unique_z_bnd_gotm = np.unique(z_bnd_gotm)
print(unique_z_bnd_gotm)

"""
[-2.100000e+01 -2.050000e+01 -2.000000e+01 -1.950000e+01 -1.900000e+01
 -1.850000e+01 -1.800000e+01 -1.750000e+01 -1.700000e+01 -1.650000e+01
 -1.600000e+01 -1.550000e+01 -1.500000e+01 -1.450000e+01 -1.400000e+01
 -1.350000e+01 -1.300000e+01 -1.250000e+01 -1.200000e+01 -1.150000e+01
 -1.100000e+01 -1.050000e+01 -1.000000e+01 -9.500000e+00 -9.000000e+00
 -8.500000e+00 -8.000000e+00 -7.500000e+00 -7.000000e+00 -6.500000e+00
 -6.000000e+00 -5.500000e+00 -5.000000e+00 -4.500000e+00 -4.000000e+00
 -3.500000e+00 -3.000000e+00 -2.500000e+00 -2.000000e+00 -1.500000e+00
 -1.000000e+00 -5.000000e-01  9.103829e-15]

"""
print(np.around(unique_z_bnd_gotm, decimals=1))

"""
array([-21. , -20.5, -20. , -19.5, -19. , -18.5, -18. , -17.5, -17. ,
       -16.5, -16. , -15.5, -15. , -14.5, -14. , -13.5, -13. , -12.5,
       -12. , -11.5, -11. , -10.5, -10. ,  -9.5,  -9. ,  -8.5,  -8. ,
        -7.5,  -7. ,  -6.5,  -6. ,  -5.5,  -5. ,  -4.5,  -4. ,  -3.5,
        -3. ,  -2.5,  -2. ,  -1.5,  -1. ,  -0.5,   0. ], dtype=float32

"""


z_m_gotm= dataset_gfdl_his.variables['z'][:]
unique_z_m_gotm = np.unique(z_m_gotm)
print(unique_z_m_gotm)
"""
[-20.75 -20.25 -19.75 -19.25 -18.75 -18.25 -17.75 -17.25 -16.75 -16.25
 -15.75 -15.25 -14.75 -14.25 -13.75 -13.25 -12.75 -12.25 -11.75 -11.25
 -10.75 -10.25  -9.75  -9.25  -8.75  -8.25  -7.75  -7.25  -6.75  -6.25
  -5.75  -5.25  -4.75  -4.25  -3.75  -3.25  -2.75  -2.25  -1.75  -1.25
  -0.75  -0.25]

"""
#%%Reading temp and Kz , time  :
  
#%%1   _gfdl_his    
  
temp_gfdl_his=dataset_gfdl_his.variables['temp'][:]
temp_gfdl_his_full_prof_gotmgrid=temp_gfdl_his[: , : , 0 , 0]# the first and scond dimentions are time and depth , the third and forth are lon and lat 

kz_gfdl_his= dataset_gfdl_his.variables['avh'][:]
kz_gfdl_his_full_prof_gotmgrid=kz_gfdl_his[: , : , 0 , 0]


time_variable_gfdl_his = dataset_gfdl_his.variables['time']
time_units_str_gfdl_his = time_variable_gfdl_his.units.decode()  # Convert bytes to string
time_units_gfdl_his, _, reference_time_str_gfdl_his = time_units_str_gfdl_his.partition(' since ')

# Convert reference_time_str to datetime object
reference_time_gfdl_his = datetime.strptime(reference_time_str_gfdl_his, '%Y-%m-%d %H:%M:%S')

# Convert numerical values to datetime objects
time_in_seconds_gfdl_his = time_variable_gfdl_his[:]
time_in_datetime_gfdl_his = [reference_time_gfdl_his + timedelta(seconds=int(t)) for t in time_in_seconds_gfdl_his]

# Convert time_in_datetime to a NumPy array
time_in_datetime_array_gfdl_his = np.array(time_in_datetime_gfdl_his)

# Format datetime objects as strings
formatted_time_list_gfdl_his = [dt.strftime("%Y-%m-%d") for dt in time_in_datetime_array_gfdl_his]
# Convert the formatted_time strings back to datetime objects
formatted_time_datetime_gfdl_his = [datetime.strptime(time_str, "%Y-%m-%d") for time_str in formatted_time_list_gfdl_his]

#%%2   _gfdl_pic
"""
temp_gfdl_pic=dataset_gfdl_pic.variables['temp'][:]
temp_gfdl_pic_full_prof_gotmgrid=temp_gfdl_pic[: , : , 0 , 0]# the first and scond dimentions are time and depth , the third and forth are lon and lat 

kz_gfdl_pic= dataset_gfdl_pic.variables['avh'][:]
kz_gfdl_pic_full_prof_gotmgrid=kz_gfdl_pic[: , : , 0 , 0]


time_variable_gfdl_pic = dataset_gfdl_pic.variables['time']
time_units_str_gfdl_pic = time_variable_gfdl_pic.units.decode()  # Convert bytes to string
time_units_gfdl_pic, _, reference_time_str_gfdl_pic = time_units_str_gfdl_pic.partition(' since ')

# Convert reference_time_str to datetime object
reference_time_gfdl_pic = datetime.strptime(reference_time_str_gfdl_pic, '%Y-%m-%d %H:%M:%S')

# Convert numerical values to datetime objects
time_in_seconds_gfdl_pic = time_variable_gfdl_pic[:]
time_in_datetime_gfdl_pic = [reference_time_gfdl_pic + timedelta(seconds=int(t)) for t in time_in_seconds_gfdl_pic]

# Convert time_in_datetime to a NumPy array
time_in_datetime_array_gfdl_pic = np.array(time_in_datetime_gfdl_pic)

# Format datetime objects as strings
formatted_time_list_gfdl_pic = [dt.strftime("%Y-%m-%d") for dt in time_in_datetime_array_gfdl_pic]
# Convert the formatted_time strings back to datetime objects
formatted_time_datetime_gfdl_pic = [datetime.strptime(time_str, "%Y-%m-%d") for time_str in formatted_time_list_gfdl_pic]
"""

#%%3.      gfdl_rcp26

temp_gfdl_rcp26=dataset_gfdl_rcp26.variables['temp'][:]
temp_gfdl_rcp26_full_prof_gotmgrid=temp_gfdl_rcp26[: , : , 0 , 0]# the first and scond dimentions are time and depth , the third and forth are lon and lat 

kz_gfdl_rcp26= dataset_gfdl_rcp26.variables['avh'][:]
kz_gfdl_rcp26_full_prof_gotmgrid=kz_gfdl_rcp26[: , : , 0 , 0]


time_variable_gfdl_rcp26 = dataset_gfdl_rcp26.variables['time']
time_units_str_gfdl_rcp26 = time_variable_gfdl_rcp26.units.decode()  # Convert bytes to string
time_units_gfdl_rcp26, _, reference_time_str_gfdl_rcp26 = time_units_str_gfdl_rcp26.partition(' since ')

# Convert reference_time_str to datetime object
reference_time_gfdl_rcp26 = datetime.strptime(reference_time_str_gfdl_rcp26, '%Y-%m-%d %H:%M:%S')

# Convert numerical values to datetime objects
time_in_seconds_gfdl_rcp26 = time_variable_gfdl_rcp26[:]
time_in_datetime_gfdl_rcp26 = [reference_time_gfdl_rcp26 + timedelta(seconds=int(t)) for t in time_in_seconds_gfdl_rcp26]

# Convert time_in_datetime to a NumPy array
time_in_datetime_array_gfdl_rcp26 = np.array(time_in_datetime_gfdl_rcp26)

# Format datetime objects as strings
formatted_time_list_gfdl_rcp26 = [dt.strftime("%Y-%m-%d") for dt in time_in_datetime_array_gfdl_rcp26]
# Convert the formatted_time strings back to datetime objects
formatted_time_datetime_gfdl_rcp26 = [datetime.strptime(time_str, "%Y-%m-%d") for time_str in formatted_time_list_gfdl_rcp26]



#%%4.      gfdl_rcp60

temp_gfdl_rcp60=dataset_gfdl_rcp60.variables['temp'][:]
temp_gfdl_rcp60_full_prof_gotmgrid=temp_gfdl_rcp60[: , : , 0 , 0]# the first and scond dimentions are time and depth , the third and forth are lon and lat 

kz_gfdl_rcp60= dataset_gfdl_rcp60.variables['avh'][:]
kz_gfdl_rcp60_full_prof_gotmgrid=kz_gfdl_rcp60[: , : , 0 , 0]


time_variable_gfdl_rcp60 = dataset_gfdl_rcp60.variables['time']
time_units_str_gfdl_rcp60 = time_variable_gfdl_rcp60.units.decode()  # Convert bytes to string
time_units_gfdl_rcp60, _, reference_time_str_gfdl_rcp60 = time_units_str_gfdl_rcp60.partition(' since ')

# Convert reference_time_str to datetime object
reference_time_gfdl_rcp60 = datetime.strptime(reference_time_str_gfdl_rcp60, '%Y-%m-%d %H:%M:%S')

# Convert numerical values to datetime objects
time_in_seconds_gfdl_rcp60 = time_variable_gfdl_rcp60[:]
time_in_datetime_gfdl_rcp60 = [reference_time_gfdl_rcp60 + timedelta(seconds=int(t)) for t in time_in_seconds_gfdl_rcp60]

# Convert time_in_datetime to a NumPy array
time_in_datetime_array_gfdl_rcp60 = np.array(time_in_datetime_gfdl_rcp60)

# Format datetime objects as strings
formatted_time_list_gfdl_rcp60 = [dt.strftime("%Y-%m-%d") for dt in time_in_datetime_array_gfdl_rcp60]
# Convert the formatted_time strings back to datetime objects
formatted_time_datetime_gfdl_rcp60 = [datetime.strptime(time_str, "%Y-%m-%d") for time_str in formatted_time_list_gfdl_rcp60]


#%%5.      gfdl_rcp85

temp_gfdl_rcp85=dataset_gfdl_rcp85.variables['temp'][:]
temp_gfdl_rcp85_full_prof_gotmgrid=temp_gfdl_rcp85[: , : , 0 , 0]# the first and scond dimentions are time and depth , the third and forth are lon and lat 

kz_gfdl_rcp85= dataset_gfdl_rcp85.variables['avh'][:]
kz_gfdl_rcp85_full_prof_gotmgrid=kz_gfdl_rcp85[: , : , 0 , 0]


time_variable_gfdl_rcp85 = dataset_gfdl_rcp85.variables['time']
time_units_str_gfdl_rcp85 = time_variable_gfdl_rcp85.units.decode()  # Convert bytes to string
time_units_gfdl_rcp85, _, reference_time_str_gfdl_rcp85 = time_units_str_gfdl_rcp85.partition(' since ')

# Convert reference_time_str to datetime object
reference_time_gfdl_rcp85 = datetime.strptime(reference_time_str_gfdl_rcp85, '%Y-%m-%d %H:%M:%S')

# Convert numerical values to datetime objects
time_in_seconds_gfdl_rcp85 = time_variable_gfdl_rcp85[:]
time_in_datetime_gfdl_rcp85 = [reference_time_gfdl_rcp85 + timedelta(seconds=int(t)) for t in time_in_seconds_gfdl_rcp85]

# Convert time_in_datetime to a NumPy array
time_in_datetime_array_gfdl_rcp85 = np.array(time_in_datetime_gfdl_rcp85)

# Format datetime objects as strings
formatted_time_list_gfdl_rcp85 = [dt.strftime("%Y-%m-%d") for dt in time_in_datetime_array_gfdl_rcp85]
# Convert the formatted_time strings back to datetime objects
formatted_time_datetime_gfdl_rcp85 = [datetime.strptime(time_str, "%Y-%m-%d") for time_str in formatted_time_list_gfdl_rcp85]


#%%general giuldness about ncdf files:
"""
#1. Access variables # example of using below
var_name = "variable_name"
data = dataset.variables[var_name][:]  # This will read the entire data from the variable

#2. Access number of dimensions
dim_name = "dimension_name"
dim_data = dataset.dimensions[dim_name]


dataset.dimensions['zi']
Out[353]: 43

dataset.dimensions['z']
Out[353]: 42

#3.?! Access attributes # tested for erken it seems it dosnt work
#AttributeError: 'netcdf_file' object has no attribute 'getncattr'
attr_name = "attribute_name"
attr_value = dataset.getncattr(attr_name)

"""

#%%reading the depth of each layer _first attemt 
"""
import numpy as np
from datetime import datetime, timedelta
import netCDF4
netCDF4.num2date



lat=dataset.variables['lat'][:]
print (lat)#[59.6]

lon=dataset.variables['lon'][:]
print (lon)#[18.6]


z_bnd_gotm= dataset.variables['zi'][:]
unique_z_bnd_gotm = np.unique(z_bnd_gotm)
print(unique_z_bnd_gotm)

"""
[-2.100000e+01 -2.050000e+01 -2.000000e+01 -1.950000e+01 -1.900000e+01
 -1.850000e+01 -1.800000e+01 -1.750000e+01 -1.700000e+01 -1.650000e+01
 -1.600000e+01 -1.550000e+01 -1.500000e+01 -1.450000e+01 -1.400000e+01
 -1.350000e+01 -1.300000e+01 -1.250000e+01 -1.200000e+01 -1.150000e+01
 -1.100000e+01 -1.050000e+01 -1.000000e+01 -9.500000e+00 -9.000000e+00
 -8.500000e+00 -8.000000e+00 -7.500000e+00 -7.000000e+00 -6.500000e+00
 -6.000000e+00 -5.500000e+00 -5.000000e+00 -4.500000e+00 -4.000000e+00
 -3.500000e+00 -3.000000e+00 -2.500000e+00 -2.000000e+00 -1.500000e+00
 -1.000000e+00 -5.000000e-01  9.103829e-15]

"""
print(np.around(unique_z_bnd_gotm, decimals=1))

"""
array([-21. , -20.5, -20. , -19.5, -19. , -18.5, -18. , -17.5, -17. ,
       -16.5, -16. , -15.5, -15. , -14.5, -14. , -13.5, -13. , -12.5,
       -12. , -11.5, -11. , -10.5, -10. ,  -9.5,  -9. ,  -8.5,  -8. ,
        -7.5,  -7. ,  -6.5,  -6. ,  -5.5,  -5. ,  -4.5,  -4. ,  -3.5,
        -3. ,  -2.5,  -2. ,  -1.5,  -1. ,  -0.5,   0. ], dtype=float32

"""


z_m_gotm= dataset.variables['z'][:]
unique_z_m_gotm = np.unique(z_m_gotm)
print(unique_z_m_gotm)

"""
[-20.75 -20.25 -19.75 -19.25 -18.75 -18.25 -17.75 -17.25 -16.75 -16.25
 -15.75 -15.25 -14.75 -14.25 -13.75 -13.25 -12.75 -12.25 -11.75 -11.25
 -10.75 -10.25  -9.75  -9.25  -8.75  -8.25  -7.75  -7.25  -6.75  -6.25
  -5.75  -5.25  -4.75  -4.25  -3.75  -3.25  -2.75  -2.25  -1.75  -1.25
  -0.75  -0.25]
"""
#You can see the gotm grid of Z_m_gotm is not equal to Z_m_obsgrid:
# get average for each two in row     
"""    
#%%first simple source code for raeding temp and kz full prof and time steps
"""
#temp
temp_gotm= dataset.variables['temp'][:]
temp_gotm_full_prof_gotmgrid=temp_gotm[: , : , 0 , 0]# the first and scond dimentions are time and depth , the third and forth are lon and lat 

#kz
kz_gotm= dataset.variables['avh'][:]
kz_gotm_full_prof_gotmgrid=kz_gotm[: , : , 0 , 0]


#testing this:
#kz_gotmgrid_hypo_revers=kz_gotm_full_prof_gotmgrid[ :, :14]
#kz_gotmgrid_hypo= kz_gotm_full_prof_gotmgrid[ :, 13::-1]
#time_variable = dataset.variables['time'][:]


# Assuming the time variable is named 'time'
time_variable = dataset.variables['time']

# Extract time units and reference time from the time_variable.units
time_units_str = time_variable.units.decode()  # Convert bytes to string
time_units, _, reference_time_str = time_units_str.partition(' since ')

# Convert reference_time_str to datetime object
reference_time = datetime.strptime(reference_time_str, '%Y-%m-%d %H:%M:%S')

# Convert numerical values to datetime objects
time_in_seconds = time_variable[:]
time_in_datetime = [reference_time + timedelta(seconds=int(t)) for t in time_in_seconds]

# Convert time_in_datetime to a NumPy array
time_in_datetime_array = np.array(time_in_datetime)

# Format datetime objects as strings
formatted_time_list = [dt.strftime("%Y-%m-%d") for dt in time_in_datetime_array]
# Convert the formatted_time strings back to datetime objects
formatted_time_datetime = [datetime.strptime(time_str, "%Y-%m-%d") for time_str in formatted_time_list]
"""
#%% GOTM grid morphology
from scipy.interpolate import interp1d

df_morphro
bath



# Make sure the lengths match
formatted_array = np.around(unique_z_bnd_gotm, decimals=3)
z_values = bath['Z(m)']  # Use the 'Z(m)' column from the DataFrame

# Create interpolation functions for each column
interpolated_columns = {}
for column in bath.columns:
    if column != 'Z(m)':
        interp_func = interp1d(z_values, bath[column], kind='linear', fill_value='interpolate')
        interpolated_columns[column] = interp_func(formatted_array)

# Create a new DataFrame with interpolated values
interpolated_bath = pd.DataFrame(interpolated_columns)

# Add the 'Z(m)' column
interpolated_bath['Z_up_bnd'] = formatted_array
interpolated_bath['Z_m'] = np.append (np.nan, unique_z_m_gotm )

interpolated_bath['V_r']=np.append (0 , np.diff(interpolated_bath['V_cum']))
interpolated_bath['A_l']=np.append (0 , np.diff(interpolated_bath['A_cum']))
interpolated_bath['A_s']=interpolated_bath['A_cum'].copy()

#%%surface an hypo top layer

np.where(unique_z_m_gotm == -13.75)#14
np.where(unique_z_m_gotm == -0.25)#41# the shape is 42 
np.where(unique_z_m_gotm == -1.25)#39
np.where(unique_z_m_gotm == -20.75)#0

#%% original code for surf and hypo seperation :
"""
tem_gotm_surf=temp_gotm_full_prof_gotmgrid[: , 41]
tem_gotm_top_hypo= temp_gotm_full_prof_gotmgrid[: , 14]
tem_gotm_1m= temp_gotm_full_prof_gotmgrid[: , 39]
temp_gotm_hypo= temp_gotm_full_prof_gotmgrid[: , 0:14]
"""
#%%his
kz_gfdl_his_full_prof_gotmgrid
temp_gfdl_his_full_prof_gotmgrid

tem_gfdl_his_surf=temp_gfdl_his_full_prof_gotmgrid[: , 41]
tem_gfdl_his_top_hypo= temp_gfdl_his_full_prof_gotmgrid[: , 14]
tem_gfdl_his_1m= temp_gfdl_his_full_prof_gotmgrid[: , 39]
temp_gfdl_his_hypo= temp_gfdl_his_full_prof_gotmgrid[: , 0:14]


density_gfdl_his_surf=Lab_Density(tem_gfdl_his_surf)
density_gfdl_his_1m=Lab_Density(tem_gfdl_his_1m)
density_gfdl_his_top_hypo=Lab_Density(tem_gfdl_his_top_hypo)


density_difference_surf_top_hypo_gfdl_his=density_gfdl_his_surf -density_gfdl_his_top_hypo
density_difference_1m_top_hypo_gfdl_his=density_gfdl_his_1m-density_gfdl_his_top_hypo
# Convert formatted_time_datetime to a pandas Series or NumPy array
formatted_time_series_gfdl_his = pd.Series(formatted_time_datetime_gfdl_his)  # or np.array(formatted_time_datetime)

# Create the DataFrame with temp_diff_gotm_obsgrid_top_135 as the data and formatted_time_series as the index
formatted_time_series_gfdl_his = pd.Series(formatted_time_datetime_gfdl_his)



density_difference_surf_top_hypo_gfdl_his_indexed = pd.Series(density_difference_surf_top_hypo_gfdl_his, index=pd.to_datetime(formatted_time_series_gfdl_his))
density_difference_surf_top_hypo_gfdl_his_indexed.index.name = 'Datetime'


density_difference_1m_top_hypo_gfdl_his_indexed = pd.Series(density_difference_1m_top_hypo_gfdl_his, index=pd.to_datetime(formatted_time_series_gfdl_his))
density_difference_1m_top_hypo_gfdl_his_indexed.index.name = 'Datetime'

#%%pi# starting date: 1661 end 2099 the minimum date of pi control is lower than datetime.min() 
#print(pd.Timestamp.min)
#1677-09-21 00:12:43.145224193
"""
kz_gfdl_pic_full_prof_gotmgrid
temp_gfdl_pic_full_prof_gotmgrid

tem_gfdl_pic_surf=temp_gfdl_pic_full_prof_gotmgrid[: , 41]
tem_gfdl_pic_top_hypo= temp_gfdl_pic_full_prof_gotmgrid[: , 14]
tem_gfdl_pic_1m= temp_gfdl_pic_full_prof_gotmgrid[: , 39]
temp_gfdl_pic_hypo= temp_gfdl_pic_full_prof_gotmgrid[: , 0:14]


density_gfdl_pic_surf=Lab_Density(tem_gfdl_pic_surf)
density_gfdl_pic_1m=Lab_Density(tem_gfdl_pic_1m)
density_gfdl_pic_top_hypo=Lab_Density(tem_gfdl_pic_top_hypo)


density_difference_surf_top_hypo_gfdl_pic=density_gfdl_pic_surf -density_gfdl_pic_top_hypo
density_difference_1m_top_hypo_gfdl_pic=density_gfdl_pic_1m-density_gfdl_pic_top_hypo
# Convert formatted_time_datetime to a pandas Series or NumPy array
formatted_time_series_gfdl_pic = pd.Series(formatted_time_datetime_gfdl_pic)  # or np.array(formatted_time_datetime)

# Create the DataFrame with temp_diff_gotm_obsgrid_top_135 as the data and formatted_time_series as the index
formatted_time_series_gfdl_pic = pd.Series(formatted_time_datetime_gfdl_pic)



density_difference_surf_top_hypo_gfdl_pic_indexed = pd.Series(density_difference_surf_top_hypo_gfdl_pic, index=pd.to_datetime(formatted_time_series_gfdl_pic ,errors = 'coerce'))
density_difference_surf_top_hypo_gfdl_pic_indexed.index.name = 'Datetime'


density_difference_1m_top_hypo_gfdl_pic_indexed = pd.Series(density_difference_1m_top_hypo_gfdl_pic, index=pd.to_datetime(formatted_time_series_gfdl_pic,errors = 'coerce'))
density_difference_surf_top_hypo_gfdl_pic_indexed.index.name = 'Datetime'
density_difference_1m_top_hypo_gfdl_pic_indexed.index.name = 'Datetime'
"""

#%%rcp26
kz_gfdl_rcp26_full_prof_gotmgrid
temp_gfdl_rcp26_full_prof_gotmgrid

tem_gfdl_rcp26_surf=temp_gfdl_rcp26_full_prof_gotmgrid[: , 41]
tem_gfdl_rcp26_top_hypo= temp_gfdl_rcp26_full_prof_gotmgrid[: , 14]
tem_gfdl_rcp26_1m= temp_gfdl_rcp26_full_prof_gotmgrid[: , 39]
temp_gfdl_rcp26_hypo= temp_gfdl_rcp26_full_prof_gotmgrid[: , 0:14]


density_gfdl_rcp26_surf=Lab_Density(tem_gfdl_rcp26_surf)
density_gfdl_rcp26_1m=Lab_Density(tem_gfdl_rcp26_1m)
density_gfdl_rcp26_top_hypo=Lab_Density(tem_gfdl_rcp26_top_hypo)


density_difference_surf_top_hypo_gfdl_rcp26=density_gfdl_rcp26_surf -density_gfdl_rcp26_top_hypo
density_difference_1m_top_hypo_gfdl_rcp26=density_gfdl_rcp26_1m-density_gfdl_rcp26_top_hypo
# Convert formatted_time_datetime to a pandas Series or NumPy array
formatted_time_series_gfdl_rcp26 = pd.Series(formatted_time_datetime_gfdl_rcp26)  # or np.array(formatted_time_datetime)

# Create the DataFrame with temp_diff_gotm_obsgrid_top_135 as the data and formatted_time_series as the index
formatted_time_series_gfdl_rcp26 = pd.Series(formatted_time_datetime_gfdl_rcp26)



density_difference_surf_top_hypo_gfdl_rcp26_indexed = pd.Series(density_difference_surf_top_hypo_gfdl_rcp26, index=pd.to_datetime(formatted_time_series_gfdl_rcp26))
density_difference_surf_top_hypo_gfdl_rcp26_indexed.index.name = 'Datetime'


density_difference_1m_top_hypo_gfdl_rcp26_indexed = pd.Series(density_difference_1m_top_hypo_gfdl_rcp26, index=pd.to_datetime(formatted_time_series_gfdl_rcp26))
density_difference_1m_top_hypo_gfdl_rcp26_indexed.index.name = 'Datetime'

#%%rcp60
kz_gfdl_rcp60_full_prof_gotmgrid
temp_gfdl_rcp60_full_prof_gotmgrid

tem_gfdl_rcp60_surf=temp_gfdl_rcp60_full_prof_gotmgrid[: , 41]
tem_gfdl_rcp60_top_hypo= temp_gfdl_rcp60_full_prof_gotmgrid[: , 14]
tem_gfdl_rcp60_1m= temp_gfdl_rcp60_full_prof_gotmgrid[: , 39]
temp_gfdl_rcp60_hypo= temp_gfdl_rcp60_full_prof_gotmgrid[: , 0:14]


density_gfdl_rcp60_surf=Lab_Density(tem_gfdl_rcp60_surf)
density_gfdl_rcp60_1m=Lab_Density(tem_gfdl_rcp60_1m)
density_gfdl_rcp60_top_hypo=Lab_Density(tem_gfdl_rcp60_top_hypo)


density_difference_surf_top_hypo_gfdl_rcp60=density_gfdl_rcp60_surf -density_gfdl_rcp60_top_hypo
density_difference_1m_top_hypo_gfdl_rcp60=density_gfdl_rcp60_1m-density_gfdl_rcp60_top_hypo
# Convert formatted_time_datetime to a pandas Series or NumPy array
formatted_time_series_gfdl_rcp60 = pd.Series(formatted_time_datetime_gfdl_rcp60)  # or np.array(formatted_time_datetime)

# Create the DataFrame with temp_diff_gotm_obsgrid_top_135 as the data and formatted_time_series as the index
formatted_time_series_gfdl_rcp60 = pd.Series(formatted_time_datetime_gfdl_rcp60)



density_difference_surf_top_hypo_gfdl_rcp60_indexed = pd.Series(density_difference_surf_top_hypo_gfdl_rcp60, index=pd.to_datetime(formatted_time_series_gfdl_rcp60))
density_difference_surf_top_hypo_gfdl_rcp60_indexed.index.name = 'Datetime'


density_difference_1m_top_hypo_gfdl_rcp60_indexed = pd.Series(density_difference_1m_top_hypo_gfdl_rcp60, index=pd.to_datetime(formatted_time_series_gfdl_rcp60))
density_difference_1m_top_hypo_gfdl_rcp60_indexed.index.name = 'Datetime'




#%%rcp85
kz_gfdl_rcp85_full_prof_gotmgrid
temp_gfdl_rcp85_full_prof_gotmgrid

tem_gfdl_rcp85_surf=temp_gfdl_rcp85_full_prof_gotmgrid[: , 41]
tem_gfdl_rcp85_top_hypo= temp_gfdl_rcp85_full_prof_gotmgrid[: , 14]
tem_gfdl_rcp85_1m= temp_gfdl_rcp85_full_prof_gotmgrid[: , 39]
temp_gfdl_rcp85_hypo= temp_gfdl_rcp85_full_prof_gotmgrid[: , 0:14]


density_gfdl_rcp85_surf=Lab_Density(tem_gfdl_rcp85_surf)
density_gfdl_rcp85_1m=Lab_Density(tem_gfdl_rcp85_1m)
density_gfdl_rcp85_top_hypo=Lab_Density(tem_gfdl_rcp85_top_hypo)


density_difference_surf_top_hypo_gfdl_rcp85=density_gfdl_rcp85_surf -density_gfdl_rcp85_top_hypo
density_difference_1m_top_hypo_gfdl_rcp85=density_gfdl_rcp85_1m-density_gfdl_rcp85_top_hypo
# Convert formatted_time_datetime to a pandas Series or NumPy array
formatted_time_series_gfdl_rcp85 = pd.Series(formatted_time_datetime_gfdl_rcp85)  # or np.array(formatted_time_datetime)

# Create the DataFrame with temp_diff_gotm_obsgrid_top_135 as the data and formatted_time_series as the index
formatted_time_series_gfdl_rcp85 = pd.Series(formatted_time_datetime_gfdl_rcp85)



density_difference_surf_top_hypo_gfdl_rcp85_indexed = pd.Series(density_difference_surf_top_hypo_gfdl_rcp85, index=pd.to_datetime(formatted_time_series_gfdl_rcp85))
density_difference_surf_top_hypo_gfdl_rcp85_indexed.index.name = 'Datetime'


density_difference_1m_top_hypo_gfdl_rcp85_indexed = pd.Series(density_difference_1m_top_hypo_gfdl_rcp85, index=pd.to_datetime(formatted_time_series_gfdl_rcp85))
density_difference_1m_top_hypo_gfdl_rcp85_indexed.index.name = 'Datetime'


#%%Resahping from top to bottom 
#%%his

kz_gfdl_his_full_prof_gotmgrid
temp_gfdl_his_full_prof_gotmgrid


temp_gfdl_his_full_prof_TB=temp_gfdl_his_full_prof_gotmgrid[: , ::-1 ]

kz_gfdl_his_full_prof_TB=kz_gfdl_his_full_prof_gotmgrid[: , ::-1 ]

 
unique_z_m_gotm_TB=unique_z_m_gotm[::-1]

np.where(unique_z_m_gotm_TB == -13.75)#27
np.where(unique_z_m_gotm_TB == -14.25)#28
np.where(unique_z_m_gotm_TB == -17.25)#34
np.where(unique_z_m_gotm_TB == -0.25)#0
np.where(unique_z_m_gotm_TB == -1.25)#2




temp_gfdl_his_hypo_TB =temp_gfdl_his_full_prof_TB[:  ,28: ]#  14.25m-20.75m
temp_gfdl_his_meta= temp_gfdl_his_full_prof_TB[:  , 27 ]# 13.75m 

kz_gfdl_his_hypo_TB =kz_gfdl_his_full_prof_TB[:  , 28: ]# 14.25m-20.75m

kz_gfdl_his_hypo_T17 =kz_gfdl_his_full_prof_TB[:  , 28:35 ]# 14.25m-17.25m(34+1)

#%%pic
"""
kz_gfdl_pic_full_prof_gotmgrid
temp_gfdl_pic_full_prof_gotmgrid


temp_gfdl_pic_full_prof_TB=temp_gfdl_pic_full_prof_gotmgrid[: , ::-1 ]

kz_gfdl_pic_full_prof_TB=kz_gfdl_pic_full_prof_gotmgrid[: , ::-1 ]

 
unique_z_m_gotm_TB=unique_z_m_gotm[::-1]

np.where(unique_z_m_gotm_TB == -13.75)#27
np.where(unique_z_m_gotm_TB == -14.25)#28
np.where(unique_z_m_gotm_TB == -17.25)#34
np.where(unique_z_m_gotm_TB == -0.25)#0
np.where(unique_z_m_gotm_TB == -1.25)#2



temp_gfdl_pic_hypo_TB =temp_gfdl_pic_full_prof_TB[:  ,28: ]#  14.25m-20.75m
temp_gfdl_pic_meta= temp_gfdl_pic_full_prof_TB[:  , 27 ]# 13.75m 

kz_gfdl_pic_hypo_TB =kz_gfdl_pic_full_prof_TB[:  , 28: ]# 14.25m-20.75m

kz_gfdl_pic_hypo_T17 =kz_gfdl_pic_full_prof_TB[:  , 28:35 ]# 14.25m-17.25m(34+1)
"""
#%%rcp26

kz_gfdl_rcp26_full_prof_gotmgrid
temp_gfdl_rcp26_full_prof_gotmgrid


temp_gfdl_rcp26_full_prof_TB=temp_gfdl_rcp26_full_prof_gotmgrid[: , ::-1 ]

kz_gfdl_rcp26_full_prof_TB=kz_gfdl_rcp26_full_prof_gotmgrid[: , ::-1 ]

 
unique_z_m_gotm_TB=unique_z_m_gotm[::-1]

np.where(unique_z_m_gotm_TB == -13.75)#27
np.where(unique_z_m_gotm_TB == -14.25)#28
np.where(unique_z_m_gotm_TB == -17.25)#34
np.where(unique_z_m_gotm_TB == -0.25)#0
np.where(unique_z_m_gotm_TB == -1.25)#2




temp_gfdl_rcp26_hypo_TB =temp_gfdl_rcp26_full_prof_TB[:  ,28: ]#  14.25m-20.75m
temp_gfdl_rcp26_meta= temp_gfdl_rcp26_full_prof_TB[:  , 27 ]# 13.75m 

kz_gfdl_rcp26_hypo_TB =kz_gfdl_rcp26_full_prof_TB[:  , 28: ]# 14.25m-20.75m

kz_gfdl_rcp26_hypo_T17 =kz_gfdl_rcp26_full_prof_TB[:  , 28:35 ]# 14.25m-17.25m(34+1)


#%%rcp60

kz_gfdl_rcp60_full_prof_gotmgrid
temp_gfdl_rcp60_full_prof_gotmgrid


temp_gfdl_rcp60_full_prof_TB=temp_gfdl_rcp60_full_prof_gotmgrid[: , ::-1 ]

kz_gfdl_rcp60_full_prof_TB=kz_gfdl_rcp60_full_prof_gotmgrid[: , ::-1 ]

 
unique_z_m_gotm_TB=unique_z_m_gotm[::-1]

np.where(unique_z_m_gotm_TB == -13.75)#27
np.where(unique_z_m_gotm_TB == -14.25)#28
np.where(unique_z_m_gotm_TB == -17.25)#34
np.where(unique_z_m_gotm_TB == -0.25)#0
np.where(unique_z_m_gotm_TB == -1.25)#2


unique_z_m_gotm_hypo_TB=unique_z_m_gotm_TB[28:]


temp_gfdl_rcp60_hypo_TB =temp_gfdl_rcp60_full_prof_TB[:  ,28: ]#  14.25m-20.75m
temp_gfdl_rcp60_meta= temp_gfdl_rcp60_full_prof_TB[:  , 27 ]# 13.75m 

kz_gfdl_rcp60_hypo_TB =kz_gfdl_rcp60_full_prof_TB[:  , 28: ]# 14.25m-20.75m

kz_gfdl_rcp60_hypo_T17 =kz_gfdl_rcp60_full_prof_TB[:  , 28:35 ]# 14.25m-17.25m(34+1)


#%%rcp85

kz_gfdl_rcp85_full_prof_gotmgrid
temp_gfdl_rcp85_full_prof_gotmgrid


temp_gfdl_rcp85_full_prof_TB=temp_gfdl_rcp85_full_prof_gotmgrid[: , ::-1 ]

kz_gfdl_rcp85_full_prof_TB=kz_gfdl_rcp85_full_prof_gotmgrid[: , ::-1 ]

 
unique_z_m_gotm_TB=unique_z_m_gotm[::-1]

np.where(unique_z_m_gotm_TB == -13.75)#27
np.where(unique_z_m_gotm_TB == -14.25)#28
np.where(unique_z_m_gotm_TB == -17.25)#34
np.where(unique_z_m_gotm_TB == -0.25)#0
np.where(unique_z_m_gotm_TB == -1.25)#2


unique_z_m_gotm_hypo_TB=unique_z_m_gotm_TB[28:]


temp_gfdl_rcp85_hypo_TB =temp_gfdl_rcp85_full_prof_TB[:  ,28: ]#  14.25m-20.75m
temp_gfdl_rcp85_meta= temp_gfdl_rcp85_full_prof_TB[:  , 27 ]# 13.75m 

kz_gfdl_rcp85_hypo_TB =kz_gfdl_rcp85_full_prof_TB[:  , 28: ]# 14.25m-20.75m

kz_gfdl_rcp85_hypo_T17 =kz_gfdl_rcp85_full_prof_TB[:  , 28:35 ]# 14.25m-17.25m(34+1)


#%%find_deox_period for each scenarios
#%%his
os.chdir ('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/gfdl_senarios/his')

#df_deox_period_1m_gfdl_his=find_deox_period ( density_difference_1m_top_hypo_gfdl_his_indexed)   

df_deox_period_surf_gfdl_his=find_deox_period ( density_difference_surf_top_hypo_gfdl_his_indexed , np.array(tem_gfdl_his_surf,dtype='<i4')  ) 

df_deox_period_surf_gfdl_his.to_csv('deox_period_surf_gfdl_his.csv', index=False)


#%%pic: problem with date has an error: NameError: name 'df_deox_period_1m_gfdl_pic' is not defined
"""

#df_deox_period_1m_gfdl_pic=find_deox_period ( density_difference_1m_top_hypo_gfdl_pic_indexed)   

df_deox_period_surf_gfdl_pic=find_deox_period ( density_difference_surf_top_hypo_gfdl_pic_indexed , np.array(tem_gfdl_pic_surf,dtype='<i4'))   
"""


#%%rcp26
os.chdir ('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/gfdl_senarios/rcp26')

#df_deox_period_1m_gfdl_rcp26=find_deox_period ( density_difference_1m_top_hypo_gfdl_rcp26_indexed)   

df_deox_period_surf_gfdl_rcp26=find_deox_period ( density_difference_surf_top_hypo_gfdl_rcp26_indexed , np.array(tem_gfdl_rcp26_surf,dtype='<i4'))   

df_deox_period_surf_gfdl_rcp26.to_csv('deox_period_surf_gfdl_rcp26.csv', index=False)


#%%rcp60
os.chdir ('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/gfdl_senarios/rcp60')

#df_deox_period_1m_gfdl_rcp60=find_deox_period ( density_difference_1m_top_hypo_gfdl_rcp60_indexed)   

df_deox_period_surf_gfdl_rcp60=find_deox_period ( density_difference_surf_top_hypo_gfdl_rcp60_indexed,  np.array(tem_gfdl_rcp60_surf,dtype='<i4'))  

df_deox_period_surf_gfdl_rcp60.to_csv('deox_period_surf_gfdl_rcp60.csv', index=False)

#%%rcp85
os.chdir ('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/gfdl_senarios/rcp85')

#df_deox_period_1m_gfdl_rcp85=find_deox_period ( density_difference_1m_top_hypo_gfdl_rcp85_indexed)   

df_deox_period_surf_gfdl_rcp85=find_deox_period ( density_difference_surf_top_hypo_gfdl_rcp85_indexed ,  np.array(tem_gfdl_rcp85_surf,dtype='<i4'))    

df_deox_period_surf_gfdl_rcp85.to_csv('deox_period_surf_gfdl_rcp85.csv', index=False)



#%% a function for statt function 
def summary_stats(column):
    max_value = column.max()
    min_value = column.min()
    mean_value = column.mean()
    std_dev = column.std()
    
    summary_dict = {
        'Maximum': max_value,
        'Minimum': min_value,
        'Mean': mean_value,
        'Standard Deviation': std_dev
    }
    
    return summary_dict




#%%Onsets 

#Baseline his 1976-2005 

def baseline_onset_1976_2005 (df):
    onset_1976_2005=df [(df['year']> 1975) & (df['index_deox_period_in_year']==0)]['start_dates_Jday']
    onset_1976_2005 = pd.DataFrame(onset_1976_2005)  # Convert Series to DataFrame
    onset_1976_2005.index = range(1976, 2006) 
    return (onset_1976_2005 , summary_stats(onset_1976_2005)) 


# near future deox-dur 
def baseline_duration_1976_2005 (df):
    df_1976_2005=df [df['year']> 1975]
    deox_dur_1976_2005 =annual_deox_duarion(df_1976_2005)  # Convert Series to DataFrame
    return (deox_dur_1976_2005 ) 


# near future turnover date 
def baseline_offset_1976_2005 (df):
    df_1976_2005=df [df['year']> 1975]
    offset_1976_2005  =end_dates_Jday(df_1976_2005 )  # Convert Series to DataFrame
    return (offset_1976_2005 ) 


baseline_onset_1976_2005(df_deox_period_surf_gfdl_his)
"""
 {'Maximum': start_dates_Jday    144
  dtype: int32,
  'Minimum': start_dates_Jday    112
  dtype: int32,
  'Mean': start_dates_Jday    128.4
  dtype: float64,
  'Standard Deviation': start_dates_Jday    7.993963
  dtype: float64})

"""



# near future (2030-2059) 


def near_future_onset_2030_2059 (df):
    onset_2030_2059=df [(df['year']> 2029)& (df['year']< 2060) & (df['index_deox_period_in_year']==0)]['start_dates_Jday']
    onset_2030_2059 = pd.DataFrame(onset_2030_2059)  # Convert Series to DataFrame
    onset_2030_2059.index = range(2030, 2060) 
    return (onset_2030_2059 , summary_stats(onset_2030_2059)) 


# near future deox-dur 
def near_future_duration_2030_2059 (df):
    df_2030_2059=df [(df['year']> 2029)& (df['year']< 2060)]
    deox_dur_2030_2059 =annual_deox_duarion(df_2030_2059)  # Convert Series to DataFrame
    return (deox_dur_2030_2059) 


# near future turnover date 
def near_future_offset_2030_2059 (df):
    df_2030_2059=df [(df['year']> 2029)& (df['year']< 2060)]
    offset_2030_2059 =end_dates_Jday(df_2030_2059)  # Convert Series to DataFrame
    return (offset_2030_2059) 


near_future_onset_2030_2059(df_deox_period_surf_gfdl_rcp26)
"""
 {'Maximum': start_dates_Jday    145
  dtype: int32,
  'Minimum': start_dates_Jday    108
  dtype: int32,
  'Mean': start_dates_Jday    127.433333
  dtype: float64,
  'Standard Deviation': start_dates_Jday    9.77923
  dtype: float64})
"""



near_future_onset_2030_2059(df_deox_period_surf_gfdl_rcp60)
"""
 {'Maximum': start_dates_Jday    142
  dtype: int32,
  'Minimum': start_dates_Jday    107
  dtype: int32,
  'Mean': start_dates_Jday    125.633333
  dtype: float64,
  'Standard Deviation': start_dates_Jday    8.63227
  dtype: float64})
"""


near_future_onset_2030_2059( df_deox_period_surf_gfdl_rcp85)
"""
 {'Maximum': start_dates_Jday    156
  dtype: int32,
  'Minimum': start_dates_Jday    112
  dtype: int32,
  'Mean': start_dates_Jday    130.166667
  dtype: float64,
  'Standard Deviation': start_dates_Jday    9.68854
  dtype: float64})

"""                                                            


# far future (2070-2099)

def distant_future_onset_2070_2099 (df):
    onset_2070_2099=df [(df['year']> 2069) & (df['index_deox_period_in_year']==0)]['start_dates_Jday']
    onset_2070_2099 = pd.DataFrame(onset_2070_2099)  # Convert Series to DataFrame
    onset_2070_2099.index = range(2070, 2100) 
    return (onset_2070_2099 , summary_stats(onset_2070_2099)) 

# far future deox-dur 
def distant_future_duration_2070_2099 (df):
    df_2070_2099=df [df['year']> 2069]
    deox_dur_2070_2099 =annual_deox_duarion(df_2070_2099)  # Convert Series to DataFrame
    return (deox_dur_2070_2099) 


# far future turnover date 
def distant_future_offset_2070_2099 (df):
    df_2070_2099=df [df['year']> 2069]
    offset_2070_2099 =end_dates_Jday(df_2070_2099)  # Convert Series to DataFrame
    return (offset_2070_2099) 





#rcp26
distant_future_onset_2070_2099( df_deox_period_surf_gfdl_rcp26)
"""
 {'Maximum': start_dates_Jday    149
  dtype: int32,
  'Minimum': start_dates_Jday    108
  dtype: int32,
  'Mean': start_dates_Jday    122.733333
  dtype: float64,
  'Standard Deviation': start_dates_Jday    9.920141
  dtype: float64})
"""

#rcp60
distant_future_onset_2070_2099( df_deox_period_surf_gfdl_rcp60)
"""
 {'Maximum': start_dates_Jday    176
  dtype: int32,
  'Minimum': start_dates_Jday    93
  dtype: int32,
  'Mean': start_dates_Jday    124.2
  dtype: float64,
  'Standard Deviation': start_dates_Jday    14.624967
  dtype: float64})
"""




#rcp85
distant_future_onset_2070_2099( df_deox_period_surf_gfdl_rcp85)

"""
 {'Maximum': start_dates_Jday    142
  dtype: int32,
  'Minimum': start_dates_Jday    104
  dtype: int32,
  'Mean': start_dates_Jday    122.9
  dtype: float64,
  'Standard Deviation': start_dates_Jday    10.423283
  dtype: float64})

"""




#%%saving the onset number of years with the year 




#####onset 
baseline_onset_gfdl=baseline_onset_1976_2005(df_deox_period_surf_gfdl_his)[0]



near_future_onset_gfdl_rcp26=near_future_onset_2030_2059(df_deox_period_surf_gfdl_rcp26)[0]

near_future_onset_gfdl_rcp60=near_future_onset_2030_2059(df_deox_period_surf_gfdl_rcp60)[0]

near_future_onset_gfdl_rcp85=near_future_onset_2030_2059(df_deox_period_surf_gfdl_rcp85)[0]




distant_future_onset_gfdl_rcp26=distant_future_onset_2070_2099( df_deox_period_surf_gfdl_rcp26)[0]

distant_future_onset_gfdl_rcp60=distant_future_onset_2070_2099( df_deox_period_surf_gfdl_rcp60)[0]

distant_future_onset_gfdl_rcp85=distant_future_onset_2070_2099( df_deox_period_surf_gfdl_rcp85)[0]



#%%offset 


baseline_offset_gfdl=baseline_offset_1976_2005(df_deox_period_surf_gfdl_his)



near_future_offset_gfdl_rcp26=near_future_offset_2030_2059(df_deox_period_surf_gfdl_rcp26)

near_future_offset_gfdl_rcp60=near_future_offset_2030_2059(df_deox_period_surf_gfdl_rcp60)

near_future_offset_gfdl_rcp85=near_future_offset_2030_2059(df_deox_period_surf_gfdl_rcp85)




distant_future_offset_gfdl_rcp26=distant_future_offset_2070_2099( df_deox_period_surf_gfdl_rcp26)

distant_future_offset_gfdl_rcp60=distant_future_offset_2070_2099( df_deox_period_surf_gfdl_rcp60)

distant_future_offset_gfdl_rcp85=distant_future_offset_2070_2099( df_deox_period_surf_gfdl_rcp85)


#%%duration 


baseline_duration_gfdl=baseline_duration_1976_2005(df_deox_period_surf_gfdl_his)



near_future_duration_gfdl_rcp26=near_future_duration_2030_2059(df_deox_period_surf_gfdl_rcp26)

near_future_duration_gfdl_rcp60=near_future_duration_2030_2059(df_deox_period_surf_gfdl_rcp60)

near_future_duration_gfdl_rcp85=near_future_duration_2030_2059(df_deox_period_surf_gfdl_rcp85)




distant_future_duration_gfdl_rcp26=distant_future_duration_2070_2099( df_deox_period_surf_gfdl_rcp26)

distant_future_duration_gfdl_rcp60=distant_future_duration_2070_2099( df_deox_period_surf_gfdl_rcp60)

distant_future_duration_gfdl_rcp85=distant_future_duration_2070_2099( df_deox_period_surf_gfdl_rcp85)


#%%onset_date 2020-2100-gfdl

summary_stats(start_dates_Jday(df_deox_period_surf_gfdl_rcp26[df_deox_period_surf_gfdl_rcp26['year']>2019]))
"""
{'Maximum': 153,
 'Minimum': 108,
 'Mean': 125.6125,
 'Standard Deviation': 10.363633776976643}
"""

summary_stats(start_dates_Jday(df_deox_period_surf_gfdl_rcp60[df_deox_period_surf_gfdl_rcp60['year']>2019]))
"""
{'Maximum': 176,
 'Minimum': 93,
 'Mean': 124.8625,
 'Standard Deviation': 11.411457433627557}
"""

summary_stats(start_dates_Jday(df_deox_period_surf_gfdl_rcp85[df_deox_period_surf_gfdl_rcp85['year']>2019]))
"""
{'Maximum': 181,
 'Minimum': 104,
 'Mean': 129.375,
 'Standard Deviation': 13.248716202434794}
"""

#%%deox_dur 2020-2100-gfdl


#rcp26 ()
summary_stats(annual_deox_duarion(df_deox_period_surf_gfdl_rcp26[df_deox_period_surf_gfdl_rcp26['year']>2019]))
"""
{'Maximum': 147,
 'Minimum': 79,
 'Mean': 121.7625,
 'Standard Deviation': 13.393030258073447}
"""


#rcp60 ()
summary_stats(annual_deox_duarion(df_deox_period_surf_gfdl_rcp60[df_deox_period_surf_gfdl_rcp60['year']>2019]))
"""
{'Maximum': 151,
 'Minimum': 55,
 'Mean': 116.6,
 'Standard Deviation': 14.954445594470382}
"""




#rcp85 ()
summary_stats(annual_deox_duarion(df_deox_period_surf_gfdl_rcp85[df_deox_period_surf_gfdl_rcp85['year']>2019]))
"""
{'Maximum': 147,
 'Minimum': 57,
 'Mean': 102.25,
 'Standard Deviation': 17.9968351648107}
"""


#%%offset_date 2020-2100-gfdl

summary_stats(end_dates_Jday(df_deox_period_surf_gfdl_rcp26[df_deox_period_surf_gfdl_rcp26['year']>2019]))
"""
{'Maximum': 262,
 'Minimum': 211,
 'Mean': 247.375,
 'Standard Deviation': 9.00685393028659}
"""

summary_stats(end_dates_Jday(df_deox_period_surf_gfdl_rcp60[df_deox_period_surf_gfdl_rcp60['year']>2019]))
"""
{'Maximum': 261,
 'Minimum': 217,
 'Mean': 241.4625,
 'Standard Deviation': 9.266714286676054}
"""

summary_stats(end_dates_Jday(df_deox_period_surf_gfdl_rcp85[df_deox_period_surf_gfdl_rcp85['year']>2019]))
"""
{'Maximum': 258,
 'Minimum': 205,
 'Mean': 231.625,
 'Standard Deviation': 10.879518557851396}
"""

#%% number of polymictic years over 2020-2100-gfdl

count_polymictic(df_deox_period_surf_gfdl_rcp26[df_deox_period_surf_gfdl_rcp26['year']>2019])
#7
count_polymictic(df_deox_period_surf_gfdl_rcp60[df_deox_period_surf_gfdl_rcp60['year']>2019])
#8
count_polymictic(df_deox_period_surf_gfdl_rcp85[df_deox_period_surf_gfdl_rcp85['year']>2019])
#13

#%% Simulation of DO prof
#inital common inputs 

unique_z_m_gotm_hypo_TB
#array([-14.25, -14.75, -15.25, -15.75, -16.25, -16.75, -17.25, -17.75,
#       -18.25, -18.75, -19.25, -19.75, -20.25, -20.75], dtype=float32)

hypo_morpho_vriables_gotm_grid=[np.array (interpolated_bath['V_r'][1:15][::-1]),
                               np.array (interpolated_bath['A_s'][1:15][::-1]),
                               np.array (interpolated_bath['A_l'][1:15][::-1]),
                               0.5, np.array (interpolated_bath['V_r'][1:15][::-1]).size]#V_r, A_s, A_l, dz, nl



#%%Reading the winner Ja and Jv ready for apply :
   
####################with variable theta:    
# Define the file path
file_path = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Calibration&Validation/Final/df_winner_of_all_180combinations_interval1e_1.csv'

# Read the Excel file
df_winner_of_all = pd.read_csv(file_path)

df_winner_of_all['weights']

#%%##################with fixed theta:  

"""
# Define the file path

#file_path = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Calibration&Validation/Final/df_winner_of_all_180combinations_interval1e_1_fixedtheta.csv'

#using of the temp ave hypo from onset to deephypoxia
file_path = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Calibration&Validation/Final/df_winner_of_all_180combinations_interval1e_1_fixedtheta_on_avetemp_fromonset_todeephypoxia.csv'

# Read the Excel file
df_winner_of_all = pd.read_csv(file_path)
df_winner_of_all['weights']
"""





#%%%%%%%%%%%%%%%%%%%%%%without kz running the model 
#%%his DO simulation 
import time

os.chdir ('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/gfdl_senarios/his')

start_time = time.time()


for index, row in df_winner_of_all.iterrows():
    p1 = row['Jv']
    p2 = row['Ja']
    p3 = row['weights']

    header_values = {'Jv': p1, 'Ja': p2 , 'weights': p3 }
    header_df = pd.DataFrame([header_values])
    
    # Round Ja and Jv to 3 decimal places
    Jv_name = round(p1, 3)
    Ja_name = round(p2, 3)

    DO_2D_deox_gfdl_his_hypoprof , temp_2D_deox_gfdl_his_hypoprof  =do_model_comprehensive_gotm([p1 , p2 , 1], density_difference_surf_top_hypo_gfdl_his_indexed , np.array(tem_gfdl_his_surf,dtype='<i4') , hypo_morpho_vriables_gotm_grid 
                               ,temp_gfdl_his_hypo_TB ,kz_gfdl_his_hypo_TB , replanishmnet_rate= 2.7946 )

    #NO KZ function : , kz_2D_deox_gfdl_his_hypoprof , full_sat_hypo_condition_his_gfdl
    
    # Create a DataFrame for result
    DO_2D_deox_gfdl_his_hypoprof = pd.DataFrame(DO_2D_deox_gfdl_his_hypoprof, columns=[f'{depth}m' for depth in unique_z_m_gotm_hypo_TB])

    # Add a column for dates
    DO_2D_deox_gfdl_his_hypoprof.insert(0, 'Datetime', formatted_time_series_gfdl_his)  # Replace 'your_date_array' with your actual date array

      
    # Define the filename
    DO_filename = f'DO_prof_gfdl_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
    
    # add jv, ja and weights values in the first row 
    header_df = pd.DataFrame([header_values])
    header_df.to_csv(DO_filename, index=False)
    
    
    # Save the result to a CSV file
    DO_2D_deox_gfdl_his_hypoprof.to_csv(DO_filename,mode='a', index=False, na_rep='NaN')#, header=False)  


    fullsatarray_filename= f'fullsat_array_gfdl_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
    
    
    
    
    

temp_filename = f'temp_prof_gfdl_his.csv'
kz_filename= f'kz_prof_gfdl_his.csv'



df_temp_deox_gfdl_his_hypoprof =pd.DataFrame(temp_2D_deox_gfdl_his_hypoprof , columns=[f'{depth}m' for depth in unique_z_m_gotm_hypo_TB])
df_temp_deox_gfdl_his_hypoprof.insert(0, 'Datetime', formatted_time_series_gfdl_his) 
df_temp_deox_gfdl_his_hypoprof.to_csv(temp_filename, index=False, na_rep='NaN')# header=False)  
"""
df_kz_deox_gfdl_his_hypoprof =pd.DataFrame(kz_2D_deox_gfdl_his_hypoprof , columns=[f'{depth}m' for depth in unique_z_m_gotm_hypo_TB])
df_kz_deox_gfdl_his_hypoprof.insert(0, 'Datetime', formatted_time_series_gfdl_his) 
df_kz_deox_gfdl_his_hypoprof.to_csv(kz_filename, index=False, na_rep='NaN')# header=False)  

df_fullsat_array_gfdl_his =pd.DataFrame(full_sat_hypo_condition_his_gfdl , columns=[f'{depth}m' for depth in unique_z_m_gotm_hypo_TB])
df_fullsat_array_gfdl_his.insert(0, 'Datetime', formatted_time_series_gfdl_his) 
df_fullsat_array_gfdl_his.to_csv(fullsatarray_filename, index=False, na_rep='NaN')# header=False)  
"""

# Record the end time
end_time = time.time()

# Calculate the elapsed time
elapsed_time = end_time - start_time

# Print the elapsed time in seconds
print(f"The code took {elapsed_time} seconds to run.")

#%%rcp26 DO simulation 
import time

os.chdir ('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/gfdl_senarios/rcp26')

start_time = time.time()


for index, row in df_winner_of_all.iterrows():
    p1 = row['Jv']
    p2 = row['Ja']
    p3 = row['weights']

    header_values = {'Jv': p1, 'Ja': p2 , 'weights': p3 }
    header_df = pd.DataFrame([header_values])
    
    # Round Ja and Jv to 3 decimal places
    Jv_name = round(p1, 3)
    Ja_name = round(p2, 3)

    DO_2D_deox_gfdl_rcp26_hypoprof , temp_2D_deox_gfdl_rcp26_hypoprof  =do_model_comprehensive_gotm([p1 , p2 , 1], density_difference_surf_top_hypo_gfdl_rcp26_indexed , np.array(tem_gfdl_rcp26_surf,dtype='<i4') , hypo_morpho_vriables_gotm_grid 
                               ,temp_gfdl_rcp26_hypo_TB ,kz_gfdl_rcp26_hypo_TB , replanishmnet_rate= 2.7946 )
    #, kz_2D_deox_gfdl_rcp26_hypoprof , full_sat_hypo_condition_rcp26_gfdl
 
    
    # Create a DataFrame for result
    DO_2D_deox_gfdl_rcp26_hypoprof = pd.DataFrame(DO_2D_deox_gfdl_rcp26_hypoprof, columns=[f'{depth}m' for depth in unique_z_m_gotm_hypo_TB])

    # Add a column for dates
    DO_2D_deox_gfdl_rcp26_hypoprof.insert(0, 'Datetime', formatted_time_series_gfdl_rcp26)  # Replace 'your_date_array' with your actual date array

      
    # Define the filename
    DO_filename = f'DO_prof_gfdl_rcp26_Jv_{Jv_name}_Ja_{Ja_name}.csv'
    
    # add jv, ja and weights values in the first row 
    header_df = pd.DataFrame([header_values])
    header_df.to_csv(DO_filename, index=False)
    
    
    # Save the result to a CSV file
    DO_2D_deox_gfdl_rcp26_hypoprof.to_csv(DO_filename,mode='a', index=False, na_rep='NaN')#, header=False)  



temp_filename = f'temp_prof_gfdl_rcp26.csv'
kz_filename= f'kz_prof_gfdl_rcp26.csv'
fullsatarray_filename= f'fullsat_array_gfdl_rcp26.csv'


df_temp_deox_gfdl_rcp26_hypoprof =pd.DataFrame(temp_2D_deox_gfdl_rcp26_hypoprof , columns=[f'{depth}m' for depth in unique_z_m_gotm_hypo_TB])
df_temp_deox_gfdl_rcp26_hypoprof.insert(0, 'Datetime', formatted_time_series_gfdl_rcp26) 
df_temp_deox_gfdl_rcp26_hypoprof.to_csv(temp_filename, index=False, na_rep='NaN')# header=False)  
"""
df_kz_deox_gfdl_rcp26_hypoprof =pd.DataFrame(kz_2D_deox_gfdl_rcp26_hypoprof , columns=[f'{depth}m' for depth in unique_z_m_gotm_hypo_TB])
df_kz_deox_gfdl_rcp26_hypoprof.insert(0, 'Datetime', formatted_time_series_gfdl_rcp26) 
df_kz_deox_gfdl_rcp26_hypoprof.to_csv(kz_filename, index=False, na_rep='NaN')# header=False)  

df_fullsat_array_gfdl_rcp26 =pd.DataFrame(full_sat_hypo_condition_rcp26_gfdl , columns=[f'{depth}m' for depth in unique_z_m_gotm_hypo_TB])
df_fullsat_array_gfdl_rcp26.insert(0, 'Datetime', formatted_time_series_gfdl_rcp26) 
df_fullsat_array_gfdl_rcp26.to_csv(fullsatarray_filename, index=False, na_rep='NaN')# header=False)  
"""

# Record the end time
end_time = time.time()

# Calculate the elapsed time
elapsed_time = end_time - start_time

# Print the elapsed time in seconds
print(f"The code took {elapsed_time} seconds to run.")


#%%rcp60 DO simulation 
import time

os.chdir ('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/gfdl_senarios/rcp60')

start_time = time.time()


for index, row in df_winner_of_all.iterrows():
    p1 = row['Jv']
    p2 = row['Ja']
    p3 = row['weights']

    header_values = {'Jv': p1, 'Ja': p2 , 'weights': p3 }
    header_df = pd.DataFrame([header_values])
    
    # Round Ja and Jv to 3 decimal places
    Jv_name = round(p1, 3)
    Ja_name = round(p2, 3)

    DO_2D_deox_gfdl_rcp60_hypoprof , temp_2D_deox_gfdl_rcp60_hypoprof  =do_model_comprehensive_gotm([p1 , p2 , 1], density_difference_surf_top_hypo_gfdl_rcp60_indexed , np.array(tem_gfdl_rcp60_surf,dtype='<i4') , hypo_morpho_vriables_gotm_grid 
                               ,temp_gfdl_rcp60_hypo_TB ,kz_gfdl_rcp60_hypo_TB , replanishmnet_rate= 2.7946 )
    #, kz_2D_deox_gfdl_rcp60_hypoprof , full_sat_hypo_condition_rcp60_gfdl
 
    
    # Create a DataFrame for result
    DO_2D_deox_gfdl_rcp60_hypoprof = pd.DataFrame(DO_2D_deox_gfdl_rcp60_hypoprof, columns=[f'{depth}m' for depth in unique_z_m_gotm_hypo_TB])

    # Add a column for dates
    DO_2D_deox_gfdl_rcp60_hypoprof.insert(0, 'Datetime', formatted_time_series_gfdl_rcp60)  # Replace 'your_date_array' with your actual date array

      
    # Define the filename
    DO_filename = f'DO_prof_gfdl_rcp60_Jv_{Jv_name}_Ja_{Ja_name}.csv'
    
    # add jv, ja and weights values in the first row 
    header_df = pd.DataFrame([header_values])
    header_df.to_csv(DO_filename, index=False)
    
    
    # Save the result to a CSV file
    DO_2D_deox_gfdl_rcp60_hypoprof.to_csv(DO_filename,mode='a', index=False, na_rep='NaN')#, header=False)  



temp_filename = f'temp_prof_gfdl_rcp60.csv'
kz_filename= f'kz_prof_gfdl_rcp60.csv'
fullsatarray_filename= f'fullsat_array_gfdl_rcp60.csv'


df_temp_deox_gfdl_rcp60_hypoprof =pd.DataFrame(temp_2D_deox_gfdl_rcp60_hypoprof , columns=[f'{depth}m' for depth in unique_z_m_gotm_hypo_TB])
df_temp_deox_gfdl_rcp60_hypoprof.insert(0, 'Datetime', formatted_time_series_gfdl_rcp60) 
df_temp_deox_gfdl_rcp60_hypoprof.to_csv(temp_filename, index=False, na_rep='NaN')# header=False)  
"""
df_kz_deox_gfdl_rcp60_hypoprof =pd.DataFrame(kz_2D_deox_gfdl_rcp60_hypoprof , columns=[f'{depth}m' for depth in unique_z_m_gotm_hypo_TB])
df_kz_deox_gfdl_rcp60_hypoprof.insert(0, 'Datetime', formatted_time_series_gfdl_rcp60) 
df_kz_deox_gfdl_rcp60_hypoprof.to_csv(kz_filename, index=False, na_rep='NaN')# header=False)  

df_fullsat_array_gfdl_rcp60 =pd.DataFrame(full_sat_hypo_condition_rcp60_gfdl , columns=[f'{depth}m' for depth in unique_z_m_gotm_hypo_TB])
df_fullsat_array_gfdl_rcp60.insert(0, 'Datetime', formatted_time_series_gfdl_rcp60) 
df_fullsat_array_gfdl_rcp60.to_csv(fullsatarray_filename, index=False, na_rep='NaN')# header=False)  
"""

# Record the end time
end_time = time.time()

# Calculate the elapsed time
elapsed_time = end_time - start_time

# Print the elapsed time in seconds
print(f"The code took {elapsed_time} seconds to run.")

#%%rcp85 DO simulation 
import time

os.chdir ('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/gfdl_senarios/rcp85')

start_time = time.time()


for index, row in df_winner_of_all.iterrows():
    p1 = row['Jv']
    p2 = row['Ja']
    p3 = row['weights']

    header_values = {'Jv': p1, 'Ja': p2 , 'weights': p3 }
    header_df = pd.DataFrame([header_values])
    
    # Round Ja and Jv to 3 decimal places
    Jv_name = round(p1, 3)
    Ja_name = round(p2, 3)

    DO_2D_deox_gfdl_rcp85_hypoprof , temp_2D_deox_gfdl_rcp85_hypoprof  =do_model_comprehensive_gotm([p1 , p2 , 1], density_difference_surf_top_hypo_gfdl_rcp85_indexed , np.array(tem_gfdl_rcp85_surf,dtype='<i4') , hypo_morpho_vriables_gotm_grid 
                               ,temp_gfdl_rcp85_hypo_TB ,kz_gfdl_rcp85_hypo_TB , replanishmnet_rate= 2.7946 )
    #, kz_2D_deox_gfdl_rcp85_hypoprof , full_sat_hypo_condition_rcp85_gfdl
 
    
    # Create a DataFrame for result
    DO_2D_deox_gfdl_rcp85_hypoprof = pd.DataFrame(DO_2D_deox_gfdl_rcp85_hypoprof, columns=[f'{depth}m' for depth in unique_z_m_gotm_hypo_TB])

    # Add a column for dates
    DO_2D_deox_gfdl_rcp85_hypoprof.insert(0, 'Datetime', formatted_time_series_gfdl_rcp85)  # Replace 'your_date_array' with your actual date array

      
    # Define the filename
    DO_filename = f'DO_prof_gfdl_rcp85_Jv_{Jv_name}_Ja_{Ja_name}.csv'
    
    # add jv, ja and weights values in the first row 
    header_df = pd.DataFrame([header_values])
    header_df.to_csv(DO_filename, index=False)
    
    
    # Save the result to a CSV file
    DO_2D_deox_gfdl_rcp85_hypoprof.to_csv(DO_filename,mode='a', index=False, na_rep='NaN')#, header=False)  



temp_filename = f'temp_prof_gfdl_rcp85.csv'
kz_filename= f'kz_prof_gfdl_rcp85.csv'
fullsatarray_filename= f'fullsat_array_gfdl_rcp85.csv'


df_temp_deox_gfdl_rcp85_hypoprof =pd.DataFrame(temp_2D_deox_gfdl_rcp85_hypoprof , columns=[f'{depth}m' for depth in unique_z_m_gotm_hypo_TB])
df_temp_deox_gfdl_rcp85_hypoprof.insert(0, 'Datetime', formatted_time_series_gfdl_rcp85) 
df_temp_deox_gfdl_rcp85_hypoprof.to_csv(temp_filename, index=False, na_rep='NaN')# header=False)  
"""
df_kz_deox_gfdl_rcp85_hypoprof =pd.DataFrame(kz_2D_deox_gfdl_rcp85_hypoprof , columns=[f'{depth}m' for depth in unique_z_m_gotm_hypo_TB])
df_kz_deox_gfdl_rcp85_hypoprof.insert(0, 'Datetime', formatted_time_series_gfdl_rcp85) 
df_kz_deox_gfdl_rcp85_hypoprof.to_csv(kz_filename, index=False, na_rep='NaN')# header=False)  

df_fullsat_array_gfdl_rcp85 =pd.DataFrame(full_sat_hypo_condition_rcp85_gfdl , columns=[f'{depth}m' for depth in unique_z_m_gotm_hypo_TB])
df_fullsat_array_gfdl_rcp85.insert(0, 'Datetime', formatted_time_series_gfdl_rcp85) 
df_fullsat_array_gfdl_rcp85.to_csv(fullsatarray_filename, index=False, na_rep='NaN')# header=False)  
"""

# Record the end time
end_time = time.time()

# Calculate the elapsed time
elapsed_time = end_time - start_time

# Print the elapsed time in seconds
print(f"The code took {elapsed_time} seconds to run.")





































#%% testing new idea of average of temp in 2020 and 2021 of each scenarios 


# gfdl
#rcp26
temp_ave_hypo_2020_2021_gfdl_rcp26=(temp_hypo_deox_ave_gfdl_rcp26 [(temp_hypo_deox_ave_gfdl_rcp26.index.year == 2021)].dropna()[0] +temp_hypo_deox_ave_gfdl_rcp26 [(temp_hypo_deox_ave_gfdl_rcp26.index.year == 2020)].dropna()[0])/2
# 10.71454337033238# ave temp 2020, 2021
#5.339681126608722# onset temp 2020 and 2021
#rcp60
temp_ave_hypo_2020_2021_gfdl_rcp60=(temp_hypo_deox_ave_gfdl_rcp60 [(temp_hypo_deox_ave_gfdl_rcp60.index.year == 2021)].dropna()[0] +temp_hypo_deox_ave_gfdl_rcp60 [(temp_hypo_deox_ave_gfdl_rcp60.index.year == 2020)].dropna()[0])/2
#9.295762932087847
#4.33706446795583
#rcp85
temp_ave_hypo_2020_2021_gfdl_rcp85=(temp_hypo_deox_ave_gfdl_rcp85 [(temp_hypo_deox_ave_gfdl_rcp85.index.year == 2021)].dropna()[0] +temp_hypo_deox_ave_gfdl_rcp85 [(temp_hypo_deox_ave_gfdl_rcp85.index.year == 2020)].dropna()[0])/2
#10.140706151244498
#6.466027301242095


#%% the ave temp of onset to hypoxia in 2020 and 2021
temp_ave_hypo_2020_2021_gfdl_rcp26=temp_ave_hypo_2020_2021_gfdl_rcp60=temp_ave_hypo_2020_2021_gfdl_rcp85=9.460405011459684

#%%%%%%%%%%%%%%%with Kz 
#%%his



#########Tvajoh kon modelling farme work of GOTM ro change kardam be jaye 
#########Median value of kz to it is value 
#########comment lines of 
"""

 ###########kz_hypo_surf_deox_subdaily=np.median(kz_hypo_deox_subdaily[0 , :-1])

 ############b[0] = b[0] + (0.0989060 * delta_t[j-1] * A_s[0] *kz_hypo_surf_deox_subdaily) / (dz * V_r[0])
 

"""


import time

######original test : variable theta: not ave temp in two days in rows 
os.chdir ('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/gfdl_senarios/his')


######original test : variable theta: not ave temp in two days in rows 
######os.chdir ('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/gfdl_senarios/his_notavetemp')


###### test with fixed theta
######os.chdir ('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/gfdl_senarios/his_fixedtheta')


###### test with fixed theta at onset temp
######os.chdir ('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/gfdl_senarios/his_fixedtheta_at_temp_onset')


###### test with fixed theta at onset_tempave_onsettodeephypoxia in both calib and simulation
######os.chdir ('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/gfdl_senarios/his_fixedtheta_at_tempave_onsettodeephypoxia')


###### test with fixed theta at onset_tempave_onsettodeephypoxia in calib_but not in simulation
######os.chdir ('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/gfdl_senarios/his_fixedtheta_at_tempave_onsettodeephypoxia')


###### test with fixed theta in calibration but variable for GOTM simulation 
######os.chdir ('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/gfdl_senarios/his_calibinfixedtheta_simuvartheta')






start_time = time.time()


for index, row in df_winner_of_all.iterrows():
    p1 = row['Jv']
    p2 = row['Ja']
    p3 = row['weights']

    header_values = {'Jv': p1, 'Ja': p2 , 'weights': p3 }
    header_df = pd.DataFrame([header_values])
    
    # Round Ja and Jv to 3 decimal places
    Jv_name = round(p1, 3)
    Ja_name = round(p2, 3)

    DO_2D_deox_gfdl_his_hypoprof , temp_2D_deox_gfdl_his_hypoprof , kz_2D_deox_gfdl_his_hypoprof , full_sat_hypo_condition_his_gfdl =do_model_comprehensive_gotm([p1 , p2 , 1], density_difference_surf_top_hypo_gfdl_his_indexed , np.array(tem_gfdl_his_surf,dtype='<i4') , hypo_morpho_vriables_gotm_grid 
                               ,temp_gfdl_his_hypo_TB ,kz_gfdl_his_hypo_TB , replanishmnet_rate= 2.7946 )
    
    DO_2D_deox_gfdl_his_mixingincl , temp_2D_deox_gfdl_his_mixingincl, kz_2D_deox_gfdl_his_mixingincl= mixing_incl_do_model_comprehensive_gotm([p1 , p2 , 1], density_difference_surf_top_hypo_gfdl_his_indexed , np.array(tem_gfdl_his_surf,dtype='<i4') , hypo_morpho_vriables_gotm_grid 
                               ,temp_gfdl_his_hypo_TB ,kz_gfdl_his_hypo_TB , replanishmnet_rate= 2.7946 )
    
    # Create a DataFrame for result
    DO_2D_deox_gfdl_his_hypoprof = pd.DataFrame(DO_2D_deox_gfdl_his_hypoprof, columns=[f'{depth}m' for depth in unique_z_m_gotm_hypo_TB])

    DO_2D_deox_gfdl_his_mixingincl= pd.DataFrame(DO_2D_deox_gfdl_his_mixingincl, columns=[f'{depth}m' for depth in unique_z_m_gotm_hypo_TB])
    
    # Add a column for dates
    DO_2D_deox_gfdl_his_hypoprof.insert(0, 'Datetime', formatted_time_series_gfdl_his)  # Replace 'your_date_array' with your actual date array
    DO_2D_deox_gfdl_his_mixingincl.insert(0, 'Datetime', formatted_time_series_gfdl_his)
      
    # Define the filename
    DO_filename = f'DO_prof_gfdl_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
    
    mixingincl_DO_filename = f'mixingincl_DO_prof_gfdl_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'

    
    # add jv, ja and weights values in the first row 
    header_df = pd.DataFrame([header_values])
    header_df.to_csv(DO_filename, index=False)
    header_df.to_csv(mixingincl_DO_filename, index=False)
    
    
    # Save the result to a CSV file
    DO_2D_deox_gfdl_his_hypoprof.to_csv(DO_filename,mode='a', index=False, na_rep='NaN')#, header=False)  

    DO_2D_deox_gfdl_his_mixingincl.to_csv(mixingincl_DO_filename,mode='a', index=False, na_rep='NaN')

temp_filename = f'temp_prof_gfdl_his.csv'
kz_filename= f'kz_prof_gfdl_his.csv'

temp_filename_mixingincl = f'mixingincl_temp_prof_gfdl_his.csv'
kz_filename_mixingincl= f'mixingincl_kz_prof_gfdl_his.csv'

fullsatarray_filename= f'fullsat_array_gfdl_his.csv'


df_temp_deox_gfdl_his_hypoprof =pd.DataFrame(temp_2D_deox_gfdl_his_hypoprof , columns=[f'{depth}m' for depth in unique_z_m_gotm_hypo_TB])
df_temp_deox_gfdl_his_hypoprof.insert(0, 'Datetime', formatted_time_series_gfdl_his) 
df_temp_deox_gfdl_his_hypoprof.to_csv(temp_filename, index=False, na_rep='NaN')# header=False)  

df_kz_deox_gfdl_his_hypoprof =pd.DataFrame(kz_2D_deox_gfdl_his_hypoprof , columns=[f'{depth}m' for depth in unique_z_m_gotm_hypo_TB])
df_kz_deox_gfdl_his_hypoprof.insert(0, 'Datetime', formatted_time_series_gfdl_his) 
df_kz_deox_gfdl_his_hypoprof.to_csv(kz_filename, index=False, na_rep='NaN')# header=False)  


####_mixingincl

df_temp_deox_gfdl_his_hypoprof_mixingincl =pd.DataFrame(temp_2D_deox_gfdl_his_mixingincl , columns=[f'{depth}m' for depth in unique_z_m_gotm_hypo_TB])
df_temp_deox_gfdl_his_hypoprof_mixingincl.insert(0, 'Datetime', formatted_time_series_gfdl_his) 
df_temp_deox_gfdl_his_hypoprof_mixingincl.to_csv(temp_filename_mixingincl, index=False, na_rep='NaN')# header=False)  

df_kz_deox_gfdl_his_hypoprof_mixingincl =pd.DataFrame(kz_2D_deox_gfdl_his_mixingincl , columns=[f'{depth}m' for depth in unique_z_m_gotm_hypo_TB])
df_kz_deox_gfdl_his_hypoprof_mixingincl.insert(0, 'Datetime', formatted_time_series_gfdl_his) 
df_kz_deox_gfdl_his_hypoprof_mixingincl.to_csv(kz_filename_mixingincl, index=False, na_rep='NaN')# header=False)  



df_fullsat_array_gfdl_his =pd.DataFrame(full_sat_hypo_condition_his_gfdl , columns=[f'{depth}m' for depth in unique_z_m_gotm_hypo_TB])
df_fullsat_array_gfdl_his.insert(0, 'Datetime', formatted_time_series_gfdl_his) 
df_fullsat_array_gfdl_his.to_csv(fullsatarray_filename, index=False, na_rep='NaN')# header=False)  


# Record the end time
end_time = time.time()

# Calculate the elapsed time
elapsed_time = end_time - start_time

# Print the elapsed time in seconds
print(f"The code took {elapsed_time} seconds to run.")



#%%rcp26

import time

#########Tvajoh kon modelling farme work of GOTM ro change kardam be jaye 
#########Median value of kz to it is value 
#########comment lines of 
"""

 ###########kz_hypo_surf_deox_subdaily=np.median(kz_hypo_deox_subdaily[0 , :-1])

 ############b[0] = b[0] + (0.0989060 * delta_t[j-1] * A_s[0] *kz_hypo_surf_deox_subdaily) / (dz * V_r[0])
 

"""


import time

######original test : variable theta: not ave temp in two days in rows 
os.chdir ('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/gfdl_senarios/rcp26')


######original test : variable theta: not ave temp in two days in rows 
######os.chdir ('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/gfdl_senarios/rcp26_notavetemp')


###### test with fixed theta
######os.chdir ('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/gfdl_senarios/rcp26_fixedtheta')


###### test with fixed theta at onset temp
######os.chdir ('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/gfdl_senarios/rcp26_fixedtheta_at_temp_onset')


###### test with fixed theta at onset_tempave_onsettodeephypoxia in both calib and simulation
######os.chdir ('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/gfdl_senarios/rcp26_fixedtheta_at_tempave_onsettodeephypoxia')


###### test with fixed theta at onset_tempave_onsettodeephypoxia in calib_but not in simulation
######os.chdir ('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/gfdl_senarios/rcp26_fixedtheta_at_tempave_onsettodeephypoxia')


###### test with fixed theta in calibration but variable for GOTM simulation 
######os.chdir ('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/gfdl_senarios/rcp26_calibinfixedtheta_simuvartheta')






start_time = time.time()


for index, row in df_winner_of_all.iterrows():
    p1 = row['Jv']
    p2 = row['Ja']
    p3 = row['weights']

    header_values = {'Jv': p1, 'Ja': p2 , 'weights': p3 }
    header_df = pd.DataFrame([header_values])
    
    # Round Ja and Jv to 3 decimal places
    Jv_name = round(p1, 3)
    Ja_name = round(p2, 3)

    DO_2D_deox_gfdl_rcp26_hypoprof , temp_2D_deox_gfdl_rcp26_hypoprof , kz_2D_deox_gfdl_rcp26_hypoprof , full_sat_hypo_condition_rcp26_gfdl =do_model_comprehensive_gotm([p1 , p2 , 1], density_difference_surf_top_hypo_gfdl_rcp26_indexed , np.array(tem_gfdl_rcp26_surf,dtype='<i4') , hypo_morpho_vriables_gotm_grid 
                               ,temp_gfdl_rcp26_hypo_TB ,kz_gfdl_rcp26_hypo_TB , replanishmnet_rate= 2.7946 )
    
    DO_2D_deox_gfdl_rcp26_mixingincl , temp_2D_deox_gfdl_rcp26_mixingincl, kz_2D_deox_gfdl_rcp26_mixingincl= mixing_incl_do_model_comprehensive_gotm([p1 , p2 , 1], density_difference_surf_top_hypo_gfdl_rcp26_indexed , np.array(tem_gfdl_rcp26_surf,dtype='<i4') , hypo_morpho_vriables_gotm_grid ,temp_gfdl_rcp26_hypo_TB ,kz_gfdl_rcp26_hypo_TB , replanishmnet_rate= 2.7946 )
    
    # Create a DataFrame for result
    DO_2D_deox_gfdl_rcp26_hypoprof = pd.DataFrame(DO_2D_deox_gfdl_rcp26_hypoprof, columns=[f'{depth}m' for depth in unique_z_m_gotm_hypo_TB])

    DO_2D_deox_gfdl_rcp26_mixingincl= pd.DataFrame(DO_2D_deox_gfdl_rcp26_mixingincl, columns=[f'{depth}m' for depth in unique_z_m_gotm_hypo_TB])
    
    # Add a column for dates
    DO_2D_deox_gfdl_rcp26_hypoprof.insert(0, 'Datetime', formatted_time_series_gfdl_rcp26)  # Replace 'your_date_array' with your actual date array
    DO_2D_deox_gfdl_rcp26_mixingincl.insert(0, 'Datetime', formatted_time_series_gfdl_rcp26)
      
    # Define the filename
    DO_filename = f'DO_prof_gfdl_rcp26_Jv_{Jv_name}_Ja_{Ja_name}.csv'
    
    mixingincl_DO_filename = f'mixingincl_DO_prof_gfdl_rcp26_Jv_{Jv_name}_Ja_{Ja_name}.csv'

    
    # add jv, ja and weights values in the first row 
    header_df = pd.DataFrame([header_values])
    header_df.to_csv(DO_filename, index=False)
    header_df.to_csv(mixingincl_DO_filename, index=False)
    
    
    # Save the result to a CSV file
    DO_2D_deox_gfdl_rcp26_hypoprof.to_csv(DO_filename,mode='a', index=False, na_rep='NaN')#, header=False)  

    DO_2D_deox_gfdl_rcp26_mixingincl.to_csv(mixingincl_DO_filename,mode='a', index=False, na_rep='NaN')

temp_filename = f'temp_prof_gfdl_rcp26.csv'
kz_filename= f'kz_prof_gfdl_rcp26.csv'

temp_filename_mixingincl = f'mixingincl_temp_prof_gfdl_rcp26.csv'
kz_filename_mixingincl= f'mixingincl_kz_prof_gfdl_rcp26.csv'

fullsatarray_filename= f'fullsat_array_gfdl_rcp26.csv'


df_temp_deox_gfdl_rcp26_hypoprof =pd.DataFrame(temp_2D_deox_gfdl_rcp26_hypoprof , columns=[f'{depth}m' for depth in unique_z_m_gotm_hypo_TB])
df_temp_deox_gfdl_rcp26_hypoprof.insert(0, 'Datetime', formatted_time_series_gfdl_rcp26) 
df_temp_deox_gfdl_rcp26_hypoprof.to_csv(temp_filename, index=False, na_rep='NaN')# header=False)  

df_kz_deox_gfdl_rcp26_hypoprof =pd.DataFrame(kz_2D_deox_gfdl_rcp26_hypoprof , columns=[f'{depth}m' for depth in unique_z_m_gotm_hypo_TB])
df_kz_deox_gfdl_rcp26_hypoprof.insert(0, 'Datetime', formatted_time_series_gfdl_rcp26) 
df_kz_deox_gfdl_rcp26_hypoprof.to_csv(kz_filename, index=False, na_rep='NaN')# header=False)  


####_mixingincl

df_temp_deox_gfdl_rcp26_hypoprof_mixingincl =pd.DataFrame(temp_2D_deox_gfdl_rcp26_mixingincl , columns=[f'{depth}m' for depth in unique_z_m_gotm_hypo_TB])
df_temp_deox_gfdl_rcp26_hypoprof_mixingincl.insert(0, 'Datetime', formatted_time_series_gfdl_rcp26) 
df_temp_deox_gfdl_rcp26_hypoprof_mixingincl.to_csv(temp_filename_mixingincl, index=False, na_rep='NaN')# header=False)  

df_kz_deox_gfdl_rcp26_hypoprof_mixingincl =pd.DataFrame(kz_2D_deox_gfdl_rcp26_mixingincl , columns=[f'{depth}m' for depth in unique_z_m_gotm_hypo_TB])
df_kz_deox_gfdl_rcp26_hypoprof_mixingincl.insert(0, 'Datetime', formatted_time_series_gfdl_rcp26) 
df_kz_deox_gfdl_rcp26_hypoprof_mixingincl.to_csv(kz_filename_mixingincl, index=False, na_rep='NaN')# header=False)  



df_fullsat_array_gfdl_rcp26 =pd.DataFrame(full_sat_hypo_condition_rcp26_gfdl , columns=[f'{depth}m' for depth in unique_z_m_gotm_hypo_TB])
df_fullsat_array_gfdl_rcp26.insert(0, 'Datetime', formatted_time_series_gfdl_rcp26) 
df_fullsat_array_gfdl_rcp26.to_csv(fullsatarray_filename, index=False, na_rep='NaN')# header=False)  


# Record the end time
end_time = time.time()

# Calculate the elapsed time
elapsed_time = end_time - start_time

# Print the elapsed time in seconds
print(f"The code took {elapsed_time} seconds to run.")


#%%rcp26-attribution test 


#########Tvajoh kon modelling farme work of GOTM ro change kardam be jaye 
#########Median value of kz to it is value 
#########comment lines of 
"""

 ###########kz_hypo_surf_deox_subdaily=np.median(kz_hypo_deox_subdaily[0 , :-1])

 ############b[0] = b[0] + (0.0989060 * delta_t[j-1] * A_s[0] *kz_hypo_surf_deox_subdaily) / (dz * V_r[0])
 

"""


import time

######original test : variable theta: not ave temp in two days in rows 
os.chdir ('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/gfdl_senarios/rcp26_initialcond_attribution')


######original test : variable theta: not ave temp in two days in rows 
######os.chdir ('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/gfdl_senarios/rcp26_notavetemp')


###### test with fixed theta
######os.chdir ('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/gfdl_senarios/rcp26_fixedtheta')


###### test with fixed theta at onset temp
######os.chdir ('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/gfdl_senarios/rcp26_fixedtheta_at_temp_onset')


###### test with fixed theta at onset_tempave_onsettodeephypoxia in both calib and simulation
######os.chdir ('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/gfdl_senarios/rcp26_fixedtheta_at_tempave_onsettodeephypoxia')


###### test with fixed theta at onset_tempave_onsettodeephypoxia in calib_but not in simulation
######os.chdir ('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/gfdl_senarios/rcp26_fixedtheta_at_tempave_onsettodeephypoxia')


###### test with fixed theta in calibration but variable for GOTM simulation 
######os.chdir ('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/gfdl_senarios/rcp26_calibinfixedtheta_simuvartheta')






start_time = time.time()


for index, row in df_winner_of_all.iterrows():
    p1 = row['Jv']
    p2 = row['Ja']
    p3 = row['weights']

    header_values = {'Jv': p1, 'Ja': p2 , 'weights': p3 }
    header_df = pd.DataFrame([header_values])
    
    # Round Ja and Jv to 3 decimal places
    Jv_name = round(p1, 3)
    Ja_name = round(p2, 3)

    DO_2D_deox_gfdl_rcp26_hypoprof_att_test =do_model_comprehensive_gotm_rcp26_test([p1 , p2 , 1], density_difference_surf_top_hypo_gfdl_rcp26_indexed , np.array(tem_gfdl_rcp26_surf,dtype='<i4') , hypo_morpho_vriables_gotm_grid 
                               ,temp_gfdl_rcp26_hypo_TB ,kz_gfdl_rcp26_hypo_TB , replanishmnet_rate= 2.7946 )[0]
    
    DO_2D_deox_gfdl_rcp26_mixingincl_att_test = mixing_incl_do_model_comprehensive_gotm_rcp26_test([p1 , p2 , 1], density_difference_surf_top_hypo_gfdl_rcp26_indexed , np.array(tem_gfdl_rcp26_surf,dtype='<i4') , hypo_morpho_vriables_gotm_grid 
                               ,temp_gfdl_rcp26_hypo_TB ,kz_gfdl_rcp26_hypo_TB , replanishmnet_rate= 2.7946 )[0]
    
    # Create a DataFrame for result
    DO_2D_deox_gfdl_rcp26_hypoprof_att_test = pd.DataFrame(DO_2D_deox_gfdl_rcp26_hypoprof_att_test, columns=[f'{depth}m' for depth in unique_z_m_gotm_hypo_TB])

    DO_2D_deox_gfdl_rcp26_mixingincl_att_test= pd.DataFrame(DO_2D_deox_gfdl_rcp26_mixingincl_att_test, columns=[f'{depth}m' for depth in unique_z_m_gotm_hypo_TB])
    
    # Add a column for dates
    DO_2D_deox_gfdl_rcp26_hypoprof_att_test.insert(0, 'Datetime', formatted_time_series_gfdl_rcp26)  # Replace 'your_date_array' with your actual date array
    DO_2D_deox_gfdl_rcp26_mixingincl_att_test.insert(0, 'Datetime', formatted_time_series_gfdl_rcp26)
      
    # Define the filename
    DO_filename_att_test = f'DO_prof_gfdl_rcp26_att_test_Jv_{Jv_name}_Ja_{Ja_name}.csv'
    
    mixingincl_DO_filename_att_test = f'mixingincl_DO_prof_gfdl_rcp26_att_test_Jv_{Jv_name}_Ja_{Ja_name}.csv'

    
    # add jv, ja and weights values in the first row 
    header_df = pd.DataFrame([header_values])
    header_df.to_csv(DO_filename_att_test, index=False)
    header_df.to_csv(mixingincl_DO_filename_att_test, index=False)
    
    
    # Save the result to a CSV file
    DO_2D_deox_gfdl_rcp26_hypoprof_att_test.to_csv(DO_filename_att_test,mode='a', index=False, na_rep='NaN')#, header=False)  

    DO_2D_deox_gfdl_rcp26_mixingincl_att_test.to_csv(mixingincl_DO_filename_att_test,mode='a', index=False, na_rep='NaN')

# Record the end time
end_time = time.time()

# Calculate the elapsed time
elapsed_time = end_time - start_time

# Print the elapsed time in seconds
print(f"The code took {elapsed_time} seconds to run.")













#%%rcp60



#########Tvajoh kon modelling farme work of GOTM ro change kardam be jaye 
#########Median value of kz to it is value 
#########comment lines of 
"""

 ###########kz_hypo_surf_deox_subdaily=np.median(kz_hypo_deox_subdaily[0 , :-1])

 ############b[0] = b[0] + (0.0989060 * delta_t[j-1] * A_s[0] *kz_hypo_surf_deox_subdaily) / (dz * V_r[0])
 

"""


import time

######original test : variable theta: not ave temp in two days in rows 
os.chdir ('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/gfdl_senarios/rcp60')


######original test : variable theta: not ave temp in two days in rows 
######os.chdir ('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/gfdl_senarios/rcp60_notavetemp')


###### test with fixed theta
######os.chdir ('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/gfdl_senarios/rcp60_fixedtheta')


###### test with fixed theta at onset temp
######os.chdir ('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/gfdl_senarios/rcp60_fixedtheta_at_temp_onset')


###### test with fixed theta at onset_tempave_onsettodeephypoxia in both calib and simulation
######os.chdir ('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/gfdl_senarios/rcp60_fixedtheta_at_tempave_onsettodeephypoxia')


###### test with fixed theta at onset_tempave_onsettodeephypoxia in calib_but not in simulation
######os.chdir ('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/gfdl_senarios/rcp60_fixedtheta_at_tempave_onsettodeephypoxia')


###### test with fixed theta in calibration but variable for GOTM simulation 
######os.chdir ('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/gfdl_senarios/rcp60_calibinfixedtheta_simuvartheta')


start_time = time.time()


for index, row in df_winner_of_all.iterrows():
    p1 = row['Jv']
    p2 = row['Ja']
    p3 = row['weights']

    header_values = {'Jv': p1, 'Ja': p2 , 'weights': p3 }
    header_df = pd.DataFrame([header_values])
    
    # Round Ja and Jv to 3 decimal places
    Jv_name = round(p1, 3)
    Ja_name = round(p2, 3)

    DO_2D_deox_gfdl_rcp60_hypoprof , temp_2D_deox_gfdl_rcp60_hypoprof , kz_2D_deox_gfdl_rcp60_hypoprof , full_sat_hypo_condition_rcp60_gfdl =do_model_comprehensive_gotm([p1 , p2 , 1], density_difference_surf_top_hypo_gfdl_rcp60_indexed , np.array(tem_gfdl_rcp60_surf,dtype='<i4') , hypo_morpho_vriables_gotm_grid 
                               ,temp_gfdl_rcp60_hypo_TB ,kz_gfdl_rcp60_hypo_TB , replanishmnet_rate= 2.7946 )
    
    DO_2D_deox_gfdl_rcp60_mixingincl , temp_2D_deox_gfdl_rcp60_mixingincl, kz_2D_deox_gfdl_rcp60_mixingincl= mixing_incl_do_model_comprehensive_gotm([p1 , p2 , 1], density_difference_surf_top_hypo_gfdl_rcp60_indexed , np.array(tem_gfdl_rcp60_surf,dtype='<i4') , hypo_morpho_vriables_gotm_grid 
                               ,temp_gfdl_rcp60_hypo_TB ,kz_gfdl_rcp60_hypo_TB , replanishmnet_rate= 2.7946 )
    
    # Create a DataFrame for result
    DO_2D_deox_gfdl_rcp60_hypoprof = pd.DataFrame(DO_2D_deox_gfdl_rcp60_hypoprof, columns=[f'{depth}m' for depth in unique_z_m_gotm_hypo_TB])

    DO_2D_deox_gfdl_rcp60_mixingincl= pd.DataFrame(DO_2D_deox_gfdl_rcp60_mixingincl, columns=[f'{depth}m' for depth in unique_z_m_gotm_hypo_TB])
    
    # Add a column for dates
    DO_2D_deox_gfdl_rcp60_hypoprof.insert(0, 'Datetime', formatted_time_series_gfdl_rcp60)  # Replace 'your_date_array' with your actual date array
    DO_2D_deox_gfdl_rcp60_mixingincl.insert(0, 'Datetime', formatted_time_series_gfdl_rcp60)
      
    # Define the filename
    DO_filename = f'DO_prof_gfdl_rcp60_Jv_{Jv_name}_Ja_{Ja_name}.csv'
    
    mixingincl_DO_filename = f'mixingincl_DO_prof_gfdl_rcp60_Jv_{Jv_name}_Ja_{Ja_name}.csv'

    
    # add jv, ja and weights values in the first row 
    header_df = pd.DataFrame([header_values])
    header_df.to_csv(DO_filename, index=False)
    header_df.to_csv(mixingincl_DO_filename, index=False)
    
    
    # Save the result to a CSV file
    DO_2D_deox_gfdl_rcp60_hypoprof.to_csv(DO_filename,mode='a', index=False, na_rep='NaN')#, header=False)  

    DO_2D_deox_gfdl_rcp60_mixingincl.to_csv(mixingincl_DO_filename,mode='a', index=False, na_rep='NaN')

temp_filename = f'temp_prof_gfdl_rcp60.csv'
kz_filename= f'kz_prof_gfdl_rcp60.csv'

temp_filename_mixingincl = f'mixingincl_temp_prof_gfdl_rcp60.csv'
kz_filename_mixingincl= f'mixingincl_kz_prof_gfdl_rcp60.csv'

fullsatarray_filename= f'fullsat_array_gfdl_rcp60.csv'


df_temp_deox_gfdl_rcp60_hypoprof =pd.DataFrame(temp_2D_deox_gfdl_rcp60_hypoprof , columns=[f'{depth}m' for depth in unique_z_m_gotm_hypo_TB])
df_temp_deox_gfdl_rcp60_hypoprof.insert(0, 'Datetime', formatted_time_series_gfdl_rcp60) 
df_temp_deox_gfdl_rcp60_hypoprof.to_csv(temp_filename, index=False, na_rep='NaN')# header=False)  

df_kz_deox_gfdl_rcp60_hypoprof =pd.DataFrame(kz_2D_deox_gfdl_rcp60_hypoprof , columns=[f'{depth}m' for depth in unique_z_m_gotm_hypo_TB])
df_kz_deox_gfdl_rcp60_hypoprof.insert(0, 'Datetime', formatted_time_series_gfdl_rcp60) 
df_kz_deox_gfdl_rcp60_hypoprof.to_csv(kz_filename, index=False, na_rep='NaN')# header=False)  


####_mixingincl

df_temp_deox_gfdl_rcp60_hypoprof_mixingincl =pd.DataFrame(temp_2D_deox_gfdl_rcp60_mixingincl , columns=[f'{depth}m' for depth in unique_z_m_gotm_hypo_TB])
df_temp_deox_gfdl_rcp60_hypoprof_mixingincl.insert(0, 'Datetime', formatted_time_series_gfdl_rcp60) 
df_temp_deox_gfdl_rcp60_hypoprof_mixingincl.to_csv(temp_filename_mixingincl, index=False, na_rep='NaN')# header=False)  

df_kz_deox_gfdl_rcp60_hypoprof_mixingincl =pd.DataFrame(kz_2D_deox_gfdl_rcp60_mixingincl , columns=[f'{depth}m' for depth in unique_z_m_gotm_hypo_TB])
df_kz_deox_gfdl_rcp60_hypoprof_mixingincl.insert(0, 'Datetime', formatted_time_series_gfdl_rcp60) 
df_kz_deox_gfdl_rcp60_hypoprof_mixingincl.to_csv(kz_filename_mixingincl, index=False, na_rep='NaN')# header=False)  



df_fullsat_array_gfdl_rcp60 =pd.DataFrame(full_sat_hypo_condition_rcp60_gfdl , columns=[f'{depth}m' for depth in unique_z_m_gotm_hypo_TB])
df_fullsat_array_gfdl_rcp60.insert(0, 'Datetime', formatted_time_series_gfdl_rcp60) 
df_fullsat_array_gfdl_rcp60.to_csv(fullsatarray_filename, index=False, na_rep='NaN')# header=False)  


# Record the end time
end_time = time.time()

# Calculate the elapsed time
elapsed_time = end_time - start_time

# Print the elapsed time in seconds
print(f"The code took {elapsed_time} seconds to run.")



#%%rcp85



#########Tvajoh kon modelling farme work of GOTM ro change kardam be jaye 
#########Median value of kz to it is value 
#########comment lines of 
"""

 ###########kz_hypo_surf_deox_subdaily=np.median(kz_hypo_deox_subdaily[0 , :-1])

 ############b[0] = b[0] + (0.0989060 * delta_t[j-1] * A_s[0] *kz_hypo_surf_deox_subdaily) / (dz * V_r[0])
 

"""


import time

######original test : variable theta: not ave temp in two days in rows 
os.chdir ('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/gfdl_senarios/rcp85')


######original test : variable theta: not ave temp in two days in rows 
######os.chdir ('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/gfdl_senarios/rcp85_notavetemp')


###### test with fixed theta
######os.chdir ('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/gfdl_senarios/rcp85_fixedtheta')


###### test with fixed theta at onset temp
######os.chdir ('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/gfdl_senarios/rcp85_fixedtheta_at_temp_onset')


###### test with fixed theta at onset_tempave_onsettodeephypoxia in both calib and simulation
######os.chdir ('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/gfdl_senarios/rcp85_fixedtheta_at_tempave_onsettodeephypoxia')


###### test with fixed theta at onset_tempave_onsettodeephypoxia in calib_but not in simulation
######os.chdir ('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/gfdl_senarios/rcp85_fixedtheta_at_tempave_onsettodeephypoxia')


###### test with fixed theta in calibration but variable for GOTM simulation 
######os.chdir ('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/gfdl_senarios/rcp85_calibinfixedtheta_simuvartheta')






start_time = time.time()


for index, row in df_winner_of_all.iterrows():
    p1 = row['Jv']
    p2 = row['Ja']
    p3 = row['weights']

    header_values = {'Jv': p1, 'Ja': p2 , 'weights': p3 }
    header_df = pd.DataFrame([header_values])
    
    # Round Ja and Jv to 3 decimal places
    Jv_name = round(p1, 3)
    Ja_name = round(p2, 3)

    DO_2D_deox_gfdl_rcp85_hypoprof , temp_2D_deox_gfdl_rcp85_hypoprof , kz_2D_deox_gfdl_rcp85_hypoprof , full_sat_hypo_condition_rcp85_gfdl =do_model_comprehensive_gotm([p1 , p2 , 1], density_difference_surf_top_hypo_gfdl_rcp85_indexed , np.array(tem_gfdl_rcp85_surf,dtype='<i4') , hypo_morpho_vriables_gotm_grid 
                               ,temp_gfdl_rcp85_hypo_TB ,kz_gfdl_rcp85_hypo_TB , replanishmnet_rate= 2.7946 )
    
    DO_2D_deox_gfdl_rcp85_mixingincl , temp_2D_deox_gfdl_rcp85_mixingincl, kz_2D_deox_gfdl_rcp85_mixingincl= mixing_incl_do_model_comprehensive_gotm([p1 , p2 , 1], density_difference_surf_top_hypo_gfdl_rcp85_indexed , np.array(tem_gfdl_rcp85_surf,dtype='<i4') , hypo_morpho_vriables_gotm_grid 
                               ,temp_gfdl_rcp85_hypo_TB ,kz_gfdl_rcp85_hypo_TB , replanishmnet_rate= 2.7946 )
    
    # Create a DataFrame for result
    DO_2D_deox_gfdl_rcp85_hypoprof = pd.DataFrame(DO_2D_deox_gfdl_rcp85_hypoprof, columns=[f'{depth}m' for depth in unique_z_m_gotm_hypo_TB])

    DO_2D_deox_gfdl_rcp85_mixingincl= pd.DataFrame(DO_2D_deox_gfdl_rcp85_mixingincl, columns=[f'{depth}m' for depth in unique_z_m_gotm_hypo_TB])
    
    # Add a column for dates
    DO_2D_deox_gfdl_rcp85_hypoprof.insert(0, 'Datetime', formatted_time_series_gfdl_rcp85)  # Replace 'your_date_array' with your actual date array
    DO_2D_deox_gfdl_rcp85_mixingincl.insert(0, 'Datetime', formatted_time_series_gfdl_rcp85)
      
    # Define the filename
    DO_filename = f'DO_prof_gfdl_rcp85_Jv_{Jv_name}_Ja_{Ja_name}.csv'
    
    mixingincl_DO_filename = f'mixingincl_DO_prof_gfdl_rcp85_Jv_{Jv_name}_Ja_{Ja_name}.csv'

    
    # add jv, ja and weights values in the first row 
    header_df = pd.DataFrame([header_values])
    header_df.to_csv(DO_filename, index=False)
    header_df.to_csv(mixingincl_DO_filename, index=False)
    
    
    # Save the result to a CSV file
    DO_2D_deox_gfdl_rcp85_hypoprof.to_csv(DO_filename,mode='a', index=False, na_rep='NaN')#, header=False)  

    DO_2D_deox_gfdl_rcp85_mixingincl.to_csv(mixingincl_DO_filename,mode='a', index=False, na_rep='NaN')

temp_filename = f'temp_prof_gfdl_rcp85.csv'
kz_filename= f'kz_prof_gfdl_rcp85.csv'

temp_filename_mixingincl = f'mixingincl_temp_prof_gfdl_rcp85.csv'
kz_filename_mixingincl= f'mixingincl_kz_prof_gfdl_rcp85.csv'

fullsatarray_filename= f'fullsat_array_gfdl_rcp85.csv'


df_temp_deox_gfdl_rcp85_hypoprof =pd.DataFrame(temp_2D_deox_gfdl_rcp85_hypoprof , columns=[f'{depth}m' for depth in unique_z_m_gotm_hypo_TB])
df_temp_deox_gfdl_rcp85_hypoprof.insert(0, 'Datetime', formatted_time_series_gfdl_rcp85) 
df_temp_deox_gfdl_rcp85_hypoprof.to_csv(temp_filename, index=False, na_rep='NaN')# header=False)  

df_kz_deox_gfdl_rcp85_hypoprof =pd.DataFrame(kz_2D_deox_gfdl_rcp85_hypoprof , columns=[f'{depth}m' for depth in unique_z_m_gotm_hypo_TB])
df_kz_deox_gfdl_rcp85_hypoprof.insert(0, 'Datetime', formatted_time_series_gfdl_rcp85) 
df_kz_deox_gfdl_rcp85_hypoprof.to_csv(kz_filename, index=False, na_rep='NaN')# header=False)  


####_mixingincl

df_temp_deox_gfdl_rcp85_hypoprof_mixingincl =pd.DataFrame(temp_2D_deox_gfdl_rcp85_mixingincl , columns=[f'{depth}m' for depth in unique_z_m_gotm_hypo_TB])
df_temp_deox_gfdl_rcp85_hypoprof_mixingincl.insert(0, 'Datetime', formatted_time_series_gfdl_rcp85) 
df_temp_deox_gfdl_rcp85_hypoprof_mixingincl.to_csv(temp_filename_mixingincl, index=False, na_rep='NaN')# header=False)  

df_kz_deox_gfdl_rcp85_hypoprof_mixingincl =pd.DataFrame(kz_2D_deox_gfdl_rcp85_mixingincl , columns=[f'{depth}m' for depth in unique_z_m_gotm_hypo_TB])
df_kz_deox_gfdl_rcp85_hypoprof_mixingincl.insert(0, 'Datetime', formatted_time_series_gfdl_rcp85) 
df_kz_deox_gfdl_rcp85_hypoprof_mixingincl.to_csv(kz_filename_mixingincl, index=False, na_rep='NaN')# header=False)  



df_fullsat_array_gfdl_rcp85 =pd.DataFrame(full_sat_hypo_condition_rcp85_gfdl , columns=[f'{depth}m' for depth in unique_z_m_gotm_hypo_TB])
df_fullsat_array_gfdl_rcp85.insert(0, 'Datetime', formatted_time_series_gfdl_rcp85) 
df_fullsat_array_gfdl_rcp85.to_csv(fullsatarray_filename, index=False, na_rep='NaN')# header=False)  


# Record the end time
end_time = time.time()

# Calculate the elapsed time
elapsed_time = end_time - start_time

# Print the elapsed time in seconds
print(f"The code took {elapsed_time} seconds to run.")


#%%###### Managemnet :testing different Ja and Jv combination less than calibrated test
#########

#%%1. Mangemnet with only VHOD
 
#%% testing the DO model using VHOD ranges lower than the calibarted ones 
"""
16 behavioural VHOD:
'Minimum': 0.49552461937155823,
 'Maximum': 0.6014850988014254,
"""

jz_min, jz_max = 0, 0.6

num_points =len(np.arange(jz_min, jz_max+0.01 , 0.01))

param_values = np.arange(jz_min, jz_max+0.01 , 0.01)



jz_management_test=[]
for i, p in enumerate(param_values):
    
    
    jz_management_test.append([p, 1])


#minimum is mnnually set to 0.001
jz_management_test[0]=[0.001, 1]
    
#%%RCP2.6 only with Jz
import time

######managemnet test
os.chdir ('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/gfdl_senarios/rcp26_C_daily_VHOD_mangement_test')


start_time = time.time()

for par_jz in jz_management_test:
    p1 = par_jz[0]
    
    header_values = {'Jz': p1}
    # Round Ja and Jv to 3 decimal places
    Jz_name = round(p1, 3)


    DO_2D_deox_gfdl_rcp26_hypoprof =do_model_comprehensive_VHOD_gotm([p1 , 1], density_difference_surf_top_hypo_gfdl_rcp26_indexed , np.array(tem_gfdl_rcp26_surf,dtype='<i4') , hypo_morpho_vriables_gotm_grid 
                               ,temp_gfdl_rcp26_hypo_TB ,kz_gfdl_rcp26_hypo_TB , replanishmnet_rate= 2.7946  )[0]
    

    DO_2D_deox_gfdl_rcp26_mixingincl =mixing_incl_do_model_comprehensive_VHOD_gotm([p1 , 1], density_difference_surf_top_hypo_gfdl_rcp26_indexed , np.array(tem_gfdl_rcp26_surf,dtype='<i4') , hypo_morpho_vriables_gotm_grid 
                               ,temp_gfdl_rcp26_hypo_TB ,kz_gfdl_rcp26_hypo_TB , replanishmnet_rate= 2.7946  )[0]
    
    
    
    # Create a DataFrame for result
    DO_2D_deox_gfdl_rcp26_hypoprof = pd.DataFrame(DO_2D_deox_gfdl_rcp26_hypoprof, columns=[f'{depth}m' for depth in unique_z_m_gotm_hypo_TB])
    DO_2D_deox_gfdl_rcp26_mixingincl= pd.DataFrame(DO_2D_deox_gfdl_rcp26_mixingincl, columns=[f'{depth}m' for depth in unique_z_m_gotm_hypo_TB])
    # Add a column for dates
    DO_2D_deox_gfdl_rcp26_hypoprof.insert(0, 'Datetime', formatted_time_series_gfdl_rcp26)  # Replace 'your_date_array' with your actual date array
    DO_2D_deox_gfdl_rcp26_mixingincl.insert(0, 'Datetime', formatted_time_series_gfdl_rcp26)  # Replace 'your_date_array' with your actual date array
      
    # Define the filename
    DO_filename = f'DO_prof_gfdl_rcp26_Jz_{Jz_name}.csv'
    mixingincl_DO_filename = f'mixingincl_DO_prof_gfdl_rcp26_Jz_{Jz_name}.csv'
    
    # add jv, ja and weights values in the first row 
    header_df = pd.DataFrame([header_values])
    header_df.to_csv(DO_filename, index=False)
    header_df.to_csv(mixingincl_DO_filename, index=False)
    
    
    # Save the result to a CSV file
    DO_2D_deox_gfdl_rcp26_hypoprof.to_csv(DO_filename,mode='a', index=False, na_rep='NaN')#, header=False)  
    DO_2D_deox_gfdl_rcp26_mixingincl.to_csv(mixingincl_DO_filename,mode='a', index=False, na_rep='NaN')



# Record the end time
end_time = time.time()

# Calculate the elapsed time
elapsed_time = end_time - start_time

# Print the elapsed time in seconds
print(f"The code took {elapsed_time} seconds to run.")



#%%RCP6.0 only with Jz

import time

######managemnet test
os.chdir ('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/gfdl_senarios/rcp60_C_daily_VHOD_mangement_test')


start_time = time.time()

for par_jz in jz_management_test:
    p1 = par_jz[0]
    
    header_values = {'Jz': p1}
    # Round Ja and Jv to 3 decimal places
    Jz_name = round(p1, 3)


    DO_2D_deox_gfdl_rcp60_hypoprof =do_model_comprehensive_VHOD_gotm([p1 , 1], density_difference_surf_top_hypo_gfdl_rcp60_indexed , np.array(tem_gfdl_rcp60_surf,dtype='<i4') , hypo_morpho_vriables_gotm_grid 
                               ,temp_gfdl_rcp60_hypo_TB ,kz_gfdl_rcp60_hypo_TB , replanishmnet_rate= 2.7946  )[0]
    

    DO_2D_deox_gfdl_rcp60_mixingincl =mixing_incl_do_model_comprehensive_VHOD_gotm([p1 , 1], density_difference_surf_top_hypo_gfdl_rcp60_indexed , np.array(tem_gfdl_rcp60_surf,dtype='<i4') , hypo_morpho_vriables_gotm_grid 
                               ,temp_gfdl_rcp60_hypo_TB ,kz_gfdl_rcp60_hypo_TB , replanishmnet_rate= 2.7946  )[0]
    
    
    
    # Create a DataFrame for result
    DO_2D_deox_gfdl_rcp60_hypoprof = pd.DataFrame(DO_2D_deox_gfdl_rcp60_hypoprof, columns=[f'{depth}m' for depth in unique_z_m_gotm_hypo_TB])
    DO_2D_deox_gfdl_rcp60_mixingincl= pd.DataFrame(DO_2D_deox_gfdl_rcp60_mixingincl, columns=[f'{depth}m' for depth in unique_z_m_gotm_hypo_TB])
    # Add a column for dates
    DO_2D_deox_gfdl_rcp60_hypoprof.insert(0, 'Datetime', formatted_time_series_gfdl_rcp60)  # Replace 'your_date_array' with your actual date array
    DO_2D_deox_gfdl_rcp60_mixingincl.insert(0, 'Datetime', formatted_time_series_gfdl_rcp60)  # Replace 'your_date_array' with your actual date array
      
    # Define the filename
    DO_filename = f'DO_prof_gfdl_rcp60_Jz_{Jz_name}.csv'
    mixingincl_DO_filename = f'mixingincl_DO_prof_gfdl_rcp60_Jz_{Jz_name}.csv'
    
    # add jv, ja and weights values in the first row 
    header_df = pd.DataFrame([header_values])
    header_df.to_csv(DO_filename, index=False)
    header_df.to_csv(mixingincl_DO_filename, index=False)
    
    
    # Save the result to a CSV file
    DO_2D_deox_gfdl_rcp60_hypoprof.to_csv(DO_filename,mode='a', index=False, na_rep='NaN')#, header=False)  
    DO_2D_deox_gfdl_rcp60_mixingincl.to_csv(mixingincl_DO_filename,mode='a', index=False, na_rep='NaN')



# Record the end time
end_time = time.time()

# Calculate the elapsed time
elapsed_time = end_time - start_time

# Print the elapsed time in seconds
print(f"The code took {elapsed_time} seconds to run.")



#%%RCP8.5 only with Jz

import time

######managemnet test
os.chdir ('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/gfdl_senarios/rcp85_C_daily_VHOD_mangement_test')


start_time = time.time()

for par_jz in jz_management_test:
    p1 = par_jz[0]
    
    header_values = {'Jz': p1}
    # Round Ja and Jv to 3 decimal places
    Jz_name = round(p1, 3)


    DO_2D_deox_gfdl_rcp85_hypoprof =do_model_comprehensive_VHOD_gotm([p1 , 1], density_difference_surf_top_hypo_gfdl_rcp85_indexed , np.array(tem_gfdl_rcp85_surf,dtype='<i4') , hypo_morpho_vriables_gotm_grid 
                               ,temp_gfdl_rcp85_hypo_TB ,kz_gfdl_rcp85_hypo_TB , replanishmnet_rate= 2.7946  )[0]
    

    DO_2D_deox_gfdl_rcp85_mixingincl =mixing_incl_do_model_comprehensive_VHOD_gotm([p1 , 1], density_difference_surf_top_hypo_gfdl_rcp85_indexed , np.array(tem_gfdl_rcp85_surf,dtype='<i4') , hypo_morpho_vriables_gotm_grid 
                               ,temp_gfdl_rcp85_hypo_TB ,kz_gfdl_rcp85_hypo_TB , replanishmnet_rate= 2.7946  )[0]
    
    
    
    # Create a DataFrame for result
    DO_2D_deox_gfdl_rcp85_hypoprof = pd.DataFrame(DO_2D_deox_gfdl_rcp85_hypoprof, columns=[f'{depth}m' for depth in unique_z_m_gotm_hypo_TB])
    DO_2D_deox_gfdl_rcp85_mixingincl= pd.DataFrame(DO_2D_deox_gfdl_rcp85_mixingincl, columns=[f'{depth}m' for depth in unique_z_m_gotm_hypo_TB])
    # Add a column for dates
    DO_2D_deox_gfdl_rcp85_hypoprof.insert(0, 'Datetime', formatted_time_series_gfdl_rcp85)  # Replace 'your_date_array' with your actual date array
    DO_2D_deox_gfdl_rcp85_mixingincl.insert(0, 'Datetime', formatted_time_series_gfdl_rcp85)  # Replace 'your_date_array' with your actual date array
      
    # Define the filename
    DO_filename = f'DO_prof_gfdl_rcp85_Jz_{Jz_name}.csv'
    mixingincl_DO_filename = f'mixingincl_DO_prof_gfdl_rcp85_Jz_{Jz_name}.csv'
    
    # add jv, ja and weights values in the first row 
    header_df = pd.DataFrame([header_values])
    header_df.to_csv(DO_filename, index=False)
    header_df.to_csv(mixingincl_DO_filename, index=False)
    
    
    # Save the result to a CSV file
    DO_2D_deox_gfdl_rcp85_hypoprof.to_csv(DO_filename,mode='a', index=False, na_rep='NaN')#, header=False)  
    DO_2D_deox_gfdl_rcp85_mixingincl.to_csv(mixingincl_DO_filename,mode='a', index=False, na_rep='NaN')



# Record the end time
end_time = time.time()

# Calculate the elapsed time
elapsed_time = end_time - start_time

# Print the elapsed time in seconds
print(f"The code took {elapsed_time} seconds to run.")













#%%Using metrics for 

#1. DO hypolimnetic average 

#%%his
import os
import pandas as pd

# Specify the directory where the CSV files are located


#########original test with variable theta:
#########directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/gfdl_senarios/his'

######original test : variable theta: not ave temp in two days in rows 
######directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/gfdl_senarios/his_notavetemp'




########fixed theta both in calib and simulation 
########directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/gfdl_senarios/his_fixedtheta'


###### test with fixed theta at onset temp
##### directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/gfdl_senarios/his_fixedtheta_at_temp_onset'



######test ave temp onset to deep hypoxia
########directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/gfdl_senarios/his_fixedtheta_at_tempave_onsettodeephypoxia'




# test with fixed theta in calibration but variable for GOTM simulation 
directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/gfdl_senarios/his_calibinfixedtheta_simuvartheta'



# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("DO_prof_gfdl_his_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr = hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the hypolimnetic_ave function
        result = hypolimnetic_ave(C, Vr, time_series)

        # Set time_series as the index
        result.index = time_series
        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'hypolimnetic_ave_gfdl_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename), index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='Datetime', na_rep='NaN', header=['Hypolimnetic_Ave'])
        
             
#%%rcp26
import os
import pandas as pd

# Specify the directory where the CSV files are located
#########original test with variable theta:
#########directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/gfdl_senarios/rcp26'


######attribution test  on initial condition
######directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/gfdl_senarios/rcp26_initialcond_attribution'



######attribution test  on initial condition fixed at intercpt
directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/gfdl_senarios/rcp26_initialcond_fixedintercpt_attribution'



######original test : variable theta: not ave temp in two days in rows 
######directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/gfdl_senarios/rcp26_notavetemp'




######## fixed theta both in calib and simulation 
#########directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/gfdl_senarios/rcp26_fixedtheta'


###### test with fixed theta in calibration a temp ave hypo in gfd rcp26 for years 2020 and 2021
########directory='C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/gfdl_senarios/rcp26_fixedthetaincalib_simurcp26temp20202021'




###### test with fixed theta in calibration at onset temp ave hypo in gfdl rcp26 for years 2020 and 2021
#####directory='C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/gfdl_senarios/rcp26_fixedthetaincalib_at_temp_onsetsimurcp26'


######test ave temp onset to deep hypoxia
########directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/gfdl_senarios/rcp26_fixedtheta_at_tempave_onsettodeephypoxia'


###### test with fixed theta in calibration but variable for GOTM simulation 
######directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/gfdl_senarios/rcp26_calibinfixedtheta_simuvartheta'



# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("DO_prof_gfdl_rcp26_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr = hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the hypolimnetic_ave function
        result = hypolimnetic_ave(C, Vr, time_series)

        # Set time_series as the index
        result.index = time_series
        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'hypolimnetic_ave_gfdl_rcp26_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename), index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='Datetime', na_rep='NaN', header=['Hypolimnetic_Ave'])
        
        

#%%rcp60
import os
import pandas as pd

# Specify the directory where the CSV files are located
#########original test with variable theta:
#########directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/gfdl_senarios/rcp60'


######original test : variable theta: not ave temp in two days in rows 
#######directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/gfdl_senarios/rcp60_notavetemp'



######## fixed theta both in calib and simulation 
#######directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/gfdl_senarios/rcp60_fixedtheta'


###### test with fixed theta in calibration a temp ave hypo in gfd rcp60 for years 2020 and 2021
########directory ='C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/gfdl_senarios/rcp60_fixedthetaincalib_simurcp60temp20202021'



###### test with fixed theta in calibration at onset temp ave hypo in gfdl rcp60 for years 2020 and 2021
#####directory='C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/gfdl_senarios/rcp60_fixedthetaincalib_at_temp_onsetsimurcp60'


######test ave temp onset to deep hypoxia
######directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/gfdl_senarios/rcp60_fixedtheta_at_tempave_onsettodeephypoxia'


# test with fixed theta in calibration but variable for GOTM simulation 
directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/gfdl_senarios/rcp60_calibinfixedtheta_simuvartheta'




# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("DO_prof_gfdl_rcp60_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr = hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the hypolimnetic_ave function
        result = hypolimnetic_ave(C, Vr, time_series)

        # Set time_series as the index
        result.index = time_series
        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'hypolimnetic_ave_gfdl_rcp60_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename), index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='Datetime', na_rep='NaN', header=['Hypolimnetic_Ave'])
        
#%%rcp85
import os
import pandas as pd

# Specify the directory where the CSV files are located
#########original test with variable theta:
#########directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/gfdl_senarios/rcp85'


######original test : variable theta: not ave temp in two days in rows 
######directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/gfdl_senarios/rcp85_notavetemp'



######## fixed theta both in calib and simulation 
######## directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/gfdl_senarios/rcp85_fixedtheta'



###### test with fixed theta in calibration a temp ave hypo in gfd rcp85 for years 2020 and 2021
########directory= 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/gfdl_senarios/rcp85_fixedthetaincalib_simurcp85temp20202021'


###### test with fixed theta in calibration at onset temp ave hypo in gfdl rcp85 for years 2020 and 2021
#####directory='C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/gfdl_senarios/rcp85_fixedthetaincalib_at_temp_onsetsimurcp85'


######test fixed theta in ave temp onset to deep hypoxia
directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/gfdl_senarios/rcp85_fixedtheta_at_tempave_onsettodeephypoxia'

# test with fixed theta in calibration but variable for GOTM simulation 
########directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/gfdl_senarios/rcp85_calibinfixedtheta_simuvartheta'



# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("DO_prof_gfdl_rcp85_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr = hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the hypolimnetic_ave function
        result = hypolimnetic_ave(C, Vr, time_series)

        # Set time_series as the index
        result.index = time_series
        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'hypolimnetic_ave_gfdl_rcp85_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename), index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='Datetime', na_rep='NaN', header=['Hypolimnetic_Ave'])
        
                

#%%Using metrics:
    
Vr_Erk= hypo_morpho_vriables_gotm_grid[0]
Al_Erk=hypo_morpho_vriables_gotm_grid[2] 
Z_hypo_TB_Erk= unique_z_m_gotm[0:14][::-1]




#%% annual deoxygenation period of different scenarios:
#allsenarios_deoxygenation_periods

os.chdir ('C:/Users/mahta/OneDrive/Documents/all_python_coding/Future_simulation_results/gfdl_senarios')
    

import numpy as np

plt.figure(figsize=(10, 8))    

# Data
data_gfdl_his = annual_deox_duration(df_deox_period_surf_gfdl_his)
data_gfdl_rcp26 = annual_deox_duration(df_deox_period_surf_gfdl_rcp26)
data_gfdl_rcp60 = annual_deox_duration(df_deox_period_surf_gfdl_rcp60)

# Plot data
plt.plot(data_gfdl_his, label='gfdl_his', color='grey')#marker='o',
plt.plot(data_gfdl_rcp26, label='gfdl_rcp26',  color='g')#marker='o',
plt.plot(data_gfdl_rcp60, label='gfdl_rcp60',  color='b')#marker='o',


# Calculate trendlines
trendline_his = np.polyfit(data_gfdl_his.index, data_gfdl_his, 1)
trendline_values_his = np.polyval(trendline_his, data_gfdl_his.index)
plt.plot(data_gfdl_his.index, trendline_values_his, linestyle='--', color='grey')
#plt.text(2000, trendline_values_his[0], f'y = {trendline_his[0]:.2f}x + {trendline_his[1]:.2f}', color='k')
#trendline_his[0]
#0.028936387970398533


trendline_rcp26 = np.polyfit(data_gfdl_rcp26.index, data_gfdl_rcp26, 1)
trendline_values_rcp26 = np.polyval(trendline_rcp26, data_gfdl_rcp26.index)
plt.plot(data_gfdl_rcp26.index, trendline_values_rcp26, linestyle='--', color='g')
#plt.text(2000, trendline_values_rcp26[0], f'y = {trendline_rcp26[0]:.2f}x + {trendline_rcp26[1]:.2f}', color='k')
#trendline_rcp26[0]#slop of trendline
#0.004414261460102711


trendline_rcp60 = np.polyfit(data_gfdl_rcp60.index, data_gfdl_rcp60, 1)
trendline_values_rcp60 = np.polyval(trendline_rcp60, data_gfdl_rcp60.index)
plt.plot(data_gfdl_rcp60.index, trendline_values_rcp60, linestyle='--', color='b')
#plt.text(2000, trendline_values_rcp60[0], f'y = {trendline_rcp60[0]:.2f}x + {trendline_rcp60[1]:.2f}', color='k')
#trendline_rcp60[0]#slop of trendline
#0.08121229635516368

# Set the y-axis limits with an interval of 25
y_ticks = np.arange(0, 176, 50)
plt.yticks(y_ticks)

plt.ylabel('Annual deoxygenation duration [d]')
plt.xlabel('Year')
plt.legend(loc='lower center')

plt.savefig("gfdl_allsenarios_deoxygenation_periods.png", dpi=300)

#%%end Jday 


os.chdir ('C:/Users/mahta/OneDrive/Documents/all_python_coding/Future_simulation_results/gfdl_senarios')

# Combine the datasets and create labels for the legend
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

# Combine the datasets and create labels for the legend
combined_data = [df_deox_period_surf_gfdl_his['end_dates_Jday'], df_deox_period_surf_gfdl_rcp26['end_dates_Jday'], df_deox_period_surf_gfdl_rcp60['end_dates_Jday']]
labels = ['gfdl_his', 'gfdl_rcp26', 'gfdl_rcp60']

# Define a custom color palette
custom_palette = ['grey', 'green', 'blue']

# Create a violin plot with custom colors for each dataset
plt.figure(figsize=(8, 6))
ax = sns.violinplot(data=combined_data, palette=custom_palette)  # Use custom color palette
ax.set_xticklabels([])  # Remove x-axis labels
plt.ylabel('Turnover date [Jday]')

# Create custom legend
legend_elements = [Line2D([0], [0], marker='o', color='w', markerfacecolor=color, markersize=10, label=label) for color, label in zip(custom_palette, labels)]
ax.legend(handles=legend_elements)


plt.savefig("gfdl_allsenarios_enddateJday.png", dpi=300)



#%%start date- Jday  

os.chdir ('C:/Users/mahta/OneDrive/Documents/all_python_coding/Future_simulation_results/gfdl_senarios')

# Combine the datasets and create labels for the legend
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

# Combine the datasets and create labels for the legend
combined_data = [df_deox_period_surf_gfdl_his['start_dates_Jday'], df_deox_period_surf_gfdl_rcp26['start_dates_Jday'], df_deox_period_surf_gfdl_rcp60['start_dates_Jday']]
labels = ['gfdl_his', 'gfdl_rcp26', 'gfdl_rcp60']

# Define a custom color palette
custom_palette = ['grey', 'green', 'blue']

# Create a violin plot with custom colors for each dataset
plt.figure(figsize=(8, 6))
ax = sns.violinplot(data=combined_data, palette=custom_palette)  # Use custom color palette
ax.set_xticklabels([])  # Remove x-axis labels
plt.ylabel('Onset date [Jday]')

# Create custom legend
legend_elements = [Line2D([0], [0], marker='o', color='w', markerfacecolor=color, markersize=10, label=label) for color, label in zip(custom_palette, labels)]
ax.legend(handles=legend_elements)


plt.savefig("gfdl_allsenarios_startdateJday.png", dpi=300)


#%%combined deoxygenation informations datafrme togther

import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

# Data for the first plot
data_gfdl_his = annual_deox_duration(df_deox_period_surf_gfdl_his)
data_gfdl_rcp26 = annual_deox_duration(df_deox_period_surf_gfdl_rcp26)
data_gfdl_rcp60 = annual_deox_duration(df_deox_period_surf_gfdl_rcp60)

# Data for the second plot
combined_data_jday = [df_deox_period_surf_gfdl_his['end_dates_Jday'], df_deox_period_surf_gfdl_rcp26['end_dates_Jday'], df_deox_period_surf_gfdl_rcp60['end_dates_Jday']]

# Data for the third plot
combined_data_start_jday = [df_deox_period_surf_gfdl_his['start_dates_Jday'], df_deox_period_surf_gfdl_rcp26['start_dates_Jday'], df_deox_period_surf_gfdl_rcp60['start_dates_Jday']]

labels = ['gfdl_his', 'gfdl_rcp26', 'gfdl_rcp60']
custom_palette = ['grey', 'green', 'blue']

# Create subplots
fig, axs = plt.subplots(3, 1, figsize=(10, 24))

# Plot 1: Annual deoxygenation duration
axs[0].plot(data_gfdl_his, label='gfdl_his', color='grey')
axs[0].plot(data_gfdl_rcp26, label='gfdl_rcp26', color='g')
axs[0].plot(data_gfdl_rcp60, label='gfdl_rcp60', color='b')

# Add trendlines if needed
# ...

axs[0].set_ylabel('Annual deoxygenation duration [d]')
axs[0].set_xlabel('Year')
axs[0].set_yticks(np.aranfge(0, 176, 50))
axs[0].legend(loc='lower center')

# Plot 2: End Dates Jday
axs[1] = sns.violinplot(data=combined_data_jday, palette=custom_palette, ax=axs[1])
axs[1].set_xticklabels([])
axs[1].set_ylabel('Turnover date [Jday]')

# Create custom legend for Plot 2
legend_elements = [Line2D([0], [0], marker='o', color='w', markerfacecolor=color, markersize=10, label=label) for color, label in zip(custom_palette, labels)]
axs[1].legend(handles=legend_elements)

# Plot 3: Start Dates Jday
axs[2] = sns.violinplot(data=combined_data_start_jday, palette=custom_palette, ax=axs[2])
axs[2].set_xticklabels([])
axs[2].set_ylabel('Onset date [Jday]')

# Create custom legend for Plot 3
axs[2].legend(handles=legend_elements)

# Adjust spacing between subplots
plt.tight_layout()

plt.savefig("gfdl_allsenarios_deox_info_duration_Jdayd_start_end.png", dpi=300)



#%%

Z_hypo_TB_Erk

formatted_time_series_gfdl_his
df_temp_deox_gfdl_his_hypoprof
df_kz_deox_gfdl_his_hypoprof


formatted_time_series_gfdl_rcp26
df_temp_deox_gfdl_rcp26_hypoprof
df_kz_deox_gfdl_rcp26_hypoprof


formatted_time_series_gfdl_rcp60
df_temp_deox_gfdl_rcp60_hypoprof
df_kz_deox_gfdl_rcp60_hypoprof

#%%hist-temp_ave_nnual
import matplotlib.pyplot as plt
import numpy as np
df_kz_deox_gfdl_rcp26_hypoprof

######

df_temp_deox_gfdl_his = pd.DataFrame(df_temp_deox_gfdl_his_hypoprof)

df_temp_deox_gfdl_his= df_temp_deox_gfdl_his.set_index (pd.to_datetime(formatted_time_series_gfdl_his))

df_temp_gfdl_his_deox=df_temp_deox_gfdl_his.dropna()


temp_prof_deox_annual_period=df_temp_gfdl_his_deox.groupby(df_temp_gfdl_his_deox.index.year).mean()

year_prof_deox_annual_period=df_temp_gfdl_his_deox.index.year.unique()


# Assuming you have a 2D array with shape (n, m), and Z_hypo_TB_Erk and formatted_time_series as described
n, m = temp_prof_deox_annual_period.shape
Z_hypo_TB_Erk = np.array([-14.25, -14.75, -15.25, -15.75, -16.25, -16.75, -17.25, -17.75, -18.25, -18.75, -19.25, -19.75, -20.25, -20.75])


# Create a meshgrid for the contour plot
X, Y = np.meshgrid(year_prof_deox_annual_period, Z_hypo_TB_Erk)


data = temp_prof_deox_annual_period.values


# Transpose the data
data = data.T

# Create the contour plot
plt.figure(figsize=(12, 10))
contour = plt.contourf(X, Y, data,levels=np.arange(6, 15, 0.5), cmap='RdBu')  # Change the colormap as needed

# Add labels and title
plt.xlabel('Year')
plt.ylabel('Depth [m]')
plt.title('Annaul temperature profile during deoxygen period')

# Add a colorbar
colorbar = plt.colorbar(contour)
colorbar.set_label('Temp [°C]')  # Add label to the colorbar


plt.savefig('Annual_temperature_profile_gfdl_his_deox_period.png' , dpi=300)
# Show the plot
plt.show()

#%%his kz

df_kz_deox_gfdl_his = pd.DataFrame(df_kz_deox_gfdl_his_hypoprof)

df_kz_deox_gfdl_his= df_kz_deox_gfdl_his.set_index (pd.to_datetime(formatted_time_series_gfdl_his))

df_kz_gfdl_his_deox=df_kz_deox_gfdl_his.dropna()


kz_prof_deox_annual_period=df_kz_gfdl_his_deox.groupby(df_kz_gfdl_his_deox.index.year).mean()

year_prof_deox_annual_period=df_kz_gfdl_his_deox.index.year.unique()


# Assuming you have a 2D array with shape (n, m), and Z_hypo_TB_Erk and formatted_time_series as described
n, m = kz_prof_deox_annual_period.shape
Z_hypo_TB_Erk = np.array([-14.25, -14.75, -15.25, -15.75, -16.25, -16.75, -17.25, -17.75, -18.25, -18.75, -19.25, -19.75, -20.25, -20.75])


# Create a meshgrid for the contour plot
X, Y = np.meshgrid(year_prof_deox_annual_period, Z_hypo_TB_Erk)


data = kz_prof_deox_annual_period.values


# Transpose the data
data = data.T

# Create the contour plot
plt.figure(figsize=(12, 10))
contour = plt.contourf(X, Y, data, levels=np.arange(10**-7, 2*10**-4, 10**-6) , cmap='RdBu')  # Change the colormap as needed

# Add labels and title
plt.xlabel('Year')
plt.ylabel('Depth [m]')
plt.title('Annaul diffusivity coefficient profile during deoxygen period')

# Add a colorbar
#colorbar = plt.colorbar(contour)
#colorbar.set_label('kz[m s$^{-2}$]')  # Add label to the colorbar

colorbar = plt.colorbar(contour, format='%.0e')  # Use scientific notation format
colorbar.set_label(r'$ kz \, [\mathrm{m \, s^{-2}}]$')  # Use LaTeX for formatting

plt.savefig('Annual_kz_profile_gfdl_his_deox_period.png' , dpi=300)
# Show the plot
plt.show()

#%%
#%%rcp26t-temp_ave_nnual
import matplotlib.pyplot as plt
import numpy as np
df_kz_deox_gfdl_rcp26_hypoprof

######

df_temp_deox_gfdl_rcp26 = pd.DataFrame(df_temp_deox_gfdl_rcp26_hypoprof)

df_temp_deox_gfdl_rcp26= df_temp_deox_gfdl_rcp26.set_index (pd.to_datetime(formatted_time_series_gfdl_rcp26))

df_temp_gfdl_rcp26_deox=df_temp_deox_gfdl_rcp26.dropna()


temp_prof_deox_annual_period=df_temp_gfdl_rcp26_deox.groupby(df_temp_gfdl_rcp26_deox.index.year).mean()

year_prof_deox_annual_period=df_temp_gfdl_rcp26_deox.index.year.unique()


# Assuming you have a 2D array with shape (n, m), and Z_hypo_TB_Erk and formatted_time_series as described
n, m = temp_prof_deox_annual_period.shape
Z_hypo_TB_Erk = np.array([-14.25, -14.75, -15.25, -15.75, -16.25, -16.75, -17.25, -17.75, -18.25, -18.75, -19.25, -19.75, -20.25, -20.75])


# Create a meshgrid for the contour plot
X, Y = np.meshgrid(year_prof_deox_annual_period, Z_hypo_TB_Erk)


data = temp_prof_deox_annual_period.values


# Transpose the data
data = data.T

# Create the contour plot
plt.figure(figsize=(12, 10))
contour = plt.contourf(X, Y, data,levels=np.arange(6, 15, 0.5), cmap='RdBu')  # Change the colormap as needed

# Add labels and title
plt.xlabel('Year')
plt.ylabel('Depth [m]')
plt.title('Annaul temperature profile during deoxygen period')

# Add a colorbar
colorbar = plt.colorbar(contour)
colorbar.set_label('Temp [°C]')  # Add label to the colorbar


plt.savefig('Annual_temperature_profile_gfdl_rcp26_deox_period.png' , dpi=300)
# Show the plot
plt.show()

#%%rcp26 kz

df_kz_deox_gfdl_rcp26 = pd.DataFrame(df_kz_deox_gfdl_rcp26_hypoprof)

df_kz_deox_gfdl_rcp26= df_kz_deox_gfdl_rcp26.set_index (pd.to_datetime(formatted_time_series_gfdl_rcp26))

df_kz_gfdl_rcp26_deox=df_kz_deox_gfdl_rcp26.dropna()


kz_prof_deox_annual_period=df_kz_gfdl_rcp26_deox.groupby(df_kz_gfdl_rcp26_deox.index.year).mean()

year_prof_deox_annual_period=df_kz_gfdl_rcp26_deox.index.year.unique()


# Assuming you have a 2D array with shape (n, m), and Z_hypo_TB_Erk and formatted_time_series as described
n, m = kz_prof_deox_annual_period.shape
Z_hypo_TB_Erk = np.array([-14.25, -14.75, -15.25, -15.75, -16.25, -16.75, -17.25, -17.75, -18.25, -18.75, -19.25, -19.75, -20.25, -20.75])


# Create a meshgrid for the contour plot
X, Y = np.meshgrid(year_prof_deox_annual_period, Z_hypo_TB_Erk)


data = kz_prof_deox_annual_period.values


# Transpose the data
data = data.T

# Create the contour plot
plt.figure(figsize=(12, 10))
contour = plt.contourf(X, Y, data, levels=np.arange(10**-7, 2*10**-4, 10**-6) , cmap='RdBu')  # Change the colormap as needed

# Add labels and title
plt.xlabel('Year')
plt.ylabel('Depth [m]')
plt.title('Annaul diffusivity coefficient profile during deoxygen period')

# Add a colorbar
#colorbar = plt.colorbar(contour)
#colorbar.set_label('kz[m s$^{-2}$]')  # Add label to the colorbar

colorbar = plt.colorbar(contour, format='%.0e')  # Use scientific notation format
colorbar.set_label(r'$ kz \, [\mathrm{m \, s^{-2}}]$')  # Use LaTeX for formatting

plt.savefig('Annual_kz_profile_gfdl_rcp26_deox_period.png' , dpi=300)
# Show the plot
plt.show()

#%%rcp60

#%%rcp60t-temp_ave_nnual
import matplotlib.pyplot as plt
import numpy as np
df_kz_deox_gfdl_rcp60_hypoprof

######

df_temp_deox_gfdl_rcp60 = pd.DataFrame(df_temp_deox_gfdl_rcp60_hypoprof)

df_temp_deox_gfdl_rcp60= df_temp_deox_gfdl_rcp60.set_index (pd.to_datetime(formatted_time_series_gfdl_rcp60))

df_temp_gfdl_rcp60_deox=df_temp_deox_gfdl_rcp60.dropna()


temp_prof_deox_annual_period=df_temp_gfdl_rcp60_deox.groupby(df_temp_gfdl_rcp60_deox.index.year).mean()

year_prof_deox_annual_period=df_temp_gfdl_rcp60_deox.index.year.unique()


# Assuming you have a 2D array with shape (n, m), and Z_hypo_TB_Erk and formatted_time_series as described
n, m = temp_prof_deox_annual_period.shape
Z_hypo_TB_Erk = np.array([-14.25, -14.75, -15.25, -15.75, -16.25, -16.75, -17.25, -17.75, -18.25, -18.75, -19.25, -19.75, -20.25, -20.75])


# Create a meshgrid for the contour plot
X, Y = np.meshgrid(year_prof_deox_annual_period, Z_hypo_TB_Erk)


data = temp_prof_deox_annual_period.values


# Transpose the data
data = data.T

# Create the contour plot
plt.figure(figsize=(12, 10))
contour = plt.contourf(X, Y, data,levels=np.arange(6, 15, 0.5), cmap='RdBu')  # Change the colormap as needed

# Add labels and title
plt.xlabel('Year')
plt.ylabel('Depth [m]')
plt.title('Annaul temperature profile during deoxygen period')

# Add a colorbar
colorbar = plt.colorbar(contour)
colorbar.set_label('Temp [°C]')  # Add label to the colorbar


plt.savefig('Annual_temperature_profile_gfdl_rcp60_deox_period.png' , dpi=300)
# Show the plot
plt.show()

#%%rcp60 kz

df_kz_deox_gfdl_rcp60 = pd.DataFrame(df_kz_deox_gfdl_rcp60_hypoprof)

df_kz_deox_gfdl_rcp60= df_kz_deox_gfdl_rcp60.set_index (pd.to_datetime(formatted_time_series_gfdl_rcp60))

df_kz_gfdl_rcp60_deox=df_kz_deox_gfdl_rcp60.dropna()


kz_prof_deox_annual_period=df_kz_gfdl_rcp60_deox.groupby(df_kz_gfdl_rcp60_deox.index.year).mean()

year_prof_deox_annual_period=df_kz_gfdl_rcp60_deox.index.year.unique()


# Assuming you have a 2D array with shape (n, m), and Z_hypo_TB_Erk and formatted_time_series as described
n, m = kz_prof_deox_annual_period.shape
Z_hypo_TB_Erk = np.array([-14.25, -14.75, -15.25, -15.75, -16.25, -16.75, -17.25, -17.75, -18.25, -18.75, -19.25, -19.75, -20.25, -20.75])


# Create a meshgrid for the contour plot
X, Y = np.meshgrid(year_prof_deox_annual_period, Z_hypo_TB_Erk)


data = kz_prof_deox_annual_period.values


# Transpose the data
data = data.T

# Create the contour plot
plt.figure(figsize=(12, 10))
contour = plt.contourf(X, Y, data, levels=np.arange(10**-7, 2*10**-4, 10**-6) , cmap='RdBu')  # Change the colormap as needed

# Add labels and title
plt.xlabel('Year')
plt.ylabel('Depth [m]')
plt.title('Annaul diffusivity coefficient profile during deoxygen period')

# Add a colorbar
#colorbar = plt.colorbar(contour)
#colorbar.set_label('kz[m s$^{-2}$]')  # Add label to the colorbar

colorbar = plt.colorbar(contour, format='%.0e')  # Use scientific notation format
colorbar.set_label(r'$ kz \, [\mathrm{m \, s^{-2}}]$')  # Use LaTeX for formatting

plt.savefig('Annual_kz_profile_gfdl_rcp60_deox_period.png' , dpi=300)
# Show the plot
plt.show()

















#%%his=======
#%% His_Annual hypo DO ave


#time_series->formatted_time_series_gfdl_his

os.chdir ('C:/Users/mahta/OneDrive/Documents/all_python_coding/Future_simulation_results/gfdl_senarios/his')

import seaborn as sns

# Set a custom color palette for better distinguishability
#
#for creating a plate using in each line color:
    
colors = plt.get_cmap('tab20').colors    
    
#sns.set_palette("Set1")
plt.figure(figsize=(20, 15))

all_output= pd.DataFrame([])

for i, (index, row) in enumerate(df_winner_of_all.iterrows()):
    p1 = row['Jv']
    p2 = row['Ja']

    # Round Ja and Jv to 3 decimal places
    Jv_name = round(p1, 3)
    Ja_name = round(p2, 3)

    DO_filename = f'DO_prof_gfdl_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'

    # Read the CSV file
    df_result = pd.read_csv(DO_filename, header=None, na_values=['NaN'])  
    
    output = hypolimnetic_ave(df_result, Vr_Erk, formatted_time_series_gfdl_his)

    output.index = pd.to_datetime(output.index)


    all_output = pd.concat([all_output, output], axis=1)# a dataframe with in ecah column different JAJV combinations
    # and each line the daily hypolimnetic do 
    
    #for plotting I want to get the 1. DO hypo annual average  
    
    annual_output_ave= output.groupby(output.index.year).mean() 
    
   
    plt.plot(annual_output_ave.index, annual_output_ave.values, 
            label='Jv: {}, Ja: {}'.format(Jv_name, Ja_name), 
            linestyle='-', marker='o', color=colors[i % len(colors)]) 
   
    #plt.plot(annual_output_ave.index, annual_output_ave.values, label='Jv: {}, Ja: {}'.format(Jv_name, Ja_name) , 
    #         linestyle='-', marker='o')#, marker='o', s=100, label='Jv: {}, Ja: {}'.format(Jv_name, Ja_name))
    
    
    # 2. DO hypo average for several critical monthes 
    
    

plt.ylabel('Annual hypolimnetic DO average [g m$^{-3}$]')
plt.title('Average of hypolimnetic DO during deoxygenation periods of each year')   
plt.legend(bbox_to_anchor=(0.9, 1.06), loc='upper left')
    
plt.savefig("annual_DO_ave_his.png", dpi=300)
    




#%%rcp26=========

#%%rcp26- Annual hypo DO ave



#time_series->formatted_time_series_gfdl_rcp26

os.chdir ('C:/Users/mahta/OneDrive/Documents/all_python_coding/Future_simulation_results/gfdl_senarios/rcp26')

import seaborn as sns

# Set a custom color palette for better distinguishability
#
#for creating a plate using in each line color:
    
colors = plt.get_cmap('tab20').colors    
    
#sns.set_palette("Set1")
plt.figure(figsize=(20, 15))

all_output= pd.DataFrame([])

for i, (index, row) in enumerate(df_winner_of_all.iterrows()):
    p1 = row['Jv']
    p2 = row['Ja']

    # Round Ja and Jv to 3 decimal places
    Jv_name = round(p1, 3)
    Ja_name = round(p2, 3)

    DO_filename = f'DO_prof_gfdl_rcp26_Jv_{Jv_name}_Ja_{Ja_name}.csv'

    # Read the CSV file
    df_result = pd.read_csv(DO_filename, header=None, na_values=['NaN'])  
    
    output = hypolimnetic_ave(df_result, Vr_Erk, formatted_time_series_gfdl_rcp26)

    output.index = pd.to_datetime(output.index)


    all_output = pd.concat([all_output, output], axis=1)# a dataframe with in ecah column different JAJV combinations
    # and each line the daily hypolimnetic do 
    
    #for plotting I want to get the 1. DO hypo annual average  
    
    annual_output_ave= output.groupby(output.index.year).mean() 
    
   
    plt.plot(annual_output_ave.index, annual_output_ave.values, 
            label='Jv: {}, Ja: {}'.format(Jv_name, Ja_name), 
            linestyle='-', marker='o', color=colors[i % len(colors)]) 
   
    #plt.plot(annual_output_ave.index, annual_output_ave.values, label='Jv: {}, Ja: {}'.format(Jv_name, Ja_name) , 
    #         linestyle='-', marker='o')#, marker='o', s=100, label='Jv: {}, Ja: {}'.format(Jv_name, Ja_name))
    
    
    # 2. DO hypo average for several critical monthes 
    
    

plt.ylabel('Annual hypolimnetic DO average [g m$^{-3}$]')
plt.title('Average of hypolimnetic DO during deoxygenation periods of each year')   
plt.legend(bbox_to_anchor=(0.9, 1.06), loc='upper left')
    
plt.savefig("annual_DO_ave_rcp26.png", dpi=300)

#%%information about deoxygenation periods

os.chdir ('C:/Users/mahta/OneDrive/Documents/all_python_coding/Future_simulation_results/gfdl_senarios/rcp26')

deox_period_surf_gfdl_rcp26 = pd.read_csv('deox_period_surf_gfdl_rcp26.csv', na_values=['NaN'])  

deox_period_surf_gfdl_rcp26.columns


#%%rcp60

#%% rcp60- Annual hypo DO ave


#time_series->formatted_time_series_gfdl_rcp60

os.chdir ('C:/Users/mahta/OneDrive/Documents/all_python_coding/Future_simulation_results/gfdl_senarios/rcp60')

import seaborn as sns

# Set a custom color palette for better distinguishability
#
#for creating a plate using in each line color:
    
colors = plt.get_cmap('tab20').colors    
    
#sns.set_palette("Set1")
plt.figure(figsize=(20, 15))

all_output= pd.DataFrame([])

for i, (index, row) in enumerate(df_winner_of_all.iterrows()):
    p1 = row['Jv']
    p2 = row['Ja']

    # Round Ja and Jv to 3 decimal places
    Jv_name = round(p1, 3)
    Ja_name = round(p2, 3)

    DO_filename = f'DO_prof_gfdl_rcp60_Jv_{Jv_name}_Ja_{Ja_name}.csv'

    # Read the CSV file
    df_result = pd.read_csv(DO_filename, header=None, na_values=['NaN'])  
    
    output = hypolimnetic_ave(df_result, Vr_Erk, formatted_time_series_gfdl_rcp60)

    output.index = pd.to_datetime(output.index)


    all_output = pd.concat([all_output, output], axis=1)# a dataframe with in ecah column different JAJV combinations
    # and each line the daily hypolimnetic do 
    
    #for plotting I want to get the 1. DO hypo annual average  
    
    annual_output_ave= output.groupby(output.index.year).mean() 
    
   
    plt.plot(annual_output_ave.index, annual_output_ave.values, 
            label='Jv: {}, Ja: {}'.format(Jv_name, Ja_name), 
            linestyle='-', marker='o', color=colors[i % len(colors)]) 
   
    #plt.plot(annual_output_ave.index, annual_output_ave.values, label='Jv: {}, Ja: {}'.format(Jv_name, Ja_name) , 
    #         linestyle='-', marker='o')#, marker='o', s=100, label='Jv: {}, Ja: {}'.format(Jv_name, Ja_name))
    
    
    # 2. DO hypo average for several critical monthes 
    
    

plt.ylabel('Annual hypolimnetic DO average [g m$^{-3}$]')
plt.title('Average of hypolimnetic DO during deoxygenation periods of each year')   
plt.legend(bbox_to_anchor=(0.9, 1.06), loc='upper left')
    
plt.savefig("annual_DO_ave_rcp60.png", dpi=300)    





































#%% density top hypo nand surface_1stTry_RCP60


density_gotm_surf=Lab_Density(tem_gotm_surf)
density_gotm_1m=Lab_Density(tem_gotm_1m)
density_gotm_top_hypo=Lab_Density(tem_gotm_top_hypo)


density_difference_surf_top_hypo=density_gotm_surf -density_gotm_top_hypo
density_difference_1m_top_hypo=density_gotm_1m-density_gotm_top_hypo
# Convert formatted_time_datetime to a pandas Series or NumPy array
formatted_time_series = pd.Series(formatted_time_datetime)  # or np.array(formatted_time_datetime)

# Create the DataFrame with temp_diff_gotm_obsgrid_top_135 as the data and formatted_time_series as the index
formatted_time_series = pd.Series(formatted_time_datetime)



density_difference_surf_top_hypo_indexed = pd.Series(density_difference_surf_top_hypo, index=pd.to_datetime(formatted_time_series))
density_difference_surf_top_hypo_indexed.index.name = 'Datetime'


density_difference_1m_top_hypo_indexed = pd.Series(density_difference_1m_top_hypo, index=pd.to_datetime(formatted_time_series))
density_difference_1m_top_hypo_indexed.index.name = 'Datetime'


#density_difference_surf_top_hypo_indexed = pd.DataFrame({'density_difference_surf_top_hypo': density_difference_surf_top_hypo}, index=formatted_time_series)
#density_difference_1m_top_hypo_indexed= pd.DataFrame({'density_difference_1m_top_hypo': density_difference_1m_top_hypo}, index=formatted_time_series)


#%%comparsion of this scenario density profile from 2018-2022_1stTry_RCP60
#with obseved values in actual world

# resahping from top to bottom 
temp_gotm_full_prof_TB=temp_gotm_full_prof_gotmgrid[: , ::-1 ]

kz_gotm_full_prof_TB=kz_gotm_full_prof_gotmgrid[: , ::-1 ]

 
unique_z_m_gotm_TB=unique_z_m_gotm[::-1]

np.where(unique_z_m_gotm_TB == -13.75)#27
np.where(unique_z_m_gotm_TB == -14.25)#28
np.where(unique_z_m_gotm_TB == -17.25)#34
np.where(unique_z_m_gotm_TB == -0.25)#0
np.where(unique_z_m_gotm_TB == -1.25)#2

"""
array([ -0.25,  -0.75,  -1.25,  -1.75,  -2.25,  -2.75,  -3.25,  -3.75,
        -4.25,  -4.75,  -5.25,  -5.75,  -6.25,  -6.75,  -7.25,  -7.75,
        -8.25,  -8.75,  -9.25,  -9.75, -10.25, -10.75, -11.25, -11.75,
       -12.25, -12.75, -13.25, -13.75, -14.25, -14.75, -15.25, -15.75,
       -16.25, -16.75, -17.25, -17.75, -18.25, -18.75, -19.25, -19.75,
       -20.25, -20.75], dtype=float32)
"""
# 2018 start and end of obs 
np.where(formatted_time_series=='2018-05-08')# 4510

np.where(formatted_time_series=='2018-11-14')# 4700


temp_gotm_2018_matchobs=temp_gotm_full_prof_TB[4510:4701 , : ]
density_gotm_2018_matchobs=Lab_Density( temp_gotm_2018_matchobs)
density_diff_2018_sur_tophyp=density_gotm_2018_matchobs[: , 0]-density_gotm_2018_matchobs[: , 27]


# 2019 start and end of obs 
np.where(formatted_time_series=='2019-04-17')#17/04/2019 #4854

np.where(formatted_time_series=='2019-09-26')#26/09/2019 #5016


date_gotm_2019_matchobs= formatted_time_datetime [4854:5017]
temp_gotm_2019_matchobs=temp_gotm_full_prof_TB[4854:5017 , : ]
density_gotm_2019_matchobs=Lab_Density( temp_gotm_2019_matchobs)
density_diff_2019_sur_tophyp=density_gotm_2019_matchobs[:, 0]-density_gotm_2019_matchobs[:, 27]



# 2020 start and end of obs 
np.where(formatted_time_series=='2020-03-06')#06/03/2020 #5178

np.where(formatted_time_series=='2020-11-12')#12/11/2020 #5429

date_gotm_2020_matchobs= formatted_time_datetime [5178:5430]
temp_gotm_2020_matchobs= temp_gotm_full_prof_TB[5178:5430 , : ]
density_gotm_2020_matchobs=Lab_Density( temp_gotm_2020_matchobs)
density_diff_2020_sur_tophyp=density_gotm_2020_matchobs[:, 0]-density_gotm_2020_matchobs[: , 27]

# 2021 start and end of obs 
np.where(formatted_time_series=='2021-04-01')#01/04/2021 #5569

np.where(formatted_time_series=='2021-11-15')#15/11/2021 #5797

date_gotm_2021_matchobs= formatted_time_datetime [5569:5798]
temp_gotm_2021_matchobs=temp_gotm_full_prof_TB[5569:5798 , : ]
density_gotm_2021_matchobs=Lab_Density( temp_gotm_2021_matchobs)
density_diff_2021_sur_tophyp=density_gotm_2021_matchobs[: , 0]-density_gotm_2021_matchobs[: , 27]


# 2022 start and end of obs 
np.where(formatted_time_series=='2022-04-28')#28/04/2022 #5961

np.where(formatted_time_series=='2022-11-07')#07/11/2022 #6154

date_gotm_2022_matchobs= formatted_time_datetime [5961:6155]
temp_gotm_2022_matchobs=temp_gotm_full_prof_TB[5961:6155 , : ]
density_gotm_2022_matchobs=Lab_Density( temp_gotm_2022_matchobs)
density_diff_2022_sur_tophyp=density_gotm_2022_matchobs[:, 0]-density_gotm_2022_matchobs[:, 27]



#density difference of top layer and above the hypolimnion: 

densdity_diff_2018_2022_surf_tophyp=np.concatenate([density_diff_2018_sur_tophyp,  density_diff_2019_sur_tophyp, density_diff_2020_sur_tophyp , density_diff_2021_sur_tophyp , density_diff_2022_sur_tophyp])


difference_obs_density_diff=densdity_diff_2018_2022_surf_tophyp-dens_diff_top_135

abs(difference_obs_density_diff).mean()# 0.2949083001440737

(difference_obs_density_diff).mean()# -0.09089195734769291

plt.figure( figsize= (15, 10), dpi=200)
plt.scatter ( dens_diff_top_135.index , dens_diff_top_135 , label= 'obs_years')
plt.scatter (dens_diff_top_135.index ,densdity_diff_2018_2022_surf_tophyp, label= 'gotm_years')
plt.ylabel('Depth [m]')
plt.legend()
plt.savefig('dens_diff_top_135VSdensdity_diff_2018_2022_surf_tophyp.png')



plt.figure (figsize= (15, 10), dpi= 200)
plt.scatter (dens_diff_top_135.index  , difference_obs_density_diff, label='difference_obs_density_diff')
plt.ylabel('Density difgference obs and gotm rcp6')
plt.legend()
plt.savefig('Density difgference obs and gotm rcp6.png')




density_gotm_2018_2022_obsmatch=np.concatenate([density_gotm_2018_matchobs, density_gotm_2019_matchobs , density_gotm_2020_matchobs , density_gotm_2021_matchobs , density_gotm_2022_matchobs])



# Assuming density_2D_full_2018_2022 is the density data
# You may need to adjust this depending on how your data is structured
density_data = density_gotm_2018_2022_obsmatch.T  # Transpose the data if needed

# Create a grid of dates and depths
dates = datetime_unique_2018_2022
depths = unique_z_m_gotm_TB   
dates_mesh, depths_mesh = np.meshgrid(dates, depths)

# Get years from the dates
years = np.unique(np.array([np.datetime_as_string(date, unit='Y') for date in dates]))

# Calculate the number of rows and columns needed for the grid
num_rows = int(np.ceil(len(years) / 2))
num_cols = 2

# Create a grid of subplots
fig, axes = plt.subplots(num_rows, num_cols, figsize=(25, 20))

# Flatten the axes array to simplify indexing
axes = axes.flatten()

# Plot each year separately
for i, year in enumerate(years):
    year_dates = dates[np.datetime_as_string(dates, unit='Y') == year]
    year_density_data = density_data[:, np.isin(dates, year_dates)]
    
    dates_mesh, depths_mesh = np.meshgrid(year_dates, depths)
    
    # Plot in the corresponding subplot
    ax = axes[i]
    #im = ax.pcolormesh(dates_mesh, depths_mesh, year_density_data, cmap='viridis')  # Change the cmap as needed
    im = ax.pcolormesh(dates_mesh, depths_mesh, year_density_data, cmap='viridis')  # Change the cmap as needed
    #fig.colorbar(im, ax=ax, label='Density (kg m$^{-3}$)')
    ax.set_xlabel('Dates')
    ax.set_ylabel('Depth (m)')
    ax.set_title(f'Water Profile Density - Year {year}')
    ax.tick_params(axis='x', rotation=45)


# Loop through subplots and set y-axis ticks
#for ax in axes:
#    ax.set_yticks(np.arange(min(depths), max(depths) -1, 1))  # Set ticks every 1 meter
#    ax.invert_yaxis()  # Invert the y-axis to have shallower depths at the top
        
# Remove any empty subplots
for i in range(len(years), num_rows*num_cols):
    fig.delaxes(axes[i])

# Create a colorbar outside of the subplots
cbar_ax = fig.add_axes([1.1, 0.1, 0.03, 0.9])  # Adjust the parameters as needed
cbar = fig.colorbar(im, cax=cbar_ax, label='Density (kg m$^{-3}$)')
# Adjust layout
plt.tight_layout()

# Save the figure
plt.savefig('Water_Profile_Density_All_Years_gotm_2018_2022_matchobs.png', dpi=300)

# Show the plot
plt.show()


#%%comparsion of this scenario density profile from 2018-2022_1stTry_RCP60 
#with obseved values in actual world
for i, year in enumerate(years):
    year_dates = dates[np.datetime_as_string(dates, unit='Y') == year]
    year_density_data = density_data[:, np.isin(dates, year_dates)]
    
    dates_mesh, depths_mesh = np.meshgrid(year_dates, depths)
    
    # Plot in the corresponding subplot
    ax = axes[i]
    im = ax.pcolormesh(dates_mesh, depths_mesh, year_density_data, cmap='viridis')  # Change the cmap as needed
    ax.set_xlabel('Dates')
    ax.set_ylabel('Depth (m)')
    ax.set_title(f'Water Profile Density - Year {year}')
    ax.tick_params(axis='x', rotation=45)

# Remove any empty subplots
for i in range(len(years), num_rows*num_cols):
    fig.delaxes(axes[i])


# Adjust layout
plt.tight_layout()

# Save the figure
plt.savefig('Water_Profile_Density_All_Years_gotm_2018_2022_matchobs.png', dpi=300)

# Show the plot
plt.show()




#%% tempearture and density profile in 2019-2022_1stTry_RCP60
    
temp_gotm_hypo_from_top_to_bot=temp_gotm_hypo[: , ::-1] 
depth_hypo_top_bot= unique_z_m_gotm[0:14][::-1]

# Convert the 'date' column to datetime
formatted_time_series = pd.to_datetime(formatted_time_series)

# Filter the data between 2018 and 2022
subsetted_data = formatted_time_series[(formatted_time_series.dt.year >= 2018) & 
                                       (formatted_time_series.dt.year <= 2022)]


#subsetted_data = formatted_time_series[(formatted_time_series.dt.year == 2022)]




# Get the index of the start and end dates
start_index = subsetted_data.index[0]#4383# start of 2022: 5844
end_index = subsetted_data.index[-1]#6208# end of 2022: 6208


temp_gotm_hypo_2018_2022=temp_gotm_hypo_from_top_to_bot[4383:6209]

density_gotm_hypo_2018_2022=Lab_Density( temp_gotm_hypo_2018_2022)

# Create a meshgrid for dates and depths
dates_mesh, depths_mesh = np.meshgrid(subsetted_data, depth_hypo_top_bot)

# Assuming density_2D_full_2018_2022 is the density data
# You may need to adjust this depending on how your data is structured
temp_data = temp_gotm_hypo_2018_2022.T  # Transpose the data if needed

# Create the plot
plt.figure(figsize=(10, 6))
plt.pcolormesh(dates_mesh, depths_mesh, temp_data, cmap='coolwarm')  # Change the cmap as needed
plt.colorbar(label='Temperature (°C)')
plt.xlabel('Dates')
plt.ylabel('Depth (m)')
plt.title('Water Profile Temperature ')
plt.xticks(rotation=45)

# Customize date formatting
date_format = mdates.DateFormatter('%Y-%m-%d')  # Adjust the format as needed
plt.gca().xaxis.set_major_formatter(date_format)

plt.tight_layout()

# Save the figure with higher quality
#plt.savefig('water_profile_temperature_2018_2022.png', dpi=300)  # Adjust the file name and dpi as needed


#temp_data= temp_data.T








#%% testing the 2022_1stTry_RCP60
"""    
a=Lab_Density(temp_gotm_full_prof_TB[5844:6208 ,0 ]) - Lab_Density(temp_gotm_full_prof_TB[5844:6208 ,27 ])

akzhypo=kz_gotm_full_prof_TB[5845:6209 , 28:]

atemphypo=temp_gotm_hypo_TB[5844:6208]

a=[4.25,	4.25,	4.25,	4.25,	4.24,	4.24,	4.24,	4.24,	4.24,	4.24,	4.24,	4.24,	4.23,	4.23]
"""



#%% Changing Temp and Kz into from top to bottom_1stTry_RCP60


# resahping from top to bottom 
temp_gotm_full_prof_TB=temp_gotm_full_prof_gotmgrid[: , ::-1 ]

kz_gotm_full_prof_TB=kz_gotm_full_prof_gotmgrid[: , ::-1 ]

 
unique_z_m_gotm_TB=unique_z_m_gotm[::-1]

np.where(unique_z_m_gotm_TB == -13.75)#27
np.where(unique_z_m_gotm_TB == -14.25)#28
np.where(unique_z_m_gotm_TB == -17.25)#34
np.where(unique_z_m_gotm_TB == -0.25)#0
np.where(unique_z_m_gotm_TB == -1.25)#2




temp_gotm_hypo_TB =temp_gotm_full_prof_TB[:  ,28: ]#  14.25m-20.75m
temp_gotm_meta= temp_gotm_full_prof_TB[:  , 27 ]# 13.75m 

kz_gotm_hypo_TB =kz_gotm_full_prof_TB[:  , 28: ]# 14.25m-20.75m

kz_gotm_hypo_T17 =kz_gotm_full_prof_TB[:  , 28:35 ]# 14.25m-17.25m(34+1)




#%%Apply new version of coding for finding deoxygenation period_1stTry_RCP60
    
df_deox_period_1m_hypo_2006_2099=find_deox_period ( density_difference_1m_top_hypo_indexed)   

df_deox_period_surf_hypo_2006_2099=find_deox_period ( density_difference_surf_top_hypo_indexed)   

#calculate the number of yaer in each year 
"""
df_deox_period_surf_hypo_2006_2099['num_day_of_year_start']=df_deox_period_surf_hypo_2006_2099['start_dates'].dt.dayofyear

df_deox_period_surf_hypo_2006_2099['num_day_of_year_end']=df_deox_period_surf_hypo_2006_2099['end_dates'].dt.dayofyear

"""
#%%Run the function from previous manuscript named : "Theta_j" and "do_one_deox_implicit"


#%% usage new written function- do_model_comprehensive : 
params= [0.08,  0.1, 1]  

hypo_morpho_vriables_gotm_grid=[np.array (interpolated_bath['V_r'][1:15][::-1]),
                               np.array (interpolated_bath['A_s'][1:15][::-1]),
                               np.array (interpolated_bath['A_l'][1:15][::-1]),
                               0.5, np.array (interpolated_bath['V_r'][1:15][::-1]).size]#V_r, A_s, A_l, dz, nl


dens_diff_top_meta= density_difference_surf_top_hypo_indexed

temp_hypo_2D= temp_gotm_hypo_TB.copy()

kz_hypo_2D= kz_gotm_hypo_TB.copy()




  
DO_2D_2006_2099_hypoprof , temp_deox_2D_2006_2099_hypoprof , kz_deox_2D_2006_2099_hypoprof=do_model_comprehensive(params, dens_diff_top_meta , hypo_morpho_vriables_gotm_grid 
                           ,temp_hypo_2D ,kz_hypo_2D , replanishmnet_rate= 2.7946 )



#%% for specific day viewing profile of Saturation

# Extract month and day
month = formatted_time_series.dt.month
day = formatted_time_series.dt.day

# Find the indices where month is 8 and day is 15
indices = (month == 8) & (day == 1)

# Get the indices
indices_of_8_1 = indices[indices].index

#sat_deox_2D_2006_2099_hypoprof[[190, 192]]# for reading serveal index of array the desired indexs should be in a list 

sat_deox_2D_2006_2099_hypoprof[indices_of_8_1]


#%% ploting Saturation Percentage Profile for July 1st


import matplotlib.pyplot as plt
import numpy as np

# Assuming `sat_deox_2D_2006_2099_hypoprof` is a NumPy array
data = sat_deox_2D_2006_2099_hypoprof[indices_of_8_1]

# Generate x and y values for the contour plot
x = np.arange(2006, 2100)  # Assuming 94 rows
y = np.arange(-14.25, -21, -0.5)  # Assuming 14 columns

# Create a grid of x and y values
X, Y = np.meshgrid(x, y)

# Create the contour plot
plt.figure(figsize=(10, 6))
contour = plt.contourf(X, Y, data.T, cmap='viridis' , level= 5000)  # You can choose a different colormap

# Add colorbar
cbar = plt.colorbar(contour)

# Set labels and title

plt.text( 2000, 14, params ,  fontsize=12)
plt.ylabel('Depth [m]')
plt.title('Saturation Percentage Profile for July 1st')
plt.savefig('Rcp6_Saturation Percentage Profile for July 1st.png', dpi=300)
# Show the plot
plt.show()

#%% looking at the DO estimated in one year: 2022
# Extract month and day
month = formatted_time_series.dt.month
day = formatted_time_series.dt.day
year= formatted_time_series.dt.year

# Find the indices where month is 6 and day is 1
indices = (year== 2099)

# Get the indices
indices_of_2099 = indices[indices].index

DO_2D_2006_2099_hypoprof[indices_of_8_1]


#%% ploting DO profile for whole year 2099

os.chdir('C:/Users/mahta/OneDrive/Documents/all_python_coding/Future_simulation_results')

import matplotlib.pyplot as plt
import numpy as np

# Assuming `sat_deox_2D_2006_2099_hypoprof` is a NumPy array
data = DO_2D_2006_2099_hypoprof[indices_of_2022]
# Generate datetime range for 2022
dates_2099 = pd.date_range(start='2099-01-01', end='2099-12-30', freq='D')

# Assuming `data` has the same shape as the number of dates in 2022 and 14 columns
data = DO_2D_2006_2099_hypoprof[indices_of_2099]

# Generate x and y values for the contour plot
x = dates_2099  # Use the dates as x values
y = np.arange(14.25, 21, 0.5)  # Assuming 14 columns

# Create a grid of x and y values
X, Y = np.meshgrid(x, y)

# Create the contour plot
plt.figure(figsize=(10, 6))
contour = plt.contourf(X, Y, data.T, cmap='viridis', levels=2000)  # You can choose a different colormap

# Add colorbar
cbar = plt.colorbar(contour)

# Set labels and title

plt.text( pd.Timestamp('2098-11-01'), 14,  params ,  fontsize=12)
plt.ylabel('Depth [m]')
plt.title('DO profile projection for 2099- RCP6.0')

# Rotate x-axis labels
plt.xticks(rotation=45)
plt.savefig('Rcp6_DO_profile_for_2099.png', dpi=300)
# Show the plot
plt.show()



#%%Plot of annual fluction of deox_duation duration

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

new_directory = r'C:\Users\mahta\OneDrive\Documents\all_python_coding\Future_simulation_results'
os.chdir(new_directory)


# Your code to calculate the grouped sum
grouped_data = df_deox_period_surf_hypo_2006_2099.groupby(df_deox_period_surf_hypo_2006_2099['start_dates'].dt.year)['deox_duration'].sum()

# Plot the data
plt.plot(grouped_data)

# Fit a linear regression line
years = grouped_data.index.values
deox_duration = grouped_data.values
slope, intercept, r_value, p_value, std_err = linregress(years, deox_duration)

# Calculate the trendline
trendline = slope * years + intercept

# Plot the trendline
plt.plot(years, trendline,'--', label=f'Trendline (slope={slope:.2f}, R²={r_value**2:.2f})', color='red')

# Add legend
plt.legend()


# Add labels and title
plt.ylabel('Deoxygenation period duration [day/year]')

plt.savefig('Fluctuation_of_Annual_deoxygenation_duration_gfdl2es_RCP6_density_epi_10p_2.png', dpi=300)


# Display the equation and R² value
print(f"Equation of the trendline: y = {slope:.2f}x + {intercept:.2f}")
print(f"R² Value: {r_value**2:.2f}")
"""
Equation of the trendline: y = 0.37x + -626.59
R² Value: 0.37
3.7 day increase in each decay 
"""
#%%

import matplotlib.pyplot as plt
import pandas as pd

# Assuming `df_deox_period_surf_hypo_2006_2099` is a DataFrame containing your provided data
# You might need to convert the date columns to datetime if they're not already in that format
df_deox_period_surf_hypo_2006_2099['start_dates'] = pd.to_datetime(df_deox_period_surf_hypo_2006_2099['start_dates'])
df_deox_period_surf_hypo_2006_2099['end_dates'] = pd.to_datetime(df_deox_period_surf_hypo_2006_2099['end_dates'])

# Create a figure
plt.figure(figsize=(10, 6))

# Iterate through each row in the DataFrame
for index, row in df_deox_period_surf_hypo_2006_2099.iterrows():
    year = row['start_dates'].year
    start_day = row['start_dates'].day + row['start_dates'].month * 30  # Approximate day within the year
    end_day = row['end_dates'].day + row['end_dates'].month * 30  # Approximate day within the year

    # Plot a line for the period
    plt.plot([start_day, end_day], [year, year], label=f'Period {index+1}', linewidth=2)

# Set the x-axis ticks to represent days within a year
plt.xticks([i*30 for i in range(13)], ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec', 'Jan'])

# Set labels and title
plt.xlabel('Day of the Year')
plt.ylabel('Year')
plt.title('Periods (2006-2099)')

# Add a legend
#plt.legend()

# Show the plot
plt.tight_layout()
plt.show()

#%%Animiation of onset and loss of deoxygenation period 
#honestly not very informative maybe possible to add average (daily or per each deoxygenation period) tempaerture/DO in the hypolimnion  
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import pandas as pd

# Assuming `df_deox_period_surf_hypo_2006_2099` is a DataFrame containing your provided data
# You might need to convert the date columns to datetime if they're not already in that format
df_deox_period_surf_hypo_2006_2099['start_dates'] = pd.to_datetime(df_deox_period_surf_hypo_2006_2099['start_dates'])
df_deox_period_surf_hypo_2006_2099['end_dates'] = pd.to_datetime(df_deox_period_surf_hypo_2006_2099['end_dates'])

# Create a figure
fig, ax = plt.subplots(figsize=(10, 6))

def update(frame):
    #ax.clear()

    # Filter rows for the current year
    df_year = df_deox_period_surf_hypo_2006_2099[(df_deox_period_surf_hypo_2006_2099['start_dates'].dt.year <= frame) & (df_deox_period_surf_hypo_2006_2099['end_dates'].dt.year >= frame)]

    # Iterate through each row in the filtered DataFrame
    for index, row in df_year.iterrows():
        year = frame
        start_day = row['start_dates'].day + row['start_dates'].month * 30  # Approximate day within the year
        end_day = row['end_dates'].day + row['end_dates'].month * 30  # Approximate day within the year

        # Plot a line for the period
        ax.plot([start_day, end_day], [year, year], linewidth=2)#label=f'Period {index+1}', 

    # Set the x-axis ticks to represent days within a year
    ax.set_xticks([i*30 for i in range(13)])
    ax.set_xticklabels(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec', 'Jan'])

    # Set labels and title
    #ax.set_xlabel('Day of the Year')
    ax.set_ylabel('Year')
    ax.set_title(f'Deoxygenation periods (2006-{frame})')

    # Add a dynamic legend
    ax.legend()
# Create an animation
ani = animation.FuncAnimation(fig, update, frames=range(2006, 2100), repeat=False, interval=500)

# Save the animation to a file (uncomment the line below if you want to save)
#ani.save('your_animation.mp4')
ani.save('deoxygenation_start_end_animation.gif', writer='pillow', dpi=300)

# Show the animation
plt.tight_layout()
plt.show()


#%%PDF plotting for onset and loss , duartion of deoxygenation period :
    
import seaborn as sns
import matplotlib.pyplot as plt

# Assuming df_deox_period_surf_hypo_2006_2099['num_day_of_year_start'] is your data series
onset = df_deox_period_surf_hypo_2006_2099['num_day_of_year_start']
loss = df_deox_period_surf_hypo_2006_2099['num_day_of_year_end']
deox_duration = df_deox_period_surf_hypo_2006_2099.groupby(df_deox_period_surf_hypo_2006_2099['start_dates'].dt.year)['deox_duration'].sum()




#===========the Shapiro–Wilk test is used for testing normality.
from scipy.stats import shapiro

# Perform the Shapiro-Wilk test
stat, p_value = shapiro(deox_duration)

# Print the results
print(f"Shapiro-Wilk Test Statistic: {stat}, p-value: {p_value}")
if p_value > 0.05:
    print("The data appears to be normally distributed.")
else:
    print("The data does not appear to be normally distributed.")
"""
#onset:
Shapiro-Wilk Test Statistic: 0.5926550626754761, p-value: 6.4968621370860465e-15
The data does not appear to be normally distributed.    
    
#loss:
Shapiro-Wilk Test Statistic: 0.6238381862640381, p-value: 2.5446111485819857e-14
The data does not appear to be normally distributed.


#duration:    
Shapiro-Wilk Test Statistic: 0.9840049147605896, p-value: 0.30821287631988525
The data appears to be normally distributed.
"""


# Plot KDE# kernel density estimation (KDE) to estimate the PDF
#===============PDF-onset of deoxygenation# not normal
sns.histplot(onset, kde=True, stat='density')
plt.axvline(statistics.median(onset), color='r', linestyle='dashed', linewidth=1.5, label='Median')
plt.xlabel('Onset [day]')
plt.ylabel('PDF')
plt.legend()
plt.savefig('PDF_onset_deox_rcp60.png', dpi= 300)


#=================PDF-loss of deoxygenation# not normal
sns.histplot(loss, kde=True, stat='density')
plt.axvline(statistics.median(loss), color='r', linestyle='dashed', linewidth=1.5, label='Median')
plt.xlabel('Loss [day]')
plt.ylabel('PDF')
plt.legend()
plt.savefig('PDF_loss_deox_rcp60.png', dpi= 300)



#=================== PDF-duration of deoxygenation# normal
sns.histplot(deox_duration, kde=True, stat='density')
plt.axvline(deox_duration.mean(), color='r', linestyle='dashed', linewidth=1.5, label='Mean')
plt.xlabel('Deoxygenation duration [day]')
plt.ylabel('PDF')
plt.legend()
plt.savefig('PDF_duration_deox_rcp60.png', dpi= 300)


##====================Combine the three
# Ana in her paper had categorized to have tjis graph
# for one scenario and 5 model and also in Figure 7

# 1. prereference period based on the 1981-2010 from historical period 
# 2. mid_century: 2041-2070-> change to the prereference period
# 3. late_century: 2071-2100->change to the prereference period


# Create a figure with 3 subplots arranged in a single column

#use sns.kdeplot() instead of sns.histplot() if you want to remove histogram plots 
fig, axes = plt.subplots(3, 1, figsize=(10, 15))

# Plot 1: Onset
sns.kdeplot(onset, color='blue', label='KDE', ax=axes[0])
axes[0].axvline(statistics.median(onset), color='r', linestyle='dashed', linewidth=1.5, label='Median')
axes[0].set_xlabel('Onset [day]')
axes[0].set_ylabel('PDF')
axes[0].legend()

# Plot 2: Loss
sns.kdeplot(loss, color='green', label='KDE', ax=axes[1])
axes[1].axvline(statistics.median(loss), color='r', linestyle='dashed', linewidth=1.5, label='Median')
axes[1].set_xlabel('Loss [day]')
axes[1].set_ylabel('PDF')
axes[1].legend()

# Plot 3: Deoxygenation Duration
sns.kdeplot(deox_duration, color='purple', label='KDE', ax=axes[2])
axes[2].axvline(deox_duration.mean(), color='r', linestyle='dashed', linewidth=1.5, label='Mean')
axes[2].set_xlabel('Deoxygenation duration [day]')
axes[2].set_ylabel('PDF')
axes[2].legend()

# Adjust layout
plt.tight_layout()

plt.savefig('PDF_onset_loss_duartion_deoxygenation.png', dpi=300)


#=========================plotting three including histogram as well
"""
fig, axes = plt.subplots(3, 1, figsize=(10, 15))

# Plot 1: Onset
sns.histplot(onset, kde=True, stat='density', ax=axes[0])
axes[0].axvline(statistics.median(onset), color='r', linestyle='dashed', linewidth=1.5, label='Median')
axes[0].set_xlabel('Onset [day]')
axes[0].set_ylabel('PDF')
axes[0].legend()

# Plot 2: Loss
sns.histplot(loss, kde=True, stat='density', ax=axes[1])
axes[1].axvline(statistics.median(loss), color='r', linestyle='dashed', linewidth=1.5, label='Median')
axes[1].set_xlabel('Loss [day]')
axes[1].set_ylabel('PDF')
axes[1].legend()

# Plot 3: Deoxygenation Duration
sns.histplot(deox_duration, kde=True, stat='density', ax=axes[2])
axes[2].axvline(deox_duration.mean(), color='r', linestyle='dashed', linewidth=1.5, label='Mean')
axes[2].set_xlabel('Deoxygenation duration [day]')
axes[2].set_ylabel('PDF')
axes[2].legend()

# Adjust layout
plt.tight_layout()

plt.savefig('PDF_onset_loss_duartion_deoxygenation_histogram.png', dpi=300)

"""




#%%probeblibity of having the onset, loss and duration of observed years (2019-2022) according to the RCP2.6 estimated values 

import seaborn as sns
import matplotlib.pyplot as plt
from scipy.integrate import simps
import statistics

#====================onset 
onset = df_deox_period_surf_hypo_2006_2099['num_day_of_year_start']

# Plot KDE
sns.histplot(onset, kde=True, stat='density')
plt.axvline(statistics.median(onset), color='r', linestyle='dashed', linewidth=1.5, label='Median')
plt.xlabel('Onset [day]')
plt.ylabel('PDF')
plt.legend()

# Define the range of observation onset date number between 2019-2022:
# df_deox_period_2019_2022['num_day_of_year_start']->[135 , 193, 143, 133, 143]
start_range = 133
end_range = 193

# Calculate the PDF within the range
pdf_values = sns.histplot(onset, kde=True, stat='density').get_lines()[0].get_data()
pdf_range = pdf_values[1][(pdf_values[0] >= start_range) & (pdf_values[0] <= end_range)]
probability = simps(pdf_range, dx=(onset.max() - onset.min()) / len(onset))

# Print the probability
print(f"The probability of having data between {start_range} and {end_range} is {probability:.4f}")

#The probability of onset day number of year between 133 and 193 is 0.2722 (27.22%)
# (these two numbers are max and min of onset dates in years 2019-2022)

# Show the plot
plt.show()



#=============Loss 


loss = df_deox_period_surf_hypo_2006_2099['num_day_of_year_end']

# Plot KDE
sns.histplot(loss, kde=True, stat='density')
plt.axvline(statistics.median(loss), color='r', linestyle='dashed', linewidth=1.5, label='Median')
plt.xlabel('loss [day]')
plt.ylabel('PDF')
plt.legend()

# Define the range of observation loss date number between 2019-2022:
# df_deox_period_2019_2022['num_day_of_year_end']->[181 , 242, 247, 239, 243]
start_range = df_deox_period_2019_2022['num_day_of_year_end'].min()
end_range = df_deox_period_2019_2022['num_day_of_year_end'].max()

# Calculate the PDF within the range
pdf_values = sns.histplot(loss, kde=True, stat='density').get_lines()[0].get_data()
pdf_range = pdf_values[1][(pdf_values[0] >= start_range) & (pdf_values[0] <= end_range)]
probability = simps(pdf_range, dx=(loss.max() - loss.min()) / len(onset))

# Print the probability
print(f"The probability of having data between {start_range} and {end_range} is {probability:.4f}")

#The probability of loss day number of year between 181 and 247 is 0.6100(61%)
#(these two numbers are max and min of loss dates in years 2019-2022)

# Show the plot
plt.show()


#==============deoxygenation duartion 



deox_duration = df_deox_period_surf_hypo_2006_2099.groupby(df_deox_period_surf_hypo_2006_2099['start_dates'].dt.year)['deox_duration'].sum()

# Plot KDE
sns.histplot(deox_duration, kde=True, stat='density')
plt.axvline(statistics.median(deox_duration), color='r', linestyle='dashed', linewidth=1.5, label='Median')
plt.xlabel('Duration [day]')
plt.ylabel('PDF')
plt.legend()

# Define the range of observation deox_duration date number between 2019-2022:
# df_deox_period_2019_2022['deox_duration']->[47,50 , 105, 107, 101]
start_range = 47+50
end_range = df_deox_period_2019_2022['deox_duration'].max()

# Calculate the PDF within the range
pdf_values = sns.histplot(deox_duration, kde=True, stat='density').get_lines()[0].get_data()
pdf_range = pdf_values[1][(pdf_values[0] >= start_range) & (pdf_values[0] <= end_range)]
probability = simps(pdf_range, dx=(deox_duration.max() - deox_duration.min()) / len(onset))

# Print the probability
print(f"The probability of having data between {start_range} and {end_range} is {probability:.4f}")

#The probability of deox_duration day number of year between 181 and 247 is 0.0976(9.76%)
#(these two numbers are max and min of deox_duration dates in years 2019-2022)

# Show the plot
plt.show()


#%%DO model for one year implicit# density_difference_1m_top_hypo_indexed-OLD version_not working correctly 
"""
#find_stratification_periods_density_diff    


bath_hypo_gotm_grid= np.array (interpolated_bath['V_r'][1:15][::-1]),  np.array (interpolated_bath['A_s'][1:15][::-1]),  np.array (interpolated_bath['A_l'][1:15][::-1]), 0.5


#deltat=1
#temp=temp_gotm_hypo_str_overturn 
#kz_array= kz_gotm_hypo_str_overturn
#params=[0.01 , 0.6 , 1/3]

#temp=temp_gotm_hypo_str_overturn#138x15
#kz_array=kz_gotm_hypo_str_overturn# 138x15
#deltat=1




def do_for_one_str_model_imp(params, temp ,kz_array  ,  bath=bath_hypo_gotm_grid  ,deltat=1 , sat_onset= 1):
    # Extracting parameters from params
    jv, ja, scale_subdaily = params
    Vr , As , Al ,deltaz = bath 
    n = len(As)
    #temp_theta= temp.copy()
    # Calculate the number of subdaily time steps
    num_time_steps_subdaily = int(1 / scale_subdaily)
    
    #temp_theta= (np.repeat(temp_theta, num_time_steps_subdaily, axis=0)).T
    # Initialize initial_cond using C_satur
    initial_cond= C_satur(temp[0, :], sat_onset)
    #temp=temp[1:]
    #kz_array=kz_array[1: , :]
    # Calculate the number of repeats    
    num_repeats = (temp.shape[0]-1)#remove the day of before onset of startification 
    # Create the deltat array based on num_repeats
    deltat_array =np.repeat( deltat, num_repeats)# works for daily 
    
    
    
    # Reshape and repeat deltat for each time step
    deltat_subdaily=scale_subdaily*np.tile(deltat_array, (num_time_steps_subdaily, 1)).transpose().flatten()
    
    m = len(deltat_subdaily)  # without mixing 
    # Repeat the temperature array for subdaily time steps
    #temp_subdaily = np.repeat(temp[1: , :], num_time_steps_subdaily, axis=0)
    temp_subdaily: np.ndarray = np.repeat(temp[1: , :], num_time_steps_subdaily, axis=0)# without mixing 
    #temp_subdaily_overturn= np.vstack((temp[0, :],temp_subdaily ))
    
    
    kz_subdaily:np.ndarray = np.repeat(kz_array[1: , :], num_time_steps_subdaily, axis=0)
    #kz_subdaily_overturn=np.vstack((kz_array[0, :],kz_subdaily ))
    
    
    kz = (24 * 3600 * kz_subdaily).T  #kz_subdaily_overturn
    ###NO Kz
    #kz = np.zeros(kz.shape)
    temp=temp_subdaily.T#temp_subdaily_overturn.T
    
    
    # Initialize Factor_dig as an empty matrix
    Factor_dig = np.zeros((n, n))

    
    def Theta_j(temp):
        theta = 1.087
        return theta ** (temp - 20)

    
    # Initialize the left-hand side (lhs) for the first time step
    lhs = initial_cond #- deltat[0] * ((Al / Vr) * ja * Theta_j(temp[:, 0]) + jv * Theta_j(temp[:, 0]))
    # Initialize the concentration matrix C
    C = np.zeros((n, m))# layer x timestep 
    C[:, 0] = lhs
    # Loop through each time step
    for j in range(1, m):#time
    # Loop through each depth
    
        for i in range(n):#depth
        # Update the Factor_dig matrix based on the depth index
            if i == 0:
            # Handle first depth index    
                Factor_dig[i, i] = 1 + deltat_subdaily[j] * As[i + 1] * kz[i + 1, j] / (Vr[i] * deltaz)
                Factor_dig[i, i + 1] = -deltat_subdaily[j] * As[i + 1] * kz[i + 1, j] / (Vr[i] * deltaz)
            elif i == n - 1:
            # Handle last depth index    
                Factor_dig[i, i] = 1 + deltat_subdaily[j] * As[i] * kz[i, j] / (Vr[i] * deltaz)
                Factor_dig[i, i - 1] = -deltat_subdaily[j] * As[i] * kz[i, j] / (Vr[i] * deltaz)
            
            else:
            # Handle middle depth indices
                Factor_dig[i, i] = 1 + deltat_subdaily[j] * As[i] * kz[i, j] / (Vr[i] * deltaz) + deltat_subdaily[j] * As[i + 1] * kz[i + 1, j] / (deltaz * Vr[i])
                Factor_dig[i, i - 1] = -deltat_subdaily[j] * As[i] * kz[i, j] / (Vr[i] * deltaz)
                Factor_dig[i, i + 1] = -deltat_subdaily[j] * As[i + 1] * kz[i + 1, j] / (deltaz * Vr[i])

    
        # Update the right-hand side (b) for the current time step
        b = C[:, j - 1].copy()
        b[0] = b[0] + (0.1) * deltat_subdaily[j] * As[0] * kz[0, j] / (deltaz * Vr[0])
        # Solve the linear system of equations using np.linalg.solve
        solution = np.linalg.solve(Factor_dig, b - deltat_subdaily[j-1] * ((Al / Vr) * ja * Theta_j((temp[:,j] +temp[: , j-1])/2) + jv * Theta_j((temp[:,j] +temp[: , j-1])/2)))
        #without averaging two days tem for theta temperature correction
        # Theta_j(temp[:, j])
        # Update the concentration matrix C for the current time step
        C[:, j] = solution

    
    
    #if C> satuartion level get the satuartion level as DO concentration:
    number_of_sub_day_str_bigger_saturated= np.sum(C > C_satur(temp, 1))//(num_time_steps_subdaily*n)
    # Calculate the number of days in the simulation
    number_of_day_str_bigger_saturated=0
    number_of_day_str_bigger_saturated+=number_of_sub_day_str_bigger_saturated
   
    C= np.where (C> C_satur(temp) , C_satur(temp) , C)    
    num_days = C.shape[1] // num_time_steps_subdaily
    # Reshape the concentration matrix to a 3D array
    C_3d =C.reshape(n, num_days, num_time_steps_subdaily)
    C_3d = np.where(C_3d < 0, 0, C_3d)
    # Now you can extract the last value from each subdaily group
    #C_daily_str = C_3d[:, :, -1]
    # geting average on the time steps scale 
    C_daily_str = np.mean(C_3d, axis=2)
    # Apply a threshold to ensure non-negative concentrations
    C_f = np.where(C_daily_str < 0, 0, C_daily_str).T
    
    # adding the day before startification onset
    C_daily_str_turnover= np.concatenate(( initial_cond.reshape(1, -1),C_f ))
    
    # Calculate weighted average DO concentrations for both cases
    DO_ave_str_model = np.dot(C_f, Vr) / sum(Vr)# weight average 
    DO_ave_str_overturn_model=np.dot(C_f , Vr)/sum(Vr)
    #DO_ave_overturn_model= np.dot(C_daily_str_turnover[0, :] , Vr)/sum(Vr)
    
    return  C_3d, C_f, DO_ave_str_model , C_daily_str_turnover , DO_ave_str_overturn_model , number_of_day_str_bigger_saturated#, DO_ave_overturn_model
"""


#%% DO model # density_difference_1m_top_hypo_indexed_OLD version_not working correctly 
"""
#params=[0.01 , 1.156 , 1]
#find_dod_periods_densdiff
#density_difference_1m_top_hypo_indexed, temp_gotm_hypo_TB, kz_gotm_hypo_TB
density_difference_1m_top_hypo_indexed

#density_difference_surf_top_hypo_non_indexed
def DO_model_future_yt(params , density_difference_1m_top_hypo_indexed=density_difference_1m_top_hypo_indexed , bath= bath_hypo_gotm_grid,  temp_gotm_hypo_obsgrid=temp_gotm_hypo_TB , kz_gotm_hypo_obsgrid=kz_gotm_hypo_TB ,thereshold=-0.05, concequetive_day=7 ):
    
    jv, ja, scale_subdaily = params
    Vr , As , Al ,deltaz = bath     

    density_difference_1m_top_hypo_non_indexed=density_difference_1m_top_hypo_indexed.reset_index()
    # Create an empty array to store the final DO values
    do_str_daily = np.full_like(temp_gotm_hypo_obsgrid, np.nan)
    do_str_ave= np.full((temp_gotm_hypo_obsgrid.shape[0]), np.nan)
    
    temp_hypo_str_overturn_daily = np.full_like(temp_gotm_hypo_obsgrid, np.nan)
    kz_hypo_str_overturn_daily = np.full_like(temp_gotm_hypo_obsgrid, np.nan)
    
    do_overturn_daily=do_str_daily.copy()
    do_overturn_ave= do_str_ave.copy()
    
    subset_indices = {}
    annual_str_duartion=[]
    polymectic_years=[]
    
    num_day_bigger_saturation=0
    for year in range(density_difference_1m_top_hypo_indexed.index.year.min(), density_difference_1m_top_hypo_indexed.index.year.max()+1):
        C_ave_previous_end=np.array([])
        year_data = density_difference_1m_top_hypo_indexed.loc[density_difference_1m_top_hypo_indexed.index.year ==year]#.values# year
        consecutive_true = (year_data < thereshold).rolling(window=concequetive_day, min_periods=concequetive_day, center=False).sum() == concequetive_day
        consecutive_true=consecutive_true.shift(-concequetive_day)# the last 5 values in the new series will be NaN
        
        diffs = consecutive_true.diff()
        
        starts = diffs.where((diffs == 1))# actually including the turnover date
        starts = starts.dropna()
        
        ends = diffs.where((diffs == -1))#.shift(6)# only the onset should have the 5 days in row limitation but not the offset 
        ends = ends.dropna()
        
        if len(starts)==0:
            starts= diffs[diffs.index== diffs.index.min() ]
        
        if len(ends)==0:
            ends= diffs[diffs.index== diffs.index.max() ]
            
            
        
        length= (ends.index- (starts.index + pd.Timedelta(days=1))).days

        starts= starts[length> concequetive_day] 
        ends= ends[length> concequetive_day]


        num_starts= np.where(np.isin(density_difference_1m_top_hypo_non_indexed['index'], starts.index))[0]
        num_ends= np.where(np.isin(density_difference_1m_top_hypo_non_indexed['index'], ends.index))[0]
        
        total_days = 0
        days_per_annual_str_period = (ends.index-(starts.index+ pd.Timedelta(days=1))).days
        days_per_annual_str_period= list (days_per_annual_str_period)
        # Check if the year has two parts (two separate stratification periods)
        if len(days_per_annual_str_period) > 1:
            total_days = sum(days_per_annual_str_period)
            polymectic_years= np.append(polymectic_years , year)
                       
            
            
        else:
            total_days = days_per_annual_str_period[0]
            
            
        number_of_polymectic_years= len(polymectic_years)
        annual_str_duartion=np.append ( annual_str_duartion , total_days)    
        
        #print (ends.index-(starts.index- pd.Timedelta(days=1)) , total_days)
        
        
               
        for i, (start_index, end_index) in enumerate(zip(starts.index, ends.index)):
            #print(i , start_index, end_index)
           
            
            if i==0:  
                
                subset_name = f"{year}_{i+1}"
                
                num_start_index= np.where(density_difference_1m_top_hypo_non_indexed['index']==start_index)[0][0]
                num_end_index= np.where(density_difference_1m_top_hypo_non_indexed['index']==end_index)[0][0]#-1
            
            
            
                #temp_gotm_overturn= temp_gotm_hypo_obsgrid[np.array(num_start_index)]
                temp_gotm_hypo_str_overturn=temp_gotm_hypo_obsgrid[np.array(num_start_index) :np.array(num_end_index)+1, :]# including the day of mixing (a day before satrification)
                kz_gotm_hypo_str_overturn= kz_gotm_hypo_obsgrid[np.array(num_start_index)+1:np.array(num_end_index)+1+1 , :]# including the day of mixing (a day before satrification)
           
                
                
                #setting saturation percentage on onset:
                
                sat_new_onset=1
    
                C_3d_subdaily ,C_str_daily, DO_ave_str_model , C_daily_str_turnover , DO_ave_str_overturn_model , number_of_day_str_bigger_str = do_for_one_str_model_imp(params, temp=temp_gotm_hypo_str_overturn ,kz_array=kz_gotm_hypo_str_overturn,  bath=bath_hypo_gotm_grid  ,deltat=1 , sat_onset= sat_new_onset)
            
                C_ave_previous_end= DO_ave_str_model[-1].copy()
                
                num_day_bigger_saturation += number_of_day_str_bigger_str


                # Store the calculated DO values in the corresponding positions
                do_str_daily[num_start_index:num_end_index, :] = C_str_daily
                do_str_ave[num_start_index+1:num_end_index+1]= DO_ave_str_model
                
                #do_str_daily[num_start_index:num_end_index+1, :] = C_daily_str_turnover
                #do_str_ave[num_start_index:num_end_index]= DO_ave_str_overturn_model
                
                
                #do_overturn_daily[num_start_index, :]= C_daily_str_turnover[0, :]
                #do_overturn_ave[num_start_index]=DO_ave_str_overturn_model[0]
                
                temp_hypo_str_overturn_daily[num_start_index:num_end_index+1, :]=temp_gotm_hypo_str_overturn
                kz_hypo_str_overturn_daily[num_start_index:num_end_index+1, :]=kz_gotm_hypo_str_overturn



            elif i>0: #for i in range(1 , len(starts)):# in enumerate(range(i))
                
                subset_name = f"{year}_{i+1}"
                
                num_start_index= np.where(density_difference_1m_top_hypo_non_indexed['index']==start_index)[0][0]
                num_end_index= np.where(density_difference_1m_top_hypo_non_indexed['index']==end_index)[0][0]#-1
            
            
            
                #temp_gotm_overturn= temp_gotm_hypo_obsgrid[np.array(num_start_index)]
                temp_gotm_hypo_str_overturn=temp_gotm_hypo_obsgrid[np.array(num_start_index) :np.array(num_end_index)+1, :]# including the day of mixing (a day before satrification)
                kz_gotm_hypo_str_overturn= kz_gotm_hypo_obsgrid[np.array(num_start_index)+1:np.array(num_end_index)+1+1 , :]# including the day of mixing (a day before satrification)

                temp_ave_previous_end =np.dot (temp_gotm_hypo_obsgrid[num_ends[i-1]],  Vr) / sum(Vr)
                sat_previous_end=C_ave_previous_end/ C_satur(temp_ave_previous_end ,1 )
                duration_repl = ((starts.index[i] + pd.Timedelta(days=1))-ends.index[i-1]).days
                increase_sat_repl=duration_repl*(2.7861/100)##3.4902
                sat_new_onset =sat_previous_end + increase_sat_repl
           
                C_3d_subdaily ,C_str_daily, DO_ave_str_model , C_daily_str_turnover , DO_ave_str_overturn_model , number_of_day_str_bigger_str = do_for_one_str_model_imp(params, temp=temp_gotm_hypo_str_overturn ,kz_array=kz_gotm_hypo_str_overturn,  bath=bath_hypo_gotm_grid  ,deltat=1 , sat_onset= sat_new_onset)
            
                C_ave_previous_end= DO_ave_str_model[-1].copy()
               
           
                num_day_bigger_saturation += number_of_day_str_bigger_str
    
    
                # Store the calculated DO values in the corresponding positions
                do_str_daily[num_start_index+1:num_end_index+1, :] = C_str_daily
                do_str_ave[num_start_index+1:num_end_index+1]= DO_ave_str_model
                
                #do_str_daily[num_start_index:num_end_index+1, :] = C_daily_str_turnover
                #do_str_ave[num_start_index:num_end_index]= DO_ave_str_overturn_model
                
                
                #do_overturn_daily[num_start_index, :]= C_daily_str_turnover[0, :]
                #do_overturn_ave[num_start_index]=DO_ave_str_overturn_model[0]
                
                temp_hypo_str_overturn_daily[num_start_index:num_end_index+1, :]=temp_gotm_hypo_str_overturn
                kz_hypo_str_overturn_daily[num_start_index:num_end_index+1, :]=kz_gotm_hypo_str_overturn



    return (do_str_daily , do_str_ave  , temp_hypo_str_overturn_daily , kz_hypo_str_overturn_daily , num_day_bigger_saturation)
"""
#%%Testing the function_OLD version_#It is not workinggggg right
"""
x1, x2, x3, x4 , x5 =DO_model_future_yt([0.01, 1.156, 1] , density_difference_1m_top_hypo_indexed=density_difference_1m_top_hypo_indexed  , bath= bath_hypo_gotm_grid,  temp_gotm_hypo_obsgrid=temp_gotm_hypo_TB , kz_gotm_hypo_obsgrid=kz_gotm_hypo_TB,thereshold=-0.2, concequetive_day=7  )
    
x1_cleaned = x1[~np.isnan(x1).any(axis=1)]
max_value = np.max(x1_cleaned)#

x1y= x1[: , 0:8]
x1y_cleaned = x1y[~np.isnan(x1y).any(axis=1)]
max_value_x1y = np.max(x1y_cleaned)#



[0.01, 1.136, 1]with 0.1 density-> max:20.63815->100*x7/np.size(x1_cleaned)->%0.99

[0.01, 1.136, 1]with 0.05 density -> max:23.90->1% of all size 

[0.01 , 1.136 , 1/24]with 0.05 density -> max:23.84563->1% of all size 

x2_indexed = pd.DataFrame({'ave_hypo_do': x2}, index=formatted_time_series)
mask = ~np.isnan(x2_indexed['ave_hypo_do'])

# Apply the boolean mask to filter out rows with NaN values
do_ave_simulated= x2_indexed[mask]


    
kz_2060_1=find_dod_periods_densdiff(density_difference_surf_top_hypo_indexed, temp_gotm_hypo_TB, kz_gotm_hypo_TB)[0]['2060_1']['kz_gotm_hypo_str_overturn']
    
"""
#%%OLD version:plotting the duartion of deoxygenation a long the future years and the observed years values 
"""

new_directory = r'C:\Users\mahta\OneDrive\Documents\all_python_coding\Future_simulation_results'
os.chdir(new_directory)

import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt


# Create a new figure
plt.figure(figsize=(10, 6))
# Plot the data
plt.plot(formatted_time_series.dt.year.unique(), annual_dod_duartion)

# Calculate linear regression
x = formatted_time_series.dt.year.unique()
y = annual_dod_duartion
slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
reg_line = slope * x + intercept

# Plot the linear regression line
plt.plot(x, reg_line, '--', label=f'Regression Line: y = {slope:.2f}x + {intercept:.2f}')

# Calculate R-squared
r_squared = r_value**2

# Add R-squared value to the legend
plt.legend(title=f'R-squared: {r_squared:.2f}')
# results from previous coding:
deoygenation_duration_calival=[(2019, 65) , (2020, 99) , (2021 , 88) , (2022, 87)]

# Plot the scatter points for extra data
extra_years, extra_counts = zip(*deoygenation_duration_calival)
plt.scatter(extra_years, extra_counts, color='green', label='Observations', s=50, zorder=5)



# Add labels and title
plt.ylabel('Duration [day]')
plt.xlabel('Years')
plt.title('Annual deoxygenation duration_gfdl2es_RCP6_dd_5e-2_6daysmore')
plt.legend()
# Increase the quality of the plot to dpi=300 and save it
plt.savefig('Fluctuation_of_Annual_deoxygenation_duration_gfdl2es_RCP6_density_epi_10p_2.png', dpi=300)
"""

















