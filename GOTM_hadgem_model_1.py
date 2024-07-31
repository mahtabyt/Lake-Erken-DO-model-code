# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 10:54:56 2023

@author: mahta
"""

#import    
import os    
import pandas as pd    
# specify the current working directory
os.chdir('C:/Users/mahta/OneDrive - University of Stirling/Erken_GOTM_simulations/4models/isimip2b_gotm_erken/hadgem2-es')

#%%Reading Netcdf file


import netCDF4 as nc

from scipy.io import netcdf  

#file direction
hadgem_his= 'C:/Users/mahta/OneDrive - University of Stirling/Erken_GOTM_simulations/4models/isimip2b_gotm_erken/hadgem2-es/isimip_gotm_erken_had_historical.nc'

#hadgem_pic= 'C:/Users/mahta/OneDrive - University of Stirling/Erken_GOTM_simulations/4models/isimip2b_gotm_erken/hadgem2-es/isimip_gotm_erken_had_picontrol.nc'

hadgem_rcp26= 'C:/Users/mahta/OneDrive - University of Stirling/Erken_GOTM_simulations/4models/isimip2b_gotm_erken/hadgem2-es/isimip_gotm_erken_had_rcp26.nc'

hadgem_rcp60= 'C:/Users/mahta/OneDrive - University of Stirling/Erken_GOTM_simulations/4models/isimip2b_gotm_erken/hadgem2-es/isimip_gotm_erken_had_rcp60.nc'

#hadgem_rcp85= 'C:/Users/mahta/OneDrive - University of Stirling/Erken_GOTM_simulations/4models/isimip2b_gotm_erken/hadgem2-es/isimip2b_gotm_erken_had_rcp85.nc'

hadgem_rcp85= 'C:/Users/mahta/OneDrive - University of Stirling/Erken_GOTM_simulations/4models/isimip2b_gotm_erken/hadgem2-es/isimip2b_gotm_erken_had_rcp85_correct.nc'

#transfering into datasets 

dataset_hadgem_his  = netcdf.netcdf_file(hadgem_his,'r')
#dataset_hadgem_pic = netcdf.netcdf_file(hadgem_pic,'r')
dataset_hadgem_rcp26  = netcdf.netcdf_file(hadgem_rcp26,'r')
dataset_hadgem_rcp60  = netcdf.netcdf_file(hadgem_rcp60,'r')
dataset_hadgem_rcp85  = netcdf.netcdf_file(hadgem_rcp85,'r')

#%%depth variable and geogharphical location 


import numpy as np
from datetime import datetime, timedelta
import netCDF4
netCDF4.num2date



lat=dataset_hadgem_his.variables['lat'][:]
print (lat)#[59.6]

lon=dataset_hadgem_his.variables['lon'][:]
print (lon)#[18.6]


z_bnd_gotm= dataset_hadgem_his.variables['zi'][:]
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


z_m_gotm= dataset_hadgem_his.variables['z'][:]
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
  
#%%1   _hadgem_his    
  
temp_hadgem_his=dataset_hadgem_his.variables['temp'][:]
temp_hadgem_his_full_prof_gotmgrid=temp_hadgem_his[: , : , 0 , 0]# the first and scond dimentions are time and depth , the third and forth are lon and lat 

kz_hadgem_his= dataset_hadgem_his.variables['avh'][:]
kz_hadgem_his_full_prof_gotmgrid=kz_hadgem_his[: , : , 0 , 0]


time_variable_hadgem_his = dataset_hadgem_his.variables['time']
time_units_str_hadgem_his = time_variable_hadgem_his.units.decode()  # Convert bytes to string
time_units_hadgem_his, _, reference_time_str_hadgem_his = time_units_str_hadgem_his.partition(' since ')

# Convert reference_time_str to datetime object
reference_time_hadgem_his = datetime.strptime(reference_time_str_hadgem_his, '%Y-%m-%d %H:%M:%S')

# Convert numerical values to datetime objects
time_in_seconds_hadgem_his = time_variable_hadgem_his[:]
time_in_datetime_hadgem_his = [reference_time_hadgem_his + timedelta(seconds=int(t)) for t in time_in_seconds_hadgem_his]

# Convert time_in_datetime to a NumPy array
time_in_datetime_array_hadgem_his = np.array(time_in_datetime_hadgem_his)

# Format datetime objects as strings
formatted_time_list_hadgem_his = [dt.strftime("%Y-%m-%d") for dt in time_in_datetime_array_hadgem_his]
# Convert the formatted_time strings back to datetime objects
formatted_time_datetime_hadgem_his = [datetime.strptime(time_str, "%Y-%m-%d") for time_str in formatted_time_list_hadgem_his]

#%%2   _hadgem_pic
"""
temp_hadgem_pic=dataset_hadgem_pic.variables['temp'][:]
temp_hadgem_pic_full_prof_gotmgrid=temp_hadgem_pic[: , : , 0 , 0]# the first and scond dimentions are time and depth , the third and forth are lon and lat 

kz_hadgem_pic= dataset_hadgem_pic.variables['avh'][:]
kz_hadgem_pic_full_prof_gotmgrid=kz_hadgem_pic[: , : , 0 , 0]


time_variable_hadgem_pic = dataset_hadgem_pic.variables['time']
time_units_str_hadgem_pic = time_variable_hadgem_pic.units.decode()  # Convert bytes to string
time_units_hadgem_pic, _, reference_time_str_hadgem_pic = time_units_str_hadgem_pic.partition(' since ')

# Convert reference_time_str to datetime object
reference_time_hadgem_pic = datetime.strptime(reference_time_str_hadgem_pic, '%Y-%m-%d %H:%M:%S')

# Convert numerical values to datetime objects
time_in_seconds_hadgem_pic = time_variable_hadgem_pic[:]
time_in_datetime_hadgem_pic = [reference_time_hadgem_pic + timedelta(seconds=int(t)) for t in time_in_seconds_hadgem_pic]

# Convert time_in_datetime to a NumPy array
time_in_datetime_array_hadgem_pic = np.array(time_in_datetime_hadgem_pic)

# Format datetime objects as strings
formatted_time_list_hadgem_pic = [dt.strftime("%Y-%m-%d") for dt in time_in_datetime_array_hadgem_pic]
# Convert the formatted_time strings back to datetime objects
formatted_time_datetime_hadgem_pic = [datetime.strptime(time_str, "%Y-%m-%d") for time_str in formatted_time_list_hadgem_pic]
"""

#%%3.      hadgem_rcp26

temp_hadgem_rcp26=dataset_hadgem_rcp26.variables['temp'][:]
temp_hadgem_rcp26_full_prof_gotmgrid=temp_hadgem_rcp26[: , : , 0 , 0]# the first and scond dimentions are time and depth , the third and forth are lon and lat 

kz_hadgem_rcp26= dataset_hadgem_rcp26.variables['avh'][:]
kz_hadgem_rcp26_full_prof_gotmgrid=kz_hadgem_rcp26[: , : , 0 , 0]


time_variable_hadgem_rcp26 = dataset_hadgem_rcp26.variables['time']
time_units_str_hadgem_rcp26 = time_variable_hadgem_rcp26.units.decode()  # Convert bytes to string
time_units_hadgem_rcp26, _, reference_time_str_hadgem_rcp26 = time_units_str_hadgem_rcp26.partition(' since ')

# Convert reference_time_str to datetime object
reference_time_hadgem_rcp26 = datetime.strptime(reference_time_str_hadgem_rcp26, '%Y-%m-%d %H:%M:%S')

# Convert numerical values to datetime objects
time_in_seconds_hadgem_rcp26 = time_variable_hadgem_rcp26[:]
time_in_datetime_hadgem_rcp26 = [reference_time_hadgem_rcp26 + timedelta(seconds=int(t)) for t in time_in_seconds_hadgem_rcp26]

# Convert time_in_datetime to a NumPy array
time_in_datetime_array_hadgem_rcp26 = np.array(time_in_datetime_hadgem_rcp26)

# Format datetime objects as strings
formatted_time_list_hadgem_rcp26 = [dt.strftime("%Y-%m-%d") for dt in time_in_datetime_array_hadgem_rcp26]
# Convert the formatted_time strings back to datetime objects
formatted_time_datetime_hadgem_rcp26 = [datetime.strptime(time_str, "%Y-%m-%d") for time_str in formatted_time_list_hadgem_rcp26]



#%%4.      hadgem_rcp60

temp_hadgem_rcp60=dataset_hadgem_rcp60.variables['temp'][:]
temp_hadgem_rcp60_full_prof_gotmgrid=temp_hadgem_rcp60[: , : , 0 , 0]# the first and scond dimentions are time and depth , the third and forth are lon and lat 

kz_hadgem_rcp60= dataset_hadgem_rcp60.variables['avh'][:]
kz_hadgem_rcp60_full_prof_gotmgrid=kz_hadgem_rcp60[: , : , 0 , 0]


time_variable_hadgem_rcp60 = dataset_hadgem_rcp60.variables['time']
time_units_str_hadgem_rcp60 = time_variable_hadgem_rcp60.units.decode()  # Convert bytes to string
time_units_hadgem_rcp60, _, reference_time_str_hadgem_rcp60 = time_units_str_hadgem_rcp60.partition(' since ')

# Convert reference_time_str to datetime object
reference_time_hadgem_rcp60 = datetime.strptime(reference_time_str_hadgem_rcp60, '%Y-%m-%d %H:%M:%S')

# Convert numerical values to datetime objects
time_in_seconds_hadgem_rcp60 = time_variable_hadgem_rcp60[:]
time_in_datetime_hadgem_rcp60 = [reference_time_hadgem_rcp60 + timedelta(seconds=int(t)) for t in time_in_seconds_hadgem_rcp60]

# Convert time_in_datetime to a NumPy array
time_in_datetime_array_hadgem_rcp60 = np.array(time_in_datetime_hadgem_rcp60)

# Format datetime objects as strings
formatted_time_list_hadgem_rcp60 = [dt.strftime("%Y-%m-%d") for dt in time_in_datetime_array_hadgem_rcp60]
# Convert the formatted_time strings back to datetime objects
formatted_time_datetime_hadgem_rcp60 = [datetime.strptime(time_str, "%Y-%m-%d") for time_str in formatted_time_list_hadgem_rcp60]


#%%5.      hadgem_rcp85

temp_hadgem_rcp85=dataset_hadgem_rcp85.variables['temp'][:]
temp_hadgem_rcp85_full_prof_gotmgrid=temp_hadgem_rcp85[: , : , 0 , 0]# the first and scond dimentions are time and depth , the third and forth are lon and lat 

kz_hadgem_rcp85= dataset_hadgem_rcp85.variables['avh'][:]
kz_hadgem_rcp85_full_prof_gotmgrid=kz_hadgem_rcp85[: , : , 0 , 0]


time_variable_hadgem_rcp85 = dataset_hadgem_rcp85.variables['time']
time_units_str_hadgem_rcp85 = time_variable_hadgem_rcp85.units.decode()  # Convert bytes to string
time_units_hadgem_rcp85, _, reference_time_str_hadgem_rcp85 = time_units_str_hadgem_rcp85.partition(' since ')

# Convert reference_time_str to datetime object
reference_time_hadgem_rcp85 = datetime.strptime(reference_time_str_hadgem_rcp85, '%Y-%m-%d %H:%M:%S')

# Convert numerical values to datetime objects
time_in_seconds_hadgem_rcp85 = time_variable_hadgem_rcp85[:]
time_in_datetime_hadgem_rcp85 = [reference_time_hadgem_rcp85 + timedelta(seconds=int(t)) for t in time_in_seconds_hadgem_rcp85]

# Convert time_in_datetime to a NumPy array
time_in_datetime_array_hadgem_rcp85 = np.array(time_in_datetime_hadgem_rcp85)

# Format datetime objects as strings
formatted_time_list_hadgem_rcp85 = [dt.strftime("%Y-%m-%d") for dt in time_in_datetime_array_hadgem_rcp85]
# Convert the formatted_time strings back to datetime objects
formatted_time_datetime_hadgem_rcp85 = [datetime.strptime(time_str, "%Y-%m-%d") for time_str in formatted_time_list_hadgem_rcp85]


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
kz_hadgem_his_full_prof_gotmgrid
temp_hadgem_his_full_prof_gotmgrid

tem_hadgem_his_surf=temp_hadgem_his_full_prof_gotmgrid[: , 41]
tem_hadgem_his_top_hypo= temp_hadgem_his_full_prof_gotmgrid[: , 14]
tem_hadgem_his_1m= temp_hadgem_his_full_prof_gotmgrid[: , 39]
temp_hadgem_his_hypo= temp_hadgem_his_full_prof_gotmgrid[: , 0:14]


density_hadgem_his_surf=Lab_Density(tem_hadgem_his_surf)
density_hadgem_his_1m=Lab_Density(tem_hadgem_his_1m)
density_hadgem_his_top_hypo=Lab_Density(tem_hadgem_his_top_hypo)


density_difference_surf_top_hypo_hadgem_his=density_hadgem_his_surf -density_hadgem_his_top_hypo
density_difference_1m_top_hypo_hadgem_his=density_hadgem_his_1m-density_hadgem_his_top_hypo
# Convert formatted_time_datetime to a pandas Series or NumPy array
formatted_time_series_hadgem_his = pd.Series(formatted_time_datetime_hadgem_his)  # or np.array(formatted_time_datetime)

# Create the DataFrame with temp_diff_gotm_obsgrid_top_135 as the data and formatted_time_series as the index
formatted_time_series_hadgem_his = pd.Series(formatted_time_datetime_hadgem_his)



density_difference_surf_top_hypo_hadgem_his_indexed = pd.Series(density_difference_surf_top_hypo_hadgem_his, index=pd.to_datetime(formatted_time_series_hadgem_his))
density_difference_surf_top_hypo_hadgem_his_indexed.index.name = 'Datetime'


density_difference_1m_top_hypo_hadgem_his_indexed = pd.Series(density_difference_1m_top_hypo_hadgem_his, index=pd.to_datetime(formatted_time_series_hadgem_his))
density_difference_1m_top_hypo_hadgem_his_indexed.index.name = 'Datetime'

#%%pi# starting date: 1661 end 2099 the minimum date of pi control is lower than datetime.min() 
#print(pd.Timestamp.min)
#1677-09-21 00:12:43.145224193
"""
kz_hadgem_pic_full_prof_gotmgrid
temp_hadgem_pic_full_prof_gotmgrid

tem_hadgem_pic_surf=temp_hadgem_pic_full_prof_gotmgrid[: , 41]
tem_hadgem_pic_top_hypo= temp_hadgem_pic_full_prof_gotmgrid[: , 14]
tem_hadgem_pic_1m= temp_hadgem_pic_full_prof_gotmgrid[: , 39]
temp_hadgem_pic_hypo= temp_hadgem_pic_full_prof_gotmgrid[: , 0:14]


density_hadgem_pic_surf=Lab_Density(tem_hadgem_pic_surf)
density_hadgem_pic_1m=Lab_Density(tem_hadgem_pic_1m)
density_hadgem_pic_top_hypo=Lab_Density(tem_hadgem_pic_top_hypo)


density_difference_surf_top_hypo_hadgem_pic=density_hadgem_pic_surf -density_hadgem_pic_top_hypo
density_difference_1m_top_hypo_hadgem_pic=density_hadgem_pic_1m-density_hadgem_pic_top_hypo
# Convert formatted_time_datetime to a pandas Series or NumPy array
formatted_time_series_hadgem_pic = pd.Series(formatted_time_datetime_hadgem_pic)  # or np.array(formatted_time_datetime)

# Create the DataFrame with temp_diff_gotm_obsgrid_top_135 as the data and formatted_time_series as the index
formatted_time_series_hadgem_pic = pd.Series(formatted_time_datetime_hadgem_pic)



density_difference_surf_top_hypo_hadgem_pic_indexed = pd.Series(density_difference_surf_top_hypo_hadgem_pic, index=pd.to_datetime(formatted_time_series_hadgem_pic ,errors = 'coerce'))
density_difference_surf_top_hypo_hadgem_pic_indexed.index.name = 'Datetime'


density_difference_1m_top_hypo_hadgem_pic_indexed = pd.Series(density_difference_1m_top_hypo_hadgem_pic, index=pd.to_datetime(formatted_time_series_hadgem_pic,errors = 'coerce'))
density_difference_surf_top_hypo_hadgem_pic_indexed.index.name = 'Datetime'
density_difference_1m_top_hypo_hadgem_pic_indexed.index.name = 'Datetime'
"""

#%%rcp26 need to subset untill 2100
kz_hadgem_rcp26_full_prof_gotmgrid=kz_hadgem_rcp26_full_prof_gotmgrid[0:34332]
temp_hadgem_rcp26_full_prof_gotmgrid=temp_hadgem_rcp26_full_prof_gotmgrid[0:34332]

tem_hadgem_rcp26_surf=temp_hadgem_rcp26_full_prof_gotmgrid[: , 41]
tem_hadgem_rcp26_top_hypo= temp_hadgem_rcp26_full_prof_gotmgrid[: , 14]
tem_hadgem_rcp26_1m= temp_hadgem_rcp26_full_prof_gotmgrid[: , 39]
temp_hadgem_rcp26_hypo= temp_hadgem_rcp26_full_prof_gotmgrid[: , 0:14]


density_hadgem_rcp26_surf=Lab_Density(tem_hadgem_rcp26_surf)
density_hadgem_rcp26_1m=Lab_Density(tem_hadgem_rcp26_1m)
density_hadgem_rcp26_top_hypo=Lab_Density(tem_hadgem_rcp26_top_hypo)


density_difference_surf_top_hypo_hadgem_rcp26=density_hadgem_rcp26_surf -density_hadgem_rcp26_top_hypo
density_difference_1m_top_hypo_hadgem_rcp26=density_hadgem_rcp26_1m-density_hadgem_rcp26_top_hypo
# Convert formatted_time_datetime to a pandas Series or NumPy array
formatted_time_series_hadgem_rcp26 = pd.Series(formatted_time_datetime_hadgem_rcp26)  # or np.array(formatted_time_datetime)

# Create the DataFrame with temp_diff_gotm_obsgrid_top_135 as the data and formatted_time_series as the index
formatted_time_series_hadgem_rcp26 = pd.Series(formatted_time_datetime_hadgem_rcp26)

formatted_time_series_hadgem_rcp26=formatted_time_series_hadgem_rcp26[:34332]




density_difference_surf_top_hypo_hadgem_rcp26_indexed = pd.Series(density_difference_surf_top_hypo_hadgem_rcp26, index=pd.to_datetime(formatted_time_series_hadgem_rcp26))
density_difference_surf_top_hypo_hadgem_rcp26_indexed.index.name = 'Datetime'


density_difference_1m_top_hypo_hadgem_rcp26_indexed = pd.Series(density_difference_1m_top_hypo_hadgem_rcp26, index=pd.to_datetime(formatted_time_series_hadgem_rcp26))
density_difference_1m_top_hypo_hadgem_rcp26_indexed.index.name = 'Datetime'

#%%rcp60
kz_hadgem_rcp60_full_prof_gotmgrid
temp_hadgem_rcp60_full_prof_gotmgrid

tem_hadgem_rcp60_surf=temp_hadgem_rcp60_full_prof_gotmgrid[: , 41]
tem_hadgem_rcp60_top_hypo= temp_hadgem_rcp60_full_prof_gotmgrid[: , 14]
tem_hadgem_rcp60_1m= temp_hadgem_rcp60_full_prof_gotmgrid[: , 39]
temp_hadgem_rcp60_hypo= temp_hadgem_rcp60_full_prof_gotmgrid[: , 0:14]


density_hadgem_rcp60_surf=Lab_Density(tem_hadgem_rcp60_surf)
density_hadgem_rcp60_1m=Lab_Density(tem_hadgem_rcp60_1m)
density_hadgem_rcp60_top_hypo=Lab_Density(tem_hadgem_rcp60_top_hypo)


density_difference_surf_top_hypo_hadgem_rcp60=density_hadgem_rcp60_surf -density_hadgem_rcp60_top_hypo
density_difference_1m_top_hypo_hadgem_rcp60=density_hadgem_rcp60_1m-density_hadgem_rcp60_top_hypo
# Convert formatted_time_datetime to a pandas Series or NumPy array
formatted_time_series_hadgem_rcp60 = pd.Series(formatted_time_datetime_hadgem_rcp60)  # or np.array(formatted_time_datetime)

# Create the DataFrame with temp_diff_gotm_obsgrid_top_135 as the data and formatted_time_series as the index
formatted_time_series_hadgem_rcp60 = pd.Series(formatted_time_datetime_hadgem_rcp60)



density_difference_surf_top_hypo_hadgem_rcp60_indexed = pd.Series(density_difference_surf_top_hypo_hadgem_rcp60, index=pd.to_datetime(formatted_time_series_hadgem_rcp60))
density_difference_surf_top_hypo_hadgem_rcp60_indexed.index.name = 'Datetime'


density_difference_1m_top_hypo_hadgem_rcp60_indexed = pd.Series(density_difference_1m_top_hypo_hadgem_rcp60, index=pd.to_datetime(formatted_time_series_hadgem_rcp60))
density_difference_1m_top_hypo_hadgem_rcp60_indexed.index.name = 'Datetime'




#%%rcp85
kz_hadgem_rcp85_full_prof_gotmgrid
temp_hadgem_rcp85_full_prof_gotmgrid

tem_hadgem_rcp85_surf=temp_hadgem_rcp85_full_prof_gotmgrid[: , 41]
tem_hadgem_rcp85_top_hypo= temp_hadgem_rcp85_full_prof_gotmgrid[: , 14]
tem_hadgem_rcp85_1m= temp_hadgem_rcp85_full_prof_gotmgrid[: , 39]
temp_hadgem_rcp85_hypo= temp_hadgem_rcp85_full_prof_gotmgrid[: , 0:14]


density_hadgem_rcp85_surf=Lab_Density(tem_hadgem_rcp85_surf)
density_hadgem_rcp85_1m=Lab_Density(tem_hadgem_rcp85_1m)
density_hadgem_rcp85_top_hypo=Lab_Density(tem_hadgem_rcp85_top_hypo)


density_difference_surf_top_hypo_hadgem_rcp85=density_hadgem_rcp85_surf -density_hadgem_rcp85_top_hypo
density_difference_1m_top_hypo_hadgem_rcp85=density_hadgem_rcp85_1m-density_hadgem_rcp85_top_hypo
# Convert formatted_time_datetime to a pandas Series or NumPy array
formatted_time_series_hadgem_rcp85 = pd.Series(formatted_time_datetime_hadgem_rcp85)  # or np.array(formatted_time_datetime)

# Create the DataFrame with temp_diff_gotm_obsgrid_top_135 as the data and formatted_time_series as the index
formatted_time_series_hadgem_rcp85 = pd.Series(formatted_time_datetime_hadgem_rcp85)



density_difference_surf_top_hypo_hadgem_rcp85_indexed = pd.Series(density_difference_surf_top_hypo_hadgem_rcp85, index=pd.to_datetime(formatted_time_series_hadgem_rcp85))
density_difference_surf_top_hypo_hadgem_rcp85_indexed.index.name = 'Datetime'


density_difference_1m_top_hypo_hadgem_rcp85_indexed = pd.Series(density_difference_1m_top_hypo_hadgem_rcp85, index=pd.to_datetime(formatted_time_series_hadgem_rcp85))
density_difference_1m_top_hypo_hadgem_rcp85_indexed.index.name = 'Datetime'


#%%Resahping from top to bottom 
#%%his

kz_hadgem_his_full_prof_gotmgrid
temp_hadgem_his_full_prof_gotmgrid


temp_hadgem_his_full_prof_TB=temp_hadgem_his_full_prof_gotmgrid[: , ::-1 ]

kz_hadgem_his_full_prof_TB=kz_hadgem_his_full_prof_gotmgrid[: , ::-1 ]

 
unique_z_m_gotm_TB=unique_z_m_gotm[::-1]

np.where(unique_z_m_gotm_TB == -13.75)#27
np.where(unique_z_m_gotm_TB == -14.25)#28
np.where(unique_z_m_gotm_TB == -17.25)#34
np.where(unique_z_m_gotm_TB == -0.25)#0
np.where(unique_z_m_gotm_TB == -1.25)#2




temp_hadgem_his_hypo_TB =temp_hadgem_his_full_prof_TB[:  ,28: ]#  14.25m-20.75m
temp_hadgem_his_meta= temp_hadgem_his_full_prof_TB[:  , 27 ]# 13.75m 

kz_hadgem_his_hypo_TB =kz_hadgem_his_full_prof_TB[:  , 28: ]# 14.25m-20.75m

kz_hadgem_his_hypo_T17 =kz_hadgem_his_full_prof_TB[:  , 28:35 ]# 14.25m-17.25m(34+1)

#%%pic
"""
kz_hadgem_pic_full_prof_gotmgrid
temp_hadgem_pic_full_prof_gotmgrid


temp_hadgem_pic_full_prof_TB=temp_hadgem_pic_full_prof_gotmgrid[: , ::-1 ]

kz_hadgem_pic_full_prof_TB=kz_hadgem_pic_full_prof_gotmgrid[: , ::-1 ]

 
unique_z_m_gotm_TB=unique_z_m_gotm[::-1]

np.where(unique_z_m_gotm_TB == -13.75)#27
np.where(unique_z_m_gotm_TB == -14.25)#28
np.where(unique_z_m_gotm_TB == -17.25)#34
np.where(unique_z_m_gotm_TB == -0.25)#0
np.where(unique_z_m_gotm_TB == -1.25)#2



temp_hadgem_pic_hypo_TB =temp_hadgem_pic_full_prof_TB[:  ,28: ]#  14.25m-20.75m
temp_hadgem_pic_meta= temp_hadgem_pic_full_prof_TB[:  , 27 ]# 13.75m 

kz_hadgem_pic_hypo_TB =kz_hadgem_pic_full_prof_TB[:  , 28: ]# 14.25m-20.75m

kz_hadgem_pic_hypo_T17 =kz_hadgem_pic_full_prof_TB[:  , 28:35 ]# 14.25m-17.25m(34+1)
"""
#%%rcp26

kz_hadgem_rcp26_full_prof_gotmgrid
temp_hadgem_rcp26_full_prof_gotmgrid


temp_hadgem_rcp26_full_prof_TB=temp_hadgem_rcp26_full_prof_gotmgrid[: , ::-1 ]

kz_hadgem_rcp26_full_prof_TB=kz_hadgem_rcp26_full_prof_gotmgrid[: , ::-1 ]

 
unique_z_m_gotm_TB=unique_z_m_gotm[::-1]

np.where(unique_z_m_gotm_TB == -13.75)#27
np.where(unique_z_m_gotm_TB == -14.25)#28
np.where(unique_z_m_gotm_TB == -17.25)#34
np.where(unique_z_m_gotm_TB == -0.25)#0
np.where(unique_z_m_gotm_TB == -1.25)#2




temp_hadgem_rcp26_hypo_TB =temp_hadgem_rcp26_full_prof_TB[:  ,28: ]#  14.25m-20.75m
temp_hadgem_rcp26_meta= temp_hadgem_rcp26_full_prof_TB[:  , 27 ]# 13.75m 

kz_hadgem_rcp26_hypo_TB =kz_hadgem_rcp26_full_prof_TB[:  , 28: ]# 14.25m-20.75m

kz_hadgem_rcp26_hypo_T17 =kz_hadgem_rcp26_full_prof_TB[:  , 28:35 ]# 14.25m-17.25m(34+1)


#%%rcp60

kz_hadgem_rcp60_full_prof_gotmgrid
temp_hadgem_rcp60_full_prof_gotmgrid


temp_hadgem_rcp60_full_prof_TB=temp_hadgem_rcp60_full_prof_gotmgrid[: , ::-1 ]

kz_hadgem_rcp60_full_prof_TB=kz_hadgem_rcp60_full_prof_gotmgrid[: , ::-1 ]

 
unique_z_m_gotm_TB=unique_z_m_gotm[::-1]

np.where(unique_z_m_gotm_TB == -13.75)#27
np.where(unique_z_m_gotm_TB == -14.25)#28
np.where(unique_z_m_gotm_TB == -17.25)#34
np.where(unique_z_m_gotm_TB == -0.25)#0
np.where(unique_z_m_gotm_TB == -1.25)#2


unique_z_m_gotm_hypo_TB=unique_z_m_gotm_TB[28:]


temp_hadgem_rcp60_hypo_TB =temp_hadgem_rcp60_full_prof_TB[:  ,28: ]#  14.25m-20.75m
temp_hadgem_rcp60_meta= temp_hadgem_rcp60_full_prof_TB[:  , 27 ]# 13.75m 

kz_hadgem_rcp60_hypo_TB =kz_hadgem_rcp60_full_prof_TB[:  , 28: ]# 14.25m-20.75m

kz_hadgem_rcp60_hypo_T17 =kz_hadgem_rcp60_full_prof_TB[:  , 28:35 ]# 14.25m-17.25m(34+1)


#%%rcp85

kz_hadgem_rcp85_full_prof_gotmgrid
temp_hadgem_rcp85_full_prof_gotmgrid


temp_hadgem_rcp85_full_prof_TB=temp_hadgem_rcp85_full_prof_gotmgrid[: , ::-1 ]

kz_hadgem_rcp85_full_prof_TB=kz_hadgem_rcp85_full_prof_gotmgrid[: , ::-1 ]

 
unique_z_m_gotm_TB=unique_z_m_gotm[::-1]

np.where(unique_z_m_gotm_TB == -13.75)#27
np.where(unique_z_m_gotm_TB == -14.25)#28
np.where(unique_z_m_gotm_TB == -17.25)#34
np.where(unique_z_m_gotm_TB == -0.25)#0
np.where(unique_z_m_gotm_TB == -1.25)#2


unique_z_m_gotm_hypo_TB=unique_z_m_gotm_TB[28:]


temp_hadgem_rcp85_hypo_TB =temp_hadgem_rcp85_full_prof_TB[:  ,28: ]#  14.25m-20.75m
temp_hadgem_rcp85_meta= temp_hadgem_rcp85_full_prof_TB[:  , 27 ]# 13.75m 

kz_hadgem_rcp85_hypo_TB =kz_hadgem_rcp85_full_prof_TB[:  , 28: ]# 14.25m-20.75m

kz_hadgem_rcp85_hypo_T17 =kz_hadgem_rcp85_full_prof_TB[:  , 28:35 ]# 14.25m-17.25m(34+1)


#%%find_deox_period for each scenarios
#%%his
os.chdir ('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/hadgem_senarios/his')

#df_deox_period_1m_hadgem_his=find_deox_period ( density_difference_1m_top_hypo_hadgem_his_indexed)   

df_deox_period_surf_hadgem_his=find_deox_period ( density_difference_surf_top_hypo_hadgem_his_indexed , np.array(tem_hadgem_his_surf,dtype='<i4')  ) 

df_deox_period_surf_hadgem_his.to_csv('deox_period_surf_hadgem_his.csv', index=False)


#%%pic: problem with date has an error: NameError: name 'df_deox_period_1m_hadgem_pic' is not defined
"""

#df_deox_period_1m_hadgem_pic=find_deox_period ( density_difference_1m_top_hypo_hadgem_pic_indexed)   

df_deox_period_surf_hadgem_pic=find_deox_period ( density_difference_surf_top_hypo_hadgem_pic_indexed , np.array(tem_hadgem_pic_surf,dtype='<i4'))   
"""


#%%rcp26
os.chdir ('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/hadgem_senarios/rcp26')

#df_deox_period_1m_hadgem_rcp26=find_deox_period ( density_difference_1m_top_hypo_hadgem_rcp26_indexed)   

df_deox_period_surf_hadgem_rcp26=find_deox_period ( density_difference_surf_top_hypo_hadgem_rcp26_indexed , np.array(tem_hadgem_rcp26_surf,dtype='<i4'))   

df_deox_period_surf_hadgem_rcp26.to_csv('deox_period_surf_hadgem_rcp26.csv', index=False)


#%%rcp60
os.chdir ('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/hadgem_senarios/rcp60')

#df_deox_period_1m_hadgem_rcp60=find_deox_period ( density_difference_1m_top_hypo_hadgem_rcp60_indexed)   

df_deox_period_surf_hadgem_rcp60=find_deox_period ( density_difference_surf_top_hypo_hadgem_rcp60_indexed,  np.array(tem_hadgem_rcp60_surf,dtype='<i4'))  

df_deox_period_surf_hadgem_rcp60.to_csv('deox_period_surf_hadgem_rcp60.csv', index=False)

#%%rcp85
os.chdir ('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/hadgem_senarios/rcp85')

#df_deox_period_1m_hadgem_rcp85=find_deox_period ( density_difference_1m_top_hypo_hadgem_rcp85_indexed)   

df_deox_period_surf_hadgem_rcp85=find_deox_period ( density_difference_surf_top_hypo_hadgem_rcp85_indexed ,  np.array(tem_hadgem_rcp85_surf,dtype='<i4'))    

df_deox_period_surf_hadgem_rcp85.to_csv('deox_period_surf_hadgem_rcp85.csv', index=False)

#%% Simulation of DO prof
#inital common inputs 

unique_z_m_gotm_hypo_TB
#array([-14.25, -14.75, -15.25, -15.75, -16.25, -16.75, -17.25, -17.75,
#       -18.25, -18.75, -19.25, -19.75, -20.25, -20.75], dtype=float32)

hypo_morpho_vriables_gotm_grid=[np.array (interpolated_bath['V_r'][1:15][::-1]),
                               np.array (interpolated_bath['A_s'][1:15][::-1]),
                               np.array (interpolated_bath['A_l'][1:15][::-1]),
                               0.5, np.array (interpolated_bath['V_r'][1:15][::-1]).size]#V_r, A_s, A_l, dz, nl



#%%onset_date 2020-2100-hadgem

summary_stats(start_dates_Jday(df_deox_period_surf_hadgem_rcp26[df_deox_period_surf_hadgem_rcp26['year']>2019]))
"""
{'Maximum': 137,
 'Minimum': 101,
 'Mean': 118.925,
 'Standard Deviation': 8.526615070293838}
"""

summary_stats(start_dates_Jday(df_deox_period_surf_hadgem_rcp60[df_deox_period_surf_hadgem_rcp60['year']>2019]))
"""
{'Maximum': 140,
 'Minimum': 93,
 'Mean': 116.225,
 'Standard Deviation': 9.691409480644133}
"""

summary_stats(start_dates_Jday(df_deox_period_surf_hadgem_rcp85[df_deox_period_surf_hadgem_rcp85['year']>2019]))
"""
{'Maximum': 134,
 'Minimum': 88,
 'Mean': 111.75,
 'Standard Deviation': 10.239536184116094}
"""





#%%deox_dur 2020-2100-hadgem


#rcp26 ()
summary_stats(annual_deox_duarion(df_deox_period_surf_hadgem_rcp26[df_deox_period_surf_hadgem_rcp26['year']>2019]))
"""
{'Maximum': 164,
 'Minimum': 100,
 'Mean': 132.05,
 'Standard Deviation': 12.497999839974396}
"""


#rcp60 ()
summary_stats(annual_deox_duarion(df_deox_period_surf_hadgem_rcp60[df_deox_period_surf_hadgem_rcp60['year']>2019]))
"""
{'Maximum': 171,
 'Minimum': 102,
 'Mean': 138.775,
 'Standard Deviation': 15.277993605431144}
"""




#rcp85 ()
summary_stats(annual_deox_duarion(df_deox_period_surf_hadgem_rcp85[df_deox_period_surf_hadgem_rcp85['year']>2019]))
"""
{'Maximum': 180,
 'Minimum': 110,
 'Mean': 146.3625,
 'Standard Deviation': 16.336062266646355}
"""

#%%offset_date 2020-2100-hadgem

summary_stats(end_dates_Jday(df_deox_period_surf_hadgem_rcp26[df_deox_period_surf_hadgem_rcp26['year']>2019]))
"""
{'Maximum': 267,
 'Minimum': 230,
 'Mean': 250.975,
 'Standard Deviation': 8.390734793791713}
"""

summary_stats(end_dates_Jday(df_deox_period_surf_hadgem_rcp60[df_deox_period_surf_hadgem_rcp60['year']>2019]))
"""
{'Maximum': 278,
 'Minimum': 231,
 'Mean': 255.0,
 'Standard Deviation': 9.39701002810758}
"""

summary_stats(end_dates_Jday(df_deox_period_surf_hadgem_rcp85[df_deox_period_surf_hadgem_rcp85['year']>2019]))
"""
{'Maximum': 282,
 'Minimum': 237,
 'Mean': 258.1125,
 'Standard Deviation': 10.168197816498413}
"""


#%% number of polymictic years over 2020-2100-hadgem

count_polymictic(df_deox_period_surf_hadgem_rcp26[df_deox_period_surf_hadgem_rcp26['year']>2019])
#8
count_polymictic(df_deox_period_surf_hadgem_rcp60[df_deox_period_surf_hadgem_rcp60['year']>2019])
#2
count_polymictic(df_deox_period_surf_hadgem_rcp85[df_deox_period_surf_hadgem_rcp85['year']>2019])
#3




#%%saving the onset number of years with the year 




#####onset 
baseline_onset_hadgem=baseline_onset_1976_2005(df_deox_period_surf_hadgem_his)[0]



near_future_onset_hadgem_rcp26=near_future_onset_2030_2059(df_deox_period_surf_hadgem_rcp26)[0]

near_future_onset_hadgem_rcp60=near_future_onset_2030_2059(df_deox_period_surf_hadgem_rcp60)[0]

near_future_onset_hadgem_rcp85=near_future_onset_2030_2059(df_deox_period_surf_hadgem_rcp85)[0]




distant_future_onset_hadgem_rcp26=distant_future_onset_2070_2099( df_deox_period_surf_hadgem_rcp26)[0]

distant_future_onset_hadgem_rcp60=distant_future_onset_2070_2099( df_deox_period_surf_hadgem_rcp60)[0]

distant_future_onset_hadgem_rcp85=distant_future_onset_2070_2099( df_deox_period_surf_hadgem_rcp85)[0]



#%%offset 


baseline_offset_hadgem=baseline_offset_1976_2005(df_deox_period_surf_hadgem_his)



near_future_offset_hadgem_rcp26=near_future_offset_2030_2059(df_deox_period_surf_hadgem_rcp26)

near_future_offset_hadgem_rcp60=near_future_offset_2030_2059(df_deox_period_surf_hadgem_rcp60)

near_future_offset_hadgem_rcp85=near_future_offset_2030_2059(df_deox_period_surf_hadgem_rcp85)




distant_future_offset_hadgem_rcp26=distant_future_offset_2070_2099( df_deox_period_surf_hadgem_rcp26)

distant_future_offset_hadgem_rcp60=distant_future_offset_2070_2099( df_deox_period_surf_hadgem_rcp60)

distant_future_offset_hadgem_rcp85=distant_future_offset_2070_2099( df_deox_period_surf_hadgem_rcp85)


#%%duration 


baseline_duration_hadgem=baseline_duration_1976_2005(df_deox_period_surf_hadgem_his)



near_future_duration_hadgem_rcp26=near_future_duration_2030_2059(df_deox_period_surf_hadgem_rcp26)

near_future_duration_hadgem_rcp60=near_future_duration_2030_2059(df_deox_period_surf_hadgem_rcp60)

near_future_duration_hadgem_rcp85=near_future_duration_2030_2059(df_deox_period_surf_hadgem_rcp85)




distant_future_duration_hadgem_rcp26=distant_future_duration_2070_2099( df_deox_period_surf_hadgem_rcp26)

distant_future_duration_hadgem_rcp60=distant_future_duration_2070_2099( df_deox_period_surf_hadgem_rcp60)

distant_future_duration_hadgem_rcp85=distant_future_duration_2070_2099( df_deox_period_surf_hadgem_rcp85)




#%%Reading the winner Ja and Jv ready for apply

#%%####################with variable theta: 
   

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

os.chdir ('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/hadgem_senarios/his')

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

    DO_2D_deox_hadgem_his_hypoprof , temp_2D_deox_hadgem_his_hypoprof  =do_model_comprehensive_gotm([p1 , p2 , 1], density_difference_surf_top_hypo_hadgem_his_indexed , np.array(tem_hadgem_his_surf,dtype='<i4') , hypo_morpho_vriables_gotm_grid 
                               ,temp_hadgem_his_hypo_TB ,kz_hadgem_his_hypo_TB , replanishmnet_rate= 2.7946 )
    #, kz_2D_deox_hadgem_his_hypoprof , full_sat_hypo_condition_his_hadgem
 
    
    # Create a DataFrame for result
    DO_2D_deox_hadgem_his_hypoprof = pd.DataFrame(DO_2D_deox_hadgem_his_hypoprof, columns=[f'{depth}m' for depth in unique_z_m_gotm_hypo_TB])

    # Add a column for dates
    DO_2D_deox_hadgem_his_hypoprof.insert(0, 'Datetime', formatted_time_series_hadgem_his)  # Replace 'your_date_array' with your actual date array

      
    # Define the filename
    DO_filename = f'DO_prof_hadgem_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
    
    # add jv, ja and weights values in the first row 
    header_df = pd.DataFrame([header_values])
    header_df.to_csv(DO_filename, index=False)
    
    
    # Save the result to a CSV file
    DO_2D_deox_hadgem_his_hypoprof.to_csv(DO_filename,mode='a', index=False, na_rep='NaN')#, header=False)  



temp_filename = f'temp_prof_hadgem_his.csv'
kz_filename= f'kz_prof_hadgem_his.csv'
fullsatarray_filename= f'fullsat_array_hadgem_his.csv'


df_temp_deox_hadgem_his_hypoprof =pd.DataFrame(temp_2D_deox_hadgem_his_hypoprof , columns=[f'{depth}m' for depth in unique_z_m_gotm_hypo_TB])
df_temp_deox_hadgem_his_hypoprof.insert(0, 'Datetime', formatted_time_series_hadgem_his) 
df_temp_deox_hadgem_his_hypoprof.to_csv(temp_filename, index=False, na_rep='NaN')# header=False)  
"""
df_kz_deox_hadgem_his_hypoprof =pd.DataFrame(kz_2D_deox_hadgem_his_hypoprof , columns=[f'{depth}m' for depth in unique_z_m_gotm_hypo_TB])
df_kz_deox_hadgem_his_hypoprof.insert(0, 'Datetime', formatted_time_series_hadgem_his) 
df_kz_deox_hadgem_his_hypoprof.to_csv(kz_filename, index=False, na_rep='NaN')# header=False)  

df_fullsat_array_hadgem_his =pd.DataFrame(full_sat_hypo_condition_his_hadgem , columns=[f'{depth}m' for depth in unique_z_m_gotm_hypo_TB])
df_fullsat_array_hadgem_his.insert(0, 'Datetime', formatted_time_series_hadgem_his) 
df_fullsat_array_hadgem_his.to_csv(fullsatarray_filename, index=False, na_rep='NaN')# header=False)  
"""

# Record the end time
end_time = time.time()

# Calculate the elapsed time
elapsed_time = end_time - start_time

# Print the elapsed time in seconds
print(f"The code took {elapsed_time} seconds to run.")

#%%rcp26 DO simulation 
import time

os.chdir ('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/hadgem_senarios/rcp26')

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

    DO_2D_deox_hadgem_rcp26_hypoprof , temp_2D_deox_hadgem_rcp26_hypoprof  =do_model_comprehensive_gotm([p1 , p2 , 1], density_difference_surf_top_hypo_hadgem_rcp26_indexed , np.array(tem_hadgem_rcp26_surf,dtype='<i4') , hypo_morpho_vriables_gotm_grid 
                               ,temp_hadgem_rcp26_hypo_TB ,kz_hadgem_rcp26_hypo_TB , replanishmnet_rate= 2.7946 )
    #, kz_2D_deox_hadgem_rcp26_hypoprof , full_sat_hypo_condition_rcp26_hadgem
 
    
    # Create a DataFrame for result
    DO_2D_deox_hadgem_rcp26_hypoprof = pd.DataFrame(DO_2D_deox_hadgem_rcp26_hypoprof, columns=[f'{depth}m' for depth in unique_z_m_gotm_hypo_TB])

    # Add a column for dates
    DO_2D_deox_hadgem_rcp26_hypoprof.insert(0, 'Datetime', formatted_time_series_hadgem_rcp26)  # Replace 'your_date_array' with your actual date array

      
    # Define the filename
    DO_filename = f'DO_prof_hadgem_rcp26_Jv_{Jv_name}_Ja_{Ja_name}.csv'
    
    # add jv, ja and weights values in the first row 
    header_df = pd.DataFrame([header_values])
    header_df.to_csv(DO_filename, index=False)
    
    
    # Save the result to a CSV file
    DO_2D_deox_hadgem_rcp26_hypoprof.to_csv(DO_filename,mode='a', index=False, na_rep='NaN')#, header=False)  



temp_filename = f'temp_prof_hadgem_rcp26.csv'
kz_filename= f'kz_prof_hadgem_rcp26.csv'
fullsatarray_filename= f'fullsat_array_hadgem_rcp26.csv'


df_temp_deox_hadgem_rcp26_hypoprof =pd.DataFrame(temp_2D_deox_hadgem_rcp26_hypoprof , columns=[f'{depth}m' for depth in unique_z_m_gotm_hypo_TB])
df_temp_deox_hadgem_rcp26_hypoprof.insert(0, 'Datetime', formatted_time_series_hadgem_rcp26) 
df_temp_deox_hadgem_rcp26_hypoprof.to_csv(temp_filename, index=False, na_rep='NaN')# header=False)  
"""
df_kz_deox_hadgem_rcp26_hypoprof =pd.DataFrame(kz_2D_deox_hadgem_rcp26_hypoprof , columns=[f'{depth}m' for depth in unique_z_m_gotm_hypo_TB])
df_kz_deox_hadgem_rcp26_hypoprof.insert(0, 'Datetime', formatted_time_series_hadgem_rcp26) 
df_kz_deox_hadgem_rcp26_hypoprof.to_csv(kz_filename, index=False, na_rep='NaN')# header=False)  

df_fullsat_array_hadgem_rcp26 =pd.DataFrame(full_sat_hypo_condition_rcp26_hadgem , columns=[f'{depth}m' for depth in unique_z_m_gotm_hypo_TB])
df_fullsat_array_hadgem_rcp26.insert(0, 'Datetime', formatted_time_series_hadgem_rcp26) 
df_fullsat_array_hadgem_rcp26.to_csv(fullsatarray_filename, index=False, na_rep='NaN')# header=False)  
"""

# Record the end time
end_time = time.time()

# Calculate the elapsed time
elapsed_time = end_time - start_time

# Print the elapsed time in seconds
print(f"The code took {elapsed_time} seconds to run.")


#%%rcp60 DO simulation 
import time

os.chdir ('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/hadgem_senarios/rcp60')

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

    DO_2D_deox_hadgem_rcp60_hypoprof , temp_2D_deox_hadgem_rcp60_hypoprof  =do_model_comprehensive_gotm([p1 , p2 , 1], density_difference_surf_top_hypo_hadgem_rcp60_indexed , np.array(tem_hadgem_rcp60_surf,dtype='<i4') , hypo_morpho_vriables_gotm_grid 
                               ,temp_hadgem_rcp60_hypo_TB ,kz_hadgem_rcp60_hypo_TB , replanishmnet_rate= 2.7946 )
    #, kz_2D_deox_hadgem_rcp60_hypoprof , full_sat_hypo_condition_rcp60_hadgem
 
    
    # Create a DataFrame for result
    DO_2D_deox_hadgem_rcp60_hypoprof = pd.DataFrame(DO_2D_deox_hadgem_rcp60_hypoprof, columns=[f'{depth}m' for depth in unique_z_m_gotm_hypo_TB])

    # Add a column for dates
    DO_2D_deox_hadgem_rcp60_hypoprof.insert(0, 'Datetime', formatted_time_series_hadgem_rcp60)  # Replace 'your_date_array' with your actual date array

      
    # Define the filename
    DO_filename = f'DO_prof_hadgem_rcp60_Jv_{Jv_name}_Ja_{Ja_name}.csv'
    
    # add jv, ja and weights values in the first row 
    header_df = pd.DataFrame([header_values])
    header_df.to_csv(DO_filename, index=False)
    
    
    # Save the result to a CSV file
    DO_2D_deox_hadgem_rcp60_hypoprof.to_csv(DO_filename,mode='a', index=False, na_rep='NaN')#, header=False)  



temp_filename = f'temp_prof_hadgem_rcp60.csv'
kz_filename= f'kz_prof_hadgem_rcp60.csv'
fullsatarray_filename= f'fullsat_array_hadgem_rcp60.csv'


df_temp_deox_hadgem_rcp60_hypoprof =pd.DataFrame(temp_2D_deox_hadgem_rcp60_hypoprof , columns=[f'{depth}m' for depth in unique_z_m_gotm_hypo_TB])
df_temp_deox_hadgem_rcp60_hypoprof.insert(0, 'Datetime', formatted_time_series_hadgem_rcp60) 
df_temp_deox_hadgem_rcp60_hypoprof.to_csv(temp_filename, index=False, na_rep='NaN')# header=False)  
"""
df_kz_deox_hadgem_rcp60_hypoprof =pd.DataFrame(kz_2D_deox_hadgem_rcp60_hypoprof , columns=[f'{depth}m' for depth in unique_z_m_gotm_hypo_TB])
df_kz_deox_hadgem_rcp60_hypoprof.insert(0, 'Datetime', formatted_time_series_hadgem_rcp60) 
df_kz_deox_hadgem_rcp60_hypoprof.to_csv(kz_filename, index=False, na_rep='NaN')# header=False)  

df_fullsat_array_hadgem_rcp60 =pd.DataFrame(full_sat_hypo_condition_rcp60_hadgem , columns=[f'{depth}m' for depth in unique_z_m_gotm_hypo_TB])
df_fullsat_array_hadgem_rcp60.insert(0, 'Datetime', formatted_time_series_hadgem_rcp60) 
df_fullsat_array_hadgem_rcp60.to_csv(fullsatarray_filename, index=False, na_rep='NaN')# header=False)  
"""

# Record the end time
end_time = time.time()

# Calculate the elapsed time
elapsed_time = end_time - start_time

# Print the elapsed time in seconds
print(f"The code took {elapsed_time} seconds to run.")

#%%rcp85 DO simulation 
import time

os.chdir ('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/hadgem_senarios/rcp85')

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

    DO_2D_deox_hadgem_rcp85_hypoprof , temp_2D_deox_hadgem_rcp85_hypoprof  =do_model_comprehensive_gotm([p1 , p2 , 1], density_difference_surf_top_hypo_hadgem_rcp85_indexed , np.array(tem_hadgem_rcp85_surf,dtype='<i4') , hypo_morpho_vriables_gotm_grid 
                               ,temp_hadgem_rcp85_hypo_TB ,kz_hadgem_rcp85_hypo_TB , replanishmnet_rate= 2.7946 )
    #, kz_2D_deox_hadgem_rcp85_hypoprof , full_sat_hypo_condition_rcp85_hadgem
 
    
    # Create a DataFrame for result
    DO_2D_deox_hadgem_rcp85_hypoprof = pd.DataFrame(DO_2D_deox_hadgem_rcp85_hypoprof, columns=[f'{depth}m' for depth in unique_z_m_gotm_hypo_TB])

    # Add a column for dates
    DO_2D_deox_hadgem_rcp85_hypoprof.insert(0, 'Datetime', formatted_time_series_hadgem_rcp85)  # Replace 'your_date_array' with your actual date array

      
    # Define the filename
    DO_filename = f'DO_prof_hadgem_rcp85_Jv_{Jv_name}_Ja_{Ja_name}.csv'
    
    # add jv, ja and weights values in the first row 
    header_df = pd.DataFrame([header_values])
    header_df.to_csv(DO_filename, index=False)
    
    
    # Save the result to a CSV file
    DO_2D_deox_hadgem_rcp85_hypoprof.to_csv(DO_filename,mode='a', index=False, na_rep='NaN')#, header=False)  



temp_filename = f'temp_prof_hadgem_rcp85.csv'
kz_filename= f'kz_prof_hadgem_rcp85.csv'
fullsatarray_filename= f'fullsat_array_hadgem_rcp85.csv'


df_temp_deox_hadgem_rcp85_hypoprof =pd.DataFrame(temp_2D_deox_hadgem_rcp85_hypoprof , columns=[f'{depth}m' for depth in unique_z_m_gotm_hypo_TB])
df_temp_deox_hadgem_rcp85_hypoprof.insert(0, 'Datetime', formatted_time_series_hadgem_rcp85) 
df_temp_deox_hadgem_rcp85_hypoprof.to_csv(temp_filename, index=False, na_rep='NaN')# header=False)  
"""
df_kz_deox_hadgem_rcp85_hypoprof =pd.DataFrame(kz_2D_deox_hadgem_rcp85_hypoprof , columns=[f'{depth}m' for depth in unique_z_m_gotm_hypo_TB])
df_kz_deox_hadgem_rcp85_hypoprof.insert(0, 'Datetime', formatted_time_series_hadgem_rcp85) 
df_kz_deox_hadgem_rcp85_hypoprof.to_csv(kz_filename, index=False, na_rep='NaN')# header=False)  

df_fullsat_array_hadgem_rcp85 =pd.DataFrame(full_sat_hypo_condition_rcp85_hadgem , columns=[f'{depth}m' for depth in unique_z_m_gotm_hypo_TB])
df_fullsat_array_hadgem_rcp85.insert(0, 'Datetime', formatted_time_series_hadgem_rcp85) 
df_fullsat_array_hadgem_rcp85.to_csv(fullsatarray_filename, index=False, na_rep='NaN')# header=False)  
"""

# Record the end time
end_time = time.time()

# Calculate the elapsed time
elapsed_time = end_time - start_time

# Print the elapsed time in seconds
print(f"The code took {elapsed_time} seconds to run.")

































#%%ave hypolimnetic temp in 2020 and 2021 

# hadgem
"""
#rcp26
temp_ave_hypo_2020_2021_hadgem_rcp26=(temp_hypo_deox_ave_hadgem_rcp26 [(temp_hypo_deox_ave_hadgem_rcp26.index.year == 2021)].mean()+temp_hypo_deox_ave_hadgem_rcp26 [(temp_hypo_deox_ave_hadgem_rcp26.index.year == 2020)].mean())/2
# 9.97460879343274
#rcp60
temp_ave_hypo_2020_2021_hadgem_rcp60=(temp_hypo_deox_ave_hadgem_rcp60 [(temp_hypo_deox_ave_hadgem_rcp60.index.year == 2021)].mean()+temp_hypo_deox_ave_hadgem_rcp60 [(temp_hypo_deox_ave_hadgem_rcp60.index.year == 2020)].mean())/2
#10.145639962171499
#rcp85
temp_ave_hypo_2020_2021_hadgem_rcp85=(temp_hypo_deox_ave_hadgem_rcp85 [(temp_hypo_deox_ave_hadgem_rcp85.index.year == 2021)].mean()+temp_hypo_deox_ave_hadgem_rcp85 [(temp_hypo_deox_ave_hadgem_rcp85.index.year == 2020)].mean())/2
#10.279446038053411


#%% testing new idea of average of temp in 2020 and 2021 of each scenarios 


# hadgem
#rcp26
temp_ave_hypo_2020_2021_hadgem_rcp26=(temp_hypo_deox_ave_hadgem_rcp26 [(temp_hypo_deox_ave_hadgem_rcp26.index.year == 2021)].dropna()[0] +temp_hypo_deox_ave_hadgem_rcp26 [(temp_hypo_deox_ave_hadgem_rcp26.index.year == 2020)].dropna()[0])/2
# 10.71454337033238# ave temp 2020, 2021
#5.339681126608722# onset temp 2020 and 2021
#rcp60
temp_ave_hypo_2020_2021_hadgem_rcp60=(temp_hypo_deox_ave_hadgem_rcp60 [(temp_hypo_deox_ave_hadgem_rcp60.index.year == 2021)].dropna()[0] +temp_hypo_deox_ave_hadgem_rcp60 [(temp_hypo_deox_ave_hadgem_rcp60.index.year == 2020)].dropna()[0])/2
#9.295762932087847
#4.33706446795583
#rcp85
temp_ave_hypo_2020_2021_hadgem_rcp85=(temp_hypo_deox_ave_hadgem_rcp85 [(temp_hypo_deox_ave_hadgem_rcp85.index.year == 2021)].dropna()[0] +temp_hypo_deox_ave_hadgem_rcp85 [(temp_hypo_deox_ave_hadgem_rcp85.index.year == 2020)].dropna()[0])/2
#10.140706151244498
#6.466027301242095




#%%
temp_ave_hypo_2020_2021_hadgem_rcp26=temp_ave_hypo_2020_2021_hadgem_rcp60=temp_ave_hypo_2020_2021_hadgem_rcp85=9.460405011459684
"""

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
os.chdir ('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/hadgem_senarios/his')


######original test : variable theta: not ave temp in two days in rows 
######os.chdir ('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/hadgem_senarios/his_notavetemp')


###### test with fixed theta
######os.chdir ('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/hadgem_senarios/his_fixedtheta')


###### test with fixed theta at onset temp
######os.chdir ('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/hadgem_senarios/his_fixedtheta_at_temp_onset')


###### test with fixed theta at onset_tempave_onsettodeephypoxia in both calib and simulation
######os.chdir ('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/hadgem_senarios/his_fixedtheta_at_tempave_onsettodeephypoxia')


###### test with fixed theta at onset_tempave_onsettodeephypoxia in calib_but not in simulation
######os.chdir ('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/hadgem_senarios/his_fixedtheta_at_tempave_onsettodeephypoxia')


###### test with fixed theta in calibration but variable for GOTM simulation 
######os.chdir ('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/hadgem_senarios/his_calibinfixedtheta_simuvartheta')






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

    DO_2D_deox_hadgem_his_hypoprof , temp_2D_deox_hadgem_his_hypoprof , kz_2D_deox_hadgem_his_hypoprof , full_sat_hypo_condition_his_hadgem =do_model_comprehensive_gotm([p1 , p2 , 1], density_difference_surf_top_hypo_hadgem_his_indexed , np.array(tem_hadgem_his_surf,dtype='<i4') , hypo_morpho_vriables_gotm_grid 
                               ,temp_hadgem_his_hypo_TB ,kz_hadgem_his_hypo_TB , replanishmnet_rate= 2.7946 )
    
    DO_2D_deox_hadgem_his_mixingincl , temp_2D_deox_hadgem_his_mixingincl, kz_2D_deox_hadgem_his_mixingincl= mixing_incl_do_model_comprehensive_gotm([p1 , p2 , 1], density_difference_surf_top_hypo_hadgem_his_indexed , np.array(tem_hadgem_his_surf,dtype='<i4') , hypo_morpho_vriables_gotm_grid 
                               ,temp_hadgem_his_hypo_TB ,kz_hadgem_his_hypo_TB , replanishmnet_rate= 2.7946 )
    
    # Create a DataFrame for result
    DO_2D_deox_hadgem_his_hypoprof = pd.DataFrame(DO_2D_deox_hadgem_his_hypoprof, columns=[f'{depth}m' for depth in unique_z_m_gotm_hypo_TB])

    DO_2D_deox_hadgem_his_mixingincl= pd.DataFrame(DO_2D_deox_hadgem_his_mixingincl, columns=[f'{depth}m' for depth in unique_z_m_gotm_hypo_TB])
    
    # Add a column for dates
    DO_2D_deox_hadgem_his_hypoprof.insert(0, 'Datetime', formatted_time_series_hadgem_his)  # Replace 'your_date_array' with your actual date array
    DO_2D_deox_hadgem_his_mixingincl.insert(0, 'Datetime', formatted_time_series_hadgem_his)
      
    # Define the filename
    DO_filename = f'DO_prof_hadgem_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
    
    mixingincl_DO_filename = f'mixingincl_DO_prof_hadgem_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'

    
    # add jv, ja and weights values in the first row 
    header_df = pd.DataFrame([header_values])
    header_df.to_csv(DO_filename, index=False)
    header_df.to_csv(mixingincl_DO_filename, index=False)
    
    
    # Save the result to a CSV file
    DO_2D_deox_hadgem_his_hypoprof.to_csv(DO_filename,mode='a', index=False, na_rep='NaN')#, header=False)  

    DO_2D_deox_hadgem_his_mixingincl.to_csv(mixingincl_DO_filename,mode='a', index=False, na_rep='NaN')

temp_filename = f'temp_prof_hadgem_his.csv'
kz_filename= f'kz_prof_hadgem_his.csv'

temp_filename_mixingincl = f'mixingincl_temp_prof_hadgem_his.csv'
kz_filename_mixingincl= f'mixingincl_kz_prof_hadgem_his.csv'

fullsatarray_filename= f'fullsat_array_hadgem_his.csv'


df_temp_deox_hadgem_his_hypoprof =pd.DataFrame(temp_2D_deox_hadgem_his_hypoprof , columns=[f'{depth}m' for depth in unique_z_m_gotm_hypo_TB])
df_temp_deox_hadgem_his_hypoprof.insert(0, 'Datetime', formatted_time_series_hadgem_his) 
df_temp_deox_hadgem_his_hypoprof.to_csv(temp_filename, index=False, na_rep='NaN')# header=False)  

df_kz_deox_hadgem_his_hypoprof =pd.DataFrame(kz_2D_deox_hadgem_his_hypoprof , columns=[f'{depth}m' for depth in unique_z_m_gotm_hypo_TB])
df_kz_deox_hadgem_his_hypoprof.insert(0, 'Datetime', formatted_time_series_hadgem_his) 
df_kz_deox_hadgem_his_hypoprof.to_csv(kz_filename, index=False, na_rep='NaN')# header=False)  


####_mixingincl

df_temp_deox_hadgem_his_hypoprof_mixingincl =pd.DataFrame(temp_2D_deox_hadgem_his_mixingincl , columns=[f'{depth}m' for depth in unique_z_m_gotm_hypo_TB])
df_temp_deox_hadgem_his_hypoprof_mixingincl.insert(0, 'Datetime', formatted_time_series_hadgem_his) 
df_temp_deox_hadgem_his_hypoprof_mixingincl.to_csv(temp_filename_mixingincl, index=False, na_rep='NaN')# header=False)  

df_kz_deox_hadgem_his_hypoprof_mixingincl =pd.DataFrame(kz_2D_deox_hadgem_his_mixingincl , columns=[f'{depth}m' for depth in unique_z_m_gotm_hypo_TB])
df_kz_deox_hadgem_his_hypoprof_mixingincl.insert(0, 'Datetime', formatted_time_series_hadgem_his) 
df_kz_deox_hadgem_his_hypoprof_mixingincl.to_csv(kz_filename_mixingincl, index=False, na_rep='NaN')# header=False)  



df_fullsat_array_hadgem_his =pd.DataFrame(full_sat_hypo_condition_his_hadgem , columns=[f'{depth}m' for depth in unique_z_m_gotm_hypo_TB])
df_fullsat_array_hadgem_his.insert(0, 'Datetime', formatted_time_series_hadgem_his) 
df_fullsat_array_hadgem_his.to_csv(fullsatarray_filename, index=False, na_rep='NaN')# header=False)  


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
os.chdir ('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/hadgem_senarios/rcp26')


######original test : variable theta: not ave temp in two days in rows 
######os.chdir ('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/hadgem_senarios/rcp26_notavetemp')


###### test with fixed theta
######os.chdir ('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/hadgem_senarios/rcp26_fixedtheta')


###### test with fixed theta at onset temp
######os.chdir ('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/hadgem_senarios/rcp26_fixedtheta_at_temp_onset')


###### test with fixed theta at onset_tempave_onsettodeephypoxia in both calib and simulation
######os.chdir ('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/hadgem_senarios/rcp26_fixedtheta_at_tempave_onsettodeephypoxia')


###### test with fixed theta at onset_tempave_onsettodeephypoxia in calib_but not in simulation
######os.chdir ('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/hadgem_senarios/rcp26_fixedtheta_at_tempave_onsettodeephypoxia')


###### test with fixed theta in calibration but variable for GOTM simulation 
######os.chdir ('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/hadgem_senarios/rcp26_calibinfixedtheta_simuvartheta')






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

    DO_2D_deox_hadgem_rcp26_hypoprof , temp_2D_deox_hadgem_rcp26_hypoprof , kz_2D_deox_hadgem_rcp26_hypoprof , full_sat_hypo_condition_rcp26_hadgem =do_model_comprehensive_gotm([p1 , p2 , 1], density_difference_surf_top_hypo_hadgem_rcp26_indexed , np.array(tem_hadgem_rcp26_surf,dtype='<i4') , hypo_morpho_vriables_gotm_grid 
                               ,temp_hadgem_rcp26_hypo_TB ,kz_hadgem_rcp26_hypo_TB , replanishmnet_rate= 2.7946 )
    
    DO_2D_deox_hadgem_rcp26_mixingincl , temp_2D_deox_hadgem_rcp26_mixingincl, kz_2D_deox_hadgem_rcp26_mixingincl= mixing_incl_do_model_comprehensive_gotm([p1 , p2 , 1], density_difference_surf_top_hypo_hadgem_rcp26_indexed , np.array(tem_hadgem_rcp26_surf,dtype='<i4') , hypo_morpho_vriables_gotm_grid 
                               ,temp_hadgem_rcp26_hypo_TB ,kz_hadgem_rcp26_hypo_TB , replanishmnet_rate= 2.7946 )
    
    # Create a DataFrame for result
    DO_2D_deox_hadgem_rcp26_hypoprof = pd.DataFrame(DO_2D_deox_hadgem_rcp26_hypoprof, columns=[f'{depth}m' for depth in unique_z_m_gotm_hypo_TB])

    DO_2D_deox_hadgem_rcp26_mixingincl= pd.DataFrame(DO_2D_deox_hadgem_rcp26_mixingincl, columns=[f'{depth}m' for depth in unique_z_m_gotm_hypo_TB])
    
    # Add a column for dates
    DO_2D_deox_hadgem_rcp26_hypoprof.insert(0, 'Datetime', formatted_time_series_hadgem_rcp26)  # Replace 'your_date_array' with your actual date array
    DO_2D_deox_hadgem_rcp26_mixingincl.insert(0, 'Datetime', formatted_time_series_hadgem_rcp26)
      
    # Define the filename
    DO_filename = f'DO_prof_hadgem_rcp26_Jv_{Jv_name}_Ja_{Ja_name}.csv'
    
    mixingincl_DO_filename = f'mixingincl_DO_prof_hadgem_rcp26_Jv_{Jv_name}_Ja_{Ja_name}.csv'

    
    # add jv, ja and weights values in the first row 
    header_df = pd.DataFrame([header_values])
    header_df.to_csv(DO_filename, index=False)
    header_df.to_csv(mixingincl_DO_filename, index=False)
    
    
    # Save the result to a CSV file
    DO_2D_deox_hadgem_rcp26_hypoprof.to_csv(DO_filename,mode='a', index=False, na_rep='NaN')#, header=False)  

    DO_2D_deox_hadgem_rcp26_mixingincl.to_csv(mixingincl_DO_filename,mode='a', index=False, na_rep='NaN')

temp_filename = f'temp_prof_hadgem_rcp26.csv'
kz_filename= f'kz_prof_hadgem_rcp26.csv'

temp_filename_mixingincl = f'mixingincl_temp_prof_hadgem_rcp26.csv'
kz_filename_mixingincl= f'mixingincl_kz_prof_hadgem_rcp26.csv'

fullsatarray_filename= f'fullsat_array_hadgem_rcp26.csv'


df_temp_deox_hadgem_rcp26_hypoprof =pd.DataFrame(temp_2D_deox_hadgem_rcp26_hypoprof , columns=[f'{depth}m' for depth in unique_z_m_gotm_hypo_TB])
df_temp_deox_hadgem_rcp26_hypoprof.insert(0, 'Datetime', formatted_time_series_hadgem_rcp26) 
df_temp_deox_hadgem_rcp26_hypoprof.to_csv(temp_filename, index=False, na_rep='NaN')# header=False)  

df_kz_deox_hadgem_rcp26_hypoprof =pd.DataFrame(kz_2D_deox_hadgem_rcp26_hypoprof , columns=[f'{depth}m' for depth in unique_z_m_gotm_hypo_TB])
df_kz_deox_hadgem_rcp26_hypoprof.insert(0, 'Datetime', formatted_time_series_hadgem_rcp26) 
df_kz_deox_hadgem_rcp26_hypoprof.to_csv(kz_filename, index=False, na_rep='NaN')# header=False)  


####_mixingincl

df_temp_deox_hadgem_rcp26_hypoprof_mixingincl =pd.DataFrame(temp_2D_deox_hadgem_rcp26_mixingincl , columns=[f'{depth}m' for depth in unique_z_m_gotm_hypo_TB])
df_temp_deox_hadgem_rcp26_hypoprof_mixingincl.insert(0, 'Datetime', formatted_time_series_hadgem_rcp26) 
df_temp_deox_hadgem_rcp26_hypoprof_mixingincl.to_csv(temp_filename_mixingincl, index=False, na_rep='NaN')# header=False)  

df_kz_deox_hadgem_rcp26_hypoprof_mixingincl =pd.DataFrame(kz_2D_deox_hadgem_rcp26_mixingincl , columns=[f'{depth}m' for depth in unique_z_m_gotm_hypo_TB])
df_kz_deox_hadgem_rcp26_hypoprof_mixingincl.insert(0, 'Datetime', formatted_time_series_hadgem_rcp26) 
df_kz_deox_hadgem_rcp26_hypoprof_mixingincl.to_csv(kz_filename_mixingincl, index=False, na_rep='NaN')# header=False)  



df_fullsat_array_hadgem_rcp26 =pd.DataFrame(full_sat_hypo_condition_rcp26_hadgem , columns=[f'{depth}m' for depth in unique_z_m_gotm_hypo_TB])
df_fullsat_array_hadgem_rcp26.insert(0, 'Datetime', formatted_time_series_hadgem_rcp26) 
df_fullsat_array_hadgem_rcp26.to_csv(fullsatarray_filename, index=False, na_rep='NaN')# header=False)  


# Record the end time
end_time = time.time()

# Calculate the elapsed time
elapsed_time = end_time - start_time

# Print the elapsed time in seconds
print(f"The code took {elapsed_time} seconds to run.")
#%%rcp26-attribution test 

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
os.chdir ('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/hadgem_senarios/rcp26_initialcond_attribution')


######original test : variable theta: not ave temp in two days in rows 
######os.chdir ('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/hadgem_senarios/rcp26_notavetemp')


###### test with fixed theta
######os.chdir ('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/hadgem_senarios/rcp26_fixedtheta')


###### test with fixed theta at onset temp
######os.chdir ('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/hadgem_senarios/rcp26_fixedtheta_at_temp_onset')


###### test with fixed theta at onset_tempave_onsettodeephypoxia in both calib and simulation
######os.chdir ('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/hadgem_senarios/rcp26_fixedtheta_at_tempave_onsettodeephypoxia')


###### test with fixed theta at onset_tempave_onsettodeephypoxia in calib_but not in simulation
######os.chdir ('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/hadgem_senarios/rcp26_fixedtheta_at_tempave_onsettodeephypoxia')


###### test with fixed theta in calibration but variable for GOTM simulation 
######os.chdir ('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/hadgem_senarios/rcp26_calibinfixedtheta_simuvartheta')






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

    DO_2D_deox_hadgem_rcp26_hypoprof_att_test =do_model_comprehensive_gotm_rcp26_test([p1 , p2 , 1], density_difference_surf_top_hypo_hadgem_rcp26_indexed , np.array(tem_hadgem_rcp26_surf,dtype='<i4') , hypo_morpho_vriables_gotm_grid 
                               ,temp_hadgem_rcp26_hypo_TB ,kz_hadgem_rcp26_hypo_TB , replanishmnet_rate= 2.7946 )[0]
    
    DO_2D_deox_hadgem_rcp26_mixingincl_att_test = mixing_incl_do_model_comprehensive_gotm_rcp26_test([p1 , p2 , 1], density_difference_surf_top_hypo_hadgem_rcp26_indexed , np.array(tem_hadgem_rcp26_surf,dtype='<i4') , hypo_morpho_vriables_gotm_grid 
                               ,temp_hadgem_rcp26_hypo_TB ,kz_hadgem_rcp26_hypo_TB , replanishmnet_rate= 2.7946 )[0]
    
    # Create a DataFrame for result
    DO_2D_deox_hadgem_rcp26_hypoprof_att_test = pd.DataFrame(DO_2D_deox_hadgem_rcp26_hypoprof_att_test, columns=[f'{depth}m' for depth in unique_z_m_gotm_hypo_TB])

    DO_2D_deox_hadgem_rcp26_mixingincl_att_test= pd.DataFrame(DO_2D_deox_hadgem_rcp26_mixingincl_att_test, columns=[f'{depth}m' for depth in unique_z_m_gotm_hypo_TB])
    
    # Add a column for dates
    DO_2D_deox_hadgem_rcp26_hypoprof_att_test.insert(0, 'Datetime', formatted_time_series_hadgem_rcp26)  # Replace 'your_date_array' with your actual date array
    DO_2D_deox_hadgem_rcp26_mixingincl_att_test.insert(0, 'Datetime', formatted_time_series_hadgem_rcp26)
      
    # Define the filename
    DO_filename_att_test = f'DO_prof_hadgem_rcp26_att_test_Jv_{Jv_name}_Ja_{Ja_name}.csv'
    
    mixingincl_DO_filename_att_test = f'mixingincl_DO_prof_hadgem_rcp26_att_test_Jv_{Jv_name}_Ja_{Ja_name}.csv'

    
    # add jv, ja and weights values in the first row 
    header_df = pd.DataFrame([header_values])
    header_df.to_csv(DO_filename_att_test, index=False)
    header_df.to_csv(mixingincl_DO_filename_att_test, index=False)
    
    
    # Save the result to a CSV file
    DO_2D_deox_hadgem_rcp26_hypoprof_att_test.to_csv(DO_filename_att_test,mode='a', index=False, na_rep='NaN')#, header=False)  

    DO_2D_deox_hadgem_rcp26_mixingincl_att_test.to_csv(mixingincl_DO_filename_att_test,mode='a', index=False, na_rep='NaN')

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
os.chdir ('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/hadgem_senarios/rcp60')


######original test : variable theta: not ave temp in two days in rows 
######os.chdir ('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/hadgem_senarios/rcp60_notavetemp')


###### test with fixed theta
######os.chdir ('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/hadgem_senarios/rcp60_fixedtheta')


###### test with fixed theta at onset temp
######os.chdir ('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/hadgem_senarios/rcp60_fixedtheta_at_temp_onset')


###### test with fixed theta at onset_tempave_onsettodeephypoxia in both calib and simulation
######os.chdir ('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/hadgem_senarios/rcp60_fixedtheta_at_tempave_onsettodeephypoxia')


###### test with fixed theta at onset_tempave_onsettodeephypoxia in calib_but not in simulation
######os.chdir ('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/hadgem_senarios/rcp60_fixedtheta_at_tempave_onsettodeephypoxia')


###### test with fixed theta in calibration but variable for GOTM simulation 
######os.chdir ('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/hadgem_senarios/rcp60_calibinfixedtheta_simuvartheta')






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

    DO_2D_deox_hadgem_rcp60_hypoprof , temp_2D_deox_hadgem_rcp60_hypoprof , kz_2D_deox_hadgem_rcp60_hypoprof , full_sat_hypo_condition_rcp60_hadgem =do_model_comprehensive_gotm([p1 , p2 , 1], density_difference_surf_top_hypo_hadgem_rcp60_indexed , np.array(tem_hadgem_rcp60_surf,dtype='<i4') , hypo_morpho_vriables_gotm_grid 
                               ,temp_hadgem_rcp60_hypo_TB ,kz_hadgem_rcp60_hypo_TB , replanishmnet_rate= 2.7946 )
    
    DO_2D_deox_hadgem_rcp60_mixingincl , temp_2D_deox_hadgem_rcp60_mixingincl, kz_2D_deox_hadgem_rcp60_mixingincl= mixing_incl_do_model_comprehensive_gotm([p1 , p2 , 1], density_difference_surf_top_hypo_hadgem_rcp60_indexed , np.array(tem_hadgem_rcp60_surf,dtype='<i4') , hypo_morpho_vriables_gotm_grid 
                               ,temp_hadgem_rcp60_hypo_TB ,kz_hadgem_rcp60_hypo_TB , replanishmnet_rate= 2.7946 )
    
    # Create a DataFrame for result
    DO_2D_deox_hadgem_rcp60_hypoprof = pd.DataFrame(DO_2D_deox_hadgem_rcp60_hypoprof, columns=[f'{depth}m' for depth in unique_z_m_gotm_hypo_TB])

    DO_2D_deox_hadgem_rcp60_mixingincl= pd.DataFrame(DO_2D_deox_hadgem_rcp60_mixingincl, columns=[f'{depth}m' for depth in unique_z_m_gotm_hypo_TB])
    
    # Add a column for dates
    DO_2D_deox_hadgem_rcp60_hypoprof.insert(0, 'Datetime', formatted_time_series_hadgem_rcp60)  # Replace 'your_date_array' with your actual date array
    DO_2D_deox_hadgem_rcp60_mixingincl.insert(0, 'Datetime', formatted_time_series_hadgem_rcp60)
      
    # Define the filename
    DO_filename = f'DO_prof_hadgem_rcp60_Jv_{Jv_name}_Ja_{Ja_name}.csv'
    
    mixingincl_DO_filename = f'mixingincl_DO_prof_hadgem_rcp60_Jv_{Jv_name}_Ja_{Ja_name}.csv'

    
    # add jv, ja and weights values in the first row 
    header_df = pd.DataFrame([header_values])
    header_df.to_csv(DO_filename, index=False)
    header_df.to_csv(mixingincl_DO_filename, index=False)
    
    
    # Save the result to a CSV file
    DO_2D_deox_hadgem_rcp60_hypoprof.to_csv(DO_filename,mode='a', index=False, na_rep='NaN')#, header=False)  

    DO_2D_deox_hadgem_rcp60_mixingincl.to_csv(mixingincl_DO_filename,mode='a', index=False, na_rep='NaN')

temp_filename = f'temp_prof_hadgem_rcp60.csv'
kz_filename= f'kz_prof_hadgem_rcp60.csv'

temp_filename_mixingincl = f'mixingincl_temp_prof_hadgem_rcp60.csv'
kz_filename_mixingincl= f'mixingincl_kz_prof_hadgem_rcp60.csv'

fullsatarray_filename= f'fullsat_array_hadgem_rcp60.csv'


df_temp_deox_hadgem_rcp60_hypoprof =pd.DataFrame(temp_2D_deox_hadgem_rcp60_hypoprof , columns=[f'{depth}m' for depth in unique_z_m_gotm_hypo_TB])
df_temp_deox_hadgem_rcp60_hypoprof.insert(0, 'Datetime', formatted_time_series_hadgem_rcp60) 
df_temp_deox_hadgem_rcp60_hypoprof.to_csv(temp_filename, index=False, na_rep='NaN')# header=False)  

df_kz_deox_hadgem_rcp60_hypoprof =pd.DataFrame(kz_2D_deox_hadgem_rcp60_hypoprof , columns=[f'{depth}m' for depth in unique_z_m_gotm_hypo_TB])
df_kz_deox_hadgem_rcp60_hypoprof.insert(0, 'Datetime', formatted_time_series_hadgem_rcp60) 
df_kz_deox_hadgem_rcp60_hypoprof.to_csv(kz_filename, index=False, na_rep='NaN')# header=False)  


####_mixingincl

df_temp_deox_hadgem_rcp60_hypoprof_mixingincl =pd.DataFrame(temp_2D_deox_hadgem_rcp60_mixingincl , columns=[f'{depth}m' for depth in unique_z_m_gotm_hypo_TB])
df_temp_deox_hadgem_rcp60_hypoprof_mixingincl.insert(0, 'Datetime', formatted_time_series_hadgem_rcp60) 
df_temp_deox_hadgem_rcp60_hypoprof_mixingincl.to_csv(temp_filename_mixingincl, index=False, na_rep='NaN')# header=False)  

df_kz_deox_hadgem_rcp60_hypoprof_mixingincl =pd.DataFrame(kz_2D_deox_hadgem_rcp60_mixingincl , columns=[f'{depth}m' for depth in unique_z_m_gotm_hypo_TB])
df_kz_deox_hadgem_rcp60_hypoprof_mixingincl.insert(0, 'Datetime', formatted_time_series_hadgem_rcp60) 
df_kz_deox_hadgem_rcp60_hypoprof_mixingincl.to_csv(kz_filename_mixingincl, index=False, na_rep='NaN')# header=False)  



df_fullsat_array_hadgem_rcp60 =pd.DataFrame(full_sat_hypo_condition_rcp60_hadgem , columns=[f'{depth}m' for depth in unique_z_m_gotm_hypo_TB])
df_fullsat_array_hadgem_rcp60.insert(0, 'Datetime', formatted_time_series_hadgem_rcp60) 
df_fullsat_array_hadgem_rcp60.to_csv(fullsatarray_filename, index=False, na_rep='NaN')# header=False)  


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
os.chdir ('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/hadgem_senarios/rcp85')


######original test : variable theta: not ave temp in two days in rows 
######os.chdir ('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/hadgem_senarios/rcp85_notavetemp')


###### test with fixed theta
######os.chdir ('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/hadgem_senarios/rcp85_fixedtheta')


###### test with fixed theta at onset temp
######os.chdir ('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/hadgem_senarios/rcp85_fixedtheta_at_temp_onset')


###### test with fixed theta at onset_tempave_onsettodeephypoxia in both calib and simulation
######os.chdir ('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/hadgem_senarios/rcp85_fixedtheta_at_tempave_onsettodeephypoxia')


###### test with fixed theta at onset_tempave_onsettodeephypoxia in calib_but not in simulation
######os.chdir ('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/hadgem_senarios/rcp85_fixedtheta_at_tempave_onsettodeephypoxia')


###### test with fixed theta in calibration but variable for GOTM simulation 
######os.chdir ('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/hadgem_senarios/rcp85_calibinfixedtheta_simuvartheta')






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

    DO_2D_deox_hadgem_rcp85_hypoprof , temp_2D_deox_hadgem_rcp85_hypoprof , kz_2D_deox_hadgem_rcp85_hypoprof , full_sat_hypo_condition_rcp85_hadgem =do_model_comprehensive_gotm([p1 , p2 , 1], density_difference_surf_top_hypo_hadgem_rcp85_indexed , np.array(tem_hadgem_rcp85_surf,dtype='<i4') , hypo_morpho_vriables_gotm_grid 
                               ,temp_hadgem_rcp85_hypo_TB ,kz_hadgem_rcp85_hypo_TB , replanishmnet_rate= 2.7946 )
    
    DO_2D_deox_hadgem_rcp85_mixingincl , temp_2D_deox_hadgem_rcp85_mixingincl, kz_2D_deox_hadgem_rcp85_mixingincl= mixing_incl_do_model_comprehensive_gotm([p1 , p2 , 1], density_difference_surf_top_hypo_hadgem_rcp85_indexed , np.array(tem_hadgem_rcp85_surf,dtype='<i4') , hypo_morpho_vriables_gotm_grid 
                               ,temp_hadgem_rcp85_hypo_TB ,kz_hadgem_rcp85_hypo_TB , replanishmnet_rate= 2.7946 )
    
    # Create a DataFrame for result
    DO_2D_deox_hadgem_rcp85_hypoprof = pd.DataFrame(DO_2D_deox_hadgem_rcp85_hypoprof, columns=[f'{depth}m' for depth in unique_z_m_gotm_hypo_TB])

    DO_2D_deox_hadgem_rcp85_mixingincl= pd.DataFrame(DO_2D_deox_hadgem_rcp85_mixingincl, columns=[f'{depth}m' for depth in unique_z_m_gotm_hypo_TB])
    
    # Add a column for dates
    DO_2D_deox_hadgem_rcp85_hypoprof.insert(0, 'Datetime', formatted_time_series_hadgem_rcp85)  # Replace 'your_date_array' with your actual date array
    DO_2D_deox_hadgem_rcp85_mixingincl.insert(0, 'Datetime', formatted_time_series_hadgem_rcp85)
      
    # Define the filename
    DO_filename = f'DO_prof_hadgem_rcp85_Jv_{Jv_name}_Ja_{Ja_name}.csv'
    
    mixingincl_DO_filename = f'mixingincl_DO_prof_hadgem_rcp85_Jv_{Jv_name}_Ja_{Ja_name}.csv'

    
    # add jv, ja and weights values in the first row 
    header_df = pd.DataFrame([header_values])
    header_df.to_csv(DO_filename, index=False)
    header_df.to_csv(mixingincl_DO_filename, index=False)
    
    
    # Save the result to a CSV file
    DO_2D_deox_hadgem_rcp85_hypoprof.to_csv(DO_filename,mode='a', index=False, na_rep='NaN')#, header=False)  

    DO_2D_deox_hadgem_rcp85_mixingincl.to_csv(mixingincl_DO_filename,mode='a', index=False, na_rep='NaN')

temp_filename = f'temp_prof_hadgem_rcp85.csv'
kz_filename= f'kz_prof_hadgem_rcp85.csv'

temp_filename_mixingincl = f'mixingincl_temp_prof_hadgem_rcp85.csv'
kz_filename_mixingincl= f'mixingincl_kz_prof_hadgem_rcp85.csv'

fullsatarray_filename= f'fullsat_array_hadgem_rcp85.csv'


df_temp_deox_hadgem_rcp85_hypoprof =pd.DataFrame(temp_2D_deox_hadgem_rcp85_hypoprof , columns=[f'{depth}m' for depth in unique_z_m_gotm_hypo_TB])
df_temp_deox_hadgem_rcp85_hypoprof.insert(0, 'Datetime', formatted_time_series_hadgem_rcp85) 
df_temp_deox_hadgem_rcp85_hypoprof.to_csv(temp_filename, index=False, na_rep='NaN')# header=False)  

df_kz_deox_hadgem_rcp85_hypoprof =pd.DataFrame(kz_2D_deox_hadgem_rcp85_hypoprof , columns=[f'{depth}m' for depth in unique_z_m_gotm_hypo_TB])
df_kz_deox_hadgem_rcp85_hypoprof.insert(0, 'Datetime', formatted_time_series_hadgem_rcp85) 
df_kz_deox_hadgem_rcp85_hypoprof.to_csv(kz_filename, index=False, na_rep='NaN')# header=False)  


####_mixingincl

df_temp_deox_hadgem_rcp85_hypoprof_mixingincl =pd.DataFrame(temp_2D_deox_hadgem_rcp85_mixingincl , columns=[f'{depth}m' for depth in unique_z_m_gotm_hypo_TB])
df_temp_deox_hadgem_rcp85_hypoprof_mixingincl.insert(0, 'Datetime', formatted_time_series_hadgem_rcp85) 
df_temp_deox_hadgem_rcp85_hypoprof_mixingincl.to_csv(temp_filename_mixingincl, index=False, na_rep='NaN')# header=False)  

df_kz_deox_hadgem_rcp85_hypoprof_mixingincl =pd.DataFrame(kz_2D_deox_hadgem_rcp85_mixingincl , columns=[f'{depth}m' for depth in unique_z_m_gotm_hypo_TB])
df_kz_deox_hadgem_rcp85_hypoprof_mixingincl.insert(0, 'Datetime', formatted_time_series_hadgem_rcp85) 
df_kz_deox_hadgem_rcp85_hypoprof_mixingincl.to_csv(kz_filename_mixingincl, index=False, na_rep='NaN')# header=False)  



df_fullsat_array_hadgem_rcp85 =pd.DataFrame(full_sat_hypo_condition_rcp85_hadgem , columns=[f'{depth}m' for depth in unique_z_m_gotm_hypo_TB])
df_fullsat_array_hadgem_rcp85.insert(0, 'Datetime', formatted_time_series_hadgem_rcp85) 
df_fullsat_array_hadgem_rcp85.to_csv(fullsatarray_filename, index=False, na_rep='NaN')# header=False)  


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
os.chdir ('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/hadgem_senarios/rcp26_C_daily_VHOD_mangement_test')


start_time = time.time()

for par_jz in jz_management_test:
    p1 = par_jz[0]
    
    header_values = {'Jz': p1}
    # Round Ja and Jv to 3 decimal places
    Jz_name = round(p1, 3)


    DO_2D_deox_hadgem_rcp26_hypoprof =do_model_comprehensive_VHOD_gotm([p1 , 1], density_difference_surf_top_hypo_hadgem_rcp26_indexed , np.array(tem_hadgem_rcp26_surf,dtype='<i4') , hypo_morpho_vriables_gotm_grid 
                               ,temp_hadgem_rcp26_hypo_TB ,kz_hadgem_rcp26_hypo_TB , replanishmnet_rate= 2.7946  )[0]
    

    DO_2D_deox_hadgem_rcp26_mixingincl =mixing_incl_do_model_comprehensive_VHOD_gotm([p1 , 1], density_difference_surf_top_hypo_hadgem_rcp26_indexed , np.array(tem_hadgem_rcp26_surf,dtype='<i4') , hypo_morpho_vriables_gotm_grid 
                               ,temp_hadgem_rcp26_hypo_TB ,kz_hadgem_rcp26_hypo_TB , replanishmnet_rate= 2.7946  )[0]
    
    
    
    # Create a DataFrame for result
    DO_2D_deox_hadgem_rcp26_hypoprof = pd.DataFrame(DO_2D_deox_hadgem_rcp26_hypoprof, columns=[f'{depth}m' for depth in unique_z_m_gotm_hypo_TB])
    DO_2D_deox_hadgem_rcp26_mixingincl= pd.DataFrame(DO_2D_deox_hadgem_rcp26_mixingincl, columns=[f'{depth}m' for depth in unique_z_m_gotm_hypo_TB])
    # Add a column for dates
    DO_2D_deox_hadgem_rcp26_hypoprof.insert(0, 'Datetime', formatted_time_series_hadgem_rcp26)  # Replace 'your_date_array' with your actual date array
    DO_2D_deox_hadgem_rcp26_mixingincl.insert(0, 'Datetime', formatted_time_series_hadgem_rcp26)  # Replace 'your_date_array' with your actual date array
      
    # Define the filename
    DO_filename = f'DO_prof_hadgem_rcp26_Jz_{Jz_name}.csv'
    mixingincl_DO_filename = f'mixingincl_DO_prof_hadgem_rcp26_Jz_{Jz_name}.csv'
    
    # add jv, ja and weights values in the first row 
    header_df = pd.DataFrame([header_values])
    header_df.to_csv(DO_filename, index=False)
    header_df.to_csv(mixingincl_DO_filename, index=False)
    
    
    # Save the result to a CSV file
    DO_2D_deox_hadgem_rcp26_hypoprof.to_csv(DO_filename,mode='a', index=False, na_rep='NaN')#, header=False)  
    DO_2D_deox_hadgem_rcp26_mixingincl.to_csv(mixingincl_DO_filename,mode='a', index=False, na_rep='NaN')



# Record the end time
end_time = time.time()

# Calculate the elapsed time
elapsed_time = end_time - start_time

# Print the elapsed time in seconds
print(f"The code took {elapsed_time} seconds to run.")



#%%RCP6.0 only with Jz

import time

######managemnet test
os.chdir ('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/hadgem_senarios/rcp60_C_daily_VHOD_mangement_test')


start_time = time.time()

for par_jz in jz_management_test:
    p1 = par_jz[0]
    
    header_values = {'Jz': p1}
    # Round Ja and Jv to 3 decimal places
    Jz_name = round(p1, 3)


    DO_2D_deox_hadgem_rcp60_hypoprof =do_model_comprehensive_VHOD_gotm([p1 , 1], density_difference_surf_top_hypo_hadgem_rcp60_indexed , np.array(tem_hadgem_rcp60_surf,dtype='<i4') , hypo_morpho_vriables_gotm_grid 
                               ,temp_hadgem_rcp60_hypo_TB ,kz_hadgem_rcp60_hypo_TB , replanishmnet_rate= 2.7946  )[0]
    

    DO_2D_deox_hadgem_rcp60_mixingincl =mixing_incl_do_model_comprehensive_VHOD_gotm([p1 , 1], density_difference_surf_top_hypo_hadgem_rcp60_indexed , np.array(tem_hadgem_rcp60_surf,dtype='<i4') , hypo_morpho_vriables_gotm_grid 
                               ,temp_hadgem_rcp60_hypo_TB ,kz_hadgem_rcp60_hypo_TB , replanishmnet_rate= 2.7946  )[0]
    
    
    
    # Create a DataFrame for result
    DO_2D_deox_hadgem_rcp60_hypoprof = pd.DataFrame(DO_2D_deox_hadgem_rcp60_hypoprof, columns=[f'{depth}m' for depth in unique_z_m_gotm_hypo_TB])
    DO_2D_deox_hadgem_rcp60_mixingincl= pd.DataFrame(DO_2D_deox_hadgem_rcp60_mixingincl, columns=[f'{depth}m' for depth in unique_z_m_gotm_hypo_TB])
    # Add a column for dates
    DO_2D_deox_hadgem_rcp60_hypoprof.insert(0, 'Datetime', formatted_time_series_hadgem_rcp60)  # Replace 'your_date_array' with your actual date array
    DO_2D_deox_hadgem_rcp60_mixingincl.insert(0, 'Datetime', formatted_time_series_hadgem_rcp60)  # Replace 'your_date_array' with your actual date array
      
    # Define the filename
    DO_filename = f'DO_prof_hadgem_rcp60_Jz_{Jz_name}.csv'
    mixingincl_DO_filename = f'mixingincl_DO_prof_hadgem_rcp60_Jz_{Jz_name}.csv'
    
    # add jv, ja and weights values in the first row 
    header_df = pd.DataFrame([header_values])
    header_df.to_csv(DO_filename, index=False)
    header_df.to_csv(mixingincl_DO_filename, index=False)
    
    
    # Save the result to a CSV file
    DO_2D_deox_hadgem_rcp60_hypoprof.to_csv(DO_filename,mode='a', index=False, na_rep='NaN')#, header=False)  
    DO_2D_deox_hadgem_rcp60_mixingincl.to_csv(mixingincl_DO_filename,mode='a', index=False, na_rep='NaN')



# Record the end time
end_time = time.time()

# Calculate the elapsed time
elapsed_time = end_time - start_time

# Print the elapsed time in seconds
print(f"The code took {elapsed_time} seconds to run.")



#%%RCP8.5 only with Jz

import time

######managemnet test
os.chdir ('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/hadgem_senarios/rcp85_C_daily_VHOD_mangement_test')


start_time = time.time()

for par_jz in jz_management_test:
    p1 = par_jz[0]
    
    header_values = {'Jz': p1}
    # Round Ja and Jv to 3 decimal places
    Jz_name = round(p1, 3)


    DO_2D_deox_hadgem_rcp85_hypoprof =do_model_comprehensive_VHOD_gotm([p1 , 1], density_difference_surf_top_hypo_hadgem_rcp85_indexed , np.array(tem_hadgem_rcp85_surf,dtype='<i4') , hypo_morpho_vriables_gotm_grid 
                               ,temp_hadgem_rcp85_hypo_TB ,kz_hadgem_rcp85_hypo_TB , replanishmnet_rate= 2.7946  )[0]
    

    DO_2D_deox_hadgem_rcp85_mixingincl =mixing_incl_do_model_comprehensive_VHOD_gotm([p1 , 1], density_difference_surf_top_hypo_hadgem_rcp85_indexed , np.array(tem_hadgem_rcp85_surf,dtype='<i4') , hypo_morpho_vriables_gotm_grid 
                               ,temp_hadgem_rcp85_hypo_TB ,kz_hadgem_rcp85_hypo_TB , replanishmnet_rate= 2.7946  )[0]
    
    
    
    # Create a DataFrame for result
    DO_2D_deox_hadgem_rcp85_hypoprof = pd.DataFrame(DO_2D_deox_hadgem_rcp85_hypoprof, columns=[f'{depth}m' for depth in unique_z_m_gotm_hypo_TB])
    DO_2D_deox_hadgem_rcp85_mixingincl= pd.DataFrame(DO_2D_deox_hadgem_rcp85_mixingincl, columns=[f'{depth}m' for depth in unique_z_m_gotm_hypo_TB])
    # Add a column for dates
    DO_2D_deox_hadgem_rcp85_hypoprof.insert(0, 'Datetime', formatted_time_series_hadgem_rcp85)  # Replace 'your_date_array' with your actual date array
    DO_2D_deox_hadgem_rcp85_mixingincl.insert(0, 'Datetime', formatted_time_series_hadgem_rcp85)  # Replace 'your_date_array' with your actual date array
      
    # Define the filename
    DO_filename = f'DO_prof_hadgem_rcp85_Jz_{Jz_name}.csv'
    mixingincl_DO_filename = f'mixingincl_DO_prof_hadgem_rcp85_Jz_{Jz_name}.csv'
    
    # add jv, ja and weights values in the first row 
    header_df = pd.DataFrame([header_values])
    header_df.to_csv(DO_filename, index=False)
    header_df.to_csv(mixingincl_DO_filename, index=False)
    
    
    # Save the result to a CSV file
    DO_2D_deox_hadgem_rcp85_hypoprof.to_csv(DO_filename,mode='a', index=False, na_rep='NaN')#, header=False)  
    DO_2D_deox_hadgem_rcp85_mixingincl.to_csv(mixingincl_DO_filename,mode='a', index=False, na_rep='NaN')



# Record the end time
end_time = time.time()

# Calculate the elapsed time
elapsed_time = end_time - start_time

# Print the elapsed time in seconds
print(f"The code took {elapsed_time} seconds to run.")





#%%OLD
#%%2.Ja and Jv mangement 



#%%definding different combinations of Ja and Jv less than current 

jv_min, jv_max = 0.001, 0.6#Max and min after calibrtaion (16 behavioral sets)
ja_min, ja_max = 0.001, 1.2 #Max and min after calibrtaion (16 behavioral sets)

num_points1 =len(np.arange(jv_min, jv_max+0.1 , 0.1))
num_points2 =len(np.arange(ja_min , ja_max+0.1 , 0.1))

param1_values = np.arange(jv_min, jv_max+0.1 , 0.1)
param2_values = np.arange(ja_min , ja_max+0.1 , 0.1)




JvJa_management_test=[]
for i, p1 in enumerate(param1_values):
    for j, p2 in enumerate(param2_values):
        
        JvJa_management_test.append([p1, p2 , 1])
              

for i in JvJa_management_test:
    print(i)
 
     
    
 
#%%RCP2.6

import time

######managemnet test
os.chdir ('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/hadgem_senarios/rcp26_C_daily_mangement_test')


start_time = time.time()

for jvja in JvJa_management_test:
    p1 = jvja[0]
    p2 = jvja[1]
    header_values = {'Jv': p1, 'Ja': p2}
    # Round Ja and Jv to 3 decimal places
    Jv_name = round(p1, 3)
    Ja_name = round(p2, 3)

    DO_2D_deox_hadgem_rcp26_hypoprof , temp_2D_deox_hadgem_rcp26_hypoprof , kz_2D_deox_hadgem_rcp26_hypoprof , full_sat_hypo_condition_rcp26_hadgem =do_model_comprehensive_gotm([p1 , p2 , 1], density_difference_surf_top_hypo_hadgem_rcp26_indexed , np.array(tem_hadgem_rcp26_surf,dtype='<i4') , hypo_morpho_vriables_gotm_grid 
                               ,temp_hadgem_rcp26_hypo_TB ,kz_hadgem_rcp26_hypo_TB , replanishmnet_rate= 2.7946  )
    
 
    
    # Create a DataFrame for result
    DO_2D_deox_hadgem_rcp26_hypoprof = pd.DataFrame(DO_2D_deox_hadgem_rcp26_hypoprof, columns=[f'{depth}m' for depth in unique_z_m_gotm_hypo_TB])

    # Add a column for dates
    DO_2D_deox_hadgem_rcp26_hypoprof.insert(0, 'Datetime', formatted_time_series_hadgem_rcp26)  # Replace 'your_date_array' with your actual date array

      
    # Define the filename
    DO_filename = f'DO_prof_hadgem_rcp26_Jv_{Jv_name}_Ja_{Ja_name}.csv'
    
    # add jv, ja and weights values in the first row 
    header_df = pd.DataFrame([header_values])
    header_df.to_csv(DO_filename, index=False)
    
    
    # Save the result to a CSV file
    DO_2D_deox_hadgem_rcp26_hypoprof.to_csv(DO_filename,mode='a', index=False, na_rep='NaN')#, header=False)  



temp_filename = f'temp_prof_hadgem_rcp26.csv'
kz_filename= f'kz_prof_hadgem_rcp26.csv'
fullsatarray_filename= f'fullsat_array_hadgem_rcp26.csv'


df_temp_deox_hadgem_rcp26_hypoprof =pd.DataFrame(temp_2D_deox_hadgem_rcp26_hypoprof , columns=[f'{depth}m' for depth in unique_z_m_gotm_hypo_TB])
df_temp_deox_hadgem_rcp26_hypoprof.insert(0, 'Datetime', formatted_time_series_hadgem_rcp26) 
df_temp_deox_hadgem_rcp26_hypoprof.to_csv(temp_filename, index=False, na_rep='NaN')# header=False)  

df_kz_deox_hadgem_rcp26_hypoprof =pd.DataFrame(kz_2D_deox_hadgem_rcp26_hypoprof , columns=[f'{depth}m' for depth in unique_z_m_gotm_hypo_TB])
df_kz_deox_hadgem_rcp26_hypoprof.insert(0, 'Datetime', formatted_time_series_hadgem_rcp26) 
df_kz_deox_hadgem_rcp26_hypoprof.to_csv(kz_filename, index=False, na_rep='NaN')# header=False)  

df_fullsat_array_hadgem_rcp26 =pd.DataFrame(full_sat_hypo_condition_rcp26_hadgem , columns=[f'{depth}m' for depth in unique_z_m_gotm_hypo_TB])
df_fullsat_array_hadgem_rcp26.insert(0, 'Datetime', formatted_time_series_hadgem_rcp26) 
df_fullsat_array_hadgem_rcp26.to_csv(fullsatarray_filename, index=False, na_rep='NaN')# header=False)  


# Record the end time
end_time = time.time()

# Calculate the elapsed time
elapsed_time = end_time - start_time

# Print the elapsed time in seconds
print(f"The code took {elapsed_time} seconds to run.")




#%%RCP6.0


######managemnet test
os.chdir ('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/hadgem_senarios/rcp60_C_daily_mangement_test')


start_time = time.time()

for jvja in JvJa_management_test:
    p1 = jvja[0]
    p2 = jvja[1]
    header_values = {'Jv': p1, 'Ja': p2}
    # Round Ja and Jv to 3 decimal places
    Jv_name = round(p1, 3)
    Ja_name = round(p2, 3)

    DO_2D_deox_hadgem_rcp60_hypoprof , temp_2D_deox_hadgem_rcp60_hypoprof , kz_2D_deox_hadgem_rcp60_hypoprof , full_sat_hypo_condition_rcp60_hadgem =do_model_comprehensive_gotm([p1 , p2 , 1], density_difference_surf_top_hypo_hadgem_rcp60_indexed , np.array(tem_hadgem_rcp60_surf,dtype='<i4') , hypo_morpho_vriables_gotm_grid 
                               ,temp_hadgem_rcp60_hypo_TB ,kz_hadgem_rcp60_hypo_TB , replanishmnet_rate= 2.7946  )
    
 
    
    # Create a DataFrame for result
    DO_2D_deox_hadgem_rcp60_hypoprof = pd.DataFrame(DO_2D_deox_hadgem_rcp60_hypoprof, columns=[f'{depth}m' for depth in unique_z_m_gotm_hypo_TB])

    # Add a column for dates
    DO_2D_deox_hadgem_rcp60_hypoprof.insert(0, 'Datetime', formatted_time_series_hadgem_rcp60)  # Replace 'your_date_array' with your actual date array

      
    # Define the filename
    DO_filename = f'DO_prof_hadgem_rcp60_Jv_{Jv_name}_Ja_{Ja_name}.csv'
    
    # add jv, ja and weights values in the first row 
    header_df = pd.DataFrame([header_values])
    header_df.to_csv(DO_filename, index=False)
    
    
    # Save the result to a CSV file
    DO_2D_deox_hadgem_rcp60_hypoprof.to_csv(DO_filename,mode='a', index=False, na_rep='NaN')#, header=False)  



temp_filename = f'temp_prof_hadgem_rcp60.csv'
kz_filename= f'kz_prof_hadgem_rcp60.csv'
fullsatarray_filename= f'fullsat_array_hadgem_rcp60.csv'


df_temp_deox_hadgem_rcp60_hypoprof =pd.DataFrame(temp_2D_deox_hadgem_rcp60_hypoprof , columns=[f'{depth}m' for depth in unique_z_m_gotm_hypo_TB])
df_temp_deox_hadgem_rcp60_hypoprof.insert(0, 'Datetime', formatted_time_series_hadgem_rcp60) 
df_temp_deox_hadgem_rcp60_hypoprof.to_csv(temp_filename, index=False, na_rep='NaN')# header=False)  

df_kz_deox_hadgem_rcp60_hypoprof =pd.DataFrame(kz_2D_deox_hadgem_rcp60_hypoprof , columns=[f'{depth}m' for depth in unique_z_m_gotm_hypo_TB])
df_kz_deox_hadgem_rcp60_hypoprof.insert(0, 'Datetime', formatted_time_series_hadgem_rcp60) 
df_kz_deox_hadgem_rcp60_hypoprof.to_csv(kz_filename, index=False, na_rep='NaN')# header=False)  

df_fullsat_array_hadgem_rcp60 =pd.DataFrame(full_sat_hypo_condition_rcp60_hadgem , columns=[f'{depth}m' for depth in unique_z_m_gotm_hypo_TB])
df_fullsat_array_hadgem_rcp60.insert(0, 'Datetime', formatted_time_series_hadgem_rcp60) 
df_fullsat_array_hadgem_rcp60.to_csv(fullsatarray_filename, index=False, na_rep='NaN')# header=False)  


# Record the end time
end_time = time.time()

# Calculate the elapsed time
elapsed_time = end_time - start_time

# Print the elapsed time in seconds
print(f"The code took {elapsed_time} seconds to run.")



#%%RCP8.5


######managemnet test
os.chdir ('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/hadgem_senarios/rcp85_C_daily_mangement_test')


start_time = time.time()

for jvja in JvJa_management_test:
    p1 = jvja[0]
    p2 = jvja[1]
    header_values = {'Jv': p1, 'Ja': p2}
    # Round Ja and Jv to 3 decimal places
    Jv_name = round(p1, 3)
    Ja_name = round(p2, 3)

    DO_2D_deox_hadgem_rcp85_hypoprof , temp_2D_deox_hadgem_rcp85_hypoprof , kz_2D_deox_hadgem_rcp85_hypoprof , full_sat_hypo_condition_rcp85_hadgem =do_model_comprehensive_gotm([p1 , p2 , 1], density_difference_surf_top_hypo_hadgem_rcp85_indexed , np.array(tem_hadgem_rcp85_surf,dtype='<i4') , hypo_morpho_vriables_gotm_grid 
                               ,temp_hadgem_rcp85_hypo_TB ,kz_hadgem_rcp85_hypo_TB , replanishmnet_rate= 2.7946  )
    
 
    
    # Create a DataFrame for result
    DO_2D_deox_hadgem_rcp85_hypoprof = pd.DataFrame(DO_2D_deox_hadgem_rcp85_hypoprof, columns=[f'{depth}m' for depth in unique_z_m_gotm_hypo_TB])

    # Add a column for dates
    DO_2D_deox_hadgem_rcp85_hypoprof.insert(0, 'Datetime', formatted_time_series_hadgem_rcp85)  # Replace 'your_date_array' with your actual date array

      
    # Define the filename
    DO_filename = f'DO_prof_hadgem_rcp85_Jv_{Jv_name}_Ja_{Ja_name}.csv'
    
    # add jv, ja and weights values in the first row 
    header_df = pd.DataFrame([header_values])
    header_df.to_csv(DO_filename, index=False)
    
    
    # Save the result to a CSV file
    DO_2D_deox_hadgem_rcp85_hypoprof.to_csv(DO_filename,mode='a', index=False, na_rep='NaN')#, header=False)  



temp_filename = f'temp_prof_hadgem_rcp85.csv'
kz_filename= f'kz_prof_hadgem_rcp85.csv'
fullsatarray_filename= f'fullsat_array_hadgem_rcp85.csv'


df_temp_deox_hadgem_rcp85_hypoprof =pd.DataFrame(temp_2D_deox_hadgem_rcp85_hypoprof , columns=[f'{depth}m' for depth in unique_z_m_gotm_hypo_TB])
df_temp_deox_hadgem_rcp85_hypoprof.insert(0, 'Datetime', formatted_time_series_hadgem_rcp85) 
df_temp_deox_hadgem_rcp85_hypoprof.to_csv(temp_filename, index=False, na_rep='NaN')# header=False)  

df_kz_deox_hadgem_rcp85_hypoprof =pd.DataFrame(kz_2D_deox_hadgem_rcp85_hypoprof , columns=[f'{depth}m' for depth in unique_z_m_gotm_hypo_TB])
df_kz_deox_hadgem_rcp85_hypoprof.insert(0, 'Datetime', formatted_time_series_hadgem_rcp85) 
df_kz_deox_hadgem_rcp85_hypoprof.to_csv(kz_filename, index=False, na_rep='NaN')# header=False)  

df_fullsat_array_hadgem_rcp85 =pd.DataFrame(full_sat_hypo_condition_rcp85_hadgem , columns=[f'{depth}m' for depth in unique_z_m_gotm_hypo_TB])
df_fullsat_array_hadgem_rcp85.insert(0, 'Datetime', formatted_time_series_hadgem_rcp85) 
df_fullsat_array_hadgem_rcp85.to_csv(fullsatarray_filename, index=False, na_rep='NaN')# header=False)  


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
#########directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/hadgem_senarios/his'

######original test : variable theta: not ave temp in two days in rows 
######directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/hadgem_senarios/his_notavetemp'




########fixed theta both in calib and simulation 
########directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/hadgem_senarios/his_fixedtheta'


###### test with fixed theta at onset temp
##### directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/hadgem_senarios/his_fixedtheta_at_temp_onset'



######test ave temp onset to deep hypoxia
########directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/hadgem_senarios/his_fixedtheta_at_tempave_onsettodeephypoxia'




# test with fixed theta in calibration but variable for GOTM simulation 
directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/hadgem_senarios/his_calibinfixedtheta_simuvartheta'



# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("DO_prof_hadgem_his_Jv_"):
        
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
        result_filename = f'hypolimnetic_ave_hadgem_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename), index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='Datetime', na_rep='NaN', header=['Hypolimnetic_Ave'])
        
             
#%%rcp26
import os
import pandas as pd

# Specify the directory where the CSV files are located
#########original test with variable theta:
#########directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/hadgem_senarios/rcp26'


######attribution test  on initial condition with incaresement on the initial condition 
######directory =  'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/hadgem_senarios/rcp26_initialcond_attribution'


######attribution test  on initial condition with swiching of the changes of initial condition with assuming the intercpt fixed 
directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/hadgem_senarios/rcp26_initialcond_fixedintercpt_attribution'



######original test : variable theta: not ave temp in two days in rows 
######directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/hadgem_senarios/rcp26_notavetemp'




######## fixed theta both in calib and simulation 
#########directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/hadgem_senarios/rcp26_fixedtheta'


###### test with fixed theta in calibration a temp ave hypo in gfd rcp26 for years 2020 and 2021
########directory='C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/hadgem_senarios/rcp26_fixedthetaincalib_simurcp26temp20202021'




###### test with fixed theta in calibration at onset temp ave hypo in hadgem rcp26 for years 2020 and 2021
#####directory='C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/hadgem_senarios/rcp26_fixedthetaincalib_at_temp_onsetsimurcp26'


######test ave temp onset to deep hypoxia
########directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/hadgem_senarios/rcp26_fixedtheta_at_tempave_onsettodeephypoxia'


##### test with fixed theta in calibration but variable for GOTM simulation 
#####directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/hadgem_senarios/rcp26_calibinfixedtheta_simuvartheta'



# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("DO_prof_hadgem_rcp26_Jv_"):
        
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
        result_filename = f'hypolimnetic_ave_hadgem_rcp26_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename), index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='Datetime', na_rep='NaN', header=['Hypolimnetic_Ave'])
        
        

#%%rcp60
import os
import pandas as pd

# Specify the directory where the CSV files are located
#########original test with variable theta:
#########directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/hadgem_senarios/rcp60'


######original test : variable theta: not ave temp in two days in rows 
#######directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/hadgem_senarios/rcp60_notavetemp'



######## fixed theta both in calib and simulation 
#######directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/hadgem_senarios/rcp60_fixedtheta'


###### test with fixed theta in calibration a temp ave hypo in gfd rcp60 for years 2020 and 2021
########directory ='C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/hadgem_senarios/rcp60_fixedthetaincalib_simurcp60temp20202021'



###### test with fixed theta in calibration at onset temp ave hypo in hadgem rcp60 for years 2020 and 2021
#####directory='C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/hadgem_senarios/rcp60_fixedthetaincalib_at_temp_onsetsimurcp60'


######test ave temp onset to deep hypoxia
######directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/hadgem_senarios/rcp60_fixedtheta_at_tempave_onsettodeephypoxia'


# test with fixed theta in calibration but variable for GOTM simulation 
directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/hadgem_senarios/rcp60_calibinfixedtheta_simuvartheta'




# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("DO_prof_hadgem_rcp60_Jv_"):
        
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
        result_filename = f'hypolimnetic_ave_hadgem_rcp60_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename), index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='Datetime', na_rep='NaN', header=['Hypolimnetic_Ave'])
        
#%%rcp85
import os
import pandas as pd

# Specify the directory where the CSV files are located
#########original test with variable theta:
#########directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/hadgem_senarios/rcp85'


######original test : variable theta: not ave temp in two days in rows 
######directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/hadgem_senarios/rcp85_notavetemp'



######## fixed theta both in calib and simulation 
######## directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/hadgem_senarios/rcp85_fixedtheta'



###### test with fixed theta in calibration a temp ave hypo in gfd rcp85 for years 2020 and 2021
########directory= 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/hadgem_senarios/rcp85_fixedthetaincalib_simurcp85temp20202021'


###### test with fixed theta in calibration at onset temp ave hypo in hadgem rcp85 for years 2020 and 2021
#####directory='C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/hadgem_senarios/rcp85_fixedthetaincalib_at_temp_onsetsimurcp85'


######test ave temp onset to deep hypoxia
directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/hadgem_senarios/rcp85_fixedtheta_at_tempave_onsettodeephypoxia'

# test with fixed theta in calibration but variable for GOTM simulation 
########directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/hadgem_senarios/rcp85_calibinfixedtheta_simuvartheta'



# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("DO_prof_hadgem_rcp85_Jv_"):
        
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
        result_filename = f'hypolimnetic_ave_hadgem_rcp85_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename), index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='Datetime', na_rep='NaN', header=['Hypolimnetic_Ave'])
        
                
