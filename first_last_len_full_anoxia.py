# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 16:54:58 2023

@author: mahta
"""



#%% Jday of first & last & length of full anoxia condition 
#%%his


# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/gfdl_senarios/his'
all_first_jday_anoxia_full_prof_inyear_his= pd.DataFrame([])
all_last_jday_anoxia_full_prof_inyear_his= pd.DataFrame([])
all_len_anoxia_full_prof_inyear_his= pd.DataFrame([])
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
        
        
        first_jday_anoxia_full_prof_inyear_his=first_last_len_anoxic_prof_inyear  (C, Vr, time_series, threshold=0.5)[1]
        last_jday_anoxia_full_prof_inyear_his=first_last_len_anoxic_prof_inyear  (C, Vr, time_series, threshold=0.5)[3]
        len_anoxia_full_prof_inyear_his=first_last_len_anoxic_prof_inyear  (C, Vr, time_series, threshold=0.5)[4]
        

        all_first_jday_anoxia_full_prof_inyear_his = pd.concat([all_first_jday_anoxia_full_prof_inyear_his , first_jday_anoxia_full_prof_inyear_his], axis=1)
        all_last_jday_anoxia_full_prof_inyear_his = pd.concat([all_last_jday_anoxia_full_prof_inyear_his , last_jday_anoxia_full_prof_inyear_his], axis=1)
        all_len_anoxia_full_prof_inyear_his = pd.concat([all_len_anoxia_full_prof_inyear_his , len_anoxia_full_prof_inyear_his], axis=1)



# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/hadgem_senarios/his'




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
        
        
        first_jday_anoxia_full_prof_inyear_his=first_last_len_anoxic_prof_inyear  (C, Vr, time_series, threshold=0.5)[1]
        last_jday_anoxia_full_prof_inyear_his=first_last_len_anoxic_prof_inyear  (C, Vr, time_series, threshold=0.5)[3]
        len_anoxia_full_prof_inyear_his=first_last_len_anoxic_prof_inyear  (C, Vr, time_series, threshold=0.5)[4]
        

        all_first_jday_anoxia_full_prof_inyear_his = pd.concat([all_first_jday_anoxia_full_prof_inyear_his , first_jday_anoxia_full_prof_inyear_his], axis=1)
        all_last_jday_anoxia_full_prof_inyear_his = pd.concat([all_last_jday_anoxia_full_prof_inyear_his , last_jday_anoxia_full_prof_inyear_his], axis=1)
        all_len_anoxia_full_prof_inyear_his = pd.concat([all_len_anoxia_full_prof_inyear_his , len_anoxia_full_prof_inyear_his], axis=1)


# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/ipsl_senarios/his'




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
        
        
        first_jday_anoxia_full_prof_inyear_his=first_last_len_anoxic_prof_inyear  (C, Vr, time_series, threshold=0.5)[1]
        last_jday_anoxia_full_prof_inyear_his=first_last_len_anoxic_prof_inyear  (C, Vr, time_series, threshold=0.5)[3]
        len_anoxia_full_prof_inyear_his=first_last_len_anoxic_prof_inyear  (C, Vr, time_series, threshold=0.5)[4]
        

        all_first_jday_anoxia_full_prof_inyear_his = pd.concat([all_first_jday_anoxia_full_prof_inyear_his , first_jday_anoxia_full_prof_inyear_his], axis=1)
        all_last_jday_anoxia_full_prof_inyear_his = pd.concat([all_last_jday_anoxia_full_prof_inyear_his , last_jday_anoxia_full_prof_inyear_his], axis=1)
        all_len_anoxia_full_prof_inyear_his = pd.concat([all_len_anoxia_full_prof_inyear_his , len_anoxia_full_prof_inyear_his], axis=1)


# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/miroc_senarios/his'




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
        
        
        first_jday_anoxia_full_prof_inyear_his=first_last_len_anoxic_prof_inyear  (C, Vr, time_series, threshold=0.5)[1]
        last_jday_anoxia_full_prof_inyear_his=first_last_len_anoxic_prof_inyear  (C, Vr, time_series, threshold=0.5)[3]
        len_anoxia_full_prof_inyear_his=first_last_len_anoxic_prof_inyear  (C, Vr, time_series, threshold=0.5)[4]
        

        all_first_jday_anoxia_full_prof_inyear_his = pd.concat([all_first_jday_anoxia_full_prof_inyear_his , first_jday_anoxia_full_prof_inyear_his], axis=1)
        all_last_jday_anoxia_full_prof_inyear_his = pd.concat([all_last_jday_anoxia_full_prof_inyear_his , last_jday_anoxia_full_prof_inyear_his], axis=1)
        all_len_anoxia_full_prof_inyear_his = pd.concat([all_len_anoxia_full_prof_inyear_his , len_anoxia_full_prof_inyear_his], axis=1)

#%%annova_uncertainity_his 

all_first_jday_anoxia_full_prof_inyear_his=all_first_jday_anoxia_full_prof_inyear_his.replace(0, np.nan)

anova_first_jday_anoxia_full_prof_his=annova_uncertainity(all_first_jday_anoxia_full_prof_inyear_his)

anova_first_jday_anoxia_full_prof_his.describe().loc['mean', :]
"""
GCMs             71.291873
param            26.946674
interaction       1.761453
GCMs/param       23.985848
year           1933.000000

"""

anova_first_jday_anoxia_full_prof_his.describe().loc['std', :]
"""
GCMs           25.055037
param          24.619860
interaction     2.509374
GCMs/param     59.340957
year           42.001984

"""

all_last_jday_anoxia_full_prof_inyear_his=all_last_jday_anoxia_full_prof_inyear_his.replace(0, np.nan)


anova_last_jday_anoxia_full_prof_his=annova_uncertainity(all_last_jday_anoxia_full_prof_inyear_his.apply(pd.to_numeric, errors='coerce'))

anova_last_jday_anoxia_full_prof_his.describe().loc['mean', :]
"""
GCMs             96.567230
param             1.079908
interaction       2.352862
GCMs/param             inf
year           1933.000000
"""


anova_last_jday_anoxia_full_prof_his.describe().loc['std', :]

"""
GCMs           13.492262
param           4.373576
interaction     9.791044
GCMs/param           NaN
year           42.001984

"""



anova_len_jday_anoxia_full_prof_his=annova_uncertainity(all_len_anoxia_full_prof_inyear_his.apply(pd.to_numeric, errors='coerce'))

anova_len_jday_anoxia_full_prof_his.describe().loc['mean', :]
"""
GCMs             70.972404
param            25.801336
interaction       3.226260
GCMs/param       17.951448
year           1933.000000
Name: mean, dtype: float64
"""


anova_len_jday_anoxia_full_prof_his.describe().loc['std', :]
"""
GCMs           22.353251
param          20.656785
interaction     6.921945
GCMs/param     47.289179
year           42.001984
Name: std, dtype: float64
"""


#%%rcp26


# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/gfdl_senarios/rcp26'
all_first_jday_anoxia_full_prof_inyear_rcp26= pd.DataFrame([])
all_last_jday_anoxia_full_prof_inyear_rcp26= pd.DataFrame([])
all_len_anoxia_full_prof_inyear_rcp26= pd.DataFrame([])
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
        
        
        first_jday_anoxia_full_prof_inyear_rcp26=first_last_len_anoxic_prof_inyear  (C, Vr, time_series, threshold=0.5)[1]
        last_jday_anoxia_full_prof_inyear_rcp26=first_last_len_anoxic_prof_inyear  (C, Vr, time_series, threshold=0.5)[3]
        len_anoxia_full_prof_inyear_rcp26=first_last_len_anoxic_prof_inyear  (C, Vr, time_series, threshold=0.5)[4]
        

        all_first_jday_anoxia_full_prof_inyear_rcp26 = pd.concat([all_first_jday_anoxia_full_prof_inyear_rcp26 , first_jday_anoxia_full_prof_inyear_rcp26], axis=1)
        all_last_jday_anoxia_full_prof_inyear_rcp26 = pd.concat([all_last_jday_anoxia_full_prof_inyear_rcp26 , last_jday_anoxia_full_prof_inyear_rcp26], axis=1)
        all_len_anoxia_full_prof_inyear_rcp26 = pd.concat([all_len_anoxia_full_prof_inyear_rcp26 , len_anoxia_full_prof_inyear_rcp26], axis=1)


# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/hadgem_senarios/rcp26'




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
        
        
        first_jday_anoxia_full_prof_inyear_rcp26=first_last_len_anoxic_prof_inyear  (C, Vr, time_series, threshold=0.5)[1]
        last_jday_anoxia_full_prof_inyear_rcp26=first_last_len_anoxic_prof_inyear  (C, Vr, time_series, threshold=0.5)[3]
        len_anoxia_full_prof_inyear_rcp26=first_last_len_anoxic_prof_inyear  (C, Vr, time_series, threshold=0.5)[4]
        

        all_first_jday_anoxia_full_prof_inyear_rcp26 = pd.concat([all_first_jday_anoxia_full_prof_inyear_rcp26 , first_jday_anoxia_full_prof_inyear_rcp26], axis=1)
        all_last_jday_anoxia_full_prof_inyear_rcp26 = pd.concat([all_last_jday_anoxia_full_prof_inyear_rcp26 , last_jday_anoxia_full_prof_inyear_rcp26], axis=1)
        all_len_anoxia_full_prof_inyear_rcp26 = pd.concat([all_len_anoxia_full_prof_inyear_rcp26 , len_anoxia_full_prof_inyear_rcp26], axis=1)


# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/ipsl_senarios/rcp26'




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
        
        
        first_jday_anoxia_full_prof_inyear_rcp26=first_last_len_anoxic_prof_inyear  (C, Vr, time_series, threshold=0.5)[1]
        last_jday_anoxia_full_prof_inyear_rcp26=first_last_len_anoxic_prof_inyear  (C, Vr, time_series, threshold=0.5)[3]
        len_anoxia_full_prof_inyear_rcp26=first_last_len_anoxic_prof_inyear  (C, Vr, time_series, threshold=0.5)[4]
        

        all_first_jday_anoxia_full_prof_inyear_rcp26 = pd.concat([all_first_jday_anoxia_full_prof_inyear_rcp26 , first_jday_anoxia_full_prof_inyear_rcp26], axis=1)
        all_last_jday_anoxia_full_prof_inyear_rcp26 = pd.concat([all_last_jday_anoxia_full_prof_inyear_rcp26 , last_jday_anoxia_full_prof_inyear_rcp26], axis=1)
        all_len_anoxia_full_prof_inyear_rcp26 = pd.concat([all_len_anoxia_full_prof_inyear_rcp26 , len_anoxia_full_prof_inyear_rcp26], axis=1)


# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/miroc_senarios/rcp26'




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
        
        
        first_jday_anoxia_full_prof_inyear_rcp26=first_last_len_anoxic_prof_inyear  (C, Vr, time_series, threshold=0.5)[1]
        last_jday_anoxia_full_prof_inyear_rcp26=first_last_len_anoxic_prof_inyear  (C, Vr, time_series, threshold=0.5)[3]
        len_anoxia_full_prof_inyear_rcp26=first_last_len_anoxic_prof_inyear  (C, Vr, time_series, threshold=0.5)[4]
        

        all_first_jday_anoxia_full_prof_inyear_rcp26 = pd.concat([all_first_jday_anoxia_full_prof_inyear_rcp26 , first_jday_anoxia_full_prof_inyear_rcp26], axis=1)
        all_last_jday_anoxia_full_prof_inyear_rcp26 = pd.concat([all_last_jday_anoxia_full_prof_inyear_rcp26 , last_jday_anoxia_full_prof_inyear_rcp26], axis=1)
        all_len_anoxia_full_prof_inyear_rcp26 = pd.concat([all_len_anoxia_full_prof_inyear_rcp26 , len_anoxia_full_prof_inyear_rcp26], axis=1)

#%%annova_uncertainity_rcp26 

all_first_jday_anoxia_full_prof_inyear_rcp26=all_first_jday_anoxia_full_prof_inyear_rcp26.replace(0, np.nan)

anova_first_jday_anoxia_full_prof_rcp26=annova_uncertainity(all_first_jday_anoxia_full_prof_inyear_rcp26)

anova_first_jday_anoxia_full_prof_rcp26.describe().loc['mean', :]
"""
GCMs             71.739743
param            27.092920
interaction       1.167338
GCMs/param       23.680521
year           2052.500000
Name: mean, dtype: float64
"""

anova_first_jday_anoxia_full_prof_rcp26.describe().loc['std', :]
"""
GCMs           24.587849
param          24.401504
interaction     1.735639
GCMs/param     38.659169
year           27.279418
Name: std, dtype: float64

"""


all_last_jday_anoxia_full_prof_inyear_rcp26=all_last_jday_anoxia_full_prof_inyear_rcp26.replace(0, np.nan)

anova_last_jday_anoxia_full_prof_rcp26=annova_uncertainity(all_last_jday_anoxia_full_prof_inyear_rcp26)

anova_last_jday_anoxia_full_prof_rcp26.describe().loc['mean', :]
"""
GCMs             99.615740
param             0.120896
interaction       0.263364
GCMs/param             inf
year           2052.500000
Name: mean, dtype: float64
"""


anova_last_jday_anoxia_full_prof_rcp26.describe().loc['std', :]

"""
GCMs            3.725535
param           0.959485
interaction     2.807081
GCMs/param           NaN
year           27.279418
Name: std, dtype: float64
"""



anova_len_jday_anoxia_full_prof_rcp26=annova_uncertainity(all_len_anoxia_full_prof_inyear_rcp26.apply(pd.to_numeric, errors='coerce'))

anova_len_jday_anoxia_full_prof_rcp26.describe().loc['mean', :]
"""
GCMs             73.566679
param            24.743875
interaction       1.689446
GCMs/param       21.418043
year           2052.500000
Name: mean, dtype: float64
"""


anova_len_jday_anoxia_full_prof_rcp26.describe().loc['std', :]
"""
GCMs           23.633757
param          22.473021
interaction     5.357576
GCMs/param     36.085744
year           27.279418
Name: std, dtype: float64
"""
#%%annova_uncertainity_rcp26_80years

all_first_jday_anoxia_full_prof_inyear_rcp26= all_first_jday_anoxia_full_prof_inyear_rcp26.replace(0, np.nan)

anova_first_jday_anoxia_full_prof_rcp26_80years=annova_uncertainity(all_first_jday_anoxia_full_prof_inyear_rcp26[all_first_jday_anoxia_full_prof_inyear_rcp26.index>2019])

anova_first_jday_anoxia_full_prof_rcp26_80years.describe().loc['mean', :]
"""
GCMs             73.805277
param            24.984564
interaction       1.210159
GCMs/param       26.259775
year           2059.500000
Name: mean, dtype: float64
"""

anova_first_jday_anoxia_full_prof_rcp26_80years.describe().loc['std', :]
"""
GCMs           23.992219
param          23.772055
interaction     1.863924
GCMs/param     40.710359
year           23.237900
Name: std, dtype: float64
"""


all_len_anoxia_full_prof_inyear_rcp26=all_len_anoxia_full_prof_inyear_rcp26.replace(0, np.nan)

anova_len_jday_anoxia_full_prof_rcp26_80years=annova_uncertainity(all_len_anoxia_full_prof_inyear_rcp26[all_len_anoxia_full_prof_inyear_rcp26.index>2019].apply(pd.to_numeric, errors='coerce'))

anova_len_jday_anoxia_full_prof_rcp26_80years.describe().loc['mean', :]
"""
GCMs             75.472251
param            22.720167
interaction       1.807582
GCMs/param       23.443575
year           2059.500000
Name: mean, dtype: float64
"""


anova_len_jday_anoxia_full_prof_rcp26_80years.describe().loc['std', :]
"""
GCMs           22.772151
param          21.412628
interaction     5.789593
GCMs/param     37.942371
year           23.237900
Name: std, dtype: float64
"""








#%%rcp60


# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/gfdl_senarios/rcp60'
all_first_jday_anoxia_full_prof_inyear_rcp60= pd.DataFrame([])
all_last_jday_anoxia_full_prof_inyear_rcp60= pd.DataFrame([])
all_len_anoxia_full_prof_inyear_rcp60= pd.DataFrame([])
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
        
        
        first_jday_anoxia_full_prof_inyear_rcp60=first_last_len_anoxic_prof_inyear  (C, Vr, time_series, threshold=0.5)[1]
        last_jday_anoxia_full_prof_inyear_rcp60=first_last_len_anoxic_prof_inyear  (C, Vr, time_series, threshold=0.5)[3]
        len_anoxia_full_prof_inyear_rcp60=first_last_len_anoxic_prof_inyear  (C, Vr, time_series, threshold=0.5)[4]
        

        all_first_jday_anoxia_full_prof_inyear_rcp60 = pd.concat([all_first_jday_anoxia_full_prof_inyear_rcp60 , first_jday_anoxia_full_prof_inyear_rcp60], axis=1)
        all_last_jday_anoxia_full_prof_inyear_rcp60 = pd.concat([all_last_jday_anoxia_full_prof_inyear_rcp60 , last_jday_anoxia_full_prof_inyear_rcp60], axis=1)
        all_len_anoxia_full_prof_inyear_rcp60 = pd.concat([all_len_anoxia_full_prof_inyear_rcp60 , len_anoxia_full_prof_inyear_rcp60], axis=1)


# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/hadgem_senarios/rcp60'




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
        
        
        first_jday_anoxia_full_prof_inyear_rcp60=first_last_len_anoxic_prof_inyear  (C, Vr, time_series, threshold=0.5)[1]
        last_jday_anoxia_full_prof_inyear_rcp60=first_last_len_anoxic_prof_inyear  (C, Vr, time_series, threshold=0.5)[3]
        len_anoxia_full_prof_inyear_rcp60=first_last_len_anoxic_prof_inyear  (C, Vr, time_series, threshold=0.5)[4]
        

        all_first_jday_anoxia_full_prof_inyear_rcp60 = pd.concat([all_first_jday_anoxia_full_prof_inyear_rcp60 , first_jday_anoxia_full_prof_inyear_rcp60], axis=1)
        all_last_jday_anoxia_full_prof_inyear_rcp60 = pd.concat([all_last_jday_anoxia_full_prof_inyear_rcp60 , last_jday_anoxia_full_prof_inyear_rcp60], axis=1)
        all_len_anoxia_full_prof_inyear_rcp60 = pd.concat([all_len_anoxia_full_prof_inyear_rcp60 , len_anoxia_full_prof_inyear_rcp60], axis=1)


# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/ipsl_senarios/rcp60'




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
        
        
        first_jday_anoxia_full_prof_inyear_rcp60=first_last_len_anoxic_prof_inyear  (C, Vr, time_series, threshold=0.5)[1]
        last_jday_anoxia_full_prof_inyear_rcp60=first_last_len_anoxic_prof_inyear  (C, Vr, time_series, threshold=0.5)[3]
        len_anoxia_full_prof_inyear_rcp60=first_last_len_anoxic_prof_inyear  (C, Vr, time_series, threshold=0.5)[4]
        

        all_first_jday_anoxia_full_prof_inyear_rcp60 = pd.concat([all_first_jday_anoxia_full_prof_inyear_rcp60 , first_jday_anoxia_full_prof_inyear_rcp60], axis=1)
        all_last_jday_anoxia_full_prof_inyear_rcp60 = pd.concat([all_last_jday_anoxia_full_prof_inyear_rcp60 , last_jday_anoxia_full_prof_inyear_rcp60], axis=1)
        all_len_anoxia_full_prof_inyear_rcp60 = pd.concat([all_len_anoxia_full_prof_inyear_rcp60 , len_anoxia_full_prof_inyear_rcp60], axis=1)


# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/miroc_senarios/rcp60'




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
        
        
        first_jday_anoxia_full_prof_inyear_rcp60=first_last_len_anoxic_prof_inyear  (C, Vr, time_series, threshold=0.5)[1]
        last_jday_anoxia_full_prof_inyear_rcp60=first_last_len_anoxic_prof_inyear  (C, Vr, time_series, threshold=0.5)[3]
        len_anoxia_full_prof_inyear_rcp60=first_last_len_anoxic_prof_inyear  (C, Vr, time_series, threshold=0.5)[4]
        

        all_first_jday_anoxia_full_prof_inyear_rcp60 = pd.concat([all_first_jday_anoxia_full_prof_inyear_rcp60 , first_jday_anoxia_full_prof_inyear_rcp60], axis=1)
        all_last_jday_anoxia_full_prof_inyear_rcp60 = pd.concat([all_last_jday_anoxia_full_prof_inyear_rcp60 , last_jday_anoxia_full_prof_inyear_rcp60], axis=1)
        all_len_anoxia_full_prof_inyear_rcp60 = pd.concat([all_len_anoxia_full_prof_inyear_rcp60 , len_anoxia_full_prof_inyear_rcp60], axis=1)


#%%annova_uncertainity_rcp60 

all_first_jday_anoxia_full_prof_inyear_rcp60=all_first_jday_anoxia_full_prof_inyear_rcp60.replace(0, np.nan)

anova_first_jday_anoxia_full_prof_rcp60=annova_uncertainity(all_first_jday_anoxia_full_prof_inyear_rcp60)

anova_first_jday_anoxia_full_prof_rcp60.describe().loc['mean', :]
"""
GCMs             69.378527
param            29.301456
interaction       1.320017
GCMs/param       13.362191
year           2052.500000
Name: mean, dtype: float64
"""

anova_first_jday_anoxia_full_prof_rcp60.describe().loc['std', :]
"""
GCMs           23.700160
param          23.520450
interaction     1.197673
GCMs/param     23.263542
year           27.279418
"""

all_last_jday_anoxia_full_prof_inyear_rcp60=all_last_jday_anoxia_full_prof_inyear_rcp60.replace(0, np.nan)


anova_last_jday_anoxia_full_prof_rcp60=annova_uncertainity(all_last_jday_anoxia_full_prof_inyear_rcp60)

anova_last_jday_anoxia_full_prof_rcp60.describe().loc['mean', :]
"""
GCMs             99.330731
param             0.195553
interaction       0.473716
GCMs/param             inf
year           2052.500000
"""


anova_last_jday_anoxia_full_prof_rcp60.describe().loc['std', :]

"""
GCMs            6.488805
param           1.642233
interaction     4.877236
GCMs/param           NaN
year           27.279418
Name: std, dtype: float64
"""



anova_len_jday_anoxia_full_prof_rcp60=annova_uncertainity(all_len_anoxia_full_prof_inyear_rcp60.apply(pd.to_numeric, errors='coerce'))

anova_len_jday_anoxia_full_prof_rcp60.describe().loc['mean', :]
"""
GCMs             76.583210
param            22.101949
interaction       1.314841
GCMs/param       13.581936
year           2052.500000
Name: mean, dtype: float64
"""


anova_len_jday_anoxia_full_prof_rcp60.describe().loc['std', :]
"""
GCMs           20.245843
param          19.732958
interaction     2.039684
GCMs/param     21.813315
year           27.279418
Name: std, dtype: float64
"""

#%%annova_uncertainity_rcp60_80years

all_first_jday_anoxia_full_prof_inyear_rcp60=all_first_jday_anoxia_full_prof_inyear_rcp60.replace(0, np.nan)


anova_first_jday_anoxia_full_prof_rcp60_80years=annova_uncertainity(all_first_jday_anoxia_full_prof_inyear_rcp60[all_first_jday_anoxia_full_prof_inyear_rcp60.index>2019])

anova_first_jday_anoxia_full_prof_rcp60_80years.describe().loc['mean', :]
"""
GCMs             67.434261
param            31.269106
interaction       1.296633
GCMs/param       11.953337
year           2059.500000
Name: mean, dtype: float64
"""

anova_first_jday_anoxia_full_prof_rcp60_80years.describe().loc['std', :]
"""
GCMs           24.186913
param          23.965183
interaction     1.094109
GCMs/param     22.719892
year           23.237900
Name: std, dtype: float64

"""




anova_len_jday_anoxia_full_prof_rcp60_80years=annova_uncertainity(all_len_anoxia_full_prof_inyear_rcp60[all_len_anoxia_full_prof_inyear_rcp60.index>2019].apply(pd.to_numeric, errors='coerce'))

anova_len_jday_anoxia_full_prof_rcp60_80years.describe().loc['mean', :]
"""
GCMs             76.361272
param            22.496625
interaction       1.142102
GCMs/param       13.214313
year           2059.500000
Name: mean, dtype: float64
"""


anova_len_jday_anoxia_full_prof_rcp60_80years.describe().loc['std', :]
"""
GCMs           20.541440
param          20.046707
interaction     1.093179
GCMs/param     22.471130
year           23.237900
Name: std, dtype: float64
"""



#%%rcp85


# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/gfdl_senarios/rcp85'
all_first_jday_anoxia_full_prof_inyear_rcp85= pd.DataFrame([])
all_last_jday_anoxia_full_prof_inyear_rcp85= pd.DataFrame([])
all_len_anoxia_full_prof_inyear_rcp85= pd.DataFrame([])
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
        
        
        first_jday_anoxia_full_prof_inyear_rcp85=first_last_len_anoxic_prof_inyear  (C, Vr, time_series, threshold=0.5)[1]
        last_jday_anoxia_full_prof_inyear_rcp85=first_last_len_anoxic_prof_inyear  (C, Vr, time_series, threshold=0.5)[3]
        len_anoxia_full_prof_inyear_rcp85=first_last_len_anoxic_prof_inyear  (C, Vr, time_series, threshold=0.5)[4]
        

        all_first_jday_anoxia_full_prof_inyear_rcp85 = pd.concat([all_first_jday_anoxia_full_prof_inyear_rcp85 , first_jday_anoxia_full_prof_inyear_rcp85], axis=1)
        all_last_jday_anoxia_full_prof_inyear_rcp85 = pd.concat([all_last_jday_anoxia_full_prof_inyear_rcp85 , last_jday_anoxia_full_prof_inyear_rcp85], axis=1)
        all_len_anoxia_full_prof_inyear_rcp85 = pd.concat([all_len_anoxia_full_prof_inyear_rcp85 , len_anoxia_full_prof_inyear_rcp85], axis=1)


# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/hadgem_senarios/rcp85'




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
        
        
        first_jday_anoxia_full_prof_inyear_rcp85=first_last_len_anoxic_prof_inyear  (C, Vr, time_series, threshold=0.5)[1]
        last_jday_anoxia_full_prof_inyear_rcp85=first_last_len_anoxic_prof_inyear  (C, Vr, time_series, threshold=0.5)[3]
        len_anoxia_full_prof_inyear_rcp85=first_last_len_anoxic_prof_inyear  (C, Vr, time_series, threshold=0.5)[4]
        

        all_first_jday_anoxia_full_prof_inyear_rcp85 = pd.concat([all_first_jday_anoxia_full_prof_inyear_rcp85 , first_jday_anoxia_full_prof_inyear_rcp85], axis=1)
        all_last_jday_anoxia_full_prof_inyear_rcp85 = pd.concat([all_last_jday_anoxia_full_prof_inyear_rcp85 , last_jday_anoxia_full_prof_inyear_rcp85], axis=1)
        all_len_anoxia_full_prof_inyear_rcp85 = pd.concat([all_len_anoxia_full_prof_inyear_rcp85 , len_anoxia_full_prof_inyear_rcp85], axis=1)


# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/ipsl_senarios/rcp85'




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
        
        
        first_jday_anoxia_full_prof_inyear_rcp85=first_last_len_anoxic_prof_inyear  (C, Vr, time_series, threshold=0.5)[1]
        last_jday_anoxia_full_prof_inyear_rcp85=first_last_len_anoxic_prof_inyear  (C, Vr, time_series, threshold=0.5)[3]
        len_anoxia_full_prof_inyear_rcp85=first_last_len_anoxic_prof_inyear  (C, Vr, time_series, threshold=0.5)[4]
        

        all_first_jday_anoxia_full_prof_inyear_rcp85 = pd.concat([all_first_jday_anoxia_full_prof_inyear_rcp85 , first_jday_anoxia_full_prof_inyear_rcp85], axis=1)
        all_last_jday_anoxia_full_prof_inyear_rcp85 = pd.concat([all_last_jday_anoxia_full_prof_inyear_rcp85 , last_jday_anoxia_full_prof_inyear_rcp85], axis=1)
        all_len_anoxia_full_prof_inyear_rcp85 = pd.concat([all_len_anoxia_full_prof_inyear_rcp85 , len_anoxia_full_prof_inyear_rcp85], axis=1)


# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/miroc_senarios/rcp85'




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
        
        
        first_jday_anoxia_full_prof_inyear_rcp85=first_last_len_anoxic_prof_inyear  (C, Vr, time_series, threshold=0.5)[1]
        last_jday_anoxia_full_prof_inyear_rcp85=first_last_len_anoxic_prof_inyear  (C, Vr, time_series, threshold=0.5)[3]
        len_anoxia_full_prof_inyear_rcp85=first_last_len_anoxic_prof_inyear  (C, Vr, time_series, threshold=0.5)[4]
        

        all_first_jday_anoxia_full_prof_inyear_rcp85 = pd.concat([all_first_jday_anoxia_full_prof_inyear_rcp85 , first_jday_anoxia_full_prof_inyear_rcp85], axis=1)
        all_last_jday_anoxia_full_prof_inyear_rcp85 = pd.concat([all_last_jday_anoxia_full_prof_inyear_rcp85 , last_jday_anoxia_full_prof_inyear_rcp85], axis=1)
        all_len_anoxia_full_prof_inyear_rcp85 = pd.concat([all_len_anoxia_full_prof_inyear_rcp85 , len_anoxia_full_prof_inyear_rcp85], axis=1)



#%%annova_uncertainity_rcp85 


all_first_jday_anoxia_full_prof_inyear_rcp85=all_first_jday_anoxia_full_prof_inyear_rcp85.replace(0, np.nan)


anova_first_jday_anoxia_full_prof_rcp85=annova_uncertainity(all_first_jday_anoxia_full_prof_inyear_rcp85)

anova_first_jday_anoxia_full_prof_rcp85.describe().loc['mean', :]
"""
GCMs             70.501274
param            28.103186
interaction       1.395539
GCMs/param       23.858819
year           2052.500000
Name: mean, dtype: float64
"""

anova_first_jday_anoxia_full_prof_rcp85.describe().loc['std', :]
"""

GCMs           24.679192
param          24.185330
interaction     1.094809
GCMs/param     44.639247
year           27.279418

"""

all_last_jday_anoxia_full_prof_inyear_rcp85=all_last_jday_anoxia_full_prof_inyear_rcp85.replace(0, np.nan)


anova_last_jday_anoxia_full_prof_rcp85=annova_uncertainity(all_last_jday_anoxia_full_prof_inyear_rcp85)

anova_last_jday_anoxia_full_prof_rcp85.describe().loc['mean', :]
"""
GCMs             99.706847
param             0.073288
interaction       0.219865
GCMs/param             inf
year           2052.500000
Name: mean, dtype: float64
"""


anova_last_jday_anoxia_full_prof_rcp85.describe().loc['std', :]

"""
GCMs            2.842228
param           0.710557
interaction     2.131671
GCMs/param           NaN
year           27.279418
"""



anova_len_jday_anoxia_full_prof_rcp85=annova_uncertainity(all_len_anoxia_full_prof_inyear_rcp85.apply(pd.to_numeric, errors='coerce'))

anova_len_jday_anoxia_full_prof_rcp85.describe().loc['mean', :]
"""
GCMs             82.698199
param            15.744849
interaction       1.556952
GCMs/param       29.330543
year           2052.500000
Name: mean, dtype: float64
"""


anova_len_jday_anoxia_full_prof_rcp85.describe().loc['std', :]
"""
GCMs           16.378950
param          14.784250
interaction     4.396224
GCMs/param     49.327869
year           27.279418
Name: std, dtype: float64
"""


#%%annova_uncertainity_rcp85_80years

all_first_jday_anoxia_full_prof_inyear_rcp85=all_first_jday_anoxia_full_prof_inyear_rcp85.replace(0, np.nan)

anova_first_jday_anoxia_full_prof_rcp85_80years=annova_uncertainity(all_first_jday_anoxia_full_prof_inyear_rcp85[all_first_jday_anoxia_full_prof_inyear_rcp85.index>2019])

anova_first_jday_anoxia_full_prof_rcp85_80years.describe().loc['mean', :]
"""
GCMs             71.468322
param            27.114527
interaction       1.417151
GCMs/param       23.404825
year           2059.500000
Name: mean, dtype: float64
"""

anova_first_jday_anoxia_full_prof_rcp85_80years.describe().loc['std', :]
"""
GCMs           24.580526
param          23.984763
interaction     1.107041
GCMs/param     35.190463
year           23.237900
Name: std, dtype: float64

"""




anova_len_jday_anoxia_full_prof_rcp85_80years=annova_uncertainity(all_len_anoxia_full_prof_inyear_rcp85[all_len_anoxia_full_prof_inyear_rcp85.index>2019].apply(pd.to_numeric, errors='coerce'))

anova_len_jday_anoxia_full_prof_rcp85_80years.describe().loc['mean', :]
"""
GCMs             83.121041
param            15.242720
interaction       1.636240
GCMs/param       30.178675
year           2059.500000
Name: mean, dtype: float64
"""


anova_len_jday_anoxia_full_prof_rcp85_80years.describe().loc['std', :]
"""
GCMs           16.645287
param          14.790238
interaction     4.716272
GCMs/param     46.325134
year           23.237900
Name: std, dtype: float64
"""





#%% Plotting of anova_len_jday_anoxia_full_prof, anova_first_jday_anoxia_full_prof rcp85

#first_jday_anoxia_his

#years
contributions_first_jday_anoxia_his_years=anova_first_jday_anoxia_full_prof_his['year']
#GCMs
gcm_contributions_first_jday_anoxia_his= anova_first_jday_anoxia_full_prof_his['GCMs']
#Param
param_contributions_first_jday_anoxia_his=anova_first_jday_anoxia_full_prof_his['param']
#interaction
interact_contributions_first_jday_anoxia_his =anova_first_jday_anoxia_full_prof_his['interaction']


#len_jday_anoxia_his

#years
contributions_len_jday_anoxia_his_years=anova_len_jday_anoxia_full_prof_his['year']
#GCMs
gcm_contributions_len_jday_anoxia_his= anova_len_jday_anoxia_full_prof_his['GCMs']
#Param
param_contributions_len_jday_anoxia_his=anova_len_jday_anoxia_full_prof_his['param']
#interaction
interact_contributions_len_jday_anoxia_his =anova_len_jday_anoxia_full_prof_his['interaction']

     

#first_jday_anoxia_rcp26

#years
contributions_first_jday_anoxia_rcp26_years=anova_first_jday_anoxia_full_prof_rcp26['year']
#GCMs
gcm_contributions_first_jday_anoxia_rcp26= anova_first_jday_anoxia_full_prof_rcp26['GCMs']
#Param
param_contributions_first_jday_anoxia_rcp26=anova_first_jday_anoxia_full_prof_rcp26['param']
#interaction
interact_contributions_first_jday_anoxia_rcp26 =anova_first_jday_anoxia_full_prof_rcp26['interaction']


#len_jday_anoxia_rcp26

#years
contributions_len_jday_anoxia_rcp26_years=anova_len_jday_anoxia_full_prof_rcp26['year']
#GCMs
gcm_contributions_len_jday_anoxia_rcp26= anova_len_jday_anoxia_full_prof_rcp26['GCMs']
#Param
param_contributions_len_jday_anoxia_rcp26=anova_len_jday_anoxia_full_prof_rcp26['param']
#interaction
interact_contributions_len_jday_anoxia_rcp26 =anova_len_jday_anoxia_full_prof_rcp26['interaction']

     

#first_jday_anoxia_rcp60

#years
contributions_first_jday_anoxia_rcp60_years=anova_first_jday_anoxia_full_prof_rcp60['year']
#GCMs
gcm_contributions_first_jday_anoxia_rcp60= anova_first_jday_anoxia_full_prof_rcp60['GCMs']
#Param
param_contributions_first_jday_anoxia_rcp60=anova_first_jday_anoxia_full_prof_rcp60['param']
#interaction
interact_contributions_first_jday_anoxia_rcp60 =anova_first_jday_anoxia_full_prof_rcp60['interaction']


#len_jday_anoxia_rcp60

#years
contributions_len_jday_anoxia_rcp60_years=anova_len_jday_anoxia_full_prof_rcp60['year']
#GCMs
gcm_contributions_len_jday_anoxia_rcp60= anova_len_jday_anoxia_full_prof_rcp60['GCMs']
#Param
param_contributions_len_jday_anoxia_rcp60=anova_len_jday_anoxia_full_prof_rcp60['param']
#interaction
interact_contributions_len_jday_anoxia_rcp60 =anova_len_jday_anoxia_full_prof_rcp60['interaction']

     
#first_jday_anoxia_rcp85

#years
contributions_first_jday_anoxia_rcp85_years=anova_first_jday_anoxia_full_prof_rcp85['year']
#GCMs
gcm_contributions_first_jday_anoxia_rcp85= anova_first_jday_anoxia_full_prof_rcp85['GCMs']
#Param
param_contributions_first_jday_anoxia_rcp85=anova_first_jday_anoxia_full_prof_rcp85['param']
#interaction
interact_contributions_first_jday_anoxia_rcp85 =anova_first_jday_anoxia_full_prof_rcp85['interaction']


#len_jday_anoxia_rcp85

#years
contributions_len_jday_anoxia_rcp85_years=anova_len_jday_anoxia_full_prof_rcp85['year']
#GCMs
gcm_contributions_len_jday_anoxia_rcp85= anova_len_jday_anoxia_full_prof_rcp85['GCMs']
#Param
param_contributions_len_jday_anoxia_rcp85=anova_len_jday_anoxia_full_prof_rcp85['param']
#interaction
interact_contributions_len_jday_anoxia_rcp85 =anova_len_jday_anoxia_full_prof_rcp85['interaction']

#%%

# Define the directory path
directory_path = r'C:\Users\mahta\OneDrive\Documents\Chapter_1_PhD_py_codes_results\Future_simulation_results\all_4_models\uncertainty'

# Change the current working directory
os.chdir(directory_path)     


import matplotlib.pyplot as plt
from matplotlib.patches import Patch

# Define colors explicitly as RGB tuples
colors = [(0.96, 0.80, 0.69), (0.6, 0.4, 0.8), (0, 0, 1)]  # Flesh, Dark Orchid, Blue

# Create a figure with three subplots
fig, axs = plt.subplots(2, 2, figsize=(20, 10), sharey=True)

# Define data for each subplot (assuming you have defined your data earlier)


# Subplot for rcp26
axs[0, 0].fill_between(contributions_annual_HF_his_years, 0, gcm_contributions_annual_HF_his , label='GCMs', alpha=0.7, color=colors[0], edgecolor='black')
axs[0, 0].fill_between(contributions_annual_HF_his_years, gcm_contributions_annual_HF_his , gcm_contributions_annual_HF_his + param_contributions_annual_HF_his, label='Parameters', alpha=0.7, color=colors[1], edgecolor='black')
axs[0, 0].fill_between(contributions_annual_HF_his_years, gcm_contributions_annual_HF_his  + param_contributions_annual_HF_his, gcm_contributions_annual_HF_his + param_contributions_annual_HF_his + interact_contributions_annual_HF_his, label='Interactions', alpha=0.7, color=colors[2], edgecolor='black')
axs[0, 0].set_title('(a) His', fontsize=24)
axs[0, 0].set_ylim(0,100)
axs[0, 0].set_xlim(1861, 2005)
axs[0, 0].tick_params(axis='both', which='major', labelsize=20)

# Subplot for rcp26
axs[0, 1].fill_between(contributions_annual_HF_rcp26_years, 0, gcm_contributions_annual_HF_rcp26, label='GCMs', alpha=0.7, color=colors[0], edgecolor='black')
axs[0, 1].fill_between(contributions_annual_HF_rcp26_years, gcm_contributions_annual_HF_rcp26, gcm_contributions_annual_HF_rcp26 + param_contributions_annual_HF_rcp26, label='Parameters', alpha=0.7, color=colors[1], edgecolor='black')
axs[0, 1].fill_between(contributions_annual_HF_rcp26_years, gcm_contributions_annual_HF_rcp26 + param_contributions_annual_HF_rcp26, gcm_contributions_annual_HF_rcp26 + param_contributions_annual_HF_rcp26 + interact_contributions_annual_HF_rcp26, label='Interactions', alpha=0.7, color=colors[2], edgecolor='black')
axs[0, 1].set_title('(b) RCP2.6', fontsize=24)
axs[0, 1].set_ylim(0,100)
axs[0, 1].set_xlim(2006, 2099)
axs[0, 1].tick_params(axis='both', which='major', labelsize=20)

# Subplot for rcp60
axs[1, 0].fill_between(contributions_annual_HF_rcp60_years, 0, gcm_contributions_annual_HF_rcp60, label='GCMs', alpha=0.7, color=colors[0], edgecolor='black')
axs[1, 0].fill_between(contributions_annual_HF_rcp60_years, gcm_contributions_annual_HF_rcp60, gcm_contributions_annual_HF_rcp60 + param_contributions_annual_HF_rcp60, label='Parameters', alpha=0.7, color=colors[1], edgecolor='black')
axs[1, 0].fill_between(contributions_annual_HF_rcp60_years, gcm_contributions_annual_HF_rcp60 + param_contributions_annual_HF_rcp60, gcm_contributions_annual_HF_rcp60 + param_contributions_annual_HF_rcp60 + interact_contributions_annual_HF_rcp60, label='Interactions', alpha=0.7, color=colors[2], edgecolor='black')
axs[1, 0].set_title('(c) RCP6.0', fontsize=24)
axs[1, 0].set_ylim(0,100)
axs[1, 0].set_xlim(2006, 2099)
axs[1, 0].tick_params(axis='both', which='major', labelsize=20)

# Subplot for rcp85
axs[1, 1].fill_between(contributions_annual_HF_rcp85_years, 0, gcm_contributions_annual_HF_rcp85, label='GCMs', alpha=0.7, color=colors[0], edgecolor='black')
axs[1, 1].fill_between(contributions_annual_HF_rcp85_years, gcm_contributions_annual_HF_rcp85, gcm_contributions_annual_HF_rcp85 + param_contributions_annual_HF_rcp85, label='Parameters', alpha=0.7, color=colors[1], edgecolor='black')
axs[1, 1].fill_between(contributions_annual_HF_rcp85_years, gcm_contributions_annual_HF_rcp85 + param_contributions_annual_HF_rcp85, gcm_contributions_annual_HF_rcp85 + param_contributions_annual_HF_rcp85 + interact_contributions_annual_HF_rcp85, label='Interactions', alpha=0.7, color=colors[2], edgecolor='black')
axs[1, 1].set_title('(d) RCP8.5', fontsize=24)
axs[1, 1].set_ylim(0,100)
axs[1, 1].set_xlim(2006, 2099)
axs[1, 1].tick_params(axis='both', which='major', labelsize=20)

# Adding labels and title with increased font size
# fig.text(0.5, 0.08, 'Year', ha='center', fontsize=20)
fig.text(0.06, 0.5, 'Uncertainty sources in annual full-deep-water', va='center', rotation='vertical', fontsize=24)
fig.text(0.075, 0.5, 'anoxia duration [%]', va='center', rotation='vertical', fontsize=24)

# Create legend handles and labels
legend_handles = [Patch(facecolor=colors[0], edgecolor='black'), 
                  Patch(facecolor=colors[1], edgecolor='black'), 
                  Patch(facecolor=colors[2], edgecolor='black')]
legend_labels = ['GCMs', 'Parameters', 'Interactions']

# Add a single legend outside the subplots
fig.legend(legend_handles, legend_labels,bbox_to_anchor=(0.75, 0.1), fontsize=22, ncol=3)


# Save the plot
plt.savefig('uncertainty_len_jday_anoxia_allyears_rcps_his.png', dpi=300, bbox_inches='tight')

plt.show()















   
#%%For his

# Define the directory path
directory_path = r'C:\Users\mahta\OneDrive\Documents\Chapter_1_PhD_py_codes_results\Future_simulation_results\all_4_models\uncertainty'

# Change the current working directory
os.chdir(directory_path)     


import matplotlib.pyplot as plt
from matplotlib.patches import Patch

# Define colors explicitly as RGB tuples
colors = [(0.96, 0.80, 0.69), (0.6, 0.4, 0.8), (0, 0, 1)]  # Flesh, Dark Orchid, Blue

# Create a figure with three subplots
fig, axs = plt.subplots(1, 2, figsize=(20, 5), sharey=True, sharex=True)

axs[0].fill_between(contributions_first_jday_anoxia_his_years, 0, gcm_contributions_first_jday_anoxia_his , label='GCMs', alpha=0.7, color=colors[0], edgecolor='black')
axs[0].fill_between(contributions_first_jday_anoxia_his_years, gcm_contributions_first_jday_anoxia_his , gcm_contributions_first_jday_anoxia_his + param_contributions_first_jday_anoxia_his, label='Parameters', alpha=0.7, color=colors[1], edgecolor='black')
axs[0].fill_between(contributions_first_jday_anoxia_his_years, gcm_contributions_first_jday_anoxia_his  + param_contributions_first_jday_anoxia_his, gcm_contributions_first_jday_anoxia_his + param_contributions_first_jday_anoxia_his + interact_contributions_first_jday_anoxia_his, label='Interactions', alpha=0.7, color=colors[2], edgecolor='black')
axs[0].set_title('First day of full anoxia profile in His', fontsize=20)
axs[0].set_ylim(0,100)
axs[0].set_xlim(1861, 2005)
axs[0].tick_params(axis='both', which='major', labelsize=20)



axs[1].fill_between(contributions_len_jday_anoxia_his_years, 0, gcm_contributions_len_jday_anoxia_his , label='GCMs', alpha=0.7, color=colors[0], edgecolor='black')
axs[1].fill_between(contributions_len_jday_anoxia_his_years, gcm_contributions_len_jday_anoxia_his , gcm_contributions_len_jday_anoxia_his + param_contributions_len_jday_anoxia_his, label='Parameters', alpha=0.7, color=colors[1], edgecolor='black')
axs[1].fill_between(contributions_len_jday_anoxia_his_years, gcm_contributions_len_jday_anoxia_his  + param_contributions_len_jday_anoxia_his, gcm_contributions_len_jday_anoxia_his + param_contributions_len_jday_anoxia_his + interact_contributions_len_jday_anoxia_his, label='Interactions', alpha=0.7, color=colors[2], edgecolor='black')
axs[1].set_title('Duration of full anoxia profile in His', fontsize=20)
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
plt.savefig('uncertainty_first_len_full_anoxia_duration_allyears_his.png', dpi=300, bbox_inches='tight')

plt.show()



#%%For all RCPs  all years 

# Define the directory path
directory_path = r'C:\Users\mahta\OneDrive\Documents\Chapter_1_PhD_py_codes_results\Future_simulation_results\all_4_models\uncertainty'

# Change the current working directory
os.chdir(directory_path)     
    

import matplotlib.pyplot as plt
from matplotlib.patches import Patch

# Define colors explicitly as RGB tuples
colors = [(0.96, 0.80, 0.69), (0.6, 0.4, 0.8), (0, 0, 1)]  # Flesh, Dark Orchid, Blue

# Create a figure with three subplots
fig, axs = plt.subplots(3, 2, figsize=(20, 15), sharey=True, sharex=True)

axs[0, 0].fill_between(contributions_first_jday_anoxia_rcp26_years, 0, gcm_contributions_first_jday_anoxia_rcp26 , label='GCMs', alpha=0.7, color=colors[0], edgecolor='black')
axs[0, 0].fill_between(contributions_first_jday_anoxia_rcp26_years, gcm_contributions_first_jday_anoxia_rcp26 , gcm_contributions_first_jday_anoxia_rcp26 + param_contributions_first_jday_anoxia_rcp26, label='Parameters', alpha=0.7, color=colors[1], edgecolor='black')
axs[0, 0].fill_between(contributions_first_jday_anoxia_rcp26_years, gcm_contributions_first_jday_anoxia_rcp26  + param_contributions_first_jday_anoxia_rcp26, gcm_contributions_first_jday_anoxia_rcp26 + param_contributions_first_jday_anoxia_rcp26 + interact_contributions_first_jday_anoxia_rcp26, label='Interactions', alpha=0.7, color=colors[2], edgecolor='black')
axs[0, 0].set_title('First day of full anoxia profile in RCP2.6', fontsize=20)
axs[0, 0].set_ylim(0,100)
axs[0, 0].set_xlim(2006, 2099)
axs[0, 0].tick_params(axis='both', which='major', labelsize=20)



axs[0, 1].fill_between(contributions_len_jday_anoxia_rcp26_years, 0, gcm_contributions_len_jday_anoxia_rcp26 , label='GCMs', alpha=0.7, color=colors[0], edgecolor='black')
axs[0, 1].fill_between(contributions_len_jday_anoxia_rcp26_years, gcm_contributions_len_jday_anoxia_rcp26 , gcm_contributions_len_jday_anoxia_rcp26 + param_contributions_len_jday_anoxia_rcp26, label='Parameters', alpha=0.7, color=colors[1], edgecolor='black')
axs[0, 1].fill_between(contributions_len_jday_anoxia_rcp26_years, gcm_contributions_len_jday_anoxia_rcp26  + param_contributions_len_jday_anoxia_rcp26, gcm_contributions_len_jday_anoxia_rcp26 + param_contributions_len_jday_anoxia_rcp26 + interact_contributions_len_jday_anoxia_rcp26, label='Interactions', alpha=0.7, color=colors[2], edgecolor='black')
axs[0, 1].set_title('Duration of full anoxia profile in RCP2.6', fontsize=20)
axs[0, 1].set_ylim(0,100)
axs[0, 1].set_xlim(2006, 2099)
axs[0, 1].tick_params(axis='both', which='major', labelsize=20)

axs[1, 0].fill_between(contributions_first_jday_anoxia_rcp60_years, 0, gcm_contributions_first_jday_anoxia_rcp60 , label='GCMs', alpha=0.7, color=colors[0], edgecolor='black')
axs[1, 0].fill_between(contributions_first_jday_anoxia_rcp60_years, gcm_contributions_first_jday_anoxia_rcp60 , gcm_contributions_first_jday_anoxia_rcp60 + param_contributions_first_jday_anoxia_rcp60, label='Parameters', alpha=0.7, color=colors[1], edgecolor='black')
axs[1, 0].fill_between(contributions_first_jday_anoxia_rcp60_years, gcm_contributions_first_jday_anoxia_rcp60  + param_contributions_first_jday_anoxia_rcp60, gcm_contributions_first_jday_anoxia_rcp60 + param_contributions_first_jday_anoxia_rcp60 + interact_contributions_first_jday_anoxia_rcp60, label='Interactions', alpha=0.7, color=colors[2], edgecolor='black')
axs[1, 0].set_title('First day of full anoxia profile in RCP6.0', fontsize=20)
axs[1, 0].set_ylim(0,100)
axs[1, 0].set_xlim(2006, 2099)
axs[1, 0].tick_params(axis='both', which='major', labelsize=20)



axs[1, 1].fill_between(contributions_len_jday_anoxia_rcp60_years, 0, gcm_contributions_len_jday_anoxia_rcp60 , label='GCMs', alpha=0.7, color=colors[0], edgecolor='black')
axs[1, 1].fill_between(contributions_len_jday_anoxia_rcp60_years, gcm_contributions_len_jday_anoxia_rcp60 , gcm_contributions_len_jday_anoxia_rcp60 + param_contributions_len_jday_anoxia_rcp60, label='Parameters', alpha=0.7, color=colors[1], edgecolor='black')
axs[1, 1].fill_between(contributions_len_jday_anoxia_rcp60_years, gcm_contributions_len_jday_anoxia_rcp60  + param_contributions_len_jday_anoxia_rcp60, gcm_contributions_len_jday_anoxia_rcp60 + param_contributions_len_jday_anoxia_rcp60 + interact_contributions_len_jday_anoxia_rcp60, label='Interactions', alpha=0.7, color=colors[2], edgecolor='black')
axs[1, 1].set_title('Duration of full anoxia profile in RCP6.0', fontsize=20)
axs[1, 1].set_ylim(0,100)
axs[1, 1].set_xlim(2006, 2099)
axs[1, 1].tick_params(axis='both', which='major', labelsize=20)




axs[2, 0].fill_between(contributions_first_jday_anoxia_rcp85_years, 0, gcm_contributions_first_jday_anoxia_rcp85 , label='GCMs', alpha=0.7, color=colors[0], edgecolor='black')
axs[2, 0].fill_between(contributions_first_jday_anoxia_rcp85_years, gcm_contributions_first_jday_anoxia_rcp85 , gcm_contributions_first_jday_anoxia_rcp85 + param_contributions_first_jday_anoxia_rcp85, label='Parameters', alpha=0.7, color=colors[1], edgecolor='black')
axs[2, 0].fill_between(contributions_first_jday_anoxia_rcp85_years, gcm_contributions_first_jday_anoxia_rcp85  + param_contributions_first_jday_anoxia_rcp85, gcm_contributions_first_jday_anoxia_rcp85 + param_contributions_first_jday_anoxia_rcp85 + interact_contributions_first_jday_anoxia_rcp85, label='Interactions', alpha=0.7, color=colors[2], edgecolor='black')
axs[2, 0].set_title('First day of full anoxia profile in RCP8.5', fontsize=20)
axs[2, 0].set_ylim(0,100)
axs[2, 0].set_xlim(2006, 2099)
axs[2, 0].tick_params(axis='both', which='major', labelsize=20)



axs[2, 1].fill_between(contributions_len_jday_anoxia_rcp85_years, 0, gcm_contributions_len_jday_anoxia_rcp85 , label='GCMs', alpha=0.7, color=colors[0], edgecolor='black')
axs[2, 1].fill_between(contributions_len_jday_anoxia_rcp85_years, gcm_contributions_len_jday_anoxia_rcp85 , gcm_contributions_len_jday_anoxia_rcp85 + param_contributions_len_jday_anoxia_rcp85, label='Parameters', alpha=0.7, color=colors[1], edgecolor='black')
axs[2, 1].fill_between(contributions_len_jday_anoxia_rcp85_years, gcm_contributions_len_jday_anoxia_rcp85  + param_contributions_len_jday_anoxia_rcp85, gcm_contributions_len_jday_anoxia_rcp85 + param_contributions_len_jday_anoxia_rcp85 + interact_contributions_len_jday_anoxia_rcp85, label='Interactions', alpha=0.7, color=colors[2], edgecolor='black')
axs[2, 1].set_title('Duration of full anoxia profile in RCP8.5', fontsize=20)
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
plt.savefig('uncertainty_first_len_full_anoxia_duration_allyears_rcps.png', dpi=300, bbox_inches='tight')

plt.show()


#%% Uncertainity of 80 years in RCPs

#first_jday_anoxia_rcp26

#years
contributions_first_jday_anoxia_rcp26_years=anova_first_jday_anoxia_full_prof_rcp26[anova_first_jday_anoxia_full_prof_rcp26['year']>2019]['year']
#GCMs
gcm_contributions_first_jday_anoxia_rcp26= anova_first_jday_anoxia_full_prof_rcp26[anova_first_jday_anoxia_full_prof_rcp26['year']>2019]['GCMs']
#Param
param_contributions_first_jday_anoxia_rcp26=anova_first_jday_anoxia_full_prof_rcp26[anova_first_jday_anoxia_full_prof_rcp26['year']>2019]['param']
#interaction
interact_contributions_first_jday_anoxia_rcp26 =anova_first_jday_anoxia_full_prof_rcp26[anova_first_jday_anoxia_full_prof_rcp26['year']>2019]['interaction']


#len_jday_anoxia_rcp26

#years
contributions_len_jday_anoxia_rcp26_years=anova_len_jday_anoxia_full_prof_rcp26[anova_len_jday_anoxia_full_prof_rcp26['year']>2019]['year']
#GCMs
gcm_contributions_len_jday_anoxia_rcp26= anova_len_jday_anoxia_full_prof_rcp26[anova_len_jday_anoxia_full_prof_rcp26['year']>2019]['GCMs']
#Param
param_contributions_len_jday_anoxia_rcp26=anova_len_jday_anoxia_full_prof_rcp26[anova_len_jday_anoxia_full_prof_rcp26['year']>2019]['param']
#interaction
interact_contributions_len_jday_anoxia_rcp26 =anova_len_jday_anoxia_full_prof_rcp26[anova_len_jday_anoxia_full_prof_rcp26['year']>2019]['interaction']


     

#first_jday_anoxia_rcp60

#years
contributions_first_jday_anoxia_rcp60_years=anova_first_jday_anoxia_full_prof_rcp60[anova_first_jday_anoxia_full_prof_rcp60['year']>2019]['year']
#GCMs
gcm_contributions_first_jday_anoxia_rcp60= anova_first_jday_anoxia_full_prof_rcp60[anova_first_jday_anoxia_full_prof_rcp60['year']>2019]['GCMs']
#Param
param_contributions_first_jday_anoxia_rcp60=anova_first_jday_anoxia_full_prof_rcp60[anova_first_jday_anoxia_full_prof_rcp60['year']>2019]['param']
#interaction
interact_contributions_first_jday_anoxia_rcp60 =anova_first_jday_anoxia_full_prof_rcp60[anova_first_jday_anoxia_full_prof_rcp60['year']>2019]['interaction']


#len_jday_anoxia_rcp60

#years
contributions_len_jday_anoxia_rcp60_years=anova_len_jday_anoxia_full_prof_rcp60[anova_len_jday_anoxia_full_prof_rcp60['year']>2019]['year']
#GCMs
gcm_contributions_len_jday_anoxia_rcp60= anova_len_jday_anoxia_full_prof_rcp60[anova_len_jday_anoxia_full_prof_rcp60['year']>2019]['GCMs']
#Param
param_contributions_len_jday_anoxia_rcp60=anova_len_jday_anoxia_full_prof_rcp60[anova_len_jday_anoxia_full_prof_rcp60['year']>2019]['param']
#interaction
interact_contributions_len_jday_anoxia_rcp60 =anova_len_jday_anoxia_full_prof_rcp60[anova_len_jday_anoxia_full_prof_rcp60['year']>2019]['interaction']


#first_jday_anoxia_rcp85

#years
contributions_first_jday_anoxia_rcp85_years=anova_first_jday_anoxia_full_prof_rcp85[anova_first_jday_anoxia_full_prof_rcp85['year']>2019]['year']
#GCMs
gcm_contributions_first_jday_anoxia_rcp85= anova_first_jday_anoxia_full_prof_rcp85[anova_first_jday_anoxia_full_prof_rcp85['year']>2019]['GCMs']
#Param
param_contributions_first_jday_anoxia_rcp85=anova_first_jday_anoxia_full_prof_rcp85[anova_first_jday_anoxia_full_prof_rcp85['year']>2019]['param']
#interaction
interact_contributions_first_jday_anoxia_rcp85 =anova_first_jday_anoxia_full_prof_rcp85[anova_first_jday_anoxia_full_prof_rcp85['year']>2019]['interaction']


#len_jday_anoxia_rcp85

#years
contributions_len_jday_anoxia_rcp85_years=anova_len_jday_anoxia_full_prof_rcp85[anova_len_jday_anoxia_full_prof_rcp85['year']>2019]['year']
#GCMs
gcm_contributions_len_jday_anoxia_rcp85= anova_len_jday_anoxia_full_prof_rcp85[anova_len_jday_anoxia_full_prof_rcp85['year']>2019]['GCMs']
#Param
param_contributions_len_jday_anoxia_rcp85=anova_len_jday_anoxia_full_prof_rcp85[anova_len_jday_anoxia_full_prof_rcp85['year']>2019]['param']
#interaction
interact_contributions_len_jday_anoxia_rcp85 =anova_len_jday_anoxia_full_prof_rcp85[anova_len_jday_anoxia_full_prof_rcp85['year']>2019]['interaction']



#%%For all RCPs  80 years 

# Define the directory path
directory_path = r'C:\Users\mahta\OneDrive\Documents\Chapter_1_PhD_py_codes_results\Future_simulation_results\all_4_models\uncertainty'

# Change the current working directory
os.chdir(directory_path)     
    

import matplotlib.pyplot as plt
from matplotlib.patches import Patch

# Define colors explicitly as RGB tuples
colors = [(0.96, 0.80, 0.69), (0.6, 0.4, 0.8), (0, 0, 1)]  # Flesh, Dark Orchid, Blue

# Create a figure with three subplots
fig, axs = plt.subplots(3, 2, figsize=(20, 15), sharey=True, sharex=True)

axs[0, 0].fill_between(contributions_first_jday_anoxia_rcp26_years, 0, gcm_contributions_first_jday_anoxia_rcp26 , label='GCMs', alpha=0.7, color=colors[0], edgecolor='black')
axs[0, 0].fill_between(contributions_first_jday_anoxia_rcp26_years, gcm_contributions_first_jday_anoxia_rcp26 , gcm_contributions_first_jday_anoxia_rcp26 + param_contributions_first_jday_anoxia_rcp26, label='Parameters', alpha=0.7, color=colors[1], edgecolor='black')
axs[0, 0].fill_between(contributions_first_jday_anoxia_rcp26_years, gcm_contributions_first_jday_anoxia_rcp26  + param_contributions_first_jday_anoxia_rcp26, gcm_contributions_first_jday_anoxia_rcp26 + param_contributions_first_jday_anoxia_rcp26 + interact_contributions_first_jday_anoxia_rcp26, label='Interactions', alpha=0.7, color=colors[2], edgecolor='black')
axs[0, 0].set_title('First day of full anoxia profile in RCP2.6', fontsize=20)
axs[0, 0].set_ylim(0,100)
axs[0, 0].set_xlim(2020, 2099)
axs[0, 0].tick_params(axis='both', which='major', labelsize=20)



axs[0, 1].fill_between(contributions_len_jday_anoxia_rcp26_years, 0, gcm_contributions_len_jday_anoxia_rcp26 , label='GCMs', alpha=0.7, color=colors[0], edgecolor='black')
axs[0, 1].fill_between(contributions_len_jday_anoxia_rcp26_years, gcm_contributions_len_jday_anoxia_rcp26 , gcm_contributions_len_jday_anoxia_rcp26 + param_contributions_len_jday_anoxia_rcp26, label='Parameters', alpha=0.7, color=colors[1], edgecolor='black')
axs[0, 1].fill_between(contributions_len_jday_anoxia_rcp26_years, gcm_contributions_len_jday_anoxia_rcp26  + param_contributions_len_jday_anoxia_rcp26, gcm_contributions_len_jday_anoxia_rcp26 + param_contributions_len_jday_anoxia_rcp26 + interact_contributions_len_jday_anoxia_rcp26, label='Interactions', alpha=0.7, color=colors[2], edgecolor='black')
axs[0, 1].set_title('Duration of full anoxia profile in RCP2.6', fontsize=20)
axs[0, 1].set_ylim(0,100)
axs[0, 1].set_xlim(2020, 2099)
axs[0, 1].tick_params(axis='both', which='major', labelsize=20)

axs[1, 0].fill_between(contributions_first_jday_anoxia_rcp60_years, 0, gcm_contributions_first_jday_anoxia_rcp60 , label='GCMs', alpha=0.7, color=colors[0], edgecolor='black')
axs[1, 0].fill_between(contributions_first_jday_anoxia_rcp60_years, gcm_contributions_first_jday_anoxia_rcp60 , gcm_contributions_first_jday_anoxia_rcp60 + param_contributions_first_jday_anoxia_rcp60, label='Parameters', alpha=0.7, color=colors[1], edgecolor='black')
axs[1, 0].fill_between(contributions_first_jday_anoxia_rcp60_years, gcm_contributions_first_jday_anoxia_rcp60  + param_contributions_first_jday_anoxia_rcp60, gcm_contributions_first_jday_anoxia_rcp60 + param_contributions_first_jday_anoxia_rcp60 + interact_contributions_first_jday_anoxia_rcp60, label='Interactions', alpha=0.7, color=colors[2], edgecolor='black')
axs[1, 0].set_title('First day of full anoxia profile in RCP6.0', fontsize=20)
axs[1, 0].set_ylim(0,100)
axs[1, 0].set_xlim(2020, 2099)
axs[1, 0].tick_params(axis='both', which='major', labelsize=20)



axs[1, 1].fill_between(contributions_len_jday_anoxia_rcp60_years, 0, gcm_contributions_len_jday_anoxia_rcp60 , label='GCMs', alpha=0.7, color=colors[0], edgecolor='black')
axs[1, 1].fill_between(contributions_len_jday_anoxia_rcp60_years, gcm_contributions_len_jday_anoxia_rcp60 , gcm_contributions_len_jday_anoxia_rcp60 + param_contributions_len_jday_anoxia_rcp60, label='Parameters', alpha=0.7, color=colors[1], edgecolor='black')
axs[1, 1].fill_between(contributions_len_jday_anoxia_rcp60_years, gcm_contributions_len_jday_anoxia_rcp60  + param_contributions_len_jday_anoxia_rcp60, gcm_contributions_len_jday_anoxia_rcp60 + param_contributions_len_jday_anoxia_rcp60 + interact_contributions_len_jday_anoxia_rcp60, label='Interactions', alpha=0.7, color=colors[2], edgecolor='black')
axs[1, 1].set_title('Duration of full anoxia profile in RCP6.0', fontsize=20)
axs[1, 1].set_ylim(0,100)
axs[1, 1].set_xlim(2020, 2099)
axs[1, 1].tick_params(axis='both', which='major', labelsize=20)




axs[2, 0].fill_between(contributions_first_jday_anoxia_rcp85_years, 0, gcm_contributions_first_jday_anoxia_rcp85 , label='GCMs', alpha=0.7, color=colors[0], edgecolor='black')
axs[2, 0].fill_between(contributions_first_jday_anoxia_rcp85_years, gcm_contributions_first_jday_anoxia_rcp85 , gcm_contributions_first_jday_anoxia_rcp85 + param_contributions_first_jday_anoxia_rcp85, label='Parameters', alpha=0.7, color=colors[1], edgecolor='black')
axs[2, 0].fill_between(contributions_first_jday_anoxia_rcp85_years, gcm_contributions_first_jday_anoxia_rcp85  + param_contributions_first_jday_anoxia_rcp85, gcm_contributions_first_jday_anoxia_rcp85 + param_contributions_first_jday_anoxia_rcp85 + interact_contributions_first_jday_anoxia_rcp85, label='Interactions', alpha=0.7, color=colors[2], edgecolor='black')
axs[2, 0].set_title('First day of full anoxia profile in RCP8.5', fontsize=20)
axs[2, 0].set_ylim(0,100)
axs[2, 0].set_xlim(2020, 2099)
axs[2, 0].tick_params(axis='both', which='major', labelsize=20)



axs[2, 1].fill_between(contributions_len_jday_anoxia_rcp85_years, 0, gcm_contributions_len_jday_anoxia_rcp85 , label='GCMs', alpha=0.7, color=colors[0], edgecolor='black')
axs[2, 1].fill_between(contributions_len_jday_anoxia_rcp85_years, gcm_contributions_len_jday_anoxia_rcp85 , gcm_contributions_len_jday_anoxia_rcp85 + param_contributions_len_jday_anoxia_rcp85, label='Parameters', alpha=0.7, color=colors[1], edgecolor='black')
axs[2, 1].fill_between(contributions_len_jday_anoxia_rcp85_years, gcm_contributions_len_jday_anoxia_rcp85  + param_contributions_len_jday_anoxia_rcp85, gcm_contributions_len_jday_anoxia_rcp85 + param_contributions_len_jday_anoxia_rcp85 + interact_contributions_len_jday_anoxia_rcp85, label='Interactions', alpha=0.7, color=colors[2], edgecolor='black')
axs[2, 1].set_title('Duration of full anoxia profile in RCP8.5', fontsize=20)
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
plt.savefig('uncertainty_first_len_full_anoxia_duration_allyears_rcps_80years.png', dpi=300, bbox_inches='tight')

plt.show()


#%%#
#=====================================GLUE ============================

#%%his

# first_jday_anoxia_full_prof_inyear_his
timeseries_year_his= all_first_jday_anoxia_full_prof_inyear_his.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_first_jday_anoxia_full_prof_inyear_his.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights_his))

# Build glue df
glue_first_jday_anoxia_full_prof_inyear_his = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_first_jday_anoxia_full_prof_inyear_his=glue_first_jday_anoxia_full_prof_inyear_his.set_index(timeseries_year_his)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory
glue_first_jday_anoxia_full_prof_inyear_his.to_csv('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/all_4_models/his/glue_first_jday_anoxia_full_prof_inyear_his.csv')



# last_jday_anoxia_full_prof_inyear_his
timeseries_year_his= all_last_jday_anoxia_full_prof_inyear_his.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_last_jday_anoxia_full_prof_inyear_his.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights_his))

# Build glue df
glue_last_jday_anoxia_full_prof_inyear_his = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_last_jday_anoxia_full_prof_inyear_his=glue_last_jday_anoxia_full_prof_inyear_his.set_index(timeseries_year_his)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory
glue_last_jday_anoxia_full_prof_inyear_his.to_csv('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/all_4_models/his/glue_last_jday_anoxia_full_prof_inyear_his.csv')

           

# len_anoxia_full_prof_inyear_his
timeseries_year_his= all_len_anoxia_full_prof_inyear_his.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_len_anoxia_full_prof_inyear_his.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights_his))

# Build glue df
glue_len_anoxia_full_prof_inyear_his = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_len_anoxia_full_prof_inyear_his=glue_len_anoxia_full_prof_inyear_his.set_index(timeseries_year_his)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory
glue_len_anoxia_full_prof_inyear_his.to_csv('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/all_4_models/his/glue_len_anoxia_full_prof_inyear_his.csv')


#%%rcp26

# first_jday_anoxia_full_prof_inyear_rcp26
timeseries_year_rcp26= all_first_jday_anoxia_full_prof_inyear_rcp26.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_first_jday_anoxia_full_prof_inyear_rcp26.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights_rcp26))

# Build glue df
glue_first_jday_anoxia_full_prof_inyear_rcp26 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_first_jday_anoxia_full_prof_inyear_rcp26=glue_first_jday_anoxia_full_prof_inyear_rcp26.set_index(timeseries_year_rcp26)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory
glue_first_jday_anoxia_full_prof_inyear_rcp26.to_csv('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/all_4_models/rcp26/glue_first_jday_anoxia_full_prof_inyear_rcp26.csv')



# last_jday_anoxia_full_prof_inyear_rcp26
timeseries_year_rcp26= all_last_jday_anoxia_full_prof_inyear_rcp26.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_last_jday_anoxia_full_prof_inyear_rcp26.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights_rcp26))

# Build glue df
glue_last_jday_anoxia_full_prof_inyear_rcp26 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_last_jday_anoxia_full_prof_inyear_rcp26=glue_last_jday_anoxia_full_prof_inyear_rcp26.set_index(timeseries_year_rcp26)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory
glue_last_jday_anoxia_full_prof_inyear_rcp26.to_csv('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/all_4_models/rcp26/glue_last_jday_anoxia_full_prof_inyear_rcp26.csv')

           

# len_anoxia_full_prof_inyear_rcp26
timeseries_year_rcp26= all_len_anoxia_full_prof_inyear_rcp26.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_len_anoxia_full_prof_inyear_rcp26.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights_rcp26))

# Build glue df
glue_len_anoxia_full_prof_inyear_rcp26 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_len_anoxia_full_prof_inyear_rcp26=glue_len_anoxia_full_prof_inyear_rcp26.set_index(timeseries_year_rcp26)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory
glue_len_anoxia_full_prof_inyear_rcp26.to_csv('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/all_4_models/rcp26/glue_len_anoxia_full_prof_inyear_rcp26.csv')


#%%rcp60

# first_jday_anoxia_full_prof_inyear_rcp60
timeseries_year_rcp60= all_first_jday_anoxia_full_prof_inyear_rcp60.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_first_jday_anoxia_full_prof_inyear_rcp60.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights_rcp60))

# Build glue df
glue_first_jday_anoxia_full_prof_inyear_rcp60 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_first_jday_anoxia_full_prof_inyear_rcp60=glue_first_jday_anoxia_full_prof_inyear_rcp60.set_index(timeseries_year_rcp60)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory
glue_first_jday_anoxia_full_prof_inyear_rcp60.to_csv('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/all_4_models/rcp60/glue_first_jday_anoxia_full_prof_inyear_rcp60.csv')



# last_jday_anoxia_full_prof_inyear_rcp60
timeseries_year_rcp60= all_last_jday_anoxia_full_prof_inyear_rcp60.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_last_jday_anoxia_full_prof_inyear_rcp60.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights_rcp60))

# Build glue df
glue_last_jday_anoxia_full_prof_inyear_rcp60 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_last_jday_anoxia_full_prof_inyear_rcp60=glue_last_jday_anoxia_full_prof_inyear_rcp60.set_index(timeseries_year_rcp60)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory
glue_last_jday_anoxia_full_prof_inyear_rcp60.to_csv('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/all_4_models/rcp60/glue_last_jday_anoxia_full_prof_inyear_rcp60.csv')

           

# len_anoxia_full_prof_inyear_rcp60
timeseries_year_rcp60= all_len_anoxia_full_prof_inyear_rcp60.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_len_anoxia_full_prof_inyear_rcp60.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights_rcp60))

# Build glue df
glue_len_anoxia_full_prof_inyear_rcp60 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_len_anoxia_full_prof_inyear_rcp60=glue_len_anoxia_full_prof_inyear_rcp60.set_index(timeseries_year_rcp60)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory
glue_len_anoxia_full_prof_inyear_rcp60.to_csv('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/all_4_models/rcp60/glue_len_anoxia_full_prof_inyear_rcp60.csv')

#%%rcp85

# first_jday_anoxia_full_prof_inyear_rcp85
timeseries_year_rcp85= all_first_jday_anoxia_full_prof_inyear_rcp85.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_first_jday_anoxia_full_prof_inyear_rcp85.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights_rcp85))

# Build glue df
glue_first_jday_anoxia_full_prof_inyear_rcp85 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_first_jday_anoxia_full_prof_inyear_rcp85=glue_first_jday_anoxia_full_prof_inyear_rcp85.set_index(timeseries_year_rcp85)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory
glue_first_jday_anoxia_full_prof_inyear_rcp85.to_csv('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/all_4_models/rcp85/glue_first_jday_anoxia_full_prof_inyear_rcp85.csv')



# last_jday_anoxia_full_prof_inyear_rcp85
timeseries_year_rcp85= all_last_jday_anoxia_full_prof_inyear_rcp85.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_last_jday_anoxia_full_prof_inyear_rcp85.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights_rcp85))

# Build glue df
glue_last_jday_anoxia_full_prof_inyear_rcp85 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_last_jday_anoxia_full_prof_inyear_rcp85=glue_last_jday_anoxia_full_prof_inyear_rcp85.set_index(timeseries_year_rcp85)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory
glue_last_jday_anoxia_full_prof_inyear_rcp85.to_csv('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/all_4_models/rcp85/glue_last_jday_anoxia_full_prof_inyear_rcp85.csv')

           

# len_anoxia_full_prof_inyear_rcp85
timeseries_year_rcp85= all_len_anoxia_full_prof_inyear_rcp85.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_len_anoxia_full_prof_inyear_rcp85.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights_rcp85))

# Build glue df
glue_len_anoxia_full_prof_inyear_rcp85 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_len_anoxia_full_prof_inyear_rcp85=glue_len_anoxia_full_prof_inyear_rcp85.set_index(timeseries_year_rcp85)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory
glue_len_anoxia_full_prof_inyear_rcp85.to_csv('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/all_4_models/rcp85/glue_len_anoxia_full_prof_inyear_rcp85.csv')

#%%Sorting the glue dataframe according to the index (year)

glue_len_anoxia_full_prof_inyear_his=glue_len_anoxia_full_prof_inyear_his.sort_index()

glue_len_anoxia_full_prof_inyear_rcp26=glue_len_anoxia_full_prof_inyear_rcp26.sort_index()

glue_len_anoxia_full_prof_inyear_rcp60=glue_len_anoxia_full_prof_inyear_rcp60.sort_index()

glue_len_anoxia_full_prof_inyear_rcp85=glue_len_anoxia_full_prof_inyear_rcp85.sort_index()


#%%Plotiing%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

#%%duration of full anoxia profile 



os.chdir('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/all_4_models/')

import matplotlib.pyplot as plt

fig =plt.figure(figsize=(15, 10))
ax= plt.subplot(111)


ax=plt.fill_between(glue_len_anoxia_full_prof_inyear_his.index.astype(float), glue_len_anoxia_full_prof_inyear_his['5%'], glue_len_anoxia_full_prof_inyear_his['95%'], color='grey', alpha=0.2 ,  label= 'His 90% CI')
ax=plt.plot(glue_len_anoxia_full_prof_inyear_his.index.astype(float), glue_len_anoxia_full_prof_inyear_his['50%'].astype(float), 'k', label='His median', alpha=0.9, linewidth=3  )


ax=plt.fill_between(glue_len_anoxia_full_prof_inyear_rcp26.index.astype(float), glue_len_anoxia_full_prof_inyear_rcp26['5%'], glue_len_anoxia_full_prof_inyear_rcp26['95%'], color='green', alpha=0.3 ,  label= 'RCP2.6 90% CI')
ax=plt.plot(glue_len_anoxia_full_prof_inyear_rcp26.index.astype(float), glue_len_anoxia_full_prof_inyear_rcp26['50%'].astype(float), 'darkgreen', label='RCP2.6 median', alpha=0.9, linewidth=3  )

ax=plt.fill_between(glue_len_anoxia_full_prof_inyear_rcp60.index.astype(float), glue_len_anoxia_full_prof_inyear_rcp60['5%'], glue_len_anoxia_full_prof_inyear_rcp60['95%'], color='yellow', alpha=0.4 ,  label= 'RCP6.0 90% CI')
ax=plt.plot(glue_len_anoxia_full_prof_inyear_rcp60.index.astype(float), glue_len_anoxia_full_prof_inyear_rcp60['50%'].astype(float), 'yellow', label='RCP6.0 median', alpha=0.9, linewidth=3  )

ax=plt.fill_between(glue_len_anoxia_full_prof_inyear_rcp85.index.astype(float), glue_len_anoxia_full_prof_inyear_rcp85['5%'], glue_len_anoxia_full_prof_inyear_rcp85['95%'], color='red', alpha=0.2 ,  label= 'RCP8.5 90% CI')
ax=plt.plot(glue_len_anoxia_full_prof_inyear_rcp85.index.astype(float), glue_len_anoxia_full_prof_inyear_rcp85['50%'].astype(float), 'r', label='RCP8.5 median', alpha=0.9, linewidth=3  )

ax=plt.ylabel('Duration of full deep anoxia [d]' , fontsize=26)
ax=plt.xlabel('Year' , fontsize=26)
ax=plt.yticks(fontsize= 22)
ax=plt.xticks(rotation=45 , fontsize=22)
ax=plt.legend(bbox_to_anchor=(1.1, -0.2), fontsize=22 , ncol=4)#)   
fig.savefig("GLUE_Timeseries_length_full_anoxia_16combinationJaJv_ave_obs_4models_4scenarios.png",  dpi=300, bbox_inches='tight')



#%%
np.mean(glue_len_anoxia_full_prof_inyear_his['50%'])#39.23605957824561
np.mean(glue_len_anoxia_full_prof_inyear_rcp26['50%'])#53.75153736806038
np.mean(glue_len_anoxia_full_prof_inyear_rcp60['50%'])#56.402314939756636
np.mean(glue_len_anoxia_full_prof_inyear_rcp85['50%'])#61.32468404813171

#%%anoxia_factor 30 yerars from each scenarios compare 



#anomaly 
# baseline [1976-2005]
len_anoxia_full_prof_inyear_ref=glue_len_anoxia_full_prof_inyear_his[1975 < glue_len_anoxia_full_prof_inyear_his.index]['50%'].mean()
#40.101850467553234
glue_len_anoxia_full_prof_inyear_his[1975 < glue_len_anoxia_full_prof_inyear_his.index]['5%'].mean()
#21.61227554851154
glue_len_anoxia_full_prof_inyear_his[1975 < glue_len_anoxia_full_prof_inyear_his.index]['95%'].mean()
#63.719311778284485

##std

(63.719311778284485- 21.61227554851154)/(2*1.645)
#12.798491255250134




#near future [2030-2059] # maximum temp in 2033

glue_len_anoxia_full_prof_inyear_rcp26[(2029 < glue_len_anoxia_full_prof_inyear_rcp26.index) & (glue_len_anoxia_full_prof_inyear_rcp26.index < 2060)]['50%'].mean()
# 55.019228562850785

glue_len_anoxia_full_prof_inyear_rcp26[(2029 < glue_len_anoxia_full_prof_inyear_rcp26.index) & (glue_len_anoxia_full_prof_inyear_rcp26.index < 2060)]['5%'].mean()
#33.84526433702516

glue_len_anoxia_full_prof_inyear_rcp26[(2029 < glue_len_anoxia_full_prof_inyear_rcp26.index) & (glue_len_anoxia_full_prof_inyear_rcp26.index < 2060)]['95%'].mean()
#80.2622881068591

##std
(80.2622881068591-33.84526433702516)/(2*1.645)
#14.108517863171413






glue_len_anoxia_full_prof_inyear_rcp60[(2029 < glue_len_anoxia_full_prof_inyear_rcp60.index) & (glue_len_anoxia_full_prof_inyear_rcp60.index < 2060)]['50%'].mean()
# 53.189590898330934
glue_len_anoxia_full_prof_inyear_rcp60[(2029 < glue_len_anoxia_full_prof_inyear_rcp60.index) & (glue_len_anoxia_full_prof_inyear_rcp60.index < 2060)]['5%'].mean()
#33.48796564552809
glue_len_anoxia_full_prof_inyear_rcp60[(2029 < glue_len_anoxia_full_prof_inyear_rcp60.index) & (glue_len_anoxia_full_prof_inyear_rcp60.index < 2060)]['95%'].mean()
#75.1

####std
(75.1-33.48796564552809)/(2*1.645)
#12.648034758198147





glue_len_anoxia_full_prof_inyear_rcp85[(2029 < glue_len_anoxia_full_prof_inyear_rcp85.index) & (glue_len_anoxia_full_prof_inyear_rcp85.index < 2060)]['50%'].mean()
# 56.605652169077835
glue_len_anoxia_full_prof_inyear_rcp85[(2029 < glue_len_anoxia_full_prof_inyear_rcp85.index) & (glue_len_anoxia_full_prof_inyear_rcp85.index < 2060)]['5%'].mean()
#33.32737436379205
glue_len_anoxia_full_prof_inyear_rcp85[(2029 < glue_len_anoxia_full_prof_inyear_rcp85.index) & (glue_len_anoxia_full_prof_inyear_rcp85.index < 2060)]['95%'].mean()
#85.13333333333334
###std
(85.13333333333334-33.32737436379205)/(2*1.645)
#15.74649208800647


 
#Distant future [2070-2099]

glue_len_anoxia_full_prof_inyear_rcp26[(2069 < glue_len_anoxia_full_prof_inyear_rcp26.index) & (glue_len_anoxia_full_prof_inyear_rcp26.index < 2100)]['50%'].mean()
# 55.17751141374097
glue_len_anoxia_full_prof_inyear_rcp26[(2069 < glue_len_anoxia_full_prof_inyear_rcp26.index) & (glue_len_anoxia_full_prof_inyear_rcp26.index < 2100)]['5%'].mean()
# 34.96624789349128
glue_len_anoxia_full_prof_inyear_rcp26[(2069 < glue_len_anoxia_full_prof_inyear_rcp26.index) & (glue_len_anoxia_full_prof_inyear_rcp26.index < 2100)]['95%'].mean()
# 89.9096510081569
###std
(89.9096510081569-34.96624789349128)/(2*1.645)
#16.70012252725399



glue_len_anoxia_full_prof_inyear_rcp60[(2069 < glue_len_anoxia_full_prof_inyear_rcp60.index) & (glue_len_anoxia_full_prof_inyear_rcp60.index< 2100)]['50%'].mean()
# 64.53254321830363
glue_len_anoxia_full_prof_inyear_rcp60[(2069 < glue_len_anoxia_full_prof_inyear_rcp60.index) & (glue_len_anoxia_full_prof_inyear_rcp60.index< 2100)]['5%'].mean()
# 44.62131132673158
glue_len_anoxia_full_prof_inyear_rcp60[(2069 < glue_len_anoxia_full_prof_inyear_rcp60.index) & (glue_len_anoxia_full_prof_inyear_rcp60.index< 2100)]['95%'].mean()
# 87.90959245636591
###std
(87.90959245636591-44.62131132673158)/(2*1.645)
#13.157532258247517




glue_len_anoxia_full_prof_inyear_rcp85[(2069 < glue_len_anoxia_full_prof_inyear_rcp85.index) & (glue_len_anoxia_full_prof_inyear_rcp85.index < 2100)]['50%'].mean()
#74.42301816738942
glue_len_anoxia_full_prof_inyear_rcp85[(2069 < glue_len_anoxia_full_prof_inyear_rcp85.index) & (glue_len_anoxia_full_prof_inyear_rcp85.index < 2100)]['5%'].mean()
#48.64650206806161           
glue_len_anoxia_full_prof_inyear_rcp85[(2069 < glue_len_anoxia_full_prof_inyear_rcp85.index) & (glue_len_anoxia_full_prof_inyear_rcp85.index < 2100)]['95%'].mean()
#108.16666666666667
###std
(108.16666666666667-48.64650206806161 )/(2*1.645)
#18.09123544030549


#%%Sorting the glue first_jday dataframe according to the index (year)


glue_first_jday_anoxia_full_prof_inyear_his=glue_first_jday_anoxia_full_prof_inyear_his.sort_index()

glue_first_jday_anoxia_full_prof_inyear_rcp26=glue_first_jday_anoxia_full_prof_inyear_rcp26.sort_index()

glue_first_jday_anoxia_full_prof_inyear_rcp60=glue_first_jday_anoxia_full_prof_inyear_rcp60.sort_index()

glue_first_jday_anoxia_full_prof_inyear_rcp85=glue_first_jday_anoxia_full_prof_inyear_rcp85.sort_index()

#%%replacing 0 with nan 

glue_first_jday_anoxia_full_prof_inyear_his=glue_first_jday_anoxia_full_prof_inyear_his.replace(0, np.nan)

glue_first_jday_anoxia_full_prof_inyear_rcp26=glue_first_jday_anoxia_full_prof_inyear_rcp26.replace(0, np.nan)

glue_first_jday_anoxia_full_prof_inyear_rcp60=glue_first_jday_anoxia_full_prof_inyear_rcp60.replace(0, np.nan)

glue_first_jday_anoxia_full_prof_inyear_rcp85=glue_first_jday_anoxia_full_prof_inyear_rcp85.replace(0, np.nan)




#%%80years 


glue_80years_len_anoxia_full_prof_inyear_rcp26=glue_len_anoxia_full_prof_inyear_rcp26[2019 < glue_len_anoxia_full_prof_inyear_rcp26.index]

glue_80years_len_anoxia_full_prof_inyear_rcp60=glue_len_anoxia_full_prof_inyear_rcp60[2019 < glue_len_anoxia_full_prof_inyear_rcp60.index]


glue_80years_len_anoxia_full_prof_inyear_rcp85=glue_len_anoxia_full_prof_inyear_rcp85[2019 < glue_len_anoxia_full_prof_inyear_rcp85.index]



autocorr_MK_org_modif_sens_slope_test(glue_80years_len_anoxia_full_prof_inyear_rcp26['50%'])
Out[1215]: 
(0.04904099909031567,
 'positively autocorrelated',
 'no trend',
 0.2358663670734389,
 0,
 0)

autocorr_MK_org_modif_sens_slope_test(glue_80years_len_anoxia_full_prof_inyear_rcp60['50%'])
Out[1216]: 
(0.016107830734467928,
 'positively autocorrelated',
 'increasing',
 4.780620344035924e-13,
 0.23944298174914783,
 47.84742146977578)

autocorr_MK_org_modif_sens_slope_test(glue_80years_len_anoxia_full_prof_inyear_rcp85['50%'])
Out[1217]: 
(0.028257055554346808,
 'positively autocorrelated',
 'increasing',
 3.774758283725532e-15,
 0.4011340945918508,
 46.65520326362189)






#%%len of full anoxia_anomaly 
os.chdir('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/all_4_models/')

import matplotlib.pyplot as plt

fig =plt.figure(figsize=(15, 11))
ax= plt.subplot(111)


ax=plt.fill_between(glue_len_anoxia_full_prof_inyear_his[1975 < glue_len_anoxia_full_prof_inyear_his.index].index.astype(float),
                      glue_len_anoxia_full_prof_inyear_his[1975 < glue_len_anoxia_full_prof_inyear_his.index]['5%'] - len_anoxia_full_prof_inyear_ref,
                      glue_len_anoxia_full_prof_inyear_his[1975 < glue_len_anoxia_full_prof_inyear_his.index ]['95%'] - len_anoxia_full_prof_inyear_ref,
                      color='grey', alpha=0.2, label='His 90% CI')


ax=plt.plot(glue_len_anoxia_full_prof_inyear_his[1975< glue_len_anoxia_full_prof_inyear_his.index ].index.astype(float),
            glue_len_anoxia_full_prof_inyear_his[1975 < glue_len_anoxia_full_prof_inyear_his.index]['50%'] - len_anoxia_full_prof_inyear_ref,
            'k', label='His median', alpha=0.9, linewidth=3   )

ax=plt.fill_between(glue_len_anoxia_full_prof_inyear_rcp26.index.astype(float), glue_len_anoxia_full_prof_inyear_rcp26['5%']-len_anoxia_full_prof_inyear_ref, glue_len_anoxia_full_prof_inyear_rcp26['95%']-len_anoxia_full_prof_inyear_ref, color='darkgreen', alpha=0.2 ,  label= 'RCP6.0 90% CI')
ax=plt.plot(glue_len_anoxia_full_prof_inyear_rcp26.index.astype(float), glue_len_anoxia_full_prof_inyear_rcp26['50%']-len_anoxia_full_prof_inyear_ref, 'darkgreen', label='RCP6.0 median', alpha=0.9, linewidth=3  )
                      
                     
ax=plt.fill_between(glue_len_anoxia_full_prof_inyear_rcp60.index.astype(float), glue_len_anoxia_full_prof_inyear_rcp60['5%']-len_anoxia_full_prof_inyear_ref, glue_len_anoxia_full_prof_inyear_rcp60['95%']-len_anoxia_full_prof_inyear_ref, color='yellow', alpha=0.4 ,  label= 'RCP6.0 90% CI')
ax=plt.plot(glue_len_anoxia_full_prof_inyear_rcp60.index.astype(float), glue_len_anoxia_full_prof_inyear_rcp60['50%']-len_anoxia_full_prof_inyear_ref, 'yellow', label='RCP6.0 median', alpha=0.9, linewidth=3  )
trendline_rcp60=autocorr_MK_org_modif_sens_slope_test(glue_80years_len_anoxia_full_prof_inyear_rcp60['50%']-len_anoxia_full_prof_inyear_ref)
ax=plt.text(2022,110, f'y = {trendline_rcp60[-2]:.3f}x + {trendline_rcp60[-1]:.3f},  p-value <0.0001', color='orange', fontsize= 24 )


ax=plt.plot(glue_80years_len_anoxia_full_prof_inyear_rcp60.index.astype(float),
        trendline_rcp60[-2] * np.arange(80) + trendline_rcp60[-1],
        linestyle='--', color='yellow', alpha=0.9, linewidth=3  , label='RCP6.0 trendline')





ax=plt.fill_between(glue_len_anoxia_full_prof_inyear_rcp85.index.astype(float), glue_len_anoxia_full_prof_inyear_rcp85['5%']-len_anoxia_full_prof_inyear_ref, glue_len_anoxia_full_prof_inyear_rcp85['95%']-len_anoxia_full_prof_inyear_ref, color='r', alpha=0.2 ,  label= 'RCP8.5 90% CI')
ax=plt.plot(glue_len_anoxia_full_prof_inyear_rcp85.index.astype(float), glue_len_anoxia_full_prof_inyear_rcp85['50%']-len_anoxia_full_prof_inyear_ref, 'r', label='RCP8.5 median', alpha=0.9, linewidth=3  )
trendline_rcp85=autocorr_MK_org_modif_sens_slope_test(glue_80years_len_anoxia_full_prof_inyear_rcp85['50%']-len_anoxia_full_prof_inyear_ref)
ax=plt.text(2022, 100, f'y = {trendline_rcp85[-2]:.3f}x + {trendline_rcp85[-1]:.3f},  p-value <0.0001', color='r', fontsize= 24 )


ax=plt.plot(glue_80years_len_anoxia_full_prof_inyear_rcp85.index.astype(float),
        trendline_rcp85[-2] * np.arange(80) + trendline_rcp85[-1],
        linestyle='--', color='r', alpha=0.7, linewidth=3  , label='RCP8.5 trendline')

ax=plt.axvline(x=2020, color='grey', linestyle='--')

ax=plt.text(1974, 132, 'n=64', color='k', fontsize= 24 )

ax=plt.ylabel('Anomaly of annual full-deep-water\n anoxia duration [d]' , fontsize=26)
ax=plt.xlabel('Year' , fontsize=26)
ax=plt.yticks(fontsize= 22)
ax=plt.xticks(rotation=45 , fontsize=22)
ax=plt.legend(bbox_to_anchor=(1, -0.2), fontsize=22, ncol=3)  
fig.savefig("GLUE_Timeseries_len_anoxia_full_prof_anomaly_16combinationJaJv_ave_obs_4models_4scenarios.png",  dpi=300, bbox_inches='tight')

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% condition ###############
#########################################################################

#%%Plotiing%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

#%%First Jday with full anoxia



os.chdir('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/all_4_models/')

import matplotlib.pyplot as plt

fig =plt.figure(figsize=(15, 10))
ax= plt.subplot(111)


ax=plt.fill_between(glue_first_jday_anoxia_full_prof_inyear_his.index.astype(float), glue_first_jday_anoxia_full_prof_inyear_his['5%'], glue_first_jday_anoxia_full_prof_inyear_his['95%'], color='grey', alpha=0.2 ,  label= 'His 90% CI')
ax=plt.plot(glue_first_jday_anoxia_full_prof_inyear_his.index.astype(float), glue_first_jday_anoxia_full_prof_inyear_his['50%'].astype(float), 'k', label='His median', alpha=0.9, linewidth=3  )


ax=plt.fill_between(glue_first_jday_anoxia_full_prof_inyear_rcp26.index.astype(float), glue_first_jday_anoxia_full_prof_inyear_rcp26['5%'], glue_first_jday_anoxia_full_prof_inyear_rcp26['95%'], color='darkgreen', alpha=0.2 ,  label= 'RCP2.6 90% CI')
ax=plt.plot(glue_first_jday_anoxia_full_prof_inyear_rcp26.index.astype(float), glue_first_jday_anoxia_full_prof_inyear_rcp26['50%'].astype(float), 'darkgreen', label='RCP2.6 median', alpha=0.9, linewidth=3  )

ax=plt.fill_between(glue_first_jday_anoxia_full_prof_inyear_rcp60.index.astype(float), glue_first_jday_anoxia_full_prof_inyear_rcp60['5%'], glue_first_jday_anoxia_full_prof_inyear_rcp60['95%'], color='yellow', alpha=0.2 ,  label= 'RCP6.0 90% CI')
ax=plt.plot(glue_first_jday_anoxia_full_prof_inyear_rcp60.index.astype(float), glue_first_jday_anoxia_full_prof_inyear_rcp60['50%'].astype(float), 'yellow', label='RCP6.0 median', alpha=0.9, linewidth=3  )

ax=plt.fill_between(glue_first_jday_anoxia_full_prof_inyear_rcp85.index.astype(float), glue_first_jday_anoxia_full_prof_inyear_rcp85['5%'], glue_first_jday_anoxia_full_prof_inyear_rcp85['95%'], color='red', alpha=0.2 ,  label= 'RCP8.5 90% CI')
ax=plt.plot(glue_first_jday_anoxia_full_prof_inyear_rcp85.index.astype(float), glue_first_jday_anoxia_full_prof_inyear_rcp85['50%'].astype(float), 'r', label='RCP8.5 median', alpha=0.9, linewidth=3  )

ax=plt.ylabel('First full deep anoxia [Jday]' , fontsize=26)
ax=plt.xlabel('Year' , fontsize=26)
ax=plt.yticks(fontsize= 22)
ax=plt.xticks(rotation=45 , fontsize=22)
ax=plt.legend(bbox_to_anchor=(1.1, -0.2), fontsize=22 , ncol=4)#)   
fig.savefig("GLUE_Timeseries_first_full_anoxia_16combinationJaJv_ave_obs_4models_4scenarios.png",  dpi=300, bbox_inches='tight')




#%%
np.mean(glue_first_jday_anoxia_full_prof_inyear_his['50%'])#202.09459785632947
np.mean(glue_first_jday_anoxia_full_prof_inyear_rcp26['50%'])#195.72238913786117
np.mean(glue_first_jday_anoxia_full_prof_inyear_rcp60['50%'])# 193.41007157743243
np.mean(glue_first_jday_anoxia_full_prof_inyear_rcp85['50%'])# 190.36549991086954

#%%anoxia_factor 30 yerars from each scenarios compare 


#anomaly 
# his [1976-2005]
first_jday_anoxia_full_prof_inyear_ref=glue_first_jday_anoxia_full_prof_inyear_his[1975< glue_first_jday_anoxia_full_prof_inyear_his.index]['50%'].mean()
#205.6613479175225


#near future [2030-205]

glue_first_jday_anoxia_full_prof_inyear_rcp26[(2029 < glue_first_jday_anoxia_full_prof_inyear_rcp26.index) & (glue_first_jday_anoxia_full_prof_inyear_rcp26.index < 2060)]['50%'].mean()
#195.0656623586102
glue_first_jday_anoxia_full_prof_inyear_rcp60[(2029 < glue_first_jday_anoxia_full_prof_inyear_rcp60.index) & (glue_first_jday_anoxia_full_prof_inyear_rcp60.index < 2060)]['50%'].mean()
#194.93333333333334
glue_first_jday_anoxia_full_prof_inyear_rcp85[(2029 < glue_first_jday_anoxia_full_prof_inyear_rcp85.index) & (glue_first_jday_anoxia_full_prof_inyear_rcp85.index < 2060)]['50%'].mean()
#192.89304143335247

 
#Distant future [2070-2099]

glue_first_jday_anoxia_full_prof_inyear_rcp26[(2069 < glue_first_jday_anoxia_full_prof_inyear_rcp26.index) & (glue_first_jday_anoxia_full_prof_inyear_rcp26.index < 2100)]['50%'].mean()
#194.78361891156072
glue_first_jday_anoxia_full_prof_inyear_rcp60[(2069 < glue_first_jday_anoxia_full_prof_inyear_rcp60.index) & (glue_first_jday_anoxia_full_prof_inyear_rcp60.index < 2100)]['50%'].mean()
#187.78512927508444
glue_first_jday_anoxia_full_prof_inyear_rcp85[(2069 < glue_first_jday_anoxia_full_prof_inyear_rcp85.index) & (glue_first_jday_anoxia_full_prof_inyear_rcp85.index < 2100)]['50%'].mean()
#183.73497044103513
           



#%%depletion_rate_anomaly 
os.chdir('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/all_4_models/')

import matplotlib.pyplot as plt

fig =plt.figure(figsize=(15, 10))
ax= plt.subplot(111)


ax=plt.fill_between(glue_first_jday_anoxia_full_prof_inyear_his[1975 < glue_first_jday_anoxia_full_prof_inyear_his.index].index.astype(float),
                      glue_first_jday_anoxia_full_prof_inyear_his[1975 < glue_first_jday_anoxia_full_prof_inyear_his.index]['5%'] - first_jday_anoxia_full_prof_inyear_ref,
                      glue_first_jday_anoxia_full_prof_inyear_his[1975 < glue_first_jday_anoxia_full_prof_inyear_his.index]['95%'] - first_jday_anoxia_full_prof_inyear_ref,
                      color='grey', alpha=0.2, label='His 90% CI')


ax=plt.plot(glue_first_jday_anoxia_full_prof_inyear_his[1975 < glue_first_jday_anoxia_full_prof_inyear_his.index ].index.astype(float),
            glue_first_jday_anoxia_full_prof_inyear_his[1975 < glue_first_jday_anoxia_full_prof_inyear_his.index]['50%'] - first_jday_anoxia_full_prof_inyear_ref,
            'k', label='His median', alpha=0.9, linewidth=3   )

ax=plt.fill_between(glue_first_jday_anoxia_full_prof_inyear_rcp26.index.astype(float), glue_first_jday_anoxia_full_prof_inyear_rcp26['5%']-first_jday_anoxia_full_prof_inyear_ref, glue_first_jday_anoxia_full_prof_inyear_rcp26['95%']-first_jday_anoxia_full_prof_inyear_ref, color='darkgreen', alpha=0.2 ,  label= 'RCP6.0 90% CI')
ax=plt.plot(glue_first_jday_anoxia_full_prof_inyear_rcp26.index.astype(float), glue_first_jday_anoxia_full_prof_inyear_rcp26['50%']-first_jday_anoxia_full_prof_inyear_ref, 'darkgreen', label='RCP6.0 median', alpha=0.9, linewidth=3  )
                      
                     
ax=plt.fill_between(glue_first_jday_anoxia_full_prof_inyear_rcp60.index.astype(float), glue_first_jday_anoxia_full_prof_inyear_rcp60['5%']-first_jday_anoxia_full_prof_inyear_ref, glue_first_jday_anoxia_full_prof_inyear_rcp60['95%']-first_jday_anoxia_full_prof_inyear_ref, color='yellow', alpha=0.3 ,  label= 'RCP6.0 90% CI')
ax=plt.plot(glue_first_jday_anoxia_full_prof_inyear_rcp60.index.astype(float), glue_first_jday_anoxia_full_prof_inyear_rcp60['50%']-first_jday_anoxia_full_prof_inyear_ref, 'yellow', label='RCP6.0 median', alpha=0.9, linewidth=3  )

ax=plt.fill_between(glue_first_jday_anoxia_full_prof_inyear_rcp85.index.astype(float), glue_first_jday_anoxia_full_prof_inyear_rcp85['5%']-first_jday_anoxia_full_prof_inyear_ref, glue_first_jday_anoxia_full_prof_inyear_rcp85['95%']-first_jday_anoxia_full_prof_inyear_ref, color='r', alpha=0.2 ,  label= 'RCP8.5 90% CI')
ax=plt.plot(glue_first_jday_anoxia_full_prof_inyear_rcp85.index.astype(float), glue_first_jday_anoxia_full_prof_inyear_rcp85['50%']-first_jday_anoxia_full_prof_inyear_ref, 'r', label='RCP8.5 median', alpha=0.9, linewidth=3  )

ax=plt.ylabel('Anomaly of full deep anoxia onset [Jday]' , fontsize=26)
ax=plt.xlabel('Year' , fontsize=26)
ax=plt.yticks(fontsize= 22)
ax=plt.xticks(rotation=45 , fontsize=22)
ax=plt.legend(bbox_to_anchor=(1.1, -0.2), fontsize=22 , ncol=4)  
fig.savefig("GLUE_Timeseries_first_jday_anoxia_full_prof_anomaly_16combinationJaJv_ave_obs_4models_4scenarios.png",  dpi=300, bbox_inches='tight')

#%% Histogram or violn plot 

    
median_first_jday_anoxia_full_prof_his=glue_first_jday_anoxia_full_prof_inyear_his['50%']
median_first_jday_anoxia_full_prof_rcp26=glue_first_jday_anoxia_full_prof_inyear_rcp26['50%']
median_first_jday_anoxia_full_prof_rcp60=glue_first_jday_anoxia_full_prof_inyear_rcp60['50%']
median_first_jday_anoxia_full_prof_rcp85=glue_first_jday_anoxia_full_prof_inyear_rcp85['50%']  
    
# Create a DataFrame with NaN values
df_first_jday_anoxia_full_prof_4models =pd.concat([
    pd.Series(median_first_jday_anoxia_full_prof_his, name='His' ),
    pd.Series(median_first_jday_anoxia_full_prof_rcp26, name='RCP2.6'),
    pd.Series(median_first_jday_anoxia_full_prof_rcp60, name='RCP6.0' ),
    pd.Series(median_first_jday_anoxia_full_prof_rcp85, name='RCP8.5' )], axis=1)    
    
    

    
median_len_anoxia_full_prof_his=glue_len_anoxia_full_prof_inyear_his['50%']
median_len_anoxia_full_prof_rcp26=glue_len_anoxia_full_prof_inyear_rcp26['50%']
median_len_anoxia_full_prof_rcp60=glue_len_anoxia_full_prof_inyear_rcp60['50%']
median_len_anoxia_full_prof_rcp85=glue_len_anoxia_full_prof_inyear_rcp85['50%']  
    
# Create a DataFrame with NaN values
df_len_anoxia_full_prof_4models =pd.concat([
    pd.Series(median_len_anoxia_full_prof_his, name='His' ),
    pd.Series(median_len_anoxia_full_prof_rcp26, name='RCP2.6'),
    pd.Series(median_len_anoxia_full_prof_rcp60, name='RCP6.0' ),
    pd.Series(median_len_anoxia_full_prof_rcp85, name='RCP8.5' )], axis=1)    
    
    
median_last_jday_anoxia_full_prof_his=glue_last_jday_anoxia_full_prof_inyear_his['50%']
median_last_jday_anoxia_full_prof_rcp26=glue_last_jday_anoxia_full_prof_inyear_rcp26['50%']
median_last_jday_anoxia_full_prof_rcp60=glue_last_jday_anoxia_full_prof_inyear_rcp60['50%']
median_last_jday_anoxia_full_prof_rcp85=glue_last_jday_anoxia_full_prof_inyear_rcp85['50%']  
    
# Create a DataFrame with NaN values
df_last_jday_anoxia_full_prof_4models =pd.concat([
    pd.Series(median_last_jday_anoxia_full_prof_his, name='His' ),
    pd.Series(median_last_jday_anoxia_full_prof_rcp26, name='RCP2.6'),
    pd.Series(median_last_jday_anoxia_full_prof_rcp60, name='RCP6.0' ),
    pd.Series(median_last_jday_anoxia_full_prof_rcp85, name='RCP8.5' )], axis=1)    
    
    
    


#%%
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

os.chdir ('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results')



# Set up the color palette
custom_palette = ['grey', 'darkgreen', 'yellow', 'red']

# Create subplots with space between them
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(10, 4))

# Adjust the width space between subplots
plt.subplots_adjust(wspace=0.3)
sns.violinplot(ax=axes[0], data=df_first_jday_anoxia_full_prof_4models, palette=custom_palette)
axes[0].set_ylabel('Full deep anoxia onset [Jday]')

#axes[0].set_ylim(60, 210)  # Set the y-axis limits
axes[0].set_yticks(range(120, 250, 30))  # Set the y-axis ticks at intervals of 20



plt.subplots_adjust(wspace=0.3)
sns.violinplot(ax=axes[1], data=df_len_anoxia_full_prof_4models, palette=custom_palette)
axes[1].set_ylabel('Full deep anoxia duration [day]')
axes[1].set_yticks(range(0, 150, 30))  # Set the y-axis ticks at intervals of 20



#sns.violinplot(ax=axes[2], data=df_last_jday_anoxia_full_prof_4models, palette=custom_palette)
#axes[2].set_ylabel('Last day of full deep anoxia [day]')
#axes[2].set_yticks(range(210, 280, 30))  # Set the y-axis ticks at intervals of 20



plt.savefig("allsenarios_4models_median_first_len_of_full_anoxia.png", dpi=300)







#%% averaging over whole scenarios value 
np.mean(glue_len_anoxia_full_prof_inyear_his['50%'])#39.2360595782456
np.mean(glue_len_anoxia_full_prof_inyear_rcp26['50%'])#53.75153736806038
np.mean(glue_len_anoxia_full_prof_inyear_rcp60['50%'])#56.402314939756636
np.mean(glue_len_anoxia_full_prof_inyear_rcp85['50%'])#61.32468404813171



#%%anoxia_duration 30 yerars from each scenarios compare 



#anomaly 
# baseline [1976-2005]
glue_base_len_anoxia_full_prof_his=glue_len_anoxia_full_prof_inyear_his[1975 < glue_len_anoxia_full_prof_inyear_his.index]['50%']
len_anoxia_full_prof_ref=np.mean(glue_base_len_anoxia_full_prof_his)
# 40.101850467553234


#near future [2030-2059]

glue_near_future_len_anoxia_full_prof_rcp26=glue_len_anoxia_full_prof_inyear_rcp26[(2029 < glue_len_anoxia_full_prof_inyear_rcp26.index) & (glue_len_anoxia_full_prof_inyear_rcp26.index < 2060)]['50%']
np.mean(glue_near_future_len_anoxia_full_prof_rcp26)
#55.019228562850785
glue_near_future_len_anoxia_full_prof_rcp60=glue_len_anoxia_full_prof_inyear_rcp60[(2029 < glue_len_anoxia_full_prof_inyear_rcp60.index) & (glue_len_anoxia_full_prof_inyear_rcp60.index < 2060)]['50%']
np.mean(glue_near_future_len_anoxia_full_prof_rcp60)
# 53.189590898330934
glue_near_future_len_anoxia_full_prof_rcp85=glue_len_anoxia_full_prof_inyear_rcp85[(2029 < glue_len_anoxia_full_prof_inyear_rcp85.index) & (glue_len_anoxia_full_prof_inyear_rcp85.index < 2060)]['50%']
np.mean(glue_near_future_len_anoxia_full_prof_rcp85)
# 56.605652169077835

 
#Distant future [2070-2099]

glue_distant_future_len_anoxia_full_prof_rcp26=glue_len_anoxia_full_prof_inyear_rcp26[(2069 < glue_len_anoxia_full_prof_inyear_rcp26.index) & (glue_len_anoxia_full_prof_inyear_rcp26.index < 2100)]['50%']
np.mean(glue_distant_future_len_anoxia_full_prof_rcp26)
#55.17751141374097
glue_distant_future_len_anoxia_full_prof_rcp60=glue_len_anoxia_full_prof_inyear_rcp60[(2069 < glue_len_anoxia_full_prof_inyear_rcp60.index) & (glue_len_anoxia_full_prof_inyear_rcp60.index< 2100)]['50%']
np.mean(glue_distant_future_len_anoxia_full_prof_rcp60)
#64.53254321830363
glue_distant_future_len_anoxia_full_prof_rcp85=glue_len_anoxia_full_prof_inyear_rcp85[(2069 < glue_len_anoxia_full_prof_inyear_rcp85.index) & (glue_len_anoxia_full_prof_inyear_rcp85.index < 2100)]['50%']
np.mean(glue_distant_future_len_anoxia_full_prof_rcp85)
#74.42301816738942
   


###====over 30 years in his and each RCPs 

# baseline [1976-2005]
autocorr_MK_org_modif_sens_slope_test(glue_base_len_anoxia_full_prof_his)
(0.06817673251963975,
 'positively autocorrelated',
 'increasing',
 0.03484345525348331,
 0.3333333333333333,
 35.166666666666664)

#near future [2030-2059]


autocorr_MK_org_modif_sens_slope_test(glue_near_future_len_anoxia_full_prof_rcp26)
(0.04711275096842796,
 'positively autocorrelated',
 'no trend',
 0.06524117737116142,
 0,
 0)
autocorr_MK_org_modif_sens_slope_test(glue_near_future_len_anoxia_full_prof_rcp60)
(0.014868985413723878,
 'positively autocorrelated',
 'increasing',
 0.0491221452590338,
 0.21252951920840754,
 49.91832197147809)

autocorr_MK_org_modif_sens_slope_test(glue_near_future_len_anoxia_full_prof_rcp85)
(0.03250450533503405,
 'positively autocorrelated',
 'increasing',
 0.009487277736578204,
 0.42213127957376007,
 50.13656478285197)



#Distant future [2070-2099]


autocorr_MK_org_modif_sens_slope_test(glue_distant_future_len_anoxia_full_prof_rcp26)
(0.04959940370650393,
 'positively autocorrelated',
 'no trend',
 0.3674903140050061,
 0,
 0)
autocorr_MK_org_modif_sens_slope_test(glue_distant_future_len_anoxia_full_prof_rcp60)
(0.01651540502597596,
 'positively autocorrelated',
 'no trend',
 0.12088744633726756,
 0,
 0)

autocorr_MK_org_modif_sens_slope_test(glue_distant_future_len_anoxia_full_prof_rcp85)
(0.027554928859223834,
 'positively autocorrelated',
 'increasing',
 0.0030168069086071725,
 0.5038378713075744,
 66.94921928021127)



#%% Trendlines over whole periods:
# no trend in his but increasing trendlines of all rcps 
# for length of full anoxia    
    
# his     
  
autocorr_MK_org_modif_sens_slope_test(glue_len_anoxia_full_prof_inyear_his['50%'])
"""
(0.07459635806371567,
 'positively autocorrelated',
 'no trend',
 0.7958562747521769,
 0,
 0)
"""
#rcp26
autocorr_MK_org_modif_sens_slope_test(glue_len_anoxia_full_prof_inyear_rcp26['50%'])
"""
(0.04706429779194839,
 'positively autocorrelated',
 'increasing',
 0.0021349960098140386,
 0.08571428571428572,
 48.01428571428571)
"""

#rcp60
autocorr_MK_org_modif_sens_slope_test(glue_len_anoxia_full_prof_inyear_rcp60['50%'])
"""
(0.01963104775488452,
 'positively autocorrelated',
 'increasing',
 2.220446049250313e-16,
 0.2222222222222222,
 46.66666666666667)
"""

#rcp85
autocorr_MK_org_modif_sens_slope_test(glue_len_anoxia_full_prof_inyear_rcp85['50%'])
"""
(0.03614865782641989,
 'positively autocorrelated',
 'increasing',
 0.0,
 0.39215686274509803,
 41.76470588235294)
"""





#%% 80 years from 2020 for len_anoxia_full_prof


glue_80years_len_anoxia_full_prof_inyear_rcp26=glue_len_anoxia_full_prof_inyear_rcp26[2019 < glue_len_anoxia_full_prof_inyear_rcp26.index]

glue_80years_len_anoxia_full_prof_inyear_rcp60=glue_len_anoxia_full_prof_inyear_rcp60[2019 < glue_len_anoxia_full_prof_inyear_rcp60.index]


glue_80years_len_anoxia_full_prof_inyear_rcp85=glue_len_anoxia_full_prof_inyear_rcp85[2019 < glue_len_anoxia_full_prof_inyear_rcp85.index]



#=========== trendline # Over the 80 years


autocorr_MK_org_modif_sens_slope_test(glue_80years_len_anoxia_full_prof_inyear_rcp26['50%'])
(0.04904099909031567,
 'positively autocorrelated',
 'no trend',
 0.2358663670734389,
 0,
 0)

autocorr_MK_org_modif_sens_slope_test(glue_80years_len_anoxia_full_prof_inyear_rcp60['50%'])
(0.016107830734467928,
 'positively autocorrelated',
 'increasing',
 4.780620344035924e-13,
 0.23944298174914783,
 47.84742146977578)


autocorr_MK_org_modif_sens_slope_test(glue_80years_len_anoxia_full_prof_inyear_rcp85['50%'])
(0.028257055554346808,
 'positively autocorrelated',
 'increasing',
 3.774758283725532e-15,
 0.4011340945918508,
 46.65520326362189)

#============= mean of first 10 yaers over 80 years 

#rcp2.6
np.mean(glue_80years_len_anoxia_full_prof_inyear_rcp26[glue_80years_len_anoxia_full_prof_inyear_rcp26.index<2030]['50%'])
54.305768786231035

#rcp6.0
np.mean(glue_80years_len_anoxia_full_prof_inyear_rcp60[glue_80years_len_anoxia_full_prof_inyear_rcp60.index<2030]['50%'])
51.20929108898772

#rcp8.5
np.mean(glue_80years_len_anoxia_full_prof_inyear_rcp85[glue_80years_len_anoxia_full_prof_inyear_rcp85.index<2030]['50%'])
52.51046353471393

#============== mean of last 10 yaers over 80 years 

#rcp2.6
np.mean(glue_80years_len_anoxia_full_prof_inyear_rcp26[glue_80years_len_anoxia_full_prof_inyear_rcp26.index>2089]['50%'])
55.65035596551418

#rcp6.0
np.mean(glue_80years_len_anoxia_full_prof_inyear_rcp60[glue_80years_len_anoxia_full_prof_inyear_rcp60.index>2089]['50%'])
68.65690570928328

#rcp8.5
np.mean(glue_80years_len_anoxia_full_prof_inyear_rcp85[glue_80years_len_anoxia_full_prof_inyear_rcp85.index>2089]['50%'])
65.74230252984306
#%% averaging over whole scenarios value for first anoxia full profile 

np.mean(glue_first_jday_anoxia_full_prof_inyear_his['50%'])#202.09459785632947
np.mean(glue_first_jday_anoxia_full_prof_inyear_rcp26['50%'])#195.72238913786117
np.mean(glue_first_jday_anoxia_full_prof_inyear_rcp60['50%'])#193.41007157743243
np.mean(glue_first_jday_anoxia_full_prof_inyear_rcp85['50%'])#190.36549991086954



#%%anoxia_duration 30 yerars from each scenarios compare 



#anomaly 
# baseline [1976-2005]
glue_base_first_jday_anoxia_full_prof_his=glue_first_jday_anoxia_full_prof_inyear_his[1975 < glue_first_jday_anoxia_full_prof_inyear_his.index]['50%']
len_anoxia_full_prof_ref=np.mean(glue_base_first_jday_anoxia_full_prof_his)
#205.6613479175225


#near future [2030-2059]

glue_near_future_first_jday_anoxia_full_prof_rcp26=glue_first_jday_anoxia_full_prof_inyear_rcp26[(2029 < glue_first_jday_anoxia_full_prof_inyear_rcp26.index) & (glue_first_jday_anoxia_full_prof_inyear_rcp26.index < 2060)]['50%']
np.mean(glue_near_future_first_jday_anoxia_full_prof_rcp26)
#195.0656623586102
glue_near_future_first_jday_anoxia_full_prof_rcp60=glue_first_jday_anoxia_full_prof_inyear_rcp60[(2029 < glue_first_jday_anoxia_full_prof_inyear_rcp60.index) & (glue_first_jday_anoxia_full_prof_inyear_rcp60.index < 2060)]['50%']
np.mean(glue_near_future_first_jday_anoxia_full_prof_rcp60)
# 194.93333333333334
glue_near_future_first_jday_anoxia_full_prof_rcp85=glue_first_jday_anoxia_full_prof_inyear_rcp85[(2029 < glue_first_jday_anoxia_full_prof_inyear_rcp85.index) & (glue_first_jday_anoxia_full_prof_inyear_rcp85.index < 2060)]['50%']
np.mean(glue_near_future_first_jday_anoxia_full_prof_rcp85)
#192.89304143335247

 
#Distant future [2070-2099]

glue_distant_future_first_jday_anoxia_full_prof_rcp26=glue_first_jday_anoxia_full_prof_inyear_rcp26[(2069 < glue_first_jday_anoxia_full_prof_inyear_rcp26.index) & (glue_first_jday_anoxia_full_prof_inyear_rcp26.index < 2100)]['50%']
np.mean(glue_distant_future_first_jday_anoxia_full_prof_rcp26)
#194.78361891156072
glue_distant_future_first_jday_anoxia_full_prof_rcp60=glue_first_jday_anoxia_full_prof_inyear_rcp60[(2069 < glue_first_jday_anoxia_full_prof_inyear_rcp60.index) & (glue_first_jday_anoxia_full_prof_inyear_rcp60.index< 2100)]['50%']
np.mean(glue_distant_future_first_jday_anoxia_full_prof_rcp60)
#187.78512927508444
glue_distant_future_first_jday_anoxia_full_prof_rcp85=glue_first_jday_anoxia_full_prof_inyear_rcp85[(2069 < glue_first_jday_anoxia_full_prof_inyear_rcp85.index) & (glue_first_jday_anoxia_full_prof_inyear_rcp85.index < 2100)]['50%']
np.mean(glue_distant_future_first_jday_anoxia_full_prof_rcp85)
#183.73497044103513
   


###====over 30 years in his and each RCPs 

# baseline [1976-2005]
autocorr_MK_org_modif_sens_slope_test(glue_base_first_jday_anoxia_full_prof_his)
(0.0010714863017847968,
 'positively autocorrelated',
 'no trend',
 0.3602576026982467,
 0,
 0)
#near future [2030-2059]


autocorr_MK_org_modif_sens_slope_test(glue_near_future_first_jday_anoxia_full_prof_rcp26)
(0.0035324057727393493,
 'positively autocorrelated',
 'no trend',
 0.31651188210252346,
 0,
 0)

autocorr_MK_org_modif_sens_slope_test(glue_near_future_first_jday_anoxia_full_prof_rcp60)
(0.0008802863210169236,
 'positively autocorrelated',
 'no trend',
 0.2358361230161199,
 0,
 0)

autocorr_MK_org_modif_sens_slope_test(glue_near_future_first_jday_anoxia_full_prof_rcp85)
(0.0008526430745015595,
 'positively autocorrelated',
 'no trend',
 0.19114853424057254,
 0,
 0)



#Distant future [2070-2099]


autocorr_MK_org_modif_sens_slope_test(glue_distant_future_first_jday_anoxia_full_prof_rcp26)
(0.003631763063474989,
 'positively autocorrelated',
 'no trend',
 0.12024059391996622,
 0,
 0)


autocorr_MK_org_modif_sens_slope_test(glue_distant_future_first_jday_anoxia_full_prof_rcp60)
(0.003376404820593211,
 'positively autocorrelated',
 'no trend',
 0.6808971760160334,
 0,
 0)


autocorr_MK_org_modif_sens_slope_test(glue_distant_future_first_jday_anoxia_full_prof_rcp85)
(0.0036434361185840765,
 'positively autocorrelated',
 'decreasing',
 0.008971941759822633,
 -0.32468026094170455,
 189.43813181750903)



#%% Trendlines over whole periods:
# no trend in his but decreasing trendlines of 6.0 and 8.5 rcps 
# for first jday of full anoxia    
    
# his     
  
autocorr_MK_org_modif_sens_slope_test(glue_first_jday_anoxia_full_prof_inyear_his['50%'])
"""
(0.003263986589805516,
 'positively autocorrelated',
 'increasing',
 0.0019083924738845237,
 0.03571428571428571,
 201.42857142857142)
"""
#rcp26
autocorr_MK_org_modif_sens_slope_test(glue_first_jday_anoxia_full_prof_inyear_rcp26['50%'])
"""
(0.0035302527670915437,
 'positively autocorrelated',
 'decreasing',
 0.015757773005003806,
 -0.05536018036267541,
 199.5742483868644)
"""

#rcp60
autocorr_MK_org_modif_sens_slope_test(glue_first_jday_anoxia_full_prof_inyear_rcp60['50%'])
"""
(0.0017441207246221392,
 'positively autocorrelated',
 'decreasing',
 0.0,
 -0.14705882352941177,
 200.83823529411765)
"""

#rcp85
autocorr_MK_org_modif_sens_slope_test(glue_first_jday_anoxia_full_prof_inyear_rcp85['50%'])
"""
(0.0026975072962181538,
 'positively autocorrelated',
 'decreasing',
 5.224931598490912e-12,
 -0.16966835707199673,
 199.12111564812068)
"""





#%% 80 years from 2020 for first_jday_anoxia_full_prof


glue_80years_first_jday_anoxia_full_prof_inyear_rcp26=glue_first_jday_anoxia_full_prof_inyear_rcp26[2019 < glue_first_jday_anoxia_full_prof_inyear_rcp26.index]

glue_80years_first_jday_anoxia_full_prof_inyear_rcp60=glue_first_jday_anoxia_full_prof_inyear_rcp60[2019 < glue_first_jday_anoxia_full_prof_inyear_rcp60.index]


glue_80years_first_jday_anoxia_full_prof_inyear_rcp85=glue_first_jday_anoxia_full_prof_inyear_rcp85[2019 < glue_first_jday_anoxia_full_prof_inyear_rcp85.index]

#=========== trendline # Over the 80 years


autocorr_MK_org_modif_sens_slope_test(glue_80years_first_jday_anoxia_full_prof_inyear_rcp26['50%'])

(0.004003373183865467,
 'positively autocorrelated',
 'no trend',
 0.19695783312854775,
 0,
 0)

autocorr_MK_org_modif_sens_slope_test(glue_80years_first_jday_anoxia_full_prof_inyear_rcp60['50%'])
(0.001776268459756876,
 'positively autocorrelated',
 'decreasing',
 2.3003821070233244e-13,
 -0.1512292738707833,
 198.97355631789594)

autocorr_MK_org_modif_sens_slope_test(glue_80years_first_jday_anoxia_full_prof_inyear_rcp85['50%'])
(0.002223764327959461,
 'positively autocorrelated',
 'decreasing',
 1.5880846282456673e-07,
 -0.15672315077875631,
 196.19056445576086)

#============= mean of first 10 yaers over 80 years 

#rcp2.6
np.mean(glue_80years_first_jday_anoxia_full_prof_inyear_rcp26[glue_80years_first_jday_anoxia_full_prof_inyear_rcp26.index<2030]['50%'])
194.0484865911109

#rcp6.0
np.mean(glue_80years_first_jday_anoxia_full_prof_inyear_rcp60[glue_80years_first_jday_anoxia_full_prof_inyear_rcp60.index<2030]['50%'])
198.54959022114863

#rcp8.5
np.mean(glue_80years_first_jday_anoxia_full_prof_inyear_rcp85[glue_80years_first_jday_anoxia_full_prof_inyear_rcp85.index<2030]['50%'])
191.69440874659202
#============== mean of last 10 yaers over 80 years 

#rcp2.6
np.mean(glue_80years_first_jday_anoxia_full_prof_inyear_rcp26[glue_80years_first_jday_anoxia_full_prof_inyear_rcp26.index>2089]['50%'])
193.34396880494492

#rcp6.0
np.mean(glue_80years_first_jday_anoxia_full_prof_inyear_rcp60[glue_80years_first_jday_anoxia_full_prof_inyear_rcp60.index>2089]['50%'])
186.06985886935763

#rcp8.5
np.mean(glue_80years_first_jday_anoxia_full_prof_inyear_rcp85[glue_80years_first_jday_anoxia_full_prof_inyear_rcp85.index>2089]['50%'])
176.9101031665403





#%%
#%%plotting 80 years of len and first jday of full anoxia profile  


import matplotlib.pyplot as plt
import numpy as np

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(26, 8))

# Plotting the first subplot
ax1.fill_between(glue_80years_len_anoxia_full_prof_inyear_rcp26.index.astype(float), glue_80years_len_anoxia_full_prof_inyear_rcp26['5%'], glue_80years_len_anoxia_full_prof_inyear_rcp26['95%'], color='darkgreen', alpha=0.3)# ,  label= 'RCP2.6 90% CI')
ax1.plot(glue_80years_len_anoxia_full_prof_inyear_rcp26.index.astype(float), glue_80years_len_anoxia_full_prof_inyear_rcp26['50%'], 'darkgreen', alpha=0.9, linewidth=3  )#, label='RCP2.6 median'

ax1.fill_between(glue_80years_len_anoxia_full_prof_inyear_rcp60.index.astype(float), glue_80years_len_anoxia_full_prof_inyear_rcp60['5%'], glue_80years_len_anoxia_full_prof_inyear_rcp60['95%'], color='yellow', alpha=0.5)# ,  label= 'RCP6.0 90% CI')
ax1.plot(glue_80years_len_anoxia_full_prof_inyear_rcp60.index.astype(float), glue_80years_len_anoxia_full_prof_inyear_rcp60['50%'], 'yellow', alpha=0.9, linewidth=3  )#, label='RCP6.0 median'

ax1.fill_between(glue_80years_len_anoxia_full_prof_inyear_rcp85.index.astype(float), glue_80years_len_anoxia_full_prof_inyear_rcp85['5%'], glue_80years_len_anoxia_full_prof_inyear_rcp85['95%'], color='r', alpha=0.2)# ,  label= 'RCP8.5 90% CI')
ax1.plot(glue_80years_len_anoxia_full_prof_inyear_rcp85.index.astype(float), glue_80years_len_anoxia_full_prof_inyear_rcp85['50%'], 'r', alpha=0.9, linewidth=3  )#, label='RCP8.5 median'

trendline_rcp60_len = autocorr_MK_org_modif_sens_slope_test(glue_80years_len_anoxia_full_prof_inyear_rcp60['50%'])
ax1.text(2020, 170, f'y = {trendline_rcp60_len[-2]:.3f}x + {trendline_rcp60_len[-1]:.3f}, p-value < 0.0001', color='orange', fontsize=20 )

ax1.plot(glue_80years_len_anoxia_full_prof_inyear_rcp60.index.astype(float),
        trendline_rcp60_len[-2] * np.arange(80) + trendline_rcp60_len[-1],
        linestyle='--', color='orange', alpha=0.9, linewidth=3)


trendline_rcp85_len = autocorr_MK_org_modif_sens_slope_test(glue_80years_len_anoxia_full_prof_inyear_rcp85['50%'])
ax1.text(2020, 160, f'y = {trendline_rcp85_len[-2]:.3f}x + {trendline_rcp85_len[-1]:.3f}, p-value < 0.0001', color='red', fontsize=20 )


ax1.plot(glue_80years_len_anoxia_full_prof_inyear_rcp85.index.astype(float),
        trendline_rcp85_len[-2] * np.arange(80) + trendline_rcp85_len[-1],
        linestyle='--', color='red', alpha=0.9, linewidth=3)# , label= 'RCP8.5 trendline')


ax1.set_ylabel('Duration of full deep anoxia [d]' , fontsize=26)
ax1.set_xlabel('Year' , fontsize=26)
ax1.tick_params(axis='both', which='major', labelsize=22)
#ax1.legend(bbox_to_anchor=(0.7, -0.2), fontsize=22)
ax1.tick_params(axis='x', rotation=45, labelsize=22)




# Plotting the second subplot
ax2.fill_between(glue_80years_first_jday_anoxia_full_prof_inyear_rcp26.index.astype(float), glue_80years_first_jday_anoxia_full_prof_inyear_rcp26['5%'], glue_80years_first_jday_anoxia_full_prof_inyear_rcp26['95%'], color='darkgreen', alpha=0.3 ,  label= 'RCP2.6 90% CI')
ax2.plot(glue_80years_first_jday_anoxia_full_prof_inyear_rcp26.index.astype(float), glue_80years_first_jday_anoxia_full_prof_inyear_rcp26['50%'], 'darkgreen', label='RCP2.6 median', alpha=0.9, linewidth=3  )

ax2.fill_between(glue_80years_first_jday_anoxia_full_prof_inyear_rcp60.index.astype(float), glue_80years_first_jday_anoxia_full_prof_inyear_rcp60['5%'], glue_80years_first_jday_anoxia_full_prof_inyear_rcp60['95%'], color='yellow', alpha=0.5 ,  label= 'RCP6.0 90% CI')
ax2.plot(glue_80years_first_jday_anoxia_full_prof_inyear_rcp60.index.astype(float), glue_80years_first_jday_anoxia_full_prof_inyear_rcp60['50%'], 'yellow', label='RCP6.0 median', alpha=0.9, linewidth=3  )

ax2.fill_between(glue_80years_first_jday_anoxia_full_prof_inyear_rcp85.index.astype(float), glue_80years_first_jday_anoxia_full_prof_inyear_rcp85['5%'], glue_80years_first_jday_anoxia_full_prof_inyear_rcp85['95%'], color='r', alpha=0.2 ,  label= 'RCP8.5 90% CI')
ax2.plot(glue_80years_first_jday_anoxia_full_prof_inyear_rcp85.index.astype(float), glue_80years_first_jday_anoxia_full_prof_inyear_rcp85['50%'], 'r', label='RCP8.5 median', alpha=0.9, linewidth=3  )

trendline_rcp60_first = autocorr_MK_org_modif_sens_slope_test(glue_80years_first_jday_anoxia_full_prof_inyear_rcp60['50%'])
ax2.text(2020, 110, f'y = {trendline_rcp60_first[-2]:.3f}x + {trendline_rcp60_first[-1]:.3f}, p-value < 0.0001', color='orange', fontsize=20 )

ax2.plot(glue_80years_first_jday_anoxia_full_prof_inyear_rcp60.index.astype(float),
        trendline_rcp60_first[-2] * np.arange(80) + trendline_rcp60_first[-1],
        linestyle='--', color='orange', alpha=0.9, linewidth=3, label= 'RCP6.0 trendline')

trendline_rcp85_first = autocorr_MK_org_modif_sens_slope_test(glue_80years_first_jday_anoxia_full_prof_inyear_rcp85['50%'])
ax2.text(2020, 100, f'y = {trendline_rcp85_first[-2]:.3f}x + {trendline_rcp85_first[-1]:.3f}, p-value < 0.0001', color='red', fontsize=20 )

ax2.plot(glue_80years_first_jday_anoxia_full_prof_inyear_rcp85.index.astype(float),
        trendline_rcp85_first[-2] * np.arange(80) + trendline_rcp85_first[-1],
        linestyle='--', color='red', alpha=0.9, linewidth=3 , label= 'RCP8.5 trendline')

ax2.set_ylabel('First day of full deep anoxia in year [Jd]' , fontsize=26)
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
plt.savefig('GLUE_Timeseries_full_anoxia_duration_first_len_full_anoxia_80years.png', bbox_inches='tight')




#%% anormally plot of first Jda and length of full anoxia profile 


import os
import matplotlib.pyplot as plt

# Change directory
os.chdir('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/all_4_models/')

# Create a figure and axes for subplots
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(25, 10))

# Plotting the first subplot
ax1 = axes[0]
ax1.fill_between(glue_first_jday_anoxia_full_prof_inyear_his[(1975 < glue_first_jday_anoxia_full_prof_inyear_his.index)].index.astype(float),
                 glue_first_jday_anoxia_full_prof_inyear_his[(1975 < glue_first_jday_anoxia_full_prof_inyear_his.index)]['5%'] - first_jday_anoxia_full_prof_inyear_ref,
                 glue_first_jday_anoxia_full_prof_inyear_his[(1975 < glue_first_jday_anoxia_full_prof_inyear_his.index)]['95%'] - first_jday_anoxia_full_prof_inyear_ref,
                 color='grey', alpha=0.2, label='His 90% CI')

ax1.plot(glue_first_jday_anoxia_full_prof_inyear_his[(1975 < glue_first_jday_anoxia_full_prof_inyear_his.index)].index.astype(float),
         glue_first_jday_anoxia_full_prof_inyear_his[(1975 < glue_first_jday_anoxia_full_prof_inyear_his.index)]['50%'] - first_jday_anoxia_full_prof_inyear_ref,
         'k', label='His median', alpha=0.9, linewidth=3)

ax1.fill_between(glue_first_jday_anoxia_full_prof_inyear_rcp26.index.astype(float), glue_first_jday_anoxia_full_prof_inyear_rcp26['5%'] - first_jday_anoxia_full_prof_inyear_ref, glue_first_jday_anoxia_full_prof_inyear_rcp26['95%'] - first_jday_anoxia_full_prof_inyear_ref, color='darkgreen', alpha=0.3, label='RCP6.0 90% CI')

ax1.plot(glue_first_jday_anoxia_full_prof_inyear_rcp26.index.astype(float), glue_first_jday_anoxia_full_prof_inyear_rcp26['50%'] - first_jday_anoxia_full_prof_inyear_ref, 'darkgreen', label='RCP6.0 median', alpha=0.9, linewidth=3)

ax1.fill_between(glue_first_jday_anoxia_full_prof_inyear_rcp60.index.astype(float), glue_first_jday_anoxia_full_prof_inyear_rcp60['5%'] - first_jday_anoxia_full_prof_inyear_ref, glue_first_jday_anoxia_full_prof_inyear_rcp60['95%'] - first_jday_anoxia_full_prof_inyear_ref, color='yellow', alpha=0.5, label='RCP6.0 90% CI')

ax1.plot(glue_first_jday_anoxia_full_prof_inyear_rcp60.index.astype(float), glue_first_jday_anoxia_full_prof_inyear_rcp60['50%'] - first_jday_anoxia_full_prof_inyear_ref, 'yellow', label='RCP6.0 median', alpha=0.9, linewidth=3)

ax1.fill_between(glue_first_jday_anoxia_full_prof_inyear_rcp85.index.astype(float), glue_first_jday_anoxia_full_prof_inyear_rcp85['5%'] - first_jday_anoxia_full_prof_inyear_ref, glue_first_jday_anoxia_full_prof_inyear_rcp85['95%'] - first_jday_anoxia_full_prof_inyear_ref, color='r', alpha=0.2, label='RCP8.5 90% CI')

ax1.plot(glue_first_jday_anoxia_full_prof_inyear_rcp85.index.astype(float), glue_first_jday_anoxia_full_prof_inyear_rcp85['50%'] - first_jday_anoxia_full_prof_inyear_ref, 'r', label='RCP8.5 median', alpha=0.9, linewidth=3)

ax1.set_ylabel('Anomaly of first day of full deep anoxia [Jd]', fontsize=26)
ax1.set_xlabel('Year', fontsize=26)
ax1.tick_params(axis='y', labelsize=22)
ax1.tick_params(axis='x', rotation=45, labelsize=22)

# Plotting the second subplot
ax2 = axes[1]
ax2.fill_between(glue_len_anoxia_full_prof_inyear_his[(1975 < glue_len_anoxia_full_prof_inyear_his.index)].index.astype(float),
                 glue_len_anoxia_full_prof_inyear_his[(1975 < glue_len_anoxia_full_prof_inyear_his.index)]['5%'] - len_anoxia_full_prof_inyear_ref,
                 glue_len_anoxia_full_prof_inyear_his[(1975 < glue_len_anoxia_full_prof_inyear_his.index)]['95%'] - len_anoxia_full_prof_inyear_ref,
                 color='grey', alpha=0.2)#, label='His 90% CI')

ax2.plot(glue_len_anoxia_full_prof_inyear_his[(1975 < glue_len_anoxia_full_prof_inyear_his.index)].index.astype(float),
          glue_len_anoxia_full_prof_inyear_his[(1975 < glue_len_anoxia_full_prof_inyear_his.index)]['50%'] - len_anoxia_full_prof_inyear_ref,
          'k', alpha=0.9, linewidth=3)

ax2.fill_between(glue_len_anoxia_full_prof_inyear_rcp26.index.astype(float), glue_len_anoxia_full_prof_inyear_rcp26['5%'] - len_anoxia_full_prof_inyear_ref, glue_len_anoxia_full_prof_inyear_rcp26['95%'] - len_anoxia_full_prof_inyear_ref, color='darkgreen', alpha=0.3)#, label='RCP6.0 90% CI')

ax2.plot(glue_len_anoxia_full_prof_inyear_rcp26.index.astype(float), glue_len_anoxia_full_prof_inyear_rcp26['50%'] - len_anoxia_full_prof_inyear_ref, 'darkgreen',alpha=0.9, linewidth=3)

ax2.fill_between(glue_len_anoxia_full_prof_inyear_rcp60.index.astype(float), glue_len_anoxia_full_prof_inyear_rcp60['5%'] - len_anoxia_full_prof_inyear_ref, glue_len_anoxia_full_prof_inyear_rcp60['95%'] - len_anoxia_full_prof_inyear_ref, color='yellow', alpha=0.5)#, label='RCP6.0 90% CI')

ax2.plot(glue_len_anoxia_full_prof_inyear_rcp60.index.astype(float), glue_len_anoxia_full_prof_inyear_rcp60['50%'] - len_anoxia_full_prof_inyear_ref, 'yellow', alpha=0.9, linewidth=3)

ax2.fill_between(glue_len_anoxia_full_prof_inyear_rcp85.index.astype(float), glue_len_anoxia_full_prof_inyear_rcp85['5%'] - len_anoxia_full_prof_inyear_ref, glue_len_anoxia_full_prof_inyear_rcp85['95%'] - len_anoxia_full_prof_inyear_ref, color='r', alpha=0.2)#, label='RCP8.5 90% CI')

ax2.plot(glue_len_anoxia_full_prof_inyear_rcp85.index.astype(float), glue_len_anoxia_full_prof_inyear_rcp85['50%'] - len_anoxia_full_prof_inyear_ref, 'r',  alpha=0.9, linewidth=3)

ax2.set_ylabel('Anomaly of full deep anoxia duration [d]', fontsize=26)
ax2.set_xlabel('Year', fontsize=26)
ax2.tick_params(axis='y', labelsize=22)
ax2.tick_params(axis='x', rotation=45, labelsize=22)

# Legend for both subplots
fig.legend(loc='upper center', bbox_to_anchor=(0.5, -0.01), shadow=True, ncol=4, fontsize=22)

# Save the figure
fig.savefig("Anomaly_first_jday_duration_full_anoxia_profile.png", dpi=300, bbox_inches='tight')
plt.show()



#%% value plot of first Jda and length of full anoxia profile 


import os
import matplotlib.pyplot as plt

# Change directory
os.chdir('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/all_4_models/')

# Create a figure and axes for subplots
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(25, 10))

# Plotting the first subplot
ax1 = axes[0]
ax1.fill_between(glue_first_jday_anoxia_full_prof_inyear_his.index.astype(float),
                 glue_first_jday_anoxia_full_prof_inyear_his['5%'],
                 glue_first_jday_anoxia_full_prof_inyear_his['95%'],
                 color='grey', alpha=0.2, label='His 90% CI')

ax1.plot(glue_first_jday_anoxia_full_prof_inyear_his.index.astype(float),
         glue_first_jday_anoxia_full_prof_inyear_his['50%'],
         'k', label='His median', alpha=0.9, linewidth=3)

ax1.fill_between(glue_first_jday_anoxia_full_prof_inyear_rcp26.index.astype(float), glue_first_jday_anoxia_full_prof_inyear_rcp26['5%'], glue_first_jday_anoxia_full_prof_inyear_rcp26['95%'], color='darkgreen', alpha=0.3, label='RCP6.0 90% CI')

ax1.plot(glue_first_jday_anoxia_full_prof_inyear_rcp26.index.astype(float), glue_first_jday_anoxia_full_prof_inyear_rcp26['50%'], 'darkgreen', label='RCP6.0 median', alpha=0.9, linewidth=3)

ax1.fill_between(glue_first_jday_anoxia_full_prof_inyear_rcp60.index.astype(float), glue_first_jday_anoxia_full_prof_inyear_rcp60['5%'], glue_first_jday_anoxia_full_prof_inyear_rcp60['95%'], color='yellow', alpha=0.5, label='RCP6.0 90% CI')

ax1.plot(glue_first_jday_anoxia_full_prof_inyear_rcp60.index.astype(float), glue_first_jday_anoxia_full_prof_inyear_rcp60['50%'], 'yellow', label='RCP6.0 median', alpha=0.9, linewidth=3)

ax1.fill_between(glue_first_jday_anoxia_full_prof_inyear_rcp85.index.astype(float), glue_first_jday_anoxia_full_prof_inyear_rcp85['5%'], glue_first_jday_anoxia_full_prof_inyear_rcp85['95%'], color='r', alpha=0.2, label='RCP8.5 90% CI')

ax1.plot(glue_first_jday_anoxia_full_prof_inyear_rcp85.index.astype(float), glue_first_jday_anoxia_full_prof_inyear_rcp85['50%'], 'r', label='RCP8.5 median', alpha=0.9, linewidth=3)

ax1.set_ylabel('First day of full deep anoxia [Jd]', fontsize=26)
ax1.set_xlabel('Year', fontsize=26)
ax1.tick_params(axis='y', labelsize=22)
ax1.tick_params(axis='x', rotation=45, labelsize=22)

# Plotting the second subplot
ax2 = axes[1]
ax2.fill_between(glue_len_anoxia_full_prof_inyear_his.index.astype(float),
                 glue_len_anoxia_full_prof_inyear_his['5%'] ,
                 glue_len_anoxia_full_prof_inyear_his['95%'] ,
                 color='grey', alpha=0.2)#, label='His 90% CI')

ax2.plot(glue_len_anoxia_full_prof_inyear_his.index.astype(float),
          glue_len_anoxia_full_prof_inyear_his['50%'] ,
          'k', alpha=0.9, linewidth=3)

ax2.fill_between(glue_len_anoxia_full_prof_inyear_rcp26.index.astype(float), glue_len_anoxia_full_prof_inyear_rcp26['5%'] , glue_len_anoxia_full_prof_inyear_rcp26['95%'] , color='darkgreen', alpha=0.3)#, label='RCP6.0 90% CI')

ax2.plot(glue_len_anoxia_full_prof_inyear_rcp26.index.astype(float), glue_len_anoxia_full_prof_inyear_rcp26['50%'] , 'darkgreen',alpha=0.9, linewidth=3)

ax2.fill_between(glue_len_anoxia_full_prof_inyear_rcp60.index.astype(float), glue_len_anoxia_full_prof_inyear_rcp60['5%'] , glue_len_anoxia_full_prof_inyear_rcp60['95%'] , color='yellow', alpha=0.5)#, label='RCP6.0 90% CI')

ax2.plot(glue_len_anoxia_full_prof_inyear_rcp60.index.astype(float), glue_len_anoxia_full_prof_inyear_rcp60['50%'] , 'yellow', alpha=0.9, linewidth=3)

ax2.fill_between(glue_len_anoxia_full_prof_inyear_rcp85.index.astype(float), glue_len_anoxia_full_prof_inyear_rcp85['5%'] , glue_len_anoxia_full_prof_inyear_rcp85['95%'] , color='r', alpha=0.2)#, label='RCP8.5 90% CI')

ax2.plot(glue_len_anoxia_full_prof_inyear_rcp85.index.astype(float), glue_len_anoxia_full_prof_inyear_rcp85['50%'] , 'r',  alpha=0.9, linewidth=3)

ax2.set_ylabel('Full deep anoxia duration [d]', fontsize=26)
ax2.set_xlabel('Year', fontsize=26)
ax2.tick_params(axis='y', labelsize=22)
ax2.tick_params(axis='x', rotation=45, labelsize=22)

# Legend for both subplots
fig.legend(loc='upper center', bbox_to_anchor=(0.5, -0.01), shadow=True, ncol=4, fontsize=22)

# Save the figure
fig.savefig("First_jday_duration_full_anoxia_profile.png", dpi=300, bbox_inches='tight')
plt.show()




#%%

import os
import matplotlib.pyplot as plt

# Change directory
os.chdir('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/all_4_models/')

# Create a figure and axes for subplots
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(25, 10))

# Plotting the first subplot
ax1 = axes[0]
ax1.fill_between(glue_first_jday_anoxia_full_prof_inyear_his.index.astype(float),
                 glue_first_jday_anoxia_full_prof_inyear_his['5%'],
                 glue_first_jday_anoxia_full_prof_inyear_his['95%'],
                 color='grey', alpha=0.2, label='His 90% CI')

ax1.plot(glue_first_jday_anoxia_full_prof_inyear_his.index.astype(float),
         glue_first_jday_anoxia_full_prof_inyear_his['50%'],
         'k', label='His median', alpha=0.9, linewidth=3)

ax1.fill_between(glue_first_jday_anoxia_full_prof_inyear_rcp26.index.astype(float), glue_first_jday_anoxia_full_prof_inyear_rcp26['5%'], glue_first_jday_anoxia_full_prof_inyear_rcp26['95%'], color='darkgreen', alpha=0.3, label='RCP6.0 90% CI')

ax1.plot(glue_first_jday_anoxia_full_prof_inyear_rcp26.index.astype(float), glue_first_jday_anoxia_full_prof_inyear_rcp26['50%'], 'darkgreen', label='RCP6.0 median', alpha=0.9, linewidth=3)

ax1.fill_between(glue_first_jday_anoxia_full_prof_inyear_rcp60.index.astype(float), glue_first_jday_anoxia_full_prof_inyear_rcp60['5%'], glue_first_jday_anoxia_full_prof_inyear_rcp60['95%'], color='yellow', alpha=0.5, label='RCP6.0 90% CI')

ax1.plot(glue_first_jday_anoxia_full_prof_inyear_rcp60.index.astype(float), glue_first_jday_anoxia_full_prof_inyear_rcp60['50%'], 'yellow', label='RCP6.0 median', alpha=0.9, linewidth=3)

ax1.fill_between(glue_first_jday_anoxia_full_prof_inyear_rcp85.index.astype(float), glue_first_jday_anoxia_full_prof_inyear_rcp85['5%'], glue_first_jday_anoxia_full_prof_inyear_rcp85['95%'], color='r', alpha=0.2, label='RCP8.5 90% CI')

ax1.plot(glue_first_jday_anoxia_full_prof_inyear_rcp85.index.astype(float), glue_first_jday_anoxia_full_prof_inyear_rcp85['50%'], 'r', label='RCP8.5 median', alpha=0.9, linewidth=3)



trendline_his=autocorr_MK_org_modif_sens_slope_test(glue_first_jday_anoxia_full_prof_inyear_his['50%'])

trendline_rcp26=autocorr_MK_org_modif_sens_slope_test(glue_first_jday_anoxia_full_prof_inyear_rcp26['50%'])

trendline_rcp60=autocorr_MK_org_modif_sens_slope_test(glue_first_jday_anoxia_full_prof_inyear_rcp60['50%'])

trendline_rcp85=autocorr_MK_org_modif_sens_slope_test(glue_first_jday_anoxia_full_prof_inyear_rcp85['50%'])




ax1.text(1900, 165, f'y = {trendline_rcp60[-2]:.3f}x + {trendline_rcp60[-1]:.3f}, p = {trendline_rcp60[-3]:.3f}', color='gold', fontsize= 20 )

ax1.plot(glue_first_jday_anoxia_full_prof_inyear_rcp60.index.astype(float),
        trendline_rcp60[-2] * np.arange(94) + trendline_rcp60[-1],
        linestyle='--', color='yellow', alpha=0.9, linewidth=3)



ax1.text(1900, 160, f'y = {trendline_rcp85[-2]:.3f}x + {trendline_rcp85[-1]:.3f}, p = {trendline_rcp85[-3]:.3f}', color='red', fontsize= 20 )

ax1.plot(glue_first_jday_anoxia_full_prof_inyear_rcp85.index.astype(float),
        trendline_rcp85[-2] * np.arange(94) + trendline_rcp85[-1],
        linestyle='--', color='red', alpha=0.9, linewidth=3)




ax1.set_ylabel('First day of full deep anoxia [Jd]', fontsize=26)
ax1.set_xlabel('Year', fontsize=26)
ax1.tick_params(axis='y', labelsize=22)
ax1.tick_params(axis='x', rotation=45, labelsize=22)

# Plotting the second subplot
ax2 = axes[1]
ax2.fill_between(glue_len_anoxia_full_prof_inyear_his.index.astype(float),
                 glue_len_anoxia_full_prof_inyear_his['5%'] ,
                 glue_len_anoxia_full_prof_inyear_his['95%'] ,
                 color='grey', alpha=0.2)#, label='His 90% CI')

ax2.plot(glue_len_anoxia_full_prof_inyear_his.index.astype(float),
          glue_len_anoxia_full_prof_inyear_his['50%'] ,
          'k', alpha=0.9, linewidth=3)

ax2.fill_between(glue_len_anoxia_full_prof_inyear_rcp26.index.astype(float), glue_len_anoxia_full_prof_inyear_rcp26['5%'] , glue_len_anoxia_full_prof_inyear_rcp26['95%'] , color='darkgreen', alpha=0.3)#, label='RCP6.0 90% CI')

ax2.plot(glue_len_anoxia_full_prof_inyear_rcp26.index.astype(float), glue_len_anoxia_full_prof_inyear_rcp26['50%'] , 'darkgreen',alpha=0.9, linewidth=3)

ax2.fill_between(glue_len_anoxia_full_prof_inyear_rcp60.index.astype(float), glue_len_anoxia_full_prof_inyear_rcp60['5%'] , glue_len_anoxia_full_prof_inyear_rcp60['95%'] , color='yellow', alpha=0.5)#, label='RCP6.0 90% CI')

ax2.plot(glue_len_anoxia_full_prof_inyear_rcp60.index.astype(float), glue_len_anoxia_full_prof_inyear_rcp60['50%'] , 'yellow', alpha=0.9, linewidth=3)

ax2.fill_between(glue_len_anoxia_full_prof_inyear_rcp85.index.astype(float), glue_len_anoxia_full_prof_inyear_rcp85['5%'] , glue_len_anoxia_full_prof_inyear_rcp85['95%'] , color='r', alpha=0.2)#, label='RCP8.5 90% CI')

ax2.plot(glue_len_anoxia_full_prof_inyear_rcp85.index.astype(float), glue_len_anoxia_full_prof_inyear_rcp85['50%'] , 'r',  alpha=0.9, linewidth=3)




trendline_his=autocorr_MK_org_modif_sens_slope_test(glue_len_anoxia_full_prof_inyear_his['50%'])

trendline_rcp26=autocorr_MK_org_modif_sens_slope_test(glue_len_anoxia_full_prof_inyear_rcp26['50%'])

trendline_rcp60=autocorr_MK_org_modif_sens_slope_test(glue_len_anoxia_full_prof_inyear_rcp60['50%'])

trendline_rcp85=autocorr_MK_org_modif_sens_slope_test(glue_len_anoxia_full_prof_inyear_rcp85['50%'])


ax2.text(1900,90, f'y = {trendline_rcp26[-2]:.3f}x + {trendline_rcp26[-1]:.3f}, p = {trendline_rcp26[-3]:.3f}', color='green', fontsize= 20 )

ax2.plot(glue_len_anoxia_full_prof_inyear_rcp26.index.astype(float),
        trendline_rcp26[-2] * np.arange(94) + trendline_rcp26[-1],
        linestyle='--', color='darkgreen', alpha=0.9, linewidth=3)



ax2.text(1900, 85, f'y = {trendline_rcp60[-2]:.3f}x + {trendline_rcp60[-1]:.3f}, p = {trendline_rcp60[-3]:.3f}', color='gold', fontsize= 20 )

ax2.plot(glue_len_anoxia_full_prof_inyear_rcp60.index.astype(float),
        trendline_rcp60[-2] * np.arange(94) + trendline_rcp60[-1],
        linestyle='--', color='yellow', alpha=0.9, linewidth=3)



ax2.text(1900, 80, f'y = {trendline_rcp85[-2]:.3f}x + {trendline_rcp85[-1]:.3f}, p = {trendline_rcp85[-3]:.3f}', color='red', fontsize= 20 )

ax2.plot(glue_len_anoxia_full_prof_inyear_rcp85.index.astype(float),
        trendline_rcp85[-2] * np.arange(94) + trendline_rcp85[-1],
        linestyle='--', color='red', alpha=0.9, linewidth=3)



ax2.set_ylabel('Full deep anoxia duration [d]', fontsize=26)
ax2.set_xlabel('Year', fontsize=26)
ax2.tick_params(axis='y', labelsize=22)
ax2.tick_params(axis='x', rotation=45, labelsize=22)

# Legend for both subplots
fig.legend(loc='upper center', bbox_to_anchor=(0.5, -0.01), shadow=True, ncol=4, fontsize=22)

# Save the figure
fig.savefig("First_jday_duration_full_anoxia_profile_withtrendline.png", dpi=300, bbox_inches='tight')
plt.show()





