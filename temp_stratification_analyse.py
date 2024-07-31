# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 15:57:35 2024

@author: mahta
"""


#%%number of polimictic years over baseline 




count_polymictic(df_deox_period_surf_gfdl_his[df_deox_period_surf_gfdl_his['year']>1975])
#4
count_polymictic(df_deox_period_surf_hadgem_his[df_deox_period_surf_hadgem_his['year']>1975])
#1
count_polymictic(df_deox_period_surf_ipsl_his[df_deox_period_surf_ipsl_his['year']>1975])
#1
count_polymictic(df_deox_period_surf_miroc_his[df_deox_period_surf_miroc_his['year']>1975])
#3



np.array([4, 1, 1, 3]).mean()#2.25
np.array([4, 1, 1, 3]).std()#1.30





#%%number of polimictic years over near future 





count_polymictic(df_deox_period_surf_gfdl_rcp26[(df_deox_period_surf_gfdl_rcp26['year']>2029) &(df_deox_period_surf_gfdl_rcp26['year']<2060)])
#3
count_polymictic(df_deox_period_surf_gfdl_rcp60[(df_deox_period_surf_gfdl_rcp60['year']>2029) &(df_deox_period_surf_gfdl_rcp60['year']<2060)])
#2
count_polymictic(df_deox_period_surf_gfdl_rcp85[(df_deox_period_surf_gfdl_rcp85['year']>2029) &(df_deox_period_surf_gfdl_rcp85['year']<2060)])
#4




count_polymictic(df_deox_period_surf_hadgem_rcp26[(df_deox_period_surf_hadgem_rcp26['year']>2029) &(df_deox_period_surf_hadgem_rcp26['year']<2060)])
#3
count_polymictic(df_deox_period_surf_hadgem_rcp60[(df_deox_period_surf_hadgem_rcp60['year']>2029) &(df_deox_period_surf_hadgem_rcp60['year']<2060)])
#0
count_polymictic(df_deox_period_surf_hadgem_rcp85[(df_deox_period_surf_hadgem_rcp85['year']>2029) &(df_deox_period_surf_hadgem_rcp85['year']<2060)])
#0






count_polymictic(df_deox_period_surf_ipsl_rcp26[(df_deox_period_surf_ipsl_rcp26['year']>2029) &(df_deox_period_surf_ipsl_rcp26['year']<2060)])
#8
count_polymictic(df_deox_period_surf_ipsl_rcp60[(df_deox_period_surf_ipsl_rcp60['year']>2029) &(df_deox_period_surf_ipsl_rcp60['year']<2060)])
#5
count_polymictic(df_deox_period_surf_ipsl_rcp85[(df_deox_period_surf_ipsl_rcp85['year']>2029) &(df_deox_period_surf_ipsl_rcp85['year']<2060)])
#5





count_polymictic(df_deox_period_surf_miroc_rcp26[(df_deox_period_surf_miroc_rcp26['year']>2029) &(df_deox_period_surf_miroc_rcp26['year']<2060)])
#1
count_polymictic(df_deox_period_surf_miroc_rcp60[(df_deox_period_surf_miroc_rcp60['year']>2029) &(df_deox_period_surf_miroc_rcp60['year']<2060)])
#2
count_polymictic(df_deox_period_surf_miroc_rcp85[(df_deox_period_surf_miroc_rcp85['year']>2029) &(df_deox_period_surf_miroc_rcp85['year']<2060)])
#1





#######2030-2059


#rcp2.6
np.array([3, 3, 8, 1]).mean()#3.75
np.array([3, 3, 8, 1]).std()#2.56
#rcp6.0
np.array([2, 0, 5, 2]).mean()#2.25
np.array([2, 0, 5, 2]).std()#1.78
# rcp8.5
np.array([4, 0, 5, 1]).mean()#2.5
np.array([4, 0, 5, 1]).std()#2.06















#%%number of polimictic years over distant future 





count_polymictic(df_deox_period_surf_gfdl_rcp26[df_deox_period_surf_gfdl_rcp26['year']>2069])
#2
count_polymictic(df_deox_period_surf_gfdl_rcp60[df_deox_period_surf_gfdl_rcp60['year']>2069])
#2
count_polymictic(df_deox_period_surf_gfdl_rcp85[df_deox_period_surf_gfdl_rcp85['year']>2069])
#4





count_polymictic(df_deox_period_surf_hadgem_rcp26[df_deox_period_surf_hadgem_rcp26['year']>2069])
#3
count_polymictic(df_deox_period_surf_hadgem_rcp60[df_deox_period_surf_hadgem_rcp60['year']>2069])
#1
count_polymictic(df_deox_period_surf_hadgem_rcp85[df_deox_period_surf_hadgem_rcp85['year']>2069])
#1





count_polymictic(df_deox_period_surf_ipsl_rcp26[df_deox_period_surf_ipsl_rcp26['year']>2069])
#6
count_polymictic(df_deox_period_surf_ipsl_rcp60[df_deox_period_surf_ipsl_rcp60['year']>2069])
#3
count_polymictic(df_deox_period_surf_ipsl_rcp85[df_deox_period_surf_ipsl_rcp85['year']>2069])
#6




count_polymictic(df_deox_period_surf_miroc_rcp26[df_deox_period_surf_miroc_rcp26['year']>2069])
#4
count_polymictic(df_deox_period_surf_miroc_rcp60[df_deox_period_surf_miroc_rcp60['year']>2069])
#0
count_polymictic(df_deox_period_surf_miroc_rcp85[df_deox_period_surf_miroc_rcp85['year']>2069])
#1



#######2070-2100


#rcp2.6
np.array([2, 3, 6, 4]).mean()#3.75
np.array([2, 3, 6, 4]).std()#1.48
#rcp6.0
np.array([2, 1, 3, 0]).mean()#1.5
np.array([2, 1, 3, 0]).std()#1.12
# rcp8.5
np.array([4, 1, 6, 1]).mean()#3.0
np.array([4, 1, 6, 1]).std()#2.12


#%%%%%%% recognise which GCMS is having more polimictic years 

#[ gfdl, hadgem, ipsl , miroc]
#baseline
np.array([4, 1, 1, 3])

#near-future 
np.array([3, 3, 8, 1])+np.array([2, 0, 5, 2])+np.array([4, 0, 5, 1])
#np.array([ 9,  3, 18,  4])
#distant-future
np.array([2, 3, 6, 4])+np.array([2, 1, 3, 0])+np.array([4, 1, 6, 1])
#np.array([ 8,  5, 15,  5])


#baseline+rcp26+rcp60+rcp85
np.array([21,  9, 34, 12])

#ipsl-> the most polimictic GCM
#gfdl-> the 2nd most polimitic 
#hadgem-> the least polimictic 
#miroc-> the one before the laest one 


#%%Baseline

#%%duration of deoxygenation 

baseline_duration_gfdl
baseline_duration_hadgem
baseline_duration_ipsl
baseline_duration_miroc



# Create a dictionary with the data
data = {
    'year': baseline_duration_gfdl.index,
    'gfdl': baseline_duration_gfdl,
    'hadgem': baseline_duration_hadgem,
    'ipsl': baseline_duration_ipsl,
    'miroc': baseline_duration_miroc,
}

# Convert the dictionary to a DataFrame
df_baseline_duration_4models = pd.DataFrame(data)

# Set the 'year' column as the index
df_baseline_duration_4models.set_index('year', inplace=True)

#####summary

np.mean(df_baseline_duration_4models)
#112.2
np.std(df_baseline_duration_4models.values.flatten())
#15.448624534242523

df_baseline_duration_4models.sum()
"""
gfdl      3519
hadgem    3312
ipsl      3274
miroc     3359
"""
#%%onset of deoxygenation 

# are already defined as DataFrames with a 'start_dates_Jday' column

# Extract the 1-dimensional arrays from each DataFrame column
baseline_onset_gfdl_values = baseline_onset_gfdl['start_dates_Jday'].values.flatten()
baseline_onset_hadgem_values = baseline_onset_hadgem['start_dates_Jday'].values.flatten()
baseline_onset_ipsl_values = baseline_onset_ipsl['start_dates_Jday'].values.flatten()
baseline_onset_miroc_values = baseline_onset_miroc['start_dates_Jday'].values.flatten()

# Extract the index (years)
years = baseline_onset_gfdl.index

# Create the dictionary with 1-dimensional arrays
data = {
    'year': years,
    'gfdl': baseline_onset_gfdl_values,
    'hadgem': baseline_onset_hadgem_values,
    'ipsl': baseline_onset_ipsl_values,
    'miroc': baseline_onset_miroc_values,
}

# Create the DataFrame
df_baseline_onset_4models = pd.DataFrame(data)

# Set the 'year' column as the index
df_baseline_onset_4models.set_index('year', inplace=True)

#####summary

np.mean(df_baseline_onset_4models)
#132.05
np.std(df_baseline_onset_4models.values.flatten())
#10.879529707972981
df_baseline_onset_4models.sum()
"""
gfdl      3852
hadgem    4006
ipsl      4031
miroc     3957
"""

#%%offset of deoxygenation 


baseline_offset_gfdl
baseline_offset_hadgem
baseline_offset_ipsl
baseline_offset_miroc



# Create a dictionary with the data
data = {
    'year': baseline_offset_gfdl.index,
    'gfdl': baseline_offset_gfdl,
    'hadgem': baseline_offset_hadgem,
    'ipsl': baseline_offset_ipsl,
    'miroc': baseline_offset_miroc,
}

# Convert the dictionary to a DataFrame
df_baseline_offset_4models = pd.DataFrame(data)

# Set the 'year' column as the index
df_baseline_offset_4models.set_index('year', inplace=True)

#####summary

np.mean(df_baseline_offset_4models)
#244.25
np.std(df_baseline_offset_4models.values.flatten())
#9.177190928237971

df_baseline_offset_4models.sum()
"""
gfdl      7371
hadgem    7318
ipsl      7305
miroc     7316
"""

#%%near_future 

#%%duration 
#%%rcp26


near_future_duration_gfdl_rcp26
near_future_duration_hadgem_rcp26
near_future_duration_ipsl_rcp26
near_future_duration_miroc_rcp26


data = {
    'year': near_future_duration_gfdl_rcp26.index,
    'gfdl': near_future_duration_gfdl_rcp26,
    'hadgem': near_future_duration_hadgem_rcp26,
    'ipsl': near_future_duration_ipsl_rcp26,
    'miroc': near_future_duration_miroc_rcp26,
}

# Convert the dictionary to a DataFrame
near_future_duration_4models_rcp26= pd.DataFrame(data)

# Set the 'year' column as the index
near_future_duration_4models_rcp26.set_index('year', inplace=True)


#####summary

np.mean(near_future_duration_4models_rcp26)
#125.14166666666667
np.std(near_future_duration_4models_rcp26.values.flatten())
#14.679518516929937

near_future_duration_4models_rcp26.sum()
"""
gfdl      3597
hadgem    3898
ipsl      3659
miroc     3863
"""
#%%rcp60


near_future_duration_gfdl_rcp60
near_future_duration_hadgem_rcp60
near_future_duration_ipsl_rcp60
near_future_duration_miroc_rcp60

data = {
    'year': near_future_duration_gfdl_rcp60.index,
    'gfdl': near_future_duration_gfdl_rcp60,
    'hadgem': near_future_duration_hadgem_rcp60,
    'ipsl': near_future_duration_ipsl_rcp60,
    'miroc': near_future_duration_miroc_rcp60,
}

# Convert the dictionary to a DataFrame
near_future_duration_4models_rcp60= pd.DataFrame(data)

# Set the 'year' column as the index
near_future_duration_4models_rcp60.set_index('year', inplace=True)

#####summary

np.mean(near_future_duration_4models_rcp60)
#123.00833333333334
np.std(near_future_duration_4models_rcp60.values.flatten())
#14.93513521495165

near_future_duration_4models_rcp60.sum()
"""
gfdl      3443
hadgem    3951
ipsl      3718
miroc     3649
"""


#%%rcp85

near_future_duration_gfdl_rcp85
near_future_duration_hadgem_rcp85
near_future_duration_ipsl_rcp85
near_future_duration_miroc_rcp85


data = {
    'year': near_future_duration_gfdl_rcp85.index,
    'gfdl': near_future_duration_gfdl_rcp85,
    'hadgem': near_future_duration_hadgem_rcp85,
    'ipsl': near_future_duration_ipsl_rcp85,
    'miroc': near_future_duration_miroc_rcp85,
}

# Convert the dictionary to a DataFrame
near_future_duration_4models_rcp85= pd.DataFrame(data)

# Set the 'year' column as the index
near_future_duration_4models_rcp85.set_index('year', inplace=True)


#####summary

np.mean(near_future_duration_4models_rcp85)
#125.65
np.std(near_future_duration_4models_rcp85.values.flatten())
#20.350122849752037

near_future_duration_4models_rcp85.sum()
"""
gfdl      2961
hadgem    4135
ipsl      4098
miroc     3884
"""


#%%onset

#%%rcp26


near_future_onset_gfdl_rcp26
near_future_onset_hadgem_rcp26
near_future_onset_ipsl_rcp26
near_future_onset_miroc_rcp26


data = {
    'year': near_future_onset_gfdl_rcp26.index,
    'gfdl': near_future_onset_gfdl_rcp26['start_dates_Jday'],
    'hadgem': near_future_onset_hadgem_rcp26['start_dates_Jday'],
    'ipsl': near_future_onset_ipsl_rcp26['start_dates_Jday'],
    'miroc': near_future_onset_miroc_rcp26['start_dates_Jday'],
}

# Convert the dictionary to a DataFrame
near_future_onset_4models_rcp26= pd.DataFrame(data)

# Set the 'year' column as the index
near_future_onset_4models_rcp26.set_index('year', inplace=True)

#####summary

np.mean(near_future_onset_4models_rcp26)
#122.64166666666667
np.std(near_future_onset_4models_rcp26.values.flatten())
#10.386526395073357


near_future_onset_4models_rcp26.sum()
"""
gfdl      3823
hadgem    3608
ipsl      3673
miroc     3613
"""

#%%rcp60


near_future_onset_gfdl_rcp60
near_future_onset_hadgem_rcp60
near_future_onset_ipsl_rcp60
near_future_onset_miroc_rcp60

data = {
    'year': near_future_onset_gfdl_rcp60.index,
    'gfdl': near_future_onset_gfdl_rcp60['start_dates_Jday'],
    'hadgem': near_future_onset_hadgem_rcp60['start_dates_Jday'],
    'ipsl': near_future_onset_ipsl_rcp60['start_dates_Jday'],
    'miroc': near_future_onset_miroc_rcp60['start_dates_Jday'],
}

# Convert the dictionary to a DataFrame
near_future_onset_4models_rcp60= pd.DataFrame(data)

# Set the 'year' column as the index
near_future_onset_4models_rcp60.set_index('year', inplace=True)



#####summary

np.mean(near_future_onset_4models_rcp60)
#123.74166666666666
np.std(near_future_onset_4models_rcp60.values.flatten())
#9.565995185493712

near_future_onset_4models_rcp60.sum()
"""
gfdl      3769
hadgem    3588
ipsl      3753
miroc     3739
"""
#%%rcp85

near_future_onset_gfdl_rcp85
near_future_onset_hadgem_rcp85
near_future_onset_ipsl_rcp85
near_future_onset_miroc_rcp85


data = {
    'year': near_future_onset_gfdl_rcp85.index,
    'gfdl': near_future_onset_gfdl_rcp85['start_dates_Jday'],
    'hadgem': near_future_onset_hadgem_rcp85['start_dates_Jday'],
    'ipsl': near_future_onset_ipsl_rcp85['start_dates_Jday'],
    'miroc': near_future_onset_miroc_rcp85['start_dates_Jday'],
}

# Convert the dictionary to a DataFrame
near_future_onset_4models_rcp85= pd.DataFrame(data)

# Set the 'year' column as the index
near_future_onset_4models_rcp85.set_index('year', inplace=True)


#####summary

np.mean(near_future_onset_4models_rcp85)
#121.475
np.std(near_future_onset_4models_rcp85.values.flatten())
#11.557077557352754

near_future_onset_4models_rcp85.sum()
"""
gfdl      3905
hadgem    3475
ipsl      3532
miroc     3665
"""

#%%offset

#%%rcp26


near_future_offset_gfdl_rcp26
near_future_offset_hadgem_rcp26
near_future_offset_ipsl_rcp26
near_future_offset_miroc_rcp26


data = {
    'year': near_future_offset_gfdl_rcp26.index,
    'gfdl': near_future_offset_gfdl_rcp26,
    'hadgem': near_future_offset_hadgem_rcp26,
    'ipsl': near_future_offset_ipsl_rcp26,
    'miroc': near_future_offset_miroc_rcp26,
}

# Convert the dictionary to a DataFrame
near_future_offset_4models_rcp26= pd.DataFrame(data)

# Set the 'year' column as the index
near_future_offset_4models_rcp26.set_index('year', inplace=True)


#####summary

np.mean(near_future_offset_4models_rcp26)
#247.78333333333333
np.std(near_future_offset_4models_rcp26.values.flatten())
#10.060801271381033

near_future_offset_4models_rcp26.sum()
"""
gfdl      7420
hadgem    7506
ipsl      7332
miroc     7476
"""
#%%rcp60


near_future_offset_gfdl_rcp60
near_future_offset_hadgem_rcp60
near_future_offset_ipsl_rcp60
near_future_offset_miroc_rcp60

data = {
    'year': near_future_offset_gfdl_rcp60.index,
    'gfdl': near_future_offset_gfdl_rcp60,
    'hadgem': near_future_offset_hadgem_rcp60,
    'ipsl': near_future_offset_ipsl_rcp60,
    'miroc': near_future_offset_miroc_rcp60,
}

# Convert the dictionary to a DataFrame
near_future_offset_4models_rcp60= pd.DataFrame(data)

# Set the 'year' column as the index
near_future_offset_4models_rcp60.set_index('year', inplace=True)


#####summary

np.mean(near_future_offset_4models_rcp60)
#246.75
np.std(near_future_offset_4models_rcp60.values.flatten())
#9.785405799795258

near_future_offset_4models_rcp60.sum()
"""
gfdl      7212
hadgem    7539
ipsl      7471
miroc     7388
"""


#%%rcp85

near_future_offset_gfdl_rcp85
near_future_offset_hadgem_rcp85
near_future_offset_ipsl_rcp85
near_future_offset_miroc_rcp85


data = {
    'year': near_future_offset_gfdl_rcp85.index,
    'gfdl': near_future_offset_gfdl_rcp85,
    'hadgem': near_future_offset_hadgem_rcp85,
    'ipsl': near_future_offset_ipsl_rcp85,
    'miroc': near_future_offset_miroc_rcp85,
}

# Convert the dictionary to a DataFrame
near_future_offset_4models_rcp85= pd.DataFrame(data)

# Set the 'year' column as the index
near_future_offset_4models_rcp85.set_index('year', inplace=True)



#####summary

np.mean(near_future_offset_4models_rcp85)
#247.125
np.std(near_future_offset_4models_rcp85.values.flatten())
#13.325140712202629

near_future_offset_4models_rcp85.sum()
"""
gfdl      6866
hadgem    7610
ipsl      7630
miroc     7549
"""


#%%distant_future 


#%%duration 
#%%rcp26


distant_future_duration_gfdl_rcp26
distant_future_duration_hadgem_rcp26
distant_future_duration_ipsl_rcp26
distant_future_duration_miroc_rcp26


data = {
    'year': distant_future_duration_gfdl_rcp26.index,
    'gfdl': distant_future_duration_gfdl_rcp26,
    'hadgem': distant_future_duration_hadgem_rcp26,
    'ipsl': distant_future_duration_ipsl_rcp26,
    'miroc': distant_future_duration_miroc_rcp26,
}

# Convert the dictionary to a DataFrame
distant_future_duration_4models_rcp26= pd.DataFrame(data)

# Set the 'year' column as the index
distant_future_duration_4models_rcp26.set_index('year', inplace=True)

#####summary

np.mean(distant_future_duration_4models_rcp26)
#127.13333333333334
np.std(distant_future_duration_4models_rcp26.values.flatten())
#13.890604338504817
distant_future_duration_4models_rcp26.sum()
"""
gfdl      3747
hadgem    4006
ipsl      3731
miroc     3772
"""

#%%rcp60


distant_future_duration_gfdl_rcp60
distant_future_duration_hadgem_rcp60
distant_future_duration_ipsl_rcp60
distant_future_duration_miroc_rcp60

data = {
    'year': distant_future_duration_gfdl_rcp60.index,
    'gfdl': distant_future_duration_gfdl_rcp60,
    'hadgem': distant_future_duration_hadgem_rcp60,
    'ipsl': distant_future_duration_ipsl_rcp60,
    'miroc': distant_future_duration_miroc_rcp60,
}

# Convert the dictionary to a DataFrame
distant_future_duration_4models_rcp60= pd.DataFrame(data)

# Set the 'year' column as the index
distant_future_duration_4models_rcp60.set_index('year', inplace=True)


#####summary

np.mean(distant_future_duration_4models_rcp60)
#135.475
np.std(distant_future_duration_4models_rcp60.values.flatten())
#17.710619460274863

distant_future_duration_4models_rcp60.sum()
"""
gfdl      3594
hadgem    4433
ipsl      4158
miroc     4072
"""


#%%rcp85

distant_future_duration_gfdl_rcp85
distant_future_duration_hadgem_rcp85
distant_future_duration_ipsl_rcp85
distant_future_duration_miroc_rcp85


data = {
    'year': distant_future_duration_gfdl_rcp85.index,
    'gfdl': distant_future_duration_gfdl_rcp85,
    'hadgem': distant_future_duration_hadgem_rcp85,
    'ipsl': distant_future_duration_ipsl_rcp85,
    'miroc': distant_future_duration_miroc_rcp85,
}

# Convert the dictionary to a DataFrame
distant_future_duration_4models_rcp85= pd.DataFrame(data)

# Set the 'year' column as the index
distant_future_duration_4models_rcp85.set_index('year', inplace=True)

#####summary

np.mean(distant_future_duration_4models_rcp85)
#143.41666666666666
np.std(distant_future_duration_4models_rcp85.values.flatten())
#20.94500072942361

distant_future_duration_4models_rcp85.sum()
"""
gfdl      3456
hadgem    4783
ipsl      4431
miroc     4540
"""
#%%onset

#%%rcp26


distant_future_onset_gfdl_rcp26
distant_future_onset_hadgem_rcp26
distant_future_onset_ipsl_rcp26
distant_future_onset_miroc_rcp26


data = {
    'year': distant_future_onset_gfdl_rcp26.index,
    'gfdl': distant_future_onset_gfdl_rcp26['start_dates_Jday'],
    'hadgem': distant_future_onset_hadgem_rcp26['start_dates_Jday'],
    'ipsl': distant_future_onset_ipsl_rcp26['start_dates_Jday'],
    'miroc': distant_future_onset_miroc_rcp26['start_dates_Jday'],
}

# Convert the dictionary to a DataFrame
distant_future_onset_4models_rcp26= pd.DataFrame(data)

# Set the 'year' column as the index
distant_future_onset_4models_rcp26.set_index('year', inplace=True)


#####summary

np.mean(distant_future_onset_4models_rcp26)
#121.30833333333334
np.std(distant_future_onset_4models_rcp26.values.flatten())
#9.79353173726868



distant_future_onset_4models_rcp26.sum()
"""
gfdl      3682
hadgem    3516
ipsl      3717
miroc     3642
"""
#%%rcp60


distant_future_onset_gfdl_rcp60
distant_future_onset_hadgem_rcp60
distant_future_onset_ipsl_rcp60
distant_future_onset_miroc_rcp60

data = {
    'year': distant_future_onset_gfdl_rcp60.index,
    'gfdl': distant_future_onset_gfdl_rcp60['start_dates_Jday'],
    'hadgem': distant_future_onset_hadgem_rcp60['start_dates_Jday'],
    'ipsl': distant_future_onset_ipsl_rcp60['start_dates_Jday'],
    'miroc': distant_future_onset_miroc_rcp60['start_dates_Jday'],
}

# Convert the dictionary to a DataFrame
distant_future_onset_4models_rcp60= pd.DataFrame(data)

# Set the 'year' column as the index
distant_future_onset_4models_rcp60.set_index('year', inplace=True)
#####summary

np.mean(distant_future_onset_4models_rcp60)
#117.45
np.std(distant_future_onset_4models_rcp60.values.flatten())
#11.953974234538068

distant_future_onset_4models_rcp60.sum()
"""
gfdl      3726
hadgem    3356
ipsl      3502
miroc     3510
"""

#%%rcp85

distant_future_onset_gfdl_rcp85
distant_future_onset_hadgem_rcp85
distant_future_onset_ipsl_rcp85
distant_future_onset_miroc_rcp85


data = {
    'year': distant_future_onset_gfdl_rcp85.index,
    'gfdl': distant_future_onset_gfdl_rcp85['start_dates_Jday'],
    'hadgem': distant_future_onset_hadgem_rcp85['start_dates_Jday'],
    'ipsl': distant_future_onset_ipsl_rcp85['start_dates_Jday'],
    'miroc': distant_future_onset_miroc_rcp85['start_dates_Jday'],
}

# Convert the dictionary to a DataFrame
distant_future_onset_4models_rcp85= pd.DataFrame(data)

# Set the 'year' column as the index
distant_future_onset_4models_rcp85.set_index('year', inplace=True)



#####summary

np.mean(distant_future_onset_4models_rcp85)
#112.59166666666667
np.std(distant_future_onset_4models_rcp85.values.flatten())
#11.740596118691004

distant_future_onset_4models_rcp85.sum()
"""
gfdl      3687
hadgem    3198
ipsl      3350
miroc     3276
"""
#%%offset

#%%rcp26


distant_future_offset_gfdl_rcp26
distant_future_offset_hadgem_rcp26
distant_future_offset_ipsl_rcp26
distant_future_offset_miroc_rcp26


data = {
    'year': distant_future_offset_gfdl_rcp26.index,
    'gfdl': distant_future_offset_gfdl_rcp26,
    'hadgem': distant_future_offset_hadgem_rcp26,
    'ipsl': distant_future_offset_ipsl_rcp26,
    'miroc': distant_future_offset_miroc_rcp26,
}

# Convert the dictionary to a DataFrame
distant_future_offset_4models_rcp26= pd.DataFrame(data)

# Set the 'year' column as the index
distant_future_offset_4models_rcp26.set_index('year', inplace=True)

#####summary

np.mean(distant_future_offset_4models_rcp26)
#248.44166666666666
np.std(distant_future_offset_4models_rcp26.values.flatten())
#9.221167526704825


distant_future_offset_4models_rcp26.sum()
"""
gfdl      7429
hadgem    7522
ipsl      7448
miroc     7414
"""
#%%rcp60


distant_future_offset_gfdl_rcp60
distant_future_offset_hadgem_rcp60
distant_future_offset_ipsl_rcp60
distant_future_offset_miroc_rcp60

data = {
    'year': distant_future_offset_gfdl_rcp60.index,
    'gfdl': distant_future_offset_gfdl_rcp60,
    'hadgem': distant_future_offset_hadgem_rcp60,
    'ipsl': distant_future_offset_ipsl_rcp60,
    'miroc': distant_future_offset_miroc_rcp60,
}

# Convert the dictionary to a DataFrame
distant_future_offset_4models_rcp60= pd.DataFrame(data)

# Set the 'year' column as the index
distant_future_offset_4models_rcp60.set_index('year', inplace=True)


#####summary

np.mean(distant_future_offset_4models_rcp60)
#252.925
np.std(distant_future_offset_4models_rcp60.values.flatten())
#9.971762214707422

distant_future_offset_4models_rcp60.sum()
"""
gfdl      7320
hadgem    7789
ipsl      7660
miroc     7582
"""




#%%rcp85

distant_future_offset_gfdl_rcp85
distant_future_offset_hadgem_rcp85
distant_future_offset_ipsl_rcp85
distant_future_offset_miroc_rcp85


data = {
    'year': distant_future_offset_gfdl_rcp85.index,
    'gfdl': distant_future_offset_gfdl_rcp85,
    'hadgem': distant_future_offset_hadgem_rcp85,
    'ipsl': distant_future_offset_ipsl_rcp85,
    'miroc': distant_future_offset_miroc_rcp85,
}

# Convert the dictionary to a DataFrame
distant_future_offset_4models_rcp85= pd.DataFrame(data)

# Set the 'year' column as the index
distant_future_offset_4models_rcp85.set_index('year', inplace=True)

#####summary

np.mean(distant_future_offset_4models_rcp85)
#256.0083333333333
np.std(distant_future_offset_4models_rcp85.values.flatten())
#14.085746834615795

distant_future_offset_4models_rcp85.sum()
"""
gfdl      7143
hadgem    7981
ipsl      7781
miroc     7816
"""


#%% temperature average in deep-area during stratification :
#%%baseline

#%%historical (1976-2005)

#gfdl 
temp_hypo_annual_ave_gfdl_his=annual_hypolimnetic_ave(temp_gfdl_his_hypo_TB , hypo_morpho_vriables_gotm_grid[0] , formatted_time_series_gfdl_his)

temp_hypo_annual_ave_gfdl_baseline_1976_2005= temp_hypo_annual_ave_gfdl_his[temp_hypo_annual_ave_gfdl_his.index>1975]

#hadgem 
temp_hypo_annual_ave_hadgem_his=annual_hypolimnetic_ave(temp_hadgem_his_hypo_TB , hypo_morpho_vriables_gotm_grid[0] , formatted_time_series_hadgem_his)

temp_hypo_annual_ave_hadgem_baseline_1976_2005= temp_hypo_annual_ave_hadgem_his[temp_hypo_annual_ave_hadgem_his.index>1975]

#ipsl 
temp_hypo_annual_ave_ipsl_his=annual_hypolimnetic_ave(temp_ipsl_his_hypo_TB , hypo_morpho_vriables_gotm_grid[0] , formatted_time_series_ipsl_his)

temp_hypo_annual_ave_ipsl_baseline_1976_2005= temp_hypo_annual_ave_ipsl_his[temp_hypo_annual_ave_ipsl_his.index>1975]

#miroc 
temp_hypo_annual_ave_miroc_his=annual_hypolimnetic_ave(temp_miroc_his_hypo_TB , hypo_morpho_vriables_gotm_grid[0] , formatted_time_series_miroc_his)

temp_hypo_annual_ave_miroc_baseline_1976_2005= temp_hypo_annual_ave_miroc_his[temp_hypo_annual_ave_miroc_his.index>1975]

    

####dataframe 

data = {
    'year': temp_hypo_annual_ave_gfdl_baseline_1976_2005.index,
    'gfdl': temp_hypo_annual_ave_gfdl_baseline_1976_2005.values.flatten(),
    'hadgem': temp_hypo_annual_ave_hadgem_baseline_1976_2005.values.flatten(),
    'ipsl': temp_hypo_annual_ave_ipsl_baseline_1976_2005.values.flatten(),
    'miroc': temp_hypo_annual_ave_miroc_baseline_1976_2005.values.flatten(),
}

# Convert the dictionary to a DataFrame
temp_hypo_annual_ave_4models_baseline= pd.DataFrame(data)

# Set the 'year' column as the index
temp_hypo_annual_ave_4models_baseline.set_index('year', inplace=True)

#####summary

np.mean(temp_hypo_annual_ave_4models_baseline)
# 5.938343493967671
np.std(temp_hypo_annual_ave_4models_baseline.values.flatten())
# 0.4717783948311

temp_hypo_annual_ave_4models_baseline.mean()
"""
gfdl      5.979582
hadgem    6.001968
ipsl      6.058693
miroc     5.713130
"""



#%% near future 


#%%rcp26
#gfdl_rcp26 
temp_hypo_annual_ave_gfdl_rcp26=annual_hypolimnetic_ave(temp_gfdl_rcp26_hypo_TB , hypo_morpho_vriables_gotm_grid[0] , formatted_time_series_gfdl_rcp26)

temp_hypo_annual_ave_gfdl_rcp26_near_future_2030_2059= temp_hypo_annual_ave_gfdl_rcp26[(temp_hypo_annual_ave_gfdl_rcp26.index>2029)&(temp_hypo_annual_ave_gfdl_rcp26.index<2060)]



#hadgem_rcp26 
temp_hypo_annual_ave_hadgem_rcp26=annual_hypolimnetic_ave(temp_hadgem_rcp26_hypo_TB , hypo_morpho_vriables_gotm_grid[0] , formatted_time_series_hadgem_rcp26)

temp_hypo_annual_ave_hadgem_rcp26_near_future_2030_2059= temp_hypo_annual_ave_hadgem_rcp26[(temp_hypo_annual_ave_hadgem_rcp26.index>2029)&(temp_hypo_annual_ave_hadgem_rcp26.index<2060)]



#ipsl_rcp26 
temp_hypo_annual_ave_ipsl_rcp26=annual_hypolimnetic_ave(temp_ipsl_rcp26_hypo_TB , hypo_morpho_vriables_gotm_grid[0] , formatted_time_series_ipsl_rcp26)

temp_hypo_annual_ave_ipsl_rcp26_near_future_2030_2059= temp_hypo_annual_ave_ipsl_rcp26[(temp_hypo_annual_ave_ipsl_rcp26.index>2029)&(temp_hypo_annual_ave_ipsl_rcp26.index<2060)]



#miroc_rcp26 
temp_hypo_annual_ave_miroc_rcp26=annual_hypolimnetic_ave(temp_miroc_rcp26_hypo_TB , hypo_morpho_vriables_gotm_grid[0] , formatted_time_series_miroc_rcp26)

temp_hypo_annual_ave_miroc_rcp26_near_future_2030_2059= temp_hypo_annual_ave_miroc_rcp26[(temp_hypo_annual_ave_miroc_rcp26.index>2029)&(temp_hypo_annual_ave_miroc_rcp26.index<2060)]




####dataframe 

data = {
    'year': temp_hypo_annual_ave_gfdl_rcp26_near_future_2030_2059.index,
    'gfdl': temp_hypo_annual_ave_gfdl_rcp26_near_future_2030_2059.values.flatten(),
    'hadgem': temp_hypo_annual_ave_hadgem_rcp26_near_future_2030_2059.values.flatten(),
    'ipsl': temp_hypo_annual_ave_ipsl_rcp26_near_future_2030_2059.values.flatten(),
    'miroc': temp_hypo_annual_ave_miroc_rcp26_near_future_2030_2059.values.flatten(),
}

# Convert the dictionary to a DataFrame
temp_hypo_annual_ave_4models_rcp26_near_future_2030_2059= pd.DataFrame(data)

# Set the 'year' column as the index
temp_hypo_annual_ave_4models_rcp26_near_future_2030_2059.set_index('year', inplace=True)

#####summary

np.mean(temp_hypo_annual_ave_4models_rcp26_near_future_2030_2059)
# 6.782319550413255
np.std(temp_hypo_annual_ave_4models_rcp26_near_future_2030_2059.values.flatten())
# 0.6639133717004543

temp_hypo_annual_ave_4models_rcp26_near_future_2030_2059.mean()
"""
gfdl      6.493049
hadgem    6.748865
ipsl      7.411198
miroc     6.476165
"""





#%%rcp60
#gfdl_rcp60 
temp_hypo_annual_ave_gfdl_rcp60=annual_hypolimnetic_ave(temp_gfdl_rcp60_hypo_TB , hypo_morpho_vriables_gotm_grid[0] , formatted_time_series_gfdl_rcp60)

temp_hypo_annual_ave_gfdl_rcp60_near_future_2030_2059= temp_hypo_annual_ave_gfdl_rcp60[(temp_hypo_annual_ave_gfdl_rcp60.index>2029)&(temp_hypo_annual_ave_gfdl_rcp60.index<2060)]



#hadgem_rcp60 
temp_hypo_annual_ave_hadgem_rcp60=annual_hypolimnetic_ave(temp_hadgem_rcp60_hypo_TB , hypo_morpho_vriables_gotm_grid[0] , formatted_time_series_hadgem_rcp60)

temp_hypo_annual_ave_hadgem_rcp60_near_future_2030_2059= temp_hypo_annual_ave_hadgem_rcp60[(temp_hypo_annual_ave_hadgem_rcp60.index>2029)&(temp_hypo_annual_ave_hadgem_rcp60.index<2060)]



#ipsl_rcp60 
temp_hypo_annual_ave_ipsl_rcp60=annual_hypolimnetic_ave(temp_ipsl_rcp60_hypo_TB , hypo_morpho_vriables_gotm_grid[0] , formatted_time_series_ipsl_rcp60)

temp_hypo_annual_ave_ipsl_rcp60_near_future_2030_2059= temp_hypo_annual_ave_ipsl_rcp60[(temp_hypo_annual_ave_ipsl_rcp60.index>2029)&(temp_hypo_annual_ave_ipsl_rcp60.index<2060)]



#miroc_rcp60 
temp_hypo_annual_ave_miroc_rcp60=annual_hypolimnetic_ave(temp_miroc_rcp60_hypo_TB , hypo_morpho_vriables_gotm_grid[0] , formatted_time_series_miroc_rcp60)

temp_hypo_annual_ave_miroc_rcp60_near_future_2030_2059= temp_hypo_annual_ave_miroc_rcp60[(temp_hypo_annual_ave_miroc_rcp60.index>2029)&(temp_hypo_annual_ave_miroc_rcp60.index<2060)]

####dataframe 

data = {
    'year': temp_hypo_annual_ave_gfdl_rcp60_near_future_2030_2059.index,
    'gfdl': temp_hypo_annual_ave_gfdl_rcp60_near_future_2030_2059.values.flatten(),
    'hadgem': temp_hypo_annual_ave_hadgem_rcp60_near_future_2030_2059.values.flatten(),
    'ipsl': temp_hypo_annual_ave_ipsl_rcp60_near_future_2030_2059.values.flatten(),
    'miroc': temp_hypo_annual_ave_miroc_rcp60_near_future_2030_2059.values.flatten(),
}

# Convert the dictionary to a DataFrame
temp_hypo_annual_ave_4models_rcp60_near_future_2030_2059= pd.DataFrame(data)

# Set the 'year' column as the index
temp_hypo_annual_ave_4models_rcp60_near_future_2030_2059.set_index('year', inplace=True)

#####summary

np.mean(temp_hypo_annual_ave_4models_rcp60_near_future_2030_2059)
# 6.84463605517462
np.std(temp_hypo_annual_ave_4models_rcp60_near_future_2030_2059.values.flatten())
#0.6410366013055514

temp_hypo_annual_ave_4models_rcp60_near_future_2030_2059.mean()
"""
gfdl      6.740649
hadgem    6.746365
ipsl      7.356142
miroc     6.535389
"""


#%%rcp85
#gfdl_rcp85 
temp_hypo_annual_ave_gfdl_rcp85=annual_hypolimnetic_ave(temp_gfdl_rcp85_hypo_TB , hypo_morpho_vriables_gotm_grid[0] , formatted_time_series_gfdl_rcp85)

temp_hypo_annual_ave_gfdl_rcp85_near_future_2030_2059= temp_hypo_annual_ave_gfdl_rcp85[(temp_hypo_annual_ave_gfdl_rcp85.index>2029)&(temp_hypo_annual_ave_gfdl_rcp85.index<2060)]



#hadgem_rcp85 
temp_hypo_annual_ave_hadgem_rcp85=annual_hypolimnetic_ave(temp_hadgem_rcp85_hypo_TB , hypo_morpho_vriables_gotm_grid[0] , formatted_time_series_hadgem_rcp85)

temp_hypo_annual_ave_hadgem_rcp85_near_future_2030_2059= temp_hypo_annual_ave_hadgem_rcp85[(temp_hypo_annual_ave_hadgem_rcp85.index>2029)&(temp_hypo_annual_ave_hadgem_rcp85.index<2060)]



#ipsl_rcp85 
temp_hypo_annual_ave_ipsl_rcp85=annual_hypolimnetic_ave(temp_ipsl_rcp85_hypo_TB , hypo_morpho_vriables_gotm_grid[0] , formatted_time_series_ipsl_rcp85)

temp_hypo_annual_ave_ipsl_rcp85_near_future_2030_2059= temp_hypo_annual_ave_ipsl_rcp85[(temp_hypo_annual_ave_ipsl_rcp85.index>2029)&(temp_hypo_annual_ave_ipsl_rcp85.index<2060)]



#miroc_rcp85 
temp_hypo_annual_ave_miroc_rcp85=annual_hypolimnetic_ave(temp_miroc_rcp85_hypo_TB , hypo_morpho_vriables_gotm_grid[0] , formatted_time_series_miroc_rcp85)

temp_hypo_annual_ave_miroc_rcp85_near_future_2030_2059= temp_hypo_annual_ave_miroc_rcp85[(temp_hypo_annual_ave_miroc_rcp85.index>2029)&(temp_hypo_annual_ave_miroc_rcp85.index<2060)]

####dataframe 

data = {
    'year': temp_hypo_annual_ave_gfdl_rcp85_near_future_2030_2059.index,
    'gfdl': temp_hypo_annual_ave_gfdl_rcp85_near_future_2030_2059.values.flatten(),
    'hadgem': temp_hypo_annual_ave_hadgem_rcp85_near_future_2030_2059.values.flatten(),
    'ipsl': temp_hypo_annual_ave_ipsl_rcp85_near_future_2030_2059.values.flatten(),
    'miroc': temp_hypo_annual_ave_miroc_rcp85_near_future_2030_2059.values.flatten(),
}

# Convert the dictionary to a DataFrame
temp_hypo_annual_ave_4models_rcp85_near_future_2030_2059= pd.DataFrame(data)

# Set the 'year' column as the index
temp_hypo_annual_ave_4models_rcp85_near_future_2030_2059.set_index('year', inplace=True)

#####summary

np.mean(temp_hypo_annual_ave_4models_rcp85_near_future_2030_2059)
# 7.165045872347954
np.std(temp_hypo_annual_ave_4models_rcp85_near_future_2030_2059.values.flatten())
# 0.684059555492715

temp_hypo_annual_ave_4models_rcp85_near_future_2030_2059.mean()
"""
gfdl      7.330034
hadgem    6.975514
ipsl      7.548615
miroc     6.806020
"""


#%%distant future
#%%rcp26
#gfdl_rcp26 
temp_hypo_annual_ave_gfdl_rcp26=annual_hypolimnetic_ave(temp_gfdl_rcp26_hypo_TB , hypo_morpho_vriables_gotm_grid[0] , formatted_time_series_gfdl_rcp26)

temp_hypo_annual_ave_gfdl_rcp26_distant_future_2070_2099= temp_hypo_annual_ave_gfdl_rcp26[temp_hypo_annual_ave_gfdl_rcp26.index>2069]



#hadgem_rcp26 
temp_hypo_annual_ave_hadgem_rcp26=annual_hypolimnetic_ave(temp_hadgem_rcp26_hypo_TB , hypo_morpho_vriables_gotm_grid[0] , formatted_time_series_hadgem_rcp26)

temp_hypo_annual_ave_hadgem_rcp26_near_future_2070_2099= temp_hypo_annual_ave_hadgem_rcp26[temp_hypo_annual_ave_hadgem_rcp26.index>2069]



#ipsl_rcp26 
temp_hypo_annual_ave_ipsl_rcp26=annual_hypolimnetic_ave(temp_ipsl_rcp26_hypo_TB , hypo_morpho_vriables_gotm_grid[0] , formatted_time_series_ipsl_rcp26)

temp_hypo_annual_ave_ipsl_rcp26_near_future_2070_2099= temp_hypo_annual_ave_ipsl_rcp26[temp_hypo_annual_ave_ipsl_rcp26.index>2069]



#miroc_rcp26 
temp_hypo_annual_ave_miroc_rcp26=annual_hypolimnetic_ave(temp_miroc_rcp26_hypo_TB , hypo_morpho_vriables_gotm_grid[0] , formatted_time_series_miroc_rcp26)

temp_hypo_annual_ave_miroc_rcp26_near_future_2070_2099= temp_hypo_annual_ave_miroc_rcp26[temp_hypo_annual_ave_miroc_rcp26.index>2069]




####dataframe 

data = {
    'year': temp_hypo_annual_ave_gfdl_rcp26_distant_future_2070_2099.index,
    'gfdl': temp_hypo_annual_ave_gfdl_rcp26_distant_future_2070_2099.values.flatten(),
    'hadgem': temp_hypo_annual_ave_hadgem_rcp26_near_future_2070_2099.values.flatten(),
    'ipsl': temp_hypo_annual_ave_ipsl_rcp26_near_future_2070_2099.values.flatten(),
    'miroc': temp_hypo_annual_ave_miroc_rcp26_near_future_2070_2099.values.flatten(),
}

# Convert the dictionary to a DataFrame
temp_hypo_annual_ave_4models_rcp26_distant_future_2070_2099= pd.DataFrame(data)

# Set the 'year' column as the index
temp_hypo_annual_ave_4models_rcp26_distant_future_2070_2099.set_index('year', inplace=True)

#####summary

np.mean(temp_hypo_annual_ave_4models_rcp26_distant_future_2070_2099)
# 6.759382782502316
np.std(temp_hypo_annual_ave_4models_rcp26_distant_future_2070_2099.values.flatten())
# 0.6201933927541646

temp_hypo_annual_ave_4models_rcp26_distant_future_2070_2099.mean()
"""
gfdl      6.471632
hadgem    6.935295
ipsl      7.005509
miroc     6.625095
"""




#%%rcp60
#gfdl_rcp60 
temp_hypo_annual_ave_gfdl_rcp60=annual_hypolimnetic_ave(temp_gfdl_rcp60_hypo_TB , hypo_morpho_vriables_gotm_grid[0] , formatted_time_series_gfdl_rcp60)

temp_hypo_annual_ave_gfdl_rcp60_distant_future_2070_2099= temp_hypo_annual_ave_gfdl_rcp60[temp_hypo_annual_ave_gfdl_rcp60.index>2069]



#hadgem_rcp60 
temp_hypo_annual_ave_hadgem_rcp60=annual_hypolimnetic_ave(temp_hadgem_rcp60_hypo_TB , hypo_morpho_vriables_gotm_grid[0] , formatted_time_series_hadgem_rcp60)

temp_hypo_annual_ave_hadgem_rcp60_near_future_2070_2099= temp_hypo_annual_ave_hadgem_rcp60[temp_hypo_annual_ave_hadgem_rcp60.index>2069]



#ipsl_rcp60 
temp_hypo_annual_ave_ipsl_rcp60=annual_hypolimnetic_ave(temp_ipsl_rcp60_hypo_TB , hypo_morpho_vriables_gotm_grid[0] , formatted_time_series_ipsl_rcp60)

temp_hypo_annual_ave_ipsl_rcp60_near_future_2070_2099= temp_hypo_annual_ave_ipsl_rcp60[temp_hypo_annual_ave_ipsl_rcp60.index>2069]



#miroc_rcp60 
temp_hypo_annual_ave_miroc_rcp60=annual_hypolimnetic_ave(temp_miroc_rcp60_hypo_TB , hypo_morpho_vriables_gotm_grid[0] , formatted_time_series_miroc_rcp60)

temp_hypo_annual_ave_miroc_rcp60_near_future_2070_2099= temp_hypo_annual_ave_miroc_rcp60[temp_hypo_annual_ave_miroc_rcp60.index>2069]


####dataframe 

data = {
    'year': temp_hypo_annual_ave_gfdl_rcp60_distant_future_2070_2099.index,
    'gfdl': temp_hypo_annual_ave_gfdl_rcp60_distant_future_2070_2099.values.flatten(),
    'hadgem': temp_hypo_annual_ave_hadgem_rcp60_near_future_2070_2099.values.flatten(),
    'ipsl': temp_hypo_annual_ave_ipsl_rcp60_near_future_2070_2099.values.flatten(),
    'miroc': temp_hypo_annual_ave_miroc_rcp60_near_future_2070_2099.values.flatten(),
}

# Convert the dictionary to a DataFrame
temp_hypo_annual_ave_4models_rcp60_distant_future_2070_2099= pd.DataFrame(data)

# Set the 'year' column as the index
temp_hypo_annual_ave_4models_rcp60_distant_future_2070_2099.set_index('year', inplace=True)

#####summary

np.mean(temp_hypo_annual_ave_4models_rcp60_distant_future_2070_2099)
# 7.524594633900989
np.std(temp_hypo_annual_ave_4models_rcp60_distant_future_2070_2099.values.flatten())
# 0.6744258094538468

temp_hypo_annual_ave_4models_rcp60_distant_future_2070_2099.mean()
"""
gfdl      7.482381
hadgem    7.652377
ipsl      7.893799
miroc     7.069822
"""


#%%rcp85
#gfdl_rcp85 
temp_hypo_annual_ave_gfdl_rcp85=annual_hypolimnetic_ave(temp_gfdl_rcp85_hypo_TB , hypo_morpho_vriables_gotm_grid[0] , formatted_time_series_gfdl_rcp85)

temp_hypo_annual_ave_gfdl_rcp85_distant_future_2070_2099= temp_hypo_annual_ave_gfdl_rcp85[temp_hypo_annual_ave_gfdl_rcp85.index>2069]



#hadgem_rcp85 
temp_hypo_annual_ave_hadgem_rcp85=annual_hypolimnetic_ave(temp_hadgem_rcp85_hypo_TB , hypo_morpho_vriables_gotm_grid[0] , formatted_time_series_hadgem_rcp85)

temp_hypo_annual_ave_hadgem_rcp85_near_future_2070_2099= temp_hypo_annual_ave_hadgem_rcp85[temp_hypo_annual_ave_hadgem_rcp85.index>2069]



#ipsl_rcp85 
temp_hypo_annual_ave_ipsl_rcp85=annual_hypolimnetic_ave(temp_ipsl_rcp85_hypo_TB , hypo_morpho_vriables_gotm_grid[0] , formatted_time_series_ipsl_rcp85)

temp_hypo_annual_ave_ipsl_rcp85_near_future_2070_2099= temp_hypo_annual_ave_ipsl_rcp85[temp_hypo_annual_ave_ipsl_rcp85.index>2069]



#miroc_rcp85 
temp_hypo_annual_ave_miroc_rcp85=annual_hypolimnetic_ave(temp_miroc_rcp85_hypo_TB , hypo_morpho_vriables_gotm_grid[0] , formatted_time_series_miroc_rcp85)

temp_hypo_annual_ave_miroc_rcp85_near_future_2070_2099= temp_hypo_annual_ave_miroc_rcp85[temp_hypo_annual_ave_miroc_rcp85.index>2069]


####dataframe 

data = {
    'year': temp_hypo_annual_ave_gfdl_rcp85_distant_future_2070_2099.index,
    'gfdl': temp_hypo_annual_ave_gfdl_rcp85_distant_future_2070_2099.values.flatten(),
    'hadgem': temp_hypo_annual_ave_hadgem_rcp85_near_future_2070_2099.values.flatten(),
    'ipsl': temp_hypo_annual_ave_ipsl_rcp85_near_future_2070_2099.values.flatten(),
    'miroc': temp_hypo_annual_ave_miroc_rcp85_near_future_2070_2099.values.flatten(),
}

# Convert the dictionary to a DataFrame
temp_hypo_annual_ave_4models_rcp85_distant_future_2070_2099= pd.DataFrame(data)

# Set the 'year' column as the index
temp_hypo_annual_ave_4models_rcp85_distant_future_2070_2099.set_index('year', inplace=True)

#####summary

np.mean(temp_hypo_annual_ave_4models_rcp85_distant_future_2070_2099)
# 8.430552124958213
np.std(temp_hypo_annual_ave_4models_rcp85_distant_future_2070_2099.values.flatten())
#  1.0835092506373682

temp_hypo_annual_ave_4models_rcp85_distant_future_2070_2099.mean()
"""
gfdl      8.085823
hadgem    8.379551
ipsl      9.625117
miroc     7.631717
"""
