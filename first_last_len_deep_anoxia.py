# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 16:54:58 2023

@author: mahta
"""



#%% Jday of first & last & length of deep anoxic condition 
#%%his


# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/his'
all_first_jday_anoxic_deep_prof_inyear_his= pd.DataFrame([])
all_last_jday_anoxic_deep_prof_inyear_his= pd.DataFrame([])
all_len_anoxic_deep_prof_inyear_his= pd.DataFrame([])
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
        
        
        first_jday_anoxic_deep_prof_inyear_his=first_last_len_anoxic_deep_inyear  (C, Vr, time_series, threshold=0.5)[1]
        last_jday_anoxic_deep_prof_inyear_his=first_last_len_anoxic_deep_inyear  (C, Vr, time_series, threshold=0.5)[3]
        len_anoxic_deep_prof_inyear_his=first_last_len_anoxic_deep_inyear  (C, Vr, time_series, threshold=0.5)[4]
        

        all_first_jday_anoxic_deep_prof_inyear_his = pd.concat([all_first_jday_anoxic_deep_prof_inyear_his , first_jday_anoxic_deep_prof_inyear_his], axis=1)
        all_last_jday_anoxic_deep_prof_inyear_his = pd.concat([all_last_jday_anoxic_deep_prof_inyear_his , last_jday_anoxic_deep_prof_inyear_his], axis=1)
        all_len_anoxic_deep_prof_inyear_his = pd.concat([all_len_anoxic_deep_prof_inyear_his , len_anoxic_deep_prof_inyear_his], axis=1)



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
        
        
        first_jday_anoxic_deep_prof_inyear_his=first_last_len_anoxic_deep_inyear  (C, Vr, time_series, threshold=0.5)[1]
        last_jday_anoxic_deep_prof_inyear_his=first_last_len_anoxic_deep_inyear  (C, Vr, time_series, threshold=0.5)[3]
        len_anoxic_deep_prof_inyear_his=first_last_len_anoxic_deep_inyear  (C, Vr, time_series, threshold=0.5)[4]
        

        all_first_jday_anoxic_deep_prof_inyear_his = pd.concat([all_first_jday_anoxic_deep_prof_inyear_his , first_jday_anoxic_deep_prof_inyear_his], axis=1)
        all_last_jday_anoxic_deep_prof_inyear_his = pd.concat([all_last_jday_anoxic_deep_prof_inyear_his , last_jday_anoxic_deep_prof_inyear_his], axis=1)
        all_len_anoxic_deep_prof_inyear_his = pd.concat([all_len_anoxic_deep_prof_inyear_his , len_anoxic_deep_prof_inyear_his], axis=1)


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
        
        
        first_jday_anoxic_deep_prof_inyear_his=first_last_len_anoxic_deep_inyear  (C, Vr, time_series, threshold=0.5)[1]
        last_jday_anoxic_deep_prof_inyear_his=first_last_len_anoxic_deep_inyear  (C, Vr, time_series, threshold=0.5)[3]
        len_anoxic_deep_prof_inyear_his=first_last_len_anoxic_deep_inyear  (C, Vr, time_series, threshold=0.5)[4]
        

        all_first_jday_anoxic_deep_prof_inyear_his = pd.concat([all_first_jday_anoxic_deep_prof_inyear_his , first_jday_anoxic_deep_prof_inyear_his], axis=1)
        all_last_jday_anoxic_deep_prof_inyear_his = pd.concat([all_last_jday_anoxic_deep_prof_inyear_his , last_jday_anoxic_deep_prof_inyear_his], axis=1)
        all_len_anoxic_deep_prof_inyear_his = pd.concat([all_len_anoxic_deep_prof_inyear_his , len_anoxic_deep_prof_inyear_his], axis=1)


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
        
        
        first_jday_anoxic_deep_prof_inyear_his=first_last_len_anoxic_deep_inyear  (C, Vr, time_series, threshold=0.5)[1]
        last_jday_anoxic_deep_prof_inyear_his=first_last_len_anoxic_deep_inyear  (C, Vr, time_series, threshold=0.5)[3]
        len_anoxic_deep_prof_inyear_his=first_last_len_anoxic_deep_inyear  (C, Vr, time_series, threshold=0.5)[4]
        

        all_first_jday_anoxic_deep_prof_inyear_his = pd.concat([all_first_jday_anoxic_deep_prof_inyear_his , first_jday_anoxic_deep_prof_inyear_his], axis=1)
        all_last_jday_anoxic_deep_prof_inyear_his = pd.concat([all_last_jday_anoxic_deep_prof_inyear_his , last_jday_anoxic_deep_prof_inyear_his], axis=1)
        all_len_anoxic_deep_prof_inyear_his = pd.concat([all_len_anoxic_deep_prof_inyear_his , len_anoxic_deep_prof_inyear_his], axis=1)

#%%annova_uncertainity_his 
all_first_jday_anoxic_deep_prof_inyear_his=all_first_jday_anoxic_deep_prof_inyear_his.replace(0, np.nan)

anova_first_jday_anoxic_deep_prof_his=annova_uncertainity(all_first_jday_anoxic_deep_prof_inyear_his)

anova_first_jday_anoxic_deep_prof_his.describe().loc['mean', :]
"""
GCMs             60.762731
param            37.459464
interaction       1.777805
GCMs/param        3.546097
year           1933.000000
Name: mean, dtype: float64
"""

anova_first_jday_anoxic_deep_prof_his.describe().loc['std', :]
"""
GCMs           20.478780
param          20.839016
interaction     2.912749
GCMs/param      8.596057
year           42.001984

"""

all_last_jday_anoxic_deep_prof_inyear_his=all_last_jday_anoxic_deep_prof_inyear_his.replace(0, np.nan)

anova_last_jday_anoxic_deep_prof_his=annova_uncertainity(all_last_jday_anoxic_deep_prof_inyear_his)

anova_last_jday_anoxic_deep_prof_his.describe().loc['mean', :]
"""
GCMs             99.648245
param             0.531892
interaction      -0.180137
GCMs/param             inf
year           1933.000000
Name: mean, dtype: float64
"""


anova_last_jday_anoxic_deep_prof_his.describe().loc['std', :]

"""
GCMs            4.235693
param           2.441643
interaction     3.497959
GCMs/param           NaN
year           42.001984
Name: std, dtype: float64
"""



anova_len_jday_anoxic_deep_prof_his=annova_uncertainity(all_len_anoxic_deep_prof_inyear_his)

anova_len_jday_anoxic_deep_prof_his.describe().loc['mean', :]
"""
GCMs             67.977982
param            30.913088
interaction       1.108930
GCMs/param        4.508759
year           1933.000000
Name: mean, dtype: float64
"""


anova_len_jday_anoxic_deep_prof_his.describe().loc['std', :]
"""
GCMs           19.705277
param          19.293568
interaction     1.411545
GCMs/param      5.370804
year           42.001984
Name: std, dtype: float64
"""


#%%rcp26


# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp26'
all_first_jday_anoxic_deep_prof_inyear_rcp26= pd.DataFrame([])
all_last_jday_anoxic_deep_prof_inyear_rcp26= pd.DataFrame([])
all_len_anoxic_deep_prof_inyear_rcp26= pd.DataFrame([])
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
        
        
        first_jday_anoxic_deep_prof_inyear_rcp26=first_last_len_anoxic_deep_inyear  (C, Vr, time_series, threshold=0.5)[1]
        last_jday_anoxic_deep_prof_inyear_rcp26=first_last_len_anoxic_deep_inyear  (C, Vr, time_series, threshold=0.5)[3]
        len_anoxic_deep_prof_inyear_rcp26=first_last_len_anoxic_deep_inyear  (C, Vr, time_series, threshold=0.5)[4]
        

        all_first_jday_anoxic_deep_prof_inyear_rcp26 = pd.concat([all_first_jday_anoxic_deep_prof_inyear_rcp26 , first_jday_anoxic_deep_prof_inyear_rcp26], axis=1)
        all_last_jday_anoxic_deep_prof_inyear_rcp26 = pd.concat([all_last_jday_anoxic_deep_prof_inyear_rcp26 , last_jday_anoxic_deep_prof_inyear_rcp26], axis=1)
        all_len_anoxic_deep_prof_inyear_rcp26 = pd.concat([all_len_anoxic_deep_prof_inyear_rcp26 , len_anoxic_deep_prof_inyear_rcp26], axis=1)


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
        
        
        first_jday_anoxic_deep_prof_inyear_rcp26=first_last_len_anoxic_deep_inyear  (C, Vr, time_series, threshold=0.5)[1]
        last_jday_anoxic_deep_prof_inyear_rcp26=first_last_len_anoxic_deep_inyear  (C, Vr, time_series, threshold=0.5)[3]
        len_anoxic_deep_prof_inyear_rcp26=first_last_len_anoxic_deep_inyear  (C, Vr, time_series, threshold=0.5)[4]
        

        all_first_jday_anoxic_deep_prof_inyear_rcp26 = pd.concat([all_first_jday_anoxic_deep_prof_inyear_rcp26 , first_jday_anoxic_deep_prof_inyear_rcp26], axis=1)
        all_last_jday_anoxic_deep_prof_inyear_rcp26 = pd.concat([all_last_jday_anoxic_deep_prof_inyear_rcp26 , last_jday_anoxic_deep_prof_inyear_rcp26], axis=1)
        all_len_anoxic_deep_prof_inyear_rcp26 = pd.concat([all_len_anoxic_deep_prof_inyear_rcp26 , len_anoxic_deep_prof_inyear_rcp26], axis=1)


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
        
        
        first_jday_anoxic_deep_prof_inyear_rcp26=first_last_len_anoxic_deep_inyear  (C, Vr, time_series, threshold=0.5)[1]
        last_jday_anoxic_deep_prof_inyear_rcp26=first_last_len_anoxic_deep_inyear  (C, Vr, time_series, threshold=0.5)[3]
        len_anoxic_deep_prof_inyear_rcp26=first_last_len_anoxic_deep_inyear  (C, Vr, time_series, threshold=0.5)[4]
        

        all_first_jday_anoxic_deep_prof_inyear_rcp26 = pd.concat([all_first_jday_anoxic_deep_prof_inyear_rcp26 , first_jday_anoxic_deep_prof_inyear_rcp26], axis=1)
        all_last_jday_anoxic_deep_prof_inyear_rcp26 = pd.concat([all_last_jday_anoxic_deep_prof_inyear_rcp26 , last_jday_anoxic_deep_prof_inyear_rcp26], axis=1)
        all_len_anoxic_deep_prof_inyear_rcp26 = pd.concat([all_len_anoxic_deep_prof_inyear_rcp26 , len_anoxic_deep_prof_inyear_rcp26], axis=1)


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
        
        
        first_jday_anoxic_deep_prof_inyear_rcp26=first_last_len_anoxic_deep_inyear  (C, Vr, time_series, threshold=0.5)[1]
        last_jday_anoxic_deep_prof_inyear_rcp26=first_last_len_anoxic_deep_inyear  (C, Vr, time_series, threshold=0.5)[3]
        len_anoxic_deep_prof_inyear_rcp26=first_last_len_anoxic_deep_inyear  (C, Vr, time_series, threshold=0.5)[4]
        

        all_first_jday_anoxic_deep_prof_inyear_rcp26 = pd.concat([all_first_jday_anoxic_deep_prof_inyear_rcp26 , first_jday_anoxic_deep_prof_inyear_rcp26], axis=1)
        all_last_jday_anoxic_deep_prof_inyear_rcp26 = pd.concat([all_last_jday_anoxic_deep_prof_inyear_rcp26 , last_jday_anoxic_deep_prof_inyear_rcp26], axis=1)
        all_len_anoxic_deep_prof_inyear_rcp26 = pd.concat([all_len_anoxic_deep_prof_inyear_rcp26 , len_anoxic_deep_prof_inyear_rcp26], axis=1)

#%%annova_uncertainity_rcp26 

all_first_jday_anoxic_deep_prof_inyear_rcp26=all_first_jday_anoxic_deep_prof_inyear_rcp26.replace(0, np.nan)

anova_first_jday_anoxic_deep_prof_rcp26=annova_uncertainity(all_first_jday_anoxic_deep_prof_inyear_rcp26)

anova_first_jday_anoxic_deep_prof_rcp26.describe().loc['mean', :]
"""
GCMs             60.821982
param            38.201095
interaction       0.976923
GCMs/param        2.458457
year           2052.500000
Name: mean, dtype: float64
"""

anova_first_jday_anoxic_deep_prof_rcp26.describe().loc['std', :]
"""
GCMs           19.292018
param          19.266510
interaction     1.078287
GCMs/param      2.671773
year           27.279418
Name: std, dtype: float64

"""
all_last_jday_anoxic_deep_prof_inyear_rcp26=all_last_jday_anoxic_deep_prof_inyear_rcp26.replace(0, np.nan)


anova_last_jday_anoxic_deep_prof_rcp26=annova_uncertainity(all_last_jday_anoxic_deep_prof_inyear_rcp26)

anova_last_jday_anoxic_deep_prof_rcp26.describe().loc['mean', :]
"""
GCMs            100.000000
param             0.040627
interaction      -0.040627
GCMs/param             inf
year           2052.500000
Name: mean, dtype: float64
"""


anova_last_jday_anoxic_deep_prof_rcp26.describe().loc['std', :]

"""
GCMs           4.420791e-15
param          3.938941e-01
interaction    3.938941e-01
GCMs/param              NaN
year           2.727942e+01
Name: std, dtype: float64
"""



anova_len_jday_anoxic_deep_prof_rcp26=annova_uncertainity(all_len_anoxic_deep_prof_inyear_rcp26)

anova_len_jday_anoxic_deep_prof_rcp26.describe().loc['mean', :]
"""
GCMs             65.461433
param            33.655693
interaction       0.882874
GCMs/param        3.210500
year           2052.500000
"""


anova_len_jday_anoxic_deep_prof_rcp26.describe().loc['std', :]
"""
GCMs           19.952247
param          19.540054
interaction     1.140931
GCMs/param      3.229791
year           27.279418
Name: std, dtype: float64
"""
#%%annova_uncertainity_rcp26_80years

all_first_jday_anoxic_deep_prof_inyear_rcp26=all_first_jday_anoxic_deep_prof_inyear_rcp26.replace(0, np.nan)
anova_first_jday_anoxic_deep_prof_rcp26_80years=annova_uncertainity(all_first_jday_anoxic_deep_prof_inyear_rcp26[all_first_jday_anoxic_deep_prof_inyear_rcp26.index>2019])


anova_first_jday_anoxic_deep_prof_rcp26_80years.describe().loc['mean', :]
"""
GCMs             62.445515
param            36.556533
interaction       0.997953
GCMs/param        2.589388
year           2059.500000
Name: mean, dtype: float64
"""

anova_first_jday_anoxic_deep_prof_rcp26_80years.describe().loc['std', :]
"""
GCMs           18.227004
param          18.227201
interaction     1.147927
GCMs/param      2.799279
year           23.237900
Name: std, dtype: float64
"""




anova_len_jday_anoxic_deep_prof_rcp26_80years=annova_uncertainity(all_len_anoxic_deep_prof_inyear_rcp26[all_len_anoxic_deep_prof_inyear_rcp26.index>2019])

anova_len_jday_anoxic_deep_prof_rcp26_80years.describe().loc['mean', :]
"""
GCMs             67.033257
param            32.090202
interaction       0.876541
GCMs/param        3.417425
year           2059.500000
Name: mean, dtype: float64
"""


anova_len_jday_anoxic_deep_prof_rcp26_80years.describe().loc['std', :]
"""
GCMs           19.065506
param          18.704240
interaction     1.175567
GCMs/param      3.397873
year           23.237900
Name: std, dtype: float64
"""








#%%rcp60


# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp60'
all_first_jday_anoxic_deep_prof_inyear_rcp60= pd.DataFrame([])
all_last_jday_anoxic_deep_prof_inyear_rcp60= pd.DataFrame([])
all_len_anoxic_deep_prof_inyear_rcp60= pd.DataFrame([])
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
        
        
        first_jday_anoxic_deep_prof_inyear_rcp60=first_last_len_anoxic_deep_inyear  (C, Vr, time_series, threshold=0.5)[1]
        last_jday_anoxic_deep_prof_inyear_rcp60=first_last_len_anoxic_deep_inyear  (C, Vr, time_series, threshold=0.5)[3]
        len_anoxic_deep_prof_inyear_rcp60=first_last_len_anoxic_deep_inyear  (C, Vr, time_series, threshold=0.5)[4]
        

        all_first_jday_anoxic_deep_prof_inyear_rcp60 = pd.concat([all_first_jday_anoxic_deep_prof_inyear_rcp60 , first_jday_anoxic_deep_prof_inyear_rcp60], axis=1)
        all_last_jday_anoxic_deep_prof_inyear_rcp60 = pd.concat([all_last_jday_anoxic_deep_prof_inyear_rcp60 , last_jday_anoxic_deep_prof_inyear_rcp60], axis=1)
        all_len_anoxic_deep_prof_inyear_rcp60 = pd.concat([all_len_anoxic_deep_prof_inyear_rcp60 , len_anoxic_deep_prof_inyear_rcp60], axis=1)


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
        
        
        first_jday_anoxic_deep_prof_inyear_rcp60=first_last_len_anoxic_deep_inyear  (C, Vr, time_series, threshold=0.5)[1]
        last_jday_anoxic_deep_prof_inyear_rcp60=first_last_len_anoxic_deep_inyear  (C, Vr, time_series, threshold=0.5)[3]
        len_anoxic_deep_prof_inyear_rcp60=first_last_len_anoxic_deep_inyear  (C, Vr, time_series, threshold=0.5)[4]
        

        all_first_jday_anoxic_deep_prof_inyear_rcp60 = pd.concat([all_first_jday_anoxic_deep_prof_inyear_rcp60 , first_jday_anoxic_deep_prof_inyear_rcp60], axis=1)
        all_last_jday_anoxic_deep_prof_inyear_rcp60 = pd.concat([all_last_jday_anoxic_deep_prof_inyear_rcp60 , last_jday_anoxic_deep_prof_inyear_rcp60], axis=1)
        all_len_anoxic_deep_prof_inyear_rcp60 = pd.concat([all_len_anoxic_deep_prof_inyear_rcp60 , len_anoxic_deep_prof_inyear_rcp60], axis=1)


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
        
        
        first_jday_anoxic_deep_prof_inyear_rcp60=first_last_len_anoxic_deep_inyear  (C, Vr, time_series, threshold=0.5)[1]
        last_jday_anoxic_deep_prof_inyear_rcp60=first_last_len_anoxic_deep_inyear  (C, Vr, time_series, threshold=0.5)[3]
        len_anoxic_deep_prof_inyear_rcp60=first_last_len_anoxic_deep_inyear  (C, Vr, time_series, threshold=0.5)[4]
        

        all_first_jday_anoxic_deep_prof_inyear_rcp60 = pd.concat([all_first_jday_anoxic_deep_prof_inyear_rcp60 , first_jday_anoxic_deep_prof_inyear_rcp60], axis=1)
        all_last_jday_anoxic_deep_prof_inyear_rcp60 = pd.concat([all_last_jday_anoxic_deep_prof_inyear_rcp60 , last_jday_anoxic_deep_prof_inyear_rcp60], axis=1)
        all_len_anoxic_deep_prof_inyear_rcp60 = pd.concat([all_len_anoxic_deep_prof_inyear_rcp60 , len_anoxic_deep_prof_inyear_rcp60], axis=1)


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
        
        
        first_jday_anoxic_deep_prof_inyear_rcp60=first_last_len_anoxic_deep_inyear  (C, Vr, time_series, threshold=0.5)[1]
        last_jday_anoxic_deep_prof_inyear_rcp60=first_last_len_anoxic_deep_inyear  (C, Vr, time_series, threshold=0.5)[3]
        len_anoxic_deep_prof_inyear_rcp60=first_last_len_anoxic_deep_inyear  (C, Vr, time_series, threshold=0.5)[4]
        

        all_first_jday_anoxic_deep_prof_inyear_rcp60 = pd.concat([all_first_jday_anoxic_deep_prof_inyear_rcp60 , first_jday_anoxic_deep_prof_inyear_rcp60], axis=1)
        all_last_jday_anoxic_deep_prof_inyear_rcp60 = pd.concat([all_last_jday_anoxic_deep_prof_inyear_rcp60 , last_jday_anoxic_deep_prof_inyear_rcp60], axis=1)
        all_len_anoxic_deep_prof_inyear_rcp60 = pd.concat([all_len_anoxic_deep_prof_inyear_rcp60 , len_anoxic_deep_prof_inyear_rcp60], axis=1)


#%%annova_uncertainity_rcp60 


all_first_jday_anoxic_deep_prof_inyear_rcp60=all_first_jday_anoxic_deep_prof_inyear_rcp60.replace(0, np.nan)

anova_first_jday_anoxic_deep_prof_rcp60=annova_uncertainity(all_first_jday_anoxic_deep_prof_inyear_rcp60)

anova_first_jday_anoxic_deep_prof_rcp60.describe().loc['mean', :]
"""
GCMs             58.325590
param            40.364895
interaction       1.309515
GCMs/param        2.360479
year           2052.500000
Name: mean, dtype: float64
"""

anova_first_jday_anoxic_deep_prof_rcp60.describe().loc['std', :]
"""
GCMs           22.030395
param          21.370573
interaction     2.500340
GCMs/param      2.392298
year           27.279418
Name: std, dtype: float64
"""
all_last_jday_anoxic_deep_prof_inyear_rcp60= all_last_jday_anoxic_deep_prof_inyear_rcp60.replace(0, np.nan)

anova_last_jday_anoxic_deep_prof_rcp60=annova_uncertainity(all_last_jday_anoxic_deep_prof_inyear_rcp60)

anova_last_jday_anoxic_deep_prof_rcp60.describe().loc['mean', :]
"""
GCMs            100.000000
param             0.043445
interaction      -0.043445
GCMs/param             inf
year           2052.500000
Name: mean, dtype: float64

"""


anova_last_jday_anoxic_deep_prof_rcp60.describe().loc['std', :]

"""
GCMs           7.367985e-15
param          2.981198e-01
interaction    2.981198e-01
GCMs/param              NaN
year           2.727942e+01
Name: std, dtype: float64
"""



anova_len_jday_anoxic_deep_prof_rcp60=annova_uncertainity(all_len_anoxic_deep_prof_inyear_rcp60)

anova_len_jday_anoxic_deep_prof_rcp60.describe().loc['mean', :]
"""
GCMs             70.250514
param            28.866986
interaction       0.882499
GCMs/param        4.452638
year           2052.500000
Name: mean, dtype: float64
"""


anova_len_jday_anoxic_deep_prof_rcp60.describe().loc['std', :]
"""
GCMs           19.239140
param          18.670917
interaction     1.276650
GCMs/param      4.647413
year           27.279418
Name: std, dtype: float64
"""

#%%annova_uncertainity_rcp60_80years
all_first_jday_anoxic_deep_prof_inyear_rcp60= all_first_jday_anoxic_deep_prof_inyear_rcp60.replace(0, np.nan)

anova_first_jday_anoxic_deep_prof_rcp60_80years=annova_uncertainity(all_first_jday_anoxic_deep_prof_inyear_rcp60[all_first_jday_anoxic_deep_prof_inyear_rcp60.index>2019])

anova_first_jday_anoxic_deep_prof_rcp60_80years.describe().loc['mean', :]
"""
GCMs             58.145114
param            40.582960
interaction       1.271926
GCMs/param        2.223800
year           2059.500000
Name: mean, dtype: float64
"""

anova_first_jday_anoxic_deep_prof_rcp60_80years.describe().loc['std', :]
"""
GCMs           22.154935
param          21.206215
interaction     2.560534
GCMs/param      1.998924
year           23.237900
Name: std, dtype: float64

"""


all_len_anoxic_deep_prof_inyear_rcp60=all_len_anoxic_deep_prof_inyear_rcp60.replace(0, np.nan)

anova_len_jday_anoxic_deep_prof_rcp60_80years=annova_uncertainity(all_len_anoxic_deep_prof_inyear_rcp60[all_len_anoxic_deep_prof_inyear_rcp60.index>2019])

anova_len_jday_anoxic_deep_prof_rcp60_80years.describe().loc['mean', :]
"""
GCMs             70.226053
param            28.863931
interaction       0.910015
GCMs/param        4.219813
year           2059.500000
Name: mean, dtype: float64
"""


anova_len_jday_anoxic_deep_prof_rcp60_80years.describe().loc['std', :]
"""
GCMs           19.462944
param          18.858147
interaction     1.358864
GCMs/param      3.965990
year           23.237900
Name: std, dtype: float64
"""



#%%rcp85


# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp85'
all_first_jday_anoxic_deep_prof_inyear_rcp85= pd.DataFrame([])
all_last_jday_anoxic_deep_prof_inyear_rcp85= pd.DataFrame([])
all_len_anoxic_deep_prof_inyear_rcp85= pd.DataFrame([])
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
        
        
        first_jday_anoxic_deep_prof_inyear_rcp85=first_last_len_anoxic_deep_inyear  (C, Vr, time_series, threshold=0.5)[1]
        last_jday_anoxic_deep_prof_inyear_rcp85=first_last_len_anoxic_deep_inyear  (C, Vr, time_series, threshold=0.5)[3]
        len_anoxic_deep_prof_inyear_rcp85=first_last_len_anoxic_deep_inyear  (C, Vr, time_series, threshold=0.5)[4]
        

        all_first_jday_anoxic_deep_prof_inyear_rcp85 = pd.concat([all_first_jday_anoxic_deep_prof_inyear_rcp85 , first_jday_anoxic_deep_prof_inyear_rcp85], axis=1)
        all_last_jday_anoxic_deep_prof_inyear_rcp85 = pd.concat([all_last_jday_anoxic_deep_prof_inyear_rcp85 , last_jday_anoxic_deep_prof_inyear_rcp85], axis=1)
        all_len_anoxic_deep_prof_inyear_rcp85 = pd.concat([all_len_anoxic_deep_prof_inyear_rcp85 , len_anoxic_deep_prof_inyear_rcp85], axis=1)


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
        
        
        first_jday_anoxic_deep_prof_inyear_rcp85=first_last_len_anoxic_deep_inyear  (C, Vr, time_series, threshold=0.5)[1]
        last_jday_anoxic_deep_prof_inyear_rcp85=first_last_len_anoxic_deep_inyear  (C, Vr, time_series, threshold=0.5)[3]
        len_anoxic_deep_prof_inyear_rcp85=first_last_len_anoxic_deep_inyear  (C, Vr, time_series, threshold=0.5)[4]
        

        all_first_jday_anoxic_deep_prof_inyear_rcp85 = pd.concat([all_first_jday_anoxic_deep_prof_inyear_rcp85 , first_jday_anoxic_deep_prof_inyear_rcp85], axis=1)
        all_last_jday_anoxic_deep_prof_inyear_rcp85 = pd.concat([all_last_jday_anoxic_deep_prof_inyear_rcp85 , last_jday_anoxic_deep_prof_inyear_rcp85], axis=1)
        all_len_anoxic_deep_prof_inyear_rcp85 = pd.concat([all_len_anoxic_deep_prof_inyear_rcp85 , len_anoxic_deep_prof_inyear_rcp85], axis=1)


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
        
        
        first_jday_anoxic_deep_prof_inyear_rcp85=first_last_len_anoxic_deep_inyear  (C, Vr, time_series, threshold=0.5)[1]
        last_jday_anoxic_deep_prof_inyear_rcp85=first_last_len_anoxic_deep_inyear  (C, Vr, time_series, threshold=0.5)[3]
        len_anoxic_deep_prof_inyear_rcp85=first_last_len_anoxic_deep_inyear  (C, Vr, time_series, threshold=0.5)[4]
        

        all_first_jday_anoxic_deep_prof_inyear_rcp85 = pd.concat([all_first_jday_anoxic_deep_prof_inyear_rcp85 , first_jday_anoxic_deep_prof_inyear_rcp85], axis=1)
        all_last_jday_anoxic_deep_prof_inyear_rcp85 = pd.concat([all_last_jday_anoxic_deep_prof_inyear_rcp85 , last_jday_anoxic_deep_prof_inyear_rcp85], axis=1)
        all_len_anoxic_deep_prof_inyear_rcp85 = pd.concat([all_len_anoxic_deep_prof_inyear_rcp85 , len_anoxic_deep_prof_inyear_rcp85], axis=1)


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
        
        
        first_jday_anoxic_deep_prof_inyear_rcp85=first_last_len_anoxic_deep_inyear  (C, Vr, time_series, threshold=0.5)[1]
        last_jday_anoxic_deep_prof_inyear_rcp85=first_last_len_anoxic_deep_inyear  (C, Vr, time_series, threshold=0.5)[3]
        len_anoxic_deep_prof_inyear_rcp85=first_last_len_anoxic_deep_inyear  (C, Vr, time_series, threshold=0.5)[4]
        

        all_first_jday_anoxic_deep_prof_inyear_rcp85 = pd.concat([all_first_jday_anoxic_deep_prof_inyear_rcp85 , first_jday_anoxic_deep_prof_inyear_rcp85], axis=1)
        all_last_jday_anoxic_deep_prof_inyear_rcp85 = pd.concat([all_last_jday_anoxic_deep_prof_inyear_rcp85 , last_jday_anoxic_deep_prof_inyear_rcp85], axis=1)
        all_len_anoxic_deep_prof_inyear_rcp85 = pd.concat([all_len_anoxic_deep_prof_inyear_rcp85 , len_anoxic_deep_prof_inyear_rcp85], axis=1)



#%%annova_uncertainity_rcp85 

all_first_jday_anoxic_deep_prof_inyear_rcp85= all_first_jday_anoxic_deep_prof_inyear_rcp85.replace(0, np.nan)

anova_first_jday_anoxic_deep_prof_rcp85=annova_uncertainity(all_first_jday_anoxic_deep_prof_inyear_rcp85)

anova_first_jday_anoxic_deep_prof_rcp85.describe().loc['mean', :]
"""
GCMs             58.481396
param            40.229669
interaction       1.288934
GCMs/param        2.465617
year           2052.500000
Name: mean, dtype: float64
"""

anova_first_jday_anoxic_deep_prof_rcp85.describe().loc['std', :]
"""
GCMs           22.130504
param          21.864997
interaction     1.140512
GCMs/param      2.554115
year           27.279418
Name: std, dtype: float64

"""
all_last_jday_anoxic_deep_prof_inyear_rcp85= all_last_jday_anoxic_deep_prof_inyear_rcp85.replace(0, np.nan)

anova_last_jday_anoxic_deep_prof_rcp85=annova_uncertainity(all_last_jday_anoxic_deep_prof_inyear_rcp85)

anova_last_jday_anoxic_deep_prof_rcp85.describe().loc['mean', :]
"""
GCMs            100.000000
param             0.036892
interaction      -0.036892
GCMs/param             inf
year           2052.500000
Name: mean, dtype: float64
"""


anova_last_jday_anoxic_deep_prof_rcp85.describe().loc['std', :]

"""
GCMs           2.947194e-15
param          3.576842e-01
interaction    3.576842e-01
GCMs/param              NaN
year           2.727942e+01
Name: std, dtype: float64
"""



anova_len_jday_anoxic_deep_prof_rcp85=annova_uncertainity(all_len_anoxic_deep_prof_inyear_rcp85)

anova_len_jday_anoxic_deep_prof_rcp85.describe().loc['mean', :]
"""
GCMs             78.783142
param            20.525787
interaction       0.691071
GCMs/param        6.668543
year           2052.500000
Name: mean, dtype: float64
"""


anova_len_jday_anoxic_deep_prof_rcp85.describe().loc['std', :]
"""
GCMs           15.803703
param          15.248261
interaction     0.740030
GCMs/param      5.626518
year           27.279418
Name: std, dtype: float64
"""


#%%annova_uncertainity_rcp85_80years
all_first_jday_anoxic_deep_prof_inyear_rcp85=all_first_jday_anoxic_deep_prof_inyear_rcp85.replace(0, np.nan)

anova_first_jday_anoxic_deep_prof_rcp85_80years=annova_uncertainity(all_first_jday_anoxic_deep_prof_inyear_rcp85[all_first_jday_anoxic_deep_prof_inyear_rcp85.index>2019])

anova_first_jday_anoxic_deep_prof_rcp85_80years.describe().loc['mean', :]
"""
GCMs             58.370460
param            40.286506
interaction       1.343035
GCMs/param        2.472025
year           2059.500000
Name: mean, dtype: float64
"""

anova_first_jday_anoxic_deep_prof_rcp85_80years.describe().loc['std', :]
"""
GCMs           22.014840
param          21.756008
interaction     1.200388
GCMs/param      2.651246
year           23.237900
Name: std, dtype: float64
"""




anova_len_jday_anoxic_deep_prof_rcp85_80years=annova_uncertainity(all_len_anoxic_deep_prof_inyear_rcp85[all_len_anoxic_deep_prof_inyear_rcp85.index>2019])

anova_len_jday_anoxic_deep_prof_rcp85_80years.describe().loc['mean', :]
"""
GCMs             79.261022
param            20.032370
interaction       0.706608
GCMs/param        7.059975
year           2059.500000
Name: mean, dtype: float64
"""


anova_len_jday_anoxic_deep_prof_rcp85_80years.describe().loc['std', :]
"""
GCMs           15.950746
param          15.322115
interaction     0.777911
GCMs/param      5.938013
year           23.237900
Name: std, dtype: float64
"""





#%% Plotting of anova_len_jday_anoxic_deep_prof, anova_first_jday_anoxic_deep_prof rcp85

#first_jday_anoxic_his

#years
contributions_first_jday_anoxic_his_years=anova_first_jday_anoxic_deep_prof_his['year']
#GCMs
gcm_contributions_first_jday_anoxic_his= anova_first_jday_anoxic_deep_prof_his['GCMs']
#Param
param_contributions_first_jday_anoxic_his=anova_first_jday_anoxic_deep_prof_his['param']
#interaction
interact_contributions_first_jday_anoxic_his =anova_first_jday_anoxic_deep_prof_his['interaction']


#len_jday_anoxic_his

#years
contributions_len_jday_anoxic_his_years=anova_len_jday_anoxic_deep_prof_his['year']
#GCMs
gcm_contributions_len_jday_anoxic_his= anova_len_jday_anoxic_deep_prof_his['GCMs']
#Param
param_contributions_len_jday_anoxic_his=anova_len_jday_anoxic_deep_prof_his['param']
#interaction
interact_contributions_len_jday_anoxic_his =anova_len_jday_anoxic_deep_prof_his['interaction']

     

#first_jday_anoxic_rcp26

#years
contributions_first_jday_anoxic_rcp26_years=anova_first_jday_anoxic_deep_prof_rcp26['year']
#GCMs
gcm_contributions_first_jday_anoxic_rcp26= anova_first_jday_anoxic_deep_prof_rcp26['GCMs']
#Param
param_contributions_first_jday_anoxic_rcp26=anova_first_jday_anoxic_deep_prof_rcp26['param']
#interaction
interact_contributions_first_jday_anoxic_rcp26 =anova_first_jday_anoxic_deep_prof_rcp26['interaction']


#len_jday_anoxic_rcp26

#years
contributions_len_jday_anoxic_rcp26_years=anova_len_jday_anoxic_deep_prof_rcp26['year']
#GCMs
gcm_contributions_len_jday_anoxic_rcp26= anova_len_jday_anoxic_deep_prof_rcp26['GCMs']
#Param
param_contributions_len_jday_anoxic_rcp26=anova_len_jday_anoxic_deep_prof_rcp26['param']
#interaction
interact_contributions_len_jday_anoxic_rcp26 =anova_len_jday_anoxic_deep_prof_rcp26['interaction']

     

#first_jday_anoxic_rcp60

#years
contributions_first_jday_anoxic_rcp60_years=anova_first_jday_anoxic_deep_prof_rcp60['year']
#GCMs
gcm_contributions_first_jday_anoxic_rcp60= anova_first_jday_anoxic_deep_prof_rcp60['GCMs']
#Param
param_contributions_first_jday_anoxic_rcp60=anova_first_jday_anoxic_deep_prof_rcp60['param']
#interaction
interact_contributions_first_jday_anoxic_rcp60 =anova_first_jday_anoxic_deep_prof_rcp60['interaction']


#len_jday_anoxic_rcp60

#years
contributions_len_jday_anoxic_rcp60_years=anova_len_jday_anoxic_deep_prof_rcp60['year']
#GCMs
gcm_contributions_len_jday_anoxic_rcp60= anova_len_jday_anoxic_deep_prof_rcp60['GCMs']
#Param
param_contributions_len_jday_anoxic_rcp60=anova_len_jday_anoxic_deep_prof_rcp60['param']
#interaction
interact_contributions_len_jday_anoxic_rcp60 =anova_len_jday_anoxic_deep_prof_rcp60['interaction']

     
#first_jday_anoxic_rcp85

#years
contributions_first_jday_anoxic_rcp85_years=anova_first_jday_anoxic_deep_prof_rcp85['year']
#GCMs
gcm_contributions_first_jday_anoxic_rcp85= anova_first_jday_anoxic_deep_prof_rcp85['GCMs']
#Param
param_contributions_first_jday_anoxic_rcp85=anova_first_jday_anoxic_deep_prof_rcp85['param']
#interaction
interact_contributions_first_jday_anoxic_rcp85 =anova_first_jday_anoxic_deep_prof_rcp85['interaction']


#len_jday_anoxic_rcp85

#years
contributions_len_jday_anoxic_rcp85_years=anova_len_jday_anoxic_deep_prof_rcp85['year']
#GCMs
gcm_contributions_len_jday_anoxic_rcp85= anova_len_jday_anoxic_deep_prof_rcp85['GCMs']
#Param
param_contributions_len_jday_anoxic_rcp85=anova_len_jday_anoxic_deep_prof_rcp85['param']
#interaction
interact_contributions_len_jday_anoxic_rcp85 =anova_len_jday_anoxic_deep_prof_rcp85['interaction']

     
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

axs[0].fill_between(contributions_first_jday_anoxic_his_years, 0, gcm_contributions_first_jday_anoxic_his , label='GCMs', alpha=0.7, color=colors[0], edgecolor='black')
axs[0].fill_between(contributions_first_jday_anoxic_his_years, gcm_contributions_first_jday_anoxic_his , gcm_contributions_first_jday_anoxic_his + param_contributions_first_jday_anoxic_his, label='Parameters', alpha=0.7, color=colors[1], edgecolor='black')
axs[0].fill_between(contributions_first_jday_anoxic_his_years, gcm_contributions_first_jday_anoxic_his  + param_contributions_first_jday_anoxic_his, gcm_contributions_first_jday_anoxic_his + param_contributions_first_jday_anoxic_his + interact_contributions_first_jday_anoxic_his, label='Interactions', alpha=0.7, color=colors[2], edgecolor='black')
axs[0].set_title('First day of deep anoxia in His', fontsize=20)
axs[0].set_ylim(0,100)
axs[0].set_xlim(1861, 2005)
axs[0].tick_params(axis='both', which='major', labelsize=20)



axs[1].fill_between(contributions_len_jday_anoxic_his_years, 0, gcm_contributions_len_jday_anoxic_his , label='GCMs', alpha=0.7, color=colors[0], edgecolor='black')
axs[1].fill_between(contributions_len_jday_anoxic_his_years, gcm_contributions_len_jday_anoxic_his , gcm_contributions_len_jday_anoxic_his + param_contributions_len_jday_anoxic_his, label='Parameters', alpha=0.7, color=colors[1], edgecolor='black')
axs[1].fill_between(contributions_len_jday_anoxic_his_years, gcm_contributions_len_jday_anoxic_his  + param_contributions_len_jday_anoxic_his, gcm_contributions_len_jday_anoxic_his + param_contributions_len_jday_anoxic_his + interact_contributions_len_jday_anoxic_his, label='Interactions', alpha=0.7, color=colors[2], edgecolor='black')
axs[1].set_title('Duration of deep anoxia in His', fontsize=20)
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
plt.savefig('uncertainty_first_len_deep_anoxia_duration_allyears_his.png', dpi=300, bbox_inches='tight')

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

axs[0, 0].fill_between(contributions_first_jday_anoxic_rcp26_years, 0, gcm_contributions_first_jday_anoxic_rcp26 , label='GCMs', alpha=0.7, color=colors[0], edgecolor='black')
axs[0, 0].fill_between(contributions_first_jday_anoxic_rcp26_years, gcm_contributions_first_jday_anoxic_rcp26 , gcm_contributions_first_jday_anoxic_rcp26 + param_contributions_first_jday_anoxic_rcp26, label='Parameters', alpha=0.7, color=colors[1], edgecolor='black')
axs[0, 0].fill_between(contributions_first_jday_anoxic_rcp26_years, gcm_contributions_first_jday_anoxic_rcp26  + param_contributions_first_jday_anoxic_rcp26, gcm_contributions_first_jday_anoxic_rcp26 + param_contributions_first_jday_anoxic_rcp26 + interact_contributions_first_jday_anoxic_rcp26, label='Interactions', alpha=0.7, color=colors[2], edgecolor='black')
axs[0, 0].set_title('First day of deep anoxia in RCP2.6', fontsize=20)
axs[0, 0].set_ylim(0,100)
axs[0, 0].set_xlim(2006, 2099)
axs[0, 0].tick_params(axis='both', which='major', labelsize=20)



axs[0, 1].fill_between(contributions_len_jday_anoxic_rcp26_years, 0, gcm_contributions_len_jday_anoxic_rcp26 , label='GCMs', alpha=0.7, color=colors[0], edgecolor='black')
axs[0, 1].fill_between(contributions_len_jday_anoxic_rcp26_years, gcm_contributions_len_jday_anoxic_rcp26 , gcm_contributions_len_jday_anoxic_rcp26 + param_contributions_len_jday_anoxic_rcp26, label='Parameters', alpha=0.7, color=colors[1], edgecolor='black')
axs[0, 1].fill_between(contributions_len_jday_anoxic_rcp26_years, gcm_contributions_len_jday_anoxic_rcp26  + param_contributions_len_jday_anoxic_rcp26, gcm_contributions_len_jday_anoxic_rcp26 + param_contributions_len_jday_anoxic_rcp26 + interact_contributions_len_jday_anoxic_rcp26, label='Interactions', alpha=0.7, color=colors[2], edgecolor='black')
axs[0, 1].set_title('Duration of deep anoxia in RCP2.6', fontsize=20)
axs[0, 1].set_ylim(0,100)
axs[0, 1].set_xlim(2006, 2099)
axs[0, 1].tick_params(axis='both', which='major', labelsize=20)

axs[1, 0].fill_between(contributions_first_jday_anoxic_rcp60_years, 0, gcm_contributions_first_jday_anoxic_rcp60 , label='GCMs', alpha=0.7, color=colors[0], edgecolor='black')
axs[1, 0].fill_between(contributions_first_jday_anoxic_rcp60_years, gcm_contributions_first_jday_anoxic_rcp60 , gcm_contributions_first_jday_anoxic_rcp60 + param_contributions_first_jday_anoxic_rcp60, label='Parameters', alpha=0.7, color=colors[1], edgecolor='black')
axs[1, 0].fill_between(contributions_first_jday_anoxic_rcp60_years, gcm_contributions_first_jday_anoxic_rcp60  + param_contributions_first_jday_anoxic_rcp60, gcm_contributions_first_jday_anoxic_rcp60 + param_contributions_first_jday_anoxic_rcp60 + interact_contributions_first_jday_anoxic_rcp60, label='Interactions', alpha=0.7, color=colors[2], edgecolor='black')
axs[1, 0].set_title('First day of deep anoxia in RCP6.0', fontsize=20)
axs[1, 0].set_ylim(0,100)
axs[1, 0].set_xlim(2006, 2099)
axs[1, 0].tick_params(axis='both', which='major', labelsize=20)



axs[1, 1].fill_between(contributions_len_jday_anoxic_rcp60_years, 0, gcm_contributions_len_jday_anoxic_rcp60 , label='GCMs', alpha=0.7, color=colors[0], edgecolor='black')
axs[1, 1].fill_between(contributions_len_jday_anoxic_rcp60_years, gcm_contributions_len_jday_anoxic_rcp60 , gcm_contributions_len_jday_anoxic_rcp60 + param_contributions_len_jday_anoxic_rcp60, label='Parameters', alpha=0.7, color=colors[1], edgecolor='black')
axs[1, 1].fill_between(contributions_len_jday_anoxic_rcp60_years, gcm_contributions_len_jday_anoxic_rcp60  + param_contributions_len_jday_anoxic_rcp60, gcm_contributions_len_jday_anoxic_rcp60 + param_contributions_len_jday_anoxic_rcp60 + interact_contributions_len_jday_anoxic_rcp60, label='Interactions', alpha=0.7, color=colors[2], edgecolor='black')
axs[1, 1].set_title('Duration of deep anoxia in RCP6.0', fontsize=20)
axs[1, 1].set_ylim(0,100)
axs[1, 1].set_xlim(2006, 2099)
axs[1, 1].tick_params(axis='both', which='major', labelsize=20)




axs[2, 0].fill_between(contributions_first_jday_anoxic_rcp85_years, 0, gcm_contributions_first_jday_anoxic_rcp85 , label='GCMs', alpha=0.7, color=colors[0], edgecolor='black')
axs[2, 0].fill_between(contributions_first_jday_anoxic_rcp85_years, gcm_contributions_first_jday_anoxic_rcp85 , gcm_contributions_first_jday_anoxic_rcp85 + param_contributions_first_jday_anoxic_rcp85, label='Parameters', alpha=0.7, color=colors[1], edgecolor='black')
axs[2, 0].fill_between(contributions_first_jday_anoxic_rcp85_years, gcm_contributions_first_jday_anoxic_rcp85  + param_contributions_first_jday_anoxic_rcp85, gcm_contributions_first_jday_anoxic_rcp85 + param_contributions_first_jday_anoxic_rcp85 + interact_contributions_first_jday_anoxic_rcp85, label='Interactions', alpha=0.7, color=colors[2], edgecolor='black')
axs[2, 0].set_title('First day of deep anoxia in RCP8.5', fontsize=20)
axs[2, 0].set_ylim(0,100)
axs[2, 0].set_xlim(2006, 2099)
axs[2, 0].tick_params(axis='both', which='major', labelsize=20)



axs[2, 1].fill_between(contributions_len_jday_anoxic_rcp85_years, 0, gcm_contributions_len_jday_anoxic_rcp85 , label='GCMs', alpha=0.7, color=colors[0], edgecolor='black')
axs[2, 1].fill_between(contributions_len_jday_anoxic_rcp85_years, gcm_contributions_len_jday_anoxic_rcp85 , gcm_contributions_len_jday_anoxic_rcp85 + param_contributions_len_jday_anoxic_rcp85, label='Parameters', alpha=0.7, color=colors[1], edgecolor='black')
axs[2, 1].fill_between(contributions_len_jday_anoxic_rcp85_years, gcm_contributions_len_jday_anoxic_rcp85  + param_contributions_len_jday_anoxic_rcp85, gcm_contributions_len_jday_anoxic_rcp85 + param_contributions_len_jday_anoxic_rcp85 + interact_contributions_len_jday_anoxic_rcp85, label='Interactions', alpha=0.7, color=colors[2], edgecolor='black')
axs[2, 1].set_title('Duration of deep anoxia in RCP8.5', fontsize=20)
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
plt.savefig('uncertainty_first_len_deep_anoxia_duration_allyears_rcps.png', dpi=300, bbox_inches='tight')

plt.show()


#%% Uncertainity of 80 years in RCPs

#first_jday_anoxic_rcp26

#years
contributions_first_jday_anoxic_rcp26_years=anova_first_jday_anoxic_deep_prof_rcp26[anova_first_jday_anoxic_deep_prof_rcp26['year']>2019]['year']
#GCMs
gcm_contributions_first_jday_anoxic_rcp26= anova_first_jday_anoxic_deep_prof_rcp26[anova_first_jday_anoxic_deep_prof_rcp26['year']>2019]['GCMs']
#Param
param_contributions_first_jday_anoxic_rcp26=anova_first_jday_anoxic_deep_prof_rcp26[anova_first_jday_anoxic_deep_prof_rcp26['year']>2019]['param']
#interaction
interact_contributions_first_jday_anoxic_rcp26 =anova_first_jday_anoxic_deep_prof_rcp26[anova_first_jday_anoxic_deep_prof_rcp26['year']>2019]['interaction']


#len_jday_anoxic_rcp26

#years
contributions_len_jday_anoxic_rcp26_years=anova_len_jday_anoxic_deep_prof_rcp26[anova_len_jday_anoxic_deep_prof_rcp26['year']>2019]['year']
#GCMs
gcm_contributions_len_jday_anoxic_rcp26= anova_len_jday_anoxic_deep_prof_rcp26[anova_len_jday_anoxic_deep_prof_rcp26['year']>2019]['GCMs']
#Param
param_contributions_len_jday_anoxic_rcp26=anova_len_jday_anoxic_deep_prof_rcp26[anova_len_jday_anoxic_deep_prof_rcp26['year']>2019]['param']
#interaction
interact_contributions_len_jday_anoxic_rcp26 =anova_len_jday_anoxic_deep_prof_rcp26[anova_len_jday_anoxic_deep_prof_rcp26['year']>2019]['interaction']


     

#first_jday_anoxic_rcp60

#years
contributions_first_jday_anoxic_rcp60_years=anova_first_jday_anoxic_deep_prof_rcp60[anova_first_jday_anoxic_deep_prof_rcp60['year']>2019]['year']
#GCMs
gcm_contributions_first_jday_anoxic_rcp60= anova_first_jday_anoxic_deep_prof_rcp60[anova_first_jday_anoxic_deep_prof_rcp60['year']>2019]['GCMs']
#Param
param_contributions_first_jday_anoxic_rcp60=anova_first_jday_anoxic_deep_prof_rcp60[anova_first_jday_anoxic_deep_prof_rcp60['year']>2019]['param']
#interaction
interact_contributions_first_jday_anoxic_rcp60 =anova_first_jday_anoxic_deep_prof_rcp60[anova_first_jday_anoxic_deep_prof_rcp60['year']>2019]['interaction']


#len_jday_anoxic_rcp60

#years
contributions_len_jday_anoxic_rcp60_years=anova_len_jday_anoxic_deep_prof_rcp60[anova_len_jday_anoxic_deep_prof_rcp60['year']>2019]['year']
#GCMs
gcm_contributions_len_jday_anoxic_rcp60= anova_len_jday_anoxic_deep_prof_rcp60[anova_len_jday_anoxic_deep_prof_rcp60['year']>2019]['GCMs']
#Param
param_contributions_len_jday_anoxic_rcp60=anova_len_jday_anoxic_deep_prof_rcp60[anova_len_jday_anoxic_deep_prof_rcp60['year']>2019]['param']
#interaction
interact_contributions_len_jday_anoxic_rcp60 =anova_len_jday_anoxic_deep_prof_rcp60[anova_len_jday_anoxic_deep_prof_rcp60['year']>2019]['interaction']


#first_jday_anoxic_rcp85

#years
contributions_first_jday_anoxic_rcp85_years=anova_first_jday_anoxic_deep_prof_rcp85[anova_first_jday_anoxic_deep_prof_rcp85['year']>2019]['year']
#GCMs
gcm_contributions_first_jday_anoxic_rcp85= anova_first_jday_anoxic_deep_prof_rcp85[anova_first_jday_anoxic_deep_prof_rcp85['year']>2019]['GCMs']
#Param
param_contributions_first_jday_anoxic_rcp85=anova_first_jday_anoxic_deep_prof_rcp85[anova_first_jday_anoxic_deep_prof_rcp85['year']>2019]['param']
#interaction
interact_contributions_first_jday_anoxic_rcp85 =anova_first_jday_anoxic_deep_prof_rcp85[anova_first_jday_anoxic_deep_prof_rcp85['year']>2019]['interaction']


#len_jday_anoxic_rcp85

#years
contributions_len_jday_anoxic_rcp85_years=anova_len_jday_anoxic_deep_prof_rcp85[anova_len_jday_anoxic_deep_prof_rcp85['year']>2019]['year']
#GCMs
gcm_contributions_len_jday_anoxic_rcp85= anova_len_jday_anoxic_deep_prof_rcp85[anova_len_jday_anoxic_deep_prof_rcp85['year']>2019]['GCMs']
#Param
param_contributions_len_jday_anoxic_rcp85=anova_len_jday_anoxic_deep_prof_rcp85[anova_len_jday_anoxic_deep_prof_rcp85['year']>2019]['param']
#interaction
interact_contributions_len_jday_anoxic_rcp85 =anova_len_jday_anoxic_deep_prof_rcp85[anova_len_jday_anoxic_deep_prof_rcp85['year']>2019]['interaction']



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

axs[0, 0].fill_between(contributions_first_jday_anoxic_rcp26_years, 0, gcm_contributions_first_jday_anoxic_rcp26 , label='GCMs', alpha=0.7, color=colors[0], edgecolor='black')
axs[0, 0].fill_between(contributions_first_jday_anoxic_rcp26_years, gcm_contributions_first_jday_anoxic_rcp26 , gcm_contributions_first_jday_anoxic_rcp26 + param_contributions_first_jday_anoxic_rcp26, label='Parameters', alpha=0.7, color=colors[1], edgecolor='black')
axs[0, 0].fill_between(contributions_first_jday_anoxic_rcp26_years, gcm_contributions_first_jday_anoxic_rcp26  + param_contributions_first_jday_anoxic_rcp26, gcm_contributions_first_jday_anoxic_rcp26 + param_contributions_first_jday_anoxic_rcp26 + interact_contributions_first_jday_anoxic_rcp26, label='Interactions', alpha=0.7, color=colors[2], edgecolor='black')
axs[0, 0].set_title('First day of deep anoxia in RCP2.6', fontsize=20)
axs[0, 0].set_ylim(0,100)
axs[0, 0].set_xlim(2020, 2099)
axs[0, 0].tick_params(axis='both', which='major', labelsize=20)



axs[0, 1].fill_between(contributions_len_jday_anoxic_rcp26_years, 0, gcm_contributions_len_jday_anoxic_rcp26 , label='GCMs', alpha=0.7, color=colors[0], edgecolor='black')
axs[0, 1].fill_between(contributions_len_jday_anoxic_rcp26_years, gcm_contributions_len_jday_anoxic_rcp26 , gcm_contributions_len_jday_anoxic_rcp26 + param_contributions_len_jday_anoxic_rcp26, label='Parameters', alpha=0.7, color=colors[1], edgecolor='black')
axs[0, 1].fill_between(contributions_len_jday_anoxic_rcp26_years, gcm_contributions_len_jday_anoxic_rcp26  + param_contributions_len_jday_anoxic_rcp26, gcm_contributions_len_jday_anoxic_rcp26 + param_contributions_len_jday_anoxic_rcp26 + interact_contributions_len_jday_anoxic_rcp26, label='Interactions', alpha=0.7, color=colors[2], edgecolor='black')
axs[0, 1].set_title('Duration of deep anoxia in RCP2.6', fontsize=20)
axs[0, 1].set_ylim(0,100)
axs[0, 1].set_xlim(2020, 2099)
axs[0, 1].tick_params(axis='both', which='major', labelsize=20)

axs[1, 0].fill_between(contributions_first_jday_anoxic_rcp60_years, 0, gcm_contributions_first_jday_anoxic_rcp60 , label='GCMs', alpha=0.7, color=colors[0], edgecolor='black')
axs[1, 0].fill_between(contributions_first_jday_anoxic_rcp60_years, gcm_contributions_first_jday_anoxic_rcp60 , gcm_contributions_first_jday_anoxic_rcp60 + param_contributions_first_jday_anoxic_rcp60, label='Parameters', alpha=0.7, color=colors[1], edgecolor='black')
axs[1, 0].fill_between(contributions_first_jday_anoxic_rcp60_years, gcm_contributions_first_jday_anoxic_rcp60  + param_contributions_first_jday_anoxic_rcp60, gcm_contributions_first_jday_anoxic_rcp60 + param_contributions_first_jday_anoxic_rcp60 + interact_contributions_first_jday_anoxic_rcp60, label='Interactions', alpha=0.7, color=colors[2], edgecolor='black')
axs[1, 0].set_title('First day of deep anoxia in RCP6.0', fontsize=20)
axs[1, 0].set_ylim(0,100)
axs[1, 0].set_xlim(2020, 2099)
axs[1, 0].tick_params(axis='both', which='major', labelsize=20)



axs[1, 1].fill_between(contributions_len_jday_anoxic_rcp60_years, 0, gcm_contributions_len_jday_anoxic_rcp60 , label='GCMs', alpha=0.7, color=colors[0], edgecolor='black')
axs[1, 1].fill_between(contributions_len_jday_anoxic_rcp60_years, gcm_contributions_len_jday_anoxic_rcp60 , gcm_contributions_len_jday_anoxic_rcp60 + param_contributions_len_jday_anoxic_rcp60, label='Parameters', alpha=0.7, color=colors[1], edgecolor='black')
axs[1, 1].fill_between(contributions_len_jday_anoxic_rcp60_years, gcm_contributions_len_jday_anoxic_rcp60  + param_contributions_len_jday_anoxic_rcp60, gcm_contributions_len_jday_anoxic_rcp60 + param_contributions_len_jday_anoxic_rcp60 + interact_contributions_len_jday_anoxic_rcp60, label='Interactions', alpha=0.7, color=colors[2], edgecolor='black')
axs[1, 1].set_title('Duration of deep anoxia in RCP6.0', fontsize=20)
axs[1, 1].set_ylim(0,100)
axs[1, 1].set_xlim(2020, 2099)
axs[1, 1].tick_params(axis='both', which='major', labelsize=20)




axs[2, 0].fill_between(contributions_first_jday_anoxic_rcp85_years, 0, gcm_contributions_first_jday_anoxic_rcp85 , label='GCMs', alpha=0.7, color=colors[0], edgecolor='black')
axs[2, 0].fill_between(contributions_first_jday_anoxic_rcp85_years, gcm_contributions_first_jday_anoxic_rcp85 , gcm_contributions_first_jday_anoxic_rcp85 + param_contributions_first_jday_anoxic_rcp85, label='Parameters', alpha=0.7, color=colors[1], edgecolor='black')
axs[2, 0].fill_between(contributions_first_jday_anoxic_rcp85_years, gcm_contributions_first_jday_anoxic_rcp85  + param_contributions_first_jday_anoxic_rcp85, gcm_contributions_first_jday_anoxic_rcp85 + param_contributions_first_jday_anoxic_rcp85 + interact_contributions_first_jday_anoxic_rcp85, label='Interactions', alpha=0.7, color=colors[2], edgecolor='black')
axs[2, 0].set_title('First day of deep anoxia in RCP8.5', fontsize=20)
axs[2, 0].set_ylim(0,100)
axs[2, 0].set_xlim(2020, 2099)
axs[2, 0].tick_params(axis='both', which='major', labelsize=20)



axs[2, 1].fill_between(contributions_len_jday_anoxic_rcp85_years, 0, gcm_contributions_len_jday_anoxic_rcp85 , label='GCMs', alpha=0.7, color=colors[0], edgecolor='black')
axs[2, 1].fill_between(contributions_len_jday_anoxic_rcp85_years, gcm_contributions_len_jday_anoxic_rcp85 , gcm_contributions_len_jday_anoxic_rcp85 + param_contributions_len_jday_anoxic_rcp85, label='Parameters', alpha=0.7, color=colors[1], edgecolor='black')
axs[2, 1].fill_between(contributions_len_jday_anoxic_rcp85_years, gcm_contributions_len_jday_anoxic_rcp85  + param_contributions_len_jday_anoxic_rcp85, gcm_contributions_len_jday_anoxic_rcp85 + param_contributions_len_jday_anoxic_rcp85 + interact_contributions_len_jday_anoxic_rcp85, label='Interactions', alpha=0.7, color=colors[2], edgecolor='black')
axs[2, 1].set_title('Duration of deep anoxia in RCP8.5', fontsize=20)
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
plt.savefig('uncertainty_first_len_deep_anoxia_duration_allyears_rcps_80years.png', dpi=300, bbox_inches='tight')

plt.show()


#%%#
#=====================================GLUE ============================

#%%his

# first_jday_anoxic_deep_prof_inyear_his
timeseries_year_his= all_first_jday_anoxic_deep_prof_inyear_his.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_first_jday_anoxic_deep_prof_inyear_his.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights_his))

# Build glue df
glue_first_jday_anoxic_deep_prof_inyear_his = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_first_jday_anoxic_deep_prof_inyear_his=glue_first_jday_anoxic_deep_prof_inyear_his.set_index(timeseries_year_his)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory
glue_first_jday_anoxic_deep_prof_inyear_his.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/his/glue_first_jday_anoxic_deep_prof_inyear_his.csv')



# last_jday_anoxic_deep_prof_inyear_his
timeseries_year_his= all_last_jday_anoxic_deep_prof_inyear_his.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_last_jday_anoxic_deep_prof_inyear_his.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights_his))

# Build glue df
glue_last_jday_anoxic_deep_prof_inyear_his = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_last_jday_anoxic_deep_prof_inyear_his=glue_last_jday_anoxic_deep_prof_inyear_his.set_index(timeseries_year_his)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory
glue_last_jday_anoxic_deep_prof_inyear_his.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/his/glue_last_jday_anoxic_deep_prof_inyear_his.csv')

           

# len_anoxic_deep_prof_inyear_his
timeseries_year_his= all_len_anoxic_deep_prof_inyear_his.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_len_anoxic_deep_prof_inyear_his.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights_his))

# Build glue df
glue_len_anoxic_deep_prof_inyear_his = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_len_anoxic_deep_prof_inyear_his=glue_len_anoxic_deep_prof_inyear_his.set_index(timeseries_year_his)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory
glue_len_anoxic_deep_prof_inyear_his.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/his/glue_len_anoxic_deep_prof_inyear_his.csv')


#%%rcp26

# first_jday_anoxic_deep_prof_inyear_rcp26
timeseries_year_rcp26= all_first_jday_anoxic_deep_prof_inyear_rcp26.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_first_jday_anoxic_deep_prof_inyear_rcp26.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights_rcp26))

# Build glue df
glue_first_jday_anoxic_deep_prof_inyear_rcp26 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_first_jday_anoxic_deep_prof_inyear_rcp26=glue_first_jday_anoxic_deep_prof_inyear_rcp26.set_index(timeseries_year_rcp26)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory
glue_first_jday_anoxic_deep_prof_inyear_rcp26.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/rcp26/glue_first_jday_anoxic_deep_prof_inyear_rcp26.csv')



# last_jday_anoxic_deep_prof_inyear_rcp26
timeseries_year_rcp26= all_last_jday_anoxic_deep_prof_inyear_rcp26.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_last_jday_anoxic_deep_prof_inyear_rcp26.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights_rcp26))

# Build glue df
glue_last_jday_anoxic_deep_prof_inyear_rcp26 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_last_jday_anoxic_deep_prof_inyear_rcp26=glue_last_jday_anoxic_deep_prof_inyear_rcp26.set_index(timeseries_year_rcp26)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory
glue_last_jday_anoxic_deep_prof_inyear_rcp26.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/rcp26/glue_last_jday_anoxic_deep_prof_inyear_rcp26.csv')

           

# len_anoxic_deep_prof_inyear_rcp26
timeseries_year_rcp26= all_len_anoxic_deep_prof_inyear_rcp26.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_len_anoxic_deep_prof_inyear_rcp26.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights_rcp26))

# Build glue df
glue_len_anoxic_deep_prof_inyear_rcp26 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_len_anoxic_deep_prof_inyear_rcp26=glue_len_anoxic_deep_prof_inyear_rcp26.set_index(timeseries_year_rcp26)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory
glue_len_anoxic_deep_prof_inyear_rcp26.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/rcp26/glue_len_anoxic_deep_prof_inyear_rcp26.csv')


#%%rcp60

# first_jday_anoxic_deep_prof_inyear_rcp60
timeseries_year_rcp60= all_first_jday_anoxic_deep_prof_inyear_rcp60.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_first_jday_anoxic_deep_prof_inyear_rcp60.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights_rcp60))

# Build glue df
glue_first_jday_anoxic_deep_prof_inyear_rcp60 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_first_jday_anoxic_deep_prof_inyear_rcp60=glue_first_jday_anoxic_deep_prof_inyear_rcp60.set_index(timeseries_year_rcp60)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory
glue_first_jday_anoxic_deep_prof_inyear_rcp60.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/rcp60/glue_first_jday_anoxic_deep_prof_inyear_rcp60.csv')



# last_jday_anoxic_deep_prof_inyear_rcp60
timeseries_year_rcp60= all_last_jday_anoxic_deep_prof_inyear_rcp60.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_last_jday_anoxic_deep_prof_inyear_rcp60.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights_rcp60))

# Build glue df
glue_last_jday_anoxic_deep_prof_inyear_rcp60 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_last_jday_anoxic_deep_prof_inyear_rcp60=glue_last_jday_anoxic_deep_prof_inyear_rcp60.set_index(timeseries_year_rcp60)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory
glue_last_jday_anoxic_deep_prof_inyear_rcp60.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/rcp60/glue_last_jday_anoxic_deep_prof_inyear_rcp60.csv')

           

# len_anoxic_deep_prof_inyear_rcp60
timeseries_year_rcp60= all_len_anoxic_deep_prof_inyear_rcp60.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_len_anoxic_deep_prof_inyear_rcp60.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights_rcp60))

# Build glue df
glue_len_anoxic_deep_prof_inyear_rcp60 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_len_anoxic_deep_prof_inyear_rcp60=glue_len_anoxic_deep_prof_inyear_rcp60.set_index(timeseries_year_rcp60)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory
glue_len_anoxic_deep_prof_inyear_rcp60.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/rcp60/glue_len_anoxic_deep_prof_inyear_rcp60.csv')

#%%rcp85

# first_jday_anoxic_deep_prof_inyear_rcp85
timeseries_year_rcp85= all_first_jday_anoxic_deep_prof_inyear_rcp85.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_first_jday_anoxic_deep_prof_inyear_rcp85.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights_rcp85))

# Build glue df
glue_first_jday_anoxic_deep_prof_inyear_rcp85 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_first_jday_anoxic_deep_prof_inyear_rcp85=glue_first_jday_anoxic_deep_prof_inyear_rcp85.set_index(timeseries_year_rcp85)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory
glue_first_jday_anoxic_deep_prof_inyear_rcp85.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/rcp85/glue_first_jday_anoxic_deep_prof_inyear_rcp85.csv')



# last_jday_anoxic_deep_prof_inyear_rcp85
timeseries_year_rcp85= all_last_jday_anoxic_deep_prof_inyear_rcp85.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_last_jday_anoxic_deep_prof_inyear_rcp85.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights_rcp85))

# Build glue df
glue_last_jday_anoxic_deep_prof_inyear_rcp85 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_last_jday_anoxic_deep_prof_inyear_rcp85=glue_last_jday_anoxic_deep_prof_inyear_rcp85.set_index(timeseries_year_rcp85)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory
glue_last_jday_anoxic_deep_prof_inyear_rcp85.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/rcp85/glue_last_jday_anoxic_deep_prof_inyear_rcp85.csv')

           

# len_anoxic_deep_prof_inyear_rcp85
timeseries_year_rcp85= all_len_anoxic_deep_prof_inyear_rcp85.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_len_anoxic_deep_prof_inyear_rcp85.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights_rcp85))

# Build glue df
glue_len_anoxic_deep_prof_inyear_rcp85 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_len_anoxic_deep_prof_inyear_rcp85=glue_len_anoxic_deep_prof_inyear_rcp85.set_index(timeseries_year_rcp85)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory
glue_len_anoxic_deep_prof_inyear_rcp85.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/rcp85/glue_len_anoxic_deep_prof_inyear_rcp85.csv')

#%%replaced by nan values 

glue_first_jday_anoxic_deep_prof_inyear_his=glue_first_jday_anoxic_deep_prof_inyear_his.replace(0, np.nan)

glue_first_jday_anoxic_deep_prof_inyear_rcp26=glue_first_jday_anoxic_deep_prof_inyear_rcp26.replace(0, np.nan)

glue_first_jday_anoxic_deep_prof_inyear_rcp60=glue_first_jday_anoxic_deep_prof_inyear_rcp60.replace(0, np.nan)

glue_first_jday_anoxic_deep_prof_inyear_rcp85=glue_first_jday_anoxic_deep_prof_inyear_rcp85.replace(0, np.nan)

#%%Sorting the glue first_jday dataframe according to the index (year)


glue_first_jday_anoxic_deep_prof_inyear_his=glue_first_jday_anoxic_deep_prof_inyear_his.sort_index()

glue_first_jday_anoxic_deep_prof_inyear_rcp26=glue_first_jday_anoxic_deep_prof_inyear_rcp26.sort_index()

glue_first_jday_anoxic_deep_prof_inyear_rcp60=glue_first_jday_anoxic_deep_prof_inyear_rcp60.sort_index()

glue_first_jday_anoxic_deep_prof_inyear_rcp85=glue_first_jday_anoxic_deep_prof_inyear_rcp85.sort_index()


#%%Sorting the glue dataframe according to the index (year)

glue_len_anoxic_deep_prof_inyear_his=glue_len_anoxic_deep_prof_inyear_his.sort_index()

glue_len_anoxic_deep_prof_inyear_rcp26=glue_len_anoxic_deep_prof_inyear_rcp26.sort_index()

glue_len_anoxic_deep_prof_inyear_rcp60=glue_len_anoxic_deep_prof_inyear_rcp60.sort_index()

glue_len_anoxic_deep_prof_inyear_rcp85=glue_len_anoxic_deep_prof_inyear_rcp85.sort_index()


#%%Plotiing%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

#%%duration of deep anoxia 



os.chdir('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/')

import matplotlib.pyplot as plt

fig =plt.figure(figsize=(15, 10))
ax= plt.subplot(111)


ax=plt.fill_between(glue_len_anoxic_deep_prof_inyear_his.index.astype(float), glue_len_anoxic_deep_prof_inyear_his['5%'], glue_len_anoxic_deep_prof_inyear_his['95%'], color='grey', alpha=0.2 ,  label= 'His 90% CI')
ax=plt.plot(glue_len_anoxic_deep_prof_inyear_his.index.astype(float), glue_len_anoxic_deep_prof_inyear_his['50%'].astype(float), 'k', label='His median', alpha=0.9, linewidth=3  )


ax=plt.fill_between(glue_len_anoxic_deep_prof_inyear_rcp26.index.astype(float), glue_len_anoxic_deep_prof_inyear_rcp26['5%'], glue_len_anoxic_deep_prof_inyear_rcp26['95%'], color='green', alpha=0.3 ,  label= 'RCP2.6 90% CI')
ax=plt.plot(glue_len_anoxic_deep_prof_inyear_rcp26.index.astype(float), glue_len_anoxic_deep_prof_inyear_rcp26['50%'].astype(float), 'darkgreen', label='RCP2.6 median', alpha=0.9, linewidth=3  )

ax=plt.fill_between(glue_len_anoxic_deep_prof_inyear_rcp60.index.astype(float), glue_len_anoxic_deep_prof_inyear_rcp60['5%'], glue_len_anoxic_deep_prof_inyear_rcp60['95%'], color='yellow', alpha=0.6 ,  label= 'RCP6.0 90% CI')
ax=plt.plot(glue_len_anoxic_deep_prof_inyear_rcp60.index.astype(float), glue_len_anoxic_deep_prof_inyear_rcp60['50%'].astype(float), 'yellow', label='RCP6.0 median', alpha=0.9, linewidth=3  )

ax=plt.fill_between(glue_len_anoxic_deep_prof_inyear_rcp85.index.astype(float), glue_len_anoxic_deep_prof_inyear_rcp85['5%'], glue_len_anoxic_deep_prof_inyear_rcp85['95%'], color='red', alpha=0.2 ,  label= 'RCP8.5 90% CI')
ax=plt.plot(glue_len_anoxic_deep_prof_inyear_rcp85.index.astype(float), glue_len_anoxic_deep_prof_inyear_rcp85['50%'].astype(float), 'r', label='RCP8.5 median', alpha=0.9, linewidth=3  )

ax=plt.ylabel('Duration of deep anoxia [d]' , fontsize=26)
ax=plt.xlabel('Year' , fontsize=26)
ax=plt.yticks(fontsize= 22)
ax=plt.xticks(rotation=45 , fontsize=22)
ax=plt.legend(bbox_to_anchor=(1.1, -0.2), fontsize=22, ncol= 4)#)   
fig.savefig("GLUE_Timeseries_length_deep_anoxic_16combinationJaJv_ave_obs_4models_4scenarios.png",  dpi=300, bbox_inches='tight')



#%%
np.mean(glue_len_anoxic_deep_prof_inyear_his['50%'])#42.628996316914595
np.mean(glue_len_anoxic_deep_prof_inyear_rcp26['50%'])#56.86893319160042
np.mean(glue_len_anoxic_deep_prof_inyear_rcp60['50%'])#59.38530456330427
np.mean(glue_len_anoxic_deep_prof_inyear_rcp85['50%'])#64.35613805410296

#%%anoxic_factor 30 yerars from each scenarios compare 



#anomaly 
# baseline [1976-2005]
len_anoxic_deep_prof_inyear_ref=glue_len_anoxic_deep_prof_inyear_his[1975 < glue_len_anoxic_deep_prof_inyear_his.index]['50%'].mean()
#43.32810197556075

#near future [2030-2059] # maximum temp in 2033

glue_len_anoxic_deep_prof_inyear_rcp26[(2029 < glue_len_anoxic_deep_prof_inyear_rcp26.index) & (glue_len_anoxic_deep_prof_inyear_rcp26.index < 2060)]['50%'].mean()
# 57.9629971913236
glue_len_anoxic_deep_prof_inyear_rcp60[(2029 < glue_len_anoxic_deep_prof_inyear_rcp60.index) & (glue_len_anoxic_deep_prof_inyear_rcp60.index < 2060)]['50%'].mean()
# 56.24601250273317
glue_len_anoxic_deep_prof_inyear_rcp85[(2029 < glue_len_anoxic_deep_prof_inyear_rcp85.index) & (glue_len_anoxic_deep_prof_inyear_rcp85.index < 2060)]['50%'].mean()
# 59.78116471767154

 
#Distant future [2070-2099]

glue_len_anoxic_deep_prof_inyear_rcp26[(2069 < glue_len_anoxic_deep_prof_inyear_rcp26.index) & (glue_len_anoxic_deep_prof_inyear_rcp26.index < 2100)]['50%'].mean()
# 58.3558445459188
glue_len_anoxic_deep_prof_inyear_rcp60[(2069 < glue_len_anoxic_deep_prof_inyear_rcp60.index) & (glue_len_anoxic_deep_prof_inyear_rcp60.index< 2100)]['50%'].mean()
# 67.39018268983682
glue_len_anoxic_deep_prof_inyear_rcp85[(2069 < glue_len_anoxic_deep_prof_inyear_rcp85.index) & (glue_len_anoxic_deep_prof_inyear_rcp85.index < 2100)]['50%'].mean()
#77.4759964499702
           



#%%len of deep anoxia_anomaly 
os.chdir('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/')

import matplotlib.pyplot as plt

fig =plt.figure(figsize=(15, 10))
ax= plt.subplot(111)


ax=plt.fill_between(glue_len_anoxic_deep_prof_inyear_his[1975 < glue_len_anoxic_deep_prof_inyear_his.index].index.astype(float),
                      glue_len_anoxic_deep_prof_inyear_his[1975 < glue_len_anoxic_deep_prof_inyear_his.index]['5%'] - len_anoxic_deep_prof_inyear_ref,
                      glue_len_anoxic_deep_prof_inyear_his[1975 < glue_len_anoxic_deep_prof_inyear_his.index ]['95%'] - len_anoxic_deep_prof_inyear_ref,
                      color='grey', alpha=0.2, label='His 90% CI')


ax=plt.plot(glue_len_anoxic_deep_prof_inyear_his[1975< glue_len_anoxic_deep_prof_inyear_his.index ].index.astype(float),
            glue_len_anoxic_deep_prof_inyear_his[1975 < glue_len_anoxic_deep_prof_inyear_his.index]['50%'] - len_anoxic_deep_prof_inyear_ref,
            'k', label='His median', alpha=0.9, linewidth=3   )

ax=plt.fill_between(glue_len_anoxic_deep_prof_inyear_rcp26.index.astype(float), glue_len_anoxic_deep_prof_inyear_rcp26['5%']-len_anoxic_deep_prof_inyear_ref, glue_len_anoxic_deep_prof_inyear_rcp26['95%']-len_anoxic_deep_prof_inyear_ref, color='darkgreen', alpha=0.2 ,  label= 'RCP6.0 90% CI')
ax=plt.plot(glue_len_anoxic_deep_prof_inyear_rcp26.index.astype(float), glue_len_anoxic_deep_prof_inyear_rcp26['50%']-len_anoxic_deep_prof_inyear_ref, 'darkgreen', label='RCP6.0 median', alpha=0.9, linewidth=3  )
                      
                     
ax=plt.fill_between(glue_len_anoxic_deep_prof_inyear_rcp60.index.astype(float), glue_len_anoxic_deep_prof_inyear_rcp60['5%']-len_anoxic_deep_prof_inyear_ref, glue_len_anoxic_deep_prof_inyear_rcp60['95%']-len_anoxic_deep_prof_inyear_ref, color='yellow', alpha=0.5 ,  label= 'RCP6.0 90% CI')
ax=plt.plot(glue_len_anoxic_deep_prof_inyear_rcp60.index.astype(float), glue_len_anoxic_deep_prof_inyear_rcp60['50%']-len_anoxic_deep_prof_inyear_ref, 'yellow', label='RCP6.0 median', alpha=0.9, linewidth=3  )

ax=plt.fill_between(glue_len_anoxic_deep_prof_inyear_rcp85.index.astype(float), glue_len_anoxic_deep_prof_inyear_rcp85['5%']-len_anoxic_deep_prof_inyear_ref, glue_len_anoxic_deep_prof_inyear_rcp85['95%']-len_anoxic_deep_prof_inyear_ref, color='r', alpha=0.2 ,  label= 'RCP8.5 90% CI')
ax=plt.plot(glue_len_anoxic_deep_prof_inyear_rcp85.index.astype(float), glue_len_anoxic_deep_prof_inyear_rcp85['50%']-len_anoxic_deep_prof_inyear_ref, 'r', label='RCP8.5 median', alpha=0.9, linewidth=3  )

ax=plt.ylabel('Anomaly of deepest layer anoxia duration [d]' , fontsize=26)
ax=plt.xlabel('Year' , fontsize=26)
ax=plt.yticks(fontsize= 22)
ax=plt.xticks(rotation=45 , fontsize=22)
ax=plt.legend(bbox_to_anchor=(1.1, -0.2), fontsize=22 , ncol=4)  
fig.savefig("GLUE_Timeseries_len_anoxic_deep_prof_anomaly_16combinationJaJv_ave_obs_4models_4scenarios.png",  dpi=300, bbox_inches='tight')

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% condition ###############
#########################################################################

#%%Plotiing%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

#%%First Jday with deep anoxic



os.chdir('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/')

import matplotlib.pyplot as plt

fig =plt.figure(figsize=(15, 10))
ax= plt.subplot(111)


ax=plt.fill_between(glue_first_jday_anoxic_deep_prof_inyear_his.index.astype(float), glue_first_jday_anoxic_deep_prof_inyear_his['5%'], glue_first_jday_anoxic_deep_prof_inyear_his['95%'], color='grey', alpha=0.2 ,  label= 'His 90% CI')
ax=plt.plot(glue_first_jday_anoxic_deep_prof_inyear_his.index.astype(float), glue_first_jday_anoxic_deep_prof_inyear_his['50%'].astype(float), 'k', label='His median', alpha=0.9, linewidth=3  )


ax=plt.fill_between(glue_first_jday_anoxic_deep_prof_inyear_rcp26.index.astype(float), glue_first_jday_anoxic_deep_prof_inyear_rcp26['5%'], glue_first_jday_anoxic_deep_prof_inyear_rcp26['95%'], color='darkgreen', alpha=0.3 ,  label= 'RCP2.6 90% CI')
ax=plt.plot(glue_first_jday_anoxic_deep_prof_inyear_rcp26.index.astype(float), glue_first_jday_anoxic_deep_prof_inyear_rcp26['50%'].astype(float), 'darkgreen', label='RCP2.6 median', alpha=0.9, linewidth=3  )

ax=plt.fill_between(glue_first_jday_anoxic_deep_prof_inyear_rcp60.index.astype(float), glue_first_jday_anoxic_deep_prof_inyear_rcp60['5%'], glue_first_jday_anoxic_deep_prof_inyear_rcp60['95%'], color='yellow', alpha=0.5,  label= 'RCP6.0 90% CI')
ax=plt.plot(glue_first_jday_anoxic_deep_prof_inyear_rcp60.index.astype(float), glue_first_jday_anoxic_deep_prof_inyear_rcp60['50%'].astype(float), 'yellow', label='RCP6.0 median', alpha=0.9, linewidth=3  )

ax=plt.fill_between(glue_first_jday_anoxic_deep_prof_inyear_rcp85.index.astype(float), glue_first_jday_anoxic_deep_prof_inyear_rcp85['5%'], glue_first_jday_anoxic_deep_prof_inyear_rcp85['95%'], color='red', alpha=0.2 ,  label= 'RCP8.5 90% CI')
ax=plt.plot(glue_first_jday_anoxic_deep_prof_inyear_rcp85.index.astype(float), glue_first_jday_anoxic_deep_prof_inyear_rcp85['50%'].astype(float), 'r', label='RCP8.5 median', alpha=0.9, linewidth=3  )

ax=plt.ylabel('First deep anoxia [Jday]' , fontsize=26)
ax=plt.xlabel('Year' , fontsize=26)
ax=plt.yticks(fontsize= 22)
ax=plt.xticks(rotation=45 , fontsize=22)
ax=plt.legend(bbox_to_anchor=(1.1, -0.2), fontsize=22, ncol=4)#)   
fig.savefig("GLUE_Timeseries_first_deep_anoxic_16combinationJaJv_ave_obs_4models_4scenarios.png",  dpi=300, bbox_inches='tight')




#%%
np.mean(glue_first_jday_anoxic_deep_prof_inyear_his['50%'])#198.15030513270509
np.mean(glue_first_jday_anoxic_deep_prof_inyear_rcp26['50%'])#191.79536637948485
np.mean(glue_first_jday_anoxic_deep_prof_inyear_rcp60['50%'])#189.57264351525544
np.mean(glue_first_jday_anoxic_deep_prof_inyear_rcp85['50%'])# 186.54216485962053

#%%anoxic_factor 30 yerars from each scenarios compare 


#anomaly 
# his [1976-2005]
first_jday_anoxic_deep_prof_inyear_ref=glue_first_jday_anoxic_deep_prof_inyear_his[1975< glue_first_jday_anoxic_deep_prof_inyear_his.index]['50%'].mean()
#201.56606960912438


#near future [2030-205]

glue_first_jday_anoxic_deep_prof_inyear_rcp26[(2029 < glue_first_jday_anoxic_deep_prof_inyear_rcp26.index) & (glue_first_jday_anoxic_deep_prof_inyear_rcp26.index < 2060)]['50%'].mean()
#191.2690766329525
glue_first_jday_anoxic_deep_prof_inyear_rcp60[(2029 < glue_first_jday_anoxic_deep_prof_inyear_rcp60.index) & (glue_first_jday_anoxic_deep_prof_inyear_rcp60.index < 2060)]['50%'].mean()
#190.87297983597688
glue_first_jday_anoxic_deep_prof_inyear_rcp85[(2029 < glue_first_jday_anoxic_deep_prof_inyear_rcp85.index) & (glue_first_jday_anoxic_deep_prof_inyear_rcp85.index < 2060)]['50%'].mean()
#188.84957458598092

 
#Distant future [2070-2099]

glue_first_jday_anoxic_deep_prof_inyear_rcp26[(2069 < glue_first_jday_anoxic_deep_prof_inyear_rcp26.index) & (glue_first_jday_anoxic_deep_prof_inyear_rcp26.index < 2100)]['50%'].mean()
#190.81011321212333
glue_first_jday_anoxic_deep_prof_inyear_rcp60[(2069 < glue_first_jday_anoxic_deep_prof_inyear_rcp60.index) & (glue_first_jday_anoxic_deep_prof_inyear_rcp60.index < 2100)]['50%'].mean()
#184.3338306798117
glue_first_jday_anoxic_deep_prof_inyear_rcp85[(2069 < glue_first_jday_anoxic_deep_prof_inyear_rcp85.index) & (glue_first_jday_anoxic_deep_prof_inyear_rcp85.index < 2100)]['50%'].mean()
#180.24849508075735
           



#%%depletion_rate_anomaly 
os.chdir('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/')

import matplotlib.pyplot as plt

fig =plt.figure(figsize=(15, 10))
ax= plt.subplot(111)


ax=plt.fill_between(glue_first_jday_anoxic_deep_prof_inyear_his[1975 < glue_first_jday_anoxic_deep_prof_inyear_his.index].index.astype(float),
                      glue_first_jday_anoxic_deep_prof_inyear_his[1975 < glue_first_jday_anoxic_deep_prof_inyear_his.index]['5%'] - first_jday_anoxic_deep_prof_inyear_ref,
                      glue_first_jday_anoxic_deep_prof_inyear_his[1975 < glue_first_jday_anoxic_deep_prof_inyear_his.index]['95%'] - first_jday_anoxic_deep_prof_inyear_ref,
                      color='grey', alpha=0.2, label='His 90% CI')


ax=plt.plot(glue_first_jday_anoxic_deep_prof_inyear_his[1975 < glue_first_jday_anoxic_deep_prof_inyear_his.index ].index.astype(float),
            glue_first_jday_anoxic_deep_prof_inyear_his[1975 < glue_first_jday_anoxic_deep_prof_inyear_his.index]['50%'] - first_jday_anoxic_deep_prof_inyear_ref,
            'k', label='His median', alpha=0.9, linewidth=3   )

ax=plt.fill_between(glue_first_jday_anoxic_deep_prof_inyear_rcp26.index.astype(float), glue_first_jday_anoxic_deep_prof_inyear_rcp26['5%']-first_jday_anoxic_deep_prof_inyear_ref, glue_first_jday_anoxic_deep_prof_inyear_rcp26['95%']-first_jday_anoxic_deep_prof_inyear_ref, color='darkgreen', alpha=0.3 ,  label= 'RCP6.0 90% CI')
ax=plt.plot(glue_first_jday_anoxic_deep_prof_inyear_rcp26.index.astype(float), glue_first_jday_anoxic_deep_prof_inyear_rcp26['50%']-first_jday_anoxic_deep_prof_inyear_ref, 'darkgreen', label='RCP6.0 median', alpha=0.9, linewidth=3  )
                      
                     
ax=plt.fill_between(glue_first_jday_anoxic_deep_prof_inyear_rcp60.index.astype(float), glue_first_jday_anoxic_deep_prof_inyear_rcp60['5%']-first_jday_anoxic_deep_prof_inyear_ref, glue_first_jday_anoxic_deep_prof_inyear_rcp60['95%']-first_jday_anoxic_deep_prof_inyear_ref, color='yellow', alpha=0.5 ,  label= 'RCP6.0 90% CI')
ax=plt.plot(glue_first_jday_anoxic_deep_prof_inyear_rcp60.index.astype(float), glue_first_jday_anoxic_deep_prof_inyear_rcp60['50%']-first_jday_anoxic_deep_prof_inyear_ref, 'yellow', label='RCP6.0 median', alpha=0.9, linewidth=3  )

ax=plt.fill_between(glue_first_jday_anoxic_deep_prof_inyear_rcp85.index.astype(float), glue_first_jday_anoxic_deep_prof_inyear_rcp85['5%']-first_jday_anoxic_deep_prof_inyear_ref, glue_first_jday_anoxic_deep_prof_inyear_rcp85['95%']-first_jday_anoxic_deep_prof_inyear_ref, color='r', alpha=0.2 ,  label= 'RCP8.5 90% CI')
ax=plt.plot(glue_first_jday_anoxic_deep_prof_inyear_rcp85.index.astype(float), glue_first_jday_anoxic_deep_prof_inyear_rcp85['50%']-first_jday_anoxic_deep_prof_inyear_ref, 'r', label='RCP8.5 median', alpha=0.9, linewidth=3  )

ax=plt.ylabel('Anomaly of deepest layer anoxia onset [Jday]' , fontsize=26)
ax=plt.xlabel('Year' , fontsize=26)
ax=plt.yticks(fontsize= 22)
ax=plt.xticks(rotation=45 , fontsize=22)
ax=plt.legend(bbox_to_anchor=(1.1, -0.2), fontsize=22 , ncol= 4)  
fig.savefig("GLUE_Timeseries_first_jday_anoxia_deep_prof_anomaly_16combinationJaJv_ave_obs_4models_4scenarios.png",  dpi=300, bbox_inches='tight')

#%% Histogram or violn plot 

    
median_first_jday_anoxic_deep_prof_his=glue_first_jday_anoxic_deep_prof_inyear_his['50%']
median_first_jday_anoxic_deep_prof_rcp26=glue_first_jday_anoxic_deep_prof_inyear_rcp26['50%']
median_first_jday_anoxic_deep_prof_rcp60=glue_first_jday_anoxic_deep_prof_inyear_rcp60['50%']
median_first_jday_anoxic_deep_prof_rcp85=glue_first_jday_anoxic_deep_prof_inyear_rcp85['50%']  
    
# Create a DataFrame with NaN values
df_first_jday_anoxic_deep_prof_4models =pd.concat([
    pd.Series(median_first_jday_anoxic_deep_prof_his, name='His' ),
    pd.Series(median_first_jday_anoxic_deep_prof_rcp26, name='RCP2.6'),
    pd.Series(median_first_jday_anoxic_deep_prof_rcp60, name='RCP6.0' ),
    pd.Series(median_first_jday_anoxic_deep_prof_rcp85, name='RCP8.5' )], axis=1)    
    
    

    
median_len_anoxic_deep_prof_his=glue_len_anoxic_deep_prof_inyear_his['50%']
median_len_anoxic_deep_prof_rcp26=glue_len_anoxic_deep_prof_inyear_rcp26['50%']
median_len_anoxic_deep_prof_rcp60=glue_len_anoxic_deep_prof_inyear_rcp60['50%']
median_len_anoxic_deep_prof_rcp85=glue_len_anoxic_deep_prof_inyear_rcp85['50%']  
    
# Create a DataFrame with NaN values
df_len_anoxic_deep_prof_4models =pd.concat([
    pd.Series(median_len_anoxic_deep_prof_his, name='His' ),
    pd.Series(median_len_anoxic_deep_prof_rcp26, name='RCP2.6'),
    pd.Series(median_len_anoxic_deep_prof_rcp60, name='RCP6.0' ),
    pd.Series(median_len_anoxic_deep_prof_rcp85, name='RCP8.5' )], axis=1)    
    
    
median_last_jday_anoxic_deep_prof_his=glue_last_jday_anoxic_deep_prof_inyear_his['50%']
median_last_jday_anoxic_deep_prof_rcp26=glue_last_jday_anoxic_deep_prof_inyear_rcp26['50%']
median_last_jday_anoxic_deep_prof_rcp60=glue_last_jday_anoxic_deep_prof_inyear_rcp60['50%']
median_last_jday_anoxic_deep_prof_rcp85=glue_last_jday_anoxic_deep_prof_inyear_rcp85['50%']  
    
# Create a DataFrame with NaN values
df_last_jday_anoxic_deep_prof_4models =pd.concat([
    pd.Series(median_last_jday_anoxic_deep_prof_his, name='His' ),
    pd.Series(median_last_jday_anoxic_deep_prof_rcp26, name='RCP2.6'),
    pd.Series(median_last_jday_anoxic_deep_prof_rcp60, name='RCP6.0' ),
    pd.Series(median_last_jday_anoxic_deep_prof_rcp85, name='RCP8.5' )], axis=1)    
    
    
    


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
sns.violinplot(ax=axes[0], data=df_first_jday_anoxic_deep_prof_4models, palette=custom_palette)
axes[0].set_ylabel('Deepest layer anoxia onset [Jday]')

#axes[0].set_ylim(60, 210)  # Set the y-axis limits
axes[0].set_yticks(range(120, 230, 30))  # Set the y-axis ticks at intervals of 20



plt.subplots_adjust(wspace=0.3)
sns.violinplot(ax=axes[1], data=df_len_anoxic_deep_prof_4models, palette=custom_palette)
axes[1].set_ylabel('Deepest layer anoxia duration [day]')
axes[1].set_yticks(range(0, 150, 30))  # Set the y-axis ticks at intervals of 20



#sns.violinplot(ax=axes[2], data=df_last_jday_anoxic_deep_prof_4models, palette=custom_palette)
#axes[2].set_ylabel('Last day of deep anoxia [day]')
#axes[2].set_yticks(range(180, 300, 30))  # Set the y-axis ticks at intervals of 20



plt.savefig("allsenarios_4models_median_first_len_of_deep_anoxia.png", dpi=300)







#%% averaging over whole scenarios value 
np.mean(glue_len_anoxic_deep_prof_inyear_his['50%'])#42.628996316914595
np.mean(glue_len_anoxic_deep_prof_inyear_rcp26['50%'])#56.86893319160042
np.mean(glue_len_anoxic_deep_prof_inyear_rcp60['50%'])#59.38530456330427
np.mean(glue_len_anoxic_deep_prof_inyear_rcp85['50%'])#64.35613805410296



#%%anoxic_duration 30 yerars from each scenarios compare 



#anomaly 
# baseline [1976-2005]
glue_base_len_anoxic_deep_prof_his=glue_len_anoxic_deep_prof_inyear_his[1975 < glue_len_anoxic_deep_prof_inyear_his.index]['50%']
len_anoxic_deep_prof_ref=np.mean(glue_base_len_anoxic_deep_prof_his)
#43.32810197556075


#near future [2030-2059]

glue_near_future_len_anoxic_deep_prof_rcp26=glue_len_anoxic_deep_prof_inyear_rcp26[(2029 < glue_len_anoxic_deep_prof_inyear_rcp26.index) & (glue_len_anoxic_deep_prof_inyear_rcp26.index < 2060)]['50%']
np.mean(glue_near_future_len_anoxic_deep_prof_rcp26)
#57.9629971913236
glue_near_future_len_anoxic_deep_prof_rcp60=glue_len_anoxic_deep_prof_inyear_rcp60[(2029 < glue_len_anoxic_deep_prof_inyear_rcp60.index) & (glue_len_anoxic_deep_prof_inyear_rcp60.index < 2060)]['50%']
np.mean(glue_near_future_len_anoxic_deep_prof_rcp60)
# 56.24601250273317
glue_near_future_len_anoxic_deep_prof_rcp85=glue_len_anoxic_deep_prof_inyear_rcp85[(2029 < glue_len_anoxic_deep_prof_inyear_rcp85.index) & (glue_len_anoxic_deep_prof_inyear_rcp85.index < 2060)]['50%']
np.mean(glue_near_future_len_anoxic_deep_prof_rcp85)
#59.78116471767154

 
#Distant future [2070-2099]

glue_distant_future_len_anoxic_deep_prof_rcp26=glue_len_anoxic_deep_prof_inyear_rcp26[(2069 < glue_len_anoxic_deep_prof_inyear_rcp26.index) & (glue_len_anoxic_deep_prof_inyear_rcp26.index < 2100)]['50%']
np.mean(glue_distant_future_len_anoxic_deep_prof_rcp26)
#58.3558445459188
glue_distant_future_len_anoxic_deep_prof_rcp60=glue_len_anoxic_deep_prof_inyear_rcp60[(2069 < glue_len_anoxic_deep_prof_inyear_rcp60.index) & (glue_len_anoxic_deep_prof_inyear_rcp60.index< 2100)]['50%']
np.mean(glue_distant_future_len_anoxic_deep_prof_rcp60)
#67.39018268983682
glue_distant_future_len_anoxic_deep_prof_rcp85=glue_len_anoxic_deep_prof_inyear_rcp85[(2069 < glue_len_anoxic_deep_prof_inyear_rcp85.index) & (glue_len_anoxic_deep_prof_inyear_rcp85.index < 2100)]['50%']
np.mean(glue_distant_future_len_anoxic_deep_prof_rcp85)
#77.4759964499702
   


###====over 30 years in his and each RCPs 

# baseline [1976-2005]
autocorr_MK_org_modif_sens_slope_test(glue_base_len_anoxic_deep_prof_his)
(0.05884463376988538,
 'positively autocorrelated',
 'increasing',
 0.028077978752723665,
 0.3201597080870893,
 38.357684232737206)

#near future [2030-2059]


autocorr_MK_org_modif_sens_slope_test(glue_near_future_len_anoxic_deep_prof_rcp26)
(0.03985835208003137,
 'positively autocorrelated',
 'increasing',
 0.04746325405912266,
 0.3343962824295881,
 50.151253904770975)

autocorr_MK_org_modif_sens_slope_test(glue_near_future_len_anoxic_deep_prof_rcp60)
(0.011722417105355393,
 'positively autocorrelated',
 'increasing',
 0.04466067414446684,
 0.23891651556212898,
 53.319170251032205)

autocorr_MK_org_modif_sens_slope_test(glue_near_future_len_anoxic_deep_prof_rcp85)

(0.028585428597251872,
 'positively autocorrelated',
 'increasing',
 0.010720691059205922,
 0.41758464583529,
 52.709310897041064)


#Distant future [2070-2099]


autocorr_MK_org_modif_sens_slope_test(glue_distant_future_len_anoxic_deep_prof_rcp26)
(0.04094712552857874,
 'positively autocorrelated',
 'no trend',
 0.30942513881081934,
 0,
 0)

autocorr_MK_org_modif_sens_slope_test(glue_distant_future_len_anoxic_deep_prof_rcp60)
(0.013655335525177104,
 'positively autocorrelated',
 'no trend',
 0.11877798973022413,
 0,
 0)

autocorr_MK_org_modif_sens_slope_test(glue_distant_future_len_anoxic_deep_prof_rcp85)
(0.023082988430137702,
 'positively autocorrelated',
 'increasing',
 0.0017954443431502654,
 0.47368421052631576,
 70.20126659644232)



#%% Trendlines over whole periods:
# no trend in his but increasing trendlines of all rcps 
# for length of deep anoxia    
    
# his     
  
autocorr_MK_org_modif_sens_slope_test(glue_len_anoxic_deep_prof_inyear_his['50%'])
"""
(0.062431563881428065,
 'positively autocorrelated',
 'no trend',
 0.9927857948451586,
 0,
 0)
"""
#rcp26
autocorr_MK_org_modif_sens_slope_test(glue_len_anoxic_deep_prof_inyear_rcp26['50%'])
"""
(0.03888068916462068,
 'positively autocorrelated',
 'increasing',
 0.0014855195203318239,
 0.08663656009797585,
 51.22763007686477)
"""

#rcp60
autocorr_MK_org_modif_sens_slope_test(glue_len_anoxic_deep_prof_inyear_rcp60['50%'])
"""
(0.015110986297192814,
 'positively autocorrelated',
 'increasing',
 0.0,
 0.2236784847564093,
 48.40837707359544)
"""

#rcp85
autocorr_MK_org_modif_sens_slope_test(glue_len_anoxic_deep_prof_inyear_rcp85['50%'])
"""
(0.03060084167872865,
 'positively autocorrelated',
 'increasing',
 0.0,
 0.3898305084745763,
 44.87288135593221)
"""





#%% 80 years from 2020 for len_anoxic_deep_prof


glue_80years_len_anoxic_deep_prof_inyear_rcp26=glue_len_anoxic_deep_prof_inyear_rcp26[2019 < glue_len_anoxic_deep_prof_inyear_rcp26.index]

glue_80years_len_anoxic_deep_prof_inyear_rcp60=glue_len_anoxic_deep_prof_inyear_rcp60[2019 < glue_len_anoxic_deep_prof_inyear_rcp60.index]


glue_80years_len_anoxic_deep_prof_inyear_rcp85=glue_len_anoxic_deep_prof_inyear_rcp85[2019 < glue_len_anoxic_deep_prof_inyear_rcp85.index]


#============= mean of first 10 yaers over 80 years 

#rcp2.6
np.mean(glue_80years_len_anoxic_deep_prof_inyear_rcp26[glue_80years_len_anoxic_deep_prof_inyear_rcp26.index<2030]['50%'])
57.3191017282251

#rcp6.0
np.mean(glue_80years_len_anoxic_deep_prof_inyear_rcp60[glue_80years_len_anoxic_deep_prof_inyear_rcp60.index<2030]['50%'])
54.03528555520664

#rcp8.5
np.mean(glue_80years_len_anoxic_deep_prof_inyear_rcp85[glue_80years_len_anoxic_deep_prof_inyear_rcp85.index<2030]['50%'])
55.129918211584126

#============== mean of last 10 yaers over 80 years 

#rcp2.6
np.mean(glue_80years_len_anoxic_deep_prof_inyear_rcp26[glue_80years_len_anoxic_deep_prof_inyear_rcp26.index>2089]['50%'])
59.25927947680982

#rcp6.0
np.mean(glue_80years_len_anoxic_deep_prof_inyear_rcp60[glue_80years_len_anoxic_deep_prof_inyear_rcp60.index>2089]['50%'])
68.65690570928328

#rcp8.5
np.mean(glue_80years_len_anoxic_deep_prof_inyear_rcp85[glue_80years_len_anoxic_deep_prof_inyear_rcp85.index>2089]['50%'])
86.01149296223714

#=========== trendline # Over the 80 years


autocorr_MK_org_modif_sens_slope_test(glue_80years_len_anoxic_deep_prof_inyear_rcp26['50%'])
(0.04052327783240534,
 'positively autocorrelated',
 'no trend',
 0.17407813723571652,
 0,
 0)
autocorr_MK_org_modif_sens_slope_test(glue_80years_len_anoxic_deep_prof_inyear_rcp60['50%'])
(0.012975166047628899,
 'positively autocorrelated',
 'increasing',
 5.1514348342607263e-14,
 0.24449856027796846,
 51.142578166092704)

autocorr_MK_org_modif_sens_slope_test(glue_80years_len_anoxic_deep_prof_inyear_rcp85['50%'])
(0.024208458152022414,
 'positively autocorrelated',
 'increasing',
 1.1102230246251565e-15,
 0.4,
 49.95623012142066)



#%% averaging over whole scenarios value for first anoxia deep profile 

np.mean(glue_first_jday_anoxic_deep_prof_inyear_his['50%'])#198.15030513270509
np.mean(glue_first_jday_anoxic_deep_prof_inyear_rcp26['50%'])#191.79536637948485
np.mean(glue_first_jday_anoxic_deep_prof_inyear_rcp60['50%'])#189.57264351525544
np.mean(glue_first_jday_anoxic_deep_prof_inyear_rcp85['50%'])#186.54216485962053



#%%anoxic_duration 30 yerars from each scenarios compare 



#anomaly 
# baseline [1976-2005]
glue_base_first_jday_anoxic_deep_prof_his=glue_first_jday_anoxic_deep_prof_inyear_his[1975 < glue_first_jday_anoxic_deep_prof_inyear_his.index]['50%']
len_anoxic_deep_prof_ref=np.mean(glue_base_first_jday_anoxic_deep_prof_his)
#201.56606960912438


#near future [2030-2059]

glue_near_future_first_jday_anoxic_deep_prof_rcp26=glue_first_jday_anoxic_deep_prof_inyear_rcp26[(2029 < glue_first_jday_anoxic_deep_prof_inyear_rcp26.index) & (glue_first_jday_anoxic_deep_prof_inyear_rcp26.index < 2060)]['50%']
np.mean(glue_near_future_first_jday_anoxic_deep_prof_rcp26)
#191.2690766329525
glue_near_future_first_jday_anoxic_deep_prof_rcp60=glue_first_jday_anoxic_deep_prof_inyear_rcp60[(2029 < glue_first_jday_anoxic_deep_prof_inyear_rcp60.index) & (glue_first_jday_anoxic_deep_prof_inyear_rcp60.index < 2060)]['50%']
np.mean(glue_near_future_first_jday_anoxic_deep_prof_rcp60)
#190.87297983597688
glue_near_future_first_jday_anoxic_deep_prof_rcp85=glue_first_jday_anoxic_deep_prof_inyear_rcp85[(2029 < glue_first_jday_anoxic_deep_prof_inyear_rcp85.index) & (glue_first_jday_anoxic_deep_prof_inyear_rcp85.index < 2060)]['50%']
np.mean(glue_near_future_first_jday_anoxic_deep_prof_rcp85)
#188.84957458598092

 
#Distant future [2070-2099]

glue_distant_future_first_jday_anoxic_deep_prof_rcp26=glue_first_jday_anoxic_deep_prof_inyear_rcp26[(2069 < glue_first_jday_anoxic_deep_prof_inyear_rcp26.index) & (glue_first_jday_anoxic_deep_prof_inyear_rcp26.index < 2100)]['50%']
np.mean(glue_distant_future_first_jday_anoxic_deep_prof_rcp26)
#190.81011321212333
glue_distant_future_first_jday_anoxic_deep_prof_rcp60=glue_first_jday_anoxic_deep_prof_inyear_rcp60[(2069 < glue_first_jday_anoxic_deep_prof_inyear_rcp60.index) & (glue_first_jday_anoxic_deep_prof_inyear_rcp60.index< 2100)]['50%']
np.mean(glue_distant_future_first_jday_anoxic_deep_prof_rcp60)
#184.3338306798117
glue_distant_future_first_jday_anoxic_deep_prof_rcp85=glue_first_jday_anoxic_deep_prof_inyear_rcp85[(2069 < glue_first_jday_anoxic_deep_prof_inyear_rcp85.index) & (glue_first_jday_anoxic_deep_prof_inyear_rcp85.index < 2100)]['50%']
np.mean(glue_distant_future_first_jday_anoxic_deep_prof_rcp85)
#180.24849508075735
   


###====over 30 years in his and each RCPs 

# baseline [1976-2005]
autocorr_MK_org_modif_sens_slope_test(glue_base_first_jday_anoxic_deep_prof_his)
(0.0011733726093675193,
 'positively autocorrelated',
 'no trend',
 0.5515600408950192,
 0,
 0)

#near future [2030-2059]


autocorr_MK_org_modif_sens_slope_test(glue_near_future_first_jday_anoxic_deep_prof_rcp26)
(0.003384340577810356,
 'positively autocorrelated',
 'no trend',
 0.36249694706219016,
 0,
 0)

autocorr_MK_org_modif_sens_slope_test(glue_near_future_first_jday_anoxic_deep_prof_rcp60)
(0.0007625670738953188,
 'positively autocorrelated',
 'no trend',
 0.30807644325017014,
 0,
 0)

autocorr_MK_org_modif_sens_slope_test(glue_near_future_first_jday_anoxic_deep_prof_rcp85)
(0.000918206973919816,
 'positively autocorrelated',
 'no trend',
 0.21730819755375697,
 0,
 0)


#Distant future [2070-2099]


autocorr_MK_org_modif_sens_slope_test(glue_distant_future_first_jday_anoxic_deep_prof_rcp26)
(0.0035296269402442515,
 'positively autocorrelated',
 'no trend',
 0.1652443573429181,
 0,
 0)


autocorr_MK_org_modif_sens_slope_test(glue_distant_future_first_jday_anoxic_deep_prof_rcp60)
(0.003518667692360656,
 'positively autocorrelated',
 'no trend',
 0.7610600662098355,
 0,
 0)


autocorr_MK_org_modif_sens_slope_test(glue_distant_future_first_jday_anoxic_deep_prof_rcp85)
(0.0036400712692396284,
 'positively autocorrelated',
 'decreasing',
 0.01008406773247228,
 -0.31888972808948424,
 186.61862592708977)


#%% Trendlines over whole periods:
# no trend in his but decreasing trendlines of 6.0 and 8.5 rcps 
# for first jday of deep anoxia    
    
# his     
  
autocorr_MK_org_modif_sens_slope_test(glue_first_jday_anoxic_deep_prof_inyear_his['50%'])
"""
(0.0031376228147856266,
 'positively autocorrelated',
 'increasing',
 0.00014091852226516544,
 0.036140717662852095,
 196.39786832827465)
"""
#rcp26
autocorr_MK_org_modif_sens_slope_test(glue_first_jday_anoxic_deep_prof_inyear_rcp26['50%'])
"""
(0.0033783323009778645,
 'positively autocorrelated',
 'decreasing',
 0.01945905861686925,
 -0.04946637068334504,
 195.70896893955867)
"""

#rcp60
autocorr_MK_org_modif_sens_slope_test(glue_first_jday_anoxic_deep_prof_inyear_rcp60['50%'])
"""
(0.0017625818926192806,
 'positively autocorrelated',
 'decreasing',
 1.2967404927621828e-12,
 -0.13566452380390515,
 196.30840035688158)
"""

#rcp85
autocorr_MK_org_modif_sens_slope_test(glue_first_jday_anoxic_deep_prof_inyear_rcp85['50%'])
"""
(0.002649341684564933,
 'positively autocorrelated',
 'decreasing',
 8.033240739280245e-11,
 -0.16709456432767184,
 195.49787913511878)
"""





#%% 80 years from 2020 for first_jday_anoxic_deep_prof


glue_80years_first_jday_anoxic_deep_prof_inyear_rcp26=glue_first_jday_anoxic_deep_prof_inyear_rcp26[2019 < glue_first_jday_anoxic_deep_prof_inyear_rcp26.index]

glue_80years_first_jday_anoxic_deep_prof_inyear_rcp60=glue_first_jday_anoxic_deep_prof_inyear_rcp60[2019 < glue_first_jday_anoxic_deep_prof_inyear_rcp60.index]


glue_80years_first_jday_anoxic_deep_prof_inyear_rcp85=glue_first_jday_anoxic_deep_prof_inyear_rcp85[2019 < glue_first_jday_anoxic_deep_prof_inyear_rcp85.index]


#============= mean of first 10 yaers over 80 years 

#rcp2.6
np.mean(glue_80years_first_jday_anoxic_deep_prof_inyear_rcp26[glue_80years_first_jday_anoxic_deep_prof_inyear_rcp26.index<2030]['50%'])
190.18537398102035

#rcp6.0
np.mean(glue_80years_first_jday_anoxic_deep_prof_inyear_rcp60[glue_80years_first_jday_anoxic_deep_prof_inyear_rcp60.index<2030]['50%'])
194.47219144332075

#rcp8.5
np.mean(glue_80years_first_jday_anoxic_deep_prof_inyear_rcp85[glue_80years_first_jday_anoxic_deep_prof_inyear_rcp85.index<2030]['50%'])
187.87713864030113
#============== mean of last 10 yaers over 80 years 

#rcp2.6
np.mean(glue_80years_first_jday_anoxic_deep_prof_inyear_rcp26[glue_80years_first_jday_anoxic_deep_prof_inyear_rcp26.index>2089]['50%'])
189.50955388460184

#rcp6.0
np.mean(glue_80years_first_jday_anoxic_deep_prof_inyear_rcp60[glue_80years_first_jday_anoxic_deep_prof_inyear_rcp60.index>2089]['50%'])
182.65569138728154

#rcp8.5
np.mean(glue_80years_first_jday_anoxic_deep_prof_inyear_rcp85[glue_80years_first_jday_anoxic_deep_prof_inyear_rcp85.index>2089]['50%'])
173.57518207507667














#=========== trendline # Over the 80 years


autocorr_MK_org_modif_sens_slope_test(glue_80years_first_jday_anoxic_deep_prof_inyear_rcp26['50%'])
(0.003812698550925423,
 'positively autocorrelated',
 'no trend',
 0.2078731412629169,
 0,
 0)

autocorr_MK_org_modif_sens_slope_test(glue_80years_first_jday_anoxic_deep_prof_inyear_rcp60['50%'])
(0.0017905952951805827,
 'positively autocorrelated',
 'decreasing',
 8.122391648157645e-13,
 -0.13793103448275862,
 194.64788262685872)

autocorr_MK_org_modif_sens_slope_test(glue_80years_first_jday_anoxic_deep_prof_inyear_rcp85['50%'])
(0.0022191202935862814,
 'positively autocorrelated',
 'decreasing',
 3.15083295454599e-07,
 -0.15154884528874035,
 191.98617938890524)



#%%plotting 80 years of len and first jday of deep anoxia profile  


import matplotlib.pyplot as plt
import numpy as np

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(26, 8))

# Plotting the first subplot
ax1.fill_between(glue_80years_len_anoxic_deep_prof_inyear_rcp26.index.astype(float), glue_80years_len_anoxic_deep_prof_inyear_rcp26['5%'], glue_80years_len_anoxic_deep_prof_inyear_rcp26['95%'], color='darkgreen', alpha=0.3)# ,  label= 'RCP2.6 90% CI')
ax1.plot(glue_80years_len_anoxic_deep_prof_inyear_rcp26.index.astype(float), glue_80years_len_anoxic_deep_prof_inyear_rcp26['50%'], 'darkgreen', alpha=0.9, linewidth=3  )#, label='RCP2.6 median'

ax1.fill_between(glue_80years_len_anoxic_deep_prof_inyear_rcp60.index.astype(float), glue_80years_len_anoxic_deep_prof_inyear_rcp60['5%'], glue_80years_len_anoxic_deep_prof_inyear_rcp60['95%'], color='yellow', alpha=0.5)# ,  label= 'RCP6.0 90% CI')
ax1.plot(glue_80years_len_anoxic_deep_prof_inyear_rcp60.index.astype(float), glue_80years_len_anoxic_deep_prof_inyear_rcp60['50%'], 'yellow', alpha=0.9, linewidth=3  )#, label='RCP6.0 median'

ax1.fill_between(glue_80years_len_anoxic_deep_prof_inyear_rcp85.index.astype(float), glue_80years_len_anoxic_deep_prof_inyear_rcp85['5%'], glue_80years_len_anoxic_deep_prof_inyear_rcp85['95%'], color='r', alpha=0.2)# ,  label= 'RCP8.5 90% CI')
ax1.plot(glue_80years_len_anoxic_deep_prof_inyear_rcp85.index.astype(float), glue_80years_len_anoxic_deep_prof_inyear_rcp85['50%'], 'r', alpha=0.9, linewidth=3  )#, label='RCP8.5 median'

trendline_rcp60_len = autocorr_MK_org_modif_sens_slope_test(glue_80years_len_anoxic_deep_prof_inyear_rcp60['50%'])
ax1.text(2020, 170, f'y = {trendline_rcp60_len[-2]:.3f}x + {trendline_rcp60_len[-1]:.3f}, p-value < 0.0001', color='orange', fontsize=20 )

ax1.plot(glue_80years_len_anoxic_deep_prof_inyear_rcp60.index.astype(float),
        trendline_rcp60_len[-2] * np.arange(80) + trendline_rcp60_len[-1],
        linestyle='--', color='orange', alpha=0.9, linewidth=3)


trendline_rcp85_len = autocorr_MK_org_modif_sens_slope_test(glue_80years_len_anoxic_deep_prof_inyear_rcp85['50%'])
ax1.text(2020, 160, f'y = {trendline_rcp85_len[-2]:.3f}x + {trendline_rcp85_len[-1]:.3f}, p-value < 0.0001', color='red', fontsize=20 )


ax1.plot(glue_80years_len_anoxic_deep_prof_inyear_rcp85.index.astype(float),
        trendline_rcp85_len[-2] * np.arange(80) + trendline_rcp85_len[-1],
        linestyle='--', color='red', alpha=0.9, linewidth=3)# , label= 'RCP8.5 trendline')


ax1.set_ylabel('Duration of deep anoxia [d]' , fontsize=26)
ax1.set_xlabel('Year' , fontsize=26)
ax1.tick_params(axis='both', which='major', labelsize=22)
#ax1.legend(bbox_to_anchor=(0.7, -0.2), fontsize=22)
ax1.tick_params(axis='x', rotation=45, labelsize=22)




# Plotting the second subplot
ax2.fill_between(glue_80years_first_jday_anoxic_deep_prof_inyear_rcp26.index.astype(float), glue_80years_first_jday_anoxic_deep_prof_inyear_rcp26['5%'], glue_80years_first_jday_anoxic_deep_prof_inyear_rcp26['95%'], color='darkgreen', alpha=0.3 ,  label= 'RCP2.6 90% CI')
ax2.plot(glue_80years_first_jday_anoxic_deep_prof_inyear_rcp26.index.astype(float), glue_80years_first_jday_anoxic_deep_prof_inyear_rcp26['50%'], 'darkgreen', label='RCP2.6 median', alpha=0.9, linewidth=3  )

ax2.fill_between(glue_80years_first_jday_anoxic_deep_prof_inyear_rcp60.index.astype(float), glue_80years_first_jday_anoxic_deep_prof_inyear_rcp60['5%'], glue_80years_first_jday_anoxic_deep_prof_inyear_rcp60['95%'], color='yellow', alpha=0.5 ,  label= 'RCP6.0 90% CI')
ax2.plot(glue_80years_first_jday_anoxic_deep_prof_inyear_rcp60.index.astype(float), glue_80years_first_jday_anoxic_deep_prof_inyear_rcp60['50%'], 'yellow', label='RCP6.0 median', alpha=0.9, linewidth=3  )

ax2.fill_between(glue_80years_first_jday_anoxic_deep_prof_inyear_rcp85.index.astype(float), glue_80years_first_jday_anoxic_deep_prof_inyear_rcp85['5%'], glue_80years_first_jday_anoxic_deep_prof_inyear_rcp85['95%'], color='r', alpha=0.2 ,  label= 'RCP8.5 90% CI')
ax2.plot(glue_80years_first_jday_anoxic_deep_prof_inyear_rcp85.index.astype(float), glue_80years_first_jday_anoxic_deep_prof_inyear_rcp85['50%'], 'r', label='RCP8.5 median', alpha=0.9, linewidth=3  )

trendline_rcp60_first = autocorr_MK_org_modif_sens_slope_test(glue_80years_first_jday_anoxic_deep_prof_inyear_rcp60['50%'])
ax2.text(2020, 110, f'y = {trendline_rcp60_first[-2]:.3f}x + {trendline_rcp60_first[-1]:.3f}, p-value < 0.0001', color='orange', fontsize=20 )

ax2.plot(glue_80years_first_jday_anoxic_deep_prof_inyear_rcp60.index.astype(float),
        trendline_rcp60_first[-2] * np.arange(80) + trendline_rcp60_first[-1],
        linestyle='--', color='orange', alpha=0.9, linewidth=3, label= 'RCP6.0 trendline')

trendline_rcp85_first = autocorr_MK_org_modif_sens_slope_test(glue_80years_first_jday_anoxic_deep_prof_inyear_rcp85['50%'])
ax2.text(2020, 100, f'y = {trendline_rcp85_first[-2]:.3f}x + {trendline_rcp85_first[-1]:.3f}, p-value < 0.0001', color='red', fontsize=20 )

ax2.plot(glue_80years_first_jday_anoxic_deep_prof_inyear_rcp85.index.astype(float),
        trendline_rcp85_first[-2] * np.arange(80) + trendline_rcp85_first[-1],
        linestyle='--', color='red', alpha=0.9, linewidth=3 , label= 'RCP8.5 trendline')

ax2.set_ylabel('First day of deep anoxia in year [Jd]' , fontsize=26)
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
plt.savefig('GLUE_Timeseries_deep_anoxia_duration_first_len_deep_anoxia_80years.png', bbox_inches='tight')




#%% anormally plot of first Jda and length of deep anoxia profile 


import os
import matplotlib.pyplot as plt

# Change directory
os.chdir('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/')

# Create a figure and axes for subplots
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(25, 10))

# Plotting the first subplot
ax1 = axes[0]
ax1.fill_between(glue_first_jday_anoxic_deep_prof_inyear_his[(1975 < glue_first_jday_anoxic_deep_prof_inyear_his.index)].index.astype(float),
                 glue_first_jday_anoxic_deep_prof_inyear_his[(1975 < glue_first_jday_anoxic_deep_prof_inyear_his.index)]['5%'] - first_jday_anoxic_deep_prof_inyear_ref,
                 glue_first_jday_anoxic_deep_prof_inyear_his[(1975 < glue_first_jday_anoxic_deep_prof_inyear_his.index)]['95%'] - first_jday_anoxic_deep_prof_inyear_ref,
                 color='grey', alpha=0.2, label='His 90% CI')

ax1.plot(glue_first_jday_anoxic_deep_prof_inyear_his[(1975 < glue_first_jday_anoxic_deep_prof_inyear_his.index)].index.astype(float),
         glue_first_jday_anoxic_deep_prof_inyear_his[(1975 < glue_first_jday_anoxic_deep_prof_inyear_his.index)]['50%'] - first_jday_anoxic_deep_prof_inyear_ref,
         'k', label='His median', alpha=0.9, linewidth=3)

ax1.fill_between(glue_first_jday_anoxic_deep_prof_inyear_rcp26.index.astype(float), glue_first_jday_anoxic_deep_prof_inyear_rcp26['5%'] - first_jday_anoxic_deep_prof_inyear_ref, glue_first_jday_anoxic_deep_prof_inyear_rcp26['95%'] - first_jday_anoxic_deep_prof_inyear_ref, color='darkgreen', alpha=0.3, label='RCP6.0 90% CI')

ax1.plot(glue_first_jday_anoxic_deep_prof_inyear_rcp26.index.astype(float), glue_first_jday_anoxic_deep_prof_inyear_rcp26['50%'] - first_jday_anoxic_deep_prof_inyear_ref, 'darkgreen', label='RCP6.0 median', alpha=0.9, linewidth=3)

ax1.fill_between(glue_first_jday_anoxic_deep_prof_inyear_rcp60.index.astype(float), glue_first_jday_anoxic_deep_prof_inyear_rcp60['5%'] - first_jday_anoxic_deep_prof_inyear_ref, glue_first_jday_anoxic_deep_prof_inyear_rcp60['95%'] - first_jday_anoxic_deep_prof_inyear_ref, color='yellow', alpha=0.5, label='RCP6.0 90% CI')

ax1.plot(glue_first_jday_anoxic_deep_prof_inyear_rcp60.index.astype(float), glue_first_jday_anoxic_deep_prof_inyear_rcp60['50%'] - first_jday_anoxic_deep_prof_inyear_ref, 'yellow', label='RCP6.0 median', alpha=0.9, linewidth=3)

ax1.fill_between(glue_first_jday_anoxic_deep_prof_inyear_rcp85.index.astype(float), glue_first_jday_anoxic_deep_prof_inyear_rcp85['5%'] - first_jday_anoxic_deep_prof_inyear_ref, glue_first_jday_anoxic_deep_prof_inyear_rcp85['95%'] - first_jday_anoxic_deep_prof_inyear_ref, color='r', alpha=0.2, label='RCP8.5 90% CI')

ax1.plot(glue_first_jday_anoxic_deep_prof_inyear_rcp85.index.astype(float), glue_first_jday_anoxic_deep_prof_inyear_rcp85['50%'] - first_jday_anoxic_deep_prof_inyear_ref, 'r', label='RCP8.5 median', alpha=0.9, linewidth=3)

ax1.set_ylabel('Anomaly of first day of deep anoxia [Jd]', fontsize=26)
ax1.set_xlabel('Year', fontsize=26)
ax1.tick_params(axis='y', labelsize=22)
ax1.tick_params(axis='x', rotation=45, labelsize=22)

# Plotting the second subplot
ax2 = axes[1]
ax2.fill_between(glue_len_anoxic_deep_prof_inyear_his[(1975 < glue_len_anoxic_deep_prof_inyear_his.index)].index.astype(float),
                 glue_len_anoxic_deep_prof_inyear_his[(1975 < glue_len_anoxic_deep_prof_inyear_his.index)]['5%'] - len_anoxic_deep_prof_inyear_ref,
                 glue_len_anoxic_deep_prof_inyear_his[(1975 < glue_len_anoxic_deep_prof_inyear_his.index)]['95%'] - len_anoxic_deep_prof_inyear_ref,
                 color='grey', alpha=0.2)#, label='His 90% CI')

ax2.plot(glue_len_anoxic_deep_prof_inyear_his[(1975 < glue_len_anoxic_deep_prof_inyear_his.index)].index.astype(float),
          glue_len_anoxic_deep_prof_inyear_his[(1975 < glue_len_anoxic_deep_prof_inyear_his.index)]['50%'] - len_anoxic_deep_prof_inyear_ref,
          'k', alpha=0.9, linewidth=3)

ax2.fill_between(glue_len_anoxic_deep_prof_inyear_rcp26.index.astype(float), glue_len_anoxic_deep_prof_inyear_rcp26['5%'] - len_anoxic_deep_prof_inyear_ref, glue_len_anoxic_deep_prof_inyear_rcp26['95%'] - len_anoxic_deep_prof_inyear_ref, color='darkgreen', alpha=0.3)#, label='RCP6.0 90% CI')

ax2.plot(glue_len_anoxic_deep_prof_inyear_rcp26.index.astype(float), glue_len_anoxic_deep_prof_inyear_rcp26['50%'] - len_anoxic_deep_prof_inyear_ref, 'darkgreen',alpha=0.9, linewidth=3)

ax2.fill_between(glue_len_anoxic_deep_prof_inyear_rcp60.index.astype(float), glue_len_anoxic_deep_prof_inyear_rcp60['5%'] - len_anoxic_deep_prof_inyear_ref, glue_len_anoxic_deep_prof_inyear_rcp60['95%'] - len_anoxic_deep_prof_inyear_ref, color='yellow', alpha=0.5)#, label='RCP6.0 90% CI')

ax2.plot(glue_len_anoxic_deep_prof_inyear_rcp60.index.astype(float), glue_len_anoxic_deep_prof_inyear_rcp60['50%'] - len_anoxic_deep_prof_inyear_ref, 'yellow', alpha=0.9, linewidth=3)

ax2.fill_between(glue_len_anoxic_deep_prof_inyear_rcp85.index.astype(float), glue_len_anoxic_deep_prof_inyear_rcp85['5%'] - len_anoxic_deep_prof_inyear_ref, glue_len_anoxic_deep_prof_inyear_rcp85['95%'] - len_anoxic_deep_prof_inyear_ref, color='r', alpha=0.2)#, label='RCP8.5 90% CI')

ax2.plot(glue_len_anoxic_deep_prof_inyear_rcp85.index.astype(float), glue_len_anoxic_deep_prof_inyear_rcp85['50%'] - len_anoxic_deep_prof_inyear_ref, 'r',  alpha=0.9, linewidth=3)

ax2.set_ylabel('Anomaly of deep anoxia duration [d]', fontsize=26)
ax2.set_xlabel('Year', fontsize=26)
ax2.tick_params(axis='y', labelsize=22)
ax2.tick_params(axis='x', rotation=45, labelsize=22)

# Legend for both subplots
fig.legend(loc='upper center', bbox_to_anchor=(0.5, -0.01), shadow=True, ncol=4, fontsize=22)

# Save the figure
fig.savefig("Anomaly_first_jday_duration_deep_anoxia_profile.png", dpi=300, bbox_inches='tight')
plt.show()



#%% value plot of first Jda and length of deep anoxia profile 


import os
import matplotlib.pyplot as plt

# Change directory
os.chdir('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/')

# Create a figure and axes for subplots
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(25, 10))

# Plotting the first subplot
ax1 = axes[0]
ax1.fill_between(glue_first_jday_anoxic_deep_prof_inyear_his.index.astype(float),
                 glue_first_jday_anoxic_deep_prof_inyear_his['5%'],
                 glue_first_jday_anoxic_deep_prof_inyear_his['95%'],
                 color='grey', alpha=0.2, label='His 90% CI')

ax1.plot(glue_first_jday_anoxic_deep_prof_inyear_his.index.astype(float),
         glue_first_jday_anoxic_deep_prof_inyear_his['50%'],
         'k', label='His median', alpha=0.9, linewidth=3)

ax1.fill_between(glue_first_jday_anoxic_deep_prof_inyear_rcp26.index.astype(float), glue_first_jday_anoxic_deep_prof_inyear_rcp26['5%'], glue_first_jday_anoxic_deep_prof_inyear_rcp26['95%'], color='darkgreen', alpha=0.3, label='RCP6.0 90% CI')

ax1.plot(glue_first_jday_anoxic_deep_prof_inyear_rcp26.index.astype(float), glue_first_jday_anoxic_deep_prof_inyear_rcp26['50%'], 'darkgreen', label='RCP6.0 median', alpha=0.9, linewidth=3)

ax1.fill_between(glue_first_jday_anoxic_deep_prof_inyear_rcp60.index.astype(float), glue_first_jday_anoxic_deep_prof_inyear_rcp60['5%'], glue_first_jday_anoxic_deep_prof_inyear_rcp60['95%'], color='yellow', alpha=0.5, label='RCP6.0 90% CI')

ax1.plot(glue_first_jday_anoxic_deep_prof_inyear_rcp60.index.astype(float), glue_first_jday_anoxic_deep_prof_inyear_rcp60['50%'], 'yellow', label='RCP6.0 median', alpha=0.9, linewidth=3)

ax1.fill_between(glue_first_jday_anoxic_deep_prof_inyear_rcp85.index.astype(float), glue_first_jday_anoxic_deep_prof_inyear_rcp85['5%'], glue_first_jday_anoxic_deep_prof_inyear_rcp85['95%'], color='r', alpha=0.2, label='RCP8.5 90% CI')

ax1.plot(glue_first_jday_anoxic_deep_prof_inyear_rcp85.index.astype(float), glue_first_jday_anoxic_deep_prof_inyear_rcp85['50%'], 'r', label='RCP8.5 median', alpha=0.9, linewidth=3)

ax1.set_ylabel('First day of deep anoxia [Jd]', fontsize=26)
ax1.set_xlabel('Year', fontsize=26)
ax1.tick_params(axis='y', labelsize=22)
ax1.tick_params(axis='x', rotation=45, labelsize=22)

# Plotting the second subplot
ax2 = axes[1]
ax2.fill_between(glue_len_anoxic_deep_prof_inyear_his.index.astype(float),
                 glue_len_anoxic_deep_prof_inyear_his['5%'] ,
                 glue_len_anoxic_deep_prof_inyear_his['95%'] ,
                 color='grey', alpha=0.2)#, label='His 90% CI')

ax2.plot(glue_len_anoxic_deep_prof_inyear_his.index.astype(float),
          glue_len_anoxic_deep_prof_inyear_his['50%'] ,
          'k', alpha=0.9, linewidth=3)

ax2.fill_between(glue_len_anoxic_deep_prof_inyear_rcp26.index.astype(float), glue_len_anoxic_deep_prof_inyear_rcp26['5%'] , glue_len_anoxic_deep_prof_inyear_rcp26['95%'] , color='darkgreen', alpha=0.3)#, label='RCP6.0 90% CI')

ax2.plot(glue_len_anoxic_deep_prof_inyear_rcp26.index.astype(float), glue_len_anoxic_deep_prof_inyear_rcp26['50%'] , 'darkgreen',alpha=0.9, linewidth=3)

ax2.fill_between(glue_len_anoxic_deep_prof_inyear_rcp60.index.astype(float), glue_len_anoxic_deep_prof_inyear_rcp60['5%'] , glue_len_anoxic_deep_prof_inyear_rcp60['95%'] , color='yellow', alpha=0.5)#, label='RCP6.0 90% CI')

ax2.plot(glue_len_anoxic_deep_prof_inyear_rcp60.index.astype(float), glue_len_anoxic_deep_prof_inyear_rcp60['50%'] , 'yellow', alpha=0.9, linewidth=3)

ax2.fill_between(glue_len_anoxic_deep_prof_inyear_rcp85.index.astype(float), glue_len_anoxic_deep_prof_inyear_rcp85['5%'] , glue_len_anoxic_deep_prof_inyear_rcp85['95%'] , color='r', alpha=0.2)#, label='RCP8.5 90% CI')

ax2.plot(glue_len_anoxic_deep_prof_inyear_rcp85.index.astype(float), glue_len_anoxic_deep_prof_inyear_rcp85['50%'] , 'r',  alpha=0.9, linewidth=3)

ax2.set_ylabel('Deep anoxia duration [d]', fontsize=26)
ax2.set_xlabel('Year', fontsize=26)
ax2.tick_params(axis='y', labelsize=22)
ax2.tick_params(axis='x', rotation=45, labelsize=22)

# Legend for both subplots
fig.legend(loc='upper center', bbox_to_anchor=(0.5, -0.01), shadow=True, ncol=4, fontsize=22)

# Save the figure
fig.savefig("First_jday_duration_deep_anoxia_profile.png", dpi=300, bbox_inches='tight')
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
ax1.fill_between(glue_first_jday_anoxic_deep_prof_inyear_his.index.astype(float),
                 glue_first_jday_anoxic_deep_prof_inyear_his['5%'],
                 glue_first_jday_anoxic_deep_prof_inyear_his['95%'],
                 color='grey', alpha=0.2, label='His 90% CI')

ax1.plot(glue_first_jday_anoxic_deep_prof_inyear_his.index.astype(float),
         glue_first_jday_anoxic_deep_prof_inyear_his['50%'],
         'k', label='His median', alpha=0.9, linewidth=3)

ax1.fill_between(glue_first_jday_anoxic_deep_prof_inyear_rcp26.index.astype(float), glue_first_jday_anoxic_deep_prof_inyear_rcp26['5%'], glue_first_jday_anoxic_deep_prof_inyear_rcp26['95%'], color='darkgreen', alpha=0.3, label='RCP6.0 90% CI')

ax1.plot(glue_first_jday_anoxic_deep_prof_inyear_rcp26.index.astype(float), glue_first_jday_anoxic_deep_prof_inyear_rcp26['50%'], 'darkgreen', label='RCP6.0 median', alpha=0.9, linewidth=3)

ax1.fill_between(glue_first_jday_anoxic_deep_prof_inyear_rcp60.index.astype(float), glue_first_jday_anoxic_deep_prof_inyear_rcp60['5%'], glue_first_jday_anoxic_deep_prof_inyear_rcp60['95%'], color='yellow', alpha=0.5, label='RCP6.0 90% CI')

ax1.plot(glue_first_jday_anoxic_deep_prof_inyear_rcp60.index.astype(float), glue_first_jday_anoxic_deep_prof_inyear_rcp60['50%'], 'yellow', label='RCP6.0 median', alpha=0.9, linewidth=3)

ax1.fill_between(glue_first_jday_anoxic_deep_prof_inyear_rcp85.index.astype(float), glue_first_jday_anoxic_deep_prof_inyear_rcp85['5%'], glue_first_jday_anoxic_deep_prof_inyear_rcp85['95%'], color='r', alpha=0.2, label='RCP8.5 90% CI')

ax1.plot(glue_first_jday_anoxic_deep_prof_inyear_rcp85.index.astype(float), glue_first_jday_anoxic_deep_prof_inyear_rcp85['50%'], 'r', label='RCP8.5 median', alpha=0.9, linewidth=3)



trendline_his=autocorr_MK_org_modif_sens_slope_test(glue_first_jday_anoxic_deep_prof_inyear_his['50%'])

trendline_rcp26=autocorr_MK_org_modif_sens_slope_test(glue_first_jday_anoxic_deep_prof_inyear_rcp26['50%'])

trendline_rcp60=autocorr_MK_org_modif_sens_slope_test(glue_first_jday_anoxic_deep_prof_inyear_rcp60['50%'])

trendline_rcp85=autocorr_MK_org_modif_sens_slope_test(glue_first_jday_anoxic_deep_prof_inyear_rcp85['50%'])




ax1.text(1900, 165, f'y = {trendline_rcp60[-2]:.3f}x + {trendline_rcp60[-1]:.3f}, p = {trendline_rcp60[-3]:.3f}', color='gold', fontsize= 20 )

ax1.plot(glue_first_jday_anoxic_deep_prof_inyear_rcp60.index.astype(float),
        trendline_rcp60[-2] * np.arange(94) + trendline_rcp60[-1],
        linestyle='--', color='yellow', alpha=0.9, linewidth=3)



ax1.text(1900, 160, f'y = {trendline_rcp85[-2]:.3f}x + {trendline_rcp85[-1]:.3f}, p = {trendline_rcp85[-3]:.3f}', color='red', fontsize= 20 )

ax1.plot(glue_first_jday_anoxic_deep_prof_inyear_rcp85.index.astype(float),
        trendline_rcp85[-2] * np.arange(94) + trendline_rcp85[-1],
        linestyle='--', color='red', alpha=0.9, linewidth=3)




ax1.set_ylabel('First day of deep anoxia [Jd]', fontsize=26)
ax1.set_xlabel('Year', fontsize=26)
ax1.tick_params(axis='y', labelsize=22)
ax1.tick_params(axis='x', rotation=45, labelsize=22)

# Plotting the second subplot
ax2 = axes[1]
ax2.fill_between(glue_len_anoxic_deep_prof_inyear_his.index.astype(float),
                 glue_len_anoxic_deep_prof_inyear_his['5%'] ,
                 glue_len_anoxic_deep_prof_inyear_his['95%'] ,
                 color='grey', alpha=0.2)#, label='His 90% CI')

ax2.plot(glue_len_anoxic_deep_prof_inyear_his.index.astype(float),
          glue_len_anoxic_deep_prof_inyear_his['50%'] ,
          'k', alpha=0.9, linewidth=3)

ax2.fill_between(glue_len_anoxic_deep_prof_inyear_rcp26.index.astype(float), glue_len_anoxic_deep_prof_inyear_rcp26['5%'] , glue_len_anoxic_deep_prof_inyear_rcp26['95%'] , color='darkgreen', alpha=0.3)#, label='RCP6.0 90% CI')

ax2.plot(glue_len_anoxic_deep_prof_inyear_rcp26.index.astype(float), glue_len_anoxic_deep_prof_inyear_rcp26['50%'] , 'darkgreen',alpha=0.9, linewidth=3)

ax2.fill_between(glue_len_anoxic_deep_prof_inyear_rcp60.index.astype(float), glue_len_anoxic_deep_prof_inyear_rcp60['5%'] , glue_len_anoxic_deep_prof_inyear_rcp60['95%'] , color='yellow', alpha=0.5)#, label='RCP6.0 90% CI')

ax2.plot(glue_len_anoxic_deep_prof_inyear_rcp60.index.astype(float), glue_len_anoxic_deep_prof_inyear_rcp60['50%'] , 'yellow', alpha=0.9, linewidth=3)

ax2.fill_between(glue_len_anoxic_deep_prof_inyear_rcp85.index.astype(float), glue_len_anoxic_deep_prof_inyear_rcp85['5%'] , glue_len_anoxic_deep_prof_inyear_rcp85['95%'] , color='r', alpha=0.2)#, label='RCP8.5 90% CI')

ax2.plot(glue_len_anoxic_deep_prof_inyear_rcp85.index.astype(float), glue_len_anoxic_deep_prof_inyear_rcp85['50%'] , 'r',  alpha=0.9, linewidth=3)




trendline_his=autocorr_MK_org_modif_sens_slope_test(glue_len_anoxic_deep_prof_inyear_his['50%'])

trendline_rcp26=autocorr_MK_org_modif_sens_slope_test(glue_len_anoxic_deep_prof_inyear_rcp26['50%'])

trendline_rcp60=autocorr_MK_org_modif_sens_slope_test(glue_len_anoxic_deep_prof_inyear_rcp60['50%'])

trendline_rcp85=autocorr_MK_org_modif_sens_slope_test(glue_len_anoxic_deep_prof_inyear_rcp85['50%'])


ax2.text(1900,90, f'y = {trendline_rcp26[-2]:.3f}x + {trendline_rcp26[-1]:.3f}, p = {trendline_rcp26[-3]:.3f}', color='green', fontsize= 20 )

ax2.plot(glue_len_anoxic_deep_prof_inyear_rcp26.index.astype(float),
        trendline_rcp26[-2] * np.arange(94) + trendline_rcp26[-1],
        linestyle='--', color='darkgreen', alpha=0.9, linewidth=3)



ax2.text(1900, 85, f'y = {trendline_rcp60[-2]:.3f}x + {trendline_rcp60[-1]:.3f}, p = {trendline_rcp60[-3]:.3f}', color='gold', fontsize= 20 )

ax2.plot(glue_len_anoxic_deep_prof_inyear_rcp60.index.astype(float),
        trendline_rcp60[-2] * np.arange(94) + trendline_rcp60[-1],
        linestyle='--', color='yellow', alpha=0.9, linewidth=3)



ax2.text(1900, 80, f'y = {trendline_rcp85[-2]:.3f}x + {trendline_rcp85[-1]:.3f}, p = {trendline_rcp85[-3]:.3f}', color='red', fontsize= 20 )

ax2.plot(glue_len_anoxic_deep_prof_inyear_rcp85.index.astype(float),
        trendline_rcp85[-2] * np.arange(94) + trendline_rcp85[-1],
        linestyle='--', color='red', alpha=0.9, linewidth=3)



ax2.set_ylabel('Deep anoxia duration [d]', fontsize=26)
ax2.set_xlabel('Year', fontsize=26)
ax2.tick_params(axis='y', labelsize=22)
ax2.tick_params(axis='x', rotation=45, labelsize=22)

# Legend for both subplots
fig.legend(loc='upper center', bbox_to_anchor=(0.5, -0.01), shadow=True, ncol=4, fontsize=22)

# Save the figure
fig.savefig("First_jday_duration_deep_anoxia_profile_withtrendline.png", dpi=300, bbox_inches='tight')
plt.show()























