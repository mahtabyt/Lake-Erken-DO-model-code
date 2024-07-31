# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 16:54:58 2023

@author: mahta
"""



#%% Jday of first & last & length of full hypoxic condition 
#%%his


# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/his'
all_first_jday_hypoxic_full_prof_inyear_his= pd.DataFrame([])
all_last_jday_hypoxic_full_prof_inyear_his= pd.DataFrame([])
all_len_hypoxic_full_prof_inyear_his= pd.DataFrame([])
all_weights_his= np.array([])



# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_gfdl_his_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights_his= np.append(all_weights_his , weights) 
        
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr = hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        
        first_jday_hypoxic_full_prof_inyear_his=first_last_len_anoxic_prof_inyear  (C, Vr, time_series, threshold=2)[1]
        last_jday_hypoxic_full_prof_inyear_his=first_last_len_anoxic_prof_inyear  (C, Vr, time_series, threshold=2)[3]
        len_hypoxic_full_prof_inyear_his=first_last_len_anoxic_prof_inyear  (C, Vr, time_series, threshold=2)[4]
        

        all_first_jday_hypoxic_full_prof_inyear_his = pd.concat([all_first_jday_hypoxic_full_prof_inyear_his , first_jday_hypoxic_full_prof_inyear_his], axis=1)
        all_last_jday_hypoxic_full_prof_inyear_his = pd.concat([all_last_jday_hypoxic_full_prof_inyear_his , last_jday_hypoxic_full_prof_inyear_his], axis=1)
        all_len_hypoxic_full_prof_inyear_his = pd.concat([all_len_hypoxic_full_prof_inyear_his , len_hypoxic_full_prof_inyear_his], axis=1)



# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/his'




# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_hadgem_his_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights_his= np.append(all_weights_his , weights) 
        
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr = hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        
        first_jday_hypoxic_full_prof_inyear_his=first_last_len_anoxic_prof_inyear  (C, Vr, time_series, threshold=2)[1]
        last_jday_hypoxic_full_prof_inyear_his=first_last_len_anoxic_prof_inyear  (C, Vr, time_series, threshold=2)[3]
        len_hypoxic_full_prof_inyear_his=first_last_len_anoxic_prof_inyear  (C, Vr, time_series, threshold=2)[4]
        

        all_first_jday_hypoxic_full_prof_inyear_his = pd.concat([all_first_jday_hypoxic_full_prof_inyear_his , first_jday_hypoxic_full_prof_inyear_his], axis=1)
        all_last_jday_hypoxic_full_prof_inyear_his = pd.concat([all_last_jday_hypoxic_full_prof_inyear_his , last_jday_hypoxic_full_prof_inyear_his], axis=1)
        all_len_hypoxic_full_prof_inyear_his = pd.concat([all_len_hypoxic_full_prof_inyear_his , len_hypoxic_full_prof_inyear_his], axis=1)


# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/his'




# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_ipsl_his_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights_his= np.append(all_weights_his , weights) 
        
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr = hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        
        first_jday_hypoxic_full_prof_inyear_his=first_last_len_anoxic_prof_inyear  (C, Vr, time_series, threshold=2)[1]
        last_jday_hypoxic_full_prof_inyear_his=first_last_len_anoxic_prof_inyear  (C, Vr, time_series, threshold=2)[3]
        len_hypoxic_full_prof_inyear_his=first_last_len_anoxic_prof_inyear  (C, Vr, time_series, threshold=2)[4]
        

        all_first_jday_hypoxic_full_prof_inyear_his = pd.concat([all_first_jday_hypoxic_full_prof_inyear_his , first_jday_hypoxic_full_prof_inyear_his], axis=1)
        all_last_jday_hypoxic_full_prof_inyear_his = pd.concat([all_last_jday_hypoxic_full_prof_inyear_his , last_jday_hypoxic_full_prof_inyear_his], axis=1)
        all_len_hypoxic_full_prof_inyear_his = pd.concat([all_len_hypoxic_full_prof_inyear_his , len_hypoxic_full_prof_inyear_his], axis=1)


# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/his'




# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_miroc_his_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights_his= np.append(all_weights_his , weights) 
        
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr = hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        
        first_jday_hypoxic_full_prof_inyear_his=first_last_len_anoxic_prof_inyear  (C, Vr, time_series, threshold=2)[1]
        last_jday_hypoxic_full_prof_inyear_his=first_last_len_anoxic_prof_inyear  (C, Vr, time_series, threshold=2)[3]
        len_hypoxic_full_prof_inyear_his=first_last_len_anoxic_prof_inyear  (C, Vr, time_series, threshold=2)[4]
        

        all_first_jday_hypoxic_full_prof_inyear_his = pd.concat([all_first_jday_hypoxic_full_prof_inyear_his , first_jday_hypoxic_full_prof_inyear_his], axis=1)
        all_last_jday_hypoxic_full_prof_inyear_his = pd.concat([all_last_jday_hypoxic_full_prof_inyear_his , last_jday_hypoxic_full_prof_inyear_his], axis=1)
        all_len_hypoxic_full_prof_inyear_his = pd.concat([all_len_hypoxic_full_prof_inyear_his , len_hypoxic_full_prof_inyear_his], axis=1)

#%%annova_uncertainity_his 

all_first_jday_hypoxic_full_prof_inyear_his=all_first_jday_hypoxic_full_prof_inyear_his.replace(0, np.nan)

anova_first_jday_hypoxic_full_prof_his=annova_uncertainity(all_first_jday_hypoxic_full_prof_inyear_his)

anova_first_jday_hypoxic_full_prof_his.describe().loc['mean', :]
"""
GCMs             65.238665
param            32.965235
interaction       1.796100
GCMs/param        4.852386
year           1933.000000
"""

anova_first_jday_hypoxic_full_prof_his.describe().loc['std', :]
"""
GCMs           20.781685
param          20.749682
interaction     2.542161
GCMs/param     11.209417
year           42.001984

"""

all_last_jday_hypoxic_full_prof_inyear_his=all_last_jday_hypoxic_full_prof_inyear_his.replace(0, np.nan)

anova_last_jday_hypoxic_full_prof_his=annova_uncertainity(all_last_jday_hypoxic_full_prof_inyear_his)

anova_last_jday_hypoxic_full_prof_his.describe().loc['mean', :]
"""
GCMs            100.000000
param             0.379772
interaction      -0.379772
GCMs/param             inf
year           1933.000000
"""


anova_last_jday_hypoxic_full_prof_his.describe().loc['std', :]

"""
GCMs           9.096304e-15
param          1.875678e+00
interaction    1.875678e+00
GCMs/param              NaN
year           4.200198e+01
"""



anova_len_jday_hypoxic_full_prof_his=annova_uncertainity(all_len_hypoxic_full_prof_inyear_his)

anova_len_jday_hypoxic_full_prof_his.describe().loc['mean', :]
"""
GCMs             73.192191
param            25.657073
interaction       1.150735
GCMs/param        6.550131
year           1933.000000
Name: mean, dtype: float64
"""


anova_len_jday_hypoxic_full_prof_his.describe().loc['std', :]
"""
GCMs           18.387243
param          17.755574
interaction     1.281733
GCMs/param      8.558604
year           42.001984
Name: std, dtype: float64
"""


#%%rcp26


# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp26'
all_first_jday_hypoxic_full_prof_inyear_rcp26= pd.DataFrame([])
all_last_jday_hypoxic_full_prof_inyear_rcp26= pd.DataFrame([])
all_len_hypoxic_full_prof_inyear_rcp26= pd.DataFrame([])
all_weights_rcp26= np.array([])



# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_gfdl_rcp26_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights_rcp26= np.append(all_weights_rcp26 , weights) 
        
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr = hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        
        first_jday_hypoxic_full_prof_inyear_rcp26=first_last_len_anoxic_prof_inyear  (C, Vr, time_series, threshold=2)[1]
        last_jday_hypoxic_full_prof_inyear_rcp26=first_last_len_anoxic_prof_inyear  (C, Vr, time_series, threshold=2)[3]
        len_hypoxic_full_prof_inyear_rcp26=first_last_len_anoxic_prof_inyear  (C, Vr, time_series, threshold=2)[4]
        

        all_first_jday_hypoxic_full_prof_inyear_rcp26 = pd.concat([all_first_jday_hypoxic_full_prof_inyear_rcp26 , first_jday_hypoxic_full_prof_inyear_rcp26], axis=1)
        all_last_jday_hypoxic_full_prof_inyear_rcp26 = pd.concat([all_last_jday_hypoxic_full_prof_inyear_rcp26 , last_jday_hypoxic_full_prof_inyear_rcp26], axis=1)
        all_len_hypoxic_full_prof_inyear_rcp26 = pd.concat([all_len_hypoxic_full_prof_inyear_rcp26 , len_hypoxic_full_prof_inyear_rcp26], axis=1)


# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp26'




# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_hadgem_rcp26_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights_rcp26= np.append(all_weights_rcp26 , weights) 
        
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr = hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        
        first_jday_hypoxic_full_prof_inyear_rcp26=first_last_len_anoxic_prof_inyear  (C, Vr, time_series, threshold=2)[1]
        last_jday_hypoxic_full_prof_inyear_rcp26=first_last_len_anoxic_prof_inyear  (C, Vr, time_series, threshold=2)[3]
        len_hypoxic_full_prof_inyear_rcp26=first_last_len_anoxic_prof_inyear  (C, Vr, time_series, threshold=2)[4]
        

        all_first_jday_hypoxic_full_prof_inyear_rcp26 = pd.concat([all_first_jday_hypoxic_full_prof_inyear_rcp26 , first_jday_hypoxic_full_prof_inyear_rcp26], axis=1)
        all_last_jday_hypoxic_full_prof_inyear_rcp26 = pd.concat([all_last_jday_hypoxic_full_prof_inyear_rcp26 , last_jday_hypoxic_full_prof_inyear_rcp26], axis=1)
        all_len_hypoxic_full_prof_inyear_rcp26 = pd.concat([all_len_hypoxic_full_prof_inyear_rcp26 , len_hypoxic_full_prof_inyear_rcp26], axis=1)


# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp26'




# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_ipsl_rcp26_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights_rcp26= np.append(all_weights_rcp26 , weights) 
        
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr = hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        
        first_jday_hypoxic_full_prof_inyear_rcp26=first_last_len_anoxic_prof_inyear  (C, Vr, time_series, threshold=2)[1]
        last_jday_hypoxic_full_prof_inyear_rcp26=first_last_len_anoxic_prof_inyear  (C, Vr, time_series, threshold=2)[3]
        len_hypoxic_full_prof_inyear_rcp26=first_last_len_anoxic_prof_inyear  (C, Vr, time_series, threshold=2)[4]
        

        all_first_jday_hypoxic_full_prof_inyear_rcp26 = pd.concat([all_first_jday_hypoxic_full_prof_inyear_rcp26 , first_jday_hypoxic_full_prof_inyear_rcp26], axis=1)
        all_last_jday_hypoxic_full_prof_inyear_rcp26 = pd.concat([all_last_jday_hypoxic_full_prof_inyear_rcp26 , last_jday_hypoxic_full_prof_inyear_rcp26], axis=1)
        all_len_hypoxic_full_prof_inyear_rcp26 = pd.concat([all_len_hypoxic_full_prof_inyear_rcp26 , len_hypoxic_full_prof_inyear_rcp26], axis=1)


# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp26'




# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_miroc_rcp26_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights_rcp26= np.append(all_weights_rcp26 , weights) 
        
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr = hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        
        first_jday_hypoxic_full_prof_inyear_rcp26=first_last_len_anoxic_prof_inyear  (C, Vr, time_series, threshold=2)[1]
        last_jday_hypoxic_full_prof_inyear_rcp26=first_last_len_anoxic_prof_inyear  (C, Vr, time_series, threshold=2)[3]
        len_hypoxic_full_prof_inyear_rcp26=first_last_len_anoxic_prof_inyear  (C, Vr, time_series, threshold=2)[4]
        

        all_first_jday_hypoxic_full_prof_inyear_rcp26 = pd.concat([all_first_jday_hypoxic_full_prof_inyear_rcp26 , first_jday_hypoxic_full_prof_inyear_rcp26], axis=1)
        all_last_jday_hypoxic_full_prof_inyear_rcp26 = pd.concat([all_last_jday_hypoxic_full_prof_inyear_rcp26 , last_jday_hypoxic_full_prof_inyear_rcp26], axis=1)
        all_len_hypoxic_full_prof_inyear_rcp26 = pd.concat([all_len_hypoxic_full_prof_inyear_rcp26 , len_hypoxic_full_prof_inyear_rcp26], axis=1)

#%%annova_uncertainity_rcp26 

all_first_jday_hypoxic_full_prof_inyear_rcp26=all_first_jday_hypoxic_full_prof_inyear_rcp26.replace(0, np.nan)

anova_first_jday_hypoxic_full_prof_rcp26=annova_uncertainity(all_first_jday_hypoxic_full_prof_inyear_rcp26)

anova_first_jday_hypoxic_full_prof_rcp26.describe().loc['mean', :]
"""
GCMs             64.475545
param            34.359969
interaction       1.164485
GCMs/param        3.102160
year           2052.500000
"""

anova_first_jday_hypoxic_full_prof_rcp26.describe().loc['std', :]
"""
GCMs           19.609068
param          19.422421
interaction     1.287641
GCMs/param      3.620822
year           27.279418

"""


all_last_jday_hypoxic_full_prof_inyear_rcp26=all_last_jday_hypoxic_full_prof_inyear_rcp26.replace(0,np.nan)

anova_last_jday_hypoxic_full_prof_rcp26=annova_uncertainity(all_last_jday_hypoxic_full_prof_inyear_rcp26)

anova_last_jday_hypoxic_full_prof_rcp26.describe().loc['mean', :]
"""
GCMs            100.000000
param             0.040627
interaction      -0.040627
GCMs/param             inf
year           2052.500000
Name: mean, dtype: float64
"""


anova_last_jday_hypoxic_full_prof_rcp26.describe().loc['std', :]

"""
GCMs           4.420791e-15
param          3.938941e-01
interaction    3.938941e-01
GCMs/param              NaN
year           2.727942e+01
"""



anova_len_jday_hypoxic_full_prof_rcp26=annova_uncertainity(all_len_hypoxic_full_prof_inyear_rcp26)

anova_len_jday_hypoxic_full_prof_rcp26.describe().loc['mean', :]
"""
GCMs             69.986714
param            29.005878
interaction       1.007408
GCMs/param        4.169585
year           2052.500000
Name: mean, dtype: float64
"""


anova_len_jday_hypoxic_full_prof_rcp26.describe().loc['std', :]
"""
GCMs           19.031482
param          18.493748
interaction     1.182283
GCMs/param      4.193236
year           27.279418
Name: std, dtype: float64
"""
#%%annova_uncertainity_rcp26_80years

all_first_jday_hypoxic_full_prof_inyear_rcp26=all_first_jday_hypoxic_full_prof_inyear_rcp26.replace(0, np.nan)

anova_first_jday_hypoxic_full_prof_rcp26_80years=annova_uncertainity(all_first_jday_hypoxic_full_prof_inyear_rcp26[all_first_jday_hypoxic_full_prof_inyear_rcp26.index>2019])

anova_first_jday_hypoxic_full_prof_rcp26_80years.describe().loc['mean', :]
"""
GCMs             66.045297
param            32.764523
interaction       1.190180
GCMs/param        3.265675
year           2059.500000
Name: mean, dtype: float64
"""

anova_first_jday_hypoxic_full_prof_rcp26_80years.describe().loc['std', :]
"""
GCMs           18.636147
param          18.430659
interaction     1.372822
GCMs/param      3.794946
year           23.237900
Name: std, dtype: float64
"""




anova_len_jday_hypoxic_full_prof_rcp26_80years=annova_uncertainity(all_len_hypoxic_full_prof_inyear_rcp26[all_len_hypoxic_full_prof_inyear_rcp26.index>2019])

anova_len_jday_hypoxic_full_prof_rcp26_80years.describe().loc['mean', :]
"""
GCMs             71.563156
param            27.456088
interaction       0.980757
GCMs/param        4.435850
year           2059.500000
Name: mean, dtype: float64
"""


anova_len_jday_hypoxic_full_prof_rcp26_80years.describe().loc['std', :]
"""
GCMs           17.785242
param          17.362640
interaction     1.165083
GCMs/param      4.401791
year           23.237900
Name: std, dtype: float64
"""








#%%rcp60


# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp60'
all_first_jday_hypoxic_full_prof_inyear_rcp60= pd.DataFrame([])
all_last_jday_hypoxic_full_prof_inyear_rcp60= pd.DataFrame([])
all_len_hypoxic_full_prof_inyear_rcp60= pd.DataFrame([])
all_weights_rcp60= np.array([])



# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_gfdl_rcp60_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights_rcp60= np.append(all_weights_rcp60 , weights) 
        
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr = hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        
        first_jday_hypoxic_full_prof_inyear_rcp60=first_last_len_anoxic_prof_inyear  (C, Vr, time_series, threshold=2)[1]
        last_jday_hypoxic_full_prof_inyear_rcp60=first_last_len_anoxic_prof_inyear  (C, Vr, time_series, threshold=2)[3]
        len_hypoxic_full_prof_inyear_rcp60=first_last_len_anoxic_prof_inyear  (C, Vr, time_series, threshold=2)[4]
        

        all_first_jday_hypoxic_full_prof_inyear_rcp60 = pd.concat([all_first_jday_hypoxic_full_prof_inyear_rcp60 , first_jday_hypoxic_full_prof_inyear_rcp60], axis=1)
        all_last_jday_hypoxic_full_prof_inyear_rcp60 = pd.concat([all_last_jday_hypoxic_full_prof_inyear_rcp60 , last_jday_hypoxic_full_prof_inyear_rcp60], axis=1)
        all_len_hypoxic_full_prof_inyear_rcp60 = pd.concat([all_len_hypoxic_full_prof_inyear_rcp60 , len_hypoxic_full_prof_inyear_rcp60], axis=1)


# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp60'




# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_hadgem_rcp60_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights_rcp60= np.append(all_weights_rcp60 , weights) 
        
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr = hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        
        first_jday_hypoxic_full_prof_inyear_rcp60=first_last_len_anoxic_prof_inyear  (C, Vr, time_series, threshold=2)[1]
        last_jday_hypoxic_full_prof_inyear_rcp60=first_last_len_anoxic_prof_inyear  (C, Vr, time_series, threshold=2)[3]
        len_hypoxic_full_prof_inyear_rcp60=first_last_len_anoxic_prof_inyear  (C, Vr, time_series, threshold=2)[4]
        

        all_first_jday_hypoxic_full_prof_inyear_rcp60 = pd.concat([all_first_jday_hypoxic_full_prof_inyear_rcp60 , first_jday_hypoxic_full_prof_inyear_rcp60], axis=1)
        all_last_jday_hypoxic_full_prof_inyear_rcp60 = pd.concat([all_last_jday_hypoxic_full_prof_inyear_rcp60 , last_jday_hypoxic_full_prof_inyear_rcp60], axis=1)
        all_len_hypoxic_full_prof_inyear_rcp60 = pd.concat([all_len_hypoxic_full_prof_inyear_rcp60 , len_hypoxic_full_prof_inyear_rcp60], axis=1)


# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp60'




# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_ipsl_rcp60_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights_rcp60= np.append(all_weights_rcp60 , weights) 
        
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr = hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        
        first_jday_hypoxic_full_prof_inyear_rcp60=first_last_len_anoxic_prof_inyear  (C, Vr, time_series, threshold=2)[1]
        last_jday_hypoxic_full_prof_inyear_rcp60=first_last_len_anoxic_prof_inyear  (C, Vr, time_series, threshold=2)[3]
        len_hypoxic_full_prof_inyear_rcp60=first_last_len_anoxic_prof_inyear  (C, Vr, time_series, threshold=2)[4]
        

        all_first_jday_hypoxic_full_prof_inyear_rcp60 = pd.concat([all_first_jday_hypoxic_full_prof_inyear_rcp60 , first_jday_hypoxic_full_prof_inyear_rcp60], axis=1)
        all_last_jday_hypoxic_full_prof_inyear_rcp60 = pd.concat([all_last_jday_hypoxic_full_prof_inyear_rcp60 , last_jday_hypoxic_full_prof_inyear_rcp60], axis=1)
        all_len_hypoxic_full_prof_inyear_rcp60 = pd.concat([all_len_hypoxic_full_prof_inyear_rcp60 , len_hypoxic_full_prof_inyear_rcp60], axis=1)


# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp60'




# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_miroc_rcp60_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights_rcp60= np.append(all_weights_rcp60 , weights) 
        
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr = hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        
        first_jday_hypoxic_full_prof_inyear_rcp60=first_last_len_anoxic_prof_inyear  (C, Vr, time_series, threshold=2)[1]
        last_jday_hypoxic_full_prof_inyear_rcp60=first_last_len_anoxic_prof_inyear  (C, Vr, time_series, threshold=2)[3]
        len_hypoxic_full_prof_inyear_rcp60=first_last_len_anoxic_prof_inyear  (C, Vr, time_series, threshold=2)[4]
        

        all_first_jday_hypoxic_full_prof_inyear_rcp60 = pd.concat([all_first_jday_hypoxic_full_prof_inyear_rcp60 , first_jday_hypoxic_full_prof_inyear_rcp60], axis=1)
        all_last_jday_hypoxic_full_prof_inyear_rcp60 = pd.concat([all_last_jday_hypoxic_full_prof_inyear_rcp60 , last_jday_hypoxic_full_prof_inyear_rcp60], axis=1)
        all_len_hypoxic_full_prof_inyear_rcp60 = pd.concat([all_len_hypoxic_full_prof_inyear_rcp60 , len_hypoxic_full_prof_inyear_rcp60], axis=1)


#%%annova_uncertainity_rcp60 

all_first_jday_hypoxic_full_prof_inyear_rcp60=all_first_jday_hypoxic_full_prof_inyear_rcp60.replace(0, np.nan)

anova_first_jday_hypoxic_full_prof_rcp60=annova_uncertainity(all_first_jday_hypoxic_full_prof_inyear_rcp60)

anova_first_jday_hypoxic_full_prof_rcp60.describe().loc['mean', :]
"""
GCMs             62.626283
param            35.921739
interaction       1.451978
GCMs/param        2.969479
year           2052.500000
"""

anova_first_jday_hypoxic_full_prof_rcp60.describe().loc['std', :]
"""
GCMs           22.273370
param          21.234813
interaction     2.479710
GCMs/param      2.842311
year           27.279418
"""

all_last_jday_hypoxic_full_prof_inyear_rcp60=all_last_jday_hypoxic_full_prof_inyear_rcp60.replace(0, np.nan)

anova_last_jday_hypoxic_full_prof_rcp60=annova_uncertainity(all_last_jday_hypoxic_full_prof_inyear_rcp60)

anova_last_jday_hypoxic_full_prof_rcp60.describe().loc['mean', :]
"""
GCMs            100.0
param             0.0
interaction       0.0
GCMs/param        inf
year           2052.5

"""


anova_last_jday_hypoxic_full_prof_rcp60.describe().loc['std', :]

"""
GCMs            0.000000
param           0.000000
interaction     0.000000
GCMs/param           NaN
year           27.279418
Name: std, dtype: float64
"""



anova_len_jday_hypoxic_full_prof_rcp60=annova_uncertainity(all_len_hypoxic_full_prof_inyear_rcp60)

anova_len_jday_hypoxic_full_prof_rcp60.describe().loc['mean', :]
"""
GCMs             74.531978
param            24.435957
interaction       1.032065
GCMs/param        6.115543
year           2052.500000
Name: mean, dtype: float64
"""


anova_len_jday_hypoxic_full_prof_rcp60.describe().loc['std', :]
"""
GCMs           18.813962
param          18.066942
interaction     1.298195
GCMs/param      6.761448
year           27.279418
Name: std, dtype: float64
"""

#%%annova_uncertainity_rcp60_80years

all_first_jday_hypoxic_full_prof_inyear_rcp60=all_first_jday_hypoxic_full_prof_inyear_rcp60.replace(0, np.nan)

anova_first_jday_hypoxic_full_prof_rcp60_80years=annova_uncertainity(all_first_jday_hypoxic_full_prof_inyear_rcp60[all_first_jday_hypoxic_full_prof_inyear_rcp60.index>2019])

anova_first_jday_hypoxic_full_prof_rcp60_80years.describe().loc['mean', :]
"""
GCMs             62.362088
param            36.089686
interaction       1.548227
GCMs/param        2.931737
year           2059.500000
Name: mean, dtype: float64
"""

anova_first_jday_hypoxic_full_prof_rcp60_80years.describe().loc['std', :]
"""
GCMs           22.508587
param          21.328501
interaction     2.669223
GCMs/param      2.844658
year           23.237900
Name: std, dtype: float64

"""




anova_len_jday_hypoxic_full_prof_rcp60_80years=annova_uncertainity(all_len_hypoxic_full_prof_inyear_rcp60[all_len_hypoxic_full_prof_inyear_rcp60.index>2019])

anova_len_jday_hypoxic_full_prof_rcp60_80years.describe().loc['mean', :]
"""
GCMs             74.543990
param            24.392898
interaction       1.063112
GCMs/param        5.809925
year           2059.500000
Name: mean, dtype: float64
"""


anova_len_jday_hypoxic_full_prof_rcp60_80years.describe().loc['std', :]
"""
GCMs           19.215970
param          18.427814
interaction     1.374825
GCMs/param      5.797550
year           23.237900
Name: std, dtype: float64
"""



#%%rcp85


# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp85'
all_first_jday_hypoxic_full_prof_inyear_rcp85= pd.DataFrame([])
all_last_jday_hypoxic_full_prof_inyear_rcp85= pd.DataFrame([])
all_len_hypoxic_full_prof_inyear_rcp85= pd.DataFrame([])
all_weights_rcp85= np.array([])



# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_gfdl_rcp85_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights_rcp85= np.append(all_weights_rcp85 , weights) 
        
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr = hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        
        first_jday_hypoxic_full_prof_inyear_rcp85=first_last_len_anoxic_prof_inyear  (C, Vr, time_series, threshold=2)[1]
        last_jday_hypoxic_full_prof_inyear_rcp85=first_last_len_anoxic_prof_inyear  (C, Vr, time_series, threshold=2)[3]
        len_hypoxic_full_prof_inyear_rcp85=first_last_len_anoxic_prof_inyear  (C, Vr, time_series, threshold=2)[4]
        

        all_first_jday_hypoxic_full_prof_inyear_rcp85 = pd.concat([all_first_jday_hypoxic_full_prof_inyear_rcp85 , first_jday_hypoxic_full_prof_inyear_rcp85], axis=1)
        all_last_jday_hypoxic_full_prof_inyear_rcp85 = pd.concat([all_last_jday_hypoxic_full_prof_inyear_rcp85 , last_jday_hypoxic_full_prof_inyear_rcp85], axis=1)
        all_len_hypoxic_full_prof_inyear_rcp85 = pd.concat([all_len_hypoxic_full_prof_inyear_rcp85 , len_hypoxic_full_prof_inyear_rcp85], axis=1)


# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp85'




# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_hadgem_rcp85_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights_rcp85= np.append(all_weights_rcp85 , weights) 
        
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr = hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        
        first_jday_hypoxic_full_prof_inyear_rcp85=first_last_len_anoxic_prof_inyear  (C, Vr, time_series, threshold=2)[1]
        last_jday_hypoxic_full_prof_inyear_rcp85=first_last_len_anoxic_prof_inyear  (C, Vr, time_series, threshold=2)[3]
        len_hypoxic_full_prof_inyear_rcp85=first_last_len_anoxic_prof_inyear  (C, Vr, time_series, threshold=2)[4]
        

        all_first_jday_hypoxic_full_prof_inyear_rcp85 = pd.concat([all_first_jday_hypoxic_full_prof_inyear_rcp85 , first_jday_hypoxic_full_prof_inyear_rcp85], axis=1)
        all_last_jday_hypoxic_full_prof_inyear_rcp85 = pd.concat([all_last_jday_hypoxic_full_prof_inyear_rcp85 , last_jday_hypoxic_full_prof_inyear_rcp85], axis=1)
        all_len_hypoxic_full_prof_inyear_rcp85 = pd.concat([all_len_hypoxic_full_prof_inyear_rcp85 , len_hypoxic_full_prof_inyear_rcp85], axis=1)


# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp85'




# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_ipsl_rcp85_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights_rcp85= np.append(all_weights_rcp85 , weights) 
        
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr = hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        
        first_jday_hypoxic_full_prof_inyear_rcp85=first_last_len_anoxic_prof_inyear  (C, Vr, time_series, threshold=2)[1]
        last_jday_hypoxic_full_prof_inyear_rcp85=first_last_len_anoxic_prof_inyear  (C, Vr, time_series, threshold=2)[3]
        len_hypoxic_full_prof_inyear_rcp85=first_last_len_anoxic_prof_inyear  (C, Vr, time_series, threshold=2)[4]
        

        all_first_jday_hypoxic_full_prof_inyear_rcp85 = pd.concat([all_first_jday_hypoxic_full_prof_inyear_rcp85 , first_jday_hypoxic_full_prof_inyear_rcp85], axis=1)
        all_last_jday_hypoxic_full_prof_inyear_rcp85 = pd.concat([all_last_jday_hypoxic_full_prof_inyear_rcp85 , last_jday_hypoxic_full_prof_inyear_rcp85], axis=1)
        all_len_hypoxic_full_prof_inyear_rcp85 = pd.concat([all_len_hypoxic_full_prof_inyear_rcp85 , len_hypoxic_full_prof_inyear_rcp85], axis=1)


# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp85'




# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_miroc_rcp85_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights_rcp85= np.append(all_weights_rcp85 , weights) 
        
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr = hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        
        first_jday_hypoxic_full_prof_inyear_rcp85=first_last_len_anoxic_prof_inyear  (C, Vr, time_series, threshold=2)[1]
        last_jday_hypoxic_full_prof_inyear_rcp85=first_last_len_anoxic_prof_inyear  (C, Vr, time_series, threshold=2)[3]
        len_hypoxic_full_prof_inyear_rcp85=first_last_len_anoxic_prof_inyear  (C, Vr, time_series, threshold=2)[4]
        

        all_first_jday_hypoxic_full_prof_inyear_rcp85 = pd.concat([all_first_jday_hypoxic_full_prof_inyear_rcp85 , first_jday_hypoxic_full_prof_inyear_rcp85], axis=1)
        all_last_jday_hypoxic_full_prof_inyear_rcp85 = pd.concat([all_last_jday_hypoxic_full_prof_inyear_rcp85 , last_jday_hypoxic_full_prof_inyear_rcp85], axis=1)
        all_len_hypoxic_full_prof_inyear_rcp85 = pd.concat([all_len_hypoxic_full_prof_inyear_rcp85 , len_hypoxic_full_prof_inyear_rcp85], axis=1)



#%%annova_uncertainity_rcp85 
all_first_jday_hypoxic_full_prof_inyear_rcp85= all_first_jday_hypoxic_full_prof_inyear_rcp85.replace(0, np.nan)

anova_first_jday_hypoxic_full_prof_rcp85=annova_uncertainity(all_first_jday_hypoxic_full_prof_inyear_rcp85)

anova_first_jday_hypoxic_full_prof_rcp85.describe().loc['mean', :]
"""
GCMs             62.302313
param            36.107641
interaction       1.590046
GCMs/param        3.217787
year           2052.500000
Name: mean, dtype: float64
"""

anova_first_jday_hypoxic_full_prof_rcp85.describe().loc['std', :]
"""
GCMs           22.217787
param          21.681076
interaction     1.296818
GCMs/param      3.763589
year           27.279418

"""

all_last_jday_hypoxic_full_prof_inyear_rcp85= all_last_jday_hypoxic_full_prof_inyear_rcp85.replace(0, np.nan)

anova_last_jday_hypoxic_full_prof_rcp85=annova_uncertainity(all_last_jday_hypoxic_full_prof_inyear_rcp85)

anova_last_jday_hypoxic_full_prof_rcp85.describe().loc['mean', :]
"""
GCMs            100.000000
param             0.036892
interaction      -0.036892
GCMs/param             inf
year           2052.500000
"""


anova_last_jday_hypoxic_full_prof_rcp85.describe().loc['std', :]

"""
GCMs           2.947194e-15
param          3.576842e-01
interaction    3.576842e-01
GCMs/param              NaN
year           2.727942e+01
"""



anova_len_jday_hypoxic_full_prof_rcp85=annova_uncertainity(all_len_hypoxic_full_prof_inyear_rcp85)

anova_len_jday_hypoxic_full_prof_rcp85.describe().loc['mean', :]
"""
GCMs             83.010665
param            16.215528
interaction       0.773806
GCMs/param        9.195628
year           2052.500000
Name: mean, dtype: float64
"""


anova_len_jday_hypoxic_full_prof_rcp85.describe().loc['std', :]
"""
GCMs           13.645478
param          12.942353
interaction     0.918748
GCMs/param      7.637223
year           27.279418
Name: std, dtype: float64
"""


#%%annova_uncertainity_rcp85_80years
all_first_jday_hypoxic_full_prof_inyear_rcp85=all_first_jday_hypoxic_full_prof_inyear_rcp85.replace(0, np.nan)

anova_first_jday_hypoxic_full_prof_rcp85_80years=annova_uncertainity(all_first_jday_hypoxic_full_prof_inyear_rcp85[all_first_jday_hypoxic_full_prof_inyear_rcp85.index>2019])

anova_first_jday_hypoxic_full_prof_rcp85_80years.describe().loc['mean', :]
"""
GCMs             62.069102
param            36.289742
interaction       1.641157
GCMs/param        3.245750
year           2059.500000
Name: mean, dtype: float64
"""

anova_first_jday_hypoxic_full_prof_rcp85_80years.describe().loc['std', :]
"""
GCMs           22.269765
param          21.736318
interaction     1.343272
GCMs/param      3.954630
year           23.237900
Name: std, dtype: float64

"""




anova_len_jday_hypoxic_full_prof_rcp85_80years=annova_uncertainity(all_len_hypoxic_full_prof_inyear_rcp85[all_len_hypoxic_full_prof_inyear_rcp85.index>2019])

anova_len_jday_hypoxic_full_prof_rcp85_80years.describe().loc['mean', :]
"""
GCMs             83.390723
param            15.825134
interaction       0.784143
GCMs/param        9.765363
year           2059.500000
Name: mean, dtype: float64
"""


anova_len_jday_hypoxic_full_prof_rcp85_80years.describe().loc['std', :]
"""
GCMs           13.888810
param          13.096413
interaction     0.957608
GCMs/param      8.049969
year           23.237900
Name: std, dtype: float64
"""





#%% Plotting of anova_len_jday_hypoxic_full_prof, anova_first_jday_hypoxic_full_prof rcp85

#first_jday_hypoxic_his

#years
contributions_first_jday_hypoxic_his_years=anova_first_jday_hypoxic_full_prof_his['year']
#GCMs
gcm_contributions_first_jday_hypoxic_his= anova_first_jday_hypoxic_full_prof_his['GCMs']
#Param
param_contributions_first_jday_hypoxic_his=anova_first_jday_hypoxic_full_prof_his['param']
#interaction
interact_contributions_first_jday_hypoxic_his =anova_first_jday_hypoxic_full_prof_his['interaction']


#len_jday_hypoxic_his

#years
contributions_len_jday_hypoxic_his_years=anova_len_jday_hypoxic_full_prof_his['year']
#GCMs
gcm_contributions_len_jday_hypoxic_his= anova_len_jday_hypoxic_full_prof_his['GCMs']
#Param
param_contributions_len_jday_hypoxic_his=anova_len_jday_hypoxic_full_prof_his['param']
#interaction
interact_contributions_len_jday_hypoxic_his =anova_len_jday_hypoxic_full_prof_his['interaction']

     

#first_jday_hypoxic_rcp26

#years
contributions_first_jday_hypoxic_rcp26_years=anova_first_jday_hypoxic_full_prof_rcp26['year']
#GCMs
gcm_contributions_first_jday_hypoxic_rcp26= anova_first_jday_hypoxic_full_prof_rcp26['GCMs']
#Param
param_contributions_first_jday_hypoxic_rcp26=anova_first_jday_hypoxic_full_prof_rcp26['param']
#interaction
interact_contributions_first_jday_hypoxic_rcp26 =anova_first_jday_hypoxic_full_prof_rcp26['interaction']


#len_jday_hypoxic_rcp26

#years
contributions_len_jday_hypoxic_rcp26_years=anova_len_jday_hypoxic_full_prof_rcp26['year']
#GCMs
gcm_contributions_len_jday_hypoxic_rcp26= anova_len_jday_hypoxic_full_prof_rcp26['GCMs']
#Param
param_contributions_len_jday_hypoxic_rcp26=anova_len_jday_hypoxic_full_prof_rcp26['param']
#interaction
interact_contributions_len_jday_hypoxic_rcp26 =anova_len_jday_hypoxic_full_prof_rcp26['interaction']

     

#first_jday_hypoxic_rcp60

#years
contributions_first_jday_hypoxic_rcp60_years=anova_first_jday_hypoxic_full_prof_rcp60['year']
#GCMs
gcm_contributions_first_jday_hypoxic_rcp60= anova_first_jday_hypoxic_full_prof_rcp60['GCMs']
#Param
param_contributions_first_jday_hypoxic_rcp60=anova_first_jday_hypoxic_full_prof_rcp60['param']
#interaction
interact_contributions_first_jday_hypoxic_rcp60 =anova_first_jday_hypoxic_full_prof_rcp60['interaction']


#len_jday_hypoxic_rcp60

#years
contributions_len_jday_hypoxic_rcp60_years=anova_len_jday_hypoxic_full_prof_rcp60['year']
#GCMs
gcm_contributions_len_jday_hypoxic_rcp60= anova_len_jday_hypoxic_full_prof_rcp60['GCMs']
#Param
param_contributions_len_jday_hypoxic_rcp60=anova_len_jday_hypoxic_full_prof_rcp60['param']
#interaction
interact_contributions_len_jday_hypoxic_rcp60 =anova_len_jday_hypoxic_full_prof_rcp60['interaction']

     
#first_jday_hypoxic_rcp85

#years
contributions_first_jday_hypoxic_rcp85_years=anova_first_jday_hypoxic_full_prof_rcp85['year']
#GCMs
gcm_contributions_first_jday_hypoxic_rcp85= anova_first_jday_hypoxic_full_prof_rcp85['GCMs']
#Param
param_contributions_first_jday_hypoxic_rcp85=anova_first_jday_hypoxic_full_prof_rcp85['param']
#interaction
interact_contributions_first_jday_hypoxic_rcp85 =anova_first_jday_hypoxic_full_prof_rcp85['interaction']


#len_jday_hypoxic_rcp85

#years
contributions_len_jday_hypoxic_rcp85_years=anova_len_jday_hypoxic_full_prof_rcp85['year']
#GCMs
gcm_contributions_len_jday_hypoxic_rcp85= anova_len_jday_hypoxic_full_prof_rcp85['GCMs']
#Param
param_contributions_len_jday_hypoxic_rcp85=anova_len_jday_hypoxic_full_prof_rcp85['param']
#interaction
interact_contributions_len_jday_hypoxic_rcp85 =anova_len_jday_hypoxic_full_prof_rcp85['interaction']

     
#%%For his

# Define the directory path
directory_path = r'C:\Users\mahta\OneDrive\Documents\PhD_py_code\Future_simulation_results\all_4_models\uncertainty'

# Change the current working directory
os.chdir(directory_path)     


import matplotlib.pyplot as plt
from matplotlib.patches import Patch

# Define colors explicitly as RGB tuples
colors = [(0.96, 0.80, 0.69), (0.6, 0.4, 0.8), (0, 0, 1)]  # Flesh, Dark Orchid, Blue

# Create a figure with three subplots
fig, axs = plt.subplots(1, 2, figsize=(20, 5), sharey=True, sharex=True)

axs[0].fill_between(contributions_first_jday_hypoxic_his_years, 0, gcm_contributions_first_jday_hypoxic_his , label='GCMs', alpha=0.7, color=colors[0], edgecolor='black')
axs[0].fill_between(contributions_first_jday_hypoxic_his_years, gcm_contributions_first_jday_hypoxic_his , gcm_contributions_first_jday_hypoxic_his + param_contributions_first_jday_hypoxic_his, label='Parameters', alpha=0.7, color=colors[1], edgecolor='black')
axs[0].fill_between(contributions_first_jday_hypoxic_his_years, gcm_contributions_first_jday_hypoxic_his  + param_contributions_first_jday_hypoxic_his, gcm_contributions_first_jday_hypoxic_his + param_contributions_first_jday_hypoxic_his + interact_contributions_first_jday_hypoxic_his, label='Interactions', alpha=0.7, color=colors[2], edgecolor='black')
axs[0].set_title('First day of full hypoxic profile in His', fontsize=20)
axs[0].set_ylim(0,100)
axs[0].set_xlim(1861, 2005)
axs[0].tick_params(axis='both', which='major', labelsize=20)



axs[1].fill_between(contributions_len_jday_hypoxic_his_years, 0, gcm_contributions_len_jday_hypoxic_his , label='GCMs', alpha=0.7, color=colors[0], edgecolor='black')
axs[1].fill_between(contributions_len_jday_hypoxic_his_years, gcm_contributions_len_jday_hypoxic_his , gcm_contributions_len_jday_hypoxic_his + param_contributions_len_jday_hypoxic_his, label='Parameters', alpha=0.7, color=colors[1], edgecolor='black')
axs[1].fill_between(contributions_len_jday_hypoxic_his_years, gcm_contributions_len_jday_hypoxic_his  + param_contributions_len_jday_hypoxic_his, gcm_contributions_len_jday_hypoxic_his + param_contributions_len_jday_hypoxic_his + interact_contributions_len_jday_hypoxic_his, label='Interactions', alpha=0.7, color=colors[2], edgecolor='black')
axs[1].set_title('Duration of full hypoxic profile in His', fontsize=20)
axs[1].set_ylim(0,100)
axs[1].set_xlim(1861, 2005)
axs[1].tick_params(axis='both', which='major', labelsize=20)


# Adding labels and title with increased font size
# fig.text(0.5, 0.08, 'Year', ha='center', fontsize=20)
fig.text(0.08, 0.5, 'Uncertainty sources percentage  [%]', va='center', rotation='vertical', fontsize=22)

# Create legend handles and labels
legend_handles = [Patch(facecolor=colors[0], edgecolor='black'), 
                  Patch(facecolor=colors[1], edgecolor='black'), 
                  Patch(facecolor=colors[2], edgecolor='black')]
legend_labels = ['GCMs', 'Parameters', 'Interactions']

# Add a single legend outside the subplots
fig.legend(legend_handles, legend_labels,bbox_to_anchor=(0.57, 0.06), fontsize=22)


# Save the plot
plt.savefig('uncertainty_first_len_full_hypoxia_duration_allyears_his.png', dpi=300, bbox_inches='tight')

plt.show()



#%%For all RCPs  all years 

# Define the directory path
directory_path = r'C:\Users\mahta\OneDrive\Documents\PhD_py_code\Future_simulation_results\all_4_models\uncertainty'

# Change the current working directory
os.chdir(directory_path)     
    

import matplotlib.pyplot as plt
from matplotlib.patches import Patch

# Define colors explicitly as RGB tuples
colors = [(0.96, 0.80, 0.69), (0.6, 0.4, 0.8), (0, 0, 1)]  # Flesh, Dark Orchid, Blue

# Create a figure with three subplots
fig, axs = plt.subplots(3, 2, figsize=(20, 15), sharey=True, sharex=True)

axs[0, 0].fill_between(contributions_first_jday_hypoxic_rcp26_years, 0, gcm_contributions_first_jday_hypoxic_rcp26 , label='GCMs', alpha=0.7, color=colors[0], edgecolor='black')
axs[0, 0].fill_between(contributions_first_jday_hypoxic_rcp26_years, gcm_contributions_first_jday_hypoxic_rcp26 , gcm_contributions_first_jday_hypoxic_rcp26 + param_contributions_first_jday_hypoxic_rcp26, label='Parameters', alpha=0.7, color=colors[1], edgecolor='black')
axs[0, 0].fill_between(contributions_first_jday_hypoxic_rcp26_years, gcm_contributions_first_jday_hypoxic_rcp26  + param_contributions_first_jday_hypoxic_rcp26, gcm_contributions_first_jday_hypoxic_rcp26 + param_contributions_first_jday_hypoxic_rcp26 + interact_contributions_first_jday_hypoxic_rcp26, label='Interactions', alpha=0.7, color=colors[2], edgecolor='black')
axs[0, 0].set_title('First day of full hypoxic profile in RCP2.6', fontsize=20)
axs[0, 0].set_ylim(0,100)
axs[0, 0].set_xlim(2006, 2099)
axs[0, 0].tick_params(axis='both', which='major', labelsize=20)



axs[0, 1].fill_between(contributions_len_jday_hypoxic_rcp26_years, 0, gcm_contributions_len_jday_hypoxic_rcp26 , label='GCMs', alpha=0.7, color=colors[0], edgecolor='black')
axs[0, 1].fill_between(contributions_len_jday_hypoxic_rcp26_years, gcm_contributions_len_jday_hypoxic_rcp26 , gcm_contributions_len_jday_hypoxic_rcp26 + param_contributions_len_jday_hypoxic_rcp26, label='Parameters', alpha=0.7, color=colors[1], edgecolor='black')
axs[0, 1].fill_between(contributions_len_jday_hypoxic_rcp26_years, gcm_contributions_len_jday_hypoxic_rcp26  + param_contributions_len_jday_hypoxic_rcp26, gcm_contributions_len_jday_hypoxic_rcp26 + param_contributions_len_jday_hypoxic_rcp26 + interact_contributions_len_jday_hypoxic_rcp26, label='Interactions', alpha=0.7, color=colors[2], edgecolor='black')
axs[0, 1].set_title('Duration of full hypoxic profile in RCP2.6', fontsize=20)
axs[0, 1].set_ylim(0,100)
axs[0, 1].set_xlim(2006, 2099)
axs[0, 1].tick_params(axis='both', which='major', labelsize=20)

axs[1, 0].fill_between(contributions_first_jday_hypoxic_rcp60_years, 0, gcm_contributions_first_jday_hypoxic_rcp60 , label='GCMs', alpha=0.7, color=colors[0], edgecolor='black')
axs[1, 0].fill_between(contributions_first_jday_hypoxic_rcp60_years, gcm_contributions_first_jday_hypoxic_rcp60 , gcm_contributions_first_jday_hypoxic_rcp60 + param_contributions_first_jday_hypoxic_rcp60, label='Parameters', alpha=0.7, color=colors[1], edgecolor='black')
axs[1, 0].fill_between(contributions_first_jday_hypoxic_rcp60_years, gcm_contributions_first_jday_hypoxic_rcp60  + param_contributions_first_jday_hypoxic_rcp60, gcm_contributions_first_jday_hypoxic_rcp60 + param_contributions_first_jday_hypoxic_rcp60 + interact_contributions_first_jday_hypoxic_rcp60, label='Interactions', alpha=0.7, color=colors[2], edgecolor='black')
axs[1, 0].set_title('First day of full hypoxic profile in RCP6.0', fontsize=20)
axs[1, 0].set_ylim(0,100)
axs[1, 0].set_xlim(2006, 2099)
axs[1, 0].tick_params(axis='both', which='major', labelsize=20)



axs[1, 1].fill_between(contributions_len_jday_hypoxic_rcp60_years, 0, gcm_contributions_len_jday_hypoxic_rcp60 , label='GCMs', alpha=0.7, color=colors[0], edgecolor='black')
axs[1, 1].fill_between(contributions_len_jday_hypoxic_rcp60_years, gcm_contributions_len_jday_hypoxic_rcp60 , gcm_contributions_len_jday_hypoxic_rcp60 + param_contributions_len_jday_hypoxic_rcp60, label='Parameters', alpha=0.7, color=colors[1], edgecolor='black')
axs[1, 1].fill_between(contributions_len_jday_hypoxic_rcp60_years, gcm_contributions_len_jday_hypoxic_rcp60  + param_contributions_len_jday_hypoxic_rcp60, gcm_contributions_len_jday_hypoxic_rcp60 + param_contributions_len_jday_hypoxic_rcp60 + interact_contributions_len_jday_hypoxic_rcp60, label='Interactions', alpha=0.7, color=colors[2], edgecolor='black')
axs[1, 1].set_title('Duration of full hypoxic profile in RCP6.0', fontsize=20)
axs[1, 1].set_ylim(0,100)
axs[1, 1].set_xlim(2006, 2099)
axs[1, 1].tick_params(axis='both', which='major', labelsize=20)




axs[2, 0].fill_between(contributions_first_jday_hypoxic_rcp85_years, 0, gcm_contributions_first_jday_hypoxic_rcp85 , label='GCMs', alpha=0.7, color=colors[0], edgecolor='black')
axs[2, 0].fill_between(contributions_first_jday_hypoxic_rcp85_years, gcm_contributions_first_jday_hypoxic_rcp85 , gcm_contributions_first_jday_hypoxic_rcp85 + param_contributions_first_jday_hypoxic_rcp85, label='Parameters', alpha=0.7, color=colors[1], edgecolor='black')
axs[2, 0].fill_between(contributions_first_jday_hypoxic_rcp85_years, gcm_contributions_first_jday_hypoxic_rcp85  + param_contributions_first_jday_hypoxic_rcp85, gcm_contributions_first_jday_hypoxic_rcp85 + param_contributions_first_jday_hypoxic_rcp85 + interact_contributions_first_jday_hypoxic_rcp85, label='Interactions', alpha=0.7, color=colors[2], edgecolor='black')
axs[2, 0].set_title('First day of full hypoxic profile in RCP8.5', fontsize=20)
axs[2, 0].set_ylim(0,100)
axs[2, 0].set_xlim(2006, 2099)
axs[2, 0].tick_params(axis='both', which='major', labelsize=20)



axs[2, 1].fill_between(contributions_len_jday_hypoxic_rcp85_years, 0, gcm_contributions_len_jday_hypoxic_rcp85 , label='GCMs', alpha=0.7, color=colors[0], edgecolor='black')
axs[2, 1].fill_between(contributions_len_jday_hypoxic_rcp85_years, gcm_contributions_len_jday_hypoxic_rcp85 , gcm_contributions_len_jday_hypoxic_rcp85 + param_contributions_len_jday_hypoxic_rcp85, label='Parameters', alpha=0.7, color=colors[1], edgecolor='black')
axs[2, 1].fill_between(contributions_len_jday_hypoxic_rcp85_years, gcm_contributions_len_jday_hypoxic_rcp85  + param_contributions_len_jday_hypoxic_rcp85, gcm_contributions_len_jday_hypoxic_rcp85 + param_contributions_len_jday_hypoxic_rcp85 + interact_contributions_len_jday_hypoxic_rcp85, label='Interactions', alpha=0.7, color=colors[2], edgecolor='black')
axs[2, 1].set_title('Duration of full hypoxic profile in RCP8.5', fontsize=20)
axs[2, 1].set_ylim(0,100)
axs[2, 1].set_xlim(2006, 2099)
axs[2, 1].tick_params(axis='both', which='major', labelsize=20)



# Adding labels and title with increased font size
# fig.text(0.5, 0.08, 'Year', ha='center', fontsize=20)
fig.text(0.08, 0.5, 'Uncertainty sources percentage [%]', va='center', rotation='vertical', fontsize=22)

# Create legend handles and labels
legend_handles = [Patch(facecolor=colors[0], edgecolor='black'), 
                  Patch(facecolor=colors[1], edgecolor='black'), 
                  Patch(facecolor=colors[2], edgecolor='black')]
legend_labels = ['GCMs', 'Parameters', 'Interactions']

# Add a single legend outside the subplots
fig.legend(legend_handles, legend_labels,bbox_to_anchor=(0.57, 0.06), fontsize=22)


# Save the plot
plt.savefig('uncertainty_first_len_full_hypoxia_duration_allyears_rcps.png', dpi=300, bbox_inches='tight')

plt.show()


#%% Uncertainity of 80 years in RCPs

#first_jday_hypoxic_rcp26

#years
contributions_first_jday_hypoxic_rcp26_years=anova_first_jday_hypoxic_full_prof_rcp26[anova_first_jday_hypoxic_full_prof_rcp26['year']>2019]['year']
#GCMs
gcm_contributions_first_jday_hypoxic_rcp26= anova_first_jday_hypoxic_full_prof_rcp26[anova_first_jday_hypoxic_full_prof_rcp26['year']>2019]['GCMs']
#Param
param_contributions_first_jday_hypoxic_rcp26=anova_first_jday_hypoxic_full_prof_rcp26[anova_first_jday_hypoxic_full_prof_rcp26['year']>2019]['param']
#interaction
interact_contributions_first_jday_hypoxic_rcp26 =anova_first_jday_hypoxic_full_prof_rcp26[anova_first_jday_hypoxic_full_prof_rcp26['year']>2019]['interaction']


#len_jday_hypoxic_rcp26

#years
contributions_len_jday_hypoxic_rcp26_years=anova_len_jday_hypoxic_full_prof_rcp26[anova_len_jday_hypoxic_full_prof_rcp26['year']>2019]['year']
#GCMs
gcm_contributions_len_jday_hypoxic_rcp26= anova_len_jday_hypoxic_full_prof_rcp26[anova_len_jday_hypoxic_full_prof_rcp26['year']>2019]['GCMs']
#Param
param_contributions_len_jday_hypoxic_rcp26=anova_len_jday_hypoxic_full_prof_rcp26[anova_len_jday_hypoxic_full_prof_rcp26['year']>2019]['param']
#interaction
interact_contributions_len_jday_hypoxic_rcp26 =anova_len_jday_hypoxic_full_prof_rcp26[anova_len_jday_hypoxic_full_prof_rcp26['year']>2019]['interaction']


     

#first_jday_hypoxic_rcp60

#years
contributions_first_jday_hypoxic_rcp60_years=anova_first_jday_hypoxic_full_prof_rcp60[anova_first_jday_hypoxic_full_prof_rcp60['year']>2019]['year']
#GCMs
gcm_contributions_first_jday_hypoxic_rcp60= anova_first_jday_hypoxic_full_prof_rcp60[anova_first_jday_hypoxic_full_prof_rcp60['year']>2019]['GCMs']
#Param
param_contributions_first_jday_hypoxic_rcp60=anova_first_jday_hypoxic_full_prof_rcp60[anova_first_jday_hypoxic_full_prof_rcp60['year']>2019]['param']
#interaction
interact_contributions_first_jday_hypoxic_rcp60 =anova_first_jday_hypoxic_full_prof_rcp60[anova_first_jday_hypoxic_full_prof_rcp60['year']>2019]['interaction']


#len_jday_hypoxic_rcp60

#years
contributions_len_jday_hypoxic_rcp60_years=anova_len_jday_hypoxic_full_prof_rcp60[anova_len_jday_hypoxic_full_prof_rcp60['year']>2019]['year']
#GCMs
gcm_contributions_len_jday_hypoxic_rcp60= anova_len_jday_hypoxic_full_prof_rcp60[anova_len_jday_hypoxic_full_prof_rcp60['year']>2019]['GCMs']
#Param
param_contributions_len_jday_hypoxic_rcp60=anova_len_jday_hypoxic_full_prof_rcp60[anova_len_jday_hypoxic_full_prof_rcp60['year']>2019]['param']
#interaction
interact_contributions_len_jday_hypoxic_rcp60 =anova_len_jday_hypoxic_full_prof_rcp60[anova_len_jday_hypoxic_full_prof_rcp60['year']>2019]['interaction']


#first_jday_hypoxic_rcp85

#years
contributions_first_jday_hypoxic_rcp85_years=anova_first_jday_hypoxic_full_prof_rcp85[anova_first_jday_hypoxic_full_prof_rcp85['year']>2019]['year']
#GCMs
gcm_contributions_first_jday_hypoxic_rcp85= anova_first_jday_hypoxic_full_prof_rcp85[anova_first_jday_hypoxic_full_prof_rcp85['year']>2019]['GCMs']
#Param
param_contributions_first_jday_hypoxic_rcp85=anova_first_jday_hypoxic_full_prof_rcp85[anova_first_jday_hypoxic_full_prof_rcp85['year']>2019]['param']
#interaction
interact_contributions_first_jday_hypoxic_rcp85 =anova_first_jday_hypoxic_full_prof_rcp85[anova_first_jday_hypoxic_full_prof_rcp85['year']>2019]['interaction']


#len_jday_hypoxic_rcp85

#years
contributions_len_jday_hypoxic_rcp85_years=anova_len_jday_hypoxic_full_prof_rcp85[anova_len_jday_hypoxic_full_prof_rcp85['year']>2019]['year']
#GCMs
gcm_contributions_len_jday_hypoxic_rcp85= anova_len_jday_hypoxic_full_prof_rcp85[anova_len_jday_hypoxic_full_prof_rcp85['year']>2019]['GCMs']
#Param
param_contributions_len_jday_hypoxic_rcp85=anova_len_jday_hypoxic_full_prof_rcp85[anova_len_jday_hypoxic_full_prof_rcp85['year']>2019]['param']
#interaction
interact_contributions_len_jday_hypoxic_rcp85 =anova_len_jday_hypoxic_full_prof_rcp85[anova_len_jday_hypoxic_full_prof_rcp85['year']>2019]['interaction']



#%%For all RCPs  80 years 

# Define the directory path
directory_path = r'C:\Users\mahta\OneDrive\Documents\PhD_py_code\Future_simulation_results\all_4_models\uncertainty'

# Change the current working directory
os.chdir(directory_path)     
    

import matplotlib.pyplot as plt
from matplotlib.patches import Patch

# Define colors explicitly as RGB tuples
colors = [(0.96, 0.80, 0.69), (0.6, 0.4, 0.8), (0, 0, 1)]  # Flesh, Dark Orchid, Blue

# Create a figure with three subplots
fig, axs = plt.subplots(3, 2, figsize=(20, 15), sharey=True, sharex=True)

axs[0, 0].fill_between(contributions_first_jday_hypoxic_rcp26_years, 0, gcm_contributions_first_jday_hypoxic_rcp26 , label='GCMs', alpha=0.7, color=colors[0], edgecolor='black')
axs[0, 0].fill_between(contributions_first_jday_hypoxic_rcp26_years, gcm_contributions_first_jday_hypoxic_rcp26 , gcm_contributions_first_jday_hypoxic_rcp26 + param_contributions_first_jday_hypoxic_rcp26, label='Parameters', alpha=0.7, color=colors[1], edgecolor='black')
axs[0, 0].fill_between(contributions_first_jday_hypoxic_rcp26_years, gcm_contributions_first_jday_hypoxic_rcp26  + param_contributions_first_jday_hypoxic_rcp26, gcm_contributions_first_jday_hypoxic_rcp26 + param_contributions_first_jday_hypoxic_rcp26 + interact_contributions_first_jday_hypoxic_rcp26, label='Interactions', alpha=0.7, color=colors[2], edgecolor='black')
axs[0, 0].set_title('First day of full hypoxic profile in RCP2.6', fontsize=20)
axs[0, 0].set_ylim(0,100)
axs[0, 0].set_xlim(2020, 2099)
axs[0, 0].tick_params(axis='both', which='major', labelsize=20)



axs[0, 1].fill_between(contributions_len_jday_hypoxic_rcp26_years, 0, gcm_contributions_len_jday_hypoxic_rcp26 , label='GCMs', alpha=0.7, color=colors[0], edgecolor='black')
axs[0, 1].fill_between(contributions_len_jday_hypoxic_rcp26_years, gcm_contributions_len_jday_hypoxic_rcp26 , gcm_contributions_len_jday_hypoxic_rcp26 + param_contributions_len_jday_hypoxic_rcp26, label='Parameters', alpha=0.7, color=colors[1], edgecolor='black')
axs[0, 1].fill_between(contributions_len_jday_hypoxic_rcp26_years, gcm_contributions_len_jday_hypoxic_rcp26  + param_contributions_len_jday_hypoxic_rcp26, gcm_contributions_len_jday_hypoxic_rcp26 + param_contributions_len_jday_hypoxic_rcp26 + interact_contributions_len_jday_hypoxic_rcp26, label='Interactions', alpha=0.7, color=colors[2], edgecolor='black')
axs[0, 1].set_title('Duration of full hypoxic profile in RCP2.6', fontsize=20)
axs[0, 1].set_ylim(0,100)
axs[0, 1].set_xlim(2020, 2099)
axs[0, 1].tick_params(axis='both', which='major', labelsize=20)

axs[1, 0].fill_between(contributions_first_jday_hypoxic_rcp60_years, 0, gcm_contributions_first_jday_hypoxic_rcp60 , label='GCMs', alpha=0.7, color=colors[0], edgecolor='black')
axs[1, 0].fill_between(contributions_first_jday_hypoxic_rcp60_years, gcm_contributions_first_jday_hypoxic_rcp60 , gcm_contributions_first_jday_hypoxic_rcp60 + param_contributions_first_jday_hypoxic_rcp60, label='Parameters', alpha=0.7, color=colors[1], edgecolor='black')
axs[1, 0].fill_between(contributions_first_jday_hypoxic_rcp60_years, gcm_contributions_first_jday_hypoxic_rcp60  + param_contributions_first_jday_hypoxic_rcp60, gcm_contributions_first_jday_hypoxic_rcp60 + param_contributions_first_jday_hypoxic_rcp60 + interact_contributions_first_jday_hypoxic_rcp60, label='Interactions', alpha=0.7, color=colors[2], edgecolor='black')
axs[1, 0].set_title('First day of full hypoxic profile in RCP6.0', fontsize=20)
axs[1, 0].set_ylim(0,100)
axs[1, 0].set_xlim(2020, 2099)
axs[1, 0].tick_params(axis='both', which='major', labelsize=20)



axs[1, 1].fill_between(contributions_len_jday_hypoxic_rcp60_years, 0, gcm_contributions_len_jday_hypoxic_rcp60 , label='GCMs', alpha=0.7, color=colors[0], edgecolor='black')
axs[1, 1].fill_between(contributions_len_jday_hypoxic_rcp60_years, gcm_contributions_len_jday_hypoxic_rcp60 , gcm_contributions_len_jday_hypoxic_rcp60 + param_contributions_len_jday_hypoxic_rcp60, label='Parameters', alpha=0.7, color=colors[1], edgecolor='black')
axs[1, 1].fill_between(contributions_len_jday_hypoxic_rcp60_years, gcm_contributions_len_jday_hypoxic_rcp60  + param_contributions_len_jday_hypoxic_rcp60, gcm_contributions_len_jday_hypoxic_rcp60 + param_contributions_len_jday_hypoxic_rcp60 + interact_contributions_len_jday_hypoxic_rcp60, label='Interactions', alpha=0.7, color=colors[2], edgecolor='black')
axs[1, 1].set_title('Duration of full hypoxic profile in RCP6.0', fontsize=20)
axs[1, 1].set_ylim(0,100)
axs[1, 1].set_xlim(2020, 2099)
axs[1, 1].tick_params(axis='both', which='major', labelsize=20)




axs[2, 0].fill_between(contributions_first_jday_hypoxic_rcp85_years, 0, gcm_contributions_first_jday_hypoxic_rcp85 , label='GCMs', alpha=0.7, color=colors[0], edgecolor='black')
axs[2, 0].fill_between(contributions_first_jday_hypoxic_rcp85_years, gcm_contributions_first_jday_hypoxic_rcp85 , gcm_contributions_first_jday_hypoxic_rcp85 + param_contributions_first_jday_hypoxic_rcp85, label='Parameters', alpha=0.7, color=colors[1], edgecolor='black')
axs[2, 0].fill_between(contributions_first_jday_hypoxic_rcp85_years, gcm_contributions_first_jday_hypoxic_rcp85  + param_contributions_first_jday_hypoxic_rcp85, gcm_contributions_first_jday_hypoxic_rcp85 + param_contributions_first_jday_hypoxic_rcp85 + interact_contributions_first_jday_hypoxic_rcp85, label='Interactions', alpha=0.7, color=colors[2], edgecolor='black')
axs[2, 0].set_title('First day of full hypoxic profile in RCP8.5', fontsize=20)
axs[2, 0].set_ylim(0,100)
axs[2, 0].set_xlim(2020, 2099)
axs[2, 0].tick_params(axis='both', which='major', labelsize=20)



axs[2, 1].fill_between(contributions_len_jday_hypoxic_rcp85_years, 0, gcm_contributions_len_jday_hypoxic_rcp85 , label='GCMs', alpha=0.7, color=colors[0], edgecolor='black')
axs[2, 1].fill_between(contributions_len_jday_hypoxic_rcp85_years, gcm_contributions_len_jday_hypoxic_rcp85 , gcm_contributions_len_jday_hypoxic_rcp85 + param_contributions_len_jday_hypoxic_rcp85, label='Parameters', alpha=0.7, color=colors[1], edgecolor='black')
axs[2, 1].fill_between(contributions_len_jday_hypoxic_rcp85_years, gcm_contributions_len_jday_hypoxic_rcp85  + param_contributions_len_jday_hypoxic_rcp85, gcm_contributions_len_jday_hypoxic_rcp85 + param_contributions_len_jday_hypoxic_rcp85 + interact_contributions_len_jday_hypoxic_rcp85, label='Interactions', alpha=0.7, color=colors[2], edgecolor='black')
axs[2, 1].set_title('Duration of full hypoxic profile in RCP8.5', fontsize=20)
axs[2, 1].set_ylim(0,100)
axs[2, 1].set_xlim(2020, 2099)
axs[2, 1].tick_params(axis='both', which='major', labelsize=20)



# Adding labels and title with increased font size
# fig.text(0.5, 0.08, 'Year', ha='center', fontsize=20)
fig.text(0.08, 0.5, 'Uncertainty sources percentage [%]', va='center', rotation='vertical', fontsize=22)

# Create legend handles and labels
legend_handles = [Patch(facecolor=colors[0], edgecolor='black'), 
                  Patch(facecolor=colors[1], edgecolor='black'), 
                  Patch(facecolor=colors[2], edgecolor='black')]
legend_labels = ['GCMs', 'Parameters', 'Interactions']

# Add a single legend outside the subplots
fig.legend(legend_handles, legend_labels,bbox_to_anchor=(0.57, 0.06), fontsize=22)


# Save the plot
plt.savefig('uncertainty_first_len_full_hypoxia_duration_allyears_rcps_80years.png', dpi=300, bbox_inches='tight')

plt.show()


#%%#
#=====================================GLUE ============================

#%%his

# first_jday_hypoxic_full_prof_inyear_his
timeseries_year_his= all_first_jday_hypoxic_full_prof_inyear_his.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_first_jday_hypoxic_full_prof_inyear_his.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights_his))

# Build glue df
glue_first_jday_hypoxic_full_prof_inyear_his = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_first_jday_hypoxic_full_prof_inyear_his=glue_first_jday_hypoxic_full_prof_inyear_his.set_index(timeseries_year_his)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory
glue_first_jday_hypoxic_full_prof_inyear_his.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/his/glue_first_jday_hypoxic_full_prof_inyear_his.csv')



# last_jday_hypoxic_full_prof_inyear_his
timeseries_year_his= all_last_jday_hypoxic_full_prof_inyear_his.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_last_jday_hypoxic_full_prof_inyear_his.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights_his))

# Build glue df
glue_last_jday_hypoxic_full_prof_inyear_his = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_last_jday_hypoxic_full_prof_inyear_his=glue_last_jday_hypoxic_full_prof_inyear_his.set_index(timeseries_year_his)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory
glue_last_jday_hypoxic_full_prof_inyear_his.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/his/glue_last_jday_hypoxic_full_prof_inyear_his.csv')

           

# len_hypoxic_full_prof_inyear_his
timeseries_year_his= all_len_hypoxic_full_prof_inyear_his.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_len_hypoxic_full_prof_inyear_his.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights_his))

# Build glue df
glue_len_hypoxic_full_prof_inyear_his = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_len_hypoxic_full_prof_inyear_his=glue_len_hypoxic_full_prof_inyear_his.set_index(timeseries_year_his)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory
glue_len_hypoxic_full_prof_inyear_his.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/his/glue_len_hypoxic_full_prof_inyear_his.csv')


#%%rcp26

# first_jday_hypoxic_full_prof_inyear_rcp26
timeseries_year_rcp26= all_first_jday_hypoxic_full_prof_inyear_rcp26.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_first_jday_hypoxic_full_prof_inyear_rcp26.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights_rcp26))

# Build glue df
glue_first_jday_hypoxic_full_prof_inyear_rcp26 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_first_jday_hypoxic_full_prof_inyear_rcp26=glue_first_jday_hypoxic_full_prof_inyear_rcp26.set_index(timeseries_year_rcp26)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory
glue_first_jday_hypoxic_full_prof_inyear_rcp26.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/rcp26/glue_first_jday_hypoxic_full_prof_inyear_rcp26.csv')



# last_jday_hypoxic_full_prof_inyear_rcp26
timeseries_year_rcp26= all_last_jday_hypoxic_full_prof_inyear_rcp26.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_last_jday_hypoxic_full_prof_inyear_rcp26.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights_rcp26))

# Build glue df
glue_last_jday_hypoxic_full_prof_inyear_rcp26 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_last_jday_hypoxic_full_prof_inyear_rcp26=glue_last_jday_hypoxic_full_prof_inyear_rcp26.set_index(timeseries_year_rcp26)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory
glue_last_jday_hypoxic_full_prof_inyear_rcp26.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/rcp26/glue_last_jday_hypoxic_full_prof_inyear_rcp26.csv')

           

# len_hypoxic_full_prof_inyear_rcp26
timeseries_year_rcp26= all_len_hypoxic_full_prof_inyear_rcp26.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_len_hypoxic_full_prof_inyear_rcp26.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights_rcp26))

# Build glue df
glue_len_hypoxic_full_prof_inyear_rcp26 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_len_hypoxic_full_prof_inyear_rcp26=glue_len_hypoxic_full_prof_inyear_rcp26.set_index(timeseries_year_rcp26)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory
glue_len_hypoxic_full_prof_inyear_rcp26.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/rcp26/glue_len_hypoxic_full_prof_inyear_rcp26.csv')


#%%rcp60

# first_jday_hypoxic_full_prof_inyear_rcp60
timeseries_year_rcp60= all_first_jday_hypoxic_full_prof_inyear_rcp60.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_first_jday_hypoxic_full_prof_inyear_rcp60.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights_rcp60))

# Build glue df
glue_first_jday_hypoxic_full_prof_inyear_rcp60 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_first_jday_hypoxic_full_prof_inyear_rcp60=glue_first_jday_hypoxic_full_prof_inyear_rcp60.set_index(timeseries_year_rcp60)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory
glue_first_jday_hypoxic_full_prof_inyear_rcp60.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/rcp60/glue_first_jday_hypoxic_full_prof_inyear_rcp60.csv')



# last_jday_hypoxic_full_prof_inyear_rcp60
timeseries_year_rcp60= all_last_jday_hypoxic_full_prof_inyear_rcp60.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_last_jday_hypoxic_full_prof_inyear_rcp60.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights_rcp60))

# Build glue df
glue_last_jday_hypoxic_full_prof_inyear_rcp60 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_last_jday_hypoxic_full_prof_inyear_rcp60=glue_last_jday_hypoxic_full_prof_inyear_rcp60.set_index(timeseries_year_rcp60)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory
glue_last_jday_hypoxic_full_prof_inyear_rcp60.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/rcp60/glue_last_jday_hypoxic_full_prof_inyear_rcp60.csv')

           

# len_hypoxic_full_prof_inyear_rcp60
timeseries_year_rcp60= all_len_hypoxic_full_prof_inyear_rcp60.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_len_hypoxic_full_prof_inyear_rcp60.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights_rcp60))

# Build glue df
glue_len_hypoxic_full_prof_inyear_rcp60 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_len_hypoxic_full_prof_inyear_rcp60=glue_len_hypoxic_full_prof_inyear_rcp60.set_index(timeseries_year_rcp60)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory
glue_len_hypoxic_full_prof_inyear_rcp60.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/rcp60/glue_len_hypoxic_full_prof_inyear_rcp60.csv')

#%%rcp85

# first_jday_hypoxic_full_prof_inyear_rcp85
timeseries_year_rcp85= all_first_jday_hypoxic_full_prof_inyear_rcp85.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_first_jday_hypoxic_full_prof_inyear_rcp85.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights_rcp85))

# Build glue df
glue_first_jday_hypoxic_full_prof_inyear_rcp85 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_first_jday_hypoxic_full_prof_inyear_rcp85=glue_first_jday_hypoxic_full_prof_inyear_rcp85.set_index(timeseries_year_rcp85)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory
glue_first_jday_hypoxic_full_prof_inyear_rcp85.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/rcp85/glue_first_jday_hypoxic_full_prof_inyear_rcp85.csv')



# last_jday_hypoxic_full_prof_inyear_rcp85
timeseries_year_rcp85= all_last_jday_hypoxic_full_prof_inyear_rcp85.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_last_jday_hypoxic_full_prof_inyear_rcp85.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights_rcp85))

# Build glue df
glue_last_jday_hypoxic_full_prof_inyear_rcp85 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_last_jday_hypoxic_full_prof_inyear_rcp85=glue_last_jday_hypoxic_full_prof_inyear_rcp85.set_index(timeseries_year_rcp85)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory
glue_last_jday_hypoxic_full_prof_inyear_rcp85.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/rcp85/glue_last_jday_hypoxic_full_prof_inyear_rcp85.csv')

           

# len_hypoxic_full_prof_inyear_rcp85
timeseries_year_rcp85= all_len_hypoxic_full_prof_inyear_rcp85.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_len_hypoxic_full_prof_inyear_rcp85.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights_rcp85))

# Build glue df
glue_len_hypoxic_full_prof_inyear_rcp85 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_len_hypoxic_full_prof_inyear_rcp85=glue_len_hypoxic_full_prof_inyear_rcp85.set_index(timeseries_year_rcp85)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory
glue_len_hypoxic_full_prof_inyear_rcp85.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/rcp85/glue_len_hypoxic_full_prof_inyear_rcp85.csv')

#%%Sorting the glue dataframe according to the index (year)

glue_len_hypoxic_full_prof_inyear_his=glue_len_hypoxic_full_prof_inyear_his.sort_index()

glue_len_hypoxic_full_prof_inyear_rcp26=glue_len_hypoxic_full_prof_inyear_rcp26.sort_index()

glue_len_hypoxic_full_prof_inyear_rcp60=glue_len_hypoxic_full_prof_inyear_rcp60.sort_index()

glue_len_hypoxic_full_prof_inyear_rcp85=glue_len_hypoxic_full_prof_inyear_rcp85.sort_index()


#%% replacing first jday with nan instead of 0

glue_first_jday_hypoxic_full_prof_inyear_his=glue_first_jday_hypoxic_full_prof_inyear_his.replace(0, np.nan)

glue_first_jday_hypoxic_full_prof_inyear_rcp26=glue_first_jday_hypoxic_full_prof_inyear_rcp26.replace(0, np.nan)

glue_first_jday_hypoxic_full_prof_inyear_rcp60=glue_first_jday_hypoxic_full_prof_inyear_rcp60.replace(0, np.nan)

glue_first_jday_hypoxic_full_prof_inyear_rcp85=glue_first_jday_hypoxic_full_prof_inyear_rcp85.replace(0, np.nan)




#%%Plotiing%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

#%%duration of full hypoxic profile 



os.chdir('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/')

import matplotlib.pyplot as plt

fig =plt.figure(figsize=(15, 10))
ax= plt.subplot(111)


ax=plt.fill_between(glue_len_hypoxic_full_prof_inyear_his.index.astype(float), glue_len_hypoxic_full_prof_inyear_his['5%'], glue_len_hypoxic_full_prof_inyear_his['95%'], color='grey', alpha=0.2 ,  label= 'His 90% CI')
ax=plt.plot(glue_len_hypoxic_full_prof_inyear_his.index.astype(float), glue_len_hypoxic_full_prof_inyear_his['50%'].astype(float), 'k', label='His median', alpha=0.9, linewidth=3  )


ax=plt.fill_between(glue_len_hypoxic_full_prof_inyear_rcp26.index.astype(float), glue_len_hypoxic_full_prof_inyear_rcp26['5%'], glue_len_hypoxic_full_prof_inyear_rcp26['95%'], color='green', alpha=0.3 ,  label= 'RCP2.6 90% CI')
ax=plt.plot(glue_len_hypoxic_full_prof_inyear_rcp26.index.astype(float), glue_len_hypoxic_full_prof_inyear_rcp26['50%'].astype(float), 'darkgreen', label='RCP2.6 median', alpha=0.9, linewidth=3  )

ax=plt.fill_between(glue_len_hypoxic_full_prof_inyear_rcp60.index.astype(float), glue_len_hypoxic_full_prof_inyear_rcp60['5%'], glue_len_hypoxic_full_prof_inyear_rcp60['95%'], color='yellow', alpha=0.4 ,  label= 'RCP6.0 90% CI')
ax=plt.plot(glue_len_hypoxic_full_prof_inyear_rcp60.index.astype(float), glue_len_hypoxic_full_prof_inyear_rcp60['50%'].astype(float), 'yellow', label='RCP6.0 median', alpha=0.9, linewidth=3  )

ax=plt.fill_between(glue_len_hypoxic_full_prof_inyear_rcp85.index.astype(float), glue_len_hypoxic_full_prof_inyear_rcp85['5%'], glue_len_hypoxic_full_prof_inyear_rcp85['95%'], color='red', alpha=0.2 ,  label= 'RCP8.5 90% CI')
ax=plt.plot(glue_len_hypoxic_full_prof_inyear_rcp85.index.astype(float), glue_len_hypoxic_full_prof_inyear_rcp85['50%'].astype(float), 'r', label='RCP8.5 median', alpha=0.9, linewidth=3  )

ax=plt.ylabel('Duration of full deep hypoxia [d]' , fontsize=26)
ax=plt.xlabel('Year' , fontsize=26)
ax=plt.yticks(fontsize= 22)
ax=plt.xticks(rotation=45 , fontsize=22)
ax=plt.legend(bbox_to_anchor=(1.1, -0.2), fontsize=22, ncol=4)#)   
fig.savefig("GLUE_Timeseries_length_full_hypoxic_16combinationJaJv_ave_obs_4models_4scenarios.png",  dpi=300, bbox_inches='tight')



#%%
np.mean(glue_len_hypoxic_full_prof_inyear_his['50%'])#46.41731058747204
np.mean(glue_len_hypoxic_full_prof_inyear_rcp26['50%'])#60.895825759866966
np.mean(glue_len_hypoxic_full_prof_inyear_rcp60['50%'])#63.64214639675043
np.mean(glue_len_hypoxic_full_prof_inyear_rcp85['50%'])# 68.7920116520591

#%%hypoxic_factor 30 yerars from each scenarios compare 



#anormaly 
# baseline [1976-2005]
len_hypoxic_full_prof_inyear_ref=glue_len_hypoxic_full_prof_inyear_his[1975 < glue_len_hypoxic_full_prof_inyear_his.index]['50%'].mean()
#47.37051701415144

#near future [2030-2059] # maximum temp in 2033

glue_len_hypoxic_full_prof_inyear_rcp26[(2029 < glue_len_hypoxic_full_prof_inyear_rcp26.index) & (glue_len_hypoxic_full_prof_inyear_rcp26.index < 2060)]['50%'].mean()
#62.168886341908156
glue_len_hypoxic_full_prof_inyear_rcp60[(2029 < glue_len_hypoxic_full_prof_inyear_rcp60.index) & (glue_len_hypoxic_full_prof_inyear_rcp60.index < 2060)]['50%'].mean()
#60.342441872028175
glue_len_hypoxic_full_prof_inyear_rcp85[(2029 < glue_len_hypoxic_full_prof_inyear_rcp85.index) & (glue_len_hypoxic_full_prof_inyear_rcp85.index < 2060)]['50%'].mean()
# 64.13635124452689

 
#Distant future [2070-2099]

glue_len_hypoxic_full_prof_inyear_rcp26[(2069 < glue_len_hypoxic_full_prof_inyear_rcp26.index) & (glue_len_hypoxic_full_prof_inyear_rcp26.index < 2100)]['50%'].mean()
#  62.41304160839891
glue_len_hypoxic_full_prof_inyear_rcp60[(2069 < glue_len_hypoxic_full_prof_inyear_rcp60.index) & (glue_len_hypoxic_full_prof_inyear_rcp60.index< 2100)]['50%'].mean()
# 71.78399872344929
glue_len_hypoxic_full_prof_inyear_rcp85[(2069 < glue_len_hypoxic_full_prof_inyear_rcp85.index) & (glue_len_hypoxic_full_prof_inyear_rcp85.index < 2100)]['50%'].mean()
# 82.17378951111527
           

#%%Sorting the glue first_jday dataframe according to the index (year)


glue_first_jday_hypoxic_full_prof_inyear_his=glue_first_jday_hypoxic_full_prof_inyear_his.sort_index()

glue_first_jday_hypoxic_full_prof_inyear_rcp26=glue_first_jday_hypoxic_full_prof_inyear_rcp26.sort_index()

glue_first_jday_hypoxic_full_prof_inyear_rcp60=glue_first_jday_hypoxic_full_prof_inyear_rcp60.sort_index()

glue_first_jday_hypoxic_full_prof_inyear_rcp85=glue_first_jday_hypoxic_full_prof_inyear_rcp85.sort_index()



#%%len of full hypoxia_anormaly 
os.chdir('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/')

import matplotlib.pyplot as plt

fig =plt.figure(figsize=(15, 10))
ax= plt.subplot(111)


ax=plt.fill_between(glue_len_hypoxic_full_prof_inyear_his[1975 < glue_len_hypoxic_full_prof_inyear_his.index].index.astype(float),
                      glue_len_hypoxic_full_prof_inyear_his[1975 < glue_len_hypoxic_full_prof_inyear_his.index]['5%'] - len_hypoxic_full_prof_inyear_ref,
                      glue_len_hypoxic_full_prof_inyear_his[1975 < glue_len_hypoxic_full_prof_inyear_his.index ]['95%'] - len_hypoxic_full_prof_inyear_ref,
                      color='grey', alpha=0.2, label='His 90% CI')


ax=plt.plot(glue_len_hypoxic_full_prof_inyear_his[1975< glue_len_hypoxic_full_prof_inyear_his.index ].index.astype(float),
            glue_len_hypoxic_full_prof_inyear_his[1975 < glue_len_hypoxic_full_prof_inyear_his.index]['50%'] - len_hypoxic_full_prof_inyear_ref,
            'k', label='His median', alpha=0.9, linewidth=3   )

ax=plt.fill_between(glue_len_hypoxic_full_prof_inyear_rcp26.index.astype(float), glue_len_hypoxic_full_prof_inyear_rcp26['5%']-len_hypoxic_full_prof_inyear_ref, glue_len_hypoxic_full_prof_inyear_rcp26['95%']-len_hypoxic_full_prof_inyear_ref, color='darkgreen', alpha=0.2 ,  label= 'RCP6.0 90% CI')
ax=plt.plot(glue_len_hypoxic_full_prof_inyear_rcp26.index.astype(float), glue_len_hypoxic_full_prof_inyear_rcp26['50%']-len_hypoxic_full_prof_inyear_ref, 'darkgreen', label='RCP6.0 median', alpha=0.9, linewidth=3  )
                      
                     
ax=plt.fill_between(glue_len_hypoxic_full_prof_inyear_rcp60.index.astype(float), glue_len_hypoxic_full_prof_inyear_rcp60['5%']-len_hypoxic_full_prof_inyear_ref, glue_len_hypoxic_full_prof_inyear_rcp60['95%']-len_hypoxic_full_prof_inyear_ref, color='yellow', alpha=0.4 ,  label= 'RCP6.0 90% CI')
ax=plt.plot(glue_len_hypoxic_full_prof_inyear_rcp60.index.astype(float), glue_len_hypoxic_full_prof_inyear_rcp60['50%']-len_hypoxic_full_prof_inyear_ref, 'yellow', label='RCP6.0 median', alpha=0.9, linewidth=3  )

ax=plt.fill_between(glue_len_hypoxic_full_prof_inyear_rcp85.index.astype(float), glue_len_hypoxic_full_prof_inyear_rcp85['5%']-len_hypoxic_full_prof_inyear_ref, glue_len_hypoxic_full_prof_inyear_rcp85['95%']-len_hypoxic_full_prof_inyear_ref, color='r', alpha=0.2 ,  label= 'RCP8.5 90% CI')
ax=plt.plot(glue_len_hypoxic_full_prof_inyear_rcp85.index.astype(float), glue_len_hypoxic_full_prof_inyear_rcp85['50%']-len_hypoxic_full_prof_inyear_ref, 'r', label='RCP8.5 median', alpha=0.9, linewidth=3  )

ax=plt.ylabel('Anormaly of full deep hypoxia duration [d]' , fontsize=26)
ax=plt.xlabel('Year' , fontsize=26)
ax=plt.yticks(fontsize= 22)
ax=plt.xticks(rotation=45 , fontsize=22)
ax=plt.legend(bbox_to_anchor=(1.1, -0.2), fontsize=22 , ncol=4)  
fig.savefig("GLUE_Timeseries_len_hypoxic_full_prof_anormaly_16combinationJaJv_ave_obs_4models_4scenarios.png",  dpi=300, bbox_inches='tight')

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% condition ###############
#########################################################################

#%%Plotiing%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

#%%First Jday with full hypoxic



os.chdir('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/')

import matplotlib.pyplot as plt

fig =plt.figure(figsize=(15, 10))
ax= plt.subplot(111)


ax=plt.fill_between(glue_first_jday_hypoxic_full_prof_inyear_his.index.astype(float), glue_first_jday_hypoxic_full_prof_inyear_his['5%'], glue_first_jday_hypoxic_full_prof_inyear_his['95%'], color='grey', alpha=0.2 ,  label= 'His 90% CI')
ax=plt.plot(glue_first_jday_hypoxic_full_prof_inyear_his.index.astype(float), glue_first_jday_hypoxic_full_prof_inyear_his['50%'].astype(float), 'k', label='His median', alpha=0.9, linewidth=3  )


ax=plt.fill_between(glue_first_jday_hypoxic_full_prof_inyear_rcp26.index.astype(float), glue_first_jday_hypoxic_full_prof_inyear_rcp26['5%'], glue_first_jday_hypoxic_full_prof_inyear_rcp26['95%'], color='darkgreen', alpha=0.2 ,  label= 'RCP2.6 90% CI')
ax=plt.plot(glue_first_jday_hypoxic_full_prof_inyear_rcp26.index.astype(float), glue_first_jday_hypoxic_full_prof_inyear_rcp26['50%'].astype(float), 'darkgreen', label='RCP2.6 median', alpha=0.9, linewidth=3  )

ax=plt.fill_between(glue_first_jday_hypoxic_full_prof_inyear_rcp60.index.astype(float), glue_first_jday_hypoxic_full_prof_inyear_rcp60['5%'], glue_first_jday_hypoxic_full_prof_inyear_rcp60['95%'], color='yellow', alpha=0.2 ,  label= 'RCP6.0 90% CI')
ax=plt.plot(glue_first_jday_hypoxic_full_prof_inyear_rcp60.index.astype(float), glue_first_jday_hypoxic_full_prof_inyear_rcp60['50%'].astype(float), 'yellow', label='RCP6.0 median', alpha=0.9, linewidth=3  )

ax=plt.fill_between(glue_first_jday_hypoxic_full_prof_inyear_rcp85.index.astype(float), glue_first_jday_hypoxic_full_prof_inyear_rcp85['5%'], glue_first_jday_hypoxic_full_prof_inyear_rcp85['95%'], color='red', alpha=0.2 ,  label= 'RCP8.5 90% CI')
ax=plt.plot(glue_first_jday_hypoxic_full_prof_inyear_rcp85.index.astype(float), glue_first_jday_hypoxic_full_prof_inyear_rcp85['50%'].astype(float), 'r', label='RCP8.5 median', alpha=0.9, linewidth=3  )

ax=plt.ylabel('First full deep hypoxia [Jday]' , fontsize=26)
ax=plt.xlabel('Year' , fontsize=26)
ax=plt.yticks(fontsize= 22)
ax=plt.xticks(rotation=45 , fontsize=22)
ax=plt.legend(bbox_to_anchor=(1.1, -0.2), fontsize=22, ncol=4)#)   
fig.savefig("GLUE_Timeseries_first_full_hypoxic_16combinationJaJv_ave_obs_4models_4scenarios.png",  dpi=300, bbox_inches='tight')




#%%
np.mean(glue_first_jday_hypoxic_full_prof_inyear_his['50%'])#195.30215348221577
np.mean(glue_first_jday_hypoxic_full_prof_inyear_rcp26['50%'])#188.56020342622193
np.mean(glue_first_jday_hypoxic_full_prof_inyear_rcp60['50%'])# 186.30627655418263
np.mean(glue_first_jday_hypoxic_full_prof_inyear_rcp85['50%'])# 183.29976457666066

#%%hypoxic_factor 30 yerars from each scenarios compare 


#anormaly 
# his [1976-2005]
first_jday_hypoxic_full_prof_inyear_ref=glue_first_jday_hypoxic_full_prof_inyear_his[1975< glue_first_jday_hypoxic_full_prof_inyear_his.index]['50%'].mean()
#198.35993593610246


#near future [2030-205]

glue_first_jday_hypoxic_full_prof_inyear_rcp26[(2029 < glue_first_jday_hypoxic_full_prof_inyear_rcp26.index) & (glue_first_jday_hypoxic_full_prof_inyear_rcp26.index < 2060)]['50%'].mean()
#188.0561565984772
glue_first_jday_hypoxic_full_prof_inyear_rcp60[(2029 < glue_first_jday_hypoxic_full_prof_inyear_rcp60.index) & (glue_first_jday_hypoxic_full_prof_inyear_rcp60.index < 2060)]['50%'].mean()
#187.71255136707074
glue_first_jday_hypoxic_full_prof_inyear_rcp85[(2029 < glue_first_jday_hypoxic_full_prof_inyear_rcp85.index) & (glue_first_jday_hypoxic_full_prof_inyear_rcp85.index < 2060)]['50%'].mean()
#185.74501498149792

 
#Distant future [2070-2099]

glue_first_jday_hypoxic_full_prof_inyear_rcp26[(2069 < glue_first_jday_hypoxic_full_prof_inyear_rcp26.index) & (glue_first_jday_hypoxic_full_prof_inyear_rcp26.index < 2100)]['50%'].mean()
#187.55042968056745
glue_first_jday_hypoxic_full_prof_inyear_rcp60[(2069 < glue_first_jday_hypoxic_full_prof_inyear_rcp60.index) & (glue_first_jday_hypoxic_full_prof_inyear_rcp60.index < 2100)]['50%'].mean()
#180.98093806256577
glue_first_jday_hypoxic_full_prof_inyear_rcp85[(2069 < glue_first_jday_hypoxic_full_prof_inyear_rcp85.index) & (glue_first_jday_hypoxic_full_prof_inyear_rcp85.index < 2100)]['50%'].mean()
#176.61739079732752
           



#%%_anormaly 
os.chdir('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/')

import matplotlib.pyplot as plt

fig =plt.figure(figsize=(15, 10))
ax= plt.subplot(111)


ax=plt.fill_between(glue_first_jday_hypoxic_full_prof_inyear_his[1975 < glue_first_jday_hypoxic_full_prof_inyear_his.index].index.astype(float),
                      glue_first_jday_hypoxic_full_prof_inyear_his[1975 < glue_first_jday_hypoxic_full_prof_inyear_his.index]['5%'] - first_jday_hypoxic_full_prof_inyear_ref,
                      glue_first_jday_hypoxic_full_prof_inyear_his[1975 < glue_first_jday_hypoxic_full_prof_inyear_his.index]['95%'] - first_jday_hypoxic_full_prof_inyear_ref,
                      color='grey', alpha=0.2, label='His 90% CI')


ax=plt.plot(glue_first_jday_hypoxic_full_prof_inyear_his[1975 < glue_first_jday_hypoxic_full_prof_inyear_his.index ].index.astype(float),
            glue_first_jday_hypoxic_full_prof_inyear_his[1975 < glue_first_jday_hypoxic_full_prof_inyear_his.index]['50%'] - first_jday_hypoxic_full_prof_inyear_ref,
            'k', label='His median', alpha=0.9, linewidth=3   )

ax=plt.fill_between(glue_first_jday_hypoxic_full_prof_inyear_rcp26.index.astype(float), glue_first_jday_hypoxic_full_prof_inyear_rcp26['5%']-first_jday_hypoxic_full_prof_inyear_ref, glue_first_jday_hypoxic_full_prof_inyear_rcp26['95%']-first_jday_hypoxic_full_prof_inyear_ref, color='darkgreen', alpha=0.2 ,  label= 'RCP6.0 90% CI')
ax=plt.plot(glue_first_jday_hypoxic_full_prof_inyear_rcp26.index.astype(float), glue_first_jday_hypoxic_full_prof_inyear_rcp26['50%']-first_jday_hypoxic_full_prof_inyear_ref, 'darkgreen', label='RCP6.0 median', alpha=0.9, linewidth=3  )
                      
                     
ax=plt.fill_between(glue_first_jday_hypoxic_full_prof_inyear_rcp60.index.astype(float), glue_first_jday_hypoxic_full_prof_inyear_rcp60['5%']-first_jday_hypoxic_full_prof_inyear_ref, glue_first_jday_hypoxic_full_prof_inyear_rcp60['95%']-first_jday_hypoxic_full_prof_inyear_ref, color='yellow', alpha=0.3 ,  label= 'RCP6.0 90% CI')
ax=plt.plot(glue_first_jday_hypoxic_full_prof_inyear_rcp60.index.astype(float), glue_first_jday_hypoxic_full_prof_inyear_rcp60['50%']-first_jday_hypoxic_full_prof_inyear_ref, 'yellow', label='RCP6.0 median', alpha=0.9, linewidth=3  )

ax=plt.fill_between(glue_first_jday_hypoxic_full_prof_inyear_rcp85.index.astype(float), glue_first_jday_hypoxic_full_prof_inyear_rcp85['5%']-first_jday_hypoxic_full_prof_inyear_ref, glue_first_jday_hypoxic_full_prof_inyear_rcp85['95%']-first_jday_hypoxic_full_prof_inyear_ref, color='r', alpha=0.2 ,  label= 'RCP8.5 90% CI')
ax=plt.plot(glue_first_jday_hypoxic_full_prof_inyear_rcp85.index.astype(float), glue_first_jday_hypoxic_full_prof_inyear_rcp85['50%']-first_jday_hypoxic_full_prof_inyear_ref, 'r', label='RCP8.5 median', alpha=0.9, linewidth=3  )

ax=plt.ylabel('Anormaly of full deep hypoxia onset [Jday]' , fontsize=26)
ax=plt.xlabel('Year' , fontsize=26)
ax=plt.yticks(fontsize= 22)
ax=plt.xticks(rotation=45 , fontsize=22)
ax=plt.legend(bbox_to_anchor=(1.1, -0.2), fontsize=22 , ncol=4)  
fig.savefig("GLUE_Timeseries_first_jday_hypoxic_full_prof_anormaly_16combinationJaJv_ave_obs_4models_4scenarios.png",  dpi=300, bbox_inches='tight')

#%% Histogram or violn plot 

    
median_first_jday_hypoxic_full_prof_his=glue_first_jday_hypoxic_full_prof_inyear_his['50%']
median_first_jday_hypoxic_full_prof_rcp26=glue_first_jday_hypoxic_full_prof_inyear_rcp26['50%']
median_first_jday_hypoxic_full_prof_rcp60=glue_first_jday_hypoxic_full_prof_inyear_rcp60['50%']
median_first_jday_hypoxic_full_prof_rcp85=glue_first_jday_hypoxic_full_prof_inyear_rcp85['50%']  
    
# Create a DataFrame with NaN values
df_first_jday_hypoxic_full_prof_4models =pd.concat([
    pd.Series(median_first_jday_hypoxic_full_prof_his, name='His' ),
    pd.Series(median_first_jday_hypoxic_full_prof_rcp26, name='RCP2.6'),
    pd.Series(median_first_jday_hypoxic_full_prof_rcp60, name='RCP6.0' ),
    pd.Series(median_first_jday_hypoxic_full_prof_rcp85, name='RCP8.5' )], axis=1)    
    
    

    
median_len_hypoxic_full_prof_his=glue_len_hypoxic_full_prof_inyear_his['50%']
median_len_hypoxic_full_prof_rcp26=glue_len_hypoxic_full_prof_inyear_rcp26['50%']
median_len_hypoxic_full_prof_rcp60=glue_len_hypoxic_full_prof_inyear_rcp60['50%']
median_len_hypoxic_full_prof_rcp85=glue_len_hypoxic_full_prof_inyear_rcp85['50%']  
    
# Create a DataFrame with NaN values
df_len_hypoxic_full_prof_4models =pd.concat([
    pd.Series(median_len_hypoxic_full_prof_his, name='His' ),
    pd.Series(median_len_hypoxic_full_prof_rcp26, name='RCP2.6'),
    pd.Series(median_len_hypoxic_full_prof_rcp60, name='RCP6.0' ),
    pd.Series(median_len_hypoxic_full_prof_rcp85, name='RCP8.5' )], axis=1)    
    
    
median_last_jday_hypoxic_full_prof_his=glue_last_jday_hypoxic_full_prof_inyear_his['50%']
median_last_jday_hypoxic_full_prof_rcp26=glue_last_jday_hypoxic_full_prof_inyear_rcp26['50%']
median_last_jday_hypoxic_full_prof_rcp60=glue_last_jday_hypoxic_full_prof_inyear_rcp60['50%']
median_last_jday_hypoxic_full_prof_rcp85=glue_last_jday_hypoxic_full_prof_inyear_rcp85['50%']  
    
# Create a DataFrame with NaN values
df_last_jday_hypoxic_full_prof_4models =pd.concat([
    pd.Series(median_last_jday_hypoxic_full_prof_his, name='His' ),
    pd.Series(median_last_jday_hypoxic_full_prof_rcp26, name='RCP2.6'),
    pd.Series(median_last_jday_hypoxic_full_prof_rcp60, name='RCP6.0' ),
    pd.Series(median_last_jday_hypoxic_full_prof_rcp85, name='RCP8.5' )], axis=1)    
    
 



#%%
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

os.chdir ('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results')



# Set up the color palette
custom_palette = ['grey', 'darkgreen', 'yellow', 'red']

# Create subplots with space between them
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(10, 4))

# Adjust the width space between subplots
plt.subplots_adjust(wspace=0.3)
sns.violinplot(ax=axes[0], data=df_first_jday_hypoxic_full_prof_4models, palette=custom_palette)
axes[0].set_ylabel('Full deep hypoxia onset [Jday]')

#axes[0].set_ylim(60, 210)  # Set the y-axis limits
axes[0].set_yticks(range(120, 250, 30))  # Set the y-axis ticks at intervals of 20



plt.subplots_adjust(wspace=0.3)
sns.violinplot(ax=axes[1], data=df_len_hypoxic_full_prof_4models, palette=custom_palette)
axes[1].set_ylabel('Full deep hypoxia duration [day]')
axes[1].set_yticks(range(0, 150, 30))  # Set the y-axis ticks at intervals of 20



#sns.violinplot(ax=axes[2], data=df_last_jday_hypoxic_full_prof_4models, palette=custom_palette)
#axes[2].set_ylabel('Last day of full deep hypoxia [day]')
#axes[2].set_yticks(range(210, 280, 30))  # Set the y-axis ticks at intervals of 20



plt.savefig("allsenarios_4models_median_first_len_of_full_hypoxic.png", dpi=300)







#%% averaging over whole scenarios value 
np.mean(glue_len_hypoxic_full_prof_inyear_his['50%'])#46.41731058747204
np.mean(glue_len_hypoxic_full_prof_inyear_rcp26['50%'])#60.895825759866966
np.mean(glue_len_hypoxic_full_prof_inyear_rcp60['50%'])#63.64214639675043
np.mean(glue_len_hypoxic_full_prof_inyear_rcp85['50%'])#68.7920116520591



#%%hypoxic_duration 30 yerars from each scenarios compare 



#anomaly 
# baseline [1976-2005]
glue_base_len_hypoxic_full_prof_his=glue_len_hypoxic_full_prof_inyear_his[1975 < glue_len_hypoxic_full_prof_inyear_his.index]['50%']
len_hypoxic_full_prof_ref=np.mean(glue_base_len_hypoxic_full_prof_his)
# 47.37051701415144


#near future [2030-2059]

glue_near_future_len_hypoxic_full_prof_rcp26=glue_len_hypoxic_full_prof_inyear_rcp26[(2029 < glue_len_hypoxic_full_prof_inyear_rcp26.index) & (glue_len_hypoxic_full_prof_inyear_rcp26.index < 2060)]['50%']
np.mean(glue_near_future_len_hypoxic_full_prof_rcp26)
#62.168886341908156
glue_near_future_len_hypoxic_full_prof_rcp60=glue_len_hypoxic_full_prof_inyear_rcp60[(2029 < glue_len_hypoxic_full_prof_inyear_rcp60.index) & (glue_len_hypoxic_full_prof_inyear_rcp60.index < 2060)]['50%']
np.mean(glue_near_future_len_hypoxic_full_prof_rcp60)
#60.342441872028175
glue_near_future_len_hypoxic_full_prof_rcp85=glue_len_hypoxic_full_prof_inyear_rcp85[(2029 < glue_len_hypoxic_full_prof_inyear_rcp85.index) & (glue_len_hypoxic_full_prof_inyear_rcp85.index < 2060)]['50%']
np.mean(glue_near_future_len_hypoxic_full_prof_rcp85)
# 64.13635124452689

 
#Distant future [2070-2099]

glue_distant_future_len_hypoxic_full_prof_rcp26=glue_len_hypoxic_full_prof_inyear_rcp26[(2069 < glue_len_hypoxic_full_prof_inyear_rcp26.index) & (glue_len_hypoxic_full_prof_inyear_rcp26.index < 2100)]['50%']
np.mean(glue_distant_future_len_hypoxic_full_prof_rcp26)
# 62.41304160839891
glue_distant_future_len_hypoxic_full_prof_rcp60=glue_len_hypoxic_full_prof_inyear_rcp60[(2069 < glue_len_hypoxic_full_prof_inyear_rcp60.index) & (glue_len_hypoxic_full_prof_inyear_rcp60.index< 2100)]['50%']
np.mean(glue_distant_future_len_hypoxic_full_prof_rcp60)
#71.78399872344929
glue_distant_future_len_hypoxic_full_prof_rcp85=glue_len_hypoxic_full_prof_inyear_rcp85[(2069 < glue_len_hypoxic_full_prof_inyear_rcp85.index) & (glue_len_hypoxic_full_prof_inyear_rcp85.index < 2100)]['50%']
np.mean(glue_distant_future_len_hypoxic_full_prof_rcp85)
#82.17378951111527
   


###====over 30 years in his and each RCPs 

# baseline [1976-2005]
autocorr_MK_org_modif_sens_slope_test(glue_base_len_hypoxic_full_prof_his)
(0.048622571434139214,
 'positively autocorrelated',
 'increasing',
 0.017393206960585772,
 0.35,
 42.18127311789057)

#near future [2030-2059]


autocorr_MK_org_modif_sens_slope_test(glue_near_future_len_hypoxic_full_prof_rcp26)
(0.03144972148329328,
 'positively autocorrelated',
 'no trend',
 0.06785095641210503,
 0,
 0)
autocorr_MK_org_modif_sens_slope_test(glue_near_future_len_hypoxic_full_prof_rcp60)
(0.0105145145808575,
 'positively autocorrelated',
 'increasing',
 0.025355129751366112,
 0.23076923076923078,
 57.15384615384615)

autocorr_MK_org_modif_sens_slope_test(glue_near_future_len_hypoxic_full_prof_rcp85)
(0.02385084689143253,
 'positively autocorrelated',
 'increasing',
 0.009126431594368434,
 0.4970652214287575,
 55.79255428928302)



#Distant future [2070-2099]


autocorr_MK_org_modif_sens_slope_test(glue_distant_future_len_hypoxic_full_prof_rcp26)
(0.03097462610176752,
 'positively autocorrelated',
 'no trend',
 0.25200491940395464,
 0,
 0)
autocorr_MK_org_modif_sens_slope_test(glue_distant_future_len_hypoxic_full_prof_rcp60)
(0.012043582835300904,
 'positively autocorrelated',
 'no trend',
 0.10258094978938503,
 0,
 0)

autocorr_MK_org_modif_sens_slope_test(glue_distant_future_len_hypoxic_full_prof_rcp85)
(0.019588472169704975,
 'positively autocorrelated',
 'increasing',
 0.0032016611784995153,
 0.5286845195960126,
 73.84056568475262)


#%% Trendlines over whole periods:
# no trend in his but increasing trendlines of all rcps 
# for length of full hypoxic    
    
# his     
  
autocorr_MK_org_modif_sens_slope_test(glue_len_hypoxic_full_prof_inyear_his['50%'])
"""
(0.051897525140994154,
 'positively autocorrelated',
 'no trend',
 0.8786359773379031,
 0,
 0)
"""
#rcp26
autocorr_MK_org_modif_sens_slope_test(glue_len_hypoxic_full_prof_inyear_rcp26['50%'])
"""
(0.03073367570694338,
 'positively autocorrelated',
 'increasing',
 0.0009645189287477152,
 0.08695652173913043,
 55.95652173913044)
"""

#rcp60
autocorr_MK_org_modif_sens_slope_test(glue_len_hypoxic_full_prof_inyear_rcp60['50%'])
"""
(0.014097530205756194,
 'positively autocorrelated',
 'increasing',
 2.6645352591003757e-15,
 0.22857142857142856,
 52.62899561587391)
"""

#rcp85
autocorr_MK_org_modif_sens_slope_test(glue_len_hypoxic_full_prof_inyear_rcp85['50%'])
"""
(0.025915448599774737,
 'positively autocorrelated',
 'increasing',
 0.0,
 0.4008195577027446,
 48.86189056682238)
"""





#%% 80 years from 2020 for len_hypoxic_full_prof


glue_80years_len_hypoxic_full_prof_inyear_rcp26=glue_len_hypoxic_full_prof_inyear_rcp26[2019 < glue_len_hypoxic_full_prof_inyear_rcp26.index]

glue_80years_len_hypoxic_full_prof_inyear_rcp60=glue_len_hypoxic_full_prof_inyear_rcp60[2019 < glue_len_hypoxic_full_prof_inyear_rcp60.index]


glue_80years_len_hypoxic_full_prof_inyear_rcp85=glue_len_hypoxic_full_prof_inyear_rcp85[2019 < glue_len_hypoxic_full_prof_inyear_rcp85.index]



#=========== trendline # Over the 80 years


autocorr_MK_org_modif_sens_slope_test(glue_80years_len_hypoxic_full_prof_inyear_rcp26['50%'])
(0.03148266121080445,
 'positively autocorrelated',
 'no trend',
 0.15983125021669897,
 0,
 0)

autocorr_MK_org_modif_sens_slope_test(glue_80years_len_hypoxic_full_prof_inyear_rcp60['50%'])
(0.011627911699759354,
 'positively autocorrelated',
 'increasing',
 1.2922996006636822e-13,
 0.25,
 55.125)


autocorr_MK_org_modif_sens_slope_test(glue_80years_len_hypoxic_full_prof_inyear_rcp85['50%'])
(0.02070074130923784,
 'positively autocorrelated',
 'increasing',
 5.88418203051333e-14,
 0.4140616223412662,
 54.156859283061124)

#============= mean of first 10 yaers over 80 years 

#rcp2.6
np.mean(glue_80years_len_hypoxic_full_prof_inyear_rcp26[glue_80years_len_hypoxic_full_prof_inyear_rcp26.index<2030]['50%'])
61.00332456160212

#rcp6.0
np.mean(glue_80years_len_hypoxic_full_prof_inyear_rcp60[glue_80years_len_hypoxic_full_prof_inyear_rcp60.index<2030]['50%'])
58.2

#rcp8.5
np.mean(glue_80years_len_hypoxic_full_prof_inyear_rcp85[glue_80years_len_hypoxic_full_prof_inyear_rcp85.index<2030]['50%'])
59.40805716709296

#============== mean of last 10 yaers over 80 years 

#rcp2.6
np.mean(glue_80years_len_hypoxic_full_prof_inyear_rcp26[glue_80years_len_hypoxic_full_prof_inyear_rcp26.index>2089]['50%'])
63.300711931028346

#rcp6.0
np.mean(glue_80years_len_hypoxic_full_prof_inyear_rcp60[glue_80years_len_hypoxic_full_prof_inyear_rcp60.index>2089]['50%'])
72.84642970224193

#rcp8.5
np.mean(glue_80years_len_hypoxic_full_prof_inyear_rcp85[glue_80years_len_hypoxic_full_prof_inyear_rcp85.index>2089]['50%'])
90.96697411866708

#%% averaging over whole scenarios value for first hypoxic full profile 

np.mean(glue_first_jday_hypoxic_full_prof_inyear_his['50%'])#195.30215348221577
np.mean(glue_first_jday_hypoxic_full_prof_inyear_rcp26['50%'])#188.56020342622193
np.mean(glue_first_jday_hypoxic_full_prof_inyear_rcp60['50%'])#186.30627655418263
np.mean(glue_first_jday_hypoxic_full_prof_inyear_rcp85['50%'])#183.29976457666066


#%%hypoxic_duration 30 yerars from each scenarios compare 



#anomaly 
# baseline [1976-2005]
glue_base_first_jday_hypoxic_full_prof_his=glue_first_jday_hypoxic_full_prof_inyear_his[1975 < glue_first_jday_hypoxic_full_prof_inyear_his.index]['50%']
len_hypoxic_full_prof_ref=np.mean(glue_base_first_jday_hypoxic_full_prof_his)
#198.35993593610246


#near future [2030-2059]

glue_near_future_first_jday_hypoxic_full_prof_rcp26=glue_first_jday_hypoxic_full_prof_inyear_rcp26[(2029 < glue_first_jday_hypoxic_full_prof_inyear_rcp26.index) & (glue_first_jday_hypoxic_full_prof_inyear_rcp26.index < 2060)]['50%']
np.mean(glue_near_future_first_jday_hypoxic_full_prof_rcp26)
#188.0561565984772
glue_near_future_first_jday_hypoxic_full_prof_rcp60=glue_first_jday_hypoxic_full_prof_inyear_rcp60[(2029 < glue_first_jday_hypoxic_full_prof_inyear_rcp60.index) & (glue_first_jday_hypoxic_full_prof_inyear_rcp60.index < 2060)]['50%']
np.mean(glue_near_future_first_jday_hypoxic_full_prof_rcp60)
# 187.71255136707074
glue_near_future_first_jday_hypoxic_full_prof_rcp85=glue_first_jday_hypoxic_full_prof_inyear_rcp85[(2029 < glue_first_jday_hypoxic_full_prof_inyear_rcp85.index) & (glue_first_jday_hypoxic_full_prof_inyear_rcp85.index < 2060)]['50%']
np.mean(glue_near_future_first_jday_hypoxic_full_prof_rcp85)
#185.74501498149792

 
#Distant future [2070-2099]

glue_distant_future_first_jday_hypoxic_full_prof_rcp26=glue_first_jday_hypoxic_full_prof_inyear_rcp26[(2069 < glue_first_jday_hypoxic_full_prof_inyear_rcp26.index) & (glue_first_jday_hypoxic_full_prof_inyear_rcp26.index < 2100)]['50%']
np.mean(glue_distant_future_first_jday_hypoxic_full_prof_rcp26)
#187.55042968056745
glue_distant_future_first_jday_hypoxic_full_prof_rcp60=glue_first_jday_hypoxic_full_prof_inyear_rcp60[(2069 < glue_first_jday_hypoxic_full_prof_inyear_rcp60.index) & (glue_first_jday_hypoxic_full_prof_inyear_rcp60.index< 2100)]['50%']
np.mean(glue_distant_future_first_jday_hypoxic_full_prof_rcp60)
#180.98093806256577
glue_distant_future_first_jday_hypoxic_full_prof_rcp85=glue_first_jday_hypoxic_full_prof_inyear_rcp85[(2069 < glue_first_jday_hypoxic_full_prof_inyear_rcp85.index) & (glue_first_jday_hypoxic_full_prof_inyear_rcp85.index < 2100)]['50%']
np.mean(glue_distant_future_first_jday_hypoxic_full_prof_rcp85)
#176.61739079732752
   


###====over 30 years in his and each RCPs 

# baseline [1976-2005]
autocorr_MK_org_modif_sens_slope_test(glue_base_first_jday_hypoxic_full_prof_his)
(0.0010506374848320123,
 'positively autocorrelated',
 'no trend',
 0.34185757930211524,
 0,
 0)
#near future [2030-2059]


autocorr_MK_org_modif_sens_slope_test(glue_near_future_first_jday_hypoxic_full_prof_rcp26)
(0.00302555049360824,
 'positively autocorrelated',
 'no trend',
 0.31625369830892813,
 0,
 0)

autocorr_MK_org_modif_sens_slope_test(glue_near_future_first_jday_hypoxic_full_prof_rcp60)
(0.0007735362922120659,
 'positively autocorrelated',
 'no trend',
 0.1611700100757063,
 0,
 0)

autocorr_MK_org_modif_sens_slope_test(glue_near_future_first_jday_hypoxic_full_prof_rcp85)
(0.0008065610483586766,
 'positively autocorrelated',
 'no trend',
 0.11548190817571036,
 0,
 0)

#Distant future [2070-2099]


autocorr_MK_org_modif_sens_slope_test(glue_distant_future_first_jday_hypoxic_full_prof_rcp26)
(0.0031202145755079604,
 'positively autocorrelated',
 'no trend',
 0.10825951190126415,
 0,
 0)


autocorr_MK_org_modif_sens_slope_test(glue_distant_future_first_jday_hypoxic_full_prof_rcp60)
(0.003037588575477561,
 'positively autocorrelated',
 'no trend',
 0.774454513697967,
 0,
 0)


autocorr_MK_org_modif_sens_slope_test(glue_distant_future_first_jday_hypoxic_full_prof_rcp85)
(0.003355501984902021,
 'positively autocorrelated',
 'decreasing',
 0.0033425003146396737,
 -0.30434782608695654,
 182.15330877182032)


#%% Trendlines over whole periods:
# no trend in his but decreasing trendlines of 6.0 and 8.5 rcps 
# for first jday of full hypoxic    
    
# his     
  
autocorr_MK_org_modif_sens_slope_test(glue_first_jday_hypoxic_full_prof_inyear_his['50%'])
"""
(0.002704692716580061,
 'positively autocorrelated',
 'increasing',
 0.0028086029075840013,
 0.0328712810719492,
 194.13326776281966)
"""
#rcp26
autocorr_MK_org_modif_sens_slope_test(glue_first_jday_hypoxic_full_prof_inyear_rcp26['50%'])
"""
(0.0030563902266776202,
 'positively autocorrelated',
 'decreasing',
 0.01634088748053486,
 -0.05714285714285714,
 192.65714285714284)
"""

#rcp60
autocorr_MK_org_modif_sens_slope_test(glue_first_jday_hypoxic_full_prof_inyear_rcp60['50%'])
"""
(0.0016427991594115453,
 'positively autocorrelated',
 'decreasing',
 3.743672039036028e-13,
 -0.140625,
 193.5390625)
"""

#rcp85
autocorr_MK_org_modif_sens_slope_test(glue_first_jday_hypoxic_full_prof_inyear_rcp85['50%'])
"""
(0.002382963938635776,
 'positively autocorrelated',
 'decreasing',
 2.879474436667806e-12,
 -0.17489755528715706,
 192.1327363208528)
"""





#%% 80 years from 2020 for first_jday_hypoxic_full_prof


glue_80years_first_jday_hypoxic_full_prof_inyear_rcp26=glue_first_jday_hypoxic_full_prof_inyear_rcp26[2019 < glue_first_jday_hypoxic_full_prof_inyear_rcp26.index]

glue_80years_first_jday_hypoxic_full_prof_inyear_rcp60=glue_first_jday_hypoxic_full_prof_inyear_rcp60[2019 < glue_first_jday_hypoxic_full_prof_inyear_rcp60.index]


glue_80years_first_jday_hypoxic_full_prof_inyear_rcp85=glue_first_jday_hypoxic_full_prof_inyear_rcp85[2019 < glue_first_jday_hypoxic_full_prof_inyear_rcp85.index]

#=========== trendline # Over the 80 years


autocorr_MK_org_modif_sens_slope_test(glue_80years_first_jday_hypoxic_full_prof_inyear_rcp26['50%'])
(0.0034243242096363975,
 'positively autocorrelated',
 'no trend',
 0.16070927865298645,
 0,
 0)

autocorr_MK_org_modif_sens_slope_test(glue_80years_first_jday_hypoxic_full_prof_inyear_rcp60['50%'])
(0.0016287461797451584,
 'positively autocorrelated',
 'decreasing',
 1.6542323066914832e-13,
 -0.14564393939393938,
 191.75293560606062)

autocorr_MK_org_modif_sens_slope_test(glue_80years_first_jday_hypoxic_full_prof_inyear_rcp85['50%'])
(0.002038664112863069,
 'positively autocorrelated',
 'decreasing',
 1.2322086240246222e-08,
 -0.16227182668879614,
 189.40973715420745)

#============= mean of first 10 yaers over 80 years 

#rcp2.6
np.mean(glue_80years_first_jday_hypoxic_full_prof_inyear_rcp26[glue_80years_first_jday_hypoxic_full_prof_inyear_rcp26.index<2030]['50%'])
187.24999999999997

#rcp6.0
np.mean(glue_80years_first_jday_hypoxic_full_prof_inyear_rcp60[glue_80years_first_jday_hypoxic_full_prof_inyear_rcp60.index<2030]['50%'])
191.19918044229726

#rcp8.5
np.mean(glue_80years_first_jday_hypoxic_full_prof_inyear_rcp85[glue_80years_first_jday_hypoxic_full_prof_inyear_rcp85.index<2030]['50%'])
185.04399974694857

#============== mean of last 10 yaers over 80 years 

#rcp2.6
np.mean(glue_80years_first_jday_hypoxic_full_prof_inyear_rcp26[glue_80years_first_jday_hypoxic_full_prof_inyear_rcp26.index>2089]['50%'])
185.89649574593267

#rcp6.0
np.mean(glue_80years_first_jday_hypoxic_full_prof_inyear_rcp60[glue_80years_first_jday_hypoxic_full_prof_inyear_rcp60.index>2089]['50%'])
179.61274597472055

#rcp8.5
np.mean(glue_80years_first_jday_hypoxic_full_prof_inyear_rcp85[glue_80years_first_jday_hypoxic_full_prof_inyear_rcp85.index>2089]['50%'])
170.00514896234844



#%%
#%%plotting 80 years of len and first jday of full hypoxic profile  


import matplotlib.pyplot as plt
import numpy as np

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(26, 8))

# Plotting the first subplot
ax1.fill_between(glue_80years_len_hypoxic_full_prof_inyear_rcp26.index.astype(float), glue_80years_len_hypoxic_full_prof_inyear_rcp26['5%'], glue_80years_len_hypoxic_full_prof_inyear_rcp26['95%'], color='darkgreen', alpha=0.3)# ,  label= 'RCP2.6 90% CI')
ax1.plot(glue_80years_len_hypoxic_full_prof_inyear_rcp26.index.astype(float), glue_80years_len_hypoxic_full_prof_inyear_rcp26['50%'], 'darkgreen', alpha=0.9, linewidth=3  )#, label='RCP2.6 median'

ax1.fill_between(glue_80years_len_hypoxic_full_prof_inyear_rcp60.index.astype(float), glue_80years_len_hypoxic_full_prof_inyear_rcp60['5%'], glue_80years_len_hypoxic_full_prof_inyear_rcp60['95%'], color='yellow', alpha=0.5)# ,  label= 'RCP6.0 90% CI')
ax1.plot(glue_80years_len_hypoxic_full_prof_inyear_rcp60.index.astype(float), glue_80years_len_hypoxic_full_prof_inyear_rcp60['50%'], 'yellow', alpha=0.9, linewidth=3  )#, label='RCP6.0 median'

ax1.fill_between(glue_80years_len_hypoxic_full_prof_inyear_rcp85.index.astype(float), glue_80years_len_hypoxic_full_prof_inyear_rcp85['5%'], glue_80years_len_hypoxic_full_prof_inyear_rcp85['95%'], color='r', alpha=0.2)# ,  label= 'RCP8.5 90% CI')
ax1.plot(glue_80years_len_hypoxic_full_prof_inyear_rcp85.index.astype(float), glue_80years_len_hypoxic_full_prof_inyear_rcp85['50%'], 'r', alpha=0.9, linewidth=3  )#, label='RCP8.5 median'

trendline_rcp60_len = autocorr_MK_org_modif_sens_slope_test(glue_80years_len_hypoxic_full_prof_inyear_rcp60['50%'])
ax1.text(2020, 170, f'y = {trendline_rcp60_len[-2]:.3f}x + {trendline_rcp60_len[-1]:.3f}, p-value < 0.0001', color='orange', fontsize=20 )

ax1.plot(glue_80years_len_hypoxic_full_prof_inyear_rcp60.index.astype(float),
        trendline_rcp60_len[-2] * np.arange(80) + trendline_rcp60_len[-1],
        linestyle='--', color='orange', alpha=0.9, linewidth=3)


trendline_rcp85_len = autocorr_MK_org_modif_sens_slope_test(glue_80years_len_hypoxic_full_prof_inyear_rcp85['50%'])
ax1.text(2020, 160, f'y = {trendline_rcp85_len[-2]:.3f}x + {trendline_rcp85_len[-1]:.3f}, p-value < 0.0001', color='red', fontsize=20 )


ax1.plot(glue_80years_len_hypoxic_full_prof_inyear_rcp85.index.astype(float),
        trendline_rcp85_len[-2] * np.arange(80) + trendline_rcp85_len[-1],
        linestyle='--', color='red', alpha=0.9, linewidth=3)# , label= 'RCP8.5 trendline')


ax1.set_ylabel('Duration of full deep hypoxia [d]' , fontsize=26)
ax1.set_xlabel('Year' , fontsize=26)
ax1.tick_params(axis='both', which='major', labelsize=22)
#ax1.legend(bbox_to_anchor=(0.7, -0.2), fontsize=22)
ax1.tick_params(axis='x', rotation=45, labelsize=22)




# Plotting the second subplot
ax2.fill_between(glue_80years_first_jday_hypoxic_full_prof_inyear_rcp26.index.astype(float), glue_80years_first_jday_hypoxic_full_prof_inyear_rcp26['5%'], glue_80years_first_jday_hypoxic_full_prof_inyear_rcp26['95%'], color='darkgreen', alpha=0.3 ,  label= 'RCP2.6 90% CI')
ax2.plot(glue_80years_first_jday_hypoxic_full_prof_inyear_rcp26.index.astype(float), glue_80years_first_jday_hypoxic_full_prof_inyear_rcp26['50%'], 'darkgreen', label='RCP2.6 median', alpha=0.9, linewidth=3  )

ax2.fill_between(glue_80years_first_jday_hypoxic_full_prof_inyear_rcp60.index.astype(float), glue_80years_first_jday_hypoxic_full_prof_inyear_rcp60['5%'], glue_80years_first_jday_hypoxic_full_prof_inyear_rcp60['95%'], color='yellow', alpha=0.5 ,  label= 'RCP6.0 90% CI')
ax2.plot(glue_80years_first_jday_hypoxic_full_prof_inyear_rcp60.index.astype(float), glue_80years_first_jday_hypoxic_full_prof_inyear_rcp60['50%'], 'yellow', label='RCP6.0 median', alpha=0.9, linewidth=3  )

ax2.fill_between(glue_80years_first_jday_hypoxic_full_prof_inyear_rcp85.index.astype(float), glue_80years_first_jday_hypoxic_full_prof_inyear_rcp85['5%'], glue_80years_first_jday_hypoxic_full_prof_inyear_rcp85['95%'], color='r', alpha=0.2 ,  label= 'RCP8.5 90% CI')
ax2.plot(glue_80years_first_jday_hypoxic_full_prof_inyear_rcp85.index.astype(float), glue_80years_first_jday_hypoxic_full_prof_inyear_rcp85['50%'], 'r', label='RCP8.5 median', alpha=0.9, linewidth=3  )

trendline_rcp60_first = autocorr_MK_org_modif_sens_slope_test(glue_80years_first_jday_hypoxic_full_prof_inyear_rcp60['50%'])
ax2.text(2020, 110, f'y = {trendline_rcp60_first[-2]:.3f}x + {trendline_rcp60_first[-1]:.3f}, p-value < 0.0001', color='orange', fontsize=20 )

ax2.plot(glue_80years_first_jday_hypoxic_full_prof_inyear_rcp60.index.astype(float),
        trendline_rcp60_first[-2] * np.arange(80) + trendline_rcp60_first[-1],
        linestyle='--', color='orange', alpha=0.9, linewidth=3, label= 'RCP6.0 trendline')

trendline_rcp85_first = autocorr_MK_org_modif_sens_slope_test(glue_80years_first_jday_hypoxic_full_prof_inyear_rcp85['50%'])
ax2.text(2020, 100, f'y = {trendline_rcp85_first[-2]:.3f}x + {trendline_rcp85_first[-1]:.3f}, p-value < 0.0001', color='red', fontsize=20 )

ax2.plot(glue_80years_first_jday_hypoxic_full_prof_inyear_rcp85.index.astype(float),
        trendline_rcp85_first[-2] * np.arange(80) + trendline_rcp85_first[-1],
        linestyle='--', color='red', alpha=0.9, linewidth=3 , label= 'RCP8.5 trendline')

ax2.set_ylabel('First day of full deep hypoxia in year [Jd]' , fontsize=26)
ax2.set_xlabel('Year' , fontsize=26)
ax2.tick_params(axis='both', which='major', labelsize=22)
#ax2.legend(bbox_to_anchor=(0.7, -0.2), fontsize=22)
ax2.tick_params(axis='x', rotation=45, labelsize=22)

plt.subplots_adjust(wspace=0.4)
# Collecting handles and labels from both subplots

#fig.legend(handles, labels, loc='lower center', fontsize=16, ncol=3, bbox_to_anchor=(0.5, -0.2), fontsize=22)
fig.legend( loc='lower center', ncol=4, bbox_to_anchor=(0.5, -0.2), prop={'size': 22})

plt.subplots_adjust(wspace=0.3)

# Saving the figure
plt.savefig('GLUE_Timeseries_full_hypoxic_duration_first_len_full_hypoxic_80years.png', bbox_inches='tight')




#%% anormally plot of first Jda and length of full hypoxic profile 


import os
import matplotlib.pyplot as plt

# Change directory
os.chdir('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/')

# Create a figure and axes for subplots
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(25, 10))

# Plotting the first subplot
ax1 = axes[0]
ax1.fill_between(glue_first_jday_hypoxic_full_prof_inyear_his[(1975 < glue_first_jday_hypoxic_full_prof_inyear_his.index)].index.astype(float),
                 glue_first_jday_hypoxic_full_prof_inyear_his[(1975 < glue_first_jday_hypoxic_full_prof_inyear_his.index)]['5%'] - first_jday_hypoxic_full_prof_inyear_ref,
                 glue_first_jday_hypoxic_full_prof_inyear_his[(1975 < glue_first_jday_hypoxic_full_prof_inyear_his.index)]['95%'] - first_jday_hypoxic_full_prof_inyear_ref,
                 color='grey', alpha=0.2, label='His 90% CI')

ax1.plot(glue_first_jday_hypoxic_full_prof_inyear_his[(1975 < glue_first_jday_hypoxic_full_prof_inyear_his.index)].index.astype(float),
         glue_first_jday_hypoxic_full_prof_inyear_his[(1975 < glue_first_jday_hypoxic_full_prof_inyear_his.index)]['50%'] - first_jday_hypoxic_full_prof_inyear_ref,
         'k', label='His median', alpha=0.9, linewidth=3)

ax1.fill_between(glue_first_jday_hypoxic_full_prof_inyear_rcp26.index.astype(float), glue_first_jday_hypoxic_full_prof_inyear_rcp26['5%'] - first_jday_hypoxic_full_prof_inyear_ref, glue_first_jday_hypoxic_full_prof_inyear_rcp26['95%'] - first_jday_hypoxic_full_prof_inyear_ref, color='darkgreen', alpha=0.3, label='RCP6.0 90% CI')

ax1.plot(glue_first_jday_hypoxic_full_prof_inyear_rcp26.index.astype(float), glue_first_jday_hypoxic_full_prof_inyear_rcp26['50%'] - first_jday_hypoxic_full_prof_inyear_ref, 'darkgreen', label='RCP6.0 median', alpha=0.9, linewidth=3)

ax1.fill_between(glue_first_jday_hypoxic_full_prof_inyear_rcp60.index.astype(float), glue_first_jday_hypoxic_full_prof_inyear_rcp60['5%'] - first_jday_hypoxic_full_prof_inyear_ref, glue_first_jday_hypoxic_full_prof_inyear_rcp60['95%'] - first_jday_hypoxic_full_prof_inyear_ref, color='yellow', alpha=0.5, label='RCP6.0 90% CI')

ax1.plot(glue_first_jday_hypoxic_full_prof_inyear_rcp60.index.astype(float), glue_first_jday_hypoxic_full_prof_inyear_rcp60['50%'] - first_jday_hypoxic_full_prof_inyear_ref, 'yellow', label='RCP6.0 median', alpha=0.9, linewidth=3)

ax1.fill_between(glue_first_jday_hypoxic_full_prof_inyear_rcp85.index.astype(float), glue_first_jday_hypoxic_full_prof_inyear_rcp85['5%'] - first_jday_hypoxic_full_prof_inyear_ref, glue_first_jday_hypoxic_full_prof_inyear_rcp85['95%'] - first_jday_hypoxic_full_prof_inyear_ref, color='r', alpha=0.2, label='RCP8.5 90% CI')

ax1.plot(glue_first_jday_hypoxic_full_prof_inyear_rcp85.index.astype(float), glue_first_jday_hypoxic_full_prof_inyear_rcp85['50%'] - first_jday_hypoxic_full_prof_inyear_ref, 'r', label='RCP8.5 median', alpha=0.9, linewidth=3)

ax1.set_ylabel('Anomaly of first day of full deep hypoxia [Jd]', fontsize=26)
ax1.set_xlabel('Year', fontsize=26)
ax1.tick_params(axis='y', labelsize=22)
ax1.tick_params(axis='x', rotation=45, labelsize=22)

# Plotting the second subplot
ax2 = axes[1]
ax2.fill_between(glue_len_hypoxic_full_prof_inyear_his[(1975 < glue_len_hypoxic_full_prof_inyear_his.index)].index.astype(float),
                 glue_len_hypoxic_full_prof_inyear_his[(1975 < glue_len_hypoxic_full_prof_inyear_his.index)]['5%'] - len_hypoxic_full_prof_inyear_ref,
                 glue_len_hypoxic_full_prof_inyear_his[(1975 < glue_len_hypoxic_full_prof_inyear_his.index)]['95%'] - len_hypoxic_full_prof_inyear_ref,
                 color='grey', alpha=0.2)#, label='His 90% CI')

ax2.plot(glue_len_hypoxic_full_prof_inyear_his[(1975 < glue_len_hypoxic_full_prof_inyear_his.index)].index.astype(float),
          glue_len_hypoxic_full_prof_inyear_his[(1975 < glue_len_hypoxic_full_prof_inyear_his.index)]['50%'] - len_hypoxic_full_prof_inyear_ref,
          'k', alpha=0.9, linewidth=3)

ax2.fill_between(glue_len_hypoxic_full_prof_inyear_rcp26.index.astype(float), glue_len_hypoxic_full_prof_inyear_rcp26['5%'] - len_hypoxic_full_prof_inyear_ref, glue_len_hypoxic_full_prof_inyear_rcp26['95%'] - len_hypoxic_full_prof_inyear_ref, color='darkgreen', alpha=0.3)#, label='RCP6.0 90% CI')

ax2.plot(glue_len_hypoxic_full_prof_inyear_rcp26.index.astype(float), glue_len_hypoxic_full_prof_inyear_rcp26['50%'] - len_hypoxic_full_prof_inyear_ref, 'darkgreen',alpha=0.9, linewidth=3)

ax2.fill_between(glue_len_hypoxic_full_prof_inyear_rcp60.index.astype(float), glue_len_hypoxic_full_prof_inyear_rcp60['5%'] - len_hypoxic_full_prof_inyear_ref, glue_len_hypoxic_full_prof_inyear_rcp60['95%'] - len_hypoxic_full_prof_inyear_ref, color='yellow', alpha=0.5)#, label='RCP6.0 90% CI')

ax2.plot(glue_len_hypoxic_full_prof_inyear_rcp60.index.astype(float), glue_len_hypoxic_full_prof_inyear_rcp60['50%'] - len_hypoxic_full_prof_inyear_ref, 'yellow', alpha=0.9, linewidth=3)

ax2.fill_between(glue_len_hypoxic_full_prof_inyear_rcp85.index.astype(float), glue_len_hypoxic_full_prof_inyear_rcp85['5%'] - len_hypoxic_full_prof_inyear_ref, glue_len_hypoxic_full_prof_inyear_rcp85['95%'] - len_hypoxic_full_prof_inyear_ref, color='r', alpha=0.2)#, label='RCP8.5 90% CI')

ax2.plot(glue_len_hypoxic_full_prof_inyear_rcp85.index.astype(float), glue_len_hypoxic_full_prof_inyear_rcp85['50%'] - len_hypoxic_full_prof_inyear_ref, 'r',  alpha=0.9, linewidth=3)

ax2.set_ylabel('Anomaly of full deep hypoxia duration [d]', fontsize=26)
ax2.set_xlabel('Year', fontsize=26)
ax2.tick_params(axis='y', labelsize=22)
ax2.tick_params(axis='x', rotation=45, labelsize=22)

# Legend for both subplots
fig.legend(loc='upper center', bbox_to_anchor=(0.5, -0.01), shadow=True, ncol=4, fontsize=22)

# Save the figure
fig.savefig("Anomaly_first_jday_duration_full_hypoxic_profile.png", dpi=300, bbox_inches='tight')
plt.show()



#%% value plot of first Jda and length of full hypoxic profile 


import os
import matplotlib.pyplot as plt

# Change directory
os.chdir('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/')

# Create a figure and axes for subplots
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(25, 10))

# Plotting the first subplot
ax1 = axes[0]
ax1.fill_between(glue_first_jday_hypoxic_full_prof_inyear_his.index.astype(float),
                 glue_first_jday_hypoxic_full_prof_inyear_his['5%'],
                 glue_first_jday_hypoxic_full_prof_inyear_his['95%'],
                 color='grey', alpha=0.2, label='His 90% CI')

ax1.plot(glue_first_jday_hypoxic_full_prof_inyear_his.index.astype(float),
         glue_first_jday_hypoxic_full_prof_inyear_his['50%'],
         'k', label='His median', alpha=0.9, linewidth=3)

ax1.fill_between(glue_first_jday_hypoxic_full_prof_inyear_rcp26.index.astype(float), glue_first_jday_hypoxic_full_prof_inyear_rcp26['5%'], glue_first_jday_hypoxic_full_prof_inyear_rcp26['95%'], color='darkgreen', alpha=0.3, label='RCP6.0 90% CI')

ax1.plot(glue_first_jday_hypoxic_full_prof_inyear_rcp26.index.astype(float), glue_first_jday_hypoxic_full_prof_inyear_rcp26['50%'], 'darkgreen', label='RCP6.0 median', alpha=0.9, linewidth=3)

ax1.fill_between(glue_first_jday_hypoxic_full_prof_inyear_rcp60.index.astype(float), glue_first_jday_hypoxic_full_prof_inyear_rcp60['5%'], glue_first_jday_hypoxic_full_prof_inyear_rcp60['95%'], color='yellow', alpha=0.5, label='RCP6.0 90% CI')

ax1.plot(glue_first_jday_hypoxic_full_prof_inyear_rcp60.index.astype(float), glue_first_jday_hypoxic_full_prof_inyear_rcp60['50%'], 'yellow', label='RCP6.0 median', alpha=0.9, linewidth=3)

ax1.fill_between(glue_first_jday_hypoxic_full_prof_inyear_rcp85.index.astype(float), glue_first_jday_hypoxic_full_prof_inyear_rcp85['5%'], glue_first_jday_hypoxic_full_prof_inyear_rcp85['95%'], color='r', alpha=0.2, label='RCP8.5 90% CI')

ax1.plot(glue_first_jday_hypoxic_full_prof_inyear_rcp85.index.astype(float), glue_first_jday_hypoxic_full_prof_inyear_rcp85['50%'], 'r', label='RCP8.5 median', alpha=0.9, linewidth=3)

ax1.set_ylabel('First day of full deep hypoxia [Jd]', fontsize=26)
ax1.set_xlabel('Year', fontsize=26)
ax1.tick_params(axis='y', labelsize=22)
ax1.tick_params(axis='x', rotation=45, labelsize=22)

# Plotting the second subplot
ax2 = axes[1]
ax2.fill_between(glue_len_hypoxic_full_prof_inyear_his.index.astype(float),
                 glue_len_hypoxic_full_prof_inyear_his['5%'] ,
                 glue_len_hypoxic_full_prof_inyear_his['95%'] ,
                 color='grey', alpha=0.2)#, label='His 90% CI')

ax2.plot(glue_len_hypoxic_full_prof_inyear_his.index.astype(float),
          glue_len_hypoxic_full_prof_inyear_his['50%'] ,
          'k', alpha=0.9, linewidth=3)

ax2.fill_between(glue_len_hypoxic_full_prof_inyear_rcp26.index.astype(float), glue_len_hypoxic_full_prof_inyear_rcp26['5%'] , glue_len_hypoxic_full_prof_inyear_rcp26['95%'] , color='darkgreen', alpha=0.3)#, label='RCP6.0 90% CI')

ax2.plot(glue_len_hypoxic_full_prof_inyear_rcp26.index.astype(float), glue_len_hypoxic_full_prof_inyear_rcp26['50%'] , 'darkgreen',alpha=0.9, linewidth=3)

ax2.fill_between(glue_len_hypoxic_full_prof_inyear_rcp60.index.astype(float), glue_len_hypoxic_full_prof_inyear_rcp60['5%'] , glue_len_hypoxic_full_prof_inyear_rcp60['95%'] , color='yellow', alpha=0.5)#, label='RCP6.0 90% CI')

ax2.plot(glue_len_hypoxic_full_prof_inyear_rcp60.index.astype(float), glue_len_hypoxic_full_prof_inyear_rcp60['50%'] , 'yellow', alpha=0.9, linewidth=3)

ax2.fill_between(glue_len_hypoxic_full_prof_inyear_rcp85.index.astype(float), glue_len_hypoxic_full_prof_inyear_rcp85['5%'] , glue_len_hypoxic_full_prof_inyear_rcp85['95%'] , color='r', alpha=0.2)#, label='RCP8.5 90% CI')

ax2.plot(glue_len_hypoxic_full_prof_inyear_rcp85.index.astype(float), glue_len_hypoxic_full_prof_inyear_rcp85['50%'] , 'r',  alpha=0.9, linewidth=3)

ax2.set_ylabel('Full deep hypoxia duration [d]', fontsize=26)
ax2.set_xlabel('Year', fontsize=26)
ax2.tick_params(axis='y', labelsize=22)
ax2.tick_params(axis='x', rotation=45, labelsize=22)

# Legend for both subplots
fig.legend(loc='upper center', bbox_to_anchor=(0.5, -0.01), shadow=True, ncol=4, fontsize=22)

# Save the figure
fig.savefig("First_jday_duration_full_hypoxic_profile.png", dpi=300, bbox_inches='tight')
plt.show()




#%%

import os
import matplotlib.pyplot as plt

# Change directory
os.chdir('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/')

# Create a figure and axes for subplots
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(25, 10))

# Plotting the first subplot
ax1 = axes[0]
ax1.fill_between(glue_first_jday_hypoxic_full_prof_inyear_his.index.astype(float),
                 glue_first_jday_hypoxic_full_prof_inyear_his['5%'],
                 glue_first_jday_hypoxic_full_prof_inyear_his['95%'],
                 color='grey', alpha=0.2, label='His 90% CI')

ax1.plot(glue_first_jday_hypoxic_full_prof_inyear_his.index.astype(float),
         glue_first_jday_hypoxic_full_prof_inyear_his['50%'],
         'k', label='His median', alpha=0.9, linewidth=3)

ax1.fill_between(glue_first_jday_hypoxic_full_prof_inyear_rcp26.index.astype(float), glue_first_jday_hypoxic_full_prof_inyear_rcp26['5%'], glue_first_jday_hypoxic_full_prof_inyear_rcp26['95%'], color='darkgreen', alpha=0.3, label='RCP6.0 90% CI')

ax1.plot(glue_first_jday_hypoxic_full_prof_inyear_rcp26.index.astype(float), glue_first_jday_hypoxic_full_prof_inyear_rcp26['50%'], 'darkgreen', label='RCP6.0 median', alpha=0.9, linewidth=3)

ax1.fill_between(glue_first_jday_hypoxic_full_prof_inyear_rcp60.index.astype(float), glue_first_jday_hypoxic_full_prof_inyear_rcp60['5%'], glue_first_jday_hypoxic_full_prof_inyear_rcp60['95%'], color='yellow', alpha=0.5, label='RCP6.0 90% CI')

ax1.plot(glue_first_jday_hypoxic_full_prof_inyear_rcp60.index.astype(float), glue_first_jday_hypoxic_full_prof_inyear_rcp60['50%'], 'yellow', label='RCP6.0 median', alpha=0.9, linewidth=3)

ax1.fill_between(glue_first_jday_hypoxic_full_prof_inyear_rcp85.index.astype(float), glue_first_jday_hypoxic_full_prof_inyear_rcp85['5%'], glue_first_jday_hypoxic_full_prof_inyear_rcp85['95%'], color='r', alpha=0.2, label='RCP8.5 90% CI')

ax1.plot(glue_first_jday_hypoxic_full_prof_inyear_rcp85.index.astype(float), glue_first_jday_hypoxic_full_prof_inyear_rcp85['50%'], 'r', label='RCP8.5 median', alpha=0.9, linewidth=3)



trendline_his=autocorr_MK_org_modif_sens_slope_test(glue_first_jday_hypoxic_full_prof_inyear_his['50%'])

trendline_rcp26=autocorr_MK_org_modif_sens_slope_test(glue_first_jday_hypoxic_full_prof_inyear_rcp26['50%'])

trendline_rcp60=autocorr_MK_org_modif_sens_slope_test(glue_first_jday_hypoxic_full_prof_inyear_rcp60['50%'])

trendline_rcp85=autocorr_MK_org_modif_sens_slope_test(glue_first_jday_hypoxic_full_prof_inyear_rcp85['50%'])




ax1.text(1900, 165, f'y = {trendline_rcp60[-2]:.3f}x + {trendline_rcp60[-1]:.3f}, p = {trendline_rcp60[-3]:.3f}', color='gold', fontsize= 20 )

ax1.plot(glue_first_jday_hypoxic_full_prof_inyear_rcp60.index.astype(float),
        trendline_rcp60[-2] * np.arange(94) + trendline_rcp60[-1],
        linestyle='--', color='yellow', alpha=0.9, linewidth=3)



ax1.text(1900, 160, f'y = {trendline_rcp85[-2]:.3f}x + {trendline_rcp85[-1]:.3f}, p = {trendline_rcp85[-3]:.3f}', color='red', fontsize= 20 )

ax1.plot(glue_first_jday_hypoxic_full_prof_inyear_rcp85.index.astype(float),
        trendline_rcp85[-2] * np.arange(94) + trendline_rcp85[-1],
        linestyle='--', color='red', alpha=0.9, linewidth=3)




ax1.set_ylabel('First day of full deep hypoxia [Jd]', fontsize=26)
ax1.set_xlabel('Year', fontsize=26)
ax1.tick_params(axis='y', labelsize=22)
ax1.tick_params(axis='x', rotation=45, labelsize=22)

# Plotting the second subplot
ax2 = axes[1]
ax2.fill_between(glue_len_hypoxic_full_prof_inyear_his.index.astype(float),
                 glue_len_hypoxic_full_prof_inyear_his['5%'] ,
                 glue_len_hypoxic_full_prof_inyear_his['95%'] ,
                 color='grey', alpha=0.2)#, label='His 90% CI')

ax2.plot(glue_len_hypoxic_full_prof_inyear_his.index.astype(float),
          glue_len_hypoxic_full_prof_inyear_his['50%'] ,
          'k', alpha=0.9, linewidth=3)

ax2.fill_between(glue_len_hypoxic_full_prof_inyear_rcp26.index.astype(float), glue_len_hypoxic_full_prof_inyear_rcp26['5%'] , glue_len_hypoxic_full_prof_inyear_rcp26['95%'] , color='darkgreen', alpha=0.3)#, label='RCP6.0 90% CI')

ax2.plot(glue_len_hypoxic_full_prof_inyear_rcp26.index.astype(float), glue_len_hypoxic_full_prof_inyear_rcp26['50%'] , 'darkgreen',alpha=0.9, linewidth=3)

ax2.fill_between(glue_len_hypoxic_full_prof_inyear_rcp60.index.astype(float), glue_len_hypoxic_full_prof_inyear_rcp60['5%'] , glue_len_hypoxic_full_prof_inyear_rcp60['95%'] , color='yellow', alpha=0.5)#, label='RCP6.0 90% CI')

ax2.plot(glue_len_hypoxic_full_prof_inyear_rcp60.index.astype(float), glue_len_hypoxic_full_prof_inyear_rcp60['50%'] , 'yellow', alpha=0.9, linewidth=3)

ax2.fill_between(glue_len_hypoxic_full_prof_inyear_rcp85.index.astype(float), glue_len_hypoxic_full_prof_inyear_rcp85['5%'] , glue_len_hypoxic_full_prof_inyear_rcp85['95%'] , color='r', alpha=0.2)#, label='RCP8.5 90% CI')

ax2.plot(glue_len_hypoxic_full_prof_inyear_rcp85.index.astype(float), glue_len_hypoxic_full_prof_inyear_rcp85['50%'] , 'r',  alpha=0.9, linewidth=3)




trendline_his=autocorr_MK_org_modif_sens_slope_test(glue_len_hypoxic_full_prof_inyear_his['50%'])

trendline_rcp26=autocorr_MK_org_modif_sens_slope_test(glue_len_hypoxic_full_prof_inyear_rcp26['50%'])

trendline_rcp60=autocorr_MK_org_modif_sens_slope_test(glue_len_hypoxic_full_prof_inyear_rcp60['50%'])

trendline_rcp85=autocorr_MK_org_modif_sens_slope_test(glue_len_hypoxic_full_prof_inyear_rcp85['50%'])


ax2.text(1900,90, f'y = {trendline_rcp26[-2]:.3f}x + {trendline_rcp26[-1]:.3f}, p = {trendline_rcp26[-3]:.3f}', color='green', fontsize= 20 )

ax2.plot(glue_len_hypoxic_full_prof_inyear_rcp26.index.astype(float),
        trendline_rcp26[-2] * np.arange(94) + trendline_rcp26[-1],
        linestyle='--', color='darkgreen', alpha=0.9, linewidth=3)



ax2.text(1900, 85, f'y = {trendline_rcp60[-2]:.3f}x + {trendline_rcp60[-1]:.3f}, p = {trendline_rcp60[-3]:.3f}', color='gold', fontsize= 20 )

ax2.plot(glue_len_hypoxic_full_prof_inyear_rcp60.index.astype(float),
        trendline_rcp60[-2] * np.arange(94) + trendline_rcp60[-1],
        linestyle='--', color='yellow', alpha=0.9, linewidth=3)



ax2.text(1900, 80, f'y = {trendline_rcp85[-2]:.3f}x + {trendline_rcp85[-1]:.3f}, p = {trendline_rcp85[-3]:.3f}', color='red', fontsize= 20 )

ax2.plot(glue_len_hypoxic_full_prof_inyear_rcp85.index.astype(float),
        trendline_rcp85[-2] * np.arange(94) + trendline_rcp85[-1],
        linestyle='--', color='red', alpha=0.9, linewidth=3)



ax2.set_ylabel('Full deep hypoxia duration [d]', fontsize=26)
ax2.set_xlabel('Year', fontsize=26)
ax2.tick_params(axis='y', labelsize=22)
ax2.tick_params(axis='x', rotation=45, labelsize=22)

# Legend for both subplots
fig.legend(loc='upper center', bbox_to_anchor=(0.5, -0.01), shadow=True, ncol=4, fontsize=22)

# Save the figure
fig.savefig("First_jday_duration_full_hypoxic_profile_withtrendline.png", dpi=300, bbox_inches='tight')
plt.show()










