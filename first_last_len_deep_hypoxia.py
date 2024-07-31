# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 16:54:58 2023

@author: mahta
"""



#%% Jday of first & last & length of deep hypoxic condition 
#%%his


# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/his'
all_first_jday_hypoxic_deep_prof_inyear_his= pd.DataFrame([])
all_last_jday_hypoxic_deep_prof_inyear_his= pd.DataFrame([])
all_len_hypoxic_deep_prof_inyear_his= pd.DataFrame([])
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
        
        
        first_jday_hypoxic_deep_prof_inyear_his=first_last_len_anoxic_deep_inyear  (C, Vr, time_series, threshold=2)[1]
        last_jday_hypoxic_deep_prof_inyear_his=first_last_len_anoxic_deep_inyear  (C, Vr, time_series, threshold=2)[3]
        len_hypoxic_deep_prof_inyear_his=first_last_len_anoxic_deep_inyear  (C, Vr, time_series, threshold=2)[4]
        

        all_first_jday_hypoxic_deep_prof_inyear_his = pd.concat([all_first_jday_hypoxic_deep_prof_inyear_his , first_jday_hypoxic_deep_prof_inyear_his], axis=1)
        all_last_jday_hypoxic_deep_prof_inyear_his = pd.concat([all_last_jday_hypoxic_deep_prof_inyear_his , last_jday_hypoxic_deep_prof_inyear_his], axis=1)
        all_len_hypoxic_deep_prof_inyear_his = pd.concat([all_len_hypoxic_deep_prof_inyear_his , len_hypoxic_deep_prof_inyear_his], axis=1)


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
        
        
        first_jday_hypoxic_deep_prof_inyear_his=first_last_len_anoxic_deep_inyear  (C, Vr, time_series, threshold=2)[1]
        last_jday_hypoxic_deep_prof_inyear_his=first_last_len_anoxic_deep_inyear  (C, Vr, time_series, threshold=2)[3]
        len_hypoxic_deep_prof_inyear_his=first_last_len_anoxic_deep_inyear  (C, Vr, time_series, threshold=2)[4]
        

        all_first_jday_hypoxic_deep_prof_inyear_his = pd.concat([all_first_jday_hypoxic_deep_prof_inyear_his , first_jday_hypoxic_deep_prof_inyear_his], axis=1)
        all_last_jday_hypoxic_deep_prof_inyear_his = pd.concat([all_last_jday_hypoxic_deep_prof_inyear_his , last_jday_hypoxic_deep_prof_inyear_his], axis=1)
        all_len_hypoxic_deep_prof_inyear_his = pd.concat([all_len_hypoxic_deep_prof_inyear_his , len_hypoxic_deep_prof_inyear_his], axis=1)


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
        
        
        first_jday_hypoxic_deep_prof_inyear_his=first_last_len_anoxic_deep_inyear  (C, Vr, time_series, threshold=2)[1]
        last_jday_hypoxic_deep_prof_inyear_his=first_last_len_anoxic_deep_inyear  (C, Vr, time_series, threshold=2)[3]
        len_hypoxic_deep_prof_inyear_his=first_last_len_anoxic_deep_inyear  (C, Vr, time_series, threshold=2)[4]
        

        all_first_jday_hypoxic_deep_prof_inyear_his = pd.concat([all_first_jday_hypoxic_deep_prof_inyear_his , first_jday_hypoxic_deep_prof_inyear_his], axis=1)
        all_last_jday_hypoxic_deep_prof_inyear_his = pd.concat([all_last_jday_hypoxic_deep_prof_inyear_his , last_jday_hypoxic_deep_prof_inyear_his], axis=1)
        all_len_hypoxic_deep_prof_inyear_his = pd.concat([all_len_hypoxic_deep_prof_inyear_his , len_hypoxic_deep_prof_inyear_his], axis=1)


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
        
        
        first_jday_hypoxic_deep_prof_inyear_his=first_last_len_anoxic_deep_inyear  (C, Vr, time_series, threshold=2)[1]
        last_jday_hypoxic_deep_prof_inyear_his=first_last_len_anoxic_deep_inyear  (C, Vr, time_series, threshold=2)[3]
        len_hypoxic_deep_prof_inyear_his=first_last_len_anoxic_deep_inyear  (C, Vr, time_series, threshold=2)[4]
        

        all_first_jday_hypoxic_deep_prof_inyear_his = pd.concat([all_first_jday_hypoxic_deep_prof_inyear_his , first_jday_hypoxic_deep_prof_inyear_his], axis=1)
        all_last_jday_hypoxic_deep_prof_inyear_his = pd.concat([all_last_jday_hypoxic_deep_prof_inyear_his , last_jday_hypoxic_deep_prof_inyear_his], axis=1)
        all_len_hypoxic_deep_prof_inyear_his = pd.concat([all_len_hypoxic_deep_prof_inyear_his , len_hypoxic_deep_prof_inyear_his], axis=1)

#%%annova_uncertainity_his 
all_first_jday_hypoxic_deep_prof_inyear_his=all_first_jday_hypoxic_deep_prof_inyear_his.replace(0, np.nan)

anova_first_jday_hypoxic_deep_prof_his=annova_uncertainity(all_first_jday_hypoxic_deep_prof_inyear_his)

anova_first_jday_hypoxic_deep_prof_his.describe().loc['mean', :]
"""
GCMs             68.898945
param            29.489821
interaction       1.611234
GCMs/param       17.069897
year           1933.000000

"""

anova_first_jday_hypoxic_deep_prof_his.describe().loc['std', :]
"""
GCMs           25.390987
param          24.999704
interaction     2.067473
GCMs/param     42.283563
year           42.001984

"""

all_last_jday_hypoxic_deep_prof_inyear_his=all_last_jday_hypoxic_deep_prof_inyear_his.replace(0, np.nan)

anova_last_jday_hypoxic_deep_prof_his=annova_uncertainity(all_last_jday_hypoxic_deep_prof_inyear_his)

anova_last_jday_hypoxic_deep_prof_his.describe().loc['mean', :]
"""
GCMs             97.128026
param             0.742584
interaction       2.129390
GCMs/param             inf
year           1933.000000
Name: mean, dtype: float64
"""


anova_last_jday_hypoxic_deep_prof_his.describe().loc['std', :]

"""
GCMs           12.013282
param           3.011986
interaction     9.020740
GCMs/param           NaN
year           42.001984
Name: std, dtype: float64
"""


all_len_hypoxic_deep_prof_inyear_his=all_len_hypoxic_deep_prof_inyear_his.replace(0, np.nan)

anova_len_jday_hypoxic_deep_prof_his=annova_uncertainity(all_len_hypoxic_deep_prof_inyear_his)

anova_len_jday_hypoxic_deep_prof_his.describe().loc['mean', :]
"""
GCMs             70.593840
param            26.555578
interaction       2.850582
GCMs/param       11.375310
year           1933.000000
Name: mean, dtype: float64
"""


anova_len_jday_hypoxic_deep_prof_his.describe().loc['std', :]
"""
GCMs           21.776594
param          20.562527
interaction     5.471925
GCMs/param     18.296105
year           42.001984
Name: std, dtype: float64
"""


#%%rcp26


# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp26'
all_first_jday_hypoxic_deep_prof_inyear_rcp26= pd.DataFrame([])
all_last_jday_hypoxic_deep_prof_inyear_rcp26= pd.DataFrame([])
all_len_hypoxic_deep_prof_inyear_rcp26= pd.DataFrame([])
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
        
        
        first_jday_hypoxic_deep_prof_inyear_rcp26=first_last_len_anoxic_deep_inyear  (C, Vr, time_series, threshold=2)[1]
        last_jday_hypoxic_deep_prof_inyear_rcp26=first_last_len_anoxic_deep_inyear  (C, Vr, time_series, threshold=2)[3]
        len_hypoxic_deep_prof_inyear_rcp26=first_last_len_anoxic_deep_inyear  (C, Vr, time_series, threshold=2)[4]
        

        all_first_jday_hypoxic_deep_prof_inyear_rcp26 = pd.concat([all_first_jday_hypoxic_deep_prof_inyear_rcp26 , first_jday_hypoxic_deep_prof_inyear_rcp26], axis=1)
        all_last_jday_hypoxic_deep_prof_inyear_rcp26 = pd.concat([all_last_jday_hypoxic_deep_prof_inyear_rcp26 , last_jday_hypoxic_deep_prof_inyear_rcp26], axis=1)
        all_len_hypoxic_deep_prof_inyear_rcp26 = pd.concat([all_len_hypoxic_deep_prof_inyear_rcp26 , len_hypoxic_deep_prof_inyear_rcp26], axis=1)


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
        
        
        first_jday_hypoxic_deep_prof_inyear_rcp26=first_last_len_anoxic_deep_inyear  (C, Vr, time_series, threshold=2)[1]
        last_jday_hypoxic_deep_prof_inyear_rcp26=first_last_len_anoxic_deep_inyear  (C, Vr, time_series, threshold=2)[3]
        len_hypoxic_deep_prof_inyear_rcp26=first_last_len_anoxic_deep_inyear  (C, Vr, time_series, threshold=2)[4]
        

        all_first_jday_hypoxic_deep_prof_inyear_rcp26 = pd.concat([all_first_jday_hypoxic_deep_prof_inyear_rcp26 , first_jday_hypoxic_deep_prof_inyear_rcp26], axis=1)
        all_last_jday_hypoxic_deep_prof_inyear_rcp26 = pd.concat([all_last_jday_hypoxic_deep_prof_inyear_rcp26 , last_jday_hypoxic_deep_prof_inyear_rcp26], axis=1)
        all_len_hypoxic_deep_prof_inyear_rcp26 = pd.concat([all_len_hypoxic_deep_prof_inyear_rcp26 , len_hypoxic_deep_prof_inyear_rcp26], axis=1)


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
        
        
        first_jday_hypoxic_deep_prof_inyear_rcp26=first_last_len_anoxic_deep_inyear  (C, Vr, time_series, threshold=2)[1]
        last_jday_hypoxic_deep_prof_inyear_rcp26=first_last_len_anoxic_deep_inyear  (C, Vr, time_series, threshold=2)[3]
        len_hypoxic_deep_prof_inyear_rcp26=first_last_len_anoxic_deep_inyear  (C, Vr, time_series, threshold=2)[4]
        

        all_first_jday_hypoxic_deep_prof_inyear_rcp26 = pd.concat([all_first_jday_hypoxic_deep_prof_inyear_rcp26 , first_jday_hypoxic_deep_prof_inyear_rcp26], axis=1)
        all_last_jday_hypoxic_deep_prof_inyear_rcp26 = pd.concat([all_last_jday_hypoxic_deep_prof_inyear_rcp26 , last_jday_hypoxic_deep_prof_inyear_rcp26], axis=1)
        all_len_hypoxic_deep_prof_inyear_rcp26 = pd.concat([all_len_hypoxic_deep_prof_inyear_rcp26 , len_hypoxic_deep_prof_inyear_rcp26], axis=1)


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
        
        
        first_jday_hypoxic_deep_prof_inyear_rcp26=first_last_len_anoxic_deep_inyear  (C, Vr, time_series, threshold=2)[1]
        last_jday_hypoxic_deep_prof_inyear_rcp26=first_last_len_anoxic_deep_inyear  (C, Vr, time_series, threshold=2)[3]
        len_hypoxic_deep_prof_inyear_rcp26=first_last_len_anoxic_deep_inyear  (C, Vr, time_series, threshold=2)[4]
        

        all_first_jday_hypoxic_deep_prof_inyear_rcp26 = pd.concat([all_first_jday_hypoxic_deep_prof_inyear_rcp26 , first_jday_hypoxic_deep_prof_inyear_rcp26], axis=1)
        all_last_jday_hypoxic_deep_prof_inyear_rcp26 = pd.concat([all_last_jday_hypoxic_deep_prof_inyear_rcp26 , last_jday_hypoxic_deep_prof_inyear_rcp26], axis=1)
        all_len_hypoxic_deep_prof_inyear_rcp26 = pd.concat([all_len_hypoxic_deep_prof_inyear_rcp26 , len_hypoxic_deep_prof_inyear_rcp26], axis=1)

#%%annova_uncertainity_rcp26 

all_first_jday_hypoxic_deep_prof_inyear_rcp26=all_first_jday_hypoxic_deep_prof_inyear_rcp26.replace(0, np.nan)

anova_first_jday_hypoxic_deep_prof_rcp26=annova_uncertainity(all_first_jday_hypoxic_deep_prof_inyear_rcp26)

anova_first_jday_hypoxic_deep_prof_rcp26.describe().loc['mean', :]
"""
GCMs             70.342267
param            28.614912
interaction       1.042822
GCMs/param       17.695777
year           2052.500000
"""

anova_first_jday_hypoxic_deep_prof_rcp26.describe().loc['std', :]
"""
GCMs           24.504009
param          24.441023
interaction     0.582860
GCMs/param     28.841605
year           27.279418
Name: std, dtype: float64

"""
all_last_jday_hypoxic_deep_prof_inyear_rcp26=all_last_jday_hypoxic_deep_prof_inyear_rcp26.replace(0, np.nan)


anova_last_jday_hypoxic_deep_prof_rcp26=annova_uncertainity(all_last_jday_hypoxic_deep_prof_inyear_rcp26)

anova_last_jday_hypoxic_deep_prof_rcp26.describe().loc['mean', :]
"""
GCMs             99.406343
param             0.148414
interaction       0.445243
GCMs/param             inf
year           2052.500000
Name: mean, dtype: float64
"""


anova_last_jday_hypoxic_deep_prof_rcp26.describe().loc['std', :]

"""
GCMs            5.755721
param           1.438930
interaction     4.316791
GCMs/param           NaN
year           27.279418
Name: std, dtype: float64
"""
#####moskel dasht

anova_len_jday_hypoxic_deep_prof_rcp26=annova_uncertainity(all_len_hypoxic_deep_prof_inyear_rcp26)

anova_len_jday_hypoxic_deep_prof_rcp26.describe().loc['mean', :]
"""
GCMs             68.055532
param            31.018810
interaction       0.925659
GCMs/param        3.707787
year           2052.500000
"""


anova_len_jday_hypoxic_deep_prof_rcp26.describe().loc['std', :]
"""
GCMs           19.503401
param          19.000721
interaction     1.337271
GCMs/param      3.656886
year           27.279418
Name: std, dtype: float64
"""
#%%annova_uncertainity_rcp26_80years

all_first_jday_hypoxic_deep_prof_inyear_rcp26=all_first_jday_hypoxic_deep_prof_inyear_rcp26.replace(0, np.nan)

anova_first_jday_hypoxic_deep_prof_rcp26_80years=annova_uncertainity(all_first_jday_hypoxic_deep_prof_inyear_rcp26[all_first_jday_hypoxic_deep_prof_inyear_rcp26.index>2019])

anova_first_jday_hypoxic_deep_prof_rcp26_80years.describe().loc['mean', :]
"""
GCMs             63.956883
param            34.955634
interaction       1.087483
GCMs/param        2.823725
year           2059.500000
Name: mean, dtype: float64
"""

anova_first_jday_hypoxic_deep_prof_rcp26_80years.describe().loc['std', :]
"""
GCMs           18.782867
param          18.449149
interaction     1.630339
GCMs/param      2.635767
year           23.237900
Name: std, dtype: float64
"""




anova_len_jday_hypoxic_deep_prof_rcp26_80years=annova_uncertainity(all_len_hypoxic_deep_prof_inyear_rcp26[all_len_hypoxic_deep_prof_inyear_rcp26.index>2019])

anova_len_jday_hypoxic_deep_prof_rcp26_80years.describe().loc['mean', :]
"""
GCMs             69.643500
param            29.448046
interaction       0.908455
GCMs/param        3.947050
year           2059.500000
Name: mean, dtype: float64
"""


anova_len_jday_hypoxic_deep_prof_rcp26_80years.describe().loc['std', :]
"""
GCMs           18.414024
param          17.983147
interaction     1.377199
GCMs/param      3.839250
year           23.237900
Name: std, dtype: float64
"""








#%%rcp60


# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp60'
all_first_jday_hypoxic_deep_prof_inyear_rcp60= pd.DataFrame([])
all_last_jday_hypoxic_deep_prof_inyear_rcp60= pd.DataFrame([])
all_len_hypoxic_deep_prof_inyear_rcp60= pd.DataFrame([])
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
        
        
        first_jday_hypoxic_deep_prof_inyear_rcp60=first_last_len_anoxic_deep_inyear  (C, Vr, time_series, threshold=2)[1]
        last_jday_hypoxic_deep_prof_inyear_rcp60=first_last_len_anoxic_deep_inyear  (C, Vr, time_series, threshold=2)[3]
        len_hypoxic_deep_prof_inyear_rcp60=first_last_len_anoxic_deep_inyear  (C, Vr, time_series, threshold=2)[4]
        

        all_first_jday_hypoxic_deep_prof_inyear_rcp60 = pd.concat([all_first_jday_hypoxic_deep_prof_inyear_rcp60 , first_jday_hypoxic_deep_prof_inyear_rcp60], axis=1)
        all_last_jday_hypoxic_deep_prof_inyear_rcp60 = pd.concat([all_last_jday_hypoxic_deep_prof_inyear_rcp60 , last_jday_hypoxic_deep_prof_inyear_rcp60], axis=1)
        all_len_hypoxic_deep_prof_inyear_rcp60 = pd.concat([all_len_hypoxic_deep_prof_inyear_rcp60 , len_hypoxic_deep_prof_inyear_rcp60], axis=1)


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
        
        
        first_jday_hypoxic_deep_prof_inyear_rcp60=first_last_len_anoxic_deep_inyear  (C, Vr, time_series, threshold=2)[1]
        last_jday_hypoxic_deep_prof_inyear_rcp60=first_last_len_anoxic_deep_inyear  (C, Vr, time_series, threshold=2)[3]
        len_hypoxic_deep_prof_inyear_rcp60=first_last_len_anoxic_deep_inyear  (C, Vr, time_series, threshold=2)[4]
        

        all_first_jday_hypoxic_deep_prof_inyear_rcp60 = pd.concat([all_first_jday_hypoxic_deep_prof_inyear_rcp60 , first_jday_hypoxic_deep_prof_inyear_rcp60], axis=1)
        all_last_jday_hypoxic_deep_prof_inyear_rcp60 = pd.concat([all_last_jday_hypoxic_deep_prof_inyear_rcp60 , last_jday_hypoxic_deep_prof_inyear_rcp60], axis=1)
        all_len_hypoxic_deep_prof_inyear_rcp60 = pd.concat([all_len_hypoxic_deep_prof_inyear_rcp60 , len_hypoxic_deep_prof_inyear_rcp60], axis=1)


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
        
        
        first_jday_hypoxic_deep_prof_inyear_rcp60=first_last_len_anoxic_deep_inyear  (C, Vr, time_series, threshold=2)[1]
        last_jday_hypoxic_deep_prof_inyear_rcp60=first_last_len_anoxic_deep_inyear  (C, Vr, time_series, threshold=2)[3]
        len_hypoxic_deep_prof_inyear_rcp60=first_last_len_anoxic_deep_inyear  (C, Vr, time_series, threshold=2)[4]
        

        all_first_jday_hypoxic_deep_prof_inyear_rcp60 = pd.concat([all_first_jday_hypoxic_deep_prof_inyear_rcp60 , first_jday_hypoxic_deep_prof_inyear_rcp60], axis=1)
        all_last_jday_hypoxic_deep_prof_inyear_rcp60 = pd.concat([all_last_jday_hypoxic_deep_prof_inyear_rcp60 , last_jday_hypoxic_deep_prof_inyear_rcp60], axis=1)
        all_len_hypoxic_deep_prof_inyear_rcp60 = pd.concat([all_len_hypoxic_deep_prof_inyear_rcp60 , len_hypoxic_deep_prof_inyear_rcp60], axis=1)


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
        
        
        first_jday_hypoxic_deep_prof_inyear_rcp60=first_last_len_anoxic_deep_inyear  (C, Vr, time_series, threshold=2)[1]
        last_jday_hypoxic_deep_prof_inyear_rcp60=first_last_len_anoxic_deep_inyear  (C, Vr, time_series, threshold=2)[3]
        len_hypoxic_deep_prof_inyear_rcp60=first_last_len_anoxic_deep_inyear  (C, Vr, time_series, threshold=2)[4]
        

        all_first_jday_hypoxic_deep_prof_inyear_rcp60 = pd.concat([all_first_jday_hypoxic_deep_prof_inyear_rcp60 , first_jday_hypoxic_deep_prof_inyear_rcp60], axis=1)
        all_last_jday_hypoxic_deep_prof_inyear_rcp60 = pd.concat([all_last_jday_hypoxic_deep_prof_inyear_rcp60 , last_jday_hypoxic_deep_prof_inyear_rcp60], axis=1)
        all_len_hypoxic_deep_prof_inyear_rcp60 = pd.concat([all_len_hypoxic_deep_prof_inyear_rcp60 , len_hypoxic_deep_prof_inyear_rcp60], axis=1)


#%%annova_uncertainity_rcp60 


all_first_jday_hypoxic_deep_prof_inyear_rcp60=all_first_jday_hypoxic_deep_prof_inyear_rcp60.replace(0, np.nan)

anova_first_jday_hypoxic_deep_prof_rcp60=annova_uncertainity(all_first_jday_hypoxic_deep_prof_inyear_rcp60)

anova_first_jday_hypoxic_deep_prof_rcp60.describe().loc['mean', :]
"""
GCMs             66.936534
param            31.730548
interaction       1.332919
GCMs/param        9.554287
year           2052.500000
Name: mean, dtype: float64
"""

anova_first_jday_hypoxic_deep_prof_rcp60.describe().loc['std', :]
"""
GCMs           23.807308
param          23.722442
interaction     1.025556
GCMs/param     16.198575
year           27.279418
Name: std, dtype: float64
"""
all_last_jday_hypoxic_deep_prof_inyear_rcp60= all_last_jday_hypoxic_deep_prof_inyear_rcp60.replace(0, np.nan)

anova_last_jday_hypoxic_deep_prof_rcp60=annova_uncertainity(all_last_jday_hypoxic_deep_prof_inyear_rcp60)

anova_last_jday_hypoxic_deep_prof_rcp60.describe().loc['mean', :]
"""
GCMs            100.000000
param             0.201005
interaction      -0.201005
GCMs/param             inf
year           2052.500000
Name: mean, dtype: float64

"""


anova_last_jday_hypoxic_deep_prof_rcp60.describe().loc['std', :]

"""
GCMs           2.947194e-15
param          1.948813e+00
interaction    1.948813e+00
GCMs/param              NaN
year           2.727942e+01
Name: std, dtype: float64
"""



anova_len_jday_hypoxic_deep_prof_rcp60=annova_uncertainity(all_len_hypoxic_deep_prof_inyear_rcp60)

anova_len_jday_hypoxic_deep_prof_rcp60.describe().loc['mean', :]
"""
GCMs             72.765857
param            26.331829
interaction       0.902314
GCMs/param        5.449574
year           2052.500000
Name: mean, dtype: float64
"""


anova_len_jday_hypoxic_deep_prof_rcp60.describe().loc['std', :]
"""
GCMs           19.162656
param          18.457260
interaction     1.153087
GCMs/param      6.389252
year           27.279418
Name: std, dtype: float64
"""

#%%annova_uncertainity_rcp60_80years
all_first_jday_hypoxic_deep_prof_inyear_rcp60= all_first_jday_hypoxic_deep_prof_inyear_rcp60.replace(0, np.nan)

anova_first_jday_hypoxic_deep_prof_rcp60_80years=annova_uncertainity(all_first_jday_hypoxic_deep_prof_inyear_rcp60[all_first_jday_hypoxic_deep_prof_inyear_rcp60.index>2019])

anova_first_jday_hypoxic_deep_prof_rcp60_80years.describe().loc['mean', :]
"""
GCMs             65.094072
param            33.553352
interaction       1.352576
GCMs/param        8.461863
year           2059.500000
Name: mean, dtype: float64
"""

anova_first_jday_hypoxic_deep_prof_rcp60_80years.describe().loc['std', :]
"""
GCMs           24.161260
param          24.079643
interaction     1.028585
GCMs/param     15.434583
year           23.237900
Name: std, dtype: float64

"""


all_len_hypoxic_deep_prof_inyear_rcp60=all_len_hypoxic_deep_prof_inyear_rcp60.replace(0, np.nan)

anova_len_jday_hypoxic_deep_prof_rcp60_80years=annova_uncertainity(all_len_hypoxic_deep_prof_inyear_rcp60[all_len_hypoxic_deep_prof_inyear_rcp60.index>2019])

anova_len_jday_hypoxic_deep_prof_rcp60_80years.describe().loc['mean', :]
"""
GCMs             72.846901
param            26.225824
interaction       0.927275
GCMs/param        5.082550
year           2059.500000
Name: mean, dtype: float64
"""


anova_len_jday_hypoxic_deep_prof_rcp60_80years.describe().loc['std', :]
"""
GCMs           19.407161
param          18.666961
interaction     1.215239
GCMs/param      5.054526
year           23.237900
Name: std, dtype: float64
"""



#%%rcp85


# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp85'
all_first_jday_hypoxic_deep_prof_inyear_rcp85= pd.DataFrame([])
all_last_jday_hypoxic_deep_prof_inyear_rcp85= pd.DataFrame([])
all_len_hypoxic_deep_prof_inyear_rcp85= pd.DataFrame([])
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
        
        
        first_jday_hypoxic_deep_prof_inyear_rcp85=first_last_len_anoxic_deep_inyear  (C, Vr, time_series, threshold=2)[1]
        last_jday_hypoxic_deep_prof_inyear_rcp85=first_last_len_anoxic_deep_inyear  (C, Vr, time_series, threshold=2)[3]
        len_hypoxic_deep_prof_inyear_rcp85=first_last_len_anoxic_deep_inyear  (C, Vr, time_series, threshold=2)[4]
        

        all_first_jday_hypoxic_deep_prof_inyear_rcp85 = pd.concat([all_first_jday_hypoxic_deep_prof_inyear_rcp85 , first_jday_hypoxic_deep_prof_inyear_rcp85], axis=1)
        all_last_jday_hypoxic_deep_prof_inyear_rcp85 = pd.concat([all_last_jday_hypoxic_deep_prof_inyear_rcp85 , last_jday_hypoxic_deep_prof_inyear_rcp85], axis=1)
        all_len_hypoxic_deep_prof_inyear_rcp85 = pd.concat([all_len_hypoxic_deep_prof_inyear_rcp85 , len_hypoxic_deep_prof_inyear_rcp85], axis=1)


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
        
        
        first_jday_hypoxic_deep_prof_inyear_rcp85=first_last_len_anoxic_deep_inyear  (C, Vr, time_series, threshold=2)[1]
        last_jday_hypoxic_deep_prof_inyear_rcp85=first_last_len_anoxic_deep_inyear  (C, Vr, time_series, threshold=2)[3]
        len_hypoxic_deep_prof_inyear_rcp85=first_last_len_anoxic_deep_inyear  (C, Vr, time_series, threshold=2)[4]
        

        all_first_jday_hypoxic_deep_prof_inyear_rcp85 = pd.concat([all_first_jday_hypoxic_deep_prof_inyear_rcp85 , first_jday_hypoxic_deep_prof_inyear_rcp85], axis=1)
        all_last_jday_hypoxic_deep_prof_inyear_rcp85 = pd.concat([all_last_jday_hypoxic_deep_prof_inyear_rcp85 , last_jday_hypoxic_deep_prof_inyear_rcp85], axis=1)
        all_len_hypoxic_deep_prof_inyear_rcp85 = pd.concat([all_len_hypoxic_deep_prof_inyear_rcp85 , len_hypoxic_deep_prof_inyear_rcp85], axis=1)


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
        
        
        first_jday_hypoxic_deep_prof_inyear_rcp85=first_last_len_anoxic_deep_inyear  (C, Vr, time_series, threshold=2)[1]
        last_jday_hypoxic_deep_prof_inyear_rcp85=first_last_len_anoxic_deep_inyear  (C, Vr, time_series, threshold=2)[3]
        len_hypoxic_deep_prof_inyear_rcp85=first_last_len_anoxic_deep_inyear  (C, Vr, time_series, threshold=2)[4]
        

        all_first_jday_hypoxic_deep_prof_inyear_rcp85 = pd.concat([all_first_jday_hypoxic_deep_prof_inyear_rcp85 , first_jday_hypoxic_deep_prof_inyear_rcp85], axis=1)
        all_last_jday_hypoxic_deep_prof_inyear_rcp85 = pd.concat([all_last_jday_hypoxic_deep_prof_inyear_rcp85 , last_jday_hypoxic_deep_prof_inyear_rcp85], axis=1)
        all_len_hypoxic_deep_prof_inyear_rcp85 = pd.concat([all_len_hypoxic_deep_prof_inyear_rcp85 , len_hypoxic_deep_prof_inyear_rcp85], axis=1)


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
        
        
        first_jday_hypoxic_deep_prof_inyear_rcp85=first_last_len_anoxic_deep_inyear  (C, Vr, time_series, threshold=2)[1]
        last_jday_hypoxic_deep_prof_inyear_rcp85=first_last_len_anoxic_deep_inyear  (C, Vr, time_series, threshold=2)[3]
        len_hypoxic_deep_prof_inyear_rcp85=first_last_len_anoxic_deep_inyear  (C, Vr, time_series, threshold=2)[4]
        

        all_first_jday_hypoxic_deep_prof_inyear_rcp85 = pd.concat([all_first_jday_hypoxic_deep_prof_inyear_rcp85 , first_jday_hypoxic_deep_prof_inyear_rcp85], axis=1)
        all_last_jday_hypoxic_deep_prof_inyear_rcp85 = pd.concat([all_last_jday_hypoxic_deep_prof_inyear_rcp85 , last_jday_hypoxic_deep_prof_inyear_rcp85], axis=1)
        all_len_hypoxic_deep_prof_inyear_rcp85 = pd.concat([all_len_hypoxic_deep_prof_inyear_rcp85 , len_hypoxic_deep_prof_inyear_rcp85], axis=1)



#%%annova_uncertainity_rcp85 

all_first_jday_hypoxic_deep_prof_inyear_rcp85= all_first_jday_hypoxic_deep_prof_inyear_rcp85.replace(0, np.nan)

anova_first_jday_hypoxic_deep_prof_rcp85=annova_uncertainity(all_first_jday_hypoxic_deep_prof_inyear_rcp85)

anova_first_jday_hypoxic_deep_prof_rcp85.describe().loc['mean', :]
"""
GCMs             68.359267
param            30.135108
interaction       1.505626
GCMs/param       18.583851
year           2052.500000
Name: mean, dtype: float64
"""

anova_first_jday_hypoxic_deep_prof_rcp85.describe().loc['std', :]
"""
GCMs           25.343435
param          24.941366
interaction     1.199395
GCMs/param     37.917078
year           27.279418
Name: std, dtype: float64

"""
all_last_jday_hypoxic_deep_prof_inyear_rcp85= all_last_jday_hypoxic_deep_prof_inyear_rcp85.replace(0, np.nan)

anova_last_jday_hypoxic_deep_prof_rcp85=annova_uncertainity(all_last_jday_hypoxic_deep_prof_inyear_rcp85)

anova_last_jday_hypoxic_deep_prof_rcp85.describe().loc['mean', :]
"""
GCMs            100.000000
param             0.012643
interaction      -0.012643
GCMs/param             inf
year           2052.500000
Name: mean, dtype: float64
"""


anova_last_jday_hypoxic_deep_prof_rcp85.describe().loc['std', :]

"""
GCMs            0.000000
param           0.122574
interaction     0.122574
GCMs/param           NaN
year           27.279418
Name: std, dtype: float64
"""



anova_len_jday_hypoxic_deep_prof_rcp85=annova_uncertainity(all_len_hypoxic_deep_prof_inyear_rcp85)

anova_len_jday_hypoxic_deep_prof_rcp85.describe().loc['mean', :]
"""
GCMs             81.089541
param            18.100483
interaction       0.809976
GCMs/param        7.995096
year           2052.500000
Name: mean, dtype: float64
"""


anova_len_jday_hypoxic_deep_prof_rcp85.describe().loc['std', :]
"""
GCMs           14.775336
param          14.105595
interaction     1.351154
GCMs/param      6.773437
year           27.279418
Name: std, dtype: float64
"""


#%%annova_uncertainity_rcp85_80years
all_first_jday_hypoxic_deep_prof_inyear_rcp85=all_first_jday_hypoxic_deep_prof_inyear_rcp85.replace(0, np.nan)

anova_first_jday_hypoxic_deep_prof_rcp85_80years=annova_uncertainity(all_first_jday_hypoxic_deep_prof_inyear_rcp85[all_first_jday_hypoxic_deep_prof_inyear_rcp85.index>2019])

anova_first_jday_hypoxic_deep_prof_rcp85_80years.describe().loc['mean', :]
"""
GCMs             69.395320
param            29.092299
interaction       1.512381
GCMs/param       17.595662
year           2059.500000
Name: mean, dtype: float64
"""

anova_first_jday_hypoxic_deep_prof_rcp85_80years.describe().loc['std', :]
"""
GCMs           25.325205
param          24.846535
interaction     1.139253
GCMs/param     26.396837
year           23.237900
Name: std, dtype: float64
"""




anova_len_jday_hypoxic_deep_prof_rcp85_80years=annova_uncertainity(all_len_hypoxic_deep_prof_inyear_rcp85[all_len_hypoxic_deep_prof_inyear_rcp85.index>2019])

anova_len_jday_hypoxic_deep_prof_rcp85_80years.describe().loc['mean', :]
"""
GCMs             81.551885
param            17.604974
interaction       0.843140
GCMs/param        8.493650
year           2059.500000
Name: mean, dtype: float64
"""


anova_len_jday_hypoxic_deep_prof_rcp85_80years.describe().loc['std', :]
"""
GCMs           14.818788
param          14.051482
interaction     1.447706
GCMs/param      7.148096
year           23.237900
Name: std, dtype: float64
"""





#%% Plotting of anova_len_jday_hypoxic_deep_prof, anova_first_jday_hypoxic_deep_prof rcp85

#first_jday_hypoxic_his

#years
contributions_first_jday_hypoxic_his_years=anova_first_jday_hypoxic_deep_prof_his['year']
#GCMs
gcm_contributions_first_jday_hypoxic_his= anova_first_jday_hypoxic_deep_prof_his['GCMs']
#Param
param_contributions_first_jday_hypoxic_his=anova_first_jday_hypoxic_deep_prof_his['param']
#interaction
interact_contributions_first_jday_hypoxic_his =anova_first_jday_hypoxic_deep_prof_his['interaction']


#len_jday_hypoxic_his

#years
contributions_len_jday_hypoxic_his_years=anova_len_jday_hypoxic_deep_prof_his['year']
#GCMs
gcm_contributions_len_jday_hypoxic_his= anova_len_jday_hypoxic_deep_prof_his['GCMs']
#Param
param_contributions_len_jday_hypoxic_his=anova_len_jday_hypoxic_deep_prof_his['param']
#interaction
interact_contributions_len_jday_hypoxic_his =anova_len_jday_hypoxic_deep_prof_his['interaction']

     

#first_jday_hypoxic_rcp26

#years
contributions_first_jday_hypoxic_rcp26_years=anova_first_jday_hypoxic_deep_prof_rcp26['year']
#GCMs
gcm_contributions_first_jday_hypoxic_rcp26= anova_first_jday_hypoxic_deep_prof_rcp26['GCMs']
#Param
param_contributions_first_jday_hypoxic_rcp26=anova_first_jday_hypoxic_deep_prof_rcp26['param']
#interaction
interact_contributions_first_jday_hypoxic_rcp26 =anova_first_jday_hypoxic_deep_prof_rcp26['interaction']


#len_jday_hypoxic_rcp26

#years
contributions_len_jday_hypoxic_rcp26_years=anova_len_jday_hypoxic_deep_prof_rcp26['year']
#GCMs
gcm_contributions_len_jday_hypoxic_rcp26= anova_len_jday_hypoxic_deep_prof_rcp26['GCMs']
#Param
param_contributions_len_jday_hypoxic_rcp26=anova_len_jday_hypoxic_deep_prof_rcp26['param']
#interaction
interact_contributions_len_jday_hypoxic_rcp26 =anova_len_jday_hypoxic_deep_prof_rcp26['interaction']

     

#first_jday_hypoxic_rcp60

#years
contributions_first_jday_hypoxic_rcp60_years=anova_first_jday_hypoxic_deep_prof_rcp60['year']
#GCMs
gcm_contributions_first_jday_hypoxic_rcp60= anova_first_jday_hypoxic_deep_prof_rcp60['GCMs']
#Param
param_contributions_first_jday_hypoxic_rcp60=anova_first_jday_hypoxic_deep_prof_rcp60['param']
#interaction
interact_contributions_first_jday_hypoxic_rcp60 =anova_first_jday_hypoxic_deep_prof_rcp60['interaction']


#len_jday_hypoxic_rcp60

#years
contributions_len_jday_hypoxic_rcp60_years=anova_len_jday_hypoxic_deep_prof_rcp60['year']
#GCMs
gcm_contributions_len_jday_hypoxic_rcp60= anova_len_jday_hypoxic_deep_prof_rcp60['GCMs']
#Param
param_contributions_len_jday_hypoxic_rcp60=anova_len_jday_hypoxic_deep_prof_rcp60['param']
#interaction
interact_contributions_len_jday_hypoxic_rcp60 =anova_len_jday_hypoxic_deep_prof_rcp60['interaction']

     
#first_jday_hypoxic_rcp85

#years
contributions_first_jday_hypoxic_rcp85_years=anova_first_jday_hypoxic_deep_prof_rcp85['year']
#GCMs
gcm_contributions_first_jday_hypoxic_rcp85= anova_first_jday_hypoxic_deep_prof_rcp85['GCMs']
#Param
param_contributions_first_jday_hypoxic_rcp85=anova_first_jday_hypoxic_deep_prof_rcp85['param']
#interaction
interact_contributions_first_jday_hypoxic_rcp85 =anova_first_jday_hypoxic_deep_prof_rcp85['interaction']


#len_jday_hypoxic_rcp85

#years
contributions_len_jday_hypoxic_rcp85_years=anova_len_jday_hypoxic_deep_prof_rcp85['year']
#GCMs
gcm_contributions_len_jday_hypoxic_rcp85= anova_len_jday_hypoxic_deep_prof_rcp85['GCMs']
#Param
param_contributions_len_jday_hypoxic_rcp85=anova_len_jday_hypoxic_deep_prof_rcp85['param']
#interaction
interact_contributions_len_jday_hypoxic_rcp85 =anova_len_jday_hypoxic_deep_prof_rcp85['interaction']

     
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
axs[0].set_title('First day of deep hypoxia in His', fontsize=20)
axs[0].set_ylim(0,100)
axs[0].set_xlim(1861, 2005)
axs[0].tick_params(axis='both', which='major', labelsize=20)



axs[1].fill_between(contributions_len_jday_hypoxic_his_years, 0, gcm_contributions_len_jday_hypoxic_his , label='GCMs', alpha=0.7, color=colors[0], edgecolor='black')
axs[1].fill_between(contributions_len_jday_hypoxic_his_years, gcm_contributions_len_jday_hypoxic_his , gcm_contributions_len_jday_hypoxic_his + param_contributions_len_jday_hypoxic_his, label='Parameters', alpha=0.7, color=colors[1], edgecolor='black')
axs[1].fill_between(contributions_len_jday_hypoxic_his_years, gcm_contributions_len_jday_hypoxic_his  + param_contributions_len_jday_hypoxic_his, gcm_contributions_len_jday_hypoxic_his + param_contributions_len_jday_hypoxic_his + interact_contributions_len_jday_hypoxic_his, label='Interactions', alpha=0.7, color=colors[2], edgecolor='black')
axs[1].set_title('Duration of deep hypoxia in His', fontsize=20)
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
plt.savefig('uncertainty_first_len_deep_hypoxia_duration_allyears_his.png', dpi=300, bbox_inches='tight')

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
axs[0, 0].set_title('First day of deep hypoxia in RCP2.6', fontsize=20)
axs[0, 0].set_ylim(0,100)
axs[0, 0].set_xlim(2006, 2099)
axs[0, 0].tick_params(axis='both', which='major', labelsize=20)



axs[0, 1].fill_between(contributions_len_jday_hypoxic_rcp26_years, 0, gcm_contributions_len_jday_hypoxic_rcp26 , label='GCMs', alpha=0.7, color=colors[0], edgecolor='black')
axs[0, 1].fill_between(contributions_len_jday_hypoxic_rcp26_years, gcm_contributions_len_jday_hypoxic_rcp26 , gcm_contributions_len_jday_hypoxic_rcp26 + param_contributions_len_jday_hypoxic_rcp26, label='Parameters', alpha=0.7, color=colors[1], edgecolor='black')
axs[0, 1].fill_between(contributions_len_jday_hypoxic_rcp26_years, gcm_contributions_len_jday_hypoxic_rcp26  + param_contributions_len_jday_hypoxic_rcp26, gcm_contributions_len_jday_hypoxic_rcp26 + param_contributions_len_jday_hypoxic_rcp26 + interact_contributions_len_jday_hypoxic_rcp26, label='Interactions', alpha=0.7, color=colors[2], edgecolor='black')
axs[0, 1].set_title('Duration of deep hypoxia in RCP2.6', fontsize=20)
axs[0, 1].set_ylim(0,100)
axs[0, 1].set_xlim(2006, 2099)
axs[0, 1].tick_params(axis='both', which='major', labelsize=20)

axs[1, 0].fill_between(contributions_first_jday_hypoxic_rcp60_years, 0, gcm_contributions_first_jday_hypoxic_rcp60 , label='GCMs', alpha=0.7, color=colors[0], edgecolor='black')
axs[1, 0].fill_between(contributions_first_jday_hypoxic_rcp60_years, gcm_contributions_first_jday_hypoxic_rcp60 , gcm_contributions_first_jday_hypoxic_rcp60 + param_contributions_first_jday_hypoxic_rcp60, label='Parameters', alpha=0.7, color=colors[1], edgecolor='black')
axs[1, 0].fill_between(contributions_first_jday_hypoxic_rcp60_years, gcm_contributions_first_jday_hypoxic_rcp60  + param_contributions_first_jday_hypoxic_rcp60, gcm_contributions_first_jday_hypoxic_rcp60 + param_contributions_first_jday_hypoxic_rcp60 + interact_contributions_first_jday_hypoxic_rcp60, label='Interactions', alpha=0.7, color=colors[2], edgecolor='black')
axs[1, 0].set_title('First day of deep hypoxia in RCP6.0', fontsize=20)
axs[1, 0].set_ylim(0,100)
axs[1, 0].set_xlim(2006, 2099)
axs[1, 0].tick_params(axis='both', which='major', labelsize=20)



axs[1, 1].fill_between(contributions_len_jday_hypoxic_rcp60_years, 0, gcm_contributions_len_jday_hypoxic_rcp60 , label='GCMs', alpha=0.7, color=colors[0], edgecolor='black')
axs[1, 1].fill_between(contributions_len_jday_hypoxic_rcp60_years, gcm_contributions_len_jday_hypoxic_rcp60 , gcm_contributions_len_jday_hypoxic_rcp60 + param_contributions_len_jday_hypoxic_rcp60, label='Parameters', alpha=0.7, color=colors[1], edgecolor='black')
axs[1, 1].fill_between(contributions_len_jday_hypoxic_rcp60_years, gcm_contributions_len_jday_hypoxic_rcp60  + param_contributions_len_jday_hypoxic_rcp60, gcm_contributions_len_jday_hypoxic_rcp60 + param_contributions_len_jday_hypoxic_rcp60 + interact_contributions_len_jday_hypoxic_rcp60, label='Interactions', alpha=0.7, color=colors[2], edgecolor='black')
axs[1, 1].set_title('Duration of deep hypoxia in RCP6.0', fontsize=20)
axs[1, 1].set_ylim(0,100)
axs[1, 1].set_xlim(2006, 2099)
axs[1, 1].tick_params(axis='both', which='major', labelsize=20)




axs[2, 0].fill_between(contributions_first_jday_hypoxic_rcp85_years, 0, gcm_contributions_first_jday_hypoxic_rcp85 , label='GCMs', alpha=0.7, color=colors[0], edgecolor='black')
axs[2, 0].fill_between(contributions_first_jday_hypoxic_rcp85_years, gcm_contributions_first_jday_hypoxic_rcp85 , gcm_contributions_first_jday_hypoxic_rcp85 + param_contributions_first_jday_hypoxic_rcp85, label='Parameters', alpha=0.7, color=colors[1], edgecolor='black')
axs[2, 0].fill_between(contributions_first_jday_hypoxic_rcp85_years, gcm_contributions_first_jday_hypoxic_rcp85  + param_contributions_first_jday_hypoxic_rcp85, gcm_contributions_first_jday_hypoxic_rcp85 + param_contributions_first_jday_hypoxic_rcp85 + interact_contributions_first_jday_hypoxic_rcp85, label='Interactions', alpha=0.7, color=colors[2], edgecolor='black')
axs[2, 0].set_title('First day of deep hypoxia in RCP8.5', fontsize=20)
axs[2, 0].set_ylim(0,100)
axs[2, 0].set_xlim(2006, 2099)
axs[2, 0].tick_params(axis='both', which='major', labelsize=20)



axs[2, 1].fill_between(contributions_len_jday_hypoxic_rcp85_years, 0, gcm_contributions_len_jday_hypoxic_rcp85 , label='GCMs', alpha=0.7, color=colors[0], edgecolor='black')
axs[2, 1].fill_between(contributions_len_jday_hypoxic_rcp85_years, gcm_contributions_len_jday_hypoxic_rcp85 , gcm_contributions_len_jday_hypoxic_rcp85 + param_contributions_len_jday_hypoxic_rcp85, label='Parameters', alpha=0.7, color=colors[1], edgecolor='black')
axs[2, 1].fill_between(contributions_len_jday_hypoxic_rcp85_years, gcm_contributions_len_jday_hypoxic_rcp85  + param_contributions_len_jday_hypoxic_rcp85, gcm_contributions_len_jday_hypoxic_rcp85 + param_contributions_len_jday_hypoxic_rcp85 + interact_contributions_len_jday_hypoxic_rcp85, label='Interactions', alpha=0.7, color=colors[2], edgecolor='black')
axs[2, 1].set_title('Duration of deep hypoxia in RCP8.5', fontsize=20)
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
plt.savefig('uncertainty_first_len_deep_hypoxia_duration_allyears_rcps.png', dpi=300, bbox_inches='tight')

plt.show()


#%% Uncertainity of 80 years in RCPs

#first_jday_hypoxic_rcp26

#years
contributions_first_jday_hypoxic_rcp26_years=anova_first_jday_hypoxic_deep_prof_rcp26[anova_first_jday_hypoxic_deep_prof_rcp26['year']>2019]['year']
#GCMs
gcm_contributions_first_jday_hypoxic_rcp26= anova_first_jday_hypoxic_deep_prof_rcp26[anova_first_jday_hypoxic_deep_prof_rcp26['year']>2019]['GCMs']
#Param
param_contributions_first_jday_hypoxic_rcp26=anova_first_jday_hypoxic_deep_prof_rcp26[anova_first_jday_hypoxic_deep_prof_rcp26['year']>2019]['param']
#interaction
interact_contributions_first_jday_hypoxic_rcp26 =anova_first_jday_hypoxic_deep_prof_rcp26[anova_first_jday_hypoxic_deep_prof_rcp26['year']>2019]['interaction']


#len_jday_hypoxic_rcp26

#years
contributions_len_jday_hypoxic_rcp26_years=anova_len_jday_hypoxic_deep_prof_rcp26[anova_len_jday_hypoxic_deep_prof_rcp26['year']>2019]['year']
#GCMs
gcm_contributions_len_jday_hypoxic_rcp26= anova_len_jday_hypoxic_deep_prof_rcp26[anova_len_jday_hypoxic_deep_prof_rcp26['year']>2019]['GCMs']
#Param
param_contributions_len_jday_hypoxic_rcp26=anova_len_jday_hypoxic_deep_prof_rcp26[anova_len_jday_hypoxic_deep_prof_rcp26['year']>2019]['param']
#interaction
interact_contributions_len_jday_hypoxic_rcp26 =anova_len_jday_hypoxic_deep_prof_rcp26[anova_len_jday_hypoxic_deep_prof_rcp26['year']>2019]['interaction']


     

#first_jday_hypoxic_rcp60

#years
contributions_first_jday_hypoxic_rcp60_years=anova_first_jday_hypoxic_deep_prof_rcp60[anova_first_jday_hypoxic_deep_prof_rcp60['year']>2019]['year']
#GCMs
gcm_contributions_first_jday_hypoxic_rcp60= anova_first_jday_hypoxic_deep_prof_rcp60[anova_first_jday_hypoxic_deep_prof_rcp60['year']>2019]['GCMs']
#Param
param_contributions_first_jday_hypoxic_rcp60=anova_first_jday_hypoxic_deep_prof_rcp60[anova_first_jday_hypoxic_deep_prof_rcp60['year']>2019]['param']
#interaction
interact_contributions_first_jday_hypoxic_rcp60 =anova_first_jday_hypoxic_deep_prof_rcp60[anova_first_jday_hypoxic_deep_prof_rcp60['year']>2019]['interaction']


#len_jday_hypoxic_rcp60

#years
contributions_len_jday_hypoxic_rcp60_years=anova_len_jday_hypoxic_deep_prof_rcp60[anova_len_jday_hypoxic_deep_prof_rcp60['year']>2019]['year']
#GCMs
gcm_contributions_len_jday_hypoxic_rcp60= anova_len_jday_hypoxic_deep_prof_rcp60[anova_len_jday_hypoxic_deep_prof_rcp60['year']>2019]['GCMs']
#Param
param_contributions_len_jday_hypoxic_rcp60=anova_len_jday_hypoxic_deep_prof_rcp60[anova_len_jday_hypoxic_deep_prof_rcp60['year']>2019]['param']
#interaction
interact_contributions_len_jday_hypoxic_rcp60 =anova_len_jday_hypoxic_deep_prof_rcp60[anova_len_jday_hypoxic_deep_prof_rcp60['year']>2019]['interaction']


#first_jday_hypoxic_rcp85

#years
contributions_first_jday_hypoxic_rcp85_years=anova_first_jday_hypoxic_deep_prof_rcp85[anova_first_jday_hypoxic_deep_prof_rcp85['year']>2019]['year']
#GCMs
gcm_contributions_first_jday_hypoxic_rcp85= anova_first_jday_hypoxic_deep_prof_rcp85[anova_first_jday_hypoxic_deep_prof_rcp85['year']>2019]['GCMs']
#Param
param_contributions_first_jday_hypoxic_rcp85=anova_first_jday_hypoxic_deep_prof_rcp85[anova_first_jday_hypoxic_deep_prof_rcp85['year']>2019]['param']
#interaction
interact_contributions_first_jday_hypoxic_rcp85 =anova_first_jday_hypoxic_deep_prof_rcp85[anova_first_jday_hypoxic_deep_prof_rcp85['year']>2019]['interaction']


#len_jday_hypoxic_rcp85

#years
contributions_len_jday_hypoxic_rcp85_years=anova_len_jday_hypoxic_deep_prof_rcp85[anova_len_jday_hypoxic_deep_prof_rcp85['year']>2019]['year']
#GCMs
gcm_contributions_len_jday_hypoxic_rcp85= anova_len_jday_hypoxic_deep_prof_rcp85[anova_len_jday_hypoxic_deep_prof_rcp85['year']>2019]['GCMs']
#Param
param_contributions_len_jday_hypoxic_rcp85=anova_len_jday_hypoxic_deep_prof_rcp85[anova_len_jday_hypoxic_deep_prof_rcp85['year']>2019]['param']
#interaction
interact_contributions_len_jday_hypoxic_rcp85 =anova_len_jday_hypoxic_deep_prof_rcp85[anova_len_jday_hypoxic_deep_prof_rcp85['year']>2019]['interaction']



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
axs[0, 0].set_title('First day of deep hypoxia in RCP2.6', fontsize=20)
axs[0, 0].set_ylim(0,100)
axs[0, 0].set_xlim(2020, 2099)
axs[0, 0].tick_params(axis='both', which='major', labelsize=20)



axs[0, 1].fill_between(contributions_len_jday_hypoxic_rcp26_years, 0, gcm_contributions_len_jday_hypoxic_rcp26 , label='GCMs', alpha=0.7, color=colors[0], edgecolor='black')
axs[0, 1].fill_between(contributions_len_jday_hypoxic_rcp26_years, gcm_contributions_len_jday_hypoxic_rcp26 , gcm_contributions_len_jday_hypoxic_rcp26 + param_contributions_len_jday_hypoxic_rcp26, label='Parameters', alpha=0.7, color=colors[1], edgecolor='black')
axs[0, 1].fill_between(contributions_len_jday_hypoxic_rcp26_years, gcm_contributions_len_jday_hypoxic_rcp26  + param_contributions_len_jday_hypoxic_rcp26, gcm_contributions_len_jday_hypoxic_rcp26 + param_contributions_len_jday_hypoxic_rcp26 + interact_contributions_len_jday_hypoxic_rcp26, label='Interactions', alpha=0.7, color=colors[2], edgecolor='black')
axs[0, 1].set_title('Duration of deep hypoxia in RCP2.6', fontsize=20)
axs[0, 1].set_ylim(0,100)
axs[0, 1].set_xlim(2020, 2099)
axs[0, 1].tick_params(axis='both', which='major', labelsize=20)

axs[1, 0].fill_between(contributions_first_jday_hypoxic_rcp60_years, 0, gcm_contributions_first_jday_hypoxic_rcp60 , label='GCMs', alpha=0.7, color=colors[0], edgecolor='black')
axs[1, 0].fill_between(contributions_first_jday_hypoxic_rcp60_years, gcm_contributions_first_jday_hypoxic_rcp60 , gcm_contributions_first_jday_hypoxic_rcp60 + param_contributions_first_jday_hypoxic_rcp60, label='Parameters', alpha=0.7, color=colors[1], edgecolor='black')
axs[1, 0].fill_between(contributions_first_jday_hypoxic_rcp60_years, gcm_contributions_first_jday_hypoxic_rcp60  + param_contributions_first_jday_hypoxic_rcp60, gcm_contributions_first_jday_hypoxic_rcp60 + param_contributions_first_jday_hypoxic_rcp60 + interact_contributions_first_jday_hypoxic_rcp60, label='Interactions', alpha=0.7, color=colors[2], edgecolor='black')
axs[1, 0].set_title('First day of deep hypoxia in RCP6.0', fontsize=20)
axs[1, 0].set_ylim(0,100)
axs[1, 0].set_xlim(2020, 2099)
axs[1, 0].tick_params(axis='both', which='major', labelsize=20)



axs[1, 1].fill_between(contributions_len_jday_hypoxic_rcp60_years, 0, gcm_contributions_len_jday_hypoxic_rcp60 , label='GCMs', alpha=0.7, color=colors[0], edgecolor='black')
axs[1, 1].fill_between(contributions_len_jday_hypoxic_rcp60_years, gcm_contributions_len_jday_hypoxic_rcp60 , gcm_contributions_len_jday_hypoxic_rcp60 + param_contributions_len_jday_hypoxic_rcp60, label='Parameters', alpha=0.7, color=colors[1], edgecolor='black')
axs[1, 1].fill_between(contributions_len_jday_hypoxic_rcp60_years, gcm_contributions_len_jday_hypoxic_rcp60  + param_contributions_len_jday_hypoxic_rcp60, gcm_contributions_len_jday_hypoxic_rcp60 + param_contributions_len_jday_hypoxic_rcp60 + interact_contributions_len_jday_hypoxic_rcp60, label='Interactions', alpha=0.7, color=colors[2], edgecolor='black')
axs[1, 1].set_title('Duration of deep hypoxia in RCP6.0', fontsize=20)
axs[1, 1].set_ylim(0,100)
axs[1, 1].set_xlim(2020, 2099)
axs[1, 1].tick_params(axis='both', which='major', labelsize=20)




axs[2, 0].fill_between(contributions_first_jday_hypoxic_rcp85_years, 0, gcm_contributions_first_jday_hypoxic_rcp85 , label='GCMs', alpha=0.7, color=colors[0], edgecolor='black')
axs[2, 0].fill_between(contributions_first_jday_hypoxic_rcp85_years, gcm_contributions_first_jday_hypoxic_rcp85 , gcm_contributions_first_jday_hypoxic_rcp85 + param_contributions_first_jday_hypoxic_rcp85, label='Parameters', alpha=0.7, color=colors[1], edgecolor='black')
axs[2, 0].fill_between(contributions_first_jday_hypoxic_rcp85_years, gcm_contributions_first_jday_hypoxic_rcp85  + param_contributions_first_jday_hypoxic_rcp85, gcm_contributions_first_jday_hypoxic_rcp85 + param_contributions_first_jday_hypoxic_rcp85 + interact_contributions_first_jday_hypoxic_rcp85, label='Interactions', alpha=0.7, color=colors[2], edgecolor='black')
axs[2, 0].set_title('First day of deep hypoxia in RCP8.5', fontsize=20)
axs[2, 0].set_ylim(0,100)
axs[2, 0].set_xlim(2020, 2099)
axs[2, 0].tick_params(axis='both', which='major', labelsize=20)



axs[2, 1].fill_between(contributions_len_jday_hypoxic_rcp85_years, 0, gcm_contributions_len_jday_hypoxic_rcp85 , label='GCMs', alpha=0.7, color=colors[0], edgecolor='black')
axs[2, 1].fill_between(contributions_len_jday_hypoxic_rcp85_years, gcm_contributions_len_jday_hypoxic_rcp85 , gcm_contributions_len_jday_hypoxic_rcp85 + param_contributions_len_jday_hypoxic_rcp85, label='Parameters', alpha=0.7, color=colors[1], edgecolor='black')
axs[2, 1].fill_between(contributions_len_jday_hypoxic_rcp85_years, gcm_contributions_len_jday_hypoxic_rcp85  + param_contributions_len_jday_hypoxic_rcp85, gcm_contributions_len_jday_hypoxic_rcp85 + param_contributions_len_jday_hypoxic_rcp85 + interact_contributions_len_jday_hypoxic_rcp85, label='Interactions', alpha=0.7, color=colors[2], edgecolor='black')
axs[2, 1].set_title('Duration of deep hypoxia in RCP8.5', fontsize=20)
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
plt.savefig('uncertainty_first_len_deep_hypoxia_duration_allyears_rcps_80years.png', dpi=300, bbox_inches='tight')

plt.show()


#%%#
#=====================================GLUE ============================

#%%his

# first_jday_hypoxic_deep_prof_inyear_his
timeseries_year_his= all_first_jday_hypoxic_deep_prof_inyear_his.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_first_jday_hypoxic_deep_prof_inyear_his.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights_his))

# Build glue df
glue_first_jday_hypoxic_deep_prof_inyear_his = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_first_jday_hypoxic_deep_prof_inyear_his=glue_first_jday_hypoxic_deep_prof_inyear_his.set_index(timeseries_year_his)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory
glue_first_jday_hypoxic_deep_prof_inyear_his.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/his/glue_first_jday_hypoxic_deep_prof_inyear_his.csv')



# last_jday_hypoxic_deep_prof_inyear_his
timeseries_year_his= all_last_jday_hypoxic_deep_prof_inyear_his.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_last_jday_hypoxic_deep_prof_inyear_his.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights_his))

# Build glue df
glue_last_jday_hypoxic_deep_prof_inyear_his = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_last_jday_hypoxic_deep_prof_inyear_his=glue_last_jday_hypoxic_deep_prof_inyear_his.set_index(timeseries_year_his)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory
glue_last_jday_hypoxic_deep_prof_inyear_his.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/his/glue_last_jday_hypoxic_deep_prof_inyear_his.csv')

           

# len_hypoxic_deep_prof_inyear_his
timeseries_year_his= all_len_hypoxic_deep_prof_inyear_his.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_len_hypoxic_deep_prof_inyear_his.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights_his))

# Build glue df
glue_len_hypoxic_deep_prof_inyear_his = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_len_hypoxic_deep_prof_inyear_his=glue_len_hypoxic_deep_prof_inyear_his.set_index(timeseries_year_his)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory
glue_len_hypoxic_deep_prof_inyear_his.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/his/glue_len_hypoxic_deep_prof_inyear_his.csv')


#%%rcp26

# first_jday_hypoxic_deep_prof_inyear_rcp26
timeseries_year_rcp26= all_first_jday_hypoxic_deep_prof_inyear_rcp26.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_first_jday_hypoxic_deep_prof_inyear_rcp26.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights_rcp26))

# Build glue df
glue_first_jday_hypoxic_deep_prof_inyear_rcp26 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_first_jday_hypoxic_deep_prof_inyear_rcp26=glue_first_jday_hypoxic_deep_prof_inyear_rcp26.set_index(timeseries_year_rcp26)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory
glue_first_jday_hypoxic_deep_prof_inyear_rcp26.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/rcp26/glue_first_jday_hypoxic_deep_prof_inyear_rcp26.csv')



# last_jday_hypoxic_deep_prof_inyear_rcp26
timeseries_year_rcp26= all_last_jday_hypoxic_deep_prof_inyear_rcp26.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_last_jday_hypoxic_deep_prof_inyear_rcp26.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights_rcp26))

# Build glue df
glue_last_jday_hypoxic_deep_prof_inyear_rcp26 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_last_jday_hypoxic_deep_prof_inyear_rcp26=glue_last_jday_hypoxic_deep_prof_inyear_rcp26.set_index(timeseries_year_rcp26)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory
glue_last_jday_hypoxic_deep_prof_inyear_rcp26.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/rcp26/glue_last_jday_hypoxic_deep_prof_inyear_rcp26.csv')

           

# len_hypoxic_deep_prof_inyear_rcp26
timeseries_year_rcp26= all_len_hypoxic_deep_prof_inyear_rcp26.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_len_hypoxic_deep_prof_inyear_rcp26.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights_rcp26))

# Build glue df
glue_len_hypoxic_deep_prof_inyear_rcp26 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_len_hypoxic_deep_prof_inyear_rcp26=glue_len_hypoxic_deep_prof_inyear_rcp26.set_index(timeseries_year_rcp26)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory
glue_len_hypoxic_deep_prof_inyear_rcp26.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/rcp26/glue_len_hypoxic_deep_prof_inyear_rcp26.csv')


#%%rcp60

# first_jday_hypoxic_deep_prof_inyear_rcp60
timeseries_year_rcp60= all_first_jday_hypoxic_deep_prof_inyear_rcp60.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_first_jday_hypoxic_deep_prof_inyear_rcp60.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights_rcp60))

# Build glue df
glue_first_jday_hypoxic_deep_prof_inyear_rcp60 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_first_jday_hypoxic_deep_prof_inyear_rcp60=glue_first_jday_hypoxic_deep_prof_inyear_rcp60.set_index(timeseries_year_rcp60)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory
glue_first_jday_hypoxic_deep_prof_inyear_rcp60.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/rcp60/glue_first_jday_hypoxic_deep_prof_inyear_rcp60.csv')



# last_jday_hypoxic_deep_prof_inyear_rcp60
timeseries_year_rcp60= all_last_jday_hypoxic_deep_prof_inyear_rcp60.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_last_jday_hypoxic_deep_prof_inyear_rcp60.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights_rcp60))

# Build glue df
glue_last_jday_hypoxic_deep_prof_inyear_rcp60 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_last_jday_hypoxic_deep_prof_inyear_rcp60=glue_last_jday_hypoxic_deep_prof_inyear_rcp60.set_index(timeseries_year_rcp60)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory
glue_last_jday_hypoxic_deep_prof_inyear_rcp60.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/rcp60/glue_last_jday_hypoxic_deep_prof_inyear_rcp60.csv')

           

# len_hypoxic_deep_prof_inyear_rcp60
timeseries_year_rcp60= all_len_hypoxic_deep_prof_inyear_rcp60.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_len_hypoxic_deep_prof_inyear_rcp60.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights_rcp60))

# Build glue df
glue_len_hypoxic_deep_prof_inyear_rcp60 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_len_hypoxic_deep_prof_inyear_rcp60=glue_len_hypoxic_deep_prof_inyear_rcp60.set_index(timeseries_year_rcp60)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory
glue_len_hypoxic_deep_prof_inyear_rcp60.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/rcp60/glue_len_hypoxic_deep_prof_inyear_rcp60.csv')

#%%rcp85

# first_jday_hypoxic_deep_prof_inyear_rcp85
timeseries_year_rcp85= all_first_jday_hypoxic_deep_prof_inyear_rcp85.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_first_jday_hypoxic_deep_prof_inyear_rcp85.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights_rcp85))

# Build glue df
glue_first_jday_hypoxic_deep_prof_inyear_rcp85 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_first_jday_hypoxic_deep_prof_inyear_rcp85=glue_first_jday_hypoxic_deep_prof_inyear_rcp85.set_index(timeseries_year_rcp85)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory
glue_first_jday_hypoxic_deep_prof_inyear_rcp85.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/rcp85/glue_first_jday_hypoxic_deep_prof_inyear_rcp85.csv')



# last_jday_hypoxic_deep_prof_inyear_rcp85
timeseries_year_rcp85= all_last_jday_hypoxic_deep_prof_inyear_rcp85.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_last_jday_hypoxic_deep_prof_inyear_rcp85.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights_rcp85))

# Build glue df
glue_last_jday_hypoxic_deep_prof_inyear_rcp85 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_last_jday_hypoxic_deep_prof_inyear_rcp85=glue_last_jday_hypoxic_deep_prof_inyear_rcp85.set_index(timeseries_year_rcp85)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory
glue_last_jday_hypoxic_deep_prof_inyear_rcp85.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/rcp85/glue_last_jday_hypoxic_deep_prof_inyear_rcp85.csv')

           

# len_hypoxic_deep_prof_inyear_rcp85
timeseries_year_rcp85= all_len_hypoxic_deep_prof_inyear_rcp85.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_len_hypoxic_deep_prof_inyear_rcp85.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights_rcp85))

# Build glue df
glue_len_hypoxic_deep_prof_inyear_rcp85 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_len_hypoxic_deep_prof_inyear_rcp85=glue_len_hypoxic_deep_prof_inyear_rcp85.set_index(timeseries_year_rcp85)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory
glue_len_hypoxic_deep_prof_inyear_rcp85.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/rcp85/glue_len_hypoxic_deep_prof_inyear_rcp85.csv')

#%%replaced by nan values 

glue_first_jday_hypoxic_deep_prof_inyear_his=glue_first_jday_hypoxic_deep_prof_inyear_his.replace(0, np.nan)

glue_first_jday_hypoxic_deep_prof_inyear_rcp26=glue_first_jday_hypoxic_deep_prof_inyear_rcp26.replace(0, np.nan)

glue_first_jday_hypoxic_deep_prof_inyear_rcp60=glue_first_jday_hypoxic_deep_prof_inyear_rcp60.replace(0, np.nan)

glue_first_jday_hypoxic_deep_prof_inyear_rcp85=glue_first_jday_hypoxic_deep_prof_inyear_rcp85.replace(0, np.nan)

#%%Sorting the glue first_jday dataframe according to the index (year)


glue_first_jday_hypoxic_deep_prof_inyear_his=glue_first_jday_hypoxic_deep_prof_inyear_his.sort_index()

glue_first_jday_hypoxic_deep_prof_inyear_rcp26=glue_first_jday_hypoxic_deep_prof_inyear_rcp26.sort_index()

glue_first_jday_hypoxic_deep_prof_inyear_rcp60=glue_first_jday_hypoxic_deep_prof_inyear_rcp60.sort_index()

glue_first_jday_hypoxic_deep_prof_inyear_rcp85=glue_first_jday_hypoxic_deep_prof_inyear_rcp85.sort_index()


#%%Sorting the glue dataframe according to the index (year)

glue_len_hypoxic_deep_prof_inyear_his=glue_len_hypoxic_deep_prof_inyear_his.sort_index()

glue_len_hypoxic_deep_prof_inyear_rcp26=glue_len_hypoxic_deep_prof_inyear_rcp26.sort_index()

glue_len_hypoxic_deep_prof_inyear_rcp60=glue_len_hypoxic_deep_prof_inyear_rcp60.sort_index()

glue_len_hypoxic_deep_prof_inyear_rcp85=glue_len_hypoxic_deep_prof_inyear_rcp85.sort_index()


#%%Plotiing%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

#%%duration of deep hypoxia 



os.chdir('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/')

import matplotlib.pyplot as plt

fig =plt.figure(figsize=(15, 10))
ax= plt.subplot(111)


ax=plt.fill_between(glue_len_hypoxic_deep_prof_inyear_his.index.astype(float), glue_len_hypoxic_deep_prof_inyear_his['5%'], glue_len_hypoxic_deep_prof_inyear_his['95%'], color='grey', alpha=0.2 ,  label= 'His 90% CI')
ax=plt.plot(glue_len_hypoxic_deep_prof_inyear_his.index.astype(float), glue_len_hypoxic_deep_prof_inyear_his['50%'].astype(float), 'k', label='His median', alpha=0.9, linewidth=3  )


ax=plt.fill_between(glue_len_hypoxic_deep_prof_inyear_rcp26.index.astype(float), glue_len_hypoxic_deep_prof_inyear_rcp26['5%'], glue_len_hypoxic_deep_prof_inyear_rcp26['95%'], color='green', alpha=0.3 ,  label= 'RCP2.6 90% CI')
ax=plt.plot(glue_len_hypoxic_deep_prof_inyear_rcp26.index.astype(float), glue_len_hypoxic_deep_prof_inyear_rcp26['50%'].astype(float), 'darkgreen', label='RCP2.6 median', alpha=0.9, linewidth=3  )

ax=plt.fill_between(glue_len_hypoxic_deep_prof_inyear_rcp60.index.astype(float), glue_len_hypoxic_deep_prof_inyear_rcp60['5%'], glue_len_hypoxic_deep_prof_inyear_rcp60['95%'], color='yellow', alpha=0.6 ,  label= 'RCP6.0 90% CI')
ax=plt.plot(glue_len_hypoxic_deep_prof_inyear_rcp60.index.astype(float), glue_len_hypoxic_deep_prof_inyear_rcp60['50%'].astype(float), 'yellow', label='RCP6.0 median', alpha=0.9, linewidth=3  )

ax=plt.fill_between(glue_len_hypoxic_deep_prof_inyear_rcp85.index.astype(float), glue_len_hypoxic_deep_prof_inyear_rcp85['5%'], glue_len_hypoxic_deep_prof_inyear_rcp85['95%'], color='red', alpha=0.2 ,  label= 'RCP8.5 90% CI')
ax=plt.plot(glue_len_hypoxic_deep_prof_inyear_rcp85.index.astype(float), glue_len_hypoxic_deep_prof_inyear_rcp85['50%'].astype(float), 'r', label='RCP8.5 median', alpha=0.9, linewidth=3  )

ax=plt.ylabel('Duration of deep hypoxia [d]' , fontsize=26)
ax=plt.xlabel('Year' , fontsize=26)
ax=plt.yticks(fontsize= 22)
ax=plt.xticks(rotation=45 , fontsize=22)
ax=plt.legend(bbox_to_anchor=(1.1, -0.2), fontsize=22, ncol=4)#)   
fig.savefig("GLUE_Timeseries_length_deep_hypoxic_16combinationJaJv_ave_obs_4models_4scenarios.png",  dpi=300, bbox_inches='tight')



#%%
np.mean(glue_len_hypoxic_deep_prof_inyear_his['50%'])#49.51443360571123
np.mean(glue_len_hypoxic_deep_prof_inyear_rcp26['50%'])#63.85309627518068
np.mean(glue_len_hypoxic_deep_prof_inyear_rcp60['50%'])#66.37516667473243
np.mean(glue_len_hypoxic_deep_prof_inyear_rcp85['50%'])#71.56247383643593

#%%hypoxic_factor 30 yerars from each scenarios compare 



#anomaly 
# baseline [1976-2005]
len_hypoxic_deep_prof_inyear_ref=glue_len_hypoxic_deep_prof_inyear_his[1975 < glue_len_hypoxic_deep_prof_inyear_his.index]['50%'].mean()
#50.426956555924754

#near future [2030-2059] # maximum temp in 2033

glue_len_hypoxic_deep_prof_inyear_rcp26[(2029 < glue_len_hypoxic_deep_prof_inyear_rcp26.index) & (glue_len_hypoxic_deep_prof_inyear_rcp26.index < 2060)]['50%'].mean()
# 64.89917450065333
glue_len_hypoxic_deep_prof_inyear_rcp60[(2029 < glue_len_hypoxic_deep_prof_inyear_rcp60.index) & (glue_len_hypoxic_deep_prof_inyear_rcp60.index < 2060)]['50%'].mean()
# 63.12307950184921
glue_len_hypoxic_deep_prof_inyear_rcp85[(2029 < glue_len_hypoxic_deep_prof_inyear_rcp85.index) & (glue_len_hypoxic_deep_prof_inyear_rcp85.index < 2060)]['50%'].mean()
# 67.03709616532731

 
#Distant future [2070-2099]

glue_len_hypoxic_deep_prof_inyear_rcp26[(2069 < glue_len_hypoxic_deep_prof_inyear_rcp26.index) & (glue_len_hypoxic_deep_prof_inyear_rcp26.index < 2100)]['50%'].mean()
#65.23161913671755
glue_len_hypoxic_deep_prof_inyear_rcp60[(2069 < glue_len_hypoxic_deep_prof_inyear_rcp60.index) & (glue_len_hypoxic_deep_prof_inyear_rcp60.index< 2100)]['50%'].mean()
# 74.39034590789441
glue_len_hypoxic_deep_prof_inyear_rcp85[(2069 < glue_len_hypoxic_deep_prof_inyear_rcp85.index) & (glue_len_hypoxic_deep_prof_inyear_rcp85.index < 2100)]['50%'].mean()
#84.76007667514622
           



#%%len of deep hypoxia_anomaly 
os.chdir('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/')

import matplotlib.pyplot as plt

fig =plt.figure(figsize=(15, 10))
ax= plt.subplot(111)


ax=plt.fill_between(glue_len_hypoxic_deep_prof_inyear_his[1975 < glue_len_hypoxic_deep_prof_inyear_his.index].index.astype(float),
                      glue_len_hypoxic_deep_prof_inyear_his[1975 < glue_len_hypoxic_deep_prof_inyear_his.index]['5%'] - len_hypoxic_deep_prof_inyear_ref,
                      glue_len_hypoxic_deep_prof_inyear_his[1975 < glue_len_hypoxic_deep_prof_inyear_his.index ]['95%'] - len_hypoxic_deep_prof_inyear_ref,
                      color='grey', alpha=0.2, label='His 90% CI')


ax=plt.plot(glue_len_hypoxic_deep_prof_inyear_his[1975< glue_len_hypoxic_deep_prof_inyear_his.index ].index.astype(float),
            glue_len_hypoxic_deep_prof_inyear_his[1975 < glue_len_hypoxic_deep_prof_inyear_his.index]['50%'] - len_hypoxic_deep_prof_inyear_ref,
            'k', label='His median', alpha=0.9, linewidth=3   )

ax=plt.fill_between(glue_len_hypoxic_deep_prof_inyear_rcp26.index.astype(float), glue_len_hypoxic_deep_prof_inyear_rcp26['5%']-len_hypoxic_deep_prof_inyear_ref, glue_len_hypoxic_deep_prof_inyear_rcp26['95%']-len_hypoxic_deep_prof_inyear_ref, color='darkgreen', alpha=0.2 ,  label= 'RCP6.0 90% CI')
ax=plt.plot(glue_len_hypoxic_deep_prof_inyear_rcp26.index.astype(float), glue_len_hypoxic_deep_prof_inyear_rcp26['50%']-len_hypoxic_deep_prof_inyear_ref, 'darkgreen', label='RCP6.0 median', alpha=0.9, linewidth=3  )
                      
                     
ax=plt.fill_between(glue_len_hypoxic_deep_prof_inyear_rcp60.index.astype(float), glue_len_hypoxic_deep_prof_inyear_rcp60['5%']-len_hypoxic_deep_prof_inyear_ref, glue_len_hypoxic_deep_prof_inyear_rcp60['95%']-len_hypoxic_deep_prof_inyear_ref, color='yellow', alpha=0.5 ,  label= 'RCP6.0 90% CI')
ax=plt.plot(glue_len_hypoxic_deep_prof_inyear_rcp60.index.astype(float), glue_len_hypoxic_deep_prof_inyear_rcp60['50%']-len_hypoxic_deep_prof_inyear_ref, 'yellow', label='RCP6.0 median', alpha=0.9, linewidth=3  )

ax=plt.fill_between(glue_len_hypoxic_deep_prof_inyear_rcp85.index.astype(float), glue_len_hypoxic_deep_prof_inyear_rcp85['5%']-len_hypoxic_deep_prof_inyear_ref, glue_len_hypoxic_deep_prof_inyear_rcp85['95%']-len_hypoxic_deep_prof_inyear_ref, color='r', alpha=0.2 ,  label= 'RCP8.5 90% CI')
ax=plt.plot(glue_len_hypoxic_deep_prof_inyear_rcp85.index.astype(float), glue_len_hypoxic_deep_prof_inyear_rcp85['50%']-len_hypoxic_deep_prof_inyear_ref, 'r', label='RCP8.5 median', alpha=0.9, linewidth=3  )

ax=plt.ylabel('Anomaly of deepest layer hypoxia duration [d]' , fontsize=26)
ax=plt.xlabel('Year' , fontsize=26)
ax=plt.yticks(fontsize= 22)
ax=plt.xticks(rotation=45 , fontsize=22)
ax=plt.legend(bbox_to_anchor=(1.1, -0.2), fontsize=22, ncol=4)  
fig.savefig("GLUE_Timeseries_len_hypoxic_deep_prof_anomaly_16combinationJaJv_ave_obs_4models_4scenarios.png",  dpi=300, bbox_inches='tight')

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% condition ###############
#########################################################################

#%%Plotiing%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

#%%First Jday with deep hypoxic



os.chdir('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/')

import matplotlib.pyplot as plt

fig =plt.figure(figsize=(15, 10))
ax= plt.subplot(111)


ax=plt.fill_between(glue_first_jday_hypoxic_deep_prof_inyear_his.index.astype(float), glue_first_jday_hypoxic_deep_prof_inyear_his['5%'], glue_first_jday_hypoxic_deep_prof_inyear_his['95%'], color='grey', alpha=0.2 ,  label= 'His 90% CI')
ax=plt.plot(glue_first_jday_hypoxic_deep_prof_inyear_his.index.astype(float), glue_first_jday_hypoxic_deep_prof_inyear_his['50%'].astype(float), 'k', label='His median', alpha=0.9, linewidth=3  )


ax=plt.fill_between(glue_first_jday_hypoxic_deep_prof_inyear_rcp26.index.astype(float), glue_first_jday_hypoxic_deep_prof_inyear_rcp26['5%'], glue_first_jday_hypoxic_deep_prof_inyear_rcp26['95%'], color='darkgreen', alpha=0.3 ,  label= 'RCP2.6 90% CI')
ax=plt.plot(glue_first_jday_hypoxic_deep_prof_inyear_rcp26.index.astype(float), glue_first_jday_hypoxic_deep_prof_inyear_rcp26['50%'].astype(float), 'darkgreen', label='RCP2.6 median', alpha=0.9, linewidth=3  )

ax=plt.fill_between(glue_first_jday_hypoxic_deep_prof_inyear_rcp60.index.astype(float), glue_first_jday_hypoxic_deep_prof_inyear_rcp60['5%'], glue_first_jday_hypoxic_deep_prof_inyear_rcp60['95%'], color='yellow', alpha=0.5,  label= 'RCP6.0 90% CI')
ax=plt.plot(glue_first_jday_hypoxic_deep_prof_inyear_rcp60.index.astype(float), glue_first_jday_hypoxic_deep_prof_inyear_rcp60['50%'].astype(float), 'yellow', label='RCP6.0 median', alpha=0.9, linewidth=3  )

ax=plt.fill_between(glue_first_jday_hypoxic_deep_prof_inyear_rcp85.index.astype(float), glue_first_jday_hypoxic_deep_prof_inyear_rcp85['5%'], glue_first_jday_hypoxic_deep_prof_inyear_rcp85['95%'], color='red', alpha=0.2 ,  label= 'RCP8.5 90% CI')
ax=plt.plot(glue_first_jday_hypoxic_deep_prof_inyear_rcp85.index.astype(float), glue_first_jday_hypoxic_deep_prof_inyear_rcp85['50%'].astype(float), 'r', label='RCP8.5 median', alpha=0.9, linewidth=3  )

ax=plt.ylabel('First hypoxia duration in\n deepest layer [Jday]' , fontsize=26)
ax=plt.xlabel('Year' , fontsize=26)
ax=plt.yticks(fontsize= 22)
ax=plt.xticks(rotation=45 , fontsize=22)
ax=plt.legend(bbox_to_anchor=(1.1, -0.2), fontsize=22 , ncol=4)#)   
fig.savefig("GLUE_Timeseries_first_deep_hypoxic_16combinationJaJv_ave_obs_4models_4scenarios.png",  dpi=300, bbox_inches='tight')




#%%
np.mean(glue_first_jday_hypoxic_deep_prof_inyear_his['50%'])#191.55433346615138
np.mean(glue_first_jday_hypoxic_deep_prof_inyear_rcp26['50%'])#184.84279062641144
np.mean(glue_first_jday_hypoxic_deep_prof_inyear_rcp60['50%'])#182.5930386669312
np.mean(glue_first_jday_hypoxic_deep_prof_inyear_rcp85['50%'])# 179.6173593987038


#%%hypoxic_factor 30 yerars from each scenarios compare 


#anomaly 
# his [1976-2005]
first_jday_hypoxic_deep_prof_inyear_ref=glue_first_jday_hypoxic_deep_prof_inyear_his[1975< glue_first_jday_hypoxic_deep_prof_inyear_his.index]['50%'].mean()
#194.35386565698317


#near future [2030-205]

glue_first_jday_hypoxic_deep_prof_inyear_rcp26[(2029 < glue_first_jday_hypoxic_deep_prof_inyear_rcp26.index) & (glue_first_jday_hypoxic_deep_prof_inyear_rcp26.index < 2060)]['50%'].mean()
#184.33631722334215
glue_first_jday_hypoxic_deep_prof_inyear_rcp60[(2029 < glue_first_jday_hypoxic_deep_prof_inyear_rcp60.index) & (glue_first_jday_hypoxic_deep_prof_inyear_rcp60.index < 2060)]['50%'].mean()
#183.88780716825565
glue_first_jday_hypoxic_deep_prof_inyear_rcp85[(2029 < glue_first_jday_hypoxic_deep_prof_inyear_rcp85.index) & (glue_first_jday_hypoxic_deep_prof_inyear_rcp85.index < 2060)]['50%'].mean()
#181.86560301942978

 
#Distant future [2070-2099]

glue_first_jday_hypoxic_deep_prof_inyear_rcp26[(2069 < glue_first_jday_hypoxic_deep_prof_inyear_rcp26.index) & (glue_first_jday_hypoxic_deep_prof_inyear_rcp26.index < 2100)]['50%'].mean()
#183.9453893599399
glue_first_jday_hypoxic_deep_prof_inyear_rcp60[(2069 < glue_first_jday_hypoxic_deep_prof_inyear_rcp60.index) & (glue_first_jday_hypoxic_deep_prof_inyear_rcp60.index < 2100)]['50%'].mean()
#177.46075356283157
glue_first_jday_hypoxic_deep_prof_inyear_rcp85[(2069 < glue_first_jday_hypoxic_deep_prof_inyear_rcp85.index) & (glue_first_jday_hypoxic_deep_prof_inyear_rcp85.index < 2100)]['50%'].mean()
#173.1566944259347
           



#%%anomaly 
os.chdir('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/')

import matplotlib.pyplot as plt

fig =plt.figure(figsize=(15, 10))
ax= plt.subplot(111)


ax=plt.fill_between(glue_first_jday_hypoxic_deep_prof_inyear_his[1975 < glue_first_jday_hypoxic_deep_prof_inyear_his.index].index.astype(float),
                      glue_first_jday_hypoxic_deep_prof_inyear_his[1975 < glue_first_jday_hypoxic_deep_prof_inyear_his.index]['5%'] - first_jday_hypoxic_deep_prof_inyear_ref,
                      glue_first_jday_hypoxic_deep_prof_inyear_his[1975 < glue_first_jday_hypoxic_deep_prof_inyear_his.index]['95%'] - first_jday_hypoxic_deep_prof_inyear_ref,
                      color='grey', alpha=0.2, label='His 90% CI')


ax=plt.plot(glue_first_jday_hypoxic_deep_prof_inyear_his[1975 < glue_first_jday_hypoxic_deep_prof_inyear_his.index ].index.astype(float),
            glue_first_jday_hypoxic_deep_prof_inyear_his[1975 < glue_first_jday_hypoxic_deep_prof_inyear_his.index]['50%'] - first_jday_hypoxic_deep_prof_inyear_ref,
            'k', label='His median', alpha=0.9, linewidth=3   )

ax=plt.fill_between(glue_first_jday_hypoxic_deep_prof_inyear_rcp26.index.astype(float), glue_first_jday_hypoxic_deep_prof_inyear_rcp26['5%']-first_jday_hypoxic_deep_prof_inyear_ref, glue_first_jday_hypoxic_deep_prof_inyear_rcp26['95%']-first_jday_hypoxic_deep_prof_inyear_ref, color='darkgreen', alpha=0.3 ,  label= 'RCP6.0 90% CI')
ax=plt.plot(glue_first_jday_hypoxic_deep_prof_inyear_rcp26.index.astype(float), glue_first_jday_hypoxic_deep_prof_inyear_rcp26['50%']-first_jday_hypoxic_deep_prof_inyear_ref, 'darkgreen', label='RCP6.0 median', alpha=0.9, linewidth=3  )
                      
                     
ax=plt.fill_between(glue_first_jday_hypoxic_deep_prof_inyear_rcp60.index.astype(float), glue_first_jday_hypoxic_deep_prof_inyear_rcp60['5%']-first_jday_hypoxic_deep_prof_inyear_ref, glue_first_jday_hypoxic_deep_prof_inyear_rcp60['95%']-first_jday_hypoxic_deep_prof_inyear_ref, color='yellow', alpha=0.5 ,  label= 'RCP6.0 90% CI')
ax=plt.plot(glue_first_jday_hypoxic_deep_prof_inyear_rcp60.index.astype(float), glue_first_jday_hypoxic_deep_prof_inyear_rcp60['50%']-first_jday_hypoxic_deep_prof_inyear_ref, 'yellow', label='RCP6.0 median', alpha=0.9, linewidth=3  )

ax=plt.fill_between(glue_first_jday_hypoxic_deep_prof_inyear_rcp85.index.astype(float), glue_first_jday_hypoxic_deep_prof_inyear_rcp85['5%']-first_jday_hypoxic_deep_prof_inyear_ref, glue_first_jday_hypoxic_deep_prof_inyear_rcp85['95%']-first_jday_hypoxic_deep_prof_inyear_ref, color='r', alpha=0.2 ,  label= 'RCP8.5 90% CI')
ax=plt.plot(glue_first_jday_hypoxic_deep_prof_inyear_rcp85.index.astype(float), glue_first_jday_hypoxic_deep_prof_inyear_rcp85['50%']-first_jday_hypoxic_deep_prof_inyear_ref, 'r', label='RCP8.5 median', alpha=0.9, linewidth=3  )

ax=plt.ylabel('Anomaly of deepest layer hypoxia onset [Jday]' , fontsize=26)
ax=plt.xlabel('Year' , fontsize=26)
ax=plt.yticks(fontsize= 22)
ax=plt.xticks(rotation=45 , fontsize=22)
ax=plt.legend(bbox_to_anchor=(1.1, -0.2), fontsize=22, ncol=4)  
fig.savefig("GLUE_Timeseries_first_jday_hypoxic_deepest_prof_anomaly_16combinationJaJv_ave_obs_4models_4scenarios.png",  dpi=300, bbox_inches='tight')

#%% Histogram or violn plot 

    
median_first_jday_hypoxic_deep_prof_his=glue_first_jday_hypoxic_deep_prof_inyear_his['50%']
median_first_jday_hypoxic_deep_prof_rcp26=glue_first_jday_hypoxic_deep_prof_inyear_rcp26['50%']
median_first_jday_hypoxic_deep_prof_rcp60=glue_first_jday_hypoxic_deep_prof_inyear_rcp60['50%']
median_first_jday_hypoxic_deep_prof_rcp85=glue_first_jday_hypoxic_deep_prof_inyear_rcp85['50%']  
    
# Create a DataFrame with NaN values
df_first_jday_hypoxic_deep_prof_4models =pd.concat([
    pd.Series(median_first_jday_hypoxic_deep_prof_his, name='His' ),
    pd.Series(median_first_jday_hypoxic_deep_prof_rcp26, name='RCP2.6'),
    pd.Series(median_first_jday_hypoxic_deep_prof_rcp60, name='RCP6.0' ),
    pd.Series(median_first_jday_hypoxic_deep_prof_rcp85, name='RCP8.5' )], axis=1)    
    
    

    
median_len_hypoxic_deep_prof_his=glue_len_hypoxic_deep_prof_inyear_his['50%']
median_len_hypoxic_deep_prof_rcp26=glue_len_hypoxic_deep_prof_inyear_rcp26['50%']
median_len_hypoxic_deep_prof_rcp60=glue_len_hypoxic_deep_prof_inyear_rcp60['50%']
median_len_hypoxic_deep_prof_rcp85=glue_len_hypoxic_deep_prof_inyear_rcp85['50%']  
    
# Create a DataFrame with NaN values
df_len_hypoxic_deep_prof_4models =pd.concat([
    pd.Series(median_len_hypoxic_deep_prof_his, name='His' ),
    pd.Series(median_len_hypoxic_deep_prof_rcp26, name='RCP2.6'),
    pd.Series(median_len_hypoxic_deep_prof_rcp60, name='RCP6.0' ),
    pd.Series(median_len_hypoxic_deep_prof_rcp85, name='RCP8.5' )], axis=1)    
    
    
median_last_jday_hypoxic_deep_prof_his=glue_last_jday_hypoxic_deep_prof_inyear_his['50%']
median_last_jday_hypoxic_deep_prof_rcp26=glue_last_jday_hypoxic_deep_prof_inyear_rcp26['50%']
median_last_jday_hypoxic_deep_prof_rcp60=glue_last_jday_hypoxic_deep_prof_inyear_rcp60['50%']
median_last_jday_hypoxic_deep_prof_rcp85=glue_last_jday_hypoxic_deep_prof_inyear_rcp85['50%']  
    
# Create a DataFrame with NaN values
df_last_jday_hypoxic_deep_prof_4models =pd.concat([
    pd.Series(median_last_jday_hypoxic_deep_prof_his, name='His' ),
    pd.Series(median_last_jday_hypoxic_deep_prof_rcp26, name='RCP2.6'),
    pd.Series(median_last_jday_hypoxic_deep_prof_rcp60, name='RCP6.0' ),
    pd.Series(median_last_jday_hypoxic_deep_prof_rcp85, name='RCP8.5' )], axis=1)    
    
    
    


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
sns.violinplot(ax=axes[0], data=df_first_jday_hypoxic_deep_prof_4models, palette=custom_palette)
axes[0].set_ylabel('Deepest layer hypoxia onset [Jday]')

#axes[0].set_ylim(60, 210)  # Set the y-axis limits
axes[0].set_yticks(range(120, 230, 30))  # Set the y-axis ticks at intervals of 20



plt.subplots_adjust(wspace=0.3)
sns.violinplot(ax=axes[1], data=df_len_hypoxic_deep_prof_4models, palette=custom_palette)
axes[1].set_ylabel('Deepest layer hypoxia duration [day]')
axes[1].set_yticks(range(0, 150, 30))  # Set the y-axis ticks at intervals of 20



#sns.violinplot(ax=axes[2], data=df_last_jday_hypoxic_deep_prof_4models, palette=custom_palette)
#axes[2].set_ylabel('Last day of deep hypoxia [Jday]')
#axes[2].set_yticks(range(180, 300, 30))  # Set the y-axis ticks at intervals of 20



plt.savefig("allsenarios_4models_median_first_len_of_deep_hypoxia.png", dpi=300)







#%% averaging over whole scenarios value 
np.mean(glue_len_hypoxic_deep_prof_inyear_his['50%'])#49.51443360571123
np.mean(glue_len_hypoxic_deep_prof_inyear_rcp26['50%'])#63.85309627518068
np.mean(glue_len_hypoxic_deep_prof_inyear_rcp60['50%'])#66.37516667473243
np.mean(glue_len_hypoxic_deep_prof_inyear_rcp85['50%'])#71.56247383643593


#%%hypoxic_duration 30 yerars from each scenarios compare 



#anomaly 
# baseline [1976-2005]
glue_base_len_hypoxic_deep_prof_his=glue_len_hypoxic_deep_prof_inyear_his[1975 < glue_len_hypoxic_deep_prof_inyear_his.index]['50%']
len_hypoxic_deep_prof_ref=np.mean(glue_base_len_hypoxic_deep_prof_his)
#50.426956555924754


#near future [2030-2059]

glue_near_future_len_hypoxic_deep_prof_rcp26=glue_len_hypoxic_deep_prof_inyear_rcp26[(2029 < glue_len_hypoxic_deep_prof_inyear_rcp26.index) & (glue_len_hypoxic_deep_prof_inyear_rcp26.index < 2060)]['50%']
np.mean(glue_near_future_len_hypoxic_deep_prof_rcp26)
#64.89917450065333
glue_near_future_len_hypoxic_deep_prof_rcp60=glue_len_hypoxic_deep_prof_inyear_rcp60[(2029 < glue_len_hypoxic_deep_prof_inyear_rcp60.index) & (glue_len_hypoxic_deep_prof_inyear_rcp60.index < 2060)]['50%']
np.mean(glue_near_future_len_hypoxic_deep_prof_rcp60)
#63.12307950184921
glue_near_future_len_hypoxic_deep_prof_rcp85=glue_len_hypoxic_deep_prof_inyear_rcp85[(2029 < glue_len_hypoxic_deep_prof_inyear_rcp85.index) & (glue_len_hypoxic_deep_prof_inyear_rcp85.index < 2060)]['50%']
np.mean(glue_near_future_len_hypoxic_deep_prof_rcp85)
# 67.03709616532731

 
#Distant future [2070-2099]

glue_distant_future_len_hypoxic_deep_prof_rcp26=glue_len_hypoxic_deep_prof_inyear_rcp26[(2069 < glue_len_hypoxic_deep_prof_inyear_rcp26.index) & (glue_len_hypoxic_deep_prof_inyear_rcp26.index < 2100)]['50%']
np.mean(glue_distant_future_len_hypoxic_deep_prof_rcp26)
#65.23161913671755
glue_distant_future_len_hypoxic_deep_prof_rcp60=glue_len_hypoxic_deep_prof_inyear_rcp60[(2069 < glue_len_hypoxic_deep_prof_inyear_rcp60.index) & (glue_len_hypoxic_deep_prof_inyear_rcp60.index< 2100)]['50%']
np.mean(glue_distant_future_len_hypoxic_deep_prof_rcp60)
#74.39034590789441
glue_distant_future_len_hypoxic_deep_prof_rcp85=glue_len_hypoxic_deep_prof_inyear_rcp85[(2069 < glue_len_hypoxic_deep_prof_inyear_rcp85.index) & (glue_len_hypoxic_deep_prof_inyear_rcp85.index < 2100)]['50%']
np.mean(glue_distant_future_len_hypoxic_deep_prof_rcp85)
#84.76007667514622
   


###====over 30 years in his and each RCPs 

# baseline [1976-2005]
autocorr_MK_org_modif_sens_slope_test(glue_base_len_hypoxic_deep_prof_his)
(0.04337619776501505,
 'positively autocorrelated',
 'increasing',
 0.02012421864894698,
 0.3181818181818182,
 45.89126503609009)

#near future [2030-2059]


autocorr_MK_org_modif_sens_slope_test(glue_near_future_len_hypoxic_deep_prof_rcp26)
(0.027618939201601793,
 'positively autocorrelated',
 'increasing',
 0.047392543075289506,
 0.3333333333333333,
 57.45012639334974)


autocorr_MK_org_modif_sens_slope_test(glue_near_future_len_hypoxic_deep_prof_rcp60)
(0.008180265800395324,
 'positively autocorrelated',
 'increasing',
 0.01976054611693745,
 0.25733996373491125,
 60.268570525843785)

autocorr_MK_org_modif_sens_slope_test(glue_near_future_len_hypoxic_deep_prof_rcp85)
(0.021391840742548015,
 'positively autocorrelated',
 'increasing',
 0.011269371241672266,
 0.4241242383677651,
 59.36222229731422)


#Distant future [2070-2099]


autocorr_MK_org_modif_sens_slope_test(glue_distant_future_len_hypoxic_deep_prof_rcp26)
(0.02708647582281628,
 'positively autocorrelated',
 'no trend',
 0.2494742100515963,
 0,
 0)
autocorr_MK_org_modif_sens_slope_test(glue_distant_future_len_hypoxic_deep_prof_rcp60)
(0.009719855626201212,
 'positively autocorrelated',
 'no trend',
 0.07807391867668612,
 0,
 0)
autocorr_MK_org_modif_sens_slope_test(glue_distant_future_len_hypoxic_deep_prof_rcp85)
(0.017914607860126115,
 'positively autocorrelated',
 'increasing',
 0.004538590466058201,
 0.49391641333034964,
 77.121671733393)


#%% Trendlines over whole periods:
# no trend in his but increasing trendlines of all rcps 
# for length of deep hypoxia    
    
# his     
  
autocorr_MK_org_modif_sens_slope_test(glue_len_hypoxic_deep_prof_inyear_his['50%'])
"""
(0.041495273439350104,
 'positively autocorrelated',
 'no trend',
 0.9903490365040264,
 0,
 0)
"""
#rcp26
autocorr_MK_org_modif_sens_slope_test(glue_len_hypoxic_deep_prof_inyear_rcp26['50%'])
"""
(0.02575820464703041,
 'positively autocorrelated',
 'increasing',
 0.0011787420420490413,
 0.08314311753992942,
 58.91730476107636)
"""

#rcp60
autocorr_MK_org_modif_sens_slope_test(glue_len_hypoxic_deep_prof_inyear_rcp60['50%'])
"""
(0.011474459320206614,
 'positively autocorrelated',
 'increasing',
 0.0,
 0.22639579555719921,
 55.72874610781281)
"""

#rcp85
autocorr_MK_org_modif_sens_slope_test(glue_len_hypoxic_deep_prof_inyear_rcp85['50%'])
"""
(0.022947456730982405,
 'positively autocorrelated',
 'increasing',
 0.0,
 0.4,
 51.9)
"""





#%% 80 years from 2020 for len_hypoxic_deep_prof


glue_80years_len_hypoxic_deep_prof_inyear_rcp26=glue_len_hypoxic_deep_prof_inyear_rcp26[2019 < glue_len_hypoxic_deep_prof_inyear_rcp26.index]

glue_80years_len_hypoxic_deep_prof_inyear_rcp60=glue_len_hypoxic_deep_prof_inyear_rcp60[2019 < glue_len_hypoxic_deep_prof_inyear_rcp60.index]


glue_80years_len_hypoxic_deep_prof_inyear_rcp85=glue_len_hypoxic_deep_prof_inyear_rcp85[2019 < glue_len_hypoxic_deep_prof_inyear_rcp85.index]


#============= mean of first 10 yaers over 80 years 

#rcp2.6
np.mean(glue_80years_len_hypoxic_deep_prof_inyear_rcp26[glue_80years_len_hypoxic_deep_prof_inyear_rcp26.index<2030]['50%'])
64.00540446849081

#rcp6.0
np.mean(glue_80years_len_hypoxic_deep_prof_inyear_rcp60[glue_80years_len_hypoxic_deep_prof_inyear_rcp60.index<2030]['50%'])
61.17161322221087

#rcp8.5
np.mean(glue_80years_len_hypoxic_deep_prof_inyear_rcp85[glue_80years_len_hypoxic_deep_prof_inyear_rcp85.index<2030]['50%'])
62.16846737913481

#============== mean of last 10 yaers over 80 years 

#rcp2.6
np.mean(glue_80years_len_hypoxic_deep_prof_inyear_rcp26[glue_80years_len_hypoxic_deep_prof_inyear_rcp26.index>2089]['50%'])
66.35516831222967

#rcp6.0
np.mean(glue_80years_len_hypoxic_deep_prof_inyear_rcp60[glue_80years_len_hypoxic_deep_prof_inyear_rcp60.index>2089]['50%'])
75.47078110413585

#rcp8.5
np.mean(glue_80years_len_hypoxic_deep_prof_inyear_rcp85[glue_80years_len_hypoxic_deep_prof_inyear_rcp85.index>2089]['50%'])
92.87410700278302

#=========== trendline # Over the 80 years


autocorr_MK_org_modif_sens_slope_test(glue_80years_len_hypoxic_deep_prof_inyear_rcp26['50%'])
(0.02670389120577994,
 'positively autocorrelated',
 'no trend',
 0.15756843681446875,
 0,
 0)

autocorr_MK_org_modif_sens_slope_test(glue_80years_len_hypoxic_deep_prof_inyear_rcp60['50%'])
(0.009343345746993786,
 'positively autocorrelated',
 'increasing',
 1.509903313490213e-14,
 0.24743459035970938,
 58.03699767818073)

autocorr_MK_org_modif_sens_slope_test(glue_80years_len_hypoxic_deep_prof_inyear_rcp85['50%'])
(0.018535973857928566,
 'positively autocorrelated',
 'increasing',
 6.661338147750939e-16,
 0.40787435138297223,
 56.928456426371255)


#%%80 years trendlines plots for len 

#%% averaging over whole scenarios value for first hypoxia deep profile 

np.mean(glue_first_jday_hypoxic_deep_prof_inyear_his['50%'])#191.55433346615138
np.mean(glue_first_jday_hypoxic_deep_prof_inyear_rcp26['50%'])#184.84279062641144
np.mean(glue_first_jday_hypoxic_deep_prof_inyear_rcp60['50%'])#182.5930386669312
np.mean(glue_first_jday_hypoxic_deep_prof_inyear_rcp85['50%'])#179.6173593987038



#%%hypoxic_duration 30 yerars from each scenarios compare 



#anomaly 
# baseline [1976-2005]
glue_base_first_jday_hypoxic_deep_prof_his=glue_first_jday_hypoxic_deep_prof_inyear_his[1975 < glue_first_jday_hypoxic_deep_prof_inyear_his.index]['50%']
len_hypoxic_deep_prof_ref=np.mean(glue_base_first_jday_hypoxic_deep_prof_his)
#194.35386565698317


#near future [2030-2059]

glue_near_future_first_jday_hypoxic_deep_prof_rcp26=glue_first_jday_hypoxic_deep_prof_inyear_rcp26[(2029 < glue_first_jday_hypoxic_deep_prof_inyear_rcp26.index) & (glue_first_jday_hypoxic_deep_prof_inyear_rcp26.index < 2060)]['50%']
np.mean(glue_near_future_first_jday_hypoxic_deep_prof_rcp26)
#184.33631722334215
glue_near_future_first_jday_hypoxic_deep_prof_rcp60=glue_first_jday_hypoxic_deep_prof_inyear_rcp60[(2029 < glue_first_jday_hypoxic_deep_prof_inyear_rcp60.index) & (glue_first_jday_hypoxic_deep_prof_inyear_rcp60.index < 2060)]['50%']
np.mean(glue_near_future_first_jday_hypoxic_deep_prof_rcp60)
#183.88780716825565
glue_near_future_first_jday_hypoxic_deep_prof_rcp85=glue_first_jday_hypoxic_deep_prof_inyear_rcp85[(2029 < glue_first_jday_hypoxic_deep_prof_inyear_rcp85.index) & (glue_first_jday_hypoxic_deep_prof_inyear_rcp85.index < 2060)]['50%']
np.mean(glue_near_future_first_jday_hypoxic_deep_prof_rcp85)
#181.86560301942978

 
#Distant future [2070-2099]

glue_distant_future_first_jday_hypoxic_deep_prof_rcp26=glue_first_jday_hypoxic_deep_prof_inyear_rcp26[(2069 < glue_first_jday_hypoxic_deep_prof_inyear_rcp26.index) & (glue_first_jday_hypoxic_deep_prof_inyear_rcp26.index < 2100)]['50%']
np.mean(glue_distant_future_first_jday_hypoxic_deep_prof_rcp26)
#183.9453893599399
glue_distant_future_first_jday_hypoxic_deep_prof_rcp60=glue_first_jday_hypoxic_deep_prof_inyear_rcp60[(2069 < glue_first_jday_hypoxic_deep_prof_inyear_rcp60.index) & (glue_first_jday_hypoxic_deep_prof_inyear_rcp60.index< 2100)]['50%']
np.mean(glue_distant_future_first_jday_hypoxic_deep_prof_rcp60)
#177.46075356283157
glue_distant_future_first_jday_hypoxic_deep_prof_rcp85=glue_first_jday_hypoxic_deep_prof_inyear_rcp85[(2069 < glue_first_jday_hypoxic_deep_prof_inyear_rcp85.index) & (glue_first_jday_hypoxic_deep_prof_inyear_rcp85.index < 2100)]['50%']
np.mean(glue_distant_future_first_jday_hypoxic_deep_prof_rcp85)
#173.1566944259347
   


###====over 30 years in his and each RCPs 

# baseline [1976-2005]
autocorr_MK_org_modif_sens_slope_test(glue_base_first_jday_hypoxic_deep_prof_his)
(0.0011385710633231058,
 'positively autocorrelated',
 'no trend',
 0.4343750461431495,
 0,
 0)
#near future [2030-2059]


autocorr_MK_org_modif_sens_slope_test(glue_near_future_first_jday_hypoxic_deep_prof_rcp26)
(0.003038640183190806,
 'positively autocorrelated',
 'no trend',
 0.42134823269748845,
 0,
 0)

autocorr_MK_org_modif_sens_slope_test(glue_near_future_first_jday_hypoxic_deep_prof_rcp60)
(0.0006910298022606175,
 'positively autocorrelated',
 'no trend',
 0.19804143879624414,
 0,
 0)

autocorr_MK_org_modif_sens_slope_test(glue_near_future_first_jday_hypoxic_deep_prof_rcp85)
 
(0.0009369806258599652,
 'positively autocorrelated',
 'no trend',
 0.10751710550463645,
 0,
 0)


#Distant future [2070-2099]


autocorr_MK_org_modif_sens_slope_test(glue_distant_future_first_jday_hypoxic_deep_prof_rcp26)
(0.003025735226617081,
 'positively autocorrelated',
 'decreasing',
 0.04681335544290666,
 -0.23076923076923078,
 187.84615384615384)


autocorr_MK_org_modif_sens_slope_test(glue_distant_future_first_jday_hypoxic_deep_prof_rcp60)
(0.0030729383285258687,
 'positively autocorrelated',
 'no trend',
 0.7068268843863703,
 0,
 0)


autocorr_MK_org_modif_sens_slope_test(glue_distant_future_first_jday_hypoxic_deep_prof_rcp85)
(0.0033502329685755313,
 'positively autocorrelated',
 'decreasing',
 0.009548461874705705,
 -0.2857142857142857,
 178.8401249678566)



#%% Trendlines over whole periods:
# no trend in his but decreasing trendlines of 6.0 and 8.5 rcps 
# for first jday of deep hypoxia    
    
# his     
  
autocorr_MK_org_modif_sens_slope_test(glue_first_jday_hypoxic_deep_prof_inyear_his['50%'])
"""
(0.00260843786896304,
 'positively autocorrelated',
 'increasing',
 0.003860229020203887,
 0.03175701435492905,
 190.19016547158463)
"""
#rcp26
autocorr_MK_org_modif_sens_slope_test(glue_first_jday_hypoxic_deep_prof_inyear_rcp26['50%'])
"""
(0.00260843786896304,
 'positively autocorrelated',
 'increasing',
 0.003860229020203887,
 0.03175701435492905,
 190.19016547158463)
"""

#rcp60
autocorr_MK_org_modif_sens_slope_test(glue_first_jday_hypoxic_deep_prof_inyear_rcp60['50%'])
"""
(0.001618083072342559,
 'positively autocorrelated',
 'decreasing',
 6.186162693211372e-13,
 -0.1349801943604163,
 189.27657903775935)
"""

#rcp85
autocorr_MK_org_modif_sens_slope_test(glue_first_jday_hypoxic_deep_prof_inyear_rcp85['50%'])
"""
(0.002368493110353768,
 'positively autocorrelated',
 'decreasing',
 2.795097486796294e-12,
 -0.17142857142857143,
 187.97142857142856)
"""





#%% 80 years from 2020 for first_jday_hypoxic_deep_prof


glue_80years_first_jday_hypoxic_deep_prof_inyear_rcp26=glue_first_jday_hypoxic_deep_prof_inyear_rcp26[2019 < glue_first_jday_hypoxic_deep_prof_inyear_rcp26.index]

glue_80years_first_jday_hypoxic_deep_prof_inyear_rcp60=glue_first_jday_hypoxic_deep_prof_inyear_rcp60[2019 < glue_first_jday_hypoxic_deep_prof_inyear_rcp60.index]


glue_80years_first_jday_hypoxic_deep_prof_inyear_rcp85=glue_first_jday_hypoxic_deep_prof_inyear_rcp85[2019 < glue_first_jday_hypoxic_deep_prof_inyear_rcp85.index]


#============= mean of first 10 yaers over 80 years 

#rcp2.6
np.mean(glue_80years_first_jday_hypoxic_deep_prof_inyear_rcp26[glue_80years_first_jday_hypoxic_deep_prof_inyear_rcp26.index<2030]['50%'])
183.40016633790992
#rcp6.0
np.mean(glue_80years_first_jday_hypoxic_deep_prof_inyear_rcp60[glue_80years_first_jday_hypoxic_deep_prof_inyear_rcp60.index<2030]['50%'])
187.24616736271534

#rcp8.5
np.mean(glue_80years_first_jday_hypoxic_deep_prof_inyear_rcp85[glue_80years_first_jday_hypoxic_deep_prof_inyear_rcp85.index<2030]['50%'])
181.52572706979458

#============== mean of last 10 yaers over 80 years 

#rcp2.6
np.mean(glue_80years_first_jday_hypoxic_deep_prof_inyear_rcp26[glue_80years_first_jday_hypoxic_deep_prof_inyear_rcp26.index>2089]['50%'])
182.36838029283984

#rcp6.0
np.mean(glue_80years_first_jday_hypoxic_deep_prof_inyear_rcp60[glue_80years_first_jday_hypoxic_deep_prof_inyear_rcp60.index>2089]['50%'])
176.0720050974514

#rcp8.5
np.mean(glue_80years_first_jday_hypoxic_deep_prof_inyear_rcp85[glue_80years_first_jday_hypoxic_deep_prof_inyear_rcp85.index>2089]['50%'])
166.82584278084465

#=========== trendline # Over the 80 years


autocorr_MK_org_modif_sens_slope_test(glue_80years_first_jday_hypoxic_deep_prof_inyear_rcp26['50%'])
(0.0032929705039796897,
 'positively autocorrelated',
 'no trend',
 0.14710138244716164,
 0,
 0)

autocorr_MK_org_modif_sens_slope_test(glue_80years_first_jday_hypoxic_deep_prof_inyear_rcp60['50%'])
(0.0015986107782837101,
 'positively autocorrelated',
 'decreasing',
 8.144596108650148e-13,
 -0.13712060166532367,
 187.6160882620706)

autocorr_MK_org_modif_sens_slope_test(glue_80years_first_jday_hypoxic_deep_prof_inyear_rcp85['50%'])
(0.002052706580713172,
 'positively autocorrelated',
 'decreasing',
 1.7570190191662505e-08,
 -0.15772663572092316,
 185.23020211097648)

#%%plotting 80 years of len and first jday of deep hypoxia profile  


import matplotlib.pyplot as plt
import numpy as np

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(26, 8))

# Plotting the first subplot
ax1.fill_between(glue_80years_len_hypoxic_deep_prof_inyear_rcp26.index.astype(float), glue_80years_len_hypoxic_deep_prof_inyear_rcp26['5%'], glue_80years_len_hypoxic_deep_prof_inyear_rcp26['95%'], color='darkgreen', alpha=0.3)# ,  label= 'RCP2.6 90% CI')
ax1.plot(glue_80years_len_hypoxic_deep_prof_inyear_rcp26.index.astype(float), glue_80years_len_hypoxic_deep_prof_inyear_rcp26['50%'], 'darkgreen', alpha=0.9, linewidth=3  )#, label='RCP2.6 median'

ax1.fill_between(glue_80years_len_hypoxic_deep_prof_inyear_rcp60.index.astype(float), glue_80years_len_hypoxic_deep_prof_inyear_rcp60['5%'], glue_80years_len_hypoxic_deep_prof_inyear_rcp60['95%'], color='yellow', alpha=0.5)# ,  label= 'RCP6.0 90% CI')
ax1.plot(glue_80years_len_hypoxic_deep_prof_inyear_rcp60.index.astype(float), glue_80years_len_hypoxic_deep_prof_inyear_rcp60['50%'], 'yellow', alpha=0.9, linewidth=3  )#, label='RCP6.0 median'

ax1.fill_between(glue_80years_len_hypoxic_deep_prof_inyear_rcp85.index.astype(float), glue_80years_len_hypoxic_deep_prof_inyear_rcp85['5%'], glue_80years_len_hypoxic_deep_prof_inyear_rcp85['95%'], color='r', alpha=0.2)# ,  label= 'RCP8.5 90% CI')
ax1.plot(glue_80years_len_hypoxic_deep_prof_inyear_rcp85.index.astype(float), glue_80years_len_hypoxic_deep_prof_inyear_rcp85['50%'], 'r', alpha=0.9, linewidth=3  )#, label='RCP8.5 median'

trendline_rcp60_len = autocorr_MK_org_modif_sens_slope_test(glue_80years_len_hypoxic_deep_prof_inyear_rcp60['50%'])
ax1.text(2020, 170, f'y = {trendline_rcp60_len[-2]:.3f}x + {trendline_rcp60_len[-1]:.3f}, p-value < 0.0001', color='orange', fontsize=20 )

ax1.plot(glue_80years_len_hypoxic_deep_prof_inyear_rcp60.index.astype(float),
        trendline_rcp60_len[-2] * np.arange(80) + trendline_rcp60_len[-1],
        linestyle='--', color='orange', alpha=0.9, linewidth=3)


trendline_rcp85_len = autocorr_MK_org_modif_sens_slope_test(glue_80years_len_hypoxic_deep_prof_inyear_rcp85['50%'])
ax1.text(2020, 160, f'y = {trendline_rcp85_len[-2]:.3f}x + {trendline_rcp85_len[-1]:.3f}, p-value < 0.0001', color='red', fontsize=20 )


ax1.plot(glue_80years_len_hypoxic_deep_prof_inyear_rcp85.index.astype(float),
        trendline_rcp85_len[-2] * np.arange(80) + trendline_rcp85_len[-1],
        linestyle='--', color='red', alpha=0.9, linewidth=3)# , label= 'RCP8.5 trendline')


ax1.set_ylabel('Duration of deep hypoxia [d]' , fontsize=26)
ax1.set_xlabel('Year' , fontsize=26)
ax1.tick_params(axis='both', which='major', labelsize=22)
#ax1.legend(bbox_to_anchor=(0.7, -0.2), fontsize=22)
ax1.tick_params(axis='x', rotation=45, labelsize=22)




# Plotting the second subplot
ax2.fill_between(glue_80years_first_jday_hypoxic_deep_prof_inyear_rcp26.index.astype(float), glue_80years_first_jday_hypoxic_deep_prof_inyear_rcp26['5%'], glue_80years_first_jday_hypoxic_deep_prof_inyear_rcp26['95%'], color='darkgreen', alpha=0.3 ,  label= 'RCP2.6 90% CI')
ax2.plot(glue_80years_first_jday_hypoxic_deep_prof_inyear_rcp26.index.astype(float), glue_80years_first_jday_hypoxic_deep_prof_inyear_rcp26['50%'], 'darkgreen', label='RCP2.6 median', alpha=0.9, linewidth=3  )

ax2.fill_between(glue_80years_first_jday_hypoxic_deep_prof_inyear_rcp60.index.astype(float), glue_80years_first_jday_hypoxic_deep_prof_inyear_rcp60['5%'], glue_80years_first_jday_hypoxic_deep_prof_inyear_rcp60['95%'], color='yellow', alpha=0.5 ,  label= 'RCP6.0 90% CI')
ax2.plot(glue_80years_first_jday_hypoxic_deep_prof_inyear_rcp60.index.astype(float), glue_80years_first_jday_hypoxic_deep_prof_inyear_rcp60['50%'], 'yellow', label='RCP6.0 median', alpha=0.9, linewidth=3  )

ax2.fill_between(glue_80years_first_jday_hypoxic_deep_prof_inyear_rcp85.index.astype(float), glue_80years_first_jday_hypoxic_deep_prof_inyear_rcp85['5%'], glue_80years_first_jday_hypoxic_deep_prof_inyear_rcp85['95%'], color='r', alpha=0.2 ,  label= 'RCP8.5 90% CI')
ax2.plot(glue_80years_first_jday_hypoxic_deep_prof_inyear_rcp85.index.astype(float), glue_80years_first_jday_hypoxic_deep_prof_inyear_rcp85['50%'], 'r', label='RCP8.5 median', alpha=0.9, linewidth=3  )

trendline_rcp60_first = autocorr_MK_org_modif_sens_slope_test(glue_80years_first_jday_hypoxic_deep_prof_inyear_rcp60['50%'])
ax2.text(2020, 110, f'y = {trendline_rcp60_first[-2]:.3f}x + {trendline_rcp60_first[-1]:.3f}, p-value < 0.0001', color='orange', fontsize=20 )

ax2.plot(glue_80years_first_jday_hypoxic_deep_prof_inyear_rcp60.index.astype(float),
        trendline_rcp60_first[-2] * np.arange(80) + trendline_rcp60_first[-1],
        linestyle='--', color='orange', alpha=0.9, linewidth=3, label= 'RCP6.0 trendline')

trendline_rcp85_first = autocorr_MK_org_modif_sens_slope_test(glue_80years_first_jday_hypoxic_deep_prof_inyear_rcp85['50%'])
ax2.text(2020, 100, f'y = {trendline_rcp85_first[-2]:.3f}x + {trendline_rcp85_first[-1]:.3f}, p-value < 0.0001', color='red', fontsize=20 )

ax2.plot(glue_80years_first_jday_hypoxic_deep_prof_inyear_rcp85.index.astype(float),
        trendline_rcp85_first[-2] * np.arange(80) + trendline_rcp85_first[-1],
        linestyle='--', color='red', alpha=0.9, linewidth=3 , label= 'RCP8.5 trendline')

ax2.set_ylabel('First day of deep hypoxia in year [Jd]' , fontsize=26)
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
plt.savefig('GLUE_Timeseries_deep_hypoxia_duration_80years.png', bbox_inches='tight')


#%%Seperae them 

#%%plotting 80 years of len and first jday of deep hypoxia profile  


import matplotlib.pyplot as plt
import numpy as np

fig, ax2 = plt.subplots(1, 1, figsize=(10, 8))





# Plotting the second subplot
ax2.fill_between(glue_80years_first_jday_hypoxic_deep_prof_inyear_rcp26.index.astype(float), glue_80years_first_jday_hypoxic_deep_prof_inyear_rcp26['5%'], glue_80years_first_jday_hypoxic_deep_prof_inyear_rcp26['95%'], color='darkgreen', alpha=0.3 ,  label= 'RCP2.6 90% CI')
ax2.plot(glue_80years_first_jday_hypoxic_deep_prof_inyear_rcp26.index.astype(float), glue_80years_first_jday_hypoxic_deep_prof_inyear_rcp26['50%'], 'darkgreen', label='RCP2.6 median', alpha=0.9, linewidth=3  )

ax2.fill_between(glue_80years_first_jday_hypoxic_deep_prof_inyear_rcp60.index.astype(float), glue_80years_first_jday_hypoxic_deep_prof_inyear_rcp60['5%'], glue_80years_first_jday_hypoxic_deep_prof_inyear_rcp60['95%'], color='yellow', alpha=0.5 ,  label= 'RCP6.0 90% CI')
ax2.plot(glue_80years_first_jday_hypoxic_deep_prof_inyear_rcp60.index.astype(float), glue_80years_first_jday_hypoxic_deep_prof_inyear_rcp60['50%'], 'yellow', label='RCP6.0 median', alpha=0.9, linewidth=3  )

ax2.fill_between(glue_80years_first_jday_hypoxic_deep_prof_inyear_rcp85.index.astype(float), glue_80years_first_jday_hypoxic_deep_prof_inyear_rcp85['5%'], glue_80years_first_jday_hypoxic_deep_prof_inyear_rcp85['95%'], color='r', alpha=0.2 ,  label= 'RCP8.5 90% CI')
ax2.plot(glue_80years_first_jday_hypoxic_deep_prof_inyear_rcp85.index.astype(float), glue_80years_first_jday_hypoxic_deep_prof_inyear_rcp85['50%'], 'r', label='RCP8.5 median', alpha=0.9, linewidth=3  )

trendline_rcp60_first = autocorr_MK_org_modif_sens_slope_test(glue_80years_first_jday_hypoxic_deep_prof_inyear_rcp60['50%'])
ax2.text(2020, 110, f'y = {trendline_rcp60_first[-2]:.3f}x + {trendline_rcp60_first[-1]:.3f}, p-value < 0.0001', color='orange', fontsize=20 )

ax2.plot(glue_80years_first_jday_hypoxic_deep_prof_inyear_rcp60.index.astype(float),
        trendline_rcp60_first[-2] * np.arange(80) + trendline_rcp60_first[-1],
        linestyle='--', color='orange', alpha=0.9, linewidth=3, label= 'RCP6.0 trendline')

trendline_rcp85_first = autocorr_MK_org_modif_sens_slope_test(glue_80years_first_jday_hypoxic_deep_prof_inyear_rcp85['50%'])
ax2.text(2020, 100, f'y = {trendline_rcp85_first[-2]:.3f}x + {trendline_rcp85_first[-1]:.3f}, p-value < 0.0001', color='red', fontsize=20 )

ax2.plot(glue_80years_first_jday_hypoxic_deep_prof_inyear_rcp85.index.astype(float),
        trendline_rcp85_first[-2] * np.arange(80) + trendline_rcp85_first[-1],
        linestyle='--', color='red', alpha=0.9, linewidth=3 , label= 'RCP8.5 trendline')

ax2.set_ylabel('First day of deep hypoxia in year [Jd]' , fontsize=26)
ax2.set_xlabel('Year' , fontsize=26)
ax2.tick_params(axis='both', which='major', labelsize=22)
#ax2.legend(bbox_to_anchor=(0.7, -0.2), fontsize=22)
ax2.tick_params(axis='x', rotation=45, labelsize=22)

plt.subplots_adjust(wspace=0.4)
# Collecting handles and labels from both subplots

#fig.legend(handles, labels, loc='lower center', fontsize=16, ncol=3, bbox_to_anchor=(0.5, -0.2), fontsize=22)
#fig.legend( loc='lower center', ncol=3, bbox_to_anchor=(0.5, -0.2), prop={'size': 22})

plt.subplots_adjust(wspace=0.3)

# Saving the figure
plt.savefig('GLUE_Timeseries_deep_hypoxia_first_len_deep_hypoxia_80years.png', bbox_inches='tight')






#%%plotting 80 years of len and first jday of deep hypoxia profile  


import matplotlib.pyplot as plt
import numpy as np

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(26, 8))

# Plotting the first subplot
ax1.fill_between(glue_80years_len_hypoxic_deep_prof_inyear_rcp26.index.astype(float), glue_80years_len_hypoxic_deep_prof_inyear_rcp26['5%'], glue_80years_len_hypoxic_deep_prof_inyear_rcp26['95%'], color='darkgreen', alpha=0.3)# ,  label= 'RCP2.6 90% CI')
ax1.plot(glue_80years_len_hypoxic_deep_prof_inyear_rcp26.index.astype(float), glue_80years_len_hypoxic_deep_prof_inyear_rcp26['50%'], 'darkgreen', alpha=0.9, linewidth=3  )#, label='RCP2.6 median'

ax1.fill_between(glue_80years_len_hypoxic_deep_prof_inyear_rcp60.index.astype(float), glue_80years_len_hypoxic_deep_prof_inyear_rcp60['5%'], glue_80years_len_hypoxic_deep_prof_inyear_rcp60['95%'], color='yellow', alpha=0.5)# ,  label= 'RCP6.0 90% CI')
ax1.plot(glue_80years_len_hypoxic_deep_prof_inyear_rcp60.index.astype(float), glue_80years_len_hypoxic_deep_prof_inyear_rcp60['50%'], 'yellow', alpha=0.9, linewidth=3  )#, label='RCP6.0 median'

ax1.fill_between(glue_80years_len_hypoxic_deep_prof_inyear_rcp85.index.astype(float), glue_80years_len_hypoxic_deep_prof_inyear_rcp85['5%'], glue_80years_len_hypoxic_deep_prof_inyear_rcp85['95%'], color='r', alpha=0.2)# ,  label= 'RCP8.5 90% CI')
ax1.plot(glue_80years_len_hypoxic_deep_prof_inyear_rcp85.index.astype(float), glue_80years_len_hypoxic_deep_prof_inyear_rcp85['50%'], 'r', alpha=0.9, linewidth=3  )#, label='RCP8.5 median'

trendline_rcp60_len = autocorr_MK_org_modif_sens_slope_test(glue_80years_len_hypoxic_deep_prof_inyear_rcp60['50%'])
ax1.text(2020, 170, f'y = {trendline_rcp60_len[-2]:.3f}x + {trendline_rcp60_len[-1]:.3f}, p-value < 0.0001', color='orange', fontsize=20 )

ax1.plot(glue_80years_len_hypoxic_deep_prof_inyear_rcp60.index.astype(float),
        trendline_rcp60_len[-2] * np.arange(80) + trendline_rcp60_len[-1],
        linestyle='--', color='orange', alpha=0.9, linewidth=3)


trendline_rcp85_len = autocorr_MK_org_modif_sens_slope_test(glue_80years_len_hypoxic_deep_prof_inyear_rcp85['50%'])
ax1.text(2020, 160, f'y = {trendline_rcp85_len[-2]:.3f}x + {trendline_rcp85_len[-1]:.3f}, p-value < 0.0001', color='red', fontsize=20 )


ax1.plot(glue_80years_len_hypoxic_deep_prof_inyear_rcp85.index.astype(float),
        trendline_rcp85_len[-2] * np.arange(80) + trendline_rcp85_len[-1],
        linestyle='--', color='red', alpha=0.9, linewidth=3)# , label= 'RCP8.5 trendline')


ax1.set_ylabel('Duration of deep hypoxia [d]' , fontsize=26)
ax1.set_xlabel('Year' , fontsize=26)
ax1.tick_params(axis='both', which='major', labelsize=22)
#ax1.legend(bbox_to_anchor=(0.7, -0.2), fontsize=22)
ax1.tick_params(axis='x', rotation=45, labelsize=22)




# Plotting the second subplot
ax2.fill_between(glue_80years_first_jday_hypoxic_deep_prof_inyear_rcp26.index.astype(float), glue_80years_first_jday_hypoxic_deep_prof_inyear_rcp26['5%'], glue_80years_first_jday_hypoxic_deep_prof_inyear_rcp26['95%'], color='darkgreen', alpha=0.3 ,  label= 'RCP2.6 90% CI')
ax2.plot(glue_80years_first_jday_hypoxic_deep_prof_inyear_rcp26.index.astype(float), glue_80years_first_jday_hypoxic_deep_prof_inyear_rcp26['50%'], 'darkgreen', label='RCP2.6 median', alpha=0.9, linewidth=3  )

ax2.fill_between(glue_80years_first_jday_hypoxic_deep_prof_inyear_rcp60.index.astype(float), glue_80years_first_jday_hypoxic_deep_prof_inyear_rcp60['5%'], glue_80years_first_jday_hypoxic_deep_prof_inyear_rcp60['95%'], color='yellow', alpha=0.5 ,  label= 'RCP6.0 90% CI')
ax2.plot(glue_80years_first_jday_hypoxic_deep_prof_inyear_rcp60.index.astype(float), glue_80years_first_jday_hypoxic_deep_prof_inyear_rcp60['50%'], 'yellow', label='RCP6.0 median', alpha=0.9, linewidth=3  )

ax2.fill_between(glue_80years_first_jday_hypoxic_deep_prof_inyear_rcp85.index.astype(float), glue_80years_first_jday_hypoxic_deep_prof_inyear_rcp85['5%'], glue_80years_first_jday_hypoxic_deep_prof_inyear_rcp85['95%'], color='r', alpha=0.2 ,  label= 'RCP8.5 90% CI')
ax2.plot(glue_80years_first_jday_hypoxic_deep_prof_inyear_rcp85.index.astype(float), glue_80years_first_jday_hypoxic_deep_prof_inyear_rcp85['50%'], 'r', label='RCP8.5 median', alpha=0.9, linewidth=3  )

trendline_rcp60_first = autocorr_MK_org_modif_sens_slope_test(glue_80years_first_jday_hypoxic_deep_prof_inyear_rcp60['50%'])
ax2.text(2020, 110, f'y = {trendline_rcp60_first[-2]:.3f}x + {trendline_rcp60_first[-1]:.3f}, p-value < 0.0001', color='orange', fontsize=20 )

ax2.plot(glue_80years_first_jday_hypoxic_deep_prof_inyear_rcp60.index.astype(float),
        trendline_rcp60_first[-2] * np.arange(80) + trendline_rcp60_first[-1],
        linestyle='--', color='orange', alpha=0.9, linewidth=3, label= 'RCP6.0 trendline')

trendline_rcp85_first = autocorr_MK_org_modif_sens_slope_test(glue_80years_first_jday_hypoxic_deep_prof_inyear_rcp85['50%'])
ax2.text(2020, 100, f'y = {trendline_rcp85_first[-2]:.3f}x + {trendline_rcp85_first[-1]:.3f}, p-value < 0.0001', color='red', fontsize=20 )

ax2.plot(glue_80years_first_jday_hypoxic_deep_prof_inyear_rcp85.index.astype(float),
        trendline_rcp85_first[-2] * np.arange(80) + trendline_rcp85_first[-1],
        linestyle='--', color='red', alpha=0.9, linewidth=3 , label= 'RCP8.5 trendline')

ax2.set_ylabel('First day of deep hypoxia in year [Jd]' , fontsize=26)
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
plt.savefig('GLUE_Timeseries_deep_hypoxia_duration_first_len_deep_hypoxia_80years.png', bbox_inches='tight')














#%% anormally plot of first Jda and length of deep hypoxia profile 


import os
import matplotlib.pyplot as plt

# Change directory
os.chdir('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/')

# Create a figure and axes for subplots
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(25, 10))

# Plotting the first subplot
ax1 = axes[0]
ax1.fill_between(glue_first_jday_hypoxic_deep_prof_inyear_his[(1975 < glue_first_jday_hypoxic_deep_prof_inyear_his.index)].index.astype(float),
                 glue_first_jday_hypoxic_deep_prof_inyear_his[(1975 < glue_first_jday_hypoxic_deep_prof_inyear_his.index)]['5%'] - first_jday_hypoxic_deep_prof_inyear_ref,
                 glue_first_jday_hypoxic_deep_prof_inyear_his[(1975 < glue_first_jday_hypoxic_deep_prof_inyear_his.index)]['95%'] - first_jday_hypoxic_deep_prof_inyear_ref,
                 color='grey', alpha=0.2, label='His 90% CI')

ax1.plot(glue_first_jday_hypoxic_deep_prof_inyear_his[(1975 < glue_first_jday_hypoxic_deep_prof_inyear_his.index)].index.astype(float),
         glue_first_jday_hypoxic_deep_prof_inyear_his[(1975 < glue_first_jday_hypoxic_deep_prof_inyear_his.index)]['50%'] - first_jday_hypoxic_deep_prof_inyear_ref,
         'k', label='His median', alpha=0.9, linewidth=3)

ax1.fill_between(glue_first_jday_hypoxic_deep_prof_inyear_rcp26.index.astype(float), glue_first_jday_hypoxic_deep_prof_inyear_rcp26['5%'] - first_jday_hypoxic_deep_prof_inyear_ref, glue_first_jday_hypoxic_deep_prof_inyear_rcp26['95%'] - first_jday_hypoxic_deep_prof_inyear_ref, color='darkgreen', alpha=0.3, label='RCP6.0 90% CI')

ax1.plot(glue_first_jday_hypoxic_deep_prof_inyear_rcp26.index.astype(float), glue_first_jday_hypoxic_deep_prof_inyear_rcp26['50%'] - first_jday_hypoxic_deep_prof_inyear_ref, 'darkgreen', label='RCP6.0 median', alpha=0.9, linewidth=3)

ax1.fill_between(glue_first_jday_hypoxic_deep_prof_inyear_rcp60.index.astype(float), glue_first_jday_hypoxic_deep_prof_inyear_rcp60['5%'] - first_jday_hypoxic_deep_prof_inyear_ref, glue_first_jday_hypoxic_deep_prof_inyear_rcp60['95%'] - first_jday_hypoxic_deep_prof_inyear_ref, color='yellow', alpha=0.5, label='RCP6.0 90% CI')

ax1.plot(glue_first_jday_hypoxic_deep_prof_inyear_rcp60.index.astype(float), glue_first_jday_hypoxic_deep_prof_inyear_rcp60['50%'] - first_jday_hypoxic_deep_prof_inyear_ref, 'yellow', label='RCP6.0 median', alpha=0.9, linewidth=3)

ax1.fill_between(glue_first_jday_hypoxic_deep_prof_inyear_rcp85.index.astype(float), glue_first_jday_hypoxic_deep_prof_inyear_rcp85['5%'] - first_jday_hypoxic_deep_prof_inyear_ref, glue_first_jday_hypoxic_deep_prof_inyear_rcp85['95%'] - first_jday_hypoxic_deep_prof_inyear_ref, color='r', alpha=0.2, label='RCP8.5 90% CI')

ax1.plot(glue_first_jday_hypoxic_deep_prof_inyear_rcp85.index.astype(float), glue_first_jday_hypoxic_deep_prof_inyear_rcp85['50%'] - first_jday_hypoxic_deep_prof_inyear_ref, 'r', label='RCP8.5 median', alpha=0.9, linewidth=3)

ax1.set_ylabel('Anomaly of first day of deep hypoxia [Jd]', fontsize=26)
ax1.set_xlabel('Year', fontsize=26)
ax1.tick_params(axis='y', labelsize=22)
ax1.tick_params(axis='x', rotation=45, labelsize=22)

# Plotting the second subplot
ax2 = axes[1]
ax2.fill_between(glue_len_hypoxic_deep_prof_inyear_his[(1975 < glue_len_hypoxic_deep_prof_inyear_his.index)].index.astype(float),
                 glue_len_hypoxic_deep_prof_inyear_his[(1975 < glue_len_hypoxic_deep_prof_inyear_his.index)]['5%'] - len_hypoxic_deep_prof_inyear_ref,
                 glue_len_hypoxic_deep_prof_inyear_his[(1975 < glue_len_hypoxic_deep_prof_inyear_his.index)]['95%'] - len_hypoxic_deep_prof_inyear_ref,
                 color='grey', alpha=0.2)#, label='His 90% CI')

ax2.plot(glue_len_hypoxic_deep_prof_inyear_his[(1975 < glue_len_hypoxic_deep_prof_inyear_his.index)].index.astype(float),
          glue_len_hypoxic_deep_prof_inyear_his[(1975 < glue_len_hypoxic_deep_prof_inyear_his.index)]['50%'] - len_hypoxic_deep_prof_inyear_ref,
          'k', alpha=0.9, linewidth=3)

ax2.fill_between(glue_len_hypoxic_deep_prof_inyear_rcp26.index.astype(float), glue_len_hypoxic_deep_prof_inyear_rcp26['5%'] - len_hypoxic_deep_prof_inyear_ref, glue_len_hypoxic_deep_prof_inyear_rcp26['95%'] - len_hypoxic_deep_prof_inyear_ref, color='darkgreen', alpha=0.3)#, label='RCP6.0 90% CI')

ax2.plot(glue_len_hypoxic_deep_prof_inyear_rcp26.index.astype(float), glue_len_hypoxic_deep_prof_inyear_rcp26['50%'] - len_hypoxic_deep_prof_inyear_ref, 'darkgreen',alpha=0.9, linewidth=3)

ax2.fill_between(glue_len_hypoxic_deep_prof_inyear_rcp60.index.astype(float), glue_len_hypoxic_deep_prof_inyear_rcp60['5%'] - len_hypoxic_deep_prof_inyear_ref, glue_len_hypoxic_deep_prof_inyear_rcp60['95%'] - len_hypoxic_deep_prof_inyear_ref, color='yellow', alpha=0.5)#, label='RCP6.0 90% CI')

ax2.plot(glue_len_hypoxic_deep_prof_inyear_rcp60.index.astype(float), glue_len_hypoxic_deep_prof_inyear_rcp60['50%'] - len_hypoxic_deep_prof_inyear_ref, 'yellow', alpha=0.9, linewidth=3)

ax2.fill_between(glue_len_hypoxic_deep_prof_inyear_rcp85.index.astype(float), glue_len_hypoxic_deep_prof_inyear_rcp85['5%'] - len_hypoxic_deep_prof_inyear_ref, glue_len_hypoxic_deep_prof_inyear_rcp85['95%'] - len_hypoxic_deep_prof_inyear_ref, color='r', alpha=0.2)#, label='RCP8.5 90% CI')

ax2.plot(glue_len_hypoxic_deep_prof_inyear_rcp85.index.astype(float), glue_len_hypoxic_deep_prof_inyear_rcp85['50%'] - len_hypoxic_deep_prof_inyear_ref, 'r',  alpha=0.9, linewidth=3)

ax2.set_ylabel('Anomaly of deep hypoxia duration [d]', fontsize=26)
ax2.set_xlabel('Year', fontsize=26)
ax2.tick_params(axis='y', labelsize=22)
ax2.tick_params(axis='x', rotation=45, labelsize=22)

# Legend for both subplots
fig.legend(loc='upper center', bbox_to_anchor=(0.5, -0.01), shadow=True, ncol=4, fontsize=22)

# Save the figure
fig.savefig("Anomaly_first_jday_duration_deep_hypoxia_profile.png", dpi=300, bbox_inches='tight')
plt.show()



#%% value plot of first Jda and length of deep hypoxia profile 


import os
import matplotlib.pyplot as plt

# Change directory
os.chdir('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/')

# Create a figure and axes for subplots
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(25, 10))

# Plotting the first subplot
ax1 = axes[0]
ax1.fill_between(glue_first_jday_hypoxic_deep_prof_inyear_his.index.astype(float),
                 glue_first_jday_hypoxic_deep_prof_inyear_his['5%'],
                 glue_first_jday_hypoxic_deep_prof_inyear_his['95%'],
                 color='grey', alpha=0.2, label='His 90% CI')

ax1.plot(glue_first_jday_hypoxic_deep_prof_inyear_his.index.astype(float),
         glue_first_jday_hypoxic_deep_prof_inyear_his['50%'],
         'k', label='His median', alpha=0.9, linewidth=3)

ax1.fill_between(glue_first_jday_hypoxic_deep_prof_inyear_rcp26.index.astype(float), glue_first_jday_hypoxic_deep_prof_inyear_rcp26['5%'], glue_first_jday_hypoxic_deep_prof_inyear_rcp26['95%'], color='darkgreen', alpha=0.3, label='RCP6.0 90% CI')

ax1.plot(glue_first_jday_hypoxic_deep_prof_inyear_rcp26.index.astype(float), glue_first_jday_hypoxic_deep_prof_inyear_rcp26['50%'], 'darkgreen', label='RCP6.0 median', alpha=0.9, linewidth=3)

ax1.fill_between(glue_first_jday_hypoxic_deep_prof_inyear_rcp60.index.astype(float), glue_first_jday_hypoxic_deep_prof_inyear_rcp60['5%'], glue_first_jday_hypoxic_deep_prof_inyear_rcp60['95%'], color='yellow', alpha=0.5, label='RCP6.0 90% CI')

ax1.plot(glue_first_jday_hypoxic_deep_prof_inyear_rcp60.index.astype(float), glue_first_jday_hypoxic_deep_prof_inyear_rcp60['50%'], 'yellow', label='RCP6.0 median', alpha=0.9, linewidth=3)

ax1.fill_between(glue_first_jday_hypoxic_deep_prof_inyear_rcp85.index.astype(float), glue_first_jday_hypoxic_deep_prof_inyear_rcp85['5%'], glue_first_jday_hypoxic_deep_prof_inyear_rcp85['95%'], color='r', alpha=0.2, label='RCP8.5 90% CI')

ax1.plot(glue_first_jday_hypoxic_deep_prof_inyear_rcp85.index.astype(float), glue_first_jday_hypoxic_deep_prof_inyear_rcp85['50%'], 'r', label='RCP8.5 median', alpha=0.9, linewidth=3)

ax1.set_ylabel('First day of deep hypoxia [Jd]', fontsize=26)
ax1.set_xlabel('Year', fontsize=26)
ax1.tick_params(axis='y', labelsize=22)
ax1.tick_params(axis='x', rotation=45, labelsize=22)

# Plotting the second subplot
ax2 = axes[1]
ax2.fill_between(glue_len_hypoxic_deep_prof_inyear_his.index.astype(float),
                 glue_len_hypoxic_deep_prof_inyear_his['5%'] ,
                 glue_len_hypoxic_deep_prof_inyear_his['95%'] ,
                 color='grey', alpha=0.2)#, label='His 90% CI')

ax2.plot(glue_len_hypoxic_deep_prof_inyear_his.index.astype(float),
          glue_len_hypoxic_deep_prof_inyear_his['50%'] ,
          'k', alpha=0.9, linewidth=3)

ax2.fill_between(glue_len_hypoxic_deep_prof_inyear_rcp26.index.astype(float), glue_len_hypoxic_deep_prof_inyear_rcp26['5%'] , glue_len_hypoxic_deep_prof_inyear_rcp26['95%'] , color='darkgreen', alpha=0.3)#, label='RCP6.0 90% CI')

ax2.plot(glue_len_hypoxic_deep_prof_inyear_rcp26.index.astype(float), glue_len_hypoxic_deep_prof_inyear_rcp26['50%'] , 'darkgreen',alpha=0.9, linewidth=3)

ax2.fill_between(glue_len_hypoxic_deep_prof_inyear_rcp60.index.astype(float), glue_len_hypoxic_deep_prof_inyear_rcp60['5%'] , glue_len_hypoxic_deep_prof_inyear_rcp60['95%'] , color='yellow', alpha=0.5)#, label='RCP6.0 90% CI')

ax2.plot(glue_len_hypoxic_deep_prof_inyear_rcp60.index.astype(float), glue_len_hypoxic_deep_prof_inyear_rcp60['50%'] , 'yellow', alpha=0.9, linewidth=3)

ax2.fill_between(glue_len_hypoxic_deep_prof_inyear_rcp85.index.astype(float), glue_len_hypoxic_deep_prof_inyear_rcp85['5%'] , glue_len_hypoxic_deep_prof_inyear_rcp85['95%'] , color='r', alpha=0.2)#, label='RCP8.5 90% CI')

ax2.plot(glue_len_hypoxic_deep_prof_inyear_rcp85.index.astype(float), glue_len_hypoxic_deep_prof_inyear_rcp85['50%'] , 'r',  alpha=0.9, linewidth=3)

ax2.set_ylabel('Deep hypoxia duration [d]', fontsize=26)
ax2.set_xlabel('Year', fontsize=26)
ax2.tick_params(axis='y', labelsize=22)
ax2.tick_params(axis='x', rotation=45, labelsize=22)

# Legend for both subplots
fig.legend(loc='upper center', bbox_to_anchor=(0.5, -0.01), shadow=True, ncol=4, fontsize=22)

# Save the figure
fig.savefig("First_jday_duration_deep_hypoxia_profile.png", dpi=300, bbox_inches='tight')
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
ax1.fill_between(glue_first_jday_hypoxic_deep_prof_inyear_his.index.astype(float),
                 glue_first_jday_hypoxic_deep_prof_inyear_his['5%'],
                 glue_first_jday_hypoxic_deep_prof_inyear_his['95%'],
                 color='grey', alpha=0.2, label='His 90% CI')

ax1.plot(glue_first_jday_hypoxic_deep_prof_inyear_his.index.astype(float),
         glue_first_jday_hypoxic_deep_prof_inyear_his['50%'],
         'k', label='His median', alpha=0.9, linewidth=3)

ax1.fill_between(glue_first_jday_hypoxic_deep_prof_inyear_rcp26.index.astype(float), glue_first_jday_hypoxic_deep_prof_inyear_rcp26['5%'], glue_first_jday_hypoxic_deep_prof_inyear_rcp26['95%'], color='darkgreen', alpha=0.3, label='RCP6.0 90% CI')

ax1.plot(glue_first_jday_hypoxic_deep_prof_inyear_rcp26.index.astype(float), glue_first_jday_hypoxic_deep_prof_inyear_rcp26['50%'], 'darkgreen', label='RCP6.0 median', alpha=0.9, linewidth=3)

ax1.fill_between(glue_first_jday_hypoxic_deep_prof_inyear_rcp60.index.astype(float), glue_first_jday_hypoxic_deep_prof_inyear_rcp60['5%'], glue_first_jday_hypoxic_deep_prof_inyear_rcp60['95%'], color='yellow', alpha=0.5, label='RCP6.0 90% CI')

ax1.plot(glue_first_jday_hypoxic_deep_prof_inyear_rcp60.index.astype(float), glue_first_jday_hypoxic_deep_prof_inyear_rcp60['50%'], 'yellow', label='RCP6.0 median', alpha=0.9, linewidth=3)

ax1.fill_between(glue_first_jday_hypoxic_deep_prof_inyear_rcp85.index.astype(float), glue_first_jday_hypoxic_deep_prof_inyear_rcp85['5%'], glue_first_jday_hypoxic_deep_prof_inyear_rcp85['95%'], color='r', alpha=0.2, label='RCP8.5 90% CI')

ax1.plot(glue_first_jday_hypoxic_deep_prof_inyear_rcp85.index.astype(float), glue_first_jday_hypoxic_deep_prof_inyear_rcp85['50%'], 'r', label='RCP8.5 median', alpha=0.9, linewidth=3)



trendline_his=autocorr_MK_org_modif_sens_slope_test(glue_first_jday_hypoxic_deep_prof_inyear_his['50%'])

trendline_rcp26=autocorr_MK_org_modif_sens_slope_test(glue_first_jday_hypoxic_deep_prof_inyear_rcp26['50%'])

trendline_rcp60=autocorr_MK_org_modif_sens_slope_test(glue_first_jday_hypoxic_deep_prof_inyear_rcp60['50%'])

trendline_rcp85=autocorr_MK_org_modif_sens_slope_test(glue_first_jday_hypoxic_deep_prof_inyear_rcp85['50%'])




ax1.text(1900, 165, f'y = {trendline_rcp60[-2]:.3f}x + {trendline_rcp60[-1]:.3f}, p = {trendline_rcp60[-3]:.3f}', color='gold', fontsize= 20 )

ax1.plot(glue_first_jday_hypoxic_deep_prof_inyear_rcp60.index.astype(float),
        trendline_rcp60[-2] * np.arange(94) + trendline_rcp60[-1],
        linestyle='--', color='yellow', alpha=0.9, linewidth=3)



ax1.text(1900, 160, f'y = {trendline_rcp85[-2]:.3f}x + {trendline_rcp85[-1]:.3f}, p = {trendline_rcp85[-3]:.3f}', color='red', fontsize= 20 )

ax1.plot(glue_first_jday_hypoxic_deep_prof_inyear_rcp85.index.astype(float),
        trendline_rcp85[-2] * np.arange(94) + trendline_rcp85[-1],
        linestyle='--', color='red', alpha=0.9, linewidth=3)




ax1.set_ylabel('First day of deep hypoxia [Jd]', fontsize=26)
ax1.set_xlabel('Year', fontsize=26)
ax1.tick_params(axis='y', labelsize=22)
ax1.tick_params(axis='x', rotation=45, labelsize=22)

# Plotting the second subplot
ax2 = axes[1]
ax2.fill_between(glue_len_hypoxic_deep_prof_inyear_his.index.astype(float),
                 glue_len_hypoxic_deep_prof_inyear_his['5%'] ,
                 glue_len_hypoxic_deep_prof_inyear_his['95%'] ,
                 color='grey', alpha=0.2)#, label='His 90% CI')

ax2.plot(glue_len_hypoxic_deep_prof_inyear_his.index.astype(float),
          glue_len_hypoxic_deep_prof_inyear_his['50%'] ,
          'k', alpha=0.9, linewidth=3)

ax2.fill_between(glue_len_hypoxic_deep_prof_inyear_rcp26.index.astype(float), glue_len_hypoxic_deep_prof_inyear_rcp26['5%'] , glue_len_hypoxic_deep_prof_inyear_rcp26['95%'] , color='darkgreen', alpha=0.3)#, label='RCP6.0 90% CI')

ax2.plot(glue_len_hypoxic_deep_prof_inyear_rcp26.index.astype(float), glue_len_hypoxic_deep_prof_inyear_rcp26['50%'] , 'darkgreen',alpha=0.9, linewidth=3)

ax2.fill_between(glue_len_hypoxic_deep_prof_inyear_rcp60.index.astype(float), glue_len_hypoxic_deep_prof_inyear_rcp60['5%'] , glue_len_hypoxic_deep_prof_inyear_rcp60['95%'] , color='yellow', alpha=0.5)#, label='RCP6.0 90% CI')

ax2.plot(glue_len_hypoxic_deep_prof_inyear_rcp60.index.astype(float), glue_len_hypoxic_deep_prof_inyear_rcp60['50%'] , 'yellow', alpha=0.9, linewidth=3)

ax2.fill_between(glue_len_hypoxic_deep_prof_inyear_rcp85.index.astype(float), glue_len_hypoxic_deep_prof_inyear_rcp85['5%'] , glue_len_hypoxic_deep_prof_inyear_rcp85['95%'] , color='r', alpha=0.2)#, label='RCP8.5 90% CI')

ax2.plot(glue_len_hypoxic_deep_prof_inyear_rcp85.index.astype(float), glue_len_hypoxic_deep_prof_inyear_rcp85['50%'] , 'r',  alpha=0.9, linewidth=3)




trendline_his=autocorr_MK_org_modif_sens_slope_test(glue_len_hypoxic_deep_prof_inyear_his['50%'])

trendline_rcp26=autocorr_MK_org_modif_sens_slope_test(glue_len_hypoxic_deep_prof_inyear_rcp26['50%'])

trendline_rcp60=autocorr_MK_org_modif_sens_slope_test(glue_len_hypoxic_deep_prof_inyear_rcp60['50%'])

trendline_rcp85=autocorr_MK_org_modif_sens_slope_test(glue_len_hypoxic_deep_prof_inyear_rcp85['50%'])


ax2.text(1900,90, f'y = {trendline_rcp26[-2]:.3f}x + {trendline_rcp26[-1]:.3f}, p = {trendline_rcp26[-3]:.3f}', color='green', fontsize= 20 )

ax2.plot(glue_len_hypoxic_deep_prof_inyear_rcp26.index.astype(float),
        trendline_rcp26[-2] * np.arange(94) + trendline_rcp26[-1],
        linestyle='--', color='darkgreen', alpha=0.9, linewidth=3)



ax2.text(1900, 85, f'y = {trendline_rcp60[-2]:.3f}x + {trendline_rcp60[-1]:.3f}, p = {trendline_rcp60[-3]:.3f}', color='gold', fontsize= 20 )

ax2.plot(glue_len_hypoxic_deep_prof_inyear_rcp60.index.astype(float),
        trendline_rcp60[-2] * np.arange(94) + trendline_rcp60[-1],
        linestyle='--', color='yellow', alpha=0.9, linewidth=3)



ax2.text(1900, 80, f'y = {trendline_rcp85[-2]:.3f}x + {trendline_rcp85[-1]:.3f}, p = {trendline_rcp85[-3]:.3f}', color='red', fontsize= 20 )

ax2.plot(glue_len_hypoxic_deep_prof_inyear_rcp85.index.astype(float),
        trendline_rcp85[-2] * np.arange(94) + trendline_rcp85[-1],
        linestyle='--', color='red', alpha=0.9, linewidth=3)



ax2.set_ylabel('Deep hypoxia duration [d]', fontsize=26)
ax2.set_xlabel('Year', fontsize=26)
ax2.tick_params(axis='y', labelsize=22)
ax2.tick_params(axis='x', rotation=45, labelsize=22)

# Legend for both subplots
fig.legend(loc='upper center', bbox_to_anchor=(0.5, -0.01), shadow=True, ncol=4, fontsize=22)

# Save the figure
fig.savefig("First_jday_duration_deep_hypoxia_profile_withtrendline.png", dpi=300, bbox_inches='tight')
plt.show()

