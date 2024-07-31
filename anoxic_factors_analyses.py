# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 04:29:07 2023

@author: mahta
"""

#%% annual anoxic factor_his

all_annual_AF_his=pd.DataFrame([])
all_weights= np.array([])


#gfdl

# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/gfdl_senarios/his'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_gfdl_his_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Al = hypo_morpho_vriables_gotm_grid[2]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxic_factor function
        result = annual_anoxic_factor(C, time_series,Al, A0=23.67*10**6 , threshold=0.5)

        all_annual_AF_his = pd.concat([all_annual_AF_his , result], axis=1)
        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_anoxic_factor_gfdl_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_anoxic_factor'])
        
#hadgem               
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
        
        all_weights= np.append(all_weights , weights) 
        
        
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Al = hypo_morpho_vriables_gotm_grid[2]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxic_factor function
        result = annual_anoxic_factor(C, time_series,Al, A0=23.67*10**6 , threshold=0.5)

        all_annual_AF_his = pd.concat([all_annual_AF_his , result], axis=1)
        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_anoxic_factor_hadgem_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_anoxic_factor'])
#ipsl       
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
        
        all_weights= np.append(all_weights , weights) 
        
        
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Al = hypo_morpho_vriables_gotm_grid[2]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxic_factor function
        result = annual_anoxic_factor(C, time_series,Al, A0=23.67*10**6 , threshold=0.5)

        all_annual_AF_his = pd.concat([all_annual_AF_his , result], axis=1)
        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_anoxic_factor_ipsl_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_anoxic_factor'])
#miroc       
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
        
        all_weights= np.append(all_weights , weights) 
        
        
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Al = hypo_morpho_vriables_gotm_grid[2]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxic_factor function
        result = annual_anoxic_factor(C, time_series,Al, A0=23.67*10**6 , threshold=0.5)

        all_annual_AF_his = pd.concat([all_annual_AF_his , result], axis=1)
        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_anoxic_factor_miroc_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_anoxic_factor'])
        

#%%Uncertainity partitioning on all_annual_AF_his

anova_annual_AF_his=annova_uncertainity(all_annual_AF_his)

anova_annual_AF_his.describe().loc['mean', :]
"""
GCMs             70.674421
param            28.349100
interaction       0.976479
GCMs/param        5.203248
year           1933.000000
Name: mean, dtype: float64
"""


anova_annual_AF_his.describe().loc['std', :]
"""
GCMs           18.591168
param          18.335360
interaction     0.859412
GCMs/param      6.303505
year           42.001984
Name: std, dtype: float64
"""





#%% GLUE method on all_annual_AF_his 
          

        
#all_annual_AF_his= all_annual_AF_his.set_index(all_annual_AF_his['Datetime'])


# annual anoxic duration  
timeseries_year_his= all_annual_AF_his.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_annual_AF_his.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights))

# Build glue df
glue_df_annual_anoxic_factor_his = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_df_annual_anoxic_factor_his=glue_df_annual_anoxic_factor_his.set_index(timeseries_year_his)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory
glue_df_annual_anoxic_factor_his.to_csv('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/all_4_models/his/glue_df_anoxic_factor_his.csv')
        


#%% annual anoxic factor_rcp26

all_annual_AF_rcp26=pd.DataFrame([])
all_weights= np.array([])


#gfdl

# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/gfdl_senarios/rcp26'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_gfdl_rcp26_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Al = hypo_morpho_vriables_gotm_grid[2]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxic_factor function
        result = annual_anoxic_factor(C, time_series,Al, A0=23.67*10**6 , threshold=0.5)

        all_annual_AF_rcp26 = pd.concat([all_annual_AF_rcp26 , result], axis=1)
        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_anoxic_factor_gfdl_rcp26_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_anoxic_factor'])
        
#hadgem               
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
        
        all_weights= np.append(all_weights , weights) 
        
        
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Al = hypo_morpho_vriables_gotm_grid[2]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxic_factor function
        result = annual_anoxic_factor(C, time_series,Al, A0=23.67*10**6 , threshold=0.5)

        all_annual_AF_rcp26 = pd.concat([all_annual_AF_rcp26 , result], axis=1)
        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_anoxic_factor_hadgem_rcp26_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_anoxic_factor'])
#ipsl       
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
        
        all_weights= np.append(all_weights , weights) 
        
        
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Al = hypo_morpho_vriables_gotm_grid[2]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxic_factor function
        result = annual_anoxic_factor(C, time_series,Al, A0=23.67*10**6 , threshold=0.5)

        all_annual_AF_rcp26 = pd.concat([all_annual_AF_rcp26 , result], axis=1)
        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_anoxic_factor_ipsl_rcp26_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_anoxic_factor'])
#miroc       
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
        
        all_weights= np.append(all_weights , weights) 
        
        
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Al = hypo_morpho_vriables_gotm_grid[2]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxic_factor function
        result = annual_anoxic_factor(C, time_series,Al, A0=23.67*10**6 , threshold=0.5)

        all_annual_AF_rcp26 = pd.concat([all_annual_AF_rcp26 , result], axis=1)
        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_anoxic_factor_miroc_rcp26_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_anoxic_factor'])
        

#%%Uncertainity partitioning on all_annual_AF_rcp26

anova_annual_AF_rcp26=annova_uncertainity(all_annual_AF_rcp26)

anova_annual_AF_rcp26.describe().loc['mean', :]
"""
GCMs             67.687575
param            31.551958
interaction       0.760467
GCMs/param        3.542819
year           2052.500000
Name: mean, dtype: float64
"""


anova_annual_AF_rcp26.describe().loc['std', :]
"""
GCMs           19.461802
param          19.110316
interaction     0.705328
GCMs/param      3.499083
year           27.279418
Name: std, dtype: float64
"""
#80 years:
anova_annual_80years_AF_rcp26=annova_uncertainity(all_annual_AF_rcp26[all_annual_AF_rcp26.index>2019])


anova_annual_80years_AF_rcp26.describe().loc['mean', :]
"""
GCMs             69.276337
param            29.992505
interaction       0.731158
GCMs/param        3.765238
year           2059.500000
Name: mean, dtype: float64
"""


anova_annual_80years_AF_rcp26.describe().loc['std', :]

"""
GCMs           18.442281
param          18.178007
interaction     0.639334
GCMs/param      3.675612
year           23.237900
Name: std, dtype: float64

"""

autocorr_MK_org_modif_sens_slope_test(anova_annual_80years_AF_rcp26["GCMs"]) 
(0.10584211286658138,
 'positively autocorrelated',
 'no trend',
 0.32479356737896437,
 0,
 0)



autocorr_MK_org_modif_sens_slope_test(anova_annual_80years_AF_rcp26["param"]) 
(0.4291317356800156,
 'positively autocorrelated',
 'no trend',
 0.3166945320729968,
 0,
 0)
#%%%RCP6.0

#%% annual anoxic factor_rcp60

all_annual_AF_rcp60=pd.DataFrame([])
all_weights= np.array([])


#gfdl

# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/gfdl_senarios/rcp60'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_gfdl_rcp60_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Al = hypo_morpho_vriables_gotm_grid[2]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxic_factor function
        result = annual_anoxic_factor(C, time_series,Al, A0=23.67*10**6 , threshold=0.5)

        all_annual_AF_rcp60 = pd.concat([all_annual_AF_rcp60 , result], axis=1)
        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_anoxic_factor_gfdl_rcp60_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_anoxic_factor'])
        
#hadgem               
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
        
        all_weights= np.append(all_weights , weights) 
        
        
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Al = hypo_morpho_vriables_gotm_grid[2]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxic_factor function
        result = annual_anoxic_factor(C, time_series,Al, A0=23.67*10**6 , threshold=0.5)

        all_annual_AF_rcp60 = pd.concat([all_annual_AF_rcp60 , result], axis=1)
        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_anoxic_factor_hadgem_rcp60_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_anoxic_factor'])
#ipsl       
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
        
        all_weights= np.append(all_weights , weights) 
        
        
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Al = hypo_morpho_vriables_gotm_grid[2]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxic_factor function
        result = annual_anoxic_factor(C, time_series,Al, A0=23.67*10**6 , threshold=0.5)

        all_annual_AF_rcp60 = pd.concat([all_annual_AF_rcp60 , result], axis=1)
        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_anoxic_factor_ipsl_rcp60_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_anoxic_factor'])
#miroc       
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
        
        all_weights= np.append(all_weights , weights) 
        
        
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Al = hypo_morpho_vriables_gotm_grid[2]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxic_factor function
        result = annual_anoxic_factor(C, time_series,Al, A0=23.67*10**6 , threshold=0.5)

        all_annual_AF_rcp60 = pd.concat([all_annual_AF_rcp60 , result], axis=1)
        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_anoxic_factor_miroc_rcp60_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_anoxic_factor'])
        

#%%Uncertainity partitioning on all_annual_AF_rcp60

anova_annual_AF_rcp60=annova_uncertainity(all_annual_AF_rcp60)

anova_annual_AF_rcp60.describe().loc['mean', :]
"""
GCMs             72.121601
param            27.044092
interaction       0.834307
GCMs/param        4.966745
year           2052.500000
Name: mean, dtype: float64
"""


anova_annual_AF_rcp60.describe().loc['std', :]
"""
GCMs           18.965790
param          18.402505
interaction     0.875938
GCMs/param      5.006844
year           27.279418
Name: std, dtype: float64
"""

#80 years:
anova_annual_80years_AF_rcp60=annova_uncertainity(all_annual_AF_rcp60[all_annual_AF_rcp60.index>2019])


anova_annual_80years_AF_rcp60.describe().loc['mean', :]
"""
GCMs             72.117260
param            27.038247
interaction       0.844493
GCMs/param        4.763388
year           2059.500000
Name: mean, dtype: float64
"""


anova_annual_80years_AF_rcp60.describe().loc['std', :]

"""
GCMs           19.295364
param          18.702199
interaction     0.904076
GCMs/param      4.460266
year           23.237900
Name: std, dtype: float64

"""
autocorr_MK_org_modif_sens_slope_test(anova_annual_AF_rcp60["GCMs"]) 
(0.1293320665807748,
 'positively autocorrelated',
 'no trend',
 0.17874881880496374,
 0,
 0)



autocorr_MK_org_modif_sens_slope_test(anova_annual_AF_rcp60["param"]) 
(0.6327347705638106,
 'positively autocorrelated',
 'no trend',
 0.1637503824840536,
 0,
 0)
#%% GLUE method on all_annual_AF_rcp26 
          

        
#all_annual_AF_rcp26= all_annual_AF_rcp26.set_index(all_annual_AF_rcp26['Datetime'])


# annual anoxic duration  
timeseries_year_rcp26= all_annual_AF_rcp26.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_annual_AF_rcp26.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights))

# Build glue df
glue_df_annual_anoxic_factor_rcp26 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_df_annual_anoxic_factor_rcp26=glue_df_annual_anoxic_factor_rcp26.set_index(timeseries_year_rcp26)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory
glue_df_annual_anoxic_factor_rcp26.to_csv('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/all_4_models/rcp26/glue_df_anoxic_factor_rcp26.csv')
        



#%% GLUE method on all_annual_AF_rcp60 
          

        
#all_annual_AF_rcp60= all_annual_AF_rcp60.set_index(all_annual_AF_rcp60['Datetime'])


# annual anoxic duration  
timeseries_year_rcp60= all_annual_AF_rcp60.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_annual_AF_rcp60.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights))

# Build glue df
glue_df_annual_anoxic_factor_rcp60 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_df_annual_anoxic_factor_rcp60=glue_df_annual_anoxic_factor_rcp60.set_index(timeseries_year_rcp60)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory
glue_df_annual_anoxic_factor_rcp60.to_csv('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/all_4_models/rcp60/glue_df_anoxic_factor_rcp60.csv')
        


#%%RCP8.5


#%% annual anoxic factor_rcp85

all_annual_AF_rcp85=pd.DataFrame([])
all_weights= np.array([])


#gfdl

# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/gfdl_senarios/rcp85'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_gfdl_rcp85_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Al = hypo_morpho_vriables_gotm_grid[2]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxic_factor function
        result = annual_anoxic_factor(C, time_series,Al, A0=23.67*10**6 , threshold=0.5)

        all_annual_AF_rcp85 = pd.concat([all_annual_AF_rcp85 , result], axis=1)
        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_anoxic_factor_gfdl_rcp85_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_anoxic_factor'])
        
#hadgem               
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
        
        all_weights= np.append(all_weights , weights) 
        
        
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Al = hypo_morpho_vriables_gotm_grid[2]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxic_factor function
        result = annual_anoxic_factor(C, time_series,Al, A0=23.67*10**6 , threshold=0.5)

        all_annual_AF_rcp85 = pd.concat([all_annual_AF_rcp85 , result], axis=1)
        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_anoxic_factor_hadgem_rcp85_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_anoxic_factor'])
#ipsl       
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
        
        all_weights= np.append(all_weights , weights) 
        
        
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Al = hypo_morpho_vriables_gotm_grid[2]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxic_factor function
        result = annual_anoxic_factor(C, time_series,Al, A0=23.67*10**6 , threshold=0.5)

        all_annual_AF_rcp85 = pd.concat([all_annual_AF_rcp85 , result], axis=1)
        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_anoxic_factor_ipsl_rcp85_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_anoxic_factor'])
#miroc       
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
        
        all_weights= np.append(all_weights , weights) 
        
        
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Al = hypo_morpho_vriables_gotm_grid[2]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxic_factor function
        result = annual_anoxic_factor(C, time_series,Al, A0=23.67*10**6 , threshold=0.5)

        all_annual_AF_rcp85 = pd.concat([all_annual_AF_rcp85 , result], axis=1)
        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_anoxic_factor_miroc_rcp85_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_anoxic_factor'])
        

#%%Uncertainity partitioning on all_annual_AF_rcp85

anova_annual_AF_rcp85=annova_uncertainity(all_annual_AF_rcp85)

anova_annual_AF_rcp85.describe().loc['mean', :]
"""
GCMs             81.007297
param            18.298882
interaction       0.693821
GCMs/param        7.703245
year           2052.500000
Name: mean, dtype: float64
"""


anova_annual_AF_rcp85.describe().loc['std', :]
"""
GCMs           14.465636
param          13.900571
interaction     0.764163
GCMs/param      6.414142
year           27.279418
Name: std, dtype: float64
"""

#80 years:
anova_annual_80years_AF_rcp85=annova_uncertainity(all_annual_AF_rcp85[all_annual_AF_rcp85.index>2019])


anova_annual_80years_AF_rcp85.describe().loc['mean', :]
"""
GCMs             81.531283
param            17.760640
interaction       0.708077
GCMs/param        8.180962
year           2059.500000
Name: mean, dtype: float64
"""


anova_annual_80years_AF_rcp85.describe().loc['std', :]

"""
GCMs           14.610592
param          13.962809
interaction     0.796809
GCMs/param      6.750728
year           23.237900
Name: std, dtype: float64
"""


autocorr_MK_org_modif_sens_slope_test(anova_annual_80years_AF_rcp85["GCMs"]) 
(0.0544842546605573,
 'positively autocorrelated',
 'no trend',
 0.48337871201888016,
 0,
 0)



autocorr_MK_org_modif_sens_slope_test(anova_annual_80years_AF_rcp85["param"]) 
(0.6781407331528779,
 'positively autocorrelated',
 'no trend',
 0.49828253375891407,
 0,
 0)

#%% GLUE method on all_annual_AF_rcp85 
          

        
#all_annual_AF_rcp85= all_annual_AF_rcp85.set_index(all_annual_AF_rcp85['Datetime'])


# annual anoxic duration  
timeseries_year_rcp85= all_annual_AF_rcp85.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_annual_AF_rcp85.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights))

# Build glue df
glue_df_annual_anoxic_factor_rcp85 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_df_annual_anoxic_factor_rcp85=glue_df_annual_anoxic_factor_rcp85.set_index(timeseries_year_rcp85)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory
glue_df_annual_anoxic_factor_rcp85.to_csv('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/all_4_models/rcp85/glue_df_anoxic_factor_rcp85.csv')
        
       
#%% Plotting of annual AF, May_Sep AF summer AF of his 


# the whole years



#%%#####Plotting:
    

#%%Plot of Anova test on all_annual_AF_rcps+ his 
# Define the directory path
directory_path = r'C:\Users\mahta\OneDrive\Documents\Chapter_1_PhD_py_codes_results\Future_simulation_results\all_4_models\uncertainty'

# Change the current working directory
os.chdir(directory_path)     
    
######his_annual_AF

#years
contributions_annual_AF_his_years=anova_annual_AF_his['year']
#GCMs
gcm_contributions_annual_AF_his= anova_annual_AF_his['GCMs']
#Param
param_contributions_annual_AF_his=anova_annual_AF_his['param']
#interaction
interact_contributions_annual_AF_his =anova_annual_AF_his['interaction']



# the whole RCPs years


######rcp26

#years
contributions_annual_AF_rcp26_years=anova_annual_AF_rcp26['year']
#GCMs
gcm_contributions_annual_AF_rcp26 = anova_annual_AF_rcp26['GCMs']
#Param
param_contributions_annual_AF_rcp26 =anova_annual_AF_rcp26['param']
#interaction
interact_contributions_annual_AF_rcp26 =anova_annual_AF_rcp26['interaction']

######rcp60

#years
contributions_annual_AF_rcp60_years=anova_annual_AF_rcp60['year']
#GCMs
gcm_contributions_annual_AF_rcp60 = anova_annual_AF_rcp60['GCMs']
#Param
param_contributions_annual_AF_rcp60 =anova_annual_AF_rcp60['param']
#interaction
interact_contributions_annual_AF_rcp60 =anova_annual_AF_rcp60['interaction']




######rcp85

#years
contributions_annual_AF_rcp85_years=anova_annual_AF_rcp85['year']
#GCMs
gcm_contributions_annual_AF_rcp85 = anova_annual_AF_rcp85['GCMs']
#Param
param_contributions_annual_AF_rcp85 =anova_annual_AF_rcp85['param']
#interaction
interact_contributions_annual_AF_rcp85 =anova_annual_AF_rcp85['interaction']




######Plotting:

# Define the directory path
directory_path = r'C:\Users\mahta\OneDrive\Documents\Chapter_1_PhD_py_codes_results\Future_simulation_results\all_4_models\uncertainty'

# Change the current working directory
os.chdir(directory_path)     


import matplotlib.pyplot as plt
from matplotlib.patches import Patch

# Define colors explicitly as RGB tuples
colors = [(0.96, 0.80, 0.69), (0.6, 0.4, 0.8), (0, 0, 1)]  # Flesh, Dark Orchid, Blue

# Create a figure with three subplots
fig, axs = plt.subplots(2, 2, figsize=(24, 12), sharey=True)

# Define data for each subplot (assuming you have defined your data earlier)
# Subplot for rcp26
axs[0, 0].fill_between(contributions_annual_AF_his_years, 0, gcm_contributions_annual_AF_his , label='GCMs', alpha=0.7, color=colors[0], edgecolor='black')
axs[0, 0].fill_between(contributions_annual_AF_his_years, gcm_contributions_annual_AF_his , gcm_contributions_annual_AF_his + param_contributions_annual_AF_his, label='Parameters', alpha=0.7, color=colors[1], edgecolor='black')
axs[0, 0].fill_between(contributions_annual_AF_his_years, gcm_contributions_annual_AF_his  + param_contributions_annual_AF_his, gcm_contributions_annual_AF_his + param_contributions_annual_AF_his + interact_contributions_annual_AF_his, label='Interactions', alpha=0.7, color=colors[2], edgecolor='black')
axs[0, 0].set_title('(a) His', fontsize=24)
axs[0, 0].set_ylim(0,100)
axs[0, 0].set_xlim(1861, 2005)
axs[0, 0].tick_params(axis='both', which='major', labelsize=20)

# Subplot for rcp26
axs[0, 1].fill_between(contributions_annual_AF_rcp26_years, 0, gcm_contributions_annual_AF_rcp26, label='GCMs', alpha=0.7, color=colors[0], edgecolor='black')
axs[0, 1].fill_between(contributions_annual_AF_rcp26_years, gcm_contributions_annual_AF_rcp26, gcm_contributions_annual_AF_rcp26 + param_contributions_annual_AF_rcp26, label='Parameters', alpha=0.7, color=colors[1], edgecolor='black')
axs[0, 1].fill_between(contributions_annual_AF_rcp26_years, gcm_contributions_annual_AF_rcp26 + param_contributions_annual_AF_rcp26, gcm_contributions_annual_AF_rcp26 + param_contributions_annual_AF_rcp26 + interact_contributions_annual_AF_rcp26, label='Interactions', alpha=0.7, color=colors[2], edgecolor='black')
axs[0, 1].set_title('(b) RCP2.6', fontsize=24)
axs[0, 1].set_ylim(0,100)
axs[0, 1].set_xlim(2006, 2099)
axs[0, 1].tick_params(axis='both', which='major', labelsize=20)

# Subplot for rcp60
axs[1, 0].fill_between(contributions_annual_AF_rcp60_years, 0, gcm_contributions_annual_AF_rcp60, label='GCMs', alpha=0.7, color=colors[0], edgecolor='black')
axs[1, 0].fill_between(contributions_annual_AF_rcp60_years, gcm_contributions_annual_AF_rcp60, gcm_contributions_annual_AF_rcp60 + param_contributions_annual_AF_rcp60, label='Parameters', alpha=0.7, color=colors[1], edgecolor='black')
axs[1, 0].fill_between(contributions_annual_AF_rcp60_years, gcm_contributions_annual_AF_rcp60 + param_contributions_annual_AF_rcp60, gcm_contributions_annual_AF_rcp60 + param_contributions_annual_AF_rcp60 + interact_contributions_annual_AF_rcp60, label='Interactions', alpha=0.7, color=colors[2], edgecolor='black')
axs[1, 0].set_title('(c) RCP6.0', fontsize=24)
axs[1, 0].set_ylim(0,100)
axs[1, 0].set_xlim(2006, 2099)
axs[1, 0].tick_params(axis='both', which='major', labelsize=20)

# Subplot for rcp85
axs[1, 1].fill_between(contributions_annual_AF_rcp85_years, 0, gcm_contributions_annual_AF_rcp85, label='GCMs', alpha=0.7, color=colors[0], edgecolor='black')
axs[1, 1].fill_between(contributions_annual_AF_rcp85_years, gcm_contributions_annual_AF_rcp85, gcm_contributions_annual_AF_rcp85 + param_contributions_annual_AF_rcp85, label='Parameters', alpha=0.7, color=colors[1], edgecolor='black')
axs[1, 1].fill_between(contributions_annual_AF_rcp85_years, gcm_contributions_annual_AF_rcp85 + param_contributions_annual_AF_rcp85, gcm_contributions_annual_AF_rcp85 + param_contributions_annual_AF_rcp85 + interact_contributions_annual_AF_rcp85, label='Interactions', alpha=0.7, color=colors[2], edgecolor='black')
axs[1, 1].set_title('(d) RCP8.5', fontsize=24)
axs[1, 1].set_ylim(0,100)
axs[1, 1].set_xlim(2006, 2099)
axs[1, 1].tick_params(axis='both', which='major', labelsize=20)

# Adding labels and title with increased font size
# fig.text(0.5, 0.08, 'Year', ha='center', fontsize=20)
fig.text(0.08, 0.5, 'Uncertainty sources in annual anoxic factor [%]', va='center', rotation='vertical', fontsize=26)

# Create legend handles and labels
legend_handles = [Patch(facecolor=colors[0], edgecolor='black'), 
                  Patch(facecolor=colors[1], edgecolor='black'), 
                  Patch(facecolor=colors[2], edgecolor='black')]
legend_labels = ['GCMs', 'Parameters', 'Interactions']

# Add a single legend outside the subplots
fig.legend(legend_handles, legend_labels,bbox_to_anchor=(0.7, 0.1), fontsize=24, ncol=3)


# Save the plot
plt.savefig('uncertainty_annualAF_allyears_rcps_His.png', dpi=300, bbox_inches='tight')

plt.show()


#%%
######Plotting:

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
axs[0, 0].fill_between(contributions_annual_AF_his_years, 0, gcm_contributions_annual_AF_his , label='GCMs', alpha=0.7, color=colors[0], edgecolor='black')
axs[0, 0].fill_between(contributions_annual_AF_his_years, gcm_contributions_annual_AF_his , gcm_contributions_annual_AF_his + param_contributions_annual_AF_his, label='Parameters', alpha=0.7, color=colors[1], edgecolor='black')
axs[0, 0].fill_between(contributions_annual_AF_his_years, gcm_contributions_annual_AF_his  + param_contributions_annual_AF_his, gcm_contributions_annual_AF_his + param_contributions_annual_AF_his + interact_contributions_annual_AF_his, label='Interactions', alpha=0.7, color=colors[2], edgecolor='black')
axs[0, 0].set_title('His', fontsize=20)
axs[0, 0].set_ylim(0,100)
axs[0, 0].set_xlim(1861, 2005)
axs[0, 0].tick_params(axis='both', which='major', labelsize=20)

# Subplot for rcp26
axs[0, 1].fill_between(contributions_annual_AF_rcp26_years, 0, gcm_contributions_annual_AF_rcp26, label='GCMs', alpha=0.7, color=colors[0], edgecolor='black')
axs[0, 1].fill_between(contributions_annual_AF_rcp26_years, gcm_contributions_annual_AF_rcp26, gcm_contributions_annual_AF_rcp26 + param_contributions_annual_AF_rcp26, label='Parameters', alpha=0.7, color=colors[1], edgecolor='black')
axs[0, 1].fill_between(contributions_annual_AF_rcp26_years, gcm_contributions_annual_AF_rcp26 + param_contributions_annual_AF_rcp26, gcm_contributions_annual_AF_rcp26 + param_contributions_annual_AF_rcp26 + interact_contributions_annual_AF_rcp26, label='Interactions', alpha=0.7, color=colors[2], edgecolor='black')
axs[0, 1].set_title('RCP2.6', fontsize=20)
axs[0, 1].set_ylim(0,100)
axs[0, 1].set_xlim(2006, 2099)
axs[0, 1].tick_params(axis='both', which='major', labelsize=20)

# Subplot for rcp60
axs[1, 0].fill_between(contributions_annual_AF_rcp60_years, 0, gcm_contributions_annual_AF_rcp60, label='GCMs', alpha=0.7, color=colors[0], edgecolor='black')
axs[1, 0].fill_between(contributions_annual_AF_rcp60_years, gcm_contributions_annual_AF_rcp60, gcm_contributions_annual_AF_rcp60 + param_contributions_annual_AF_rcp60, label='Parameters', alpha=0.7, color=colors[1], edgecolor='black')
axs[1, 0].fill_between(contributions_annual_AF_rcp60_years, gcm_contributions_annual_AF_rcp60 + param_contributions_annual_AF_rcp60, gcm_contributions_annual_AF_rcp60 + param_contributions_annual_AF_rcp60 + interact_contributions_annual_AF_rcp60, label='Interactions', alpha=0.7, color=colors[2], edgecolor='black')
axs[1, 0].set_title('RCP6.0', fontsize=20)
axs[1, 0].set_ylim(0,100)
axs[1, 0].set_xlim(2006, 2099)
axs[1, 0].tick_params(axis='both', which='major', labelsize=20)

# Subplot for rcp85
axs[1, 1].fill_between(contributions_annual_AF_rcp85_years, 0, gcm_contributions_annual_AF_rcp85, label='GCMs', alpha=0.7, color=colors[0], edgecolor='black')
axs[1, 1].fill_between(contributions_annual_AF_rcp85_years, gcm_contributions_annual_AF_rcp85, gcm_contributions_annual_AF_rcp85 + param_contributions_annual_AF_rcp85, label='Parameters', alpha=0.7, color=colors[1], edgecolor='black')
axs[1, 1].fill_between(contributions_annual_AF_rcp85_years, gcm_contributions_annual_AF_rcp85 + param_contributions_annual_AF_rcp85, gcm_contributions_annual_AF_rcp85 + param_contributions_annual_AF_rcp85 + interact_contributions_annual_AF_rcp85, label='Interactions', alpha=0.7, color=colors[2], edgecolor='black')
axs[1, 1].set_title('RCP8.5', fontsize=20)
axs[1, 1].set_ylim(0,100)
axs[1, 1].set_xlim(2006, 2099)
axs[1, 1].tick_params(axis='both', which='major', labelsize=20)

# Adding labels and title with increased font size
# fig.text(0.5, 0.08, 'Year', ha='center', fontsize=20)
fig.text(0.08, 0.5, 'Uncertainty sources in annual anoxic factor [%]', va='center', rotation='vertical', fontsize=22)

# Create legend handles and labels
legend_handles = [Patch(facecolor=colors[0], edgecolor='black'), 
                  Patch(facecolor=colors[1], edgecolor='black'), 
                  Patch(facecolor=colors[2], edgecolor='black')]
legend_labels = ['GCMs', 'Parameters', 'Interactions']

# Add a single legend outside the subplots
fig.legend(legend_handles, legend_labels,bbox_to_anchor=(0.75, 0.06), fontsize=22, ncol=3)


# Save the plot
plt.savefig('uncertainty_annualAF_allyears_rcps_his.png', dpi=300, bbox_inches='tight')

plt.show()


#%% analyses onley for 80 years


########rcp26

#year
contributions_80years_annual_AF_rcp26_years=anova_annual_AF_rcp26[anova_annual_AF_rcp26.year>2019].year
#gcms
gcm_contributions_80years_annual_AF_rcp26 = anova_annual_AF_rcp26[anova_annual_AF_rcp26.year>2019]['GCMs']
#param
param_contributions_80years_annual_AF_rcp26 =anova_annual_AF_rcp26[anova_annual_AF_rcp26.year>2019]['param']
#interaction
interact_contributions_80years_annual_AF_rcp26 =anova_annual_AF_rcp26[anova_annual_AF_rcp26.year>2019]['interaction']



#########rcp60

#year
contributions_80years_annual_AF_rcp60_years=anova_annual_AF_rcp60[anova_annual_AF_rcp60.year>2019].year
#gcms
gcm_contributions_80years_annual_AF_rcp60 = anova_annual_AF_rcp60[anova_annual_AF_rcp60.year>2019]['GCMs']
#param
param_contributions_80years_annual_AF_rcp60 =anova_annual_AF_rcp60[anova_annual_AF_rcp60.year>2019]['param']
#interaction
interact_contributions_80years_annual_AF_rcp60 =anova_annual_AF_rcp60[anova_annual_AF_rcp60.year>2019]['interaction']


##########rcp85
#year
contributions_80years_annual_AF_rcp85_years=anova_annual_AF_rcp85[anova_annual_AF_rcp85.year>2019].year
#gcms
gcm_contributions_80years_annual_AF_rcp85 = anova_annual_AF_rcp85[anova_annual_AF_rcp85.year>2019]['GCMs']
#param
param_contributions_80years_annual_AF_rcp85 =anova_annual_AF_rcp85[anova_annual_AF_rcp85.year>2019]['param']
#interaction
interact_contributions_80years_annual_AF_rcp85 =anova_annual_AF_rcp85[anova_annual_AF_rcp85.year>2019]['interaction']


######Plotting:
# Define the directory path
directory_path = r'C:\Users\mahta\OneDrive\Documents\Chapter_1_PhD_py_codes_results\Future_simulation_results\all_4_models\uncertainty'

# Change the current working directory
os.chdir(directory_path)     
    
    

import matplotlib.pyplot as plt
from matplotlib.patches import Patch

# Define colors explicitly as RGB tuples
colors = [(0.96, 0.80, 0.69), (0.6, 0.4, 0.8), (0, 0, 1)]  # Flesh, Dark Orchid, Blue

# Create a figure with three subplots
fig, axs = plt.subplots(1, 3, figsize=(24, 5), sharey=True)

# Define data for each subplot (assuming you have defined your data earlier)

# Subplot for rcp26
axs[0].fill_between(contributions_80years_annual_AF_rcp26_years, 0, gcm_contributions_80years_annual_AF_rcp26, label='GCMs', alpha=0.7, color=colors[0], edgecolor='black')
axs[0].fill_between(contributions_80years_annual_AF_rcp26_years, gcm_contributions_80years_annual_AF_rcp26, gcm_contributions_80years_annual_AF_rcp26 + param_contributions_80years_annual_AF_rcp26, label='Parameters', alpha=0.7, color=colors[1], edgecolor='black')
axs[0].fill_between(contributions_80years_annual_AF_rcp26_years, gcm_contributions_80years_annual_AF_rcp26 + param_contributions_80years_annual_AF_rcp26, gcm_contributions_80years_annual_AF_rcp26 + param_contributions_80years_annual_AF_rcp26 + interact_contributions_80years_annual_AF_rcp26, label='Interactions', alpha=0.7, color=colors[2], edgecolor='black')
axs[0].set_title('(a) RCP2.6', fontsize=20)
axs[0].set_ylim(0,100)
axs[0].set_xlim(2020, 2099)
axs[0].tick_params(axis='both', which='major', labelsize=20)
#axs[0].set_xticks(np.arange(2020, 2100, 10),fontsize=20)

# Subplot for rcp60
axs[1].fill_between(contributions_80years_annual_AF_rcp60_years, 0, gcm_contributions_80years_annual_AF_rcp60, label='GCMs', alpha=0.7, color=colors[0], edgecolor='black')
axs[1].fill_between(contributions_80years_annual_AF_rcp60_years, gcm_contributions_80years_annual_AF_rcp60, gcm_contributions_80years_annual_AF_rcp60 + param_contributions_80years_annual_AF_rcp60, label='Parameters', alpha=0.7, color=colors[1], edgecolor='black')
axs[1].fill_between(contributions_80years_annual_AF_rcp60_years, gcm_contributions_80years_annual_AF_rcp60 + param_contributions_80years_annual_AF_rcp60, gcm_contributions_80years_annual_AF_rcp60 + param_contributions_80years_annual_AF_rcp60 + interact_contributions_80years_annual_AF_rcp60, label='Interactions', alpha=0.7, color=colors[2], edgecolor='black')
axs[1].set_title('(b) RCP6.0', fontsize=20)
axs[1].set_ylim(0,100)
axs[1].set_xlim(2020, 2099)
axs[1].tick_params(axis='both', which='major', labelsize=20)
#axs[1].set_xticks(np.arange(2020, 2100, 20),fontsize=20)


# Subplot for rcp85
axs[2].fill_between(contributions_80years_annual_AF_rcp85_years, 0, gcm_contributions_80years_annual_AF_rcp85, label='GCMs', alpha=0.7, color=colors[0], edgecolor='black')
axs[2].fill_between(contributions_80years_annual_AF_rcp85_years, gcm_contributions_80years_annual_AF_rcp85, gcm_contributions_80years_annual_AF_rcp85 + param_contributions_80years_annual_AF_rcp85, label='Parameters', alpha=0.7, color=colors[1], edgecolor='black')
axs[2].fill_between(contributions_80years_annual_AF_rcp85_years, gcm_contributions_80years_annual_AF_rcp85 + param_contributions_80years_annual_AF_rcp85, gcm_contributions_80years_annual_AF_rcp85 + param_contributions_80years_annual_AF_rcp85 + interact_contributions_80years_annual_AF_rcp85, label='Interactions', alpha=0.7, color=colors[2], edgecolor='black')
axs[2].set_title('(c) RCP8.5', fontsize=20)
axs[2].set_ylim(0,100)
axs[2].set_xlim(2020, 2099)
axs[2].tick_params(axis='both', which='major', labelsize=20)
#axs[2].set_xticks(np.arange(2020, 2100, 20),fontsize=20)


# Adding labels and title with increased font size
# fig.text(0.5, 0.08, 'Year', ha='center', fontsize=20)
fig.text(0.08, 0.5, 'Uncertainty sources in annual AF [%]', va='center', rotation='vertical', fontsize=22)

# Create legend handles and labels
legend_handles = [Patch(facecolor=colors[0], edgecolor='black'), 
                  Patch(facecolor=colors[1], edgecolor='black'), 
                  Patch(facecolor=colors[2], edgecolor='black')]
legend_labels = ['GCMs', 'Parameters', 'Interactions']

# Add a single legend outside the subplots
fig.legend(legend_handles, legend_labels,bbox_to_anchor=(0.7, 0.06), fontsize=22 , ncol=3)



# Save the plot
plt.savefig('uncertainty_annualAF_80years_rcps.png', dpi=300, bbox_inches='tight')

plt.show()






























































#%%monthly_table_of_anoxic_factor

#%%monthly_table_of_anoxic_factor_gfdl_his

# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/gfdl_senarios/his'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_gfdl_his_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Al = hypo_morpho_vriables_gotm_grid[2]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxic_factor function
        result = monthly_table_of_anoxic_factor(C, time_series,Al, A0=23.67*10**6 , threshold=0.5)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_table_of_anoxic_factor_gfdl_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        


#%%monthly_table_of_anoxic_factor_gfdl_rcp26

# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/gfdl_senarios/rcp26'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_gfdl_rcp26_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Al = hypo_morpho_vriables_gotm_grid[2]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxic_factor function
        result = monthly_table_of_anoxic_factor(C, time_series,Al, A0=23.67*10**6 , threshold=0.5)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_table_of_anoxic_factor_gfdl_rcp26_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
 

#%%monthly_table_of_anoxic_factor_gfdl_rcp60

# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/gfdl_senarios/rcp60'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_gfdl_rcp60_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Al = hypo_morpho_vriables_gotm_grid[2]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxic_factor function
        result = monthly_table_of_anoxic_factor(C, time_series,Al, A0=23.67*10**6 , threshold=0.5)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_table_of_anoxic_factor_gfdl_rcp60_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        

#%%monthly_table_of_anoxic_factor_gfdl_rcp85

# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/gfdl_senarios/rcp85'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_gfdl_rcp85_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Al = hypo_morpho_vriables_gotm_grid[2]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxic_factor function
        result = monthly_table_of_anoxic_factor(C, time_series,Al, A0=23.67*10**6 , threshold=0.5)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_table_of_anoxic_factor_gfdl_rcp85_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                
#%%hadgem

#%%monthly_table_of_anoxic_factor_hadgem_his

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
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Al = hypo_morpho_vriables_gotm_grid[2]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxic_factor function
        result = monthly_table_of_anoxic_factor(C, time_series,Al, A0=23.67*10**6 , threshold=0.5)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_table_of_anoxic_factor_hadgem_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
 
#%%monthly_table_of_anoxic_factor_hadgem_rcp26

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
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Al = hypo_morpho_vriables_gotm_grid[2]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxic_factor function
        result = monthly_table_of_anoxic_factor(C, time_series,Al, A0=23.67*10**6 , threshold=0.5)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_table_of_anoxic_factor_hadgem_rcp26_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                

#%%monthly_table_of_anoxic_factor_hadgem_rcp60

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
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Al = hypo_morpho_vriables_gotm_grid[2]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxic_factor function
        result = monthly_table_of_anoxic_factor(C, time_series,Al, A0=23.67*10**6 , threshold=0.5)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_table_of_anoxic_factor_hadgem_rcp60_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
   
#%%monthly_table_of_anoxic_factor_hadgem_rcp85

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
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Al = hypo_morpho_vriables_gotm_grid[2]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxic_factor function
        result = monthly_table_of_anoxic_factor(C, time_series,Al, A0=23.67*10**6 , threshold=0.5)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_table_of_anoxic_factor_hadgem_rcp85_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
            
#%%ipsl

#%%monthly_table_of_anoxic_factor_ipsl_his

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
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Al = hypo_morpho_vriables_gotm_grid[2]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxic_factor function
        result = monthly_table_of_anoxic_factor(C, time_series,Al, A0=23.67*10**6 , threshold=0.5)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_table_of_anoxic_factor_ipsl_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        

#%%monthly_table_of_anoxic_factor_ipsl_rcp26

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
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Al = hypo_morpho_vriables_gotm_grid[2]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxic_factor function
        result = monthly_table_of_anoxic_factor(C, time_series,Al, A0=23.67*10**6 , threshold=0.5)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_table_of_anoxic_factor_ipsl_rcp26_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                

#%%monthly_table_of_anoxic_factor_ipsl_rcp60

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
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Al = hypo_morpho_vriables_gotm_grid[2]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxic_factor function
        result = monthly_table_of_anoxic_factor(C, time_series,Al, A0=23.67*10**6 , threshold=0.5)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_table_of_anoxic_factor_ipsl_rcp60_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                


#%%monthly_table_of_anoxic_factor_ipsl_rcp85

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
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Al = hypo_morpho_vriables_gotm_grid[2]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxic_factor function
        result = monthly_table_of_anoxic_factor(C, time_series,Al, A0=23.67*10**6 , threshold=0.5)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_table_of_anoxic_factor_ipsl_rcp85_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
  
#%%monthly_table_of_anoxic_factor_miroc_his

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
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Al = hypo_morpho_vriables_gotm_grid[2]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxic_factor function
        result = monthly_table_of_anoxic_factor(C, time_series,Al, A0=23.67*10**6 , threshold=0.5)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_table_of_anoxic_factor_miroc_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
 
#%%monthly_table_of_anoxic_factor_miroc_rcp26

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
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Al = hypo_morpho_vriables_gotm_grid[2]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxic_factor function
        result = monthly_table_of_anoxic_factor(C, time_series,Al, A0=23.67*10**6 , threshold=0.5)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_table_of_anoxic_factor_miroc_rcp26_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                

#%%monthly_table_of_anoxic_factor_miroc_rcp60

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
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Al = hypo_morpho_vriables_gotm_grid[2]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxic_factor function
        result = monthly_table_of_anoxic_factor(C, time_series,Al, A0=23.67*10**6 , threshold=0.5)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_table_of_anoxic_factor_miroc_rcp60_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                



#%%monthly_table_of_anoxic_factor_miroc_rcp85

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
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Al = hypo_morpho_vriables_gotm_grid[2]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxic_factor function
        result = monthly_table_of_anoxic_factor(C, time_series,Al, A0=23.67*10**6 , threshold=0.5)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_table_of_anoxic_factor_miroc_rcp85_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        


#%%sorting the indexs_annual_anoxic_factor 

glue_df_annual_anoxic_factor_his= glue_df_annual_anoxic_factor_his.sort_index()
glue_df_annual_anoxic_factor_rcp26= glue_df_annual_anoxic_factor_rcp26.sort_index()
glue_df_annual_anoxic_factor_rcp60= glue_df_annual_anoxic_factor_rcp60.sort_index()
glue_df_annual_anoxic_factor_rcp85= glue_df_annual_anoxic_factor_rcp85.sort_index()













#%%Plotting and analyses 



#%%########annual anoxic factor 

#%%ploting annual anoxic factor 

os.chdir('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/all_4_models/')

import matplotlib.pyplot as plt

fig =plt.figure(figsize=(15, 10))
ax= plt.subplot(111)


ax=plt.fill_between(glue_df_annual_anoxic_factor_his.index.astype(float), glue_df_annual_anoxic_factor_his['5%'], glue_df_annual_anoxic_factor_his['95%'], color='grey', alpha=0.2 ,  label= 'His 90% CI')
ax=plt.plot(glue_df_annual_anoxic_factor_his.index.astype(float), glue_df_annual_anoxic_factor_his['50%'].astype(float), 'k', label='His median', alpha=0.9, linewidth=3  )



ax=plt.fill_between(glue_df_annual_anoxic_factor_rcp26.index.astype(float), glue_df_annual_anoxic_factor_rcp26['5%'], glue_df_annual_anoxic_factor_rcp26['95%'], color='darkgreen', alpha=0.3 ,  label= 'RCP2.6 90% CI')
ax=plt.plot(glue_df_annual_anoxic_factor_rcp26.index.astype(float), glue_df_annual_anoxic_factor_rcp26['50%'], 'darkgreen', label='RCP2.6 median', alpha=0.9, linewidth=3  )


ax=plt.fill_between(glue_df_annual_anoxic_factor_rcp60.index.astype(float), glue_df_annual_anoxic_factor_rcp60['5%'], glue_df_annual_anoxic_factor_rcp60['95%'], color='yellow', alpha=0.3 ,  label= 'RCP6.0 90% CI')
ax=plt.plot(glue_df_annual_anoxic_factor_rcp60.index.astype(float), glue_df_annual_anoxic_factor_rcp60['50%'], 'yellow', label='RCP6.0 median', alpha=0.9, linewidth=3  )

ax=plt.fill_between(glue_df_annual_anoxic_factor_rcp85.index.astype(float), glue_df_annual_anoxic_factor_rcp85['5%'], glue_df_annual_anoxic_factor_rcp85['95%'], color='r', alpha=0.2 ,  label= 'RCP8.5 90% CI')
ax=plt.plot(glue_df_annual_anoxic_factor_rcp85.index.astype(float), glue_df_annual_anoxic_factor_rcp85['50%'], 'r', label='RCP8.5 median', alpha=0.9, linewidth=3  )

ax=plt.ylabel('Annual anoxic factor [d year$^{-1}$]' , fontsize=26)
ax=plt.xlabel('Year' , fontsize=26)
ax=plt.yticks(fontsize= 22)
ax=plt.xticks(rotation=45 , fontsize=22)
ax=plt.legend(bbox_to_anchor=(1.1, -0.2), fontsize=22 , ncol= 4)   
fig.savefig("GLUE_Timeseries_annual_anoxic_factor.png",  dpi=300, bbox_inches='tight')




#%%
np.mean(glue_df_annual_anoxic_factor_his['50%'])#5.063555360592361
np.mean(glue_df_annual_anoxic_factor_rcp26['50%'])#6.969784666438671
np.mean(glue_df_annual_anoxic_factor_rcp60['50%'])#7.55250791445209
np.mean(glue_df_annual_anoxic_factor_rcp85['50%'])#8.105683204637998

#%%anoxic_factor 30 yerars from each scenarios compare 



#anomaly 
# baseline [1976-2005]
glue_base_annual_anoxic_factor_his=glue_df_annual_anoxic_factor_his[1975 < glue_df_annual_anoxic_factor_his.index]
annual_anoxic_factor_ref=np.mean(glue_base_annual_anoxic_factor_his['50%'])
#5.348428994157849
np.mean(glue_base_annual_anoxic_factor_his['5%'])
#2.7526708668960405
np.mean(glue_base_annual_anoxic_factor_his['95%'])
#7.1168943728881695

#std
(7.1168943728881695-2.7526708668960405)/(2*1.645)
#1.3265117039489753


#near future [2030-2059]

glue_near_future_annual_anoxic_factor_rcp26=glue_df_annual_anoxic_factor_rcp26[(2029 < glue_df_annual_anoxic_factor_rcp26.index) & (glue_df_annual_anoxic_factor_rcp26.index < 2060)]
np.mean(glue_near_future_annual_anoxic_factor_rcp26['50%'])
# 7.026365220825112
np.mean(glue_near_future_annual_anoxic_factor_rcp26['5%'])
# 4.251936924002594
np.mean(glue_near_future_annual_anoxic_factor_rcp26['95%'])
# 9.062060306566359
#std
(9.062060306566359-4.251936924002594)/(2*1.645)
#1.4620435813263721




glue_near_future_annual_anoxic_factor_rcp60=glue_df_annual_anoxic_factor_rcp60[(2029 < glue_df_annual_anoxic_factor_rcp60.index) & (glue_df_annual_anoxic_factor_rcp60.index < 2060)]
np.mean(glue_near_future_annual_anoxic_factor_rcp60['50%'])
# 7.117269330197655
np.mean(glue_near_future_annual_anoxic_factor_rcp60['5%'])
# 4.373554843557299
np.mean(glue_near_future_annual_anoxic_factor_rcp60['95%'])
# 9.266727527371255
#std
(9.266727527371255-4.373554843557299)/(2*1.645)
#1.4872865300346372



glue_near_future_annual_anoxic_factor_rcp85=glue_df_annual_anoxic_factor_rcp85[(2029 < glue_df_annual_anoxic_factor_rcp85.index) & (glue_df_annual_anoxic_factor_rcp85.index < 2060)]
np.mean(glue_near_future_annual_anoxic_factor_rcp85['50%'])
# 7.559043087615576
np.mean(glue_near_future_annual_anoxic_factor_rcp85['5%'])
# 4.277467396496866
np.mean(glue_near_future_annual_anoxic_factor_rcp85['95%'])
# 10.056906170361332
#std
(10.056906170361332-4.277467396496866)/(2*1.645)
#1.7566683203235458



 
#Distant future [2070-2099]

glue_distant_future_annual_anoxic_factor_rcp26=glue_df_annual_anoxic_factor_rcp26[(2069 < glue_df_annual_anoxic_factor_rcp26.index) & (glue_df_annual_anoxic_factor_rcp26.index < 2100)]
np.mean(glue_distant_future_annual_anoxic_factor_rcp26['50%'])
#7.132601169730247
np.mean(glue_distant_future_annual_anoxic_factor_rcp26['5%'])
#4.503020774839004
np.mean(glue_distant_future_annual_anoxic_factor_rcp26['95%'])
#9.282389975854215
#std
(9.282389975854215-4.503020774839004)/(2*1.645)
#1.4526958057796995


glue_distant_future_annual_anoxic_factor_rcp60=glue_df_annual_anoxic_factor_rcp60[(2069 < glue_df_annual_anoxic_factor_rcp60.index) & (glue_df_annual_anoxic_factor_rcp60.index< 2100)]
np.mean(glue_distant_future_annual_anoxic_factor_rcp60['50%'])
#8.720957039432054
np.mean(glue_distant_future_annual_anoxic_factor_rcp60['5%'])
#5.940528865920281
np.mean(glue_distant_future_annual_anoxic_factor_rcp60['95%'])
#11.212523542831896
#std
(11.212523542831896-5.940528865920281)/(2*1.645)
#1.6024299929822539



glue_distant_future_annual_anoxic_factor_rcp85=glue_df_annual_anoxic_factor_rcp85[(2069 < glue_df_annual_anoxic_factor_rcp85.index) & (glue_df_annual_anoxic_factor_rcp85.index < 2100)]
np.mean(glue_distant_future_annual_anoxic_factor_rcp85['50%'])
#9.893120591379976
np.mean(glue_distant_future_annual_anoxic_factor_rcp85['5%'])
#6.577599051695558  
np.mean(glue_distant_future_annual_anoxic_factor_rcp85['95%'])
#12.68915312398848
#std
(12.68915312398848-6.577599051695558)/(2*1.645)
#1.8576152195419213


###====over 30 years in his and each RCPs 

# baseline [1976-2005]
autocorr_MK_org_modif_sens_slope_test(glue_base_annual_anoxic_factor_his)
(0.056001764729932804,
 'positively autocorrelated',
 'increasing',
 0.011295345713621785,
 0.04271572722268635,
 4.7255142580521445)


#near future [2030-2059]


autocorr_MK_org_modif_sens_slope_test(glue_near_future_annual_anoxic_factor_rcp26)
(0.02509986901312969,
 'positively autocorrelated',
 'no trend',
 0.15336757080984897,
 0,
 0)
autocorr_MK_org_modif_sens_slope_test(glue_near_future_annual_anoxic_factor_rcp60)
(0.013188996298485748,
 'positively autocorrelated',
 'increasing',
 0.0019070443258202285,
 0.046129209557748796,
 6.45631797158867)

autocorr_MK_org_modif_sens_slope_test(glue_near_future_annual_anoxic_factor_rcp85)
(0.019631428389436434,
 'positively autocorrelated',
 'increasing',
 0.006691154493964735,
 0.05121080329692482,
 6.780340269777007)


#Distant future [2070-2099]


autocorr_MK_org_modif_sens_slope_test(glue_distant_future_annual_anoxic_factor_rcp26)
(0.021037114587180702,
 'positively autocorrelated',
 'no trend',
 0.2389927879015219,
 0,
 0)

autocorr_MK_org_modif_sens_slope_test(glue_distant_future_annual_anoxic_factor_rcp60)
(0.013850746291506701,
 'positively autocorrelated',
 'no trend',
 0.568058623631595,
 0,
 0)
autocorr_MK_org_modif_sens_slope_test(glue_distant_future_annual_anoxic_factor_rcp85)
(0.016849810112642045,
 'positively autocorrelated',
 'increasing',
 0.04196394457941599,
 0.04728204748103548,
 9.366942789415054)




#%% 80 years from 2020 for annual_anoxic_factor


glue_80years_annual_anoxic_factor_rcp26=glue_df_annual_anoxic_factor_rcp26[2019 < glue_df_annual_anoxic_factor_rcp26.index]

glue_80years_annual_anoxic_factor_rcp60=glue_df_annual_anoxic_factor_rcp60[2019 < glue_df_annual_anoxic_factor_rcp60.index]

glue_80years_annual_anoxic_factor_rcp85=glue_df_annual_anoxic_factor_rcp85[2019 < glue_df_annual_anoxic_factor_rcp85.index]


#============= mean of first 10 yaers over 80 years 

#rcp2.6
np.mean(glue_80years_annual_anoxic_factor_rcp26[glue_80years_annual_anoxic_factor_rcp26.index<2030]['50%'])
6.805809194434355

#rcp6.0
np.mean(glue_80years_annual_anoxic_factor_rcp60[glue_80years_annual_anoxic_factor_rcp60.index<2030]['50%'])
6.778174676652554

#rcp8.5
np.mean(glue_80years_annual_anoxic_factor_rcp85[glue_80years_annual_anoxic_factor_rcp85.index<2030]['50%'])
6.800209969882897
#============== mean of last 10 yaers over 80 years 

#rcp2.6
np.mean(glue_80years_annual_anoxic_factor_rcp26[glue_80years_annual_anoxic_factor_rcp26.index>2079]['50%'])
7.195886584624096

#rcp6.0
np.mean(glue_80years_annual_anoxic_factor_rcp60[glue_80years_annual_anoxic_factor_rcp60.index>2079]['50%'])
8.801455608057209

#rcp8.5
np.mean(glue_80years_annual_anoxic_factor_rcp85[glue_80years_annual_anoxic_factor_rcp85.index>2079]['50%'])
10.042100265234383

#=========== trendline # Over the 80 years


autocorr_MK_org_modif_sens_slope_test(glue_80years_annual_anoxic_factor_rcp26['50%'])
(0.026707382429890805,
 'positively autocorrelated',
 'no trend',
 0.11283257102472444,
 0,
 0)

autocorr_MK_org_modif_sens_slope_test(glue_80years_annual_anoxic_factor_rcp60['50%'])
(0.015040265279994244,
 'positively autocorrelated',
 'increasing',
 1.9872992140790302e-13,
 0.035390484344828034,
 6.274264200925538)


autocorr_MK_org_modif_sens_slope_test(glue_80years_annual_anoxic_factor_rcp85['50%'])
(0.01875645238185793,
 'positively autocorrelated',
 'increasing',
 0.0,
 0.05513241701116823,
 6.171818276063974)


#%%If there is a trend in entire 

# in whole his
autocorr_MK_org_modif_sens_slope_test(glue_df_annual_anoxic_factor_his['50%'])
(0.08104701209658895,
 'positively autocorrelated',
 'no trend',
 0.06932527354578055,
 0,
 0)

#in intire rcp2.6
autocorr_MK_org_modif_sens_slope_test(glue_df_annual_anoxic_factor_rcp26['50%'])

(0.026247900239600688,
 'positively autocorrelated',
 'increasing',
 0.002899298398115313,
 0.009239300571900911,
 6.514249252851193)

#in entire rcp6.0
autocorr_MK_org_modif_sens_slope_test(glue_df_annual_anoxic_factor_rcp60['50%'])
(0.017686057709990998,
 'positively autocorrelated',
 'increasing',
 2.220446049250313e-16,
 0.0326453549249918,
 6.017950676033179)
#in entire rcp8.5
autocorr_MK_org_modif_sens_slope_test(glue_df_annual_anoxic_factor_rcp85['50%'])
(0.01984674835710983,
 'positively autocorrelated',
 'increasing',
 0.0,
 0.0539503723739882,
 5.435448183829658)
#slope in entire RCP8.5> RCP6.0>RCP2.6 # his no trend 



 
#%%anoxic_factor_anomaly 
os.chdir('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/all_4_models/')

import matplotlib.pyplot as plt

fig =plt.figure(figsize=(15, 11))
ax= plt.subplot(111)


ax=plt.fill_between(glue_df_annual_anoxic_factor_his[(1975 < glue_df_annual_anoxic_factor_his.index)].index.astype(float),
                      glue_df_annual_anoxic_factor_his[(1975 < glue_df_annual_anoxic_factor_his.index)]['5%'] - annual_anoxic_factor_ref,
                      glue_df_annual_anoxic_factor_his[(1975 < glue_df_annual_anoxic_factor_his.index) ]['95%'] - annual_anoxic_factor_ref,
                      color='grey', alpha=0.2, label='His 90% CI')


ax=plt.plot(glue_df_annual_anoxic_factor_his[(1975 < glue_df_annual_anoxic_factor_his.index) ].index.astype(float),
            glue_df_annual_anoxic_factor_his[(1975 < glue_df_annual_anoxic_factor_his.index)]['50%'] - annual_anoxic_factor_ref,
            'k', label='His median', alpha=0.9, linewidth=3   )

ax=plt.fill_between(glue_df_annual_anoxic_factor_rcp26.index.astype(float), glue_df_annual_anoxic_factor_rcp26['5%']-annual_anoxic_factor_ref, glue_df_annual_anoxic_factor_rcp26['95%']-annual_anoxic_factor_ref, color='darkgreen', alpha=0.3 ,  label= 'RCP6.0 90% CI')
ax=plt.plot(glue_df_annual_anoxic_factor_rcp26.index.astype(float), glue_df_annual_anoxic_factor_rcp26['50%']-annual_anoxic_factor_ref, 'darkgreen', label='RCP6.0 median', alpha=0.9, linewidth=3  )
                      
                     
ax=plt.fill_between(glue_df_annual_anoxic_factor_rcp60.index.astype(float), glue_df_annual_anoxic_factor_rcp60['5%']-annual_anoxic_factor_ref, glue_df_annual_anoxic_factor_rcp60['95%']-annual_anoxic_factor_ref, color='yellow', alpha=0.3 ,  label= 'RCP6.0 90% CI')
ax=plt.plot(glue_df_annual_anoxic_factor_rcp60.index.astype(float), glue_df_annual_anoxic_factor_rcp60['50%']-annual_anoxic_factor_ref, 'yellow', label='RCP6.0 median', alpha=0.9, linewidth=3  )
trendline_rcp60=autocorr_MK_org_modif_sens_slope_test(glue_80years_annual_anoxic_factor_rcp60['50%']-annual_anoxic_factor_ref)
ax=plt.text(2022, 9, f'y = {trendline_rcp60[-2]:.3f}x + {trendline_rcp60[-1]:.3f}, p-value <0.0001', color='orange', fontsize= 24 )

ax=plt.plot(glue_80years_annual_anoxic_factor_rcp60.index.astype(float),
        trendline_rcp60[-2] * np.arange(80) + trendline_rcp60[-1],
        linestyle='--', color='yellow', alpha=0.9, linewidth=3 , label='RCP6.0 trendline')



ax=plt.fill_between(glue_df_annual_anoxic_factor_rcp85.index.astype(float), glue_df_annual_anoxic_factor_rcp85['5%']-annual_anoxic_factor_ref, glue_df_annual_anoxic_factor_rcp85['95%']-annual_anoxic_factor_ref, color='r', alpha=0.2 ,  label= 'RCP8.5 90% CI')
ax=plt.plot(glue_df_annual_anoxic_factor_rcp85.index.astype(float), glue_df_annual_anoxic_factor_rcp85['50%']-annual_anoxic_factor_ref, 'r', label='RCP8.5 median', alpha=0.9, linewidth=3  )
trendline_rcp85=autocorr_MK_org_modif_sens_slope_test(glue_80years_annual_anoxic_factor_rcp85['50%']-annual_anoxic_factor_ref)
ax=plt.text(2022, 8, f'y = {trendline_rcp85[-2]:.3f}x + {trendline_rcp85[-1]:.3f},  p-value <0.0001', color='r', fontsize= 24 )


ax=plt.plot(glue_80years_annual_anoxic_factor_rcp85.index.astype(float),
        trendline_rcp85[-2] * np.arange(80) + trendline_rcp85[-1],
        linestyle='--', color='r', alpha=0.7, linewidth=3  , label='RCP8.5 trendline')

ax=plt.axvline(x=2020, color='grey', linestyle='--')


ax=plt.text(1974, 9.5, 'n=64', color='k', fontsize= 24 )

ax=plt.ylabel('Annual anoxic factor anomaly [d year$^{-1}$]' , fontsize=26)
ax=plt.xlabel('Year' , fontsize=26)
ax=plt.yticks(fontsize= 22)
ax=plt.xticks(rotation=45 , fontsize=22)
ax=plt.legend(bbox_to_anchor=(1.0, -0.2), fontsize=22 , ncol=3)  
fig.savefig("GLUE_Timeseries_annual_anoxic_factor_anomaly.png",  dpi=300, bbox_inches='tight')



#%%Anoxic factor 80 years with trendline 




os.chdir('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/all_4_models/')

import matplotlib.pyplot as plt

fig =plt.figure(figsize=(15, 10))
ax= plt.subplot(111)



ax=plt.fill_between(glue_80years_annual_anoxic_factor_rcp26.index.astype(float), glue_80years_annual_anoxic_factor_rcp26['5%'], glue_80years_annual_anoxic_factor_rcp26['95%'], color='darkgreen', alpha=0.3 ,  label= 'RCP2.6 90% CI')
ax=plt.plot(glue_80years_annual_anoxic_factor_rcp26.index.astype(float), glue_80years_annual_anoxic_factor_rcp26['50%'], 'darkgreen', label='RCP2.6 median', alpha=0.9, linewidth=3  )
ax=plt.plot([2020, 2021] , [14, 14], color='white' , label=' ')

trendline_rcp26=autocorr_MK_org_modif_sens_slope_test(glue_80years_annual_anoxic_factor_rcp26['50%'])



ax=plt.fill_between(glue_80years_annual_anoxic_factor_rcp60.index.astype(float), glue_80years_annual_anoxic_factor_rcp60['5%'], glue_80years_annual_anoxic_factor_rcp60['95%'], color='yellow', alpha=0.3 ,  label= 'RCP6.0 90% CI')
ax=plt.plot(glue_80years_annual_anoxic_factor_rcp60.index.astype(float), glue_80years_annual_anoxic_factor_rcp60['50%'], 'yellow', label='RCP6.0 median', alpha=0.9, linewidth=3  )
trendline_rcp60=autocorr_MK_org_modif_sens_slope_test(glue_80years_annual_anoxic_factor_rcp60['50%'])
ax=plt.text(2020, 1, f'y = {trendline_rcp60[-2]:.3f}x + {trendline_rcp60[-1]:.3f}, p-value <0.0001', color='orange', fontsize= 20 )

ax=plt.plot(glue_80years_annual_anoxic_factor_rcp60.index.astype(float),
        trendline_rcp60[-2] * np.arange(80) + trendline_rcp60[-1],
        linestyle='--', color='orange', alpha=0.9, linewidth=3 , label='RCP6.0 trendline')


ax=plt.fill_between(glue_80years_annual_anoxic_factor_rcp85.index.astype(float), glue_80years_annual_anoxic_factor_rcp85['5%'], glue_80years_annual_anoxic_factor_rcp85['95%'], color='r', alpha=0.2 ,  label= 'RCP8.5 90% CI')
ax=plt.plot(glue_80years_annual_anoxic_factor_rcp85.index.astype(float), glue_80years_annual_anoxic_factor_rcp85['50%'], 'r', label='RCP8.5 median', alpha=0.9, linewidth=3  )
trendline_rcp85=autocorr_MK_org_modif_sens_slope_test(glue_80years_annual_anoxic_factor_rcp85['50%'])
ax=plt.text(2020, 0, f'y = {trendline_rcp85[-2]:.3f}x + {trendline_rcp85[-1]:.3f},  p-value <0.0001', color='r', fontsize= 20 )


ax=plt.plot(glue_80years_annual_anoxic_factor_rcp85.index.astype(float),
        trendline_rcp85[-2] * np.arange(80) + trendline_rcp85[-1],
        linestyle='--', color='r', alpha=0.9, linewidth=3  , label='RCP8.5 trendline')



ax=plt.ylabel('Annual anoxic factor [d year$^{-1}$]' , fontsize=26)
ax=plt.xlabel('Year' , fontsize=26)
ax=plt.yticks(fontsize= 22)
ax=plt.xticks(rotation=45 , fontsize=22)
ax=plt.legend(bbox_to_anchor=(0.95, -0.2), fontsize=22 , ncol= 3)   
fig.savefig("GLUE_Timeseries_80years_annual_anoxic_factor_trendline.png",  dpi=300, bbox_inches='tight')






#%%Anlyses on the RCP2.6 with constant inital condition as 12.298 mg/L

#annual AF
#gfdl

directory = "C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/gfdl_senarios/rcp26_initialcond_attribution"

all_annual_AF_rcp26_test= pd.DataFrame([])
all_weights= np.array([])



# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_gfdl_rcp26"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        time_series = pd.to_datetime(read_data_df['Datetime'])
        Al=hypo_morpho_vriables_gotm_grid[2]
        # Apply the  function
        result_annual =annual_anoxic_factor (C, time_series, Al, A0=23.67*10**6 , threshold=0.5)

        all_annual_AF_rcp26_test = pd.concat([all_annual_AF_rcp26_test , result_annual], axis=1)

        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result annual to a new CSV file
        result_annual_filename = f'annual_AF_gfdl_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_annual_filename))#, index=False)
       

        result_annual.to_csv(os.path.join(directory, result_annual_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_AF'])
        
        
        
        
#hadgem

directory = "C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/hadgem_senarios/rcp26_initialcond_attribution"





# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_hadgem_rcp26"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        time_series = pd.to_datetime(read_data_df['Datetime'])
        Al=hypo_morpho_vriables_gotm_grid[2]
        # Apply the  function
        result_annual =annual_anoxic_factor (C, time_series, Al, A0=23.67*10**6 , threshold=0.5)

        
        all_annual_AF_rcp26_test = pd.concat([all_annual_AF_rcp26_test , result_annual], axis=1)


        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result annual to a new CSV file
        result_annual_filename = f'annual_AF_hadgem_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_annual_filename))#, index=False)
       

        result_annual.to_csv(os.path.join(directory, result_annual_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_AF'])
        
        
       
        
#ipsl

directory = "C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/ipsl_senarios/rcp26_initialcond_attribution"





# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_ipsl_rcp26"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        time_series = pd.to_datetime(read_data_df['Datetime'])
        Al=hypo_morpho_vriables_gotm_grid[2]
        # Apply the  function
        result_annual =annual_anoxic_factor (C, time_series, Al, A0=23.67*10**6 , threshold=0.5)
   
        
        all_annual_AF_rcp26_test = pd.concat([all_annual_AF_rcp26_test , result_annual], axis=1)


        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result annual to a new CSV file
        result_annual_filename = f'annual_AF_ipsl_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_annual_filename))#, index=False)
       

        result_annual.to_csv(os.path.join(directory, result_annual_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_AF'])
        
        
       
        
#miroc

directory = "C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/miroc_senarios/rcp26_initialcond_attribution"




# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_miroc_rcp26"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        time_series = pd.to_datetime(read_data_df['Datetime'])
        Al=hypo_morpho_vriables_gotm_grid[2]
        # Apply the  function
        result_annual =annual_anoxic_factor (C, time_series, Al, A0=23.67*10**6 , threshold=0.5)
 
        
        all_annual_AF_rcp26_test = pd.concat([all_annual_AF_rcp26_test , result_annual], axis=1)


        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result annual to a new CSV file
        result_annual_filename = f'annual_AF_miroc_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_annual_filename))#, index=False)
       

        result_annual.to_csv(os.path.join(directory, result_annual_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_AF'])
        
        

    
    
    
    
    
    
    
        
#%% GLUE of testing rcp26 scenarios for annual
all_annual_AF_rcp26_test

all_annual_AF_rcp26



diff_base_test_annual_AF_rcp26= pd.DataFrame(np.array(all_annual_AF_rcp26)-np.array(all_annual_AF_rcp26_test))



all_weights


# annual DO hypolimnion 
timeseries_year_rcp26= all_annual_AF_rcp26_test.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in diff_base_test_annual_AF_rcp26.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights))

# Build glue df
glue_diff_base_test_annual_AF_rcp26 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_diff_base_test_annual_AF_rcp26=glue_diff_base_test_annual_AF_rcp26.set_index(timeseries_year_rcp26)    
glue_diff_base_test_annual_AF_rcp26=glue_diff_base_test_annual_AF_rcp26.sort_index()
glue_diff_base_test_annual_AF_rcp26_80years=glue_diff_base_test_annual_AF_rcp26[glue_diff_base_test_annual_AF_rcp26.index>2019]



#%% analysing the difference of baseline scenarios and test with fixed inital condition 

#%%annual AF

#decreaseing trend testing the initial condition effect 
autocorr_MK_org_modif_sens_slope_test(glue_diff_base_test_annual_AF_rcp26_80years['50%'])
Out[801]: 
(2.016061202856294,
 'negetively autocorrelated',
 'decreasing',
 0.025952736238498586,
 -0.0020455324895119237,
 0.029465192693039405)




#%%
all_weights


# annual DO hypolimnion 
timeseries_year_rcp26= all_annual_AF_rcp26_test.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_annual_AF_rcp26_test.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights))

# Build glue df
glue_annual_AF_rcp26_test = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_annual_AF_rcp26_test=glue_annual_AF_rcp26_test.set_index(timeseries_year_rcp26)    
glue_annual_AF_rcp26_test=glue_annual_AF_rcp26_test.sort_index()
glue_annual_AF_rcp26_test_80years=glue_annual_AF_rcp26_test[glue_annual_AF_rcp26_test.index>2019]



#%% is there any trendline over 80 years in RCP26 test scenario?
"""
Yes for annual AF 
"""

#%% annual AF
# effect of increasement in length of stratification is obvious 
autocorr_MK_org_modif_sens_slope_test(glue_annual_AF_rcp26_test_80years['50%'])
(0.02715212294414632,
 'positively autocorrelated',
 'increasing',
 0.014003289502218186,
 0.008402475473119442,
 6.754013644481539)

os.chdir('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/all_4_models/')

import matplotlib.pyplot as plt

fig =plt.figure(figsize=(15, 10))
ax= plt.subplot(111)


ax=plt.fill_between(glue_annual_AF_rcp26_test_80years.index.astype(float), glue_annual_AF_rcp26_test_80years['5%'], glue_annual_AF_rcp26_test_80years['95%'], color='green', alpha=0.2 ,  label= '90% CI')
ax=plt.plot(glue_annual_AF_rcp26_test_80years.index.astype(float), glue_annual_AF_rcp26_test_80years['50%'].astype(float), 'green', label='Median', alpha=0.9, linewidth=3  )


trendline_rcp26=autocorr_MK_org_modif_sens_slope_test(glue_annual_AF_rcp26_test_80years['50%'])
ax=plt.text(2020, 2, f'y = {trendline_rcp26[-2]:.3f}x + {trendline_rcp26[-1]:.3f}, p-value = {trendline_rcp26[-3]:.3f}', color='green', fontsize= 20 )

ax=plt.plot(glue_annual_AF_rcp26_test_80years.index.astype(float),
        trendline_rcp26[-2] * np.arange(80) + trendline_rcp26[-1],
        linestyle='--', color='green', alpha=0.9, linewidth=3)




ax=plt.ylabel('Annual anoxic factor of  RCP2.6\n with fixed inital condition [d]' , fontsize=26)
ax=plt.xlabel('Year' , fontsize=26)
ax=plt.yticks(fontsize= 22)
ax=plt.xticks(rotation=45 , fontsize=22)
ax=plt.legend(bbox_to_anchor=(0.7, -0.2), fontsize=22 , ncol= 2)#)   
fig.savefig("test_initalcondition_fixed_annual_AF_80years_rcp26.png",  dpi=300, bbox_inches='tight')


#%%for paper both plot of diff and test of Apr_Oct rcp26 in one plot 

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MaxNLocator

# Create figure and axes for subplots
fig, axs = plt.subplots(1, 2, figsize=(25, 10))

# Plot for the first subplot
ax = axs[1]
ax.fill_between(glue_diff_base_test_annual_AF_rcp26_80years.index,
                glue_diff_base_test_annual_AF_rcp26_80years['5%'],
                glue_diff_base_test_annual_AF_rcp26_80years['95%'],
                color='green', alpha=0.2, label='90% CI')
ax.plot(glue_diff_base_test_annual_AF_rcp26_80years.index,
        glue_diff_base_test_annual_AF_rcp26_80years['50%'],
        'green', label='Median', alpha=0.9, linewidth=3)

# Add trendline
trendline_rcp26_1 = autocorr_MK_org_modif_sens_slope_test(glue_diff_base_test_annual_AF_rcp26_80years['50%'])
#ax.text(0.95, 0.95, '(b)', transform=ax.transAxes, fontsize=22,
#        verticalalignment='top', horizontalalignment='right')
ax.text(2020, 0.5, f'y = {trendline_rcp26_1[-2]:.3f}x + {trendline_rcp26_1[-1]:.3f}, p-value = {trendline_rcp26_1[-3]:.3f}',
        color='green', fontsize=20)
ax.plot(glue_diff_base_test_annual_AF_rcp26_80years.index.astype(float),
        trendline_rcp26_1[-2] * np.arange(80) + trendline_rcp26_1[-1],
        linestyle='--', color='green', alpha=0.9, linewidth=3, label= 'Trendline')

# Set labels for the first subplot
ax.set_ylabel('Annual anoxic factor of RCP2.6 \n difference between fixed initial condition \n and original scenario in deep part  [mg L$^{-1}$]', fontsize=26)
ax.set_xlabel('Year', fontsize=26)
ax.tick_params(axis='y', labelsize=22)
ax.set_xticks(glue_diff_base_test_annual_AF_rcp26_80years.index)
ax.set_xticklabels(glue_diff_base_test_annual_AF_rcp26_80years.index, rotation=45, fontsize=22)
ax.xaxis.set_major_locator(MaxNLocator(prune='both'))

# Plot for the second subplot
ax = axs[0]
ax.fill_between(glue_annual_AF_rcp26_test_80years.index,
                glue_annual_AF_rcp26_test_80years['5%'],
                glue_annual_AF_rcp26_test_80years['95%'],
                color='green', alpha=0.2)#, label='90% CI')
ax.plot(glue_annual_AF_rcp26_test_80years.index,
        glue_annual_AF_rcp26_test_80years['50%'].astype(float),
        'green', alpha=0.9, linewidth=3)# label='Median',

# Add trendline
trendline_rcp26_0 = autocorr_MK_org_modif_sens_slope_test(glue_annual_AF_rcp26_test_80years['50%'])
#ax.text(0.95, 0.95, '(a)', transform=ax.transAxes, fontsize=22,
#        verticalalignment='top', horizontalalignment='right')
ax.text(2020, 10, f'y = {trendline_rcp26_0[-2]:.3f}x + {trendline_rcp26_0[-1]:.3f}, p-value = {trendline_rcp26_0[-3]:.3f}',
        color='green', fontsize=20)
ax.plot(glue_annual_AF_rcp26_test_80years.index,
        trendline_rcp26_0[-2] * np.arange(80) + trendline_rcp26_0[-1],
        linestyle='--', color='green', alpha=0.9, linewidth=3)

# Set labels for the second subplot
ax.set_ylabel('Annual anoxic factor of RCP2.6 with\n fixed initial condition in deep part [mg L$^{-1}$]', fontsize=26)
ax.set_xlabel('Year', fontsize=26)
ax.tick_params(axis='y', labelsize=22)
ax.set_xticks(glue_annual_AF_rcp26_test_80years.index)
ax.set_xticklabels(glue_annual_AF_rcp26_test_80years.index, rotation=45, fontsize=22)
ax.xaxis.set_major_locator(MaxNLocator(prune='both'))

# Add a single legend for both subplots in the center bottom
#fig.legend(loc='lower center', fontsize=22, ncol=3)
fig.legend(loc='lower center', fontsize=22, ncol=3, bbox_to_anchor=(0.5, -0.05))
plt.tight_layout()


plt.savefig("atttest_difference_test_initalcondition_fixed_annual_AF_80years_rcp26.png",  dpi=300, bbox_inches='tight')




#%%%%%%%%======================
#============OLD
#############
#%% Annual anoxic factor_gfdl_his
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/gfdl_senarios/his'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_gfdl_his_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Al = hypo_morpho_vriables_gotm_grid[2]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxic_factor function
        result = annual_anoxic_factor(C, time_series,Al, A0=23.67*10**6 , threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_anoxic_factor_gfdl_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_anoxic_factor'])
        
                

#%%monthly_table_of_anoxic_factor_gfdl_his

# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/gfdl_senarios/his'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_gfdl_his_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Al = hypo_morpho_vriables_gotm_grid[2]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxic_factor function
        result = monthly_table_of_anoxic_factor(C, time_series,Al, A0=23.67*10**6 , threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_table_of_anoxic_factor_gfdl_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                
#%% Annual anoxic factor_gfdl_rcp26
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/gfdl_senarios/rcp26'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_gfdl_rcp26_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Al = hypo_morpho_vriables_gotm_grid[2]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxic_factor function
        result = annual_anoxic_factor(C, time_series,Al, A0=23.67*10**6 , threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_anoxic_factor_gfdl_rcp26_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_anoxic_factor'])
              


#%%monthly_table_of_anoxic_factor_gfdl_rcp26

# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/gfdl_senarios/rcp26'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_gfdl_rcp26_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Al = hypo_morpho_vriables_gotm_grid[2]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxic_factor function
        result = monthly_table_of_anoxic_factor(C, time_series,Al, A0=23.67*10**6 , threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_table_of_anoxic_factor_gfdl_rcp26_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                

#%% Annual anoxic factor_gfdl_rcp60
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/gfdl_senarios/rcp60'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_gfdl_rcp60_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Al = hypo_morpho_vriables_gotm_grid[2]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxic_factor function
        result = annual_anoxic_factor(C, time_series,Al, A0=23.67*10**6 , threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_anoxic_factor_gfdl_rcp60_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_anoxic_factor'])
        
                

#%%monthly_table_of_anoxic_factor_gfdl_rcp60

# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/gfdl_senarios/rcp60'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_gfdl_rcp60_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Al = hypo_morpho_vriables_gotm_grid[2]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxic_factor function
        result = monthly_table_of_anoxic_factor(C, time_series,Al, A0=23.67*10**6 , threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_table_of_anoxic_factor_gfdl_rcp60_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                



#%% Annual anoxic factor_gfdl_rcp85
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/gfdl_senarios/rcp85'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_gfdl_rcp85_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Al = hypo_morpho_vriables_gotm_grid[2]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxic_factor function
        result = annual_anoxic_factor(C, time_series,Al, A0=23.67*10**6 , threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_anoxic_factor_gfdl_rcp85_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_anoxic_factor'])
        



#%%monthly_table_of_anoxic_factor_gfdl_rcp85

# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/gfdl_senarios/rcp85'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_gfdl_rcp85_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Al = hypo_morpho_vriables_gotm_grid[2]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxic_factor function
        result = monthly_table_of_anoxic_factor(C, time_series,Al, A0=23.67*10**6 , threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_table_of_anoxic_factor_gfdl_rcp85_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                
#%%hadgem

#%% Annual anoxic factor_hadgem_his
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
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Al = hypo_morpho_vriables_gotm_grid[2]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxic_factor function
        result = annual_anoxic_factor(C, time_series,Al, A0=23.67*10**6 , threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_anoxic_factor_hadgem_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_anoxic_factor'])
        
  



#%%monthly_table_of_anoxic_factor_hadgem_his

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
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Al = hypo_morpho_vriables_gotm_grid[2]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxic_factor function
        result = monthly_table_of_anoxic_factor(C, time_series,Al, A0=23.67*10**6 , threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_table_of_anoxic_factor_hadgem_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                
#%% Annual anoxic factor_hadgem_rcp26
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
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Al = hypo_morpho_vriables_gotm_grid[2]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxic_factor function
        result = annual_anoxic_factor(C, time_series,Al, A0=23.67*10**6 , threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_anoxic_factor_hadgem_rcp26_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_anoxic_factor'])
        



#%%monthly_table_of_anoxic_factor_hadgem_rcp26

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
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Al = hypo_morpho_vriables_gotm_grid[2]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxic_factor function
        result = monthly_table_of_anoxic_factor(C, time_series,Al, A0=23.67*10**6 , threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_table_of_anoxic_factor_hadgem_rcp26_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                

#%% Annual anoxic factor_hadgem_rcp60
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
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Al = hypo_morpho_vriables_gotm_grid[2]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxic_factor function
        result = annual_anoxic_factor(C, time_series,Al, A0=23.67*10**6 , threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_anoxic_factor_hadgem_rcp60_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_anoxic_factor'])
        


#%%monthly_table_of_anoxic_factor_hadgem_rcp60

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
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Al = hypo_morpho_vriables_gotm_grid[2]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxic_factor function
        result = monthly_table_of_anoxic_factor(C, time_series,Al, A0=23.67*10**6 , threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_table_of_anoxic_factor_hadgem_rcp60_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                



#%% Annual anoxic factor_hadgem_rcp85
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
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Al = hypo_morpho_vriables_gotm_grid[2]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxic_factor function
        result = annual_anoxic_factor(C, time_series,Al, A0=23.67*10**6 , threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_anoxic_factor_hadgem_rcp85_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_anoxic_factor'])
        


#%%monthly_table_of_anoxic_factor_hadgem_rcp85

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
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Al = hypo_morpho_vriables_gotm_grid[2]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxic_factor function
        result = monthly_table_of_anoxic_factor(C, time_series,Al, A0=23.67*10**6 , threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_table_of_anoxic_factor_hadgem_rcp85_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
            
#%%ipsl
#%% Annual anoxic factor_ipsl_his
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
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Al = hypo_morpho_vriables_gotm_grid[2]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxic_factor function
        result = annual_anoxic_factor(C, time_series,Al, A0=23.67*10**6 , threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_anoxic_factor_ipsl_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_anoxic_factor'])
        
                

#%% May_Sep anoxic factor_ipsl_his
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
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Al = hypo_morpho_vriables_gotm_grid[2]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxic_factor function
        result = May_Sep_anoxic_factor(C, time_series,Al, A0=23.67*10**6 , threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'May_Sep_anoxic_factor_ipsl_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['May_Sep_anoxic_factor'])
        
                

#%% Annual anoxic factor_ipsl_rcp26
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
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Al = hypo_morpho_vriables_gotm_grid[2]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxic_factor function
        result = annual_anoxic_factor(C, time_series,Al, A0=23.67*10**6 , threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_anoxic_factor_ipsl_rcp26_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_anoxic_factor'])


#%%monthly_table_of_anoxic_factor_ipsl_rcp26

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
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Al = hypo_morpho_vriables_gotm_grid[2]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxic_factor function
        result = monthly_table_of_anoxic_factor(C, time_series,Al, A0=23.67*10**6 , threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_table_of_anoxic_factor_ipsl_rcp26_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                

#%% Annual anoxic factor_ipsl_rcp60
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
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Al = hypo_morpho_vriables_gotm_grid[2]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxic_factor function
        result = annual_anoxic_factor(C, time_series,Al, A0=23.67*10**6 , threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_anoxic_factor_ipsl_rcp60_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_anoxic_factor'])
        


#%%monthly_table_of_anoxic_factor_ipsl_rcp60

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
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Al = hypo_morpho_vriables_gotm_grid[2]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxic_factor function
        result = monthly_table_of_anoxic_factor(C, time_series,Al, A0=23.67*10**6 , threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_table_of_anoxic_factor_ipsl_rcp60_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                



#%% Annual anoxic factor_ipsl_rcp85
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
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Al = hypo_morpho_vriables_gotm_grid[2]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxic_factor function
        result = annual_anoxic_factor(C, time_series,Al, A0=23.67*10**6 , threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_anoxic_factor_ipsl_rcp85_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_anoxic_factor'])
        
                


#%%monthly_table_of_anoxic_factor_ipsl_rcp85

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
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Al = hypo_morpho_vriables_gotm_grid[2]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxic_factor function
        result = monthly_table_of_anoxic_factor(C, time_series,Al, A0=23.67*10**6 , threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_table_of_anoxic_factor_ipsl_rcp85_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
            
#%%miroc 
#%% Annual anoxic factor_miroc_his
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
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Al = hypo_morpho_vriables_gotm_grid[2]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxic_factor function
        result = annual_anoxic_factor(C, time_series,Al, A0=23.67*10**6 , threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_anoxic_factor_miroc_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_anoxic_factor'])
        
                

#%%monthly_table_of_anoxic_factor_miroc_his

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
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Al = hypo_morpho_vriables_gotm_grid[2]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxic_factor function
        result = monthly_table_of_anoxic_factor(C, time_series,Al, A0=23.67*10**6 , threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_table_of_anoxic_factor_miroc_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                
#%% Annual anoxic factor_miroc_rcp26
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
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Al = hypo_morpho_vriables_gotm_grid[2]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxic_factor function
        result = annual_anoxic_factor(C, time_series,Al, A0=23.67*10**6 , threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_anoxic_factor_miroc_rcp26_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_anoxic_factor'])
        
              


#%%monthly_table_of_anoxic_factor_miroc_rcp26

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
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Al = hypo_morpho_vriables_gotm_grid[2]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxic_factor function
        result = monthly_table_of_anoxic_factor(C, time_series,Al, A0=23.67*10**6 , threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_table_of_anoxic_factor_miroc_rcp26_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                

#%% Annual anoxic factor_miroc_rcp60
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
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Al = hypo_morpho_vriables_gotm_grid[2]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxic_factor function
        result = annual_anoxic_factor(C, time_series,Al, A0=23.67*10**6 , threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_anoxic_factor_miroc_rcp60_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_anoxic_factor'])
        


#%%monthly_table_of_anoxic_factor_miroc_rcp60

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
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Al = hypo_morpho_vriables_gotm_grid[2]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxic_factor function
        result = monthly_table_of_anoxic_factor(C, time_series,Al, A0=23.67*10**6 , threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_table_of_anoxic_factor_miroc_rcp60_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                



#%% Annual anoxic factor_miroc_rcp85
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
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Al = hypo_morpho_vriables_gotm_grid[2]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxic_factor function
        result = annual_anoxic_factor(C, time_series,Al, A0=23.67*10**6 , threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_anoxic_factor_miroc_rcp85_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_anoxic_factor'])
        
 
#%%monthly_table_of_anoxic_factor_miroc_rcp85

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
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Al = hypo_morpho_vriables_gotm_grid[2]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxic_factor function
        result = monthly_table_of_anoxic_factor(C, time_series,Al, A0=23.67*10**6 , threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_table_of_anoxic_factor_miroc_rcp85_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
            
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%GLUE method raeding again these files %%%%%%%%%%%%%%%%%%%

#%%his_annual_anoxic_factor


# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/gfdl_senarios/his'
all_annual_anoxic_factor_his= pd.DataFrame([])
all_weights= np.array([])


# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("annual_anoxic_factor_gfdl_his"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        annual_anoxic_factor = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        annual_anoxic_factor=annual_anoxic_factor.set_index(annual_anoxic_factor.index)
        
        all_annual_anoxic_factor_his = pd.concat([all_annual_anoxic_factor_his , annual_anoxic_factor['annual_anoxic_factor']], axis=1)
        

directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/hadgem_senarios/his'
        

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("annual_anoxic_factor_hadgem_his"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        annual_anoxic_factor = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        annual_anoxic_factor=annual_anoxic_factor.set_index(annual_anoxic_factor.index)
        
        all_annual_anoxic_factor_his = pd.concat([all_annual_anoxic_factor_his , annual_anoxic_factor['annual_anoxic_factor']], axis=1)
        
        
        

directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/ipsl_senarios/his'
        

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("annual_anoxic_factor_ipsl_his"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        annual_anoxic_factor = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        annual_anoxic_factor=annual_anoxic_factor.set_index(annual_anoxic_factor.index)
        
        all_annual_anoxic_factor_his = pd.concat([all_annual_anoxic_factor_his , annual_anoxic_factor['annual_anoxic_factor']], axis=1)
        
        
        

directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/miroc_senarios/his'
        

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("annual_anoxic_factor_miroc_his"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        annual_anoxic_factor = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        annual_anoxic_factor=annual_anoxic_factor.set_index(annual_anoxic_factor.index)
        
        all_annual_anoxic_factor_his = pd.concat([all_annual_anoxic_factor_his , annual_anoxic_factor['annual_anoxic_factor']], axis=1)
        
        
        
        
all_annual_anoxic_factor_his= all_annual_anoxic_factor_his.set_index(annual_anoxic_factor['year'])


# annual anoxic duration  
timeseries_year_his= all_annual_anoxic_factor_his.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_annual_anoxic_factor_his.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights))

# Build glue df
glue_df_annual_anoxic_factor_his = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_df_annual_anoxic_factor_his=glue_df_annual_anoxic_factor_his.set_index(timeseries_year_his)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory
glue_df_annual_anoxic_factor_his.to_csv('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/all_4_models/his/glue_df_anoxic_factor_his.csv')


#%%rcp26_annual_anoxic_factor


# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/gfdl_senarios/rcp26'
all_annual_AF_rcp26= pd.DataFrame([])
all_weights= np.array([])


# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("annual_anoxic_factor_gfdl_rcp26"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        annual_anoxic_factor = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        annual_anoxic_factor=annual_anoxic_factor.set_index(annual_anoxic_factor.index)
        
        all_annual_AF_rcp26 = pd.concat([all_annual_AF_rcp26 , annual_anoxic_factor['annual_anoxic_factor']], axis=1)
        

directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/hadgem_senarios/rcp26'
        

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("annual_anoxic_factor_hadgem_rcp26"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        annual_anoxic_factor = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        annual_anoxic_factor=annual_anoxic_factor.set_index(annual_anoxic_factor.index)
        
        all_annual_AF_rcp26 = pd.concat([all_annual_AF_rcp26 , annual_anoxic_factor['annual_anoxic_factor']], axis=1)
        
        
        

directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/ipsl_senarios/rcp26'
        

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("annual_anoxic_factor_ipsl_rcp26"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        annual_anoxic_factor = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        annual_anoxic_factor=annual_anoxic_factor.set_index(annual_anoxic_factor.index)
        
        all_annual_AF_rcp26 = pd.concat([all_annual_AF_rcp26 , annual_anoxic_factor['annual_anoxic_factor']], axis=1)
        
        
        

directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/miroc_senarios/rcp26'
        

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("annual_anoxic_factor_miroc_rcp26"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        annual_anoxic_factor = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        annual_anoxic_factor=annual_anoxic_factor.set_index(annual_anoxic_factor.index)
        
        all_annual_AF_rcp26 = pd.concat([all_annual_AF_rcp26 , annual_anoxic_factor['annual_anoxic_factor']], axis=1)
        
        
        
        

all_annual_AF_rcp26= all_annual_AF_rcp26.set_index(annual_anoxic_factor['year'])

# annual anoxic duration  
timeseries_year_rcp26= all_annual_AF_rcp26.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_annual_AF_rcp26.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights))

# Build glue df
glue_df_annual_anoxic_factor_rcp26 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_df_annual_anoxic_factor_rcp26=glue_df_annual_anoxic_factor_rcp26.set_index(timeseries_year_rcp26)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory
glue_df_annual_anoxic_factor_rcp26.to_csv('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/all_4_models/rcp26/glue_df_anoxic_factor_rcp26.csv')


#%%rcp60_annual_anoxic_factor


# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/gfdl_senarios/rcp60'
all_annual_anoxic_factor_rcp60= pd.DataFrame([])
all_weights= np.array([])


# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("annual_anoxic_factor_gfdl_rcp60"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        annual_anoxic_factor = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        annual_anoxic_factor=annual_anoxic_factor.set_index(annual_anoxic_factor.index)
        
        all_annual_anoxic_factor_rcp60 = pd.concat([all_annual_anoxic_factor_rcp60 , annual_anoxic_factor['annual_anoxic_factor']], axis=1)
        

directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/hadgem_senarios/rcp60'
        

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("annual_anoxic_factor_hadgem_rcp60"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        annual_anoxic_factor = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        annual_anoxic_factor=annual_anoxic_factor.set_index(annual_anoxic_factor.index)
        
        all_annual_anoxic_factor_rcp60 = pd.concat([all_annual_anoxic_factor_rcp60 , annual_anoxic_factor['annual_anoxic_factor']], axis=1)
        
        
        

directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/ipsl_senarios/rcp60'
        

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("annual_anoxic_factor_ipsl_rcp60"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        annual_anoxic_factor = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        annual_anoxic_factor=annual_anoxic_factor.set_index(annual_anoxic_factor.index)
        
        all_annual_anoxic_factor_rcp60 = pd.concat([all_annual_anoxic_factor_rcp60 , annual_anoxic_factor['annual_anoxic_factor']], axis=1)
        
        
        

directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/miroc_senarios/rcp60'
        

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("annual_anoxic_factor_miroc_rcp60"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        annual_anoxic_factor = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        annual_anoxic_factor=annual_anoxic_factor.set_index(annual_anoxic_factor.index)
        
        all_annual_anoxic_factor_rcp60 = pd.concat([all_annual_anoxic_factor_rcp60 , annual_anoxic_factor['annual_anoxic_factor']], axis=1)
        
        
        
        

all_annual_anoxic_factor_rcp60= all_annual_anoxic_factor_rcp60.set_index(annual_anoxic_factor['year'])

# annual anoxic duration  
timeseries_year_rcp60= all_annual_anoxic_factor_rcp60.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_annual_anoxic_factor_rcp60.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights))

# Build glue df
glue_df_annual_anoxic_factor_rcp60 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_df_annual_anoxic_factor_rcp60=glue_df_annual_anoxic_factor_rcp60.set_index(timeseries_year_rcp60)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory
glue_df_annual_anoxic_factor_rcp60.to_csv('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/all_4_models/rcp60/glue_df_anoxic_factor_rcp60.csv')

#%%rcp85_annual_anoxic_factor


# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/gfdl_senarios/rcp85'
all_annual_anoxic_factor_rcp85= pd.DataFrame([])
all_weights= np.array([])


# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("annual_anoxic_factor_gfdl_rcp85"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        annual_anoxic_factor = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        annual_anoxic_factor=annual_anoxic_factor.set_index(annual_anoxic_factor.index)
        
        all_annual_anoxic_factor_rcp85 = pd.concat([all_annual_anoxic_factor_rcp85 , annual_anoxic_factor['annual_anoxic_factor']], axis=1)
        

directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/hadgem_senarios/rcp85'
        

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("annual_anoxic_factor_hadgem_rcp85"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        annual_anoxic_factor = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        annual_anoxic_factor=annual_anoxic_factor.set_index(annual_anoxic_factor.index)
        
        all_annual_anoxic_factor_rcp85 = pd.concat([all_annual_anoxic_factor_rcp85 , annual_anoxic_factor['annual_anoxic_factor']], axis=1)
        
        
        

directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/ipsl_senarios/rcp85'
        

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("annual_anoxic_factor_ipsl_rcp85"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        annual_anoxic_factor = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        annual_anoxic_factor=annual_anoxic_factor.set_index(annual_anoxic_factor.index)
        
        all_annual_anoxic_factor_rcp85 = pd.concat([all_annual_anoxic_factor_rcp85 , annual_anoxic_factor['annual_anoxic_factor']], axis=1)
        
        
        

directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/miroc_senarios/rcp85'
        

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("annual_anoxic_factor_miroc_rcp85"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        annual_anoxic_factor = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        annual_anoxic_factor=annual_anoxic_factor.set_index(annual_anoxic_factor.index)
        
        all_annual_anoxic_factor_rcp85 = pd.concat([all_annual_anoxic_factor_rcp85 , annual_anoxic_factor['annual_anoxic_factor']], axis=1)
        
        
        
        
all_annual_anoxic_factor_rcp85= all_annual_anoxic_factor_rcp85.set_index(annual_anoxic_factor['year'])


# annual anoxic duration  
timeseries_year_rcp85= all_annual_anoxic_factor_rcp85.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_annual_anoxic_factor_rcp85.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights))

# Build glue df
glue_df_annual_anoxic_factor_rcp85 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_df_annual_anoxic_factor_rcp85=glue_df_annual_anoxic_factor_rcp85.set_index(timeseries_year_rcp85)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory
glue_df_annual_anoxic_factor_rcp85.to_csv('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/all_4_models/rcp85/glue_df_anoxic_factor_rcp85.csv')




#%%sorting the indexs_annual_anoxic_factor 

glue_df_annual_anoxic_factor_his= glue_df_annual_anoxic_factor_his.sort_index()
glue_df_annual_anoxic_factor_rcp26= glue_df_annual_anoxic_factor_rcp26.sort_index()
glue_df_annual_anoxic_factor_rcp60= glue_df_annual_anoxic_factor_rcp60.sort_index()
glue_df_annual_anoxic_factor_rcp85= glue_df_annual_anoxic_factor_rcp85.sort_index()




#%%########annual anoxic factor 

#%%ploting annual anoxic factor 

os.chdir('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/all_4_models/')

import matplotlib.pyplot as plt

fig =plt.figure(figsize=(15, 10))
ax= plt.subplot(111)


ax=plt.fill_between(glue_df_annual_anoxic_factor_his.index.astype(float), glue_df_annual_anoxic_factor_his['5%'], glue_df_annual_anoxic_factor_his['95%'], color='grey', alpha=0.2 ,  label= 'His 90% CI')
ax=plt.plot(glue_df_annual_anoxic_factor_his.index.astype(float), glue_df_annual_anoxic_factor_his['50%'].astype(float), 'k', label='His median', alpha=0.9, linewidth=3  )



ax=plt.fill_between(glue_df_annual_anoxic_factor_rcp26.index.astype(float), glue_df_annual_anoxic_factor_rcp26['5%'], glue_df_annual_anoxic_factor_rcp26['95%'], color='darkgreen', alpha=0.3 ,  label= 'RCP2.6 90% CI')
ax=plt.plot(glue_df_annual_anoxic_factor_rcp26.index.astype(float), glue_df_annual_anoxic_factor_rcp26['50%'], 'darkgreen', label='RCP2.6 median', alpha=0.9, linewidth=3  )


ax=plt.fill_between(glue_df_annual_anoxic_factor_rcp60.index.astype(float), glue_df_annual_anoxic_factor_rcp60['5%'], glue_df_annual_anoxic_factor_rcp60['95%'], color='yellow', alpha=0.2 ,  label= 'RCP6.0 90% CI')
ax=plt.plot(glue_df_annual_anoxic_factor_rcp60.index.astype(float), glue_df_annual_anoxic_factor_rcp60['50%'], 'yellow', label='RCP6.0 median', alpha=0.9, linewidth=3  )

ax=plt.fill_between(glue_df_annual_anoxic_factor_rcp85.index.astype(float), glue_df_annual_anoxic_factor_rcp85['5%'], glue_df_annual_anoxic_factor_rcp85['95%'], color='r', alpha=0.2 ,  label= 'RCP8.5 90% CI')
ax=plt.plot(glue_df_annual_anoxic_factor_rcp85.index.astype(float), glue_df_annual_anoxic_factor_rcp85['50%'], 'r', label='RCP8.5 median', alpha=0.9, linewidth=3  )

ax=plt.ylabel('anoxic factor per each deoxygenation period [d/year]' , fontsize=26)
ax=plt.xlabel('Year' , fontsize=26)
ax=plt.yticks(fontsize= 22)
ax=plt.xticks(rotation=45 , fontsize=22)
ax=plt.legend(bbox_to_anchor=(0.7, -0.2), fontsize=22)#)   
fig.savefig("GLUE_Timeseries_annual_anoxic_factor.png",  dpi=300, bbox_inches='tight')




#%%
np.mean(glue_df_annual_anoxic_factor_his['50%'])#6.077082662821386
np.mean(glue_df_annual_anoxic_factor_rcp26['50%'])#7.992767795524755
np.mean(glue_df_annual_anoxic_factor_rcp60['50%'])#8.585258963812871
np.mean(glue_df_annual_anoxic_factor_rcp85['50%'])#9.156680524881311

#%%anoxic_factor 30 yerars from each scenarios compare 



#anomaly 
# baseline [1976-2005]
glue_base_annual_anoxic_factor_his=glue_df_annual_anoxic_factor_his[1975 < glue_df_annual_anoxic_factor_his.index]['50%']
annual_anoxic_factor_ref=np.mean(glue_base_annual_anoxic_factor_his)
#6.389027950812897


#near future [2030-2059]

glue_near_future_annual_anoxic_factor_rcp26=glue_df_annual_anoxic_factor_rcp26[(2029 < glue_df_annual_anoxic_factor_rcp26.index) & (glue_df_annual_anoxic_factor_rcp26.index < 2060)]['50%']
np.mean(glue_near_future_annual_anoxic_factor_rcp26)
# 8.070525139552648
glue_near_future_annual_anoxic_factor_rcp60=glue_df_annual_anoxic_factor_rcp60[(2029 < glue_df_annual_anoxic_factor_rcp60.index) & (glue_df_annual_anoxic_factor_rcp60.index < 2060)]['50%']
np.mean(glue_near_future_annual_anoxic_factor_rcp60)
# 8.107889314159742
glue_near_future_annual_anoxic_factor_rcp85=glue_df_annual_anoxic_factor_rcp85[(2029 < glue_df_annual_anoxic_factor_rcp85.index) & (glue_df_annual_anoxic_factor_rcp85.index < 2060)]['50%']
np.mean(glue_near_future_annual_anoxic_factor_rcp85)
# 8.63044924136971

 
#Distant future [2070-2099]

glue_distant_future_annual_anoxic_factor_rcp26=glue_df_annual_anoxic_factor_rcp26[(2069 < glue_df_annual_anoxic_factor_rcp26.index) & (glue_df_annual_anoxic_factor_rcp26.index < 2100)]['50%']
np.mean(glue_distant_future_annual_anoxic_factor_rcp26)
#8.153608896799094
glue_distant_future_annual_anoxic_factor_rcp60=glue_df_annual_anoxic_factor_rcp60[(2069 < glue_df_annual_anoxic_factor_rcp60.index) & (glue_df_annual_anoxic_factor_rcp60.index< 2100)]['50%']
np.mean(glue_distant_future_annual_anoxic_factor_rcp60)
#9.787975473676404
glue_distant_future_annual_anoxic_factor_rcp85=glue_df_annual_anoxic_factor_rcp85[(2069 < glue_df_annual_anoxic_factor_rcp85.index) & (glue_df_annual_anoxic_factor_rcp85.index < 2100)]['50%']
np.mean(glue_distant_future_annual_anoxic_factor_rcp85)
#10.985644903398574
   


###====over 30 years in his and each RCPs 

# baseline [1976-2005]
autocorr_MK_org_modif_sens_slope_test(glue_base_annual_anoxic_factor_his)
(0.03791672471698212,
 'positively autocorrelated',
 'increasing',
 0.004067701513906119,
 0.04887120166082099,
 5.685266536515649)


#near future [2030-2059]


autocorr_MK_org_modif_sens_slope_test(glue_near_future_annual_anoxic_factor_rcp26)
(0.018345477426765625,
 'positively autocorrelated',
 'no trend',
 0.09353135296636017,
 0,
 0)

autocorr_MK_org_modif_sens_slope_test(glue_near_future_annual_anoxic_factor_rcp60)
(0.011313156566510486,
 'positively autocorrelated',
 'increasing',
 0.0007961960227531595,
 0.0470080311379157,
 7.4730648265627355)

autocorr_MK_org_modif_sens_slope_test(glue_near_future_annual_anoxic_factor_rcp85)

(0.01548644557384171,
 'positively autocorrelated',
 'increasing',
 0.0048191095611576085,
 0.05773266804253006,
 7.722484654253696)



#Distant future [2070-2099]


autocorr_MK_org_modif_sens_slope_test(glue_distant_future_annual_anoxic_factor_rcp26)
(0.015039983618369416,
 'positively autocorrelated',
 'no trend',
 0.1989481007752456,
 0,
 0)

autocorr_MK_org_modif_sens_slope_test(glue_distant_future_annual_anoxic_factor_rcp60)
(0.012394095955031883,
 'positively autocorrelated',
 'no trend',
 0.41182433473249125,
 0,
 0)
autocorr_MK_org_modif_sens_slope_test(glue_distant_future_annual_anoxic_factor_rcp85)
(0.014499198182054042,
 'positively autocorrelated',
 'increasing',
 0.026946782463489027,
 0.05377923636923881,
 10.323144222989352)






#%% 80 years from 2020 for annual_anoxic_factor


glue_80years_annual_anoxic_factor_rcp26=glue_df_annual_anoxic_factor_rcp26[2019 < glue_df_annual_anoxic_factor_rcp26.index]

glue_80years_annual_anoxic_factor_rcp60=glue_df_annual_anoxic_factor_rcp60[2019 < glue_df_annual_anoxic_factor_rcp60.index]

glue_80years_annual_anoxic_factor_rcp85=glue_df_annual_anoxic_factor_rcp85[2019 < glue_df_annual_anoxic_factor_rcp85.index]


#============= mean of first 10 yaers over 80 years 

#rcp2.6
np.mean(glue_80years_annual_anoxic_factor_rcp26[glue_80years_annual_anoxic_factor_rcp26.index<2030]['50%'])
7.781968220542252

#rcp6.0
np.mean(glue_80years_annual_anoxic_factor_rcp60[glue_80years_annual_anoxic_factor_rcp60.index<2030]['50%'])
7.835574478598173

#rcp8.5
np.mean(glue_80years_annual_anoxic_factor_rcp85[glue_80years_annual_anoxic_factor_rcp85.index<2030]['50%'])
7.7236229767454985

#============== mean of last 10 yaers over 80 years 

#rcp2.6
np.mean(glue_80years_annual_anoxic_factor_rcp26[glue_80years_annual_anoxic_factor_rcp26.index>2079]['50%'])
8.243966830565041

#rcp6.0
np.mean(glue_80years_annual_anoxic_factor_rcp60[glue_80years_annual_anoxic_factor_rcp60.index>2079]['50%'])
9.864621453257977

#rcp8.5
np.mean(glue_80years_annual_anoxic_factor_rcp85[glue_80years_annual_anoxic_factor_rcp85.index>2079]['50%'])
11.160292464667199

#=========== trendline # Over the 80 years


autocorr_MK_org_modif_sens_slope_test(glue_80years_annual_anoxic_factor_rcp26['50%'])
(0.02031492443906448,
 'positively autocorrelated',
 'no trend',
 0.11371844918011509,
 0,
 0)


autocorr_MK_org_modif_sens_slope_test(glue_80years_annual_anoxic_factor_rcp60['50%'])
(0.012504340139489645,
 'positively autocorrelated',
 'increasing',
 1.4566126083082054e-13,
 0.036058805989694846,
 7.282950340706922)



autocorr_MK_org_modif_sens_slope_test(glue_80years_annual_anoxic_factor_rcp85['50%'])
(0.015711631920486826,
 'positively autocorrelated',
 'increasing',
 0.0,
 0.05742827331247126,
 7.128166722990812)


#%% trendline of 80 years in annual


os.chdir('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/all_4_models/')

import matplotlib.pyplot as plt

fig =plt.figure(figsize=(15, 10))
ax= plt.subplot(111)



ax=plt.fill_between(glue_80years_annual_anoxic_factor_rcp26.index.astype(float), glue_80years_annual_anoxic_factor_rcp26['5%'], glue_80years_annual_anoxic_factor_rcp26['95%'], color='darkgreen', alpha=0.3 ,  label= 'RCP2.6 90% CI')
ax=plt.plot(glue_80years_annual_anoxic_factor_rcp26.index.astype(float), glue_80years_annual_anoxic_factor_rcp26['50%'], 'darkgreen', label='RCP2.6 median', alpha=0.9, linewidth=3  )
#trendline_rcp26=autocorr_MK_org_modif_sens_slope_test(glue_80years_annual_anoxic_factor_rcp26['50%'])

ax=plt.plot([2020, 2022],[7,7],
        linestyle='--', color='white',  label=' ')




ax=plt.fill_between(glue_80years_annual_anoxic_factor_rcp60.index.astype(float), glue_80years_annual_anoxic_factor_rcp60['5%'], glue_80years_annual_anoxic_factor_rcp60['95%'], color='yellow', alpha=0.2 ,  label= 'RCP6.0 90% CI')
ax=plt.plot(glue_80years_annual_anoxic_factor_rcp60.index.astype(float), glue_80years_annual_anoxic_factor_rcp60['50%'], 'yellow', label='RCP6.0 median', alpha=0.9, linewidth=3  )
trendline_rcp60=autocorr_MK_org_modif_sens_slope_test(glue_80years_annual_anoxic_factor_rcp60['50%'])
ax=plt.text(2020, 20, f'y = {trendline_rcp60[-2]:.3f}x + {trendline_rcp60[-1]:.3f}, p-value<0.0001', color='gold', fontsize= 20 )

ax=plt.plot(glue_80years_annual_anoxic_factor_rcp60.index.astype(float),
        trendline_rcp60[-2] * np.arange(80) + trendline_rcp60[-1],
        linestyle='--', color='yellow', alpha=0.9, linewidth=3, label='RCP8.5 trendline')


ax=plt.fill_between(glue_80years_annual_anoxic_factor_rcp85.index.astype(float), glue_80years_annual_anoxic_factor_rcp85['5%'], glue_80years_annual_anoxic_factor_rcp85['95%'], color='r', alpha=0.2 ,  label= 'RCP8.5 90% CI')
ax=plt.plot(glue_80years_annual_anoxic_factor_rcp85.index.astype(float), glue_80years_annual_anoxic_factor_rcp85['50%'], 'r', label='RCP8.5 median', alpha=0.9, linewidth=3  )
trendline_rcp85=autocorr_MK_org_modif_sens_slope_test(glue_80years_annual_anoxic_factor_rcp85['50%'])
ax=plt.text(2020, 10, f'y = {trendline_rcp85[-2]:.3f}x + {trendline_rcp85[-1]:.3f},  p-value<0.0001', color='r', fontsize= 20 )


ax=plt.plot(glue_80years_annual_anoxic_factor_rcp85.index.astype(float),
        trendline_rcp85[-2] * np.arange(80) + trendline_rcp85[-1],
        linestyle='--', color='r', alpha=0.9, linewidth=3, label='RCP8.5 trendline')



ax=plt.ylabel('Anoxia duration [d year$^{-1}$]' , fontsize=26)
ax=plt.xlabel('Year' , fontsize=26)
ax=plt.yticks(fontsize= 22)
ax=plt.xticks(rotation=45 , fontsize=22)
ax=plt.legend(bbox_to_anchor=(0.97, -0.2), fontsize=22 , ncol= 3)   
fig.savefig("GLUE_Timeseries_80years_annual_anoxic_factor_trendline.png",  dpi=300, bbox_inches='tight')

















#%%If there is a trend in entire 

# in whole his
autocorr_MK_org_modif_sens_slope_test(glue_df_annual_anoxic_factor_his['50%'])
(0.054103668580385816,
 'positively autocorrelated',
 'no trend',
 0.07068845447209426,
 0,
 0)

#in intire rcp2.6
autocorr_MK_org_modif_sens_slope_test(glue_df_annual_anoxic_factor_rcp26['50%'])
(0.02002132148516097,
 'positively autocorrelated',
 'increasing',
 0.0012506240636172006,
 0.009277291512717471,
 7.539997545595559)

#in entire rcp6.0
autocorr_MK_org_modif_sens_slope_test(glue_df_annual_anoxic_factor_rcp60['50%'])
(0.01438079345143515,
 'positively autocorrelated',
 'increasing',
 2.6645352591003757e-13,
 0.03278504999647535,
 6.993374854517668)

#in entire rcp8.5
autocorr_MK_org_modif_sens_slope_test(glue_df_annual_anoxic_factor_rcp85['50%'])
(0.01670964657273115,
 'positively autocorrelated',
 'increasing',
 0.0,
 0.05615663487366421,
 6.386209763383056)

#slope in entire RCP8.5> RCP6.0>RCP2.6 # his no trend 



 
#%%anoxic_factor_anomaly 
os.chdir('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/all_4_models/')

import matplotlib.pyplot as plt

fig =plt.figure(figsize=(15, 10))
ax= plt.subplot(111)


ax=plt.fill_between(glue_df_annual_anoxic_factor_his[(1975 < glue_df_annual_anoxic_factor_his.index)].index.astype(float),
                      glue_df_annual_anoxic_factor_his[(1975 < glue_df_annual_anoxic_factor_his.index)]['5%'] - annual_anoxic_factor_ref,
                      glue_df_annual_anoxic_factor_his[(1975 < glue_df_annual_anoxic_factor_his.index) ]['95%'] - annual_anoxic_factor_ref,
                      color='grey', alpha=0.2, label='His 90% CI')


ax=plt.plot(glue_df_annual_anoxic_factor_his[(1975 < glue_df_annual_anoxic_factor_his.index) ].index.astype(float),
            glue_df_annual_anoxic_factor_his[(1975 < glue_df_annual_anoxic_factor_his.index)]['50%'] - annual_anoxic_factor_ref,
            'k', label='His median', alpha=0.9, linewidth=3   )

ax=plt.fill_between(glue_df_annual_anoxic_factor_rcp26.index.astype(float), glue_df_annual_anoxic_factor_rcp26['5%']-annual_anoxic_factor_ref, glue_df_annual_anoxic_factor_rcp26['95%']-annual_anoxic_factor_ref, color='darkgreen', alpha=0.3 ,  label= 'RCP6.0 90% CI')
ax=plt.plot(glue_df_annual_anoxic_factor_rcp26.index.astype(float), glue_df_annual_anoxic_factor_rcp26['50%']-annual_anoxic_factor_ref, 'darkgreen', label='RCP6.0 median', alpha=0.9, linewidth=3  )
                      
                     
ax=plt.fill_between(glue_df_annual_anoxic_factor_rcp60.index.astype(float), glue_df_annual_anoxic_factor_rcp60['5%']-annual_anoxic_factor_ref, glue_df_annual_anoxic_factor_rcp60['95%']-annual_anoxic_factor_ref, color='yellow', alpha=0.2 ,  label= 'RCP6.0 90% CI')
ax=plt.plot(glue_df_annual_anoxic_factor_rcp60.index.astype(float), glue_df_annual_anoxic_factor_rcp60['50%']-annual_anoxic_factor_ref, 'yellow', label='RCP6.0 median', alpha=0.9, linewidth=3  )

ax=plt.fill_between(glue_df_annual_anoxic_factor_rcp85.index.astype(float), glue_df_annual_anoxic_factor_rcp85['5%']-annual_anoxic_factor_ref, glue_df_annual_anoxic_factor_rcp85['95%']-annual_anoxic_factor_ref, color='r', alpha=0.2 ,  label= 'RCP8.5 90% CI')
ax=plt.plot(glue_df_annual_anoxic_factor_rcp85.index.astype(float), glue_df_annual_anoxic_factor_rcp85['50%']-annual_anoxic_factor_ref, 'r', label='RCP8.5 median', alpha=0.9, linewidth=3  )

ax=plt.ylabel('anomaly of annual anoxic factor [d year$^{-1}$]' , fontsize=26)
ax=plt.xlabel('Year' , fontsize=26)
ax=plt.yticks(fontsize= 22)
ax=plt.xticks(rotation=45 , fontsize=22)
ax=plt.legend(bbox_to_anchor=(1.1, -0.2), fontsize=22, ncol=4)  
fig.savefig("GLUE_Timeseries_annual_anoxic_factor_anomaly.png",  dpi=300, bbox_inches='tight')


#%%
####################################old one
############################################
############################################

#%% Annual anoxic factor_gfdl_his
# Specify the directory where the CSV files are located


#########original test with variable theta:
#########directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/gfdl_senarios/his'


######## fixed theta both in calib and simulation 
#######directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/gfdl_senarios/his_fixedtheta'




####### test with fixed theta in calibration but variable for GOTM simulation 
directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/gfdl_senarios/his_calibinfixedtheta_simuvartheta'




# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_gfdl_his_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Al = hypo_morpho_vriables_gotm_grid[2]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxic_factor function
        result = annual_anoxic_factor(C, time_series,Al, A0=23.67*10**6 , threshold=0.5)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_anoxic_factor_gfdl_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_anoxic_factor'])
        
                


#%%monthly_table_of_anoxic_factor_gfdl_his

# Specify the directory where the CSV files are located
#########original test with variable theta:
#########directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/gfdl_senarios/his'


######## fixed theta both in calib and simulation 
#######directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/gfdl_senarios/his_fixedtheta'




####### test with fixed theta in calibration but variable for GOTM simulation 
directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/gfdl_senarios/his_calibinfixedtheta_simuvartheta'


# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_gfdl_his_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Al = hypo_morpho_vriables_gotm_grid[2]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxic_factor function
        result = monthly_table_of_anpoxic_factor(C, time_series,Al, A0=23.67*10**6 , threshold=0.5)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_table_of_anpoxic_factor_gfdl_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                
#%% Annual anoxic factor_gfdl_rcp26
# Specify the directory where the CSV files are located
#########original test with variable theta:
#########directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/gfdl_senarios/rcp26'


######## fixed theta both in calib and simulation 
######## directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/gfdl_senarios/rcp26_fixedtheta'


###### test with fixed theta in calibration a temp ave hypo in gfdl rcp26 for years 2020 and 2021
#######directory='C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/gfdl_senarios/rcp26_fixedthetaincalib_simurcp26temp20202021'



####### test with fixed theta in calibration but variable for GOTM simulation 
directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/gfdl_senarios/rcp26_calibinfixedtheta_simuvartheta'


# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_gfdl_rcp26_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Al = hypo_morpho_vriables_gotm_grid[2]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxic_factor function
        result = annual_anoxic_factor(C, time_series,Al, A0=23.67*10**6 , threshold=0.5)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_anoxic_factor_gfdl_rcp26_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_anoxic_factor'])
        
                


#%%monthly_table_of_anpoxic_factor_gfdl_rcp26

# Specify the directory where the CSV files are located
#########original test with variable theta:
#########directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/gfdl_senarios/rcp26'


######## fixed theta both in calib and simulation 
######## directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/gfdl_senarios/rcp26_fixedtheta'


###### test with fixed theta in calibration a temp ave hypo in gfdl rcp26 for years 2020 and 2021
#######directory='C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/gfdl_senarios/rcp26_fixedthetaincalib_simurcp26temp20202021'



####### test with fixed theta in calibration but variable for GOTM simulation 
directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/gfdl_senarios/rcp26_calibinfixedtheta_simuvartheta'



# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_gfdl_rcp26_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Al = hypo_morpho_vriables_gotm_grid[2]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxic_factor function
        result = monthly_table_of_anpoxic_factor(C, time_series,Al, A0=23.67*10**6 , threshold=0.5)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_table_of_anpoxic_factor_gfdl_rcp26_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                

#%% Annual anoxic factor_gfdl_rcp60
# Specify the directory where the CSV files are located
#########original test with variable theta:
#########directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/gfdl_senarios/rcp60'


######## fixed theta both in calib and simulation 
######## directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/gfdl_senarios/rcp60_fixedtheta'


###### test with fixed theta in calibration a temp ave hypo in gfdl rcp60 for years 2020 and 2021
#######directory='C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/gfdl_senarios/rcp60_fixedthetaincalib_simurcp60temp20202021'



####### test with fixed theta in calibration but variable for GOTM simulation 
directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/gfdl_senarios/rcp60_calibinfixedtheta_simuvartheta'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_gfdl_rcp60_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Al = hypo_morpho_vriables_gotm_grid[2]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxic_factor function
        result = annual_anoxic_factor(C, time_series,Al, A0=23.67*10**6 , threshold=0.5)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_anoxic_factor_gfdl_rcp60_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_anoxic_factor'])
        
                


#%%monthly_table_of_anpoxic_factor_gfdl_rcp60

# Specify the directory where the CSV files are located
#########original test with variable theta:
#########directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/gfdl_senarios/rcp60'


######## fixed theta both in calib and simulation 
######## directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/gfdl_senarios/rcp60_fixedtheta'


###### test with fixed theta in calibration a temp ave hypo in gfdl rcp60 for years 2020 and 2021
#######directory='C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/gfdl_senarios/rcp60_fixedthetaincalib_simurcp60temp20202021'



####### test with fixed theta in calibration but variable for GOTM simulation 
directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/gfdl_senarios/rcp60_calibinfixedtheta_simuvartheta'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_gfdl_rcp60_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Al = hypo_morpho_vriables_gotm_grid[2]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxic_factor function
        result = monthly_table_of_anpoxic_factor(C, time_series,Al, A0=23.67*10**6 , threshold=0.5)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_table_of_anpoxic_factor_gfdl_rcp60_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                



#%% Annual anoxic factor_gfdl_rcp85
# Specify the directory where the CSV files are located
#########original test with variable theta:
#########directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/gfdl_senarios/rcp85'


######## fixed theta both in calib and simulation 
######## directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/gfdl_senarios/rcp85_fixedtheta'


###### test with fixed theta in calibration a temp ave hypo in gfdl rcp85 for years 2020 and 2021
#######directory='C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/gfdl_senarios/rcp85_fixedthetaincalib_simurcp85temp20202021'



####### test with fixed theta in calibration but variable for GOTM simulation 
directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/gfdl_senarios/rcp85_calibinfixedtheta_simuvartheta'



# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_gfdl_rcp85_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Al = hypo_morpho_vriables_gotm_grid[2]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxic_factor function
        result = annual_anoxic_factor(C, time_series,Al, A0=23.67*10**6 , threshold=0.5)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_anoxic_factor_gfdl_rcp85_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_anoxic_factor'])
        
                


#%%monthly_table_of_anpoxic_factor_gfdl_rcp85

# Specify the directory where the CSV files are located
#########original test with variable theta:
#########directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/gfdl_senarios/rcp85'


######## fixed theta both in calib and simulation 
######## directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/gfdl_senarios/rcp85_fixedtheta'


###### test with fixed theta in calibration a temp ave hypo in gfdl rcp85 for years 2020 and 2021
#######directory='C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/gfdl_senarios/rcp85_fixedthetaincalib_simurcp85temp20202021'



####### test with fixed theta in calibration but variable for GOTM simulation 
directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/gfdl_senarios/rcp85_calibinfixedtheta_simuvartheta'



# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_gfdl_rcp85_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Al = hypo_morpho_vriables_gotm_grid[2]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxic_factor function
        result = monthly_table_of_anpoxic_factor(C, time_series,Al, A0=23.67*10**6 , threshold=0.5)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_table_of_anpoxic_factor_gfdl_rcp85_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                


#%% Annual anoxic factor_hadgem_his
# Specify the directory where the CSV files are located

#########original test with variable theta:
#########directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/hadgem_senarios/his'


######## fixed theta both in calib and simulation 
#######directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/hadgem_senarios/his_fixedtheta'




####### test with fixed theta in calibration but variable for GOTM simulation 
directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/hadgem_senarios/his_calibinfixedtheta_simuvartheta'


# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_hadgem_his_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Al = hypo_morpho_vriables_gotm_grid[2]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxic_factor function
        result = annual_anoxic_factor(C, time_series,Al, A0=23.67*10**6 , threshold=0.5)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_anoxic_factor_hadgem_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_anoxic_factor'])
        
                


#%%monthly_table_of_anpoxic_factor_hadgem_his

# Specify the directory where the CSV files are located
#########original test with variable theta:
#########directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/hadgem_senarios/his'


######## fixed theta both in calib and simulation 
#######directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/hadgem_senarios/his_fixedtheta'




####### test with fixed theta in calibration but variable for GOTM simulation 
directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/hadgem_senarios/his_calibinfixedtheta_simuvartheta'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_hadgem_his_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Al = hypo_morpho_vriables_gotm_grid[2]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxic_factor function
        result = monthly_table_of_anpoxic_factor(C, time_series,Al, A0=23.67*10**6 , threshold=0.5)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_table_of_anpoxic_factor_hadgem_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                
#%% Annual anoxic factor_hadgem_rcp26
# Specify the directory where the CSV files are located

#########original test with variable theta:
#########directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/hadgem_senarios/rcp26'


######## fixed theta both in calib and simulation 
######## directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/hadgem_senarios/rcp26_fixedtheta'


###### test with fixed theta in calibration a temp ave hypo in hadgem rcp26 for years 2020 and 2021
#######directory='C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/hadgem_senarios/rcp26_fixedthetaincalib_simurcp26temp20202021'



####### test with fixed theta in calibration but variable for GOTM simulation 
directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/hadgem_senarios/rcp26_calibinfixedtheta_simuvartheta'




# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_hadgem_rcp26_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Al = hypo_morpho_vriables_gotm_grid[2]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxic_factor function
        result = annual_anoxic_factor(C, time_series,Al, A0=23.67*10**6 , threshold=0.5)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_anoxic_factor_hadgem_rcp26_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_anoxic_factor'])
        
                


#%%monthly_table_of_anpoxic_factor_hadgem_rcp26

# Specify the directory where the CSV files are located
#########original test with variable theta:
#########directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/hadgem_senarios/rcp26'


######## fixed theta both in calib and simulation 
######## directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/hadgem_senarios/rcp26_fixedtheta'


###### test with fixed theta in calibration a temp ave hypo in hadgem rcp26 for years 2020 and 2021
#######directory='C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/hadgem_senarios/rcp26_fixedthetaincalib_simurcp26temp20202021'



####### test with fixed theta in calibration but variable for GOTM simulation 
directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/hadgem_senarios/rcp26_calibinfixedtheta_simuvartheta'


# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_hadgem_rcp26_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Al = hypo_morpho_vriables_gotm_grid[2]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxic_factor function
        result = monthly_table_of_anpoxic_factor(C, time_series,Al, A0=23.67*10**6 , threshold=0.5)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_table_of_anpoxic_factor_hadgem_rcp26_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                

#%% Annual anoxic factor_hadgem_rcp60
# Specify the directory where the CSV files are located
#########original test with variable theta:
#########directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/hadgem_senarios/rcp60'


######## fixed theta both in calib and simulation 
######## directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/hadgem_senarios/rcp60_fixedtheta'


###### test with fixed theta in calibration a temp ave hypo in hadgem rcp60 for years 2020 and 2021
#######directory='C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/hadgem_senarios/rcp60_fixedthetaincalib_simurcp60temp20202021'



####### test with fixed theta in calibration but variable for GOTM simulation 
directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/hadgem_senarios/rcp60_calibinfixedtheta_simuvartheta'




# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_hadgem_rcp60_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Al = hypo_morpho_vriables_gotm_grid[2]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxic_factor function
        result = annual_anoxic_factor(C, time_series,Al, A0=23.67*10**6 , threshold=0.5)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_anoxic_factor_hadgem_rcp60_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_anoxic_factor'])
        
                


#%%monthly_table_of_anpoxic_factor_hadgem_rcp60

# Specify the directory where the CSV files are located

#########original test with variable theta:
#########directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/hadgem_senarios/rcp60'


######## fixed theta both in calib and simulation 
######## directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/hadgem_senarios/rcp60_fixedtheta'


###### test with fixed theta in calibration a temp ave hypo in hadgem rcp60 for years 2020 and 2021
#######directory='C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/hadgem_senarios/rcp60_fixedthetaincalib_simurcp60temp20202021'



####### test with fixed theta in calibration but variable for GOTM simulation 
directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/hadgem_senarios/rcp60_calibinfixedtheta_simuvartheta'



# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_hadgem_rcp60_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Al = hypo_morpho_vriables_gotm_grid[2]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxic_factor function
        result = monthly_table_of_anpoxic_factor(C, time_series,Al, A0=23.67*10**6 , threshold=0.5)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_table_of_anpoxic_factor_hadgem_rcp60_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                



#%% Annual anoxic factor_hadgem_rcp85
# Specify the directory where the CSV files are located


#########original test with variable theta:
#########directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/hadgem_senarios/rcp85'


######## fixed theta both in calib and simulation 
######## directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/hadgem_senarios/rcp85_fixedtheta'


###### test with fixed theta in calibration a temp ave hypo in hadgem rcp85 for years 2020 and 2021
#######directory='C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/hadgem_senarios/rcp85_fixedthetaincalib_simurcp85temp20202021'



####### test with fixed theta in calibration but variable for GOTM simulation 
directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/hadgem_senarios/rcp85_calibinfixedtheta_simuvartheta'




# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_hadgem_rcp85_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Al = hypo_morpho_vriables_gotm_grid[2]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxic_factor function
        result = annual_anoxic_factor(C, time_series,Al, A0=23.67*10**6 , threshold=0.5)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_anoxic_factor_hadgem_rcp85_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_anoxic_factor'])
        
                


#%%monthly_table_of_anpoxic_factor_hadgem_rcp85

# Specify the directory where the CSV files are located

#########original test with variable theta:
#########directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/hadgem_senarios/rcp85'


######## fixed theta both in calib and simulation 
######## directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/hadgem_senarios/rcp85_fixedtheta'


###### test with fixed theta in calibration a temp ave hypo in hadgem rcp85 for years 2020 and 2021
#######directory='C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/hadgem_senarios/rcp85_fixedthetaincalib_simurcp85temp20202021'



####### test with fixed theta in calibration but variable for GOTM simulation 
directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/hadgem_senarios/rcp85_calibinfixedtheta_simuvartheta'




# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_hadgem_rcp85_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Al = hypo_morpho_vriables_gotm_grid[2]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxic_factor function
        result = monthly_table_of_anpoxic_factor(C, time_series,Al, A0=23.67*10**6 , threshold=0.5)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_table_of_anpoxic_factor_hadgem_rcp85_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                


#%% Annual anoxic factor_ipsl_his
# Specify the directory where the CSV files are located
#########original test with variable theta:
#########directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/ipsl_senarios/his'


######## fixed theta both in calib and simulation 
#######directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/ipsl_senarios/his_fixedtheta'




####### test with fixed theta in calibration but variable for GOTM simulation 
directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/ipsl_senarios/his_calibinfixedtheta_simuvartheta'


# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_ipsl_his_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Al = hypo_morpho_vriables_gotm_grid[2]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxic_factor function
        result = annual_anoxic_factor(C, time_series,Al, A0=23.67*10**6 , threshold=0.5)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_anoxic_factor_ipsl_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_anoxic_factor'])
        
                


#%%monthly_table_of_anpoxic_factor_ipsl_his

# Specify the directory where the CSV files are located
#########original test with variable theta:
#########directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/ipsl_senarios/his'


######## fixed theta both in calib and simulation 
#######directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/ipsl_senarios/his_fixedtheta'




####### test with fixed theta in calibration but variable for GOTM simulation 
directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/ipsl_senarios/his_calibinfixedtheta_simuvartheta'


# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_ipsl_his_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Al = hypo_morpho_vriables_gotm_grid[2]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxic_factor function
        result = monthly_table_of_anpoxic_factor(C, time_series,Al, A0=23.67*10**6 , threshold=0.5)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_table_of_anpoxic_factor_ipsl_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                
#%% Annual anoxic factor_ipsl_rcp26
# Specify the directory where the CSV files are located

#########original test with variable theta:
#########directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/ipsl_senarios/rcp26'


######## fixed theta both in calib and simulation 
######## directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/ipsl_senarios/rcp26_fixedtheta'


###### test with fixed theta in calibration a temp ave hypo in ipcl rcp26 for years 2020 and 2021
#######directory='C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/ipsl_senarios/rcp26_fixedthetaincalib_simurcp26temp20202021'



####### test with fixed theta in calibration but variable for GOTM simulation 
directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/ipsl_senarios/rcp26_calibinfixedtheta_simuvartheta'



# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_ipsl_rcp26_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Al = hypo_morpho_vriables_gotm_grid[2]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxic_factor function
        result = annual_anoxic_factor(C, time_series,Al, A0=23.67*10**6 , threshold=0.5)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_anoxic_factor_ipsl_rcp26_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_anoxic_factor'])
        
                


#%%monthly_table_of_anpoxic_factor_ipsl_rcp26

# Specify the directory where the CSV files are located

#########original test with variable theta:
#########directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/ipsl_senarios/rcp26'


######## fixed theta both in calib and simulation 
######## directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/ipsl_senarios/rcp26_fixedtheta'


###### test with fixed theta in calibration a temp ave hypo in ipcl rcp26 for years 2020 and 2021
#######directory='C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/ipsl_senarios/rcp26_fixedthetaincalib_simurcp26temp20202021'



####### test with fixed theta in calibration but variable for GOTM simulation 
directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/ipsl_senarios/rcp26_calibinfixedtheta_simuvartheta'


# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_ipsl_rcp26_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Al = hypo_morpho_vriables_gotm_grid[2]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxic_factor function
        result = monthly_table_of_anpoxic_factor(C, time_series,Al, A0=23.67*10**6 , threshold=0.5)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_table_of_anpoxic_factor_ipsl_rcp26_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                

#%% Annual anoxic factor_ipsl_rcp60
# Specify the directory where the CSV files are located

#########original test with variable theta:
#########directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/ipsl_senarios/rcp60'


######## fixed theta both in calib and simulation 
######## directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/ipsl_senarios/rcp60_fixedtheta'


###### test with fixed theta in calibration a temp ave hypo in ipcl rcp60 for years 2020 and 2021
#######directory='C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/ipsl_senarios/rcp60_fixedthetaincalib_simurcp60temp20202021'



####### test with fixed theta in calibration but variable for GOTM simulation 
directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/ipsl_senarios/rcp60_calibinfixedtheta_simuvartheta'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_ipsl_rcp60_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Al = hypo_morpho_vriables_gotm_grid[2]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxic_factor function
        result = annual_anoxic_factor(C, time_series,Al, A0=23.67*10**6 , threshold=0.5)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_anoxic_factor_ipsl_rcp60_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_anoxic_factor'])
        
                


#%%monthly_table_of_anpoxic_factor_ipsl_rcp60

# Specify the directory where the CSV files are located
#########original test with variable theta:
#########directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/ipsl_senarios/rcp60'


######## fixed theta both in calib and simulation 
######## directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/ipsl_senarios/rcp60_fixedtheta'


###### test with fixed theta in calibration a temp ave hypo in ipcl rcp60 for years 2020 and 2021
#######directory='C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/ipsl_senarios/rcp60_fixedthetaincalib_simurcp60temp20202021'



####### test with fixed theta in calibration but variable for GOTM simulation 
directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/ipsl_senarios/rcp60_calibinfixedtheta_simuvartheta'


# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_ipsl_rcp60_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Al = hypo_morpho_vriables_gotm_grid[2]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxic_factor function
        result = monthly_table_of_anpoxic_factor(C, time_series,Al, A0=23.67*10**6 , threshold=0.5)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_table_of_anpoxic_factor_ipsl_rcp60_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                



#%% Annual anoxic factor_ipsl_rcp85
# Specify the directory where the CSV files are located

#########original test with variable theta:
#########directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/ipsl_senarios/rcp85'


######## fixed theta both in calib and simulation 
######## directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/ipsl_senarios/rcp85_fixedtheta'


###### test with fixed theta in calibration a temp ave hypo in ipcl rcp85 for years 2020 and 2021
#######directory='C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/ipsl_senarios/rcp85_fixedthetaincalib_simurcp85temp20202021'



####### test with fixed theta in calibration but variable for GOTM simulation 
directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/ipsl_senarios/rcp85_calibinfixedtheta_simuvartheta'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_ipsl_rcp85_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Al = hypo_morpho_vriables_gotm_grid[2]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxic_factor function
        result = annual_anoxic_factor(C, time_series,Al, A0=23.67*10**6 , threshold=0.5)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_anoxic_factor_ipsl_rcp85_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_anoxic_factor'])
        
                


#%%monthly_table_of_anpoxic_factor_ipsl_rcp85

# Specify the directory where the CSV files are located

#########original test with variable theta:
#########directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/ipsl_senarios/rcp85'


######## fixed theta both in calib and simulation 
######## directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/ipsl_senarios/rcp85_fixedtheta'


###### test with fixed theta in calibration a temp ave hypo in ipcl rcp85 for years 2020 and 2021
#######directory='C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/ipsl_senarios/rcp85_fixedthetaincalib_simurcp85temp20202021'



####### test with fixed theta in calibration but variable for GOTM simulation 
directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/ipsl_senarios/rcp85_calibinfixedtheta_simuvartheta'


# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_ipsl_rcp85_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Al = hypo_morpho_vriables_gotm_grid[2]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxic_factor function
        result = monthly_table_of_anpoxic_factor(C, time_series,Al, A0=23.67*10**6 , threshold=0.5)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_table_of_anpoxic_factor_ipsl_rcp85_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                

#%% Annual anoxic factor_miroc_his
# Specify the directory where the CSV files are located

#########original test with variable theta:
#########directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/miroc_senarios/his'


######## fixed theta both in calib and simulation 
#######directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/miroc_senarios/his_fixedtheta'




####### test with fixed theta in calibration but variable for GOTM simulation 
directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/miroc_senarios/his_calibinfixedtheta_simuvartheta'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_miroc_his_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Al = hypo_morpho_vriables_gotm_grid[2]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxic_factor function
        result = annual_anoxic_factor(C, time_series,Al, A0=23.67*10**6 , threshold=0.5)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_anoxic_factor_miroc_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_anoxic_factor'])
        
                


#%%monthly_table_of_anpoxic_factor_miroc_his

# Specify the directory where the CSV files are located

#########original test with variable theta:
#########directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/miroc_senarios/his'


######## fixed theta both in calib and simulation 
#######directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/miroc_senarios/his_fixedtheta'



####### test with fixed theta in calibration but variable for GOTM simulation 
directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/miroc_senarios/his_calibinfixedtheta_simuvartheta'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_miroc_his_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Al = hypo_morpho_vriables_gotm_grid[2]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxic_factor function
        result = monthly_table_of_anpoxic_factor(C, time_series,Al, A0=23.67*10**6 , threshold=0.5)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_table_of_anpoxic_factor_miroc_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                
#%% Annual anoxic factor_miroc_rcp26
# Specify the directory where the CSV files are located

#########original test with variable theta:
#########directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/miroc_senarios/rcp26'


######## fixed theta both in calib and simulation 
######## directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/miroc_senarios/rcp26_fixedtheta'


###### test with fixed theta in calibration a temp ave hypo in ipcl rcp26 for years 2020 and 2021
#######directory='C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/miroc_senarios/rcp26_fixedthetaincalib_simurcp26temp20202021'



####### test with fixed theta in calibration but variable for GOTM simulation 
directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/miroc_senarios/rcp26_calibinfixedtheta_simuvartheta'



# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_miroc_rcp26_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Al = hypo_morpho_vriables_gotm_grid[2]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxic_factor function
        result = annual_anoxic_factor(C, time_series,Al, A0=23.67*10**6 , threshold=0.5)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_anoxic_factor_miroc_rcp26_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_anoxic_factor'])
        
                


#%%monthly_table_of_anpoxic_factor_miroc_rcp26

# Specify the directory where the CSV files are located

#########original test with variable theta:
#########directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/miroc_senarios/rcp26'


######## fixed theta both in calib and simulation 
######## directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/miroc_senarios/rcp26_fixedtheta'


###### test with fixed theta in calibration a temp ave hypo in ipcl rcp26 for years 2020 and 2021
#######directory='C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/miroc_senarios/rcp26_fixedthetaincalib_simurcp26temp20202021'



####### test with fixed theta in calibration but variable for GOTM simulation 
directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/miroc_senarios/rcp26_calibinfixedtheta_simuvartheta'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_miroc_rcp26_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Al = hypo_morpho_vriables_gotm_grid[2]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxic_factor function
        result = monthly_table_of_anpoxic_factor(C, time_series,Al, A0=23.67*10**6 , threshold=0.5)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_table_of_anpoxic_factor_miroc_rcp26_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                

#%% Annual anoxic factor_miroc_rcp60
# Specify the directory where the CSV files are located

#########original test with variable theta:
#########directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/miroc_senarios/rcp60'


######## fixed theta both in calib and simulation 
######## directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/miroc_senarios/rcp60_fixedtheta'


###### test with fixed theta in calibration a temp ave hypo in ipcl rcp60 for years 2020 and 2021
#######directory='C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/miroc_senarios/rcp60_fixedthetaincalib_simurcp60temp20202021'



####### test with fixed theta in calibration but variable for GOTM simulation 
directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/miroc_senarios/rcp60_calibinfixedtheta_simuvartheta'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_miroc_rcp60_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Al = hypo_morpho_vriables_gotm_grid[2]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxic_factor function
        result = annual_anoxic_factor(C, time_series,Al, A0=23.67*10**6 , threshold=0.5)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_anoxic_factor_miroc_rcp60_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_anoxic_factor'])
        
                


#%%monthly_table_of_anpoxic_factor_miroc_rcp60

# Specify the directory where the CSV files are located
#########original test with variable theta:
#########directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/miroc_senarios/rcp60'


######## fixed theta both in calib and simulation 
######## directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/miroc_senarios/rcp60_fixedtheta'


###### test with fixed theta in calibration a temp ave hypo in ipcl rcp60 for years 2020 and 2021
#######directory='C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/miroc_senarios/rcp60_fixedthetaincalib_simurcp60temp20202021'



####### test with fixed theta in calibration but variable for GOTM simulation 
directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/miroc_senarios/rcp60_calibinfixedtheta_simuvartheta'



# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_miroc_rcp60_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Al = hypo_morpho_vriables_gotm_grid[2]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxic_factor function
        result = monthly_table_of_anpoxic_factor(C, time_series,Al, A0=23.67*10**6 , threshold=0.5)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_table_of_anpoxic_factor_miroc_rcp60_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                



#%% Annual anoxic factor_miroc_rcp85
# Specify the directory where the CSV files are located

#########original test with variable theta:
#########directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/miroc_senarios/rcp85'


######## fixed theta both in calib and simulation 
######## directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/miroc_senarios/rcp85_fixedtheta'


###### test with fixed theta in calibration a temp ave hypo in ipcl rcp85 for years 2020 and 2021
#######directory='C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/miroc_senarios/rcp85_fixedthetaincalib_simurcp85temp20202021'



####### test with fixed theta in calibration but variable for GOTM simulation 
directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/miroc_senarios/rcp85_calibinfixedtheta_simuvartheta'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_miroc_rcp85_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Al = hypo_morpho_vriables_gotm_grid[2]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxic_factor function
        result = annual_anoxic_factor(C, time_series,Al, A0=23.67*10**6 , threshold=0.5)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_anoxic_factor_miroc_rcp85_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_anoxic_factor'])
        
                


#%%monthly_table_of_anpoxic_factor_miroc_rcp85

# Specify the directory where the CSV files are located

#########original test with variable theta:
#########directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/miroc_senarios/rcp85'


######## fixed theta both in calib and simulation 
######## directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/miroc_senarios/rcp85_fixedtheta'


###### test with fixed theta in calibration a temp ave hypo in ipcl rcp85 for years 2020 and 2021
#######directory='C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/miroc_senarios/rcp85_fixedthetaincalib_simurcp85temp20202021'



####### test with fixed theta in calibration but variable for GOTM simulation 
directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/miroc_senarios/rcp85_calibinfixedtheta_simuvartheta'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_miroc_rcp85_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Al = hypo_morpho_vriables_gotm_grid[2]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxic_factor function
        result = monthly_table_of_anpoxic_factor(C, time_series,Al, A0=23.67*10**6 , threshold=0.5)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_table_of_anpoxic_factor_miroc_rcp85_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%GLUE method raeding again these files %%%%%%%%%%%%%%%%%%%

#%%his


# Specify the directory where the CSV files are located


#########original test with variable theta:
#########directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/gfdl_senarios/his'


######## fixed theta both in calib and simulation 
#######directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/gfdl_senarios/his_fixedtheta'




####### test with fixed theta in calibration but variable for GOTM simulation 
directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/gfdl_senarios/his_calibinfixedtheta_simuvartheta'



all_annual_anoxic_factor= pd.DataFrame([])
all_weights= np.array([])


# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("annual_anoxic_factor_gfdl_his"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        annual_anoxic_factor = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        annual_anoxic_factor=annual_anoxic_factor.set_index(annual_anoxic_factor['year'])
        
        all_annual_anoxic_factor = pd.concat([all_annual_anoxic_factor , annual_anoxic_factor['annual_anoxic_factor']], axis=1)
        

#########original test with variable theta:
#########directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/hadgem_senarios/his'


######## fixed theta both in calib and simulation 
#######directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/hadgem_senarios/his_fixedtheta'


####### test with fixed theta in calibration but variable for GOTM simulation 
directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/hadgem_senarios/his_calibinfixedtheta_simuvartheta'


# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("annual_anoxic_factor_hadgem_his"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        annual_anoxic_factor = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        annual_anoxic_factor=annual_anoxic_factor.set_index(annual_anoxic_factor['year'])
        
        all_annual_anoxic_factor = pd.concat([all_annual_anoxic_factor , annual_anoxic_factor['annual_anoxic_factor']], axis=1)
        
        
        

#########original test with variable theta:
#########directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/ipsl_senarios/his'


######## fixed theta both in calib and simulation 
#######directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/ipsl_senarios/his_fixedtheta'


####### test with fixed theta in calibration but variable for GOTM simulation 
directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/ipsl_senarios/his_calibinfixedtheta_simuvartheta'     

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("annual_anoxic_factor_ipsl_his"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        annual_anoxic_factor = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        annual_anoxic_factor=annual_anoxic_factor.set_index(annual_anoxic_factor['year'])
        
        all_annual_anoxic_factor = pd.concat([all_annual_anoxic_factor , annual_anoxic_factor['annual_anoxic_factor']], axis=1)
        
        
        

#########original test with variable theta:
#########directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/miroc_senarios/his'


######## fixed theta both in calib and simulation 
#######directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/miroc_senarios/his_fixedtheta'


####### test with fixed theta in calibration but variable for GOTM simulation 
directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/miroc_senarios/his_calibinfixedtheta_simuvartheta'     

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("annual_anoxic_factor_miroc_his"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        annual_anoxic_factor = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        annual_anoxic_factor=annual_anoxic_factor.set_index(annual_anoxic_factor['year'])
        
        all_annual_anoxic_factor = pd.concat([all_annual_anoxic_factor , annual_anoxic_factor['annual_anoxic_factor']], axis=1)
        
        
        
        


# annual anoxic duration  
timeseries_year_his= all_annual_anoxic_factor.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_annual_anoxic_factor.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights))

# Build glue df
glue_df_annual_anoxic_factor_his = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_df_annual_anoxic_factor_his=glue_df_annual_anoxic_factor_his.set_index(timeseries_year_his)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory

#########original test with variable theta:
#########glue_df_annual_anoxic_factor_his.to_csv('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/all_4_models/his/glue_df_anoxic_factor_his.csv')


######## fixed theta both in calib and simulation 
#########glue_df_annual_anoxic_factor_his.to_csv('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/all_4_models/his_fixedtheta/glue_df_anoxic_factor_his.csv')



####### test with fixed theta in calibration but variable for GOTM simulation 
glue_df_annual_anoxic_factor_his.to_csv('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/all_4_models/his_calibinfixedtheta_simuvartheta/glue_df_anoxic_factor_his.csv')

#%%rcp26


# Specify the directory where the CSV files are located


#########original test with variable theta:
#########directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/gfdl_senarios/rcp26'


######## fixed theta both in calib and simulation 
######## directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/gfdl_senarios/rcp26_fixedtheta'


###### test with fixed theta in calibration a temp ave hypo in ipcl rcp26 for years 2020 and 2021
#######directory='C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/gfdl_senarios/rcp26_fixedthetaincalib_simurcp26temp20202021'



####### test with fixed theta in calibration but variable for GOTM simulation 
directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/gfdl_senarios/rcp26_calibinfixedtheta_simuvartheta'



all_annual_anoxic_factor= pd.DataFrame([])
all_weights= np.array([])


# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("annual_anoxic_factor_gfdl_rcp26"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        annual_anoxic_factor = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        annual_anoxic_factor=annual_anoxic_factor.set_index(annual_anoxic_factor['year'])
        
        all_annual_anoxic_factor = pd.concat([all_annual_anoxic_factor , annual_anoxic_factor['annual_anoxic_factor']], axis=1)
        

#########original test with variable theta:
#########directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/hadgem_senarios/rcp26'


######## fixed theta both in calib and simulation 
######## directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/hadgem_senarios/rcp26_fixedtheta'


###### test with fixed theta in calibration a temp ave hypo in ipcl rcp26 for years 2020 and 2021
#######directory='C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/hadgem_senarios/rcp26_fixedthetaincalib_simurcp26temp20202021'



####### test with fixed theta in calibration but variable for GOTM simulation 
directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/hadgem_senarios/rcp26_calibinfixedtheta_simuvartheta'


# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("annual_anoxic_factor_hadgem_rcp26"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        annual_anoxic_factor = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        annual_anoxic_factor=annual_anoxic_factor.set_index(annual_anoxic_factor['year'])
        
        all_annual_anoxic_factor = pd.concat([all_annual_anoxic_factor , annual_anoxic_factor['annual_anoxic_factor']], axis=1)
        
        
        

#########original test with variable theta:
#########directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/ipsl_senarios/rcp26'


######## fixed theta both in calib and simulation 
######## directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/ipsl_senarios/rcp26_fixedtheta'


###### test with fixed theta in calibration a temp ave hypo in ipcl rcp26 for years 2020 and 2021
#######directory='C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/ipsl_senarios/rcp26_fixedthetaincalib_simurcp26temp20202021'



####### test with fixed theta in calibration but variable for GOTM simulation 
directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/ipsl_senarios/rcp26_calibinfixedtheta_simuvartheta'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("annual_anoxic_factor_ipsl_rcp26"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        annual_anoxic_factor = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        annual_anoxic_factor=annual_anoxic_factor.set_index(annual_anoxic_factor['year'])
        
        all_annual_anoxic_factor = pd.concat([all_annual_anoxic_factor , annual_anoxic_factor['annual_anoxic_factor']], axis=1)
        
        
        

#########original test with variable theta:
#########directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/miroc_senarios/rcp26'


######## fixed theta both in calib and simulation 
######## directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/miroc_senarios/rcp26_fixedtheta'


###### test with fixed theta in calibration a temp ave hypo in ipcl rcp26 for years 2020 and 2021
#######directory='C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/miroc_senarios/rcp26_fixedthetaincalib_simurcp26temp20202021'



####### test with fixed theta in calibration but variable for GOTM simulation 
directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/miroc_senarios/rcp26_calibinfixedtheta_simuvartheta'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("annual_anoxic_factor_miroc_rcp26"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        annual_anoxic_factor = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        annual_anoxic_factor=annual_anoxic_factor.set_index(annual_anoxic_factor['year'])
        
        all_annual_anoxic_factor = pd.concat([all_annual_anoxic_factor , annual_anoxic_factor['annual_anoxic_factor']], axis=1)
        
        
        
        


# annual anoxic duration  
timeseries_year_rcp26= all_annual_anoxic_factor.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_annual_anoxic_factor.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights))

# Build glue df
glue_df_annual_anoxic_factor_rcp26 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_df_annual_anoxic_factor_rcp26=glue_df_annual_anoxic_factor_rcp26.set_index(timeseries_year_rcp26)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory

#########original test with variable theta:
#########glue_df_annual_anoxic_factor_rcp26.to_csv('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/all_4_models/alltogther/glue_df_anoxic_factor_rcp26.csv')


######## fixed theta both in calib and simulation 
#########glue_df_annual_anoxic_factor_rcp26.to_csv('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/all_4_models/alltogther_fixedtheta/glue_df_anoxic_factor_rcp26.csv')


###### test with fixed theta in calibration a temp ave hypo in ipcl rcp26 for years 2020 and 2021
#########glue_df_annual_anoxic_factor_rcp26.to_csv('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/all_4_models/alltogther_fixedtheta_temp_gcms_2020_2021/glue_df_anoxic_factor_rcp26.csv')


####### test with fixed theta in calibration but variable for GOTM simulation 
glue_df_annual_anoxic_factor_rcp26.to_csv('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/all_4_models/alltogther_calibinfixedtheta_simuvartheta/glue_df_anoxic_factor_rcp26.csv')



#%%rcp60


# Specify the directory where the CSV files are located


#########original test with variable theta:
#########directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/gfdl_senarios/rcp60'


######## fixed theta both in calib and simulation 
######## directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/gfdl_senarios/rcp60_fixedtheta'


###### test with fixed theta in calibration a temp ave hypo in ipcl rcp60 for years 2020 and 2021
#######directory='C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/gfdl_senarios/rcp60_fixedthetaincalib_simurcp60temp20202021'



####### test with fixed theta in calibration but variable for GOTM simulation 
directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/gfdl_senarios/rcp60_calibinfixedtheta_simuvartheta'



all_annual_anoxic_factor= pd.DataFrame([])
all_weights= np.array([])


# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("annual_anoxic_factor_gfdl_rcp60"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        annual_anoxic_factor = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        annual_anoxic_factor=annual_anoxic_factor.set_index(annual_anoxic_factor['year'])
        
        all_annual_anoxic_factor = pd.concat([all_annual_anoxic_factor , annual_anoxic_factor['annual_anoxic_factor']], axis=1)
        

#########original test with variable theta:
#########directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/hadgem_senarios/rcp60'


######## fixed theta both in calib and simulation 
######## directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/hadgem_senarios/rcp60_fixedtheta'


###### test with fixed theta in calibration a temp ave hypo in ipcl rcp60 for years 2020 and 2021
#######directory='C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/hadgem_senarios/rcp60_fixedthetaincalib_simurcp60temp20202021'



####### test with fixed theta in calibration but variable for GOTM simulation 
directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/hadgem_senarios/rcp60_calibinfixedtheta_simuvartheta'


# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("annual_anoxic_factor_hadgem_rcp60"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        annual_anoxic_factor = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        annual_anoxic_factor=annual_anoxic_factor.set_index(annual_anoxic_factor['year'])
        
        all_annual_anoxic_factor = pd.concat([all_annual_anoxic_factor , annual_anoxic_factor['annual_anoxic_factor']], axis=1)
        
        
        

#########original test with variable theta:
#########directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/ipsl_senarios/rcp60'


######## fixed theta both in calib and simulation 
######## directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/ipsl_senarios/rcp60_fixedtheta'


###### test with fixed theta in calibration a temp ave hypo in ipcl rcp60 for years 2020 and 2021
#######directory='C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/ipsl_senarios/rcp60_fixedthetaincalib_simurcp60temp20202021'



####### test with fixed theta in calibration but variable for GOTM simulation 
directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/ipsl_senarios/rcp60_calibinfixedtheta_simuvartheta'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("annual_anoxic_factor_ipsl_rcp60"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        annual_anoxic_factor = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        annual_anoxic_factor=annual_anoxic_factor.set_index(annual_anoxic_factor['year'])
        
        all_annual_anoxic_factor = pd.concat([all_annual_anoxic_factor , annual_anoxic_factor['annual_anoxic_factor']], axis=1)
        
        
        

#########original test with variable theta:
#########directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/miroc_senarios/rcp60'


######## fixed theta both in calib and simulation 
######## directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/miroc_senarios/rcp60_fixedtheta'


###### test with fixed theta in calibration a temp ave hypo in ipcl rcp60 for years 2020 and 2021
#######directory='C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/miroc_senarios/rcp60_fixedthetaincalib_simurcp60temp20202021'



####### test with fixed theta in calibration but variable for GOTM simulation 
directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/miroc_senarios/rcp60_calibinfixedtheta_simuvartheta'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("annual_anoxic_factor_miroc_rcp60"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        annual_anoxic_factor = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        annual_anoxic_factor=annual_anoxic_factor.set_index(annual_anoxic_factor['year'])
        
        all_annual_anoxic_factor = pd.concat([all_annual_anoxic_factor , annual_anoxic_factor['annual_anoxic_factor']], axis=1)
        
        
        
        


# annual anoxic duration  
timeseries_year_rcp60= all_annual_anoxic_factor.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_annual_anoxic_factor.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights))

# Build glue df
glue_df_annual_anoxic_factor_rcp60 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_df_annual_anoxic_factor_rcp60=glue_df_annual_anoxic_factor_rcp60.set_index(timeseries_year_rcp60)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory

#########original test with variable theta:
#########glue_df_annual_anoxic_factor_rcp60.to_csv('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/all_4_models/alltogther/glue_df_anoxic_factor_rcp60.csv')


######## fixed theta both in calib and simulation 
#########glue_df_annual_anoxic_factor_rcp60.to_csv('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/all_4_models/alltogther_fixedtheta/glue_df_anoxic_factor_rcp60.csv')


###### test with fixed theta in calibration a temp ave hypo in ipcl rcp60 for years 2020 and 2021
#########glue_df_annual_anoxic_factor_rcp60.to_csv('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/all_4_models/alltogther_fixedtheta_temp_gcms_2020_2021/glue_df_anoxic_factor_rcp60.csv')


####### test with fixed theta in calibration but variable for GOTM simulation 
glue_df_annual_anoxic_factor_rcp60.to_csv('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/all_4_models/alltogther_calibinfixedtheta_simuvartheta/glue_df_anoxic_factor_rcp60.csv')



#%%rcp85


# Specify the directory where the CSV files are located


#########original test with variable theta:
#########directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/gfdl_senarios/rcp85'


######## fixed theta both in calib and simulation 
######## directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/gfdl_senarios/rcp85_fixedtheta'


###### test with fixed theta in calibration a temp ave hypo in ipcl rcp85 for years 2020 and 2021
#######directory='C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/gfdl_senarios/rcp85_fixedthetaincalib_simurcp85temp20202021'



####### test with fixed theta in calibration but variable for GOTM simulation 
directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/gfdl_senarios/rcp85_calibinfixedtheta_simuvartheta'



all_annual_anoxic_factor= pd.DataFrame([])
all_weights= np.array([])


# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("annual_anoxic_factor_gfdl_rcp85"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        annual_anoxic_factor = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        annual_anoxic_factor=annual_anoxic_factor.set_index(annual_anoxic_factor['year'])
        
        all_annual_anoxic_factor = pd.concat([all_annual_anoxic_factor , annual_anoxic_factor['annual_anoxic_factor']], axis=1)
        

#########original test with variable theta:
#########directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/hadgem_senarios/rcp85'


######## fixed theta both in calib and simulation 
######## directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/hadgem_senarios/rcp85_fixedtheta'


###### test with fixed theta in calibration a temp ave hypo in ipcl rcp85 for years 2020 and 2021
#######directory='C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/hadgem_senarios/rcp85_fixedthetaincalib_simurcp85temp20202021'



####### test with fixed theta in calibration but variable for GOTM simulation 
directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/hadgem_senarios/rcp85_calibinfixedtheta_simuvartheta'


# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("annual_anoxic_factor_hadgem_rcp85"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        annual_anoxic_factor = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        annual_anoxic_factor=annual_anoxic_factor.set_index(annual_anoxic_factor['year'])
        
        all_annual_anoxic_factor = pd.concat([all_annual_anoxic_factor , annual_anoxic_factor['annual_anoxic_factor']], axis=1)
        
        
        

#########original test with variable theta:
#########directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/ipsl_senarios/rcp85'


######## fixed theta both in calib and simulation 
######## directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/ipsl_senarios/rcp85_fixedtheta'


###### test with fixed theta in calibration a temp ave hypo in ipcl rcp85 for years 2020 and 2021
#######directory='C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/ipsl_senarios/rcp85_fixedthetaincalib_simurcp85temp20202021'



####### test with fixed theta in calibration but variable for GOTM simulation 
directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/ipsl_senarios/rcp85_calibinfixedtheta_simuvartheta'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("annual_anoxic_factor_ipsl_rcp85"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        annual_anoxic_factor = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        annual_anoxic_factor=annual_anoxic_factor.set_index(annual_anoxic_factor['year'])
        
        all_annual_anoxic_factor = pd.concat([all_annual_anoxic_factor , annual_anoxic_factor['annual_anoxic_factor']], axis=1)
        
        
        

#########original test with variable theta:
#########directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/miroc_senarios/rcp85'


######## fixed theta both in calib and simulation 
######## directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/miroc_senarios/rcp85_fixedtheta'


###### test with fixed theta in calibration a temp ave hypo in ipcl rcp85 for years 2020 and 2021
#######directory='C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/miroc_senarios/rcp85_fixedthetaincalib_simurcp85temp20202021'



####### test with fixed theta in calibration but variable for GOTM simulation 
directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/miroc_senarios/rcp85_calibinfixedtheta_simuvartheta'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("annual_anoxic_factor_miroc_rcp85"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        annual_anoxic_factor = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        annual_anoxic_factor=annual_anoxic_factor.set_index(annual_anoxic_factor['year'])
        
        all_annual_anoxic_factor = pd.concat([all_annual_anoxic_factor , annual_anoxic_factor['annual_anoxic_factor']], axis=1)
        
        
        
        


# annual anoxic duration  
timeseries_year_rcp85= all_annual_anoxic_factor.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_annual_anoxic_factor.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights))

# Build glue df
glue_df_annual_anoxic_factor_rcp85 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_df_annual_anoxic_factor_rcp85=glue_df_annual_anoxic_factor_rcp85.set_index(timeseries_year_rcp85)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory

#########original test with variable theta:
#########glue_df_annual_anoxic_factor_rcp85.to_csv('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/all_4_models/alltogther/glue_df_anoxic_factor_rcp85.csv')


######## fixed theta both in calib and simulation 
#########glue_df_annual_anoxic_factor_rcp85.to_csv('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/all_4_models/alltogther_fixedtheta/glue_df_anoxic_factor_rcp85.csv')


###### test with fixed theta in calibration a temp ave hypo in ipcl rcp85 for years 2020 and 2021
#########glue_df_annual_anoxic_factor_rcp85.to_csv('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/all_4_models/alltogther_fixedtheta_temp_gcms_2020_2021/glue_df_anoxic_factor_rcp85.csv')


####### test with fixed theta in calibration but variable for GOTM simulation 
glue_df_annual_anoxic_factor_rcp85.to_csv('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/all_4_models/alltogther_calibinfixedtheta_simuvartheta/glue_df_anoxic_factor_rcp85.csv')


#%%#######fixed theta:
    
#######glue_df_annual_anoxic_factor_his_fixedtheta=  glue_df_annual_anoxic_factor_his.copy()

glue_df_annual_anoxic_factor_his= glue_df_annual_anoxic_factor_his_fixedtheta.copy()

#######glue_df_annual_anoxic_factor_rcp26_fixedtheta=  glue_df_annual_anoxic_factor_rcp26.copy()

glue_df_annual_anoxic_factor_rcp26= glue_df_annual_anoxic_factor_rcp26_fixedtheta.copy()

#######glue_df_annual_anoxic_factor_rcp60_fixedtheta=  glue_df_annual_anoxic_factor_rcp60.copy()

glue_df_annual_anoxic_factor_rcp60= glue_df_annual_anoxic_factor_rcp60_fixedtheta.copy()

#######glue_df_annual_anoxic_factor_rcp85_fixedtheta=  glue_df_annual_anoxic_factor_rcp85.copy()

glue_df_annual_anoxic_factor_rcp85= glue_df_annual_anoxic_factor_rcp85_fixedtheta.copy()



#%%_vartheta

glue_df_annual_anoxic_factor_his_vartheta= glue_df_annual_anoxic_factor_his.copy()



glue_df_annual_anoxic_factor_rcp26_vartheta= glue_df_annual_anoxic_factor_rcp26.copy()


glue_df_annual_anoxic_factor_rcp60_vartheta= glue_df_annual_anoxic_factor_rcp60.copy()


glue_df_annual_anoxic_factor_rcp85_vartheta= glue_df_annual_anoxic_factor_rcp85.copy()


#%%difference of Vartheta model and fixed theta 


diff_median_annual_anoxic_factor_vartheta_fixedtheta_his=glue_df_annual_anoxic_factor_his_vartheta['50%']-glue_df_annual_anoxic_factor_his['50%']
np.mean(diff_median_annual_anoxic_factor_vartheta_fixedtheta_his)
-1.521539830552154

autocorr_MK_org_modif_sens_slope_test(diff_median_annual_anoxic_factor_vartheta_fixedtheta_his)
(0.4102745697759908,
 'positively autocorrelated',
 'no trend',
 0.08641995700155558,
 0,
 0)




diff_median_annual_anoxic_factor_vartheta_fixedtheta_rcp26=glue_df_annual_anoxic_factor_rcp26_vartheta['50%']-glue_df_annual_anoxic_factor_rcp26['50%']
np.mean(diff_median_annual_anoxic_factor_vartheta_fixedtheta_rcp26)
-2.3009426195783225
autocorr_MK_org_modif_sens_slope_test(diff_median_annual_anoxic_factor_vartheta_fixedtheta_rcp26)

(0.2471291056619972,
 'positively autocorrelated',
 'no trend',
 0.5406757306713583,
 0,
 0)



diff_median_annual_anoxic_factor_vartheta_fixedtheta_rcp60=glue_df_annual_anoxic_factor_rcp60_vartheta['50%']-glue_df_annual_anoxic_factor_rcp60['50%']
np.mean(diff_median_annual_anoxic_factor_vartheta_fixedtheta_rcp60)
-1.3593195664094877

autocorr_MK_org_modif_sens_slope_test(diff_median_annual_anoxic_factor_vartheta_fixedtheta_rcp60)
(0.45142216245912026,
 'positively autocorrelated',
 'no trend',
 0.24575216426645285,
 0,
 0)



diff_median_annual_anoxic_factor_vartheta_fixedtheta_rcp85=glue_df_annual_anoxic_factor_rcp85_vartheta['50%']-glue_df_annual_anoxic_factor_rcp85['50%']
np.mean(diff_median_annual_anoxic_factor_vartheta_fixedtheta_rcp85)
-1.8403265395237618

autocorr_MK_org_modif_sens_slope_test(diff_median_annual_anoxic_factor_vartheta_fixedtheta_rcp85)
(0.4311903996849538,
 'positively autocorrelated',
 'no trend',
 0.05029548584424548,
 0,
 0)


#Plot the difference of median

import matplotlib.pyplot as plt

fig =plt.figure(figsize=(15, 10))
ax= plt.subplot(111)


ax=plt.plot(diff_median_annual_anoxic_factor_vartheta_fixedtheta_his.index, diff_median_annual_anoxic_factor_vartheta_fixedtheta_his, 'grey', label='His median', alpha=1, linewidth=3 )


ax=plt.plot(diff_median_annual_anoxic_factor_vartheta_fixedtheta_rcp26.index, diff_median_annual_anoxic_factor_vartheta_fixedtheta_rcp26, 'green', label='RCP2.6 median', alpha=1, linewidth=3 )

ax=plt.plot(diff_median_annual_anoxic_factor_vartheta_fixedtheta_rcp60.index, diff_median_annual_anoxic_factor_vartheta_fixedtheta_rcp60, 'yellow', label='RCP6.0 median',alpha=1, linewidth=3 )

ax=plt.plot(diff_median_annual_anoxic_factor_vartheta_fixedtheta_rcp85.index, diff_median_annual_anoxic_factor_vartheta_fixedtheta_rcp85, 'r', label='RCP8.5 median', alpha=0.9, linewidth=3 )



ax=plt.ylabel('Difference of fixed and variable Ktemp assumption in simulating annual anoxic factor [d year$^{-1}$]' , fontsize=26)
ax=plt.xlabel('Year' , fontsize=26)
ax=plt.yticks(np.arange(-4, 3, 1) , fontsize= 22)
ax=plt.xticks(rotation=45 , fontsize=22)
ax=plt.legend(bbox_to_anchor=(0.7, -0.15), fontsize=22)


####### test with fixed theta in calibration but variable for GOTM simulation 
fig.savefig("GLUE_Timeseries_hypolimnetic_DO_6combinationJaJv_ave_obs_4models_diff_fixed_var_theta.png", dpi=300, bbox_inches='tight')




#%% first 10 years 2020-2029

#rcp26
glue_df_annual_anoxic_factor_median_1st_10years_rcp26=glue_df_annual_anoxic_factor_rcp26[(2019<glue_df_annual_anoxic_factor_rcp26.index) & (glue_df_annual_anoxic_factor_rcp26.index<2030)]['50%']
np.mean(glue_df_annual_anoxic_factor_median_1st_10years_rcp26)
#7.470031426050075

glue_df_annual_anoxic_factor_median_1st_10years_rcp26_vartheta=glue_df_annual_anoxic_factor_rcp26_vartheta[(2019<glue_df_annual_anoxic_factor_rcp26_vartheta.index) & (glue_df_annual_anoxic_factor_rcp26_vartheta.index<2030)]['50%']
np.mean(glue_df_annual_anoxic_factor_median_1st_10years_rcp26_vartheta)
#5.655030434919324


#rcp60

glue_df_annual_anoxic_factor_median_1st_10years_rcp60=glue_df_annual_anoxic_factor_rcp60[(2019<glue_df_annual_anoxic_factor_rcp60.index) & (glue_df_annual_anoxic_factor_rcp60.index<2030)]['50%']
np.mean(glue_df_annual_anoxic_factor_median_1st_10years_rcp60)
#7.077280785340525



glue_df_annual_anoxic_factor_median_1st_10years_rcp60_vartheta=glue_df_annual_anoxic_factor_rcp60_vartheta[(2019<glue_df_annual_anoxic_factor_rcp60_vartheta.index) & (glue_df_annual_anoxic_factor_rcp60_vartheta.index<2030)]['50%']
np.mean(glue_df_annual_anoxic_factor_median_1st_10years_rcp60_vartheta)
#5.442294872796134

#rcp85

glue_df_annual_anoxic_factor_median_1st_10years_rcp85=glue_df_annual_anoxic_factor_rcp85[(2019<glue_df_annual_anoxic_factor_rcp85.index) & (glue_df_annual_anoxic_factor_rcp85.index<2030)]['50%']
np.mean(glue_df_annual_anoxic_factor_median_1st_10years_rcp85)
#6.80621601212993

glue_df_annual_anoxic_factor_median_1st_10years_rcp85_vartheta=glue_df_annual_anoxic_factor_rcp85_vartheta[(2019<glue_df_annual_anoxic_factor_rcp85_vartheta.index) & (glue_df_annual_anoxic_factor_rcp85_vartheta.index<2030)]['50%']
np.mean(glue_df_annual_anoxic_factor_median_1st_10years_rcp85_vartheta)
#5.589130553716512

#%%last 10 years 2090-2099

#rcp26
glue_df_annual_anoxic_factor_median_last_10years_rcp26=glue_df_annual_anoxic_factor_rcp26[glue_df_annual_anoxic_factor_rcp26.index>2089]['50%']
np.mean(glue_df_annual_anoxic_factor_median_last_10years_rcp26)
#8.613753815447875

glue_df_annual_anoxic_factor_median_last_10years_rcp26_vartheta=glue_df_annual_anoxic_factor_rcp26_vartheta[glue_df_annual_anoxic_factor_rcp26_vartheta.index>2089]['50%']
np.mean(glue_df_annual_anoxic_factor_median_last_10years_rcp26_vartheta)
#5.99974215818178

#rcp60
glue_df_annual_anoxic_factor_median_last_10years_rcp60=glue_df_annual_anoxic_factor_rcp60[glue_df_annual_anoxic_factor_rcp60.index>2089]['50%']
np.mean(glue_df_annual_anoxic_factor_median_last_10years_rcp60)
#8.840670784774442

glue_df_annual_anoxic_factor_median_last_10years_rcp60_vartheta=glue_df_annual_anoxic_factor_rcp60_vartheta[glue_df_annual_anoxic_factor_rcp60_vartheta.index>2089]['50%']
np.mean(glue_df_annual_anoxic_factor_median_last_10years_rcp60_vartheta)
#7.461205289215991
#rcp85
glue_df_annual_anoxic_factor_median_last_10years_rcp85=glue_df_annual_anoxic_factor_rcp85[glue_df_annual_anoxic_factor_rcp85.index>2089]['50%']
np.mean(glue_df_annual_anoxic_factor_median_last_10years_rcp85)
#10.848450635366076

glue_df_annual_anoxic_factor_median_last_10years_rcp85_vartheta=glue_df_annual_anoxic_factor_rcp85_vartheta[glue_df_annual_anoxic_factor_rcp85_vartheta.index>2089]['50%']
np.mean(glue_df_annual_anoxic_factor_median_last_10years_rcp85_vartheta)
#9.225106418152142

#%% 100 years for rcps 

#rcp26

#fixed theta
glue_df_annual_anoxic_factor_4models_100years_rcp26=pd.concat([glue_df_annual_anoxic_factor_his[glue_df_annual_anoxic_factor_his.index>1999] , glue_df_annual_anoxic_factor_rcp26])
autocorr_MK_org_modif_sens_slope_test( glue_df_annual_anoxic_factor_4models_100years_rcp26 ['50%'])  

(0.03233165257593502,
 'positively autocorrelated',
 'increasing',
 1.235052435877293e-07,
 0.0121937938499866,
 7.255097746966682)





#Var theta
glue_df_annual_anoxic_factor_4models_100years_rcp26_vartheta=pd.concat([glue_df_annual_anoxic_factor_his_vartheta[glue_df_annual_anoxic_factor_his_vartheta.index>1999] , glue_df_annual_anoxic_factor_rcp26_vartheta])
autocorr_MK_org_modif_sens_slope_test( glue_df_annual_anoxic_factor_4models_100years_rcp26_vartheta ['50%'])  

(0.03955505915646442,
 'positively autocorrelated',
 'increasing',
 0.0006010992236442636,
 0.010497984593900105,
 5.030834333984101)



#rcp60

#fixed theta
glue_df_annual_anoxic_factor_4models_100years_rcp60=pd.concat([glue_df_annual_anoxic_factor_his[glue_df_annual_anoxic_factor_his.index>1999] , glue_df_annual_anoxic_factor_rcp60])
autocorr_MK_org_modif_sens_slope_test( glue_df_annual_anoxic_factor_4models_100years_rcp60 ['50%'])  
(0.02795672807292709,
 'positively autocorrelated',
 'increasing',
 2.220446049250313e-16,
 0.0332750689583886,
 5.986757230735907)




#Var theta
glue_df_annual_anoxic_factor_4models_100years_rcp60_vartheta=pd.concat([glue_df_annual_anoxic_factor_his_vartheta[glue_df_annual_anoxic_factor_his_vartheta.index>1999] , glue_df_annual_anoxic_factor_rcp60_vartheta])
autocorr_MK_org_modif_sens_slope_test( glue_df_annual_anoxic_factor_4models_100years_rcp60_vartheta ['50%'])  
(0.029177475988549587,
 'positively autocorrelated',
 'increasing',
 2.970956813896919e-13,
 0.03420571640423424,
 4.397863069746866)


#rcp85

#fixed theta
glue_df_annual_anoxic_factor_4models_100years_rcp85=pd.concat([glue_df_annual_anoxic_factor_his[glue_df_annual_anoxic_factor_his.index>1999] , glue_df_annual_anoxic_factor_rcp85])
autocorr_MK_org_modif_sens_slope_test( glue_df_annual_anoxic_factor_4models_100years_rcp85 ['50%'])  
(0.031072004914250547,
 'positively autocorrelated',
 'increasing',
 0.0,
 0.05455817956023478,
 5.832292270455436)




#Var theta
glue_df_annual_anoxic_factor_4models_100years_rcp85_vartheta=pd.concat([glue_df_annual_anoxic_factor_his_vartheta[glue_df_annual_anoxic_factor_his_vartheta.index>1999] , glue_df_annual_anoxic_factor_rcp85_vartheta])
autocorr_MK_org_modif_sens_slope_test( glue_df_annual_anoxic_factor_4models_100years_rcp85_vartheta ['50%'])  

(0.035580951696717295,
 'positively autocorrelated',
 'increasing',
 0.0,
 0.05165045008766002,
 3.9207344560109947)

#%% trendline sen's slope 

autocorr_MK_org_modif_sens_slope_test(glue_df_annual_anoxic_factor_his['50%']) 

Out[1243]: 
(0.08861134396877238,
 'positively autocorrelated',
 'no trend',
 0.10192618852194646,
 0,
 0)



autocorr_MK_org_modif_sens_slope_test(glue_df_annual_anoxic_factor_his_vartheta['50%']) 

(0.1383412609645987,
 'positively autocorrelated',
 'no trend',
 0.31072008139962315,
 0,
 0)



autocorr_MK_org_modif_sens_slope_test(glue_df_annual_anoxic_factor_rcp26['50%']) 
(0.03379118006876991,
 'positively autocorrelated',
 'increasing',
 6.908279212325397e-05,
 0.010564337601135008,
 7.4785025189153735)
autocorr_MK_org_modif_sens_slope_test(glue_df_annual_anoxic_factor_rcp26_vartheta['50%']) 
(0.039507716688300144,
 'positively autocorrelated',
 'increasing',
 0.022504355893704142,
 0.008218111766768784,
 5.1831384217248875)



autocorr_MK_org_modif_sens_slope_test(glue_df_annual_anoxic_factor_rcp60['50%']) 
(0.028720309370685593,
 'positively autocorrelated',
 'increasing',
 0.0,
 0.03880652178553318,
 5.88161432295651)
autocorr_MK_org_modif_sens_slope_test(glue_df_annual_anoxic_factor_rcp60_vartheta['50%']) 
(0.028883853368500165,
 'positively autocorrelated',
 'increasing',
 7.286293790542686e-10,
 0.033514404467106934,
 4.616452079764355)


autocorr_MK_org_modif_sens_slope_test(glue_df_annual_anoxic_factor_rcp85['50%']) 
(0.03167796451466309,
 'positively autocorrelated',
 'increasing',
 0.0,
 0.059792750353943616,
 5.873773932605548)
autocorr_MK_org_modif_sens_slope_test(glue_df_annual_anoxic_factor_rcp85_vartheta['50%']) 
(0.03389759807269532,
 'positively autocorrelated',
 'increasing',
 0.0,
 0.05300685412619691,
 4.1760561507416)



#%%Plotiing%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#%%Annual anoxic factor 

#Vartheta

#########original test with variable theta:
#########os.chdir('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/all_4_models/alltogther/')


######## fixed theta both in calib and simulation 
########os.chdir('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/all_4_models/alltogther_fixedtheta/')


###### test with fixed theta in calibration a temp ave hypo in GCMs in 2020 2021
######os.chdir('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/all_4_models/alltogther_fixedtheta_temp_gcms_2020_2021/')


####### test with fixed theta in calibration but variable for GOTM simulation 
os.chdir('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/all_4_models/alltogther_calibinfixedtheta_simuvartheta/')


import matplotlib.pyplot as plt

fig = plt.figure(figsize=(15, 10))
ax= plt.subplot(111)


#ax=plt.fill_between(glue_df_annual_anoxic_factor_his.index.astype(float), glue_df_annual_anoxic_factor_his['5%'], glue_df_annual_anoxic_factor_his['95%'], color='grey', alpha=0.2 ,  label= 'His 90% CI')
#ax=plt.plot(glue_df_annual_anoxic_factor_his.index.astype(float), glue_df_annual_anoxic_factor_his['50%'].astype(float), 'k', label='His median', alpha=0.9, linewidth=3  )



ax=plt.fill_between(glue_df_annual_anoxic_factor_4models_100years_rcp26_vartheta.index.astype(float), glue_df_annual_anoxic_factor_4models_100years_rcp26_vartheta['5%'], glue_df_annual_anoxic_factor_4models_100years_rcp26_vartheta['95%'], color='darkgreen', alpha=0.3 ,  label= 'RCP2.6 90% CI')
ax=plt.plot(glue_df_annual_anoxic_factor_4models_100years_rcp26_vartheta.index.astype(float), glue_df_annual_anoxic_factor_4models_100years_rcp26_vartheta['50%'], 'darkgreen', label='RCP2.6 median', alpha=0.9, linewidth=3  )
trendline_rcp26=autocorr_MK_org_modif_sens_slope_test(glue_df_annual_anoxic_factor_4models_100years_rcp26_vartheta['50%'])
ax=plt.text(2020, 10, f'y = {trendline_rcp26[-2]:.3f}x + {trendline_rcp26[-1]:.3f}, p-value < 0.05', color='green', fontsize= 20 )


ax=plt.fill_between(glue_df_annual_anoxic_factor_4models_100years_rcp60_vartheta.index.astype(float), glue_df_annual_anoxic_factor_4models_100years_rcp60_vartheta['5%'], glue_df_annual_anoxic_factor_4models_100years_rcp60_vartheta['95%'], color='yellow', alpha=0.2 ,  label= 'RCP6.0 90% CI')
ax=plt.plot(glue_df_annual_anoxic_factor_4models_100years_rcp60_vartheta.index.astype(float), glue_df_annual_anoxic_factor_4models_100years_rcp60_vartheta['50%'], 'yellow', label='RCP6.0 median', alpha=0.9, linewidth=3  )
trendline_rcp60=autocorr_MK_org_modif_sens_slope_test(glue_df_annual_anoxic_factor_4models_100years_rcp60_vartheta['50%'])
ax=plt.text(2020, 11, f'y = {trendline_rcp60[-2]:.3f}x + {trendline_rcp60[-1]:.3f}, p-value < 0.05', color='gold', fontsize= 20 )



ax=plt.fill_between(glue_df_annual_anoxic_factor_4models_100years_rcp85_vartheta.index.astype(float), glue_df_annual_anoxic_factor_4models_100years_rcp85_vartheta['5%'], glue_df_annual_anoxic_factor_4models_100years_rcp85_vartheta['95%'], color='r', alpha=0.2 ,  label= 'RCP8.5 90% CI')
ax=plt.plot(glue_df_annual_anoxic_factor_4models_100years_rcp85_vartheta.index.astype(float), glue_df_annual_anoxic_factor_4models_100years_rcp85_vartheta['50%'], 'r', label='RCP8.5 median', alpha=0.9, linewidth=3  )
trendline_rcp85=autocorr_MK_org_modif_sens_slope_test(glue_df_annual_anoxic_factor_4models_100years_rcp85_vartheta['50%'])
ax=plt.text(2020, 12, f'y = {trendline_rcp85[-2]:.3f}x + {trendline_rcp85[-1]:.3f}, p-value < 0.05', color='r', fontsize= 20 )



ax=plt.ylabel('Anoxic factor per each deoxygenation period [d/year]' , fontsize=26)
ax=plt.xlabel('Year' , fontsize=26)
ax=plt.yticks(fontsize= 22)
ax=plt.xticks(fontsize=22)#rotation=45 , 
ax=plt.legend(bbox_to_anchor=(0.7, -0.2), fontsize=22)#)   
fig.savefig("GLUE_100years_Timeseries_anoxic_factor_7combinationJaJv_ave_obs_4models_4scenarios.png",  dpi=300, bbox_inches='tight')


#%%fixed theta




#########original test with variable theta:
#########os.chdir('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/all_4_models/alltogther/')


######## fixed theta both in calib and simulation 
########os.chdir('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/all_4_models/alltogther_fixedtheta/')


###### test with fixed theta in calibration a temp ave hypo in GCMs in 2020 2021
os.chdir('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/all_4_models/alltogther_fixedtheta_temp_gcms_2020_2021/')


####### test with fixed theta in calibration but variable for GOTM simulation 
######os.chdir('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/all_4_models/alltogther_calibinfixedtheta_simuvartheta/')


import matplotlib.pyplot as plt

fig = plt.figure(figsize=(15, 10))
ax= plt.subplot(111)


#ax=plt.fill_between(glue_df_annual_anoxic_factor_his.index.astype(float), glue_df_annual_anoxic_factor_his['5%'], glue_df_annual_anoxic_factor_his['95%'], color='grey', alpha=0.2 ,  label= 'His 90% CI')
#ax=plt.plot(glue_df_annual_anoxic_factor_his.index.astype(float), glue_df_annual_anoxic_factor_his['50%'].astype(float), 'k', label='His median', alpha=0.9, linewidth=3  )



ax=plt.fill_between(glue_df_annual_anoxic_factor_4models_100years_rcp26.index.astype(float), glue_df_annual_anoxic_factor_4models_100years_rcp26['5%'], glue_df_annual_anoxic_factor_4models_100years_rcp26['95%'], color='darkgreen', alpha=0.3 ,  label= 'RCP2.6 90% CI')
ax=plt.plot(glue_df_annual_anoxic_factor_4models_100years_rcp26.index.astype(float), glue_df_annual_anoxic_factor_4models_100years_rcp26['50%'], 'darkgreen', label='RCP2.6 median', alpha=0.9, linewidth=3  )
trendline_rcp26=autocorr_MK_org_modif_sens_slope_test(glue_df_annual_anoxic_factor_4models_100years_rcp26['50%'])
ax=plt.text(2020, 15, f'y = {trendline_rcp26[-2]:.3f}x + {trendline_rcp26[-1]:.3f}, p-value < 0.05', color='green', fontsize= 20 )


ax=plt.fill_between(glue_df_annual_anoxic_factor_4models_100years_rcp60.index.astype(float), glue_df_annual_anoxic_factor_4models_100years_rcp60['5%'], glue_df_annual_anoxic_factor_4models_100years_rcp60['95%'], color='yellow', alpha=0.2 ,  label= 'RCP6.0 90% CI')
ax=plt.plot(glue_df_annual_anoxic_factor_4models_100years_rcp60.index.astype(float), glue_df_annual_anoxic_factor_4models_100years_rcp60['50%'], 'yellow', label='RCP6.0 median', alpha=0.9, linewidth=3  )
trendline_rcp60=autocorr_MK_org_modif_sens_slope_test(glue_df_annual_anoxic_factor_4models_100years_rcp60['50%'])
ax=plt.text(2020, 14, f'y = {trendline_rcp60[-2]:.3f}x + {trendline_rcp60[-1]:.3f}, p-value < 0.05', color='gold', fontsize= 20 )



ax=plt.fill_between(glue_df_annual_anoxic_factor_4models_100years_rcp85.index.astype(float), glue_df_annual_anoxic_factor_4models_100years_rcp85['5%'], glue_df_annual_anoxic_factor_4models_100years_rcp85['95%'], color='r', alpha=0.2 ,  label= 'RCP8.5 90% CI')
ax=plt.plot(glue_df_annual_anoxic_factor_4models_100years_rcp85.index.astype(float), glue_df_annual_anoxic_factor_4models_100years_rcp85['50%'], 'r', label='RCP8.5 median', alpha=0.9, linewidth=3  )
trendline_rcp85=autocorr_MK_org_modif_sens_slope_test(glue_df_annual_anoxic_factor_4models_100years_rcp85['50%'])
ax=plt.text(2020, 13, f'y = {trendline_rcp85[-2]:.3f}x + {trendline_rcp85[-1]:.3f}, p-value < 0.05', color='r', fontsize= 20 )



ax=plt.ylabel('Anoxic factor per each deoxygenation period [d/year]' , fontsize=26)
ax=plt.xlabel('Year' , fontsize=26)
ax=plt.yticks(fontsize= 22)
ax=plt.xticks(fontsize=22)#rotation=45 , 
ax=plt.legend(bbox_to_anchor=(0.7, -0.2), fontsize=22)#)   
fig.savefig("GLUE_100years_Timeseries_anoxic_factor_7combinationJaJv_ave_obs_4models_4scenarios.png",  dpi=300, bbox_inches='tight')




#%%
# original # fixed gcm temp in 2020 and 2021
np.mean(glue_df_annual_anoxic_factor_his['50%'])#5.118056494914366# 5.371846482897608
np.mean(glue_df_annual_anoxic_factor_rcp26['50%'])#7.009871810216667# 7.960074150018018
np.mean(glue_df_annual_anoxic_factor_rcp60['50%'])#7.599031745432739# 7.661889247294462
np.mean(glue_df_annual_anoxic_factor_rcp85['50%'])#8.15444840073441#8.680607289244922

np.mean(glue_df_annual_anoxic_factor_his_vartheta['50%'])#3.8503066523454508
np.mean(glue_df_annual_anoxic_factor_rcp26_vartheta['50%'])#5.659131530439698
np.mean(glue_df_annual_anoxic_factor_rcp60_vartheta['50%'])#6.302569680884974
np.mean(glue_df_annual_anoxic_factor_rcp85_vartheta['50%'])#6.840280749721157



#%%anoxic_factor 30 yerars from each scenarios compare 


#Sorting the glue dataframe according to the index (year)

glue_df_annual_anoxic_factor_his=glue_df_annual_anoxic_factor_his.sort_index()

glue_df_annual_anoxic_factor_rcp26=glue_df_annual_anoxic_factor_rcp26.sort_index()

glue_df_annual_anoxic_factor_rcp60=glue_df_annual_anoxic_factor_rcp60.sort_index()

glue_df_annual_anoxic_factor_rcp85=glue_df_annual_anoxic_factor_rcp85.sort_index()





#anomaly 

# baseline [1976-2005]
annual_anoxic_factor_ref=glue_df_annual_anoxic_factor_his[1975 < glue_df_annual_anoxic_factor_his.index]['50%'].mean()

#5.410877320721374
#5.914740063212032


#near future [2030-2059] 

glue_df_annual_anoxic_factor_rcp26[(2029 < glue_df_annual_anoxic_factor_rcp26.index) & (glue_df_annual_anoxic_factor_rcp26.index < 2060)]['50%'].mean()
# 7.072947718287684
# 7.950218353351354
glue_df_annual_anoxic_factor_rcp60[(2029 < glue_df_annual_anoxic_factor_rcp60.index) & (glue_df_annual_anoxic_factor_rcp60.index < 2060)]['50%'].mean()
# 7.156265572954701
# 7.139975067233944

glue_df_annual_anoxic_factor_rcp85[(2029 < glue_df_annual_anoxic_factor_rcp85.index) & (glue_df_annual_anoxic_factor_rcp85.index < 2060)]['50%'].mean()
# 7.630745663516447
# 8.223867040126178
 
#Distant future [2070-2099]

glue_df_annual_anoxic_factor_rcp26[(2069 < glue_df_annual_anoxic_factor_rcp26.index) & (glue_df_annual_anoxic_factor_rcp26.index < 2100)]['50%'].mean()
#7.17035474380281
#8.221226628944514


glue_df_annual_anoxic_factor_rcp60[(2069 < glue_df_annual_anoxic_factor_rcp60.index) & (glue_df_annual_anoxic_factor_rcp60.index < 2100)]['50%'].mean()
#8.781804641713899
#8.984771173520228

glue_df_annual_anoxic_factor_rcp85[(2069 < glue_df_annual_anoxic_factor_rcp85.index) & (glue_df_annual_anoxic_factor_rcp85.index < 2100)]['50%'].mean()
#7.630745663516447
# 10.612461480324987



#%%anoxic_factor_anomaly 
os.chdir('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/all_4_models/')

import matplotlib.pyplot as plt

fig =plt.figure(figsize=(15, 10))
ax= plt.subplot(111)


ax=plt.fill_between(glue_df_annual_anoxic_factor_his[1975 < glue_df_annual_anoxic_factor_his.index].index.astype(float),
                      glue_df_annual_anoxic_factor_his[1975 < glue_df_annual_anoxic_factor_his.index]['5%'].astype(float) - annual_anoxic_factor_ref,
                      glue_df_annual_anoxic_factor_his[1975 < glue_df_annual_anoxic_factor_his.index ]['95%'].astype(float) - annual_anoxic_factor_ref,
                      color='grey', alpha=0.2, label='His 90% CI')


ax=plt.plot(glue_df_annual_anoxic_factor_his[(1975 < glue_df_annual_anoxic_factor_his.index) ].index.astype(float),
            glue_df_annual_anoxic_factor_his[(1975 < glue_df_annual_anoxic_factor_his.index)]['50%'].astype(float) - annual_anoxic_factor_ref,
            'k', label='His median', alpha=0.9, linewidth=3   )

ax=plt.fill_between(glue_df_annual_anoxic_factor_rcp26.index.astype(float), glue_df_annual_anoxic_factor_rcp26['5%'].astype(float)-annual_anoxic_factor_ref, glue_df_annual_anoxic_factor_rcp26['95%'].astype(float)-annual_anoxic_factor_ref, color='darkgreen', alpha=0.3 ,  label= 'RCP6.0 90% CI')
ax=plt.plot(glue_df_annual_anoxic_factor_rcp26.index.astype(float), glue_df_annual_anoxic_factor_rcp26['50%'].astype(float)-annual_anoxic_factor_ref, 'darkgreen', label='RCP6.0 median', alpha=0.9, linewidth=3  )
                      
                     
ax=plt.fill_between(glue_df_annual_anoxic_factor_rcp60.index.astype(float), glue_df_annual_anoxic_factor_rcp60['5%'].astype(float)-annual_anoxic_factor_ref, glue_df_annual_anoxic_factor_rcp60['95%'].astype(float)-annual_anoxic_factor_ref, color='b', alpha=0.27 ,  label= 'RCP6.0 90% CI')
ax=plt.plot(glue_df_annual_anoxic_factor_rcp60.index.astype(float), glue_df_annual_anoxic_factor_rcp60['50%'].astype(float)-annual_anoxic_factor_ref, 'b', label='RCP6.0 median', alpha=0.9, linewidth=3  )

ax=plt.fill_between(glue_df_annual_anoxic_factor_rcp85.index.astype(float), glue_df_annual_anoxic_factor_rcp85['5%'].astype(float)-annual_anoxic_factor_ref, glue_df_annual_anoxic_factor_rcp85['95%'].astype(float)-annual_anoxic_factor_ref, color='r', alpha=0.2 ,  label= 'RCP8.5 90% CI')
ax=plt.plot(glue_df_annual_anoxic_factor_rcp85.index.astype(float), glue_df_annual_anoxic_factor_rcp85['50%'].astype(float)-annual_anoxic_factor_ref, 'r', label='RCP8.5 median', alpha=0.9, linewidth=3  )

ax=plt.ylabel('anomaly of anoxic factor [d year$^{-1}$]' , fontsize=26)
ax=plt.xlabel('Year' , fontsize=26)
ax=plt.yticks(fontsize= 22)
ax=plt.xticks(rotation=45 , fontsize=22)
ax=plt.legend(bbox_to_anchor=(0.7, -0.2), fontsize=22)  
fig.savefig("GLUE_Timeseries_anoxic_factor_anomaly_16combinationJaJv_ave_obs_4models_4scenarios.png",  dpi=300, bbox_inches='tight')


