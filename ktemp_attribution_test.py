# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 13:02:18 2023

@author: mahta
"""

#%%rcp26

all_threshold_jday_per_year_rcp26= pd.DataFrame([])
all_C_ave_onset_to_thereshold_rcp26= pd.DataFrame([])
all_temp_ave_onset_to_thereshold_rcp26= pd.DataFrame([])
all_weights_rcp26= np.array([])



#gfdl temp:
os.chdir('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/gfdl_senarios/rcp26')
input_file_path = 'temp_prof_gfdl_rcp26.csv'  # Replace with your actual input file path
temp_deox_gfdl_rcp26 = pd.read_csv(input_file_path)
temp_deox_2D_gfdl_rcp26=temp_deox_gfdl_rcp26.iloc[:, 1:].values





#gfdl DO:
directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/gfdl_senarios/rcp26'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("DO_prof_gfdl_rcp26_Jv_"):
        
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
        
        
        threshold_jday_per_year_rcp26, temp_ave_onset_to_thereshold_rcp26 , C_ave_onset_to_thereshold_rcp26=firstdeephypoxiadate_jday_tempave_DOave (temp_deox_2D_gfdl_rcp26, C, Vr,time_series, threshold=2)
        
        all_threshold_jday_per_year_rcp26= pd.concat([all_threshold_jday_per_year_rcp26 , threshold_jday_per_year_rcp26], axis=1)
        all_temp_ave_onset_to_thereshold_rcp26= pd.concat([all_temp_ave_onset_to_thereshold_rcp26 ,temp_ave_onset_to_thereshold_rcp26], axis=1)
        all_C_ave_onset_to_thereshold_rcp26= pd.concat([all_C_ave_onset_to_thereshold_rcp26 , C_ave_onset_to_thereshold_rcp26], axis=1)









#hadgem temp:
os.chdir('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/hadgem_senarios/rcp26')
input_file_path = 'temp_prof_hadgem_rcp26.csv'  # Replace with your actual input file path
temp_deox_hadgem_rcp26 = pd.read_csv(input_file_path)
temp_deox_2D_hadgem_rcp26=temp_deox_hadgem_rcp26.iloc[:, 1:].values

#hadgem DO:
directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/hadgem_senarios/rcp26'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("DO_prof_hadgem_rcp26_Jv_"):
        
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
        
        
        threshold_jday_per_year_rcp26,  temp_ave_onset_to_thereshold_rcp26 , C_ave_onset_to_thereshold_rcp26=firstdeephypoxiadate_jday_tempave_DOave (temp_deox_2D_hadgem_rcp26, C, Vr,time_series, threshold=2)
        
        all_threshold_jday_per_year_rcp26= pd.concat([all_threshold_jday_per_year_rcp26 , threshold_jday_per_year_rcp26], axis=1)
        all_temp_ave_onset_to_thereshold_rcp26= pd.concat([all_temp_ave_onset_to_thereshold_rcp26 ,temp_ave_onset_to_thereshold_rcp26], axis=1)
        all_C_ave_onset_to_thereshold_rcp26= pd.concat([all_C_ave_onset_to_thereshold_rcp26 , C_ave_onset_to_thereshold_rcp26], axis=1)

 


#ipsl temp:
os.chdir('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/ipsl_senarios/rcp26')
input_file_path = 'temp_prof_ipsl_rcp26.csv'  # Replace with your actual input file path
temp_deox_ipsl_rcp26 = pd.read_csv(input_file_path)
temp_deox_2D_ipsl_rcp26=temp_deox_ipsl_rcp26.iloc[:, 1:].values

#ipsl DO:
directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/ipsl_senarios/rcp26'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("DO_prof_ipsl_rcp26_Jv_"):
        
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
        
        
        threshold_jday_per_year_rcp26,  temp_ave_onset_to_thereshold_rcp26 , C_ave_onset_to_thereshold_rcp26=firstdeephypoxiadate_jday_tempave_DOave (temp_deox_2D_ipsl_rcp26, C, Vr,time_series, threshold=2)
        
        all_threshold_jday_per_year_rcp26= pd.concat([all_threshold_jday_per_year_rcp26 , threshold_jday_per_year_rcp26], axis=1)
        all_temp_ave_onset_to_thereshold_rcp26= pd.concat([all_temp_ave_onset_to_thereshold_rcp26 ,temp_ave_onset_to_thereshold_rcp26], axis=1)
        all_C_ave_onset_to_thereshold_rcp26= pd.concat([all_C_ave_onset_to_thereshold_rcp26 , C_ave_onset_to_thereshold_rcp26], axis=1)



#miroc temp:
os.chdir('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/miroc_senarios/rcp26')
input_file_path = 'temp_prof_miroc_rcp26.csv'  # Replace with your actual input file path
temp_deox_miroc_rcp26 = pd.read_csv(input_file_path)
temp_deox_2D_miroc_rcp26=temp_deox_miroc_rcp26.iloc[:, 1:].values

#miroc DO:
directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/miroc_senarios/rcp26'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("DO_prof_miroc_rcp26_Jv_"):
        
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
        
        
        threshold_jday_per_year_rcp26, temp_ave_onset_to_thereshold_rcp26 , C_ave_onset_to_thereshold_rcp26=firstdeephypoxiadate_jday_tempave_DOave (temp_deox_2D_miroc_rcp26, C, Vr,time_series, threshold=2)
        
        all_threshold_jday_per_year_rcp26= pd.concat([all_threshold_jday_per_year_rcp26 , threshold_jday_per_year_rcp26], axis=1)
        all_temp_ave_onset_to_thereshold_rcp26= pd.concat([all_temp_ave_onset_to_thereshold_rcp26 ,temp_ave_onset_to_thereshold_rcp26], axis=1)
        all_C_ave_onset_to_thereshold_rcp26= pd.concat([all_C_ave_onset_to_thereshold_rcp26 , C_ave_onset_to_thereshold_rcp26], axis=1)

 

#%%rcp60

all_threshold_jday_per_year_rcp60= pd.DataFrame([])
all_C_ave_onset_to_thereshold_rcp60= pd.DataFrame([])
all_temp_ave_onset_to_thereshold_rcp60= pd.DataFrame([])
all_weights_rcp60= np.array([])



#gfdl temp:
os.chdir('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/gfdl_senarios/rcp60')
input_file_path = 'temp_prof_gfdl_rcp60.csv'  # Replace with your actual input file path
temp_deox_gfdl_rcp60 = pd.read_csv(input_file_path)
temp_deox_2D_gfdl_rcp60=temp_deox_gfdl_rcp60.iloc[:, 1:].values





#gfdl DO:
directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/gfdl_senarios/rcp60'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("DO_prof_gfdl_rcp60_Jv_"):
        
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
        
        
        threshold_jday_per_year_rcp60, temp_ave_onset_to_thereshold_rcp60 , C_ave_onset_to_thereshold_rcp60=firstdeephypoxiadate_jday_tempave_DOave (temp_deox_2D_gfdl_rcp60, C, Vr,time_series, threshold=2)
        
        all_threshold_jday_per_year_rcp60= pd.concat([all_threshold_jday_per_year_rcp60 , threshold_jday_per_year_rcp60], axis=1)
        all_temp_ave_onset_to_thereshold_rcp60= pd.concat([all_temp_ave_onset_to_thereshold_rcp60 ,temp_ave_onset_to_thereshold_rcp60], axis=1)
        all_C_ave_onset_to_thereshold_rcp60= pd.concat([all_C_ave_onset_to_thereshold_rcp60 , C_ave_onset_to_thereshold_rcp60], axis=1)









#hadgem temp:
os.chdir('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/hadgem_senarios/rcp60')
input_file_path = 'temp_prof_hadgem_rcp60.csv'  # Replace with your actual input file path
temp_deox_hadgem_rcp60 = pd.read_csv(input_file_path)
temp_deox_2D_hadgem_rcp60=temp_deox_hadgem_rcp60.iloc[:, 1:].values

#hadgem DO:
directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/hadgem_senarios/rcp60'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("DO_prof_hadgem_rcp60_Jv_"):
        
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
        
        
        threshold_jday_per_year_rcp60,  temp_ave_onset_to_thereshold_rcp60 , C_ave_onset_to_thereshold_rcp60=firstdeephypoxiadate_jday_tempave_DOave (temp_deox_2D_hadgem_rcp60, C, Vr,time_series, threshold=2)
        
        all_threshold_jday_per_year_rcp60= pd.concat([all_threshold_jday_per_year_rcp60 , threshold_jday_per_year_rcp60], axis=1)
        all_temp_ave_onset_to_thereshold_rcp60= pd.concat([all_temp_ave_onset_to_thereshold_rcp60 ,temp_ave_onset_to_thereshold_rcp60], axis=1)
        all_C_ave_onset_to_thereshold_rcp60= pd.concat([all_C_ave_onset_to_thereshold_rcp60 , C_ave_onset_to_thereshold_rcp60], axis=1)

 


#ipsl temp:
os.chdir('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/ipsl_senarios/rcp60')
input_file_path = 'temp_prof_ipsl_rcp60.csv'  # Replace with your actual input file path
temp_deox_ipsl_rcp60 = pd.read_csv(input_file_path)
temp_deox_2D_ipsl_rcp60=temp_deox_ipsl_rcp60.iloc[:, 1:].values

#ipsl DO:
directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/ipsl_senarios/rcp60'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("DO_prof_ipsl_rcp60_Jv_"):
        
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
        
        
        threshold_jday_per_year_rcp60,  temp_ave_onset_to_thereshold_rcp60 , C_ave_onset_to_thereshold_rcp60=firstdeephypoxiadate_jday_tempave_DOave (temp_deox_2D_ipsl_rcp60, C, Vr,time_series, threshold=2)
        
        all_threshold_jday_per_year_rcp60= pd.concat([all_threshold_jday_per_year_rcp60 , threshold_jday_per_year_rcp60], axis=1)
        all_temp_ave_onset_to_thereshold_rcp60= pd.concat([all_temp_ave_onset_to_thereshold_rcp60 ,temp_ave_onset_to_thereshold_rcp60], axis=1)
        all_C_ave_onset_to_thereshold_rcp60= pd.concat([all_C_ave_onset_to_thereshold_rcp60 , C_ave_onset_to_thereshold_rcp60], axis=1)



#miroc temp:
os.chdir('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/miroc_senarios/rcp60')
input_file_path = 'temp_prof_miroc_rcp60.csv'  # Replace with your actual input file path
temp_deox_miroc_rcp60 = pd.read_csv(input_file_path)
temp_deox_2D_miroc_rcp60=temp_deox_miroc_rcp60.iloc[:, 1:].values

#miroc DO:
directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/miroc_senarios/rcp60'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("DO_prof_miroc_rcp60_Jv_"):
        
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
        
        
        threshold_jday_per_year_rcp60, temp_ave_onset_to_thereshold_rcp60 , C_ave_onset_to_thereshold_rcp60=firstdeephypoxiadate_jday_tempave_DOave (temp_deox_2D_miroc_rcp60, C, Vr,time_series, threshold=2)
        
        all_threshold_jday_per_year_rcp60= pd.concat([all_threshold_jday_per_year_rcp60 , threshold_jday_per_year_rcp60], axis=1)
        all_temp_ave_onset_to_thereshold_rcp60= pd.concat([all_temp_ave_onset_to_thereshold_rcp60 ,temp_ave_onset_to_thereshold_rcp60], axis=1)
        all_C_ave_onset_to_thereshold_rcp60= pd.concat([all_C_ave_onset_to_thereshold_rcp60 , C_ave_onset_to_thereshold_rcp60], axis=1)

 
#%%rcp85

all_threshold_jday_per_year_rcp85= pd.DataFrame([])
all_C_ave_onset_to_thereshold_rcp85= pd.DataFrame([])
all_temp_ave_onset_to_thereshold_rcp85= pd.DataFrame([])
all_weights_rcp85= np.array([])



#gfdl temp:
os.chdir('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/gfdl_senarios/rcp85')
input_file_path = 'temp_prof_gfdl_rcp85.csv'  # Replace with your actual input file path
temp_deox_gfdl_rcp85 = pd.read_csv(input_file_path)
temp_deox_2D_gfdl_rcp85=temp_deox_gfdl_rcp85.iloc[:, 1:].values





#gfdl DO:
directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/gfdl_senarios/rcp85'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("DO_prof_gfdl_rcp85_Jv_"):
        
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
        
        
        threshold_jday_per_year_rcp85, temp_ave_onset_to_thereshold_rcp85 , C_ave_onset_to_thereshold_rcp85=firstdeephypoxiadate_jday_tempave_DOave (temp_deox_2D_gfdl_rcp85, C, Vr,time_series, threshold=2)
        
        all_threshold_jday_per_year_rcp85= pd.concat([all_threshold_jday_per_year_rcp85 , threshold_jday_per_year_rcp85], axis=1)
        all_temp_ave_onset_to_thereshold_rcp85= pd.concat([all_temp_ave_onset_to_thereshold_rcp85 ,temp_ave_onset_to_thereshold_rcp85], axis=1)
        all_C_ave_onset_to_thereshold_rcp85= pd.concat([all_C_ave_onset_to_thereshold_rcp85 , C_ave_onset_to_thereshold_rcp85], axis=1)









#hadgem temp:
os.chdir('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/hadgem_senarios/rcp85')
input_file_path = 'temp_prof_hadgem_rcp85.csv'  # Replace with your actual input file path
temp_deox_hadgem_rcp85 = pd.read_csv(input_file_path)
temp_deox_2D_hadgem_rcp85=temp_deox_hadgem_rcp85.iloc[:, 1:].values

#hadgem DO:
directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/hadgem_senarios/rcp85'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("DO_prof_hadgem_rcp85_Jv_"):
        
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
        
        
        threshold_jday_per_year_rcp85,  temp_ave_onset_to_thereshold_rcp85 , C_ave_onset_to_thereshold_rcp85=firstdeephypoxiadate_jday_tempave_DOave (temp_deox_2D_hadgem_rcp85, C, Vr,time_series, threshold=2)
        
        all_threshold_jday_per_year_rcp85= pd.concat([all_threshold_jday_per_year_rcp85 , threshold_jday_per_year_rcp85], axis=1)
        all_temp_ave_onset_to_thereshold_rcp85= pd.concat([all_temp_ave_onset_to_thereshold_rcp85 ,temp_ave_onset_to_thereshold_rcp85], axis=1)
        all_C_ave_onset_to_thereshold_rcp85= pd.concat([all_C_ave_onset_to_thereshold_rcp85 , C_ave_onset_to_thereshold_rcp85], axis=1)

 


#ipsl temp:
os.chdir('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/ipsl_senarios/rcp85')
input_file_path = 'temp_prof_ipsl_rcp85.csv'  # Replace with your actual input file path
temp_deox_ipsl_rcp85 = pd.read_csv(input_file_path)
temp_deox_2D_ipsl_rcp85=temp_deox_ipsl_rcp85.iloc[:, 1:].values

#ipsl DO:
directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/ipsl_senarios/rcp85'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("DO_prof_ipsl_rcp85_Jv_"):
        
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
        
        
        threshold_jday_per_year_rcp85,  temp_ave_onset_to_thereshold_rcp85 , C_ave_onset_to_thereshold_rcp85=firstdeephypoxiadate_jday_tempave_DOave (temp_deox_2D_ipsl_rcp85, C, Vr,time_series, threshold=2)
        
        all_threshold_jday_per_year_rcp85= pd.concat([all_threshold_jday_per_year_rcp85 , threshold_jday_per_year_rcp85], axis=1)
        all_temp_ave_onset_to_thereshold_rcp85= pd.concat([all_temp_ave_onset_to_thereshold_rcp85 ,temp_ave_onset_to_thereshold_rcp85], axis=1)
        all_C_ave_onset_to_thereshold_rcp85= pd.concat([all_C_ave_onset_to_thereshold_rcp85 , C_ave_onset_to_thereshold_rcp85], axis=1)



#miroc temp:
os.chdir('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/miroc_senarios/rcp85')
input_file_path = 'temp_prof_miroc_rcp85.csv'  # Replace with your actual input file path
temp_deox_miroc_rcp85 = pd.read_csv(input_file_path)
temp_deox_2D_miroc_rcp85=temp_deox_miroc_rcp85.iloc[:, 1:].values

#miroc DO:
directory = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/miroc_senarios/rcp85'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("DO_prof_miroc_rcp85_Jv_"):
        
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
        
        
        threshold_jday_per_year_rcp85, temp_ave_onset_to_thereshold_rcp85 , C_ave_onset_to_thereshold_rcp85=firstdeephypoxiadate_jday_tempave_DOave (temp_deox_2D_miroc_rcp85, C, Vr,time_series, threshold=2)
        
        all_threshold_jday_per_year_rcp85= pd.concat([all_threshold_jday_per_year_rcp85 , threshold_jday_per_year_rcp85], axis=1)
        all_temp_ave_onset_to_thereshold_rcp85= pd.concat([all_temp_ave_onset_to_thereshold_rcp85 ,temp_ave_onset_to_thereshold_rcp85], axis=1)
        all_C_ave_onset_to_thereshold_rcp85= pd.concat([all_C_ave_onset_to_thereshold_rcp85 , C_ave_onset_to_thereshold_rcp85], axis=1)

 
#%%#
#=====================================GLUE ============================


#%%rcp26

#threshold_jday_per
timeseries_year_rcp26= all_threshold_jday_per_year_rcp26.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_threshold_jday_per_year_rcp26.iterrows():# for each years
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights_rcp26))

# Build glue df
glue_threshold_jday_per_year_rcp26 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_threshold_jday_per_year_rcp26=glue_threshold_jday_per_year_rcp26.set_index(timeseries_year_rcp26)    


#temp_ave_onset_to_thereshold
timeseries_year_rcp26= all_temp_ave_onset_to_thereshold_rcp26.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_temp_ave_onset_to_thereshold_rcp26.iterrows():# for each years
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights_rcp26))

# Build glue df
glue_temp_ave_onset_to_thereshold_rcp26 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_temp_ave_onset_to_thereshold_rcp26=glue_temp_ave_onset_to_thereshold_rcp26.set_index(timeseries_year_rcp26)    



#C_ave_onset_to_thereshold
timeseries_year_rcp26= all_C_ave_onset_to_thereshold_rcp26.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_C_ave_onset_to_thereshold_rcp26.iterrows():# for each years
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights_rcp26))

# Build glue df
glue_C_ave_onset_to_thereshold_rcp26 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_C_ave_onset_to_thereshold_rcp26=glue_C_ave_onset_to_thereshold_rcp26.set_index(timeseries_year_rcp26)    


#%%rcp60

#threshold_jday_per
timeseries_year_rcp60= all_threshold_jday_per_year_rcp60.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_threshold_jday_per_year_rcp60.iterrows():# for each years
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights_rcp26))

# Build glue df
glue_threshold_jday_per_year_rcp60 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_threshold_jday_per_year_rcp60=glue_threshold_jday_per_year_rcp60.set_index(timeseries_year_rcp60)    


#temp_ave_onset_to_thereshold
timeseries_year_rcp60= all_temp_ave_onset_to_thereshold_rcp60.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_temp_ave_onset_to_thereshold_rcp60.iterrows():# for each years
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights_rcp26))

# Build glue df
glue_temp_ave_onset_to_thereshold_rcp60 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_temp_ave_onset_to_thereshold_rcp60=glue_temp_ave_onset_to_thereshold_rcp60.set_index(timeseries_year_rcp60)    



#C_ave_onset_to_thereshold
timeseries_year_rcp60= all_C_ave_onset_to_thereshold_rcp60.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_C_ave_onset_to_thereshold_rcp60.iterrows():# for each years
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights_rcp26))

# Build glue df
glue_C_ave_onset_to_thereshold_rcp60 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_C_ave_onset_to_thereshold_rcp60=glue_C_ave_onset_to_thereshold_rcp60.set_index(timeseries_year_rcp60)    


#%%rcp85

#threshold_jday_per
timeseries_year_rcp85= all_threshold_jday_per_year_rcp85.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_threshold_jday_per_year_rcp85.iterrows():# for each years
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights_rcp26))

# Build glue df
glue_threshold_jday_per_year_rcp85 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_threshold_jday_per_year_rcp85=glue_threshold_jday_per_year_rcp85.set_index(timeseries_year_rcp85)    


#temp_ave_onset_to_thereshold
timeseries_year_rcp85= all_temp_ave_onset_to_thereshold_rcp85.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_temp_ave_onset_to_thereshold_rcp85.iterrows():# for each years
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights_rcp26))

# Build glue df
glue_temp_ave_onset_to_thereshold_rcp85 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_temp_ave_onset_to_thereshold_rcp85=glue_temp_ave_onset_to_thereshold_rcp85.set_index(timeseries_year_rcp85)    



#C_ave_onset_to_thereshold
timeseries_year_rcp85= all_C_ave_onset_to_thereshold_rcp85.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_C_ave_onset_to_thereshold_rcp85.iterrows():# for each years
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights_rcp26))

# Build glue df
glue_C_ave_onset_to_thereshold_rcp85 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_C_ave_onset_to_thereshold_rcp85=glue_C_ave_onset_to_thereshold_rcp85.set_index(timeseries_year_rcp85)    




#%%Sorting the glue dataframe according to the index (year)

#threshold_jday

glue_threshold_jday_per_year_rcp26=glue_threshold_jday_per_year_rcp26.sort_index()

glue_threshold_jday_per_year_rcp60=glue_threshold_jday_per_year_rcp60.sort_index()

glue_threshold_jday_per_year_rcp85=glue_threshold_jday_per_year_rcp85.sort_index()


#temp_ave

glue_temp_ave_onset_to_thereshold_rcp26=glue_temp_ave_onset_to_thereshold_rcp26.sort_index()

glue_temp_ave_onset_to_thereshold_rcp60=glue_temp_ave_onset_to_thereshold_rcp60.sort_index()

glue_temp_ave_onset_to_thereshold_rcp85=glue_temp_ave_onset_to_thereshold_rcp85.sort_index()

#C_ave

glue_C_ave_onset_to_thereshold_rcp26=glue_C_ave_onset_to_thereshold_rcp26.sort_index()

glue_C_ave_onset_to_thereshold_rcp60=glue_C_ave_onset_to_thereshold_rcp60.sort_index()

glue_C_ave_onset_to_thereshold_rcp85=glue_C_ave_onset_to_thereshold_rcp85.sort_index()





#%% MK test on onset Jday 80 years 

# temp_ave_onset_to_hypoxia


glue_temp_ave_onset_to_thereshold_80years_rcp26=glue_temp_ave_onset_to_thereshold_rcp26[glue_temp_ave_onset_to_thereshold_rcp26.index>2019]

#rcp26
autocorr_MK_org_modif_sens_slope_test(glue_temp_ave_onset_to_thereshold_80years_rcp26['50%'])
(0.012377387234765511,
 'positively autocorrelated',
 'no trend',
 0.8786171564372027,
 0,
 0)

glue_temp_ave_onset_to_thereshold_80years_rcp60=glue_temp_ave_onset_to_thereshold_rcp60[glue_temp_ave_onset_to_thereshold_rcp60.index>2019]

#rcp60
autocorr_MK_org_modif_sens_slope_test(glue_temp_ave_onset_to_thereshold_80years_rcp60['50%'])

(0.0089057009631192,
 'positively autocorrelated',
 'no trend',
 0.4166916764135762,
 0,
 0)


glue_temp_ave_onset_to_thereshold_80years_rcp85=glue_temp_ave_onset_to_thereshold_rcp85[glue_temp_ave_onset_to_thereshold_rcp85.index>2019]

#rcp85
autocorr_MK_org_modif_sens_slope_test(glue_temp_ave_onset_to_thereshold_80years_rcp85['50%'])

(0.01259470105149551,
 'positively autocorrelated',
 'no trend',
 0.059827587933114934,
 0,
 0)

#%%looking for trend in C_ave from onset to hypoxia in 80 years


glue_C_ave_onset_to_thereshold_80years_rcp26=glue_C_ave_onset_to_thereshold_rcp26[glue_C_ave_onset_to_thereshold_rcp26.index>2019]

#rcp26
autocorr_MK_org_modif_sens_slope_test(glue_C_ave_onset_to_thereshold_80years_rcp26['50%'])
(0.0033517361193248873,
 'positively autocorrelated',
 'no trend',
 0.5151243797588594,
 0,
 0)
glue_C_ave_onset_to_thereshold_80years_rcp60=glue_C_ave_onset_to_thereshold_rcp60[glue_C_ave_onset_to_thereshold_rcp60.index>2019]

#rcp60
autocorr_MK_org_modif_sens_slope_test(glue_C_ave_onset_to_thereshold_80years_rcp60['50%'])

(0.0017000030162981075,
 'positively autocorrelated',
 'no trend',
 0.5740732320346693,
 0,
 0)

glue_C_ave_onset_to_thereshold_80years_rcp85=glue_C_ave_onset_to_thereshold_rcp85[glue_C_ave_onset_to_thereshold_rcp85.index>2019]

#rcp85
autocorr_MK_org_modif_sens_slope_test(glue_C_ave_onset_to_thereshold_80years_rcp85['50%'])

(0.002682659561271449,
 'positively autocorrelated',
 'no trend',
 0.5281635210122875,
 0,
 0)



#%%Plotiing%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

#%%########original test with variable theta:
os.chdir('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/all_4_models/alltogther/')


import matplotlib.pyplot as plt

fig =plt.figure(figsize=(15, 10))
ax= plt.subplot(111)
#plt.fill_between(time_series, glue_df['2.5%'], glue_df['97.5%'], color='r', alpha=0.4)
#plt.plot(time_series, glue_df['50%'], 'r-', label='Estimated')


####ax=plt.fill_between(glue_df_hypolimnetic_ave_his[1975 <glue_df_hypolimnetic_ave_his.index].index, glue_df_hypolimnetic_ave_his[1975 <glue_df_hypolimnetic_ave_his.index]['5%'], glue_df_hypolimnetic_ave_his[1975 <glue_df_hypolimnetic_ave_his.index]['95%'], color='grey', alpha=0.4 ,  label= 'His 90% CI')
####ax=plt.plot(glue_df_hypolimnetic_ave_his[1975 <glue_df_hypolimnetic_ave_his.index].index, glue_df_hypolimnetic_ave_his[1975 <glue_df_hypolimnetic_ave_his.index]['50%'], 'grey', label='His median', alpha=1, linewidth=3 )



ax=plt.fill_between(glue_temp_ave_onset_to_thereshold_80years_rcp26.index, glue_temp_ave_onset_to_thereshold_80years_rcp26['5%'], glue_temp_ave_onset_to_thereshold_80years_rcp26['95%'], color='green', alpha=0.4,  label= 'RCP2.6 90% CI')
ax=plt.plot(glue_temp_ave_onset_to_thereshold_80years_rcp26.index, glue_temp_ave_onset_to_thereshold_80years_rcp26['50%'], 'green', label='RCP2.6 median', alpha=1, linewidth=3 )
trendline_rcp26=autocorr_MK_org_modif_sens_slope_test(glue_temp_ave_onset_to_thereshold_80years_rcp26['50%'])
#ax=plt.plot(glue_temp_ave_onset_to_thereshold_80years_rcp26.index,trendline_rcp26[-2]*(np.arange(1,81))+trendline_rcp26[-1] ,color='green',  linestyle='--')
#ax=plt.text(2065, 9, f'y = {trendline_rcp26[-2]:.3f}x + {trendline_rcp26[-1]:.3f}, p < 0.05', color='green', fontsize= 20 )


ax=plt.fill_between(glue_temp_ave_onset_to_thereshold_80years_rcp60.index, glue_temp_ave_onset_to_thereshold_80years_rcp60['5%'], glue_temp_ave_onset_to_thereshold_80years_rcp60['95%'], color='yellow', alpha=0.4 ,  label= 'RCP6.0 90% CI')
ax=plt.plot(glue_temp_ave_onset_to_thereshold_80years_rcp60.index, glue_temp_ave_onset_to_thereshold_80years_rcp60['50%'], 'yellow', label='RCP6.0 median',alpha=1, linewidth=3 )
trendline_rcp60=autocorr_MK_org_modif_sens_slope_test(glue_temp_ave_onset_to_thereshold_80years_rcp60['50%'])
#ax=plt.plot(glue_temp_ave_onset_to_thereshold_80years_rcp60.index,trendline_rcp60[-2]*(np.arange(1,81))+trendline_rcp60[-1] ,color='gold',  linestyle='--')
#ax=plt.text(2065, 9, f'y = {trendline_rcp60[-2]:.3f}x + {trendline_rcp60[-1]:.3f}, p < 0.05', color='gold', fontsize= 20 )



ax=plt.fill_between(glue_temp_ave_onset_to_thereshold_80years_rcp85.index, glue_temp_ave_onset_to_thereshold_80years_rcp85['5%'], glue_temp_ave_onset_to_thereshold_80years_rcp85['95%'], color='r', alpha=0.4 ,  label= 'RCP8.5 90% CI')
ax=plt.plot(glue_temp_ave_onset_to_thereshold_80years_rcp85.index, glue_temp_ave_onset_to_thereshold_80years_rcp85['50%'], 'r', label='RCP8.5 median', alpha=0.9, linewidth=3 )
trendline_rcp85=autocorr_MK_org_modif_sens_slope_test(glue_temp_ave_onset_to_thereshold_80years_rcp85['50%'])
#ax=plt.plot(glue_temp_ave_onset_to_thereshold_80years_rcp85.index,trendline_rcp85[-2]*(np.arange(1,81))+trendline_rcp85[-1] ,color='r',  linestyle='--')
#ax=plt.text(2065, 9.5, f'y = {trendline_rcp85[-2]:.3f}x + {trendline_rcp85[-1]:.3f}, p < 0.05', color='r', fontsize= 20 )



ax=plt.ylabel('Hypolimnetic temperature average \nduring deoxygen periods before hypoxia [°C]' , fontsize=26)
ax=plt.xlabel('Year' , fontsize=26)
ax=plt.yticks(np.arange(6, 15, 1) , fontsize= 22)
ax=plt.xticks(rotation=45 , fontsize=22)
ax=plt.legend(bbox_to_anchor=(1, -0.15), fontsize=22, ncol=3)

#########original test with variable theta:   
fig.savefig("GLUE_Timeseries_hypolimnetic_temp_onset_to_hypoxia_4models_80years_4scenarios.png", dpi=300, bbox_inches='tight')


#%%ktemp trendline

def Theta_j(temp):
    theta = 1.087
    return (theta ** (temp - 20))


glue_ktemp_80years_rcp26=glue_temp_ave_onset_to_thereshold_80years_rcp26.apply(Theta_j)
#rcp26
autocorr_MK_org_modif_sens_slope_test(glue_ktemp_80years_rcp26['50%'])
(0.006182193492235227,
 'positively autocorrelated',
 'no trend',
 0.8786562689184152,
 0,
 0)

glue_ktemp_80years_rcp60=glue_temp_ave_onset_to_thereshold_80years_rcp60.apply(Theta_j)
#rcp60
autocorr_MK_org_modif_sens_slope_test(glue_ktemp_80years_rcp60['50%'])
(0.004195356905849891,
 'positively autocorrelated',
 'no trend',
 0.4175717268078629,
 0,
 0)

glue_ktemp_80years_rcp85=glue_temp_ave_onset_to_thereshold_80years_rcp85.apply(Theta_j)

#rcp85
autocorr_MK_org_modif_sens_slope_test(glue_ktemp_80years_rcp85['50%'])
(0.006330210959738526,
 'positively autocorrelated',
 'no trend',
 0.059827587933114934,
 0,
 0)
#%%########original test with variable theta:
os.chdir('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/all_4_models/alltogther/')


import matplotlib.pyplot as plt

fig =plt.figure(figsize=(15, 10))
ax= plt.subplot(111)
#plt.fill_between(time_series, glue_df['2.5%'], glue_df['97.5%'], color='r', alpha=0.4)
#plt.plot(time_series, glue_df['50%'], 'r-', label='Estimated')


####ax=plt.fill_between(glue_df_hypolimnetic_ave_his[1975 <glue_df_hypolimnetic_ave_his.index].index, glue_df_hypolimnetic_ave_his[1975 <glue_df_hypolimnetic_ave_his.index]['5%'], glue_df_hypolimnetic_ave_his[1975 <glue_df_hypolimnetic_ave_his.index]['95%'], color='grey', alpha=0.4 ,  label= 'His 90% CI')
####ax=plt.plot(glue_df_hypolimnetic_ave_his[1975 <glue_df_hypolimnetic_ave_his.index].index, glue_df_hypolimnetic_ave_his[1975 <glue_df_hypolimnetic_ave_his.index]['50%'], 'grey', label='His median', alpha=1, linewidth=3 )



ax=plt.fill_between(glue_ktemp_80years_rcp26.index, glue_ktemp_80years_rcp26['5%'], glue_ktemp_80years_rcp26['95%'], color='green', alpha=0.4,  label= 'RCP2.6 90% CI')
ax=plt.plot(glue_ktemp_80years_rcp26.index, glue_ktemp_80years_rcp26['50%'], 'green', label='RCP2.6 median', alpha=1, linewidth=3 )
trendline_rcp26=autocorr_MK_org_modif_sens_slope_test(glue_ktemp_80years_rcp26['50%'])
#ax=plt.plot(glue_ktemp_80years_rcp26.index,trendline_rcp26[-2]*(np.arange(1,81))+trendline_rcp26[-1] ,color='green',  linestyle='--')
#ax=plt.text(2065, 9, f'y = {trendline_rcp26[-2]:.3f}x + {trendline_rcp26[-1]:.3f}, p < 0.05', color='green', fontsize= 20 )


ax=plt.fill_between(glue_ktemp_80years_rcp60.index, glue_ktemp_80years_rcp60['5%'], glue_ktemp_80years_rcp60['95%'], color='yellow', alpha=0.4 ,  label= 'RCP6.0 90% CI')
ax=plt.plot(glue_ktemp_80years_rcp26.index, glue_ktemp_80years_rcp60['50%'], 'yellow', label='RCP6.0 median',alpha=1, linewidth=3 )
trendline_rcp60=autocorr_MK_org_modif_sens_slope_test(glue_ktemp_80years_rcp60['50%'])
#ax=plt.plot(glue_ktemp_80years_rcp60.index,trendline_rcp60[-2]*(np.arange(1,81))+trendline_rcp60[-1] ,color='gold',  linestyle='--')
#ax=plt.text(2065, 9, f'y = {trendline_rcp60[-2]:.3f}x + {trendline_rcp60[-1]:.3f}, p < 0.05', color='gold', fontsize= 20 )



ax=plt.fill_between(glue_ktemp_80years_rcp85.index, glue_ktemp_80years_rcp85['5%'], glue_ktemp_80years_rcp85['95%'], color='r', alpha=0.3 ,  label= 'RCP8.5 90% CI')
ax=plt.plot(glue_ktemp_80years_rcp85.index, glue_ktemp_80years_rcp85['50%'], 'r', label='RCP8.5 median', alpha=0.9, linewidth=3 )
trendline_rcp85=autocorr_MK_org_modif_sens_slope_test(glue_ktemp_80years_rcp85['50%'])
#ax=plt.plot(glue_ktemp_80years_rcp85.index,glue_ktemp_80years_rcp85[-2]*(np.arange(1,81))+trendline_rcp85[-1] ,color='r',  linestyle='--')
#ax=plt.text(2065, 9.5, f'y = {trendline_rcp85[-2]:.3f}x + {trendline_rcp85[-1]:.3f}, p < 0.05', color='r', fontsize= 20 )



ax=plt.ylabel('Temperature modifier average \nduring deoxygen periods before hypoxia []' , fontsize=26)
ax=plt.xlabel('Year' , fontsize=26)
ax=plt.yticks(np.arange(0.3, 0.7 , 0.1) , fontsize= 22)
ax=plt.xticks(rotation=45 , fontsize=22)
ax=plt.legend(bbox_to_anchor=(0.95, -0.15), fontsize=22 , ncol=3)

#########original test with variable theta:   
fig.savefig("GLUE_temp_modifier_hypolimnetic_temp_onset_to_hypoxia_4models_80years_4scenarios.png", dpi=300, bbox_inches='tight')




#%%



