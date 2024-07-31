# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 09:51:59 2024

@author: mahta
"""

#%% monthly hypolimnetic_ave_his
all_weights= np.array([])
all_monthly_do_his_0=pd.DataFrame([])
all_monthly_do_his_1=pd.DataFrame([])
all_monthly_do_his_2=pd.DataFrame([])
all_monthly_do_his_3=pd.DataFrame([])
all_monthly_do_his_4=pd.DataFrame([])
all_monthly_do_his_5=pd.DataFrame([])
all_monthly_do_his_6=pd.DataFrame([])
all_monthly_do_his_7=pd.DataFrame([])
all_monthly_do_his_8=pd.DataFrame([])
all_monthly_do_his_9=pd.DataFrame([])
all_monthly_do_his_10=pd.DataFrame([])
all_monthly_do_his_11=pd.DataFrame([])
#gfdl

# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/his'

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
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the monthly_hypolimnetic_ave function
        result = monthly_hypolimnetic_ave(C, Vr, time_series )

        
        all_monthly_do_his_0 = pd.concat([all_monthly_do_his_0 , result.iloc[:, 0]], axis=1)
        all_monthly_do_his_1 = pd.concat([all_monthly_do_his_1 , result.iloc[:, 1]], axis=1)
        all_monthly_do_his_2 = pd.concat([all_monthly_do_his_2 , result.iloc[:, 2]], axis=1)
        all_monthly_do_his_3 = pd.concat([all_monthly_do_his_3 , result.iloc[:, 3]], axis=1)
        all_monthly_do_his_4 = pd.concat([all_monthly_do_his_4 , result.iloc[:, 4]], axis=1)
        all_monthly_do_his_5 = pd.concat([all_monthly_do_his_5 , result.iloc[:, 5]], axis=1)
        all_monthly_do_his_6 = pd.concat([all_monthly_do_his_6 , result.iloc[:, 6]], axis=1)
        all_monthly_do_his_7 = pd.concat([all_monthly_do_his_7 , result.iloc[:, 7]], axis=1)
        all_monthly_do_his_8 = pd.concat([all_monthly_do_his_8 , result.iloc[:, 8]], axis=1)
        all_monthly_do_his_9 = pd.concat([all_monthly_do_his_9 , result.iloc[:, 9]], axis=1)
        all_monthly_do_his_10 = pd.concat([all_monthly_do_his_10 , result.iloc[:, 10]], axis=1)
        all_monthly_do_his_11 = pd.concat([all_monthly_do_his_11 , result.iloc[:, 11]], axis=1)



        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_hypolimnetic_ave_gfdl_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, header=['monthly_hypolimnetic_ave'])
        
#hadgem               
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
        
        all_weights= np.append(all_weights , weights) 
        
        
        
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the monthly_hypolimnetic_ave function
        result = monthly_hypolimnetic_ave(C, Vr, time_series )

        
        all_monthly_do_his_0 = pd.concat([all_monthly_do_his_0 , result.iloc[:, 0]], axis=1)
        all_monthly_do_his_1 = pd.concat([all_monthly_do_his_1 , result.iloc[:, 1]], axis=1)
        all_monthly_do_his_2 = pd.concat([all_monthly_do_his_2 , result.iloc[:, 2]], axis=1)
        all_monthly_do_his_3 = pd.concat([all_monthly_do_his_3 , result.iloc[:, 3]], axis=1)
        all_monthly_do_his_4 = pd.concat([all_monthly_do_his_4 , result.iloc[:, 4]], axis=1)
        all_monthly_do_his_5 = pd.concat([all_monthly_do_his_5 , result.iloc[:, 5]], axis=1)
        all_monthly_do_his_6 = pd.concat([all_monthly_do_his_6 , result.iloc[:, 6]], axis=1)
        all_monthly_do_his_7 = pd.concat([all_monthly_do_his_7 , result.iloc[:, 7]], axis=1)
        all_monthly_do_his_8 = pd.concat([all_monthly_do_his_8 , result.iloc[:, 8]], axis=1)
        all_monthly_do_his_9 = pd.concat([all_monthly_do_his_9 , result.iloc[:, 9]], axis=1)
        all_monthly_do_his_10 = pd.concat([all_monthly_do_his_10 , result.iloc[:, 10]], axis=1)
        all_monthly_do_his_11 = pd.concat([all_monthly_do_his_11 , result.iloc[:, 11]], axis=1)



        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_hypolimnetic_ave_hadgem_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, header=['monthly_hypolimnetic_ave'])
      
#ipsl       
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
        
        all_weights= np.append(all_weights , weights) 
        
        
        
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the monthly_hypolimnetic_ave function
        result = monthly_hypolimnetic_ave(C, Vr, time_series )

        
        all_monthly_do_his_0 = pd.concat([all_monthly_do_his_0 , result.iloc[:, 0]], axis=1)
        all_monthly_do_his_1 = pd.concat([all_monthly_do_his_1 , result.iloc[:, 1]], axis=1)
        all_monthly_do_his_2 = pd.concat([all_monthly_do_his_2 , result.iloc[:, 2]], axis=1)
        all_monthly_do_his_3 = pd.concat([all_monthly_do_his_3 , result.iloc[:, 3]], axis=1)
        all_monthly_do_his_4 = pd.concat([all_monthly_do_his_4 , result.iloc[:, 4]], axis=1)
        all_monthly_do_his_5 = pd.concat([all_monthly_do_his_5 , result.iloc[:, 5]], axis=1)
        all_monthly_do_his_6 = pd.concat([all_monthly_do_his_6 , result.iloc[:, 6]], axis=1)
        all_monthly_do_his_7 = pd.concat([all_monthly_do_his_7 , result.iloc[:, 7]], axis=1)
        all_monthly_do_his_8 = pd.concat([all_monthly_do_his_8 , result.iloc[:, 8]], axis=1)
        all_monthly_do_his_9 = pd.concat([all_monthly_do_his_9 , result.iloc[:, 9]], axis=1)
        all_monthly_do_his_10 = pd.concat([all_monthly_do_his_10 , result.iloc[:, 10]], axis=1)
        all_monthly_do_his_11 = pd.concat([all_monthly_do_his_11 , result.iloc[:, 11]], axis=1)



        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_hypolimnetic_ave_ipsl_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, header=['monthly_hypolimnetic_ave'])
        

#miroc       
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
        
        all_weights= np.append(all_weights , weights) 
        
        
        
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the monthly_hypolimnetic_ave function
        result = monthly_hypolimnetic_ave(C, Vr, time_series )

        
        all_monthly_do_his_0 = pd.concat([all_monthly_do_his_0 , result.iloc[:, 0]], axis=1)
        all_monthly_do_his_1 = pd.concat([all_monthly_do_his_1 , result.iloc[:, 1]], axis=1)
        all_monthly_do_his_2 = pd.concat([all_monthly_do_his_2 , result.iloc[:, 2]], axis=1)
        all_monthly_do_his_3 = pd.concat([all_monthly_do_his_3 , result.iloc[:, 3]], axis=1)
        all_monthly_do_his_4 = pd.concat([all_monthly_do_his_4 , result.iloc[:, 4]], axis=1)
        all_monthly_do_his_5 = pd.concat([all_monthly_do_his_5 , result.iloc[:, 5]], axis=1)
        all_monthly_do_his_6 = pd.concat([all_monthly_do_his_6 , result.iloc[:, 6]], axis=1)
        all_monthly_do_his_7 = pd.concat([all_monthly_do_his_7 , result.iloc[:, 7]], axis=1)
        all_monthly_do_his_8 = pd.concat([all_monthly_do_his_8 , result.iloc[:, 8]], axis=1)
        all_monthly_do_his_9 = pd.concat([all_monthly_do_his_9 , result.iloc[:, 9]], axis=1)
        all_monthly_do_his_10 = pd.concat([all_monthly_do_his_10 , result.iloc[:, 10]], axis=1)
        all_monthly_do_his_11 = pd.concat([all_monthly_do_his_11 , result.iloc[:, 11]], axis=1)



        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_hypolimnetic_ave_miroc_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, header=['monthly_hypolimnetic_ave'])
        



#%%

all_monthly_do_his_0 = all_monthly_do_his_0.rename_axis('Datetime')
all_monthly_do_his_1 = all_monthly_do_his_1.rename_axis('Datetime')
all_monthly_do_his_2 = all_monthly_do_his_2.rename_axis('Datetime')
all_monthly_do_his_3 = all_monthly_do_his_3.rename_axis('Datetime')
all_monthly_do_his_4 = all_monthly_do_his_4.rename_axis('Datetime')
all_monthly_do_his_5 = all_monthly_do_his_5.rename_axis('Datetime')
all_monthly_do_his_6 = all_monthly_do_his_6.rename_axis('Datetime')
all_monthly_do_his_7 = all_monthly_do_his_7.rename_axis('Datetime')
all_monthly_do_his_8 = all_monthly_do_his_8.rename_axis('Datetime')
all_monthly_do_his_9 = all_monthly_do_his_9.rename_axis('Datetime')
all_monthly_do_his_10 = all_monthly_do_his_10.rename_axis('Datetime')
all_monthly_do_his_11 = all_monthly_do_his_11.rename_axis('Datetime')

#%%Uncertainity partitioning on all_monthly_do_his

anova_monthly_do_his_0=annova_uncertainity(all_monthly_do_his_0)

anova_monthly_do_his_0.describe().loc['mean', :]
"""
GCMs           1.000000e+02
param          5.682552e-22
interaction   -5.048721e-16
GCMs/param              inf
year           1.933000e+03
Name: mean, dtype: float64
"""

anova_monthly_do_his_1=annova_uncertainity(all_monthly_do_his_1)

anova_monthly_do_his_1.describe().loc['mean', :]
"""
GCMs           1.000000e+02
param          4.332472e-22
interaction   -1.931809e-15
GCMs/param              inf
year           1.933000e+03
Name: mean, dtype: float64
"""

anova_monthly_do_his_2=annova_uncertainity(all_monthly_do_his_2)

anova_monthly_do_his_2.describe().loc['mean', :]
"""
GCMs           1.000000e+02
param          3.137998e-24
interaction    1.968271e-15
GCMs/param              inf
year           1.933000e+03
Name: mean, dtype: float64
"""
#March 
anova_monthly_do_his_3=annova_uncertainity(all_monthly_do_his_3)
anova_monthly_do_his_3.describe().loc['mean', :]
"""
GCMs             99.985841
param             0.004390
interaction       0.009769
GCMs/param             inf
year           1933.000000
Name: mean, dtype: float64
"""
anova_monthly_do_his_3.describe().loc['std', :]
"""
GCMs            0.079383
param           0.027187
interaction     0.052332
GCMs/param           NaN
year           42.001984
Name: std, dtype: float64
"""
anova_monthly_do_his_4=annova_uncertainity(all_monthly_do_his_4)

anova_monthly_do_his_4.describe().loc['mean', :]
"""
GCMs             93.842966
param             4.593322
interaction       1.563712
GCMs/param      111.948910
year           1933.000000
Name: mean, dtype: float64
"""

anova_monthly_do_his_4.describe().loc['std', :]
"""
GCMs             9.409381
param            7.608053
interaction      2.341042
GCMs/param     327.015660
year            42.001984
Name: std, dtype: float64
"""


anova_monthly_do_his_5=annova_uncertainity(all_monthly_do_his_5)

anova_monthly_do_his_5.describe().loc['mean', :]
"""
GCMs             77.224553
param            21.389600
interaction       1.385847
GCMs/param        8.615269
year           1933.000000
Name: mean, dtype: float64
"""


anova_monthly_do_his_5.describe().loc['std', :]

"""
GCMs           18.720576
param          18.757074
interaction     1.253404
GCMs/param      9.862688
year           42.001984
Name: std, dtype: float64

"""
anova_monthly_do_his_6=annova_uncertainity(all_monthly_do_his_6)

anova_monthly_do_his_6.describe().loc['mean', :]
"""
GCMs             67.651916
param            30.837112
interaction       1.510971
GCMs/param        7.171834
year           1933.000000
Name: mean, dtype: float64
"""


anova_monthly_do_his_6.describe().loc['std', :]
"""
GCMs           22.947757
param          22.575547
interaction     1.189793
GCMs/param     12.824723
year           42.001984
Name: std, dtype: float64
"""
anova_monthly_do_his_7=annova_uncertainity(all_monthly_do_his_7)

anova_monthly_do_his_7.describe().loc['mean', :]
"""
GCMs           9.035629e+01
param          4.575630e+00
interaction    5.068081e+00
GCMs/param     1.040037e+30
year           1.933000e+03
Name: mean, dtype: float64
"""


anova_monthly_do_his_7.describe().loc['std', :]
"""
GCMs           1.919359e+01
param          1.073112e+01
interaction    9.695911e+00
GCMs/param     1.247658e+31
year           4.200198e+01
Name: std, dtype: float64
"""

anova_monthly_do_his_8=annova_uncertainity(all_monthly_do_his_8)

anova_monthly_do_his_8.describe().loc['mean', :]
"""
GCMs             99.963647
param             0.009088
interaction       0.027265
GCMs/param             inf
year           1933.000000
Name: mean, dtype: float64
"""


anova_monthly_do_his_8.describe().loc['std', :]
"""
GCMs            0.287444
param           0.071861
interaction     0.215583
GCMs/param           NaN
year           42.001984
Name: std, dtype: float64
"""

anova_monthly_do_his_9=annova_uncertainity(all_monthly_do_his_9)

anova_monthly_do_his_9.describe().loc['mean', :]
"""
GCMs           1.000000e+02
param          3.103586e-25
interaction   -3.511947e-17
GCMs/param              inf
year           1.933000e+03
Name: mean, dtype: float64
"""



anova_monthly_do_his_10=annova_uncertainity(all_monthly_do_his_10)

anova_monthly_do_his_10.describe().loc['mean', :]
"""
GCMs           1.000000e+02
param          2.206920e-25
interaction   -8.823533e-16
GCMs/param              inf
year           1.933000e+03
Name: mean, dtype: float64
"""

anova_monthly_do_his_11=annova_uncertainity(all_monthly_do_his_11)

anova_monthly_do_his_11.describe().loc['mean', :]
"""
GCMs           1.000000e+02
param          6.183183e-25
interaction    1.378583e-15
GCMs/param              inf
year           1.933000e+03
Name: mean, dtype: float64
"""




#%% GLUE method on all_monthly_do_his for each depth 
          
#month 0 : jan

# monthly anoxic duration  
timeseries_year_his= all_monthly_do_his_0.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_monthly_do_his_0.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights))

# Build glue df
glue_df_monthly_0_hypolimnetic_ave_his = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_df_monthly_0_hypolimnetic_ave_his=glue_df_monthly_0_hypolimnetic_ave_his.set_index(timeseries_year_his)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory
glue_df_monthly_0_hypolimnetic_ave_his.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/his/glue_jan_hypolimnetic_ave_his.csv')
        
#%%month feb

# monthly anoxic duration  
timeseries_year_his= all_monthly_do_his_1.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_monthly_do_his_1.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights))

# Build glue df
glue_df_monthly_1_hypolimnetic_ave_his = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_df_monthly_1_hypolimnetic_ave_his=glue_df_monthly_1_hypolimnetic_ave_his.set_index(timeseries_year_his)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory
glue_df_monthly_1_hypolimnetic_ave_his.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/his/glue_feb_hypolimnetic_ave_his.csv')
        

#%%month mar

# monthly anoxic duration  
timeseries_year_his= all_monthly_do_his_2.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_monthly_do_his_2.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights))

# Build glue df
glue_df_monthly_2_hypolimnetic_ave_his = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_df_monthly_2_hypolimnetic_ave_his=glue_df_monthly_2_hypolimnetic_ave_his.set_index(timeseries_year_his)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory
glue_df_monthly_2_hypolimnetic_ave_his.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/his/glue_mar_hypolimnetic_ave_his.csv')
        


#%%month apr

# monthly anoxic duration  
timeseries_year_his= all_monthly_do_his_3.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_monthly_do_his_3.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights))

# Build glue df
glue_df_monthly_3_hypolimnetic_ave_his = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_df_monthly_3_hypolimnetic_ave_his=glue_df_monthly_3_hypolimnetic_ave_his.set_index(timeseries_year_his)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory
glue_df_monthly_3_hypolimnetic_ave_his.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/his/glue_apr_hypolimnetic_ave_his.csv')
        


#%%month may

# monthly anoxic duration  
timeseries_year_his= all_monthly_do_his_4.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_monthly_do_his_4.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights))

# Build glue df
glue_df_monthly_4_hypolimnetic_ave_his = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_df_monthly_4_hypolimnetic_ave_his=glue_df_monthly_4_hypolimnetic_ave_his.set_index(timeseries_year_his)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory
glue_df_monthly_4_hypolimnetic_ave_his.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/his/glue_may_hypolimnetic_ave_his.csv')
        

#%%month jun

# monthly anoxic duration  
timeseries_year_his= all_monthly_do_his_5.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_monthly_do_his_5.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights))

# Build glue df
glue_df_monthly_5_hypolimnetic_ave_his = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_df_monthly_5_hypolimnetic_ave_his=glue_df_monthly_5_hypolimnetic_ave_his.set_index(timeseries_year_his)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory
glue_df_monthly_5_hypolimnetic_ave_his.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/his/glue_jun_hypolimnetic_ave_his.csv')
        


#%%month jul

# monthly anoxic duration  
timeseries_year_his= all_monthly_do_his_6.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_monthly_do_his_6.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights))

# Build glue df
glue_df_monthly_6_hypolimnetic_ave_his = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_df_monthly_6_hypolimnetic_ave_his=glue_df_monthly_6_hypolimnetic_ave_his.set_index(timeseries_year_his)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory
glue_df_monthly_6_hypolimnetic_ave_his.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/his/glue_jul_hypolimnetic_ave_his.csv')
        


#%%month aug

# monthly anoxic duration  
timeseries_year_his= all_monthly_do_his_7.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_monthly_do_his_7.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights))

# Build glue df
glue_df_monthly_7_hypolimnetic_ave_his = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_df_monthly_7_hypolimnetic_ave_his=glue_df_monthly_7_hypolimnetic_ave_his.set_index(timeseries_year_his)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory
glue_df_monthly_7_hypolimnetic_ave_his.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/his/glue_aug_hypolimnetic_ave_his.csv')
        


#%%month sep

# monthly anoxic duration  
timeseries_year_his= all_monthly_do_his_8.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_monthly_do_his_8.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights))

# Build glue df
glue_df_monthly_8_hypolimnetic_ave_his = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_df_monthly_8_hypolimnetic_ave_his=glue_df_monthly_8_hypolimnetic_ave_his.set_index(timeseries_year_his)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory
glue_df_monthly_8_hypolimnetic_ave_his.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/his/glue_sep_hypolimnetic_ave_his.csv')
        


#%%month oct

# monthly anoxic duration  
timeseries_year_his= all_monthly_do_his_9.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_monthly_do_his_9.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights))

# Build glue df
glue_df_monthly_9_hypolimnetic_ave_his = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_df_monthly_9_hypolimnetic_ave_his=glue_df_monthly_9_hypolimnetic_ave_his.set_index(timeseries_year_his)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory
glue_df_monthly_9_hypolimnetic_ave_his.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/his/glue_oct_hypolimnetic_ave_his.csv')
        

#%%month nov

# monthly anoxic duration  
timeseries_year_his= all_monthly_do_his_10.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_monthly_do_his_10.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights))

# Build glue df
glue_df_monthly_10_hypolimnetic_ave_his = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_df_monthly_10_hypolimnetic_ave_his=glue_df_monthly_10_hypolimnetic_ave_his.set_index(timeseries_year_his)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory
glue_df_monthly_10_hypolimnetic_ave_his.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/his/glue_nov_hypolimnetic_ave_his.csv')
        

#%%month dec

# monthly anoxic duration  
timeseries_year_his= all_monthly_do_his_11.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_monthly_do_his_11.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights))

# Build glue df
glue_df_monthly_11_hypolimnetic_ave_his = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_df_monthly_11_hypolimnetic_ave_his=glue_df_monthly_11_hypolimnetic_ave_his.set_index(timeseries_year_his)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory
glue_df_monthly_11_hypolimnetic_ave_his.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/his/glue_dec_hypolimnetic_ave_his.csv')
        
#%%RCP26

#%% monthly hypolimnetic_ave_rcp26
all_weights= np.array([])
all_monthly_do_rcp26_0=pd.DataFrame([])
all_monthly_do_rcp26_1=pd.DataFrame([])
all_monthly_do_rcp26_2=pd.DataFrame([])
all_monthly_do_rcp26_3=pd.DataFrame([])
all_monthly_do_rcp26_4=pd.DataFrame([])
all_monthly_do_rcp26_5=pd.DataFrame([])
all_monthly_do_rcp26_6=pd.DataFrame([])
all_monthly_do_rcp26_7=pd.DataFrame([])
all_monthly_do_rcp26_8=pd.DataFrame([])
all_monthly_do_rcp26_9=pd.DataFrame([])
all_monthly_do_rcp26_10=pd.DataFrame([])
all_monthly_do_rcp26_11=pd.DataFrame([])
#gfdl

# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp26'

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
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the monthly_hypolimnetic_ave function
        result = monthly_hypolimnetic_ave(C, Vr, time_series )

        
        all_monthly_do_rcp26_0 = pd.concat([all_monthly_do_rcp26_0 , result.iloc[:, 0]], axis=1)
        all_monthly_do_rcp26_1 = pd.concat([all_monthly_do_rcp26_1 , result.iloc[:, 1]], axis=1)
        all_monthly_do_rcp26_2 = pd.concat([all_monthly_do_rcp26_2 , result.iloc[:, 2]], axis=1)
        all_monthly_do_rcp26_3 = pd.concat([all_monthly_do_rcp26_3 , result.iloc[:, 3]], axis=1)
        all_monthly_do_rcp26_4 = pd.concat([all_monthly_do_rcp26_4 , result.iloc[:, 4]], axis=1)
        all_monthly_do_rcp26_5 = pd.concat([all_monthly_do_rcp26_5 , result.iloc[:, 5]], axis=1)
        all_monthly_do_rcp26_6 = pd.concat([all_monthly_do_rcp26_6 , result.iloc[:, 6]], axis=1)
        all_monthly_do_rcp26_7 = pd.concat([all_monthly_do_rcp26_7 , result.iloc[:, 7]], axis=1)
        all_monthly_do_rcp26_8 = pd.concat([all_monthly_do_rcp26_8 , result.iloc[:, 8]], axis=1)
        all_monthly_do_rcp26_9 = pd.concat([all_monthly_do_rcp26_9 , result.iloc[:, 9]], axis=1)
        all_monthly_do_rcp26_10 = pd.concat([all_monthly_do_rcp26_10 , result.iloc[:, 10]], axis=1)
        all_monthly_do_rcp26_11 = pd.concat([all_monthly_do_rcp26_11 , result.iloc[:, 11]], axis=1)



        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_hypolimnetic_ave_gfdl_rcp26_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, header=['monthly_hypolimnetic_ave'])
        
#hadgem               
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
        
        all_weights= np.append(all_weights , weights) 
        
        
        
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the monthly_hypolimnetic_ave function
        result = monthly_hypolimnetic_ave(C, Vr, time_series )

        
        all_monthly_do_rcp26_0 = pd.concat([all_monthly_do_rcp26_0 , result.iloc[:, 0]], axis=1)
        all_monthly_do_rcp26_1 = pd.concat([all_monthly_do_rcp26_1 , result.iloc[:, 1]], axis=1)
        all_monthly_do_rcp26_2 = pd.concat([all_monthly_do_rcp26_2 , result.iloc[:, 2]], axis=1)
        all_monthly_do_rcp26_3 = pd.concat([all_monthly_do_rcp26_3 , result.iloc[:, 3]], axis=1)
        all_monthly_do_rcp26_4 = pd.concat([all_monthly_do_rcp26_4 , result.iloc[:, 4]], axis=1)
        all_monthly_do_rcp26_5 = pd.concat([all_monthly_do_rcp26_5 , result.iloc[:, 5]], axis=1)
        all_monthly_do_rcp26_6 = pd.concat([all_monthly_do_rcp26_6 , result.iloc[:, 6]], axis=1)
        all_monthly_do_rcp26_7 = pd.concat([all_monthly_do_rcp26_7 , result.iloc[:, 7]], axis=1)
        all_monthly_do_rcp26_8 = pd.concat([all_monthly_do_rcp26_8 , result.iloc[:, 8]], axis=1)
        all_monthly_do_rcp26_9 = pd.concat([all_monthly_do_rcp26_9 , result.iloc[:, 9]], axis=1)
        all_monthly_do_rcp26_10 = pd.concat([all_monthly_do_rcp26_10 , result.iloc[:, 10]], axis=1)
        all_monthly_do_rcp26_11 = pd.concat([all_monthly_do_rcp26_11 , result.iloc[:, 11]], axis=1)



        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_hypolimnetic_ave_hadgem_rcp26_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, header=['monthly_hypolimnetic_ave'])
      
#ipsl       
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
        
        all_weights= np.append(all_weights , weights) 
        
        
        
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the monthly_hypolimnetic_ave function
        result = monthly_hypolimnetic_ave(C, Vr, time_series )

        
        all_monthly_do_rcp26_0 = pd.concat([all_monthly_do_rcp26_0 , result.iloc[:, 0]], axis=1)
        all_monthly_do_rcp26_1 = pd.concat([all_monthly_do_rcp26_1 , result.iloc[:, 1]], axis=1)
        all_monthly_do_rcp26_2 = pd.concat([all_monthly_do_rcp26_2 , result.iloc[:, 2]], axis=1)
        all_monthly_do_rcp26_3 = pd.concat([all_monthly_do_rcp26_3 , result.iloc[:, 3]], axis=1)
        all_monthly_do_rcp26_4 = pd.concat([all_monthly_do_rcp26_4 , result.iloc[:, 4]], axis=1)
        all_monthly_do_rcp26_5 = pd.concat([all_monthly_do_rcp26_5 , result.iloc[:, 5]], axis=1)
        all_monthly_do_rcp26_6 = pd.concat([all_monthly_do_rcp26_6 , result.iloc[:, 6]], axis=1)
        all_monthly_do_rcp26_7 = pd.concat([all_monthly_do_rcp26_7 , result.iloc[:, 7]], axis=1)
        all_monthly_do_rcp26_8 = pd.concat([all_monthly_do_rcp26_8 , result.iloc[:, 8]], axis=1)
        all_monthly_do_rcp26_9 = pd.concat([all_monthly_do_rcp26_9 , result.iloc[:, 9]], axis=1)
        all_monthly_do_rcp26_10 = pd.concat([all_monthly_do_rcp26_10 , result.iloc[:, 10]], axis=1)
        all_monthly_do_rcp26_11 = pd.concat([all_monthly_do_rcp26_11 , result.iloc[:, 11]], axis=1)



        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_hypolimnetic_ave_ipsl_rcp26_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, header=['monthly_hypolimnetic_ave'])
        

#miroc       
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
        
        all_weights= np.append(all_weights , weights) 
        
        
        
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the monthly_hypolimnetic_ave function
        result = monthly_hypolimnetic_ave(C, Vr, time_series )

        
        all_monthly_do_rcp26_0 = pd.concat([all_monthly_do_rcp26_0 , result.iloc[:, 0]], axis=1)
        all_monthly_do_rcp26_1 = pd.concat([all_monthly_do_rcp26_1 , result.iloc[:, 1]], axis=1)
        all_monthly_do_rcp26_2 = pd.concat([all_monthly_do_rcp26_2 , result.iloc[:, 2]], axis=1)
        all_monthly_do_rcp26_3 = pd.concat([all_monthly_do_rcp26_3 , result.iloc[:, 3]], axis=1)
        all_monthly_do_rcp26_4 = pd.concat([all_monthly_do_rcp26_4 , result.iloc[:, 4]], axis=1)
        all_monthly_do_rcp26_5 = pd.concat([all_monthly_do_rcp26_5 , result.iloc[:, 5]], axis=1)
        all_monthly_do_rcp26_6 = pd.concat([all_monthly_do_rcp26_6 , result.iloc[:, 6]], axis=1)
        all_monthly_do_rcp26_7 = pd.concat([all_monthly_do_rcp26_7 , result.iloc[:, 7]], axis=1)
        all_monthly_do_rcp26_8 = pd.concat([all_monthly_do_rcp26_8 , result.iloc[:, 8]], axis=1)
        all_monthly_do_rcp26_9 = pd.concat([all_monthly_do_rcp26_9 , result.iloc[:, 9]], axis=1)
        all_monthly_do_rcp26_10 = pd.concat([all_monthly_do_rcp26_10 , result.iloc[:, 10]], axis=1)
        all_monthly_do_rcp26_11 = pd.concat([all_monthly_do_rcp26_11 , result.iloc[:, 11]], axis=1)



        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_hypolimnetic_ave_miroc_rcp26_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, header=['monthly_hypolimnetic_ave'])
        



#%%

all_monthly_do_rcp26_0 = all_monthly_do_rcp26_0.rename_axis('Datetime')
all_monthly_do_rcp26_1 = all_monthly_do_rcp26_1.rename_axis('Datetime')
all_monthly_do_rcp26_2 = all_monthly_do_rcp26_2.rename_axis('Datetime')
all_monthly_do_rcp26_3 = all_monthly_do_rcp26_3.rename_axis('Datetime')
all_monthly_do_rcp26_4 = all_monthly_do_rcp26_4.rename_axis('Datetime')
all_monthly_do_rcp26_5 = all_monthly_do_rcp26_5.rename_axis('Datetime')
all_monthly_do_rcp26_6 = all_monthly_do_rcp26_6.rename_axis('Datetime')
all_monthly_do_rcp26_7 = all_monthly_do_rcp26_7.rename_axis('Datetime')
all_monthly_do_rcp26_8 = all_monthly_do_rcp26_8.rename_axis('Datetime')
all_monthly_do_rcp26_9 = all_monthly_do_rcp26_9.rename_axis('Datetime')
all_monthly_do_rcp26_10 = all_monthly_do_rcp26_10.rename_axis('Datetime')
all_monthly_do_rcp26_11 = all_monthly_do_rcp26_11.rename_axis('Datetime')

#%%Uncertainity partitioning on all_monthly_do_rcp26

anova_monthly_do_rcp26_0=annova_uncertainity(all_monthly_do_rcp26_0)

anova_monthly_do_rcp26_0.describe().loc['mean', :]
"""
GCMs           1.000000e+02
param          1.050261e-24
interaction    6.164172e-16
GCMs/param              inf
year           2.052500e+03
Name: mean, dtype: float64
"""

anova_monthly_do_rcp26_1=annova_uncertainity(all_monthly_do_rcp26_1)

anova_monthly_do_rcp26_1.describe().loc['mean', :]
"""
GCMs           1.000000e+02
param          8.430778e-24
interaction   -1.667397e-15
GCMs/param              inf
year           2.052500e+03
Name: mean, dtype: float64
"""

anova_monthly_do_rcp26_2=annova_uncertainity(all_monthly_do_rcp26_2)

anova_monthly_do_rcp26_2.describe().loc['mean', :]
"""
GCMs           1.000000e+02
param          2.720049e-25
interaction   -4.436785e-16
GCMs/param              inf
year           2.052500e+03
Name: mean, dtype: float64
"""
#March 
anova_monthly_do_rcp26_3=annova_uncertainity(all_monthly_do_rcp26_3)

anova_monthly_do_rcp26_3.describe().loc['mean', :]
"""
GCMs           9.983916e+01
param          6.778722e-02
interaction    9.304983e-02
GCMs/param     3.838645e+26
year           2.052500e+03
Name: mean, dtype: float64
"""
anova_monthly_do_rcp26_3.describe().loc['std', :]
"""
GCMs           2.777836e-01
param          1.516572e-01
interaction    1.579594e-01
GCMs/param     1.704457e+27
year           2.727942e+01
Name: std, dtype: float64
"""
anova_monthly_do_rcp26_4=annova_uncertainity(all_monthly_do_rcp26_4)

anova_monthly_do_rcp26_4.describe().loc['mean', :]
"""
GCMs             90.440626
param             8.017104
interaction       1.542270
GCMs/param       43.930191
year           2052.500000
Name: mean, dtype: float64
"""

anova_monthly_do_rcp26_4.describe().loc['std', :]
"""
GCMs           10.844658
param          10.222205
interaction     1.370120
GCMs/param     95.637721
year           27.279418
Name: std, dtype: float64
"""


anova_monthly_do_rcp26_5=annova_uncertainity(all_monthly_do_rcp26_5)

anova_monthly_do_rcp26_5.describe().loc['mean', :]
"""
GCMs             74.659450
param            24.612511
interaction       0.728039
GCMs/param        6.312723
year           2052.500000
Name: mean, dtype: float64
"""


anova_monthly_do_rcp26_5.describe().loc['std', :]

"""
GCMs           18.428196
param          18.372239
interaction     0.644377
GCMs/param      6.872015
year           27.279418
Name: std, dtype: float64

"""
anova_monthly_do_rcp26_6=annova_uncertainity(all_monthly_do_rcp26_6)

anova_monthly_do_rcp26_6.describe().loc['mean', :]
"""
GCMs             61.960927
param            34.026167
interaction       4.012905
GCMs/param        3.851830
year           2052.500000
Name: mean, dtype: float64
"""


anova_monthly_do_rcp26_6.describe().loc['std', :]
"""
GCMs           20.982445
param          20.796373
interaction     2.771681
GCMs/param      5.751830
year           27.279418
Name: std, dtype: float64
"""
anova_monthly_do_rcp26_7=annova_uncertainity(all_monthly_do_rcp26_7)

anova_monthly_do_rcp26_7.describe().loc['mean', :]
"""
GCMs             65.542815
param            12.250327
interaction      22.206858
GCMs/param             inf
year           2052.500000
Name: mean, dtype: float64
"""


anova_monthly_do_rcp26_7.describe().loc['std', :]
"""
GCMs           38.183186
param          15.585730
interaction    25.035118
GCMs/param           NaN
year           27.279418
Name: std, dtype: float64
"""

anova_monthly_do_rcp26_8=annova_uncertainity(all_monthly_do_rcp26_8)

anova_monthly_do_rcp26_8.describe().loc['mean', :]
"""
GCMs             99.995897
param             0.001026
interaction       0.003077
GCMs/param             inf
year           2052.500000
Name: mean, dtype: float64
"""


anova_monthly_do_rcp26_8.describe().loc['std', :]
"""
GCMs            0.038711
param           0.009678
interaction     0.029033
GCMs/param           NaN
year           27.279418
Name: std, dtype: float64
"""

anova_monthly_do_rcp26_9=annova_uncertainity(all_monthly_do_rcp26_9)

anova_monthly_do_rcp26_9.describe().loc['mean', :]
"""
GCMs           1.000000e+02
param          4.033586e-25
interaction    1.878522e-16
GCMs/param              inf
year           2.052500e+03
Name: mean, dtype: float64
"""



anova_monthly_do_rcp26_10=annova_uncertainity(all_monthly_do_rcp26_10)

anova_monthly_do_rcp26_10.describe().loc['mean', :]
"""
GCMs           1.000000e+02
param          2.340948e-25
interaction   -4.534975e-16
GCMs/param              inf
year           2.052500e+03
Name: mean, dtype: float64
"""

anova_monthly_do_rcp26_11=annova_uncertainity(all_monthly_do_rcp26_11)

anova_monthly_do_rcp26_11.describe().loc['mean', :]
"""
GCMs           1.000000e+02
param          1.665271e-25
interaction   -3.716846e-16
GCMs/param              inf
year           2.052500e+03
Name: mean, dtype: float64
"""




#%% GLUE method on all_monthly_do_rcp26 for each depth 
          
#month 0 : jan

# monthly anoxic duration  
timeseries_year_rcp26= all_monthly_do_rcp26_0.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_monthly_do_rcp26_0.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights))

# Build glue df
glue_df_monthly_0_hypolimnetic_ave_rcp26 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_df_monthly_0_hypolimnetic_ave_rcp26=glue_df_monthly_0_hypolimnetic_ave_rcp26.set_index(timeseries_year_rcp26)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory
glue_df_monthly_0_hypolimnetic_ave_rcp26.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/rcp26/glue_jan_hypolimnetic_ave_rcp26.csv')
        
#%%month feb

# monthly anoxic duration  
timeseries_year_rcp26= all_monthly_do_rcp26_1.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_monthly_do_rcp26_1.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights))

# Build glue df
glue_df_monthly_1_hypolimnetic_ave_rcp26 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_df_monthly_1_hypolimnetic_ave_rcp26=glue_df_monthly_1_hypolimnetic_ave_rcp26.set_index(timeseries_year_rcp26)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory
glue_df_monthly_1_hypolimnetic_ave_rcp26.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/rcp26/glue_feb_hypolimnetic_ave_rcp26.csv')
        

#%%month mar

# monthly anoxic duration  
timeseries_year_rcp26= all_monthly_do_rcp26_2.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_monthly_do_rcp26_2.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights))

# Build glue df
glue_df_monthly_2_hypolimnetic_ave_rcp26 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_df_monthly_2_hypolimnetic_ave_rcp26=glue_df_monthly_2_hypolimnetic_ave_rcp26.set_index(timeseries_year_rcp26)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory
glue_df_monthly_2_hypolimnetic_ave_rcp26.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/rcp26/glue_mar_hypolimnetic_ave_rcp26.csv')
        


#%%month apr

# monthly anoxic duration  
timeseries_year_rcp26= all_monthly_do_rcp26_3.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_monthly_do_rcp26_3.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights))

# Build glue df
glue_df_monthly_3_hypolimnetic_ave_rcp26 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_df_monthly_3_hypolimnetic_ave_rcp26=glue_df_monthly_3_hypolimnetic_ave_rcp26.set_index(timeseries_year_rcp26)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory
glue_df_monthly_3_hypolimnetic_ave_rcp26.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/rcp26/glue_apr_hypolimnetic_ave_rcp26.csv')
        


#%%month may

# monthly anoxic duration  
timeseries_year_rcp26= all_monthly_do_rcp26_4.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_monthly_do_rcp26_4.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights))

# Build glue df
glue_df_monthly_4_hypolimnetic_ave_rcp26 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_df_monthly_4_hypolimnetic_ave_rcp26=glue_df_monthly_4_hypolimnetic_ave_rcp26.set_index(timeseries_year_rcp26)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory
glue_df_monthly_4_hypolimnetic_ave_rcp26.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/rcp26/glue_may_hypolimnetic_ave_rcp26.csv')
        

#%%month jun

# monthly anoxic duration  
timeseries_year_rcp26= all_monthly_do_rcp26_5.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_monthly_do_rcp26_5.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights))

# Build glue df
glue_df_monthly_5_hypolimnetic_ave_rcp26 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_df_monthly_5_hypolimnetic_ave_rcp26=glue_df_monthly_5_hypolimnetic_ave_rcp26.set_index(timeseries_year_rcp26)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory
glue_df_monthly_5_hypolimnetic_ave_rcp26.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/rcp26/glue_jun_hypolimnetic_ave_rcp26.csv')
        


#%%month jul

# monthly anoxic duration  
timeseries_year_rcp26= all_monthly_do_rcp26_6.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_monthly_do_rcp26_6.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights))

# Build glue df
glue_df_monthly_6_hypolimnetic_ave_rcp26 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_df_monthly_6_hypolimnetic_ave_rcp26=glue_df_monthly_6_hypolimnetic_ave_rcp26.set_index(timeseries_year_rcp26)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory
glue_df_monthly_6_hypolimnetic_ave_rcp26.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/rcp26/glue_jul_hypolimnetic_ave_rcp26.csv')
        


#%%month aug

# monthly anoxic duration  
timeseries_year_rcp26= all_monthly_do_rcp26_7.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_monthly_do_rcp26_7.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights))

# Build glue df
glue_df_monthly_7_hypolimnetic_ave_rcp26 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_df_monthly_7_hypolimnetic_ave_rcp26=glue_df_monthly_7_hypolimnetic_ave_rcp26.set_index(timeseries_year_rcp26)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory
glue_df_monthly_7_hypolimnetic_ave_rcp26.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/rcp26/glue_aug_hypolimnetic_ave_rcp26.csv')
        


#%%month sep

# monthly anoxic duration  
timeseries_year_rcp26= all_monthly_do_rcp26_8.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_monthly_do_rcp26_8.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights))

# Build glue df
glue_df_monthly_8_hypolimnetic_ave_rcp26 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_df_monthly_8_hypolimnetic_ave_rcp26=glue_df_monthly_8_hypolimnetic_ave_rcp26.set_index(timeseries_year_rcp26)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory
glue_df_monthly_8_hypolimnetic_ave_rcp26.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/rcp26/glue_sep_hypolimnetic_ave_rcp26.csv')
        


#%%month oct

# monthly anoxic duration  
timeseries_year_rcp26= all_monthly_do_rcp26_9.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_monthly_do_rcp26_9.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights))

# Build glue df
glue_df_monthly_9_hypolimnetic_ave_rcp26 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_df_monthly_9_hypolimnetic_ave_rcp26=glue_df_monthly_9_hypolimnetic_ave_rcp26.set_index(timeseries_year_rcp26)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory
glue_df_monthly_9_hypolimnetic_ave_rcp26.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/rcp26/glue_oct_hypolimnetic_ave_rcp26.csv')
        

#%%month nov

# monthly anoxic duration  
timeseries_year_rcp26= all_monthly_do_rcp26_10.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_monthly_do_rcp26_10.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights))

# Build glue df
glue_df_monthly_10_hypolimnetic_ave_rcp26 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_df_monthly_10_hypolimnetic_ave_rcp26=glue_df_monthly_10_hypolimnetic_ave_rcp26.set_index(timeseries_year_rcp26)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory
glue_df_monthly_10_hypolimnetic_ave_rcp26.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/rcp26/glue_nov_hypolimnetic_ave_rcp26.csv')
        

#%%month dec

# monthly anoxic duration  
timeseries_year_rcp26= all_monthly_do_rcp26_11.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_monthly_do_rcp26_11.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights))

# Build glue df
glue_df_monthly_11_hypolimnetic_ave_rcp26 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_df_monthly_11_hypolimnetic_ave_rcp26=glue_df_monthly_11_hypolimnetic_ave_rcp26.set_index(timeseries_year_rcp26)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory
glue_df_monthly_11_hypolimnetic_ave_rcp26.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/rcp26/glue_dec_hypolimnetic_ave_rcp26.csv')
        









#%%RCP60
#%% monthly hypolimnetic_ave_rcp60
all_weights= np.array([])
all_monthly_do_rcp60_0=pd.DataFrame([])
all_monthly_do_rcp60_1=pd.DataFrame([])
all_monthly_do_rcp60_2=pd.DataFrame([])
all_monthly_do_rcp60_3=pd.DataFrame([])
all_monthly_do_rcp60_4=pd.DataFrame([])
all_monthly_do_rcp60_5=pd.DataFrame([])
all_monthly_do_rcp60_6=pd.DataFrame([])
all_monthly_do_rcp60_7=pd.DataFrame([])
all_monthly_do_rcp60_8=pd.DataFrame([])
all_monthly_do_rcp60_9=pd.DataFrame([])
all_monthly_do_rcp60_10=pd.DataFrame([])
all_monthly_do_rcp60_11=pd.DataFrame([])
#gfdl

# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp60'

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
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the monthly_hypolimnetic_ave function
        result = monthly_hypolimnetic_ave(C, Vr, time_series )

        
        all_monthly_do_rcp60_0 = pd.concat([all_monthly_do_rcp60_0 , result.iloc[:, 0]], axis=1)
        all_monthly_do_rcp60_1 = pd.concat([all_monthly_do_rcp60_1 , result.iloc[:, 1]], axis=1)
        all_monthly_do_rcp60_2 = pd.concat([all_monthly_do_rcp60_2 , result.iloc[:, 2]], axis=1)
        all_monthly_do_rcp60_3 = pd.concat([all_monthly_do_rcp60_3 , result.iloc[:, 3]], axis=1)
        all_monthly_do_rcp60_4 = pd.concat([all_monthly_do_rcp60_4 , result.iloc[:, 4]], axis=1)
        all_monthly_do_rcp60_5 = pd.concat([all_monthly_do_rcp60_5 , result.iloc[:, 5]], axis=1)
        all_monthly_do_rcp60_6 = pd.concat([all_monthly_do_rcp60_6 , result.iloc[:, 6]], axis=1)
        all_monthly_do_rcp60_7 = pd.concat([all_monthly_do_rcp60_7 , result.iloc[:, 7]], axis=1)
        all_monthly_do_rcp60_8 = pd.concat([all_monthly_do_rcp60_8 , result.iloc[:, 8]], axis=1)
        all_monthly_do_rcp60_9 = pd.concat([all_monthly_do_rcp60_9 , result.iloc[:, 9]], axis=1)
        all_monthly_do_rcp60_10 = pd.concat([all_monthly_do_rcp60_10 , result.iloc[:, 10]], axis=1)
        all_monthly_do_rcp60_11 = pd.concat([all_monthly_do_rcp60_11 , result.iloc[:, 11]], axis=1)



        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_hypolimnetic_ave_gfdl_rcp60_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, header=['monthly_hypolimnetic_ave'])
        
#hadgem               
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
        
        all_weights= np.append(all_weights , weights) 
        
        
        
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the monthly_hypolimnetic_ave function
        result = monthly_hypolimnetic_ave(C, Vr, time_series )

        
        all_monthly_do_rcp60_0 = pd.concat([all_monthly_do_rcp60_0 , result.iloc[:, 0]], axis=1)
        all_monthly_do_rcp60_1 = pd.concat([all_monthly_do_rcp60_1 , result.iloc[:, 1]], axis=1)
        all_monthly_do_rcp60_2 = pd.concat([all_monthly_do_rcp60_2 , result.iloc[:, 2]], axis=1)
        all_monthly_do_rcp60_3 = pd.concat([all_monthly_do_rcp60_3 , result.iloc[:, 3]], axis=1)
        all_monthly_do_rcp60_4 = pd.concat([all_monthly_do_rcp60_4 , result.iloc[:, 4]], axis=1)
        all_monthly_do_rcp60_5 = pd.concat([all_monthly_do_rcp60_5 , result.iloc[:, 5]], axis=1)
        all_monthly_do_rcp60_6 = pd.concat([all_monthly_do_rcp60_6 , result.iloc[:, 6]], axis=1)
        all_monthly_do_rcp60_7 = pd.concat([all_monthly_do_rcp60_7 , result.iloc[:, 7]], axis=1)
        all_monthly_do_rcp60_8 = pd.concat([all_monthly_do_rcp60_8 , result.iloc[:, 8]], axis=1)
        all_monthly_do_rcp60_9 = pd.concat([all_monthly_do_rcp60_9 , result.iloc[:, 9]], axis=1)
        all_monthly_do_rcp60_10 = pd.concat([all_monthly_do_rcp60_10 , result.iloc[:, 10]], axis=1)
        all_monthly_do_rcp60_11 = pd.concat([all_monthly_do_rcp60_11 , result.iloc[:, 11]], axis=1)



        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_hypolimnetic_ave_hadgem_rcp60_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, header=['monthly_hypolimnetic_ave'])
      
#ipsl       
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
        
        all_weights= np.append(all_weights , weights) 
        
        
        
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the monthly_hypolimnetic_ave function
        result = monthly_hypolimnetic_ave(C, Vr, time_series )

        
        all_monthly_do_rcp60_0 = pd.concat([all_monthly_do_rcp60_0 , result.iloc[:, 0]], axis=1)
        all_monthly_do_rcp60_1 = pd.concat([all_monthly_do_rcp60_1 , result.iloc[:, 1]], axis=1)
        all_monthly_do_rcp60_2 = pd.concat([all_monthly_do_rcp60_2 , result.iloc[:, 2]], axis=1)
        all_monthly_do_rcp60_3 = pd.concat([all_monthly_do_rcp60_3 , result.iloc[:, 3]], axis=1)
        all_monthly_do_rcp60_4 = pd.concat([all_monthly_do_rcp60_4 , result.iloc[:, 4]], axis=1)
        all_monthly_do_rcp60_5 = pd.concat([all_monthly_do_rcp60_5 , result.iloc[:, 5]], axis=1)
        all_monthly_do_rcp60_6 = pd.concat([all_monthly_do_rcp60_6 , result.iloc[:, 6]], axis=1)
        all_monthly_do_rcp60_7 = pd.concat([all_monthly_do_rcp60_7 , result.iloc[:, 7]], axis=1)
        all_monthly_do_rcp60_8 = pd.concat([all_monthly_do_rcp60_8 , result.iloc[:, 8]], axis=1)
        all_monthly_do_rcp60_9 = pd.concat([all_monthly_do_rcp60_9 , result.iloc[:, 9]], axis=1)
        all_monthly_do_rcp60_10 = pd.concat([all_monthly_do_rcp60_10 , result.iloc[:, 10]], axis=1)
        all_monthly_do_rcp60_11 = pd.concat([all_monthly_do_rcp60_11 , result.iloc[:, 11]], axis=1)



        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_hypolimnetic_ave_ipsl_rcp60_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, header=['monthly_hypolimnetic_ave'])
        

#miroc       
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
        
        all_weights= np.append(all_weights , weights) 
        
        
        
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the monthly_hypolimnetic_ave function
        result = monthly_hypolimnetic_ave(C, Vr, time_series )

        
        all_monthly_do_rcp60_0 = pd.concat([all_monthly_do_rcp60_0 , result.iloc[:, 0]], axis=1)
        all_monthly_do_rcp60_1 = pd.concat([all_monthly_do_rcp60_1 , result.iloc[:, 1]], axis=1)
        all_monthly_do_rcp60_2 = pd.concat([all_monthly_do_rcp60_2 , result.iloc[:, 2]], axis=1)
        all_monthly_do_rcp60_3 = pd.concat([all_monthly_do_rcp60_3 , result.iloc[:, 3]], axis=1)
        all_monthly_do_rcp60_4 = pd.concat([all_monthly_do_rcp60_4 , result.iloc[:, 4]], axis=1)
        all_monthly_do_rcp60_5 = pd.concat([all_monthly_do_rcp60_5 , result.iloc[:, 5]], axis=1)
        all_monthly_do_rcp60_6 = pd.concat([all_monthly_do_rcp60_6 , result.iloc[:, 6]], axis=1)
        all_monthly_do_rcp60_7 = pd.concat([all_monthly_do_rcp60_7 , result.iloc[:, 7]], axis=1)
        all_monthly_do_rcp60_8 = pd.concat([all_monthly_do_rcp60_8 , result.iloc[:, 8]], axis=1)
        all_monthly_do_rcp60_9 = pd.concat([all_monthly_do_rcp60_9 , result.iloc[:, 9]], axis=1)
        all_monthly_do_rcp60_10 = pd.concat([all_monthly_do_rcp60_10 , result.iloc[:, 10]], axis=1)
        all_monthly_do_rcp60_11 = pd.concat([all_monthly_do_rcp60_11 , result.iloc[:, 11]], axis=1)



        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_hypolimnetic_ave_miroc_rcp60_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, header=['monthly_hypolimnetic_ave'])
        



#%%

all_monthly_do_rcp60_0 = all_monthly_do_rcp60_0.rename_axis('Datetime')
all_monthly_do_rcp60_1 = all_monthly_do_rcp60_1.rename_axis('Datetime')
all_monthly_do_rcp60_2 = all_monthly_do_rcp60_2.rename_axis('Datetime')
all_monthly_do_rcp60_3 = all_monthly_do_rcp60_3.rename_axis('Datetime')
all_monthly_do_rcp60_4 = all_monthly_do_rcp60_4.rename_axis('Datetime')
all_monthly_do_rcp60_5 = all_monthly_do_rcp60_5.rename_axis('Datetime')
all_monthly_do_rcp60_6 = all_monthly_do_rcp60_6.rename_axis('Datetime')
all_monthly_do_rcp60_7 = all_monthly_do_rcp60_7.rename_axis('Datetime')
all_monthly_do_rcp60_8 = all_monthly_do_rcp60_8.rename_axis('Datetime')
all_monthly_do_rcp60_9 = all_monthly_do_rcp60_9.rename_axis('Datetime')
all_monthly_do_rcp60_10 = all_monthly_do_rcp60_10.rename_axis('Datetime')
all_monthly_do_rcp60_11 = all_monthly_do_rcp60_11.rename_axis('Datetime')

#%%Uncertainity partitioning on all_monthly_do_rcp60

anova_monthly_do_rcp60_0=annova_uncertainity(all_monthly_do_rcp60_0)

anova_monthly_do_rcp60_0.describe().loc['mean', :]
"""
GCMs           1.000000e+02
param          8.685978e-25
interaction    7.388064e-16
GCMs/param              inf
year           2.052500e+03
Name: mean, dtype: float64
"""

anova_monthly_do_rcp60_1=annova_uncertainity(all_monthly_do_rcp60_1)

anova_monthly_do_rcp60_1.describe().loc['mean', :]
"""
GCMs           1.000000e+02
param          2.291319e-22
interaction    7.807487e-16
GCMs/param              inf
year           2.052500e+03
Name: mean, dtype: float64
"""

anova_monthly_do_rcp60_2=annova_uncertainity(all_monthly_do_rcp60_2)

anova_monthly_do_rcp60_2.describe().loc['mean', :]
"""
GCMs           1.000000e+02
param          2.720049e-25
interaction   -4.436785e-16
GCMs/param              inf
year           2.052500e+03
Name: mean, dtype: float64
"""
#March 
anova_monthly_do_rcp60_3=annova_uncertainity(all_monthly_do_rcp60_3)

anova_monthly_do_rcp60_3.describe().loc['mean', :]
"""
GCMs           1.000000e+02
param          3.732922e-11
interaction    1.119868e-10
GCMs/param              inf
year           2.052500e+03
Name: mean, dtype: float64
"""
anova_monthly_do_rcp60_3.describe().loc['std', :]
"""
GCMs           6.675178e-01
param          2.906196e-01
interaction    3.873454e-01
GCMs/param     1.610360e+27
year           2.727942e+01
Name: std, dtype: float64
"""
#May
anova_monthly_do_rcp60_4=annova_uncertainity(all_monthly_do_rcp60_4)

anova_monthly_do_rcp60_4.describe().loc['mean', :]
"""
GCMs             86.269546
param            12.131101
interaction       1.599353
GCMs/param       31.816106
year           2052.500000
Name: mean, dtype: float64
"""

anova_monthly_do_rcp60_4.describe().loc['std', :]
"""
GCMs           16.119350
param          15.441854
interaction     1.805008
GCMs/param     56.042877
year           27.279418
Name: std, dtype: float64
"""


anova_monthly_do_rcp60_5=annova_uncertainity(all_monthly_do_rcp60_5)

anova_monthly_do_rcp60_5.describe().loc['mean', :]
"""
GCMs             71.152053
param            27.955348
interaction       0.892599
GCMs/param        6.028617
year           2052.500000
Name: mean, dtype: float64
"""


anova_monthly_do_rcp60_5.describe().loc['std', :]

"""
GCMs           20.193063
param          20.126510
interaction     1.402368
GCMs/param      7.112314
year           27.279418
Name: std, dtype: float64
"""
anova_monthly_do_rcp60_6=annova_uncertainity(all_monthly_do_rcp60_6)

anova_monthly_do_rcp60_6.describe().loc['mean', :]
"""
GCMs             58.517195
param            34.836016
interaction       6.646789
GCMs/param        5.071489
year           2052.500000
Name: mean, dtype: float64
"""


anova_monthly_do_rcp60_6.describe().loc['std', :]
"""
GCMs           23.682440
param          22.826306
interaction     5.476316
GCMs/param     10.596920
year           27.279418
Name: std, dtype: float64
"""
anova_monthly_do_rcp60_7=annova_uncertainity(all_monthly_do_rcp60_7)

anova_monthly_do_rcp60_7.describe().loc['mean', :]
"""
GCMs             79.170874
param             6.340980
interaction      14.488147
GCMs/param             inf
year           2052.500000
Name: mean, dtype: float64
"""


anova_monthly_do_rcp60_7.describe().loc['std', :]
"""
GCMs           34.412443
param          10.896342
interaction    24.242717
GCMs/param           NaN
year           27.279418
Name: std, dtype: float64
"""

anova_monthly_do_rcp60_8=annova_uncertainity(all_monthly_do_rcp60_8)

anova_monthly_do_rcp60_8.describe().loc['mean', :]
"""
GCMs             99.999944
param             0.000014
interaction       0.000042
GCMs/param             inf
year           2052.500000
Name: mean, dtype: float64
"""


anova_monthly_do_rcp60_8.describe().loc['std', :]
"""
GCMs            0.000396
param           0.000099
interaction     0.000297
GCMs/param           NaN
year           27.279418
Name: std, dtype: float64
"""

anova_monthly_do_rcp60_9=annova_uncertainity(all_monthly_do_rcp60_9)

anova_monthly_do_rcp60_9.describe().loc['mean', :]
"""
GCMs           1.000000e+02
param          3.280364e-25
interaction    4.916934e-16
GCMs/param              inf
year           2.052500e+03
Name: mean, dtype: float64
"""



anova_monthly_do_rcp60_10=annova_uncertainity(all_monthly_do_rcp60_10)

anova_monthly_do_rcp60_10.describe().loc['mean', :]
"""
GCMs           1.000000e+02
param          1.680672e-25
interaction   -1.015517e-16
GCMs/param              inf
year           2.052500e+03
Name: mean, dtype: float64
"""

anova_monthly_do_rcp60_11=annova_uncertainity(all_monthly_do_rcp60_11)

anova_monthly_do_rcp60_11.describe().loc['mean', :]
"""
GCMs           1.000000e+02
param          3.291279e-25
interaction    2.395710e-15
GCMs/param              inf
year           2.052500e+03
Name: mean, dtype: float64
"""




#%% GLUE method on all_monthly_do_rcp60 for each depth 
          
#month 0 : jan

# monthly anoxic duration  
timeseries_year_rcp60= all_monthly_do_rcp60_0.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_monthly_do_rcp60_0.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights))

# Build glue df
glue_df_monthly_0_hypolimnetic_ave_rcp60 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_df_monthly_0_hypolimnetic_ave_rcp60=glue_df_monthly_0_hypolimnetic_ave_rcp60.set_index(timeseries_year_rcp60)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory
glue_df_monthly_0_hypolimnetic_ave_rcp60.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/rcp60/glue_jan_hypolimnetic_ave_rcp60.csv')
        
#%%month feb

# monthly anoxic duration  
timeseries_year_rcp60= all_monthly_do_rcp60_1.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_monthly_do_rcp60_1.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights))

# Build glue df
glue_df_monthly_1_hypolimnetic_ave_rcp60 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_df_monthly_1_hypolimnetic_ave_rcp60=glue_df_monthly_1_hypolimnetic_ave_rcp60.set_index(timeseries_year_rcp60)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory
glue_df_monthly_1_hypolimnetic_ave_rcp60.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/rcp60/glue_feb_hypolimnetic_ave_rcp60.csv')
        

#%%month mar

# monthly anoxic duration  
timeseries_year_rcp60= all_monthly_do_rcp60_2.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_monthly_do_rcp60_2.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights))

# Build glue df
glue_df_monthly_2_hypolimnetic_ave_rcp60 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_df_monthly_2_hypolimnetic_ave_rcp60=glue_df_monthly_2_hypolimnetic_ave_rcp60.set_index(timeseries_year_rcp60)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory
glue_df_monthly_2_hypolimnetic_ave_rcp60.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/rcp60/glue_mar_hypolimnetic_ave_rcp60.csv')
        


#%%month apr

# monthly anoxic duration  
timeseries_year_rcp60= all_monthly_do_rcp60_3.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_monthly_do_rcp60_3.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights))

# Build glue df
glue_df_monthly_3_hypolimnetic_ave_rcp60 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_df_monthly_3_hypolimnetic_ave_rcp60=glue_df_monthly_3_hypolimnetic_ave_rcp60.set_index(timeseries_year_rcp60)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory
glue_df_monthly_3_hypolimnetic_ave_rcp60.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/rcp60/glue_apr_hypolimnetic_ave_rcp60.csv')
        


#%%month may

# monthly anoxic duration  
timeseries_year_rcp60= all_monthly_do_rcp60_4.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_monthly_do_rcp60_4.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights))

# Build glue df
glue_df_monthly_4_hypolimnetic_ave_rcp60 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_df_monthly_4_hypolimnetic_ave_rcp60=glue_df_monthly_4_hypolimnetic_ave_rcp60.set_index(timeseries_year_rcp60)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory
glue_df_monthly_4_hypolimnetic_ave_rcp60.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/rcp60/glue_may_hypolimnetic_ave_rcp60.csv')
        

#%%month jun

# monthly anoxic duration  
timeseries_year_rcp60= all_monthly_do_rcp60_5.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_monthly_do_rcp60_5.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights))

# Build glue df
glue_df_monthly_5_hypolimnetic_ave_rcp60 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_df_monthly_5_hypolimnetic_ave_rcp60=glue_df_monthly_5_hypolimnetic_ave_rcp60.set_index(timeseries_year_rcp60)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory
glue_df_monthly_5_hypolimnetic_ave_rcp60.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/rcp60/glue_jun_hypolimnetic_ave_rcp60.csv')
        


#%%month jul

# monthly anoxic duration  
timeseries_year_rcp60= all_monthly_do_rcp60_6.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_monthly_do_rcp60_6.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights))

# Build glue df
glue_df_monthly_6_hypolimnetic_ave_rcp60 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_df_monthly_6_hypolimnetic_ave_rcp60=glue_df_monthly_6_hypolimnetic_ave_rcp60.set_index(timeseries_year_rcp60)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory
glue_df_monthly_6_hypolimnetic_ave_rcp60.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/rcp60/glue_jul_hypolimnetic_ave_rcp60.csv')
        


#%%month aug

# monthly anoxic duration  
timeseries_year_rcp60= all_monthly_do_rcp60_7.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_monthly_do_rcp60_7.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights))

# Build glue df
glue_df_monthly_7_hypolimnetic_ave_rcp60 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_df_monthly_7_hypolimnetic_ave_rcp60=glue_df_monthly_7_hypolimnetic_ave_rcp60.set_index(timeseries_year_rcp60)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory
glue_df_monthly_7_hypolimnetic_ave_rcp60.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/rcp60/glue_aug_hypolimnetic_ave_rcp60.csv')
        


#%%month sep

# monthly anoxic duration  
timeseries_year_rcp60= all_monthly_do_rcp60_8.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_monthly_do_rcp60_8.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights))

# Build glue df
glue_df_monthly_8_hypolimnetic_ave_rcp60 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_df_monthly_8_hypolimnetic_ave_rcp60=glue_df_monthly_8_hypolimnetic_ave_rcp60.set_index(timeseries_year_rcp60)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory
glue_df_monthly_8_hypolimnetic_ave_rcp60.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/rcp60/glue_sep_hypolimnetic_ave_rcp60.csv')
        


#%%month oct

# monthly anoxic duration  
timeseries_year_rcp60= all_monthly_do_rcp60_9.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_monthly_do_rcp60_9.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights))

# Build glue df
glue_df_monthly_9_hypolimnetic_ave_rcp60 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_df_monthly_9_hypolimnetic_ave_rcp60=glue_df_monthly_9_hypolimnetic_ave_rcp60.set_index(timeseries_year_rcp60)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory
glue_df_monthly_9_hypolimnetic_ave_rcp60.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/rcp60/glue_oct_hypolimnetic_ave_rcp60.csv')
        

#%%month nov

# monthly anoxic duration  
timeseries_year_rcp60= all_monthly_do_rcp60_10.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_monthly_do_rcp60_10.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights))

# Build glue df
glue_df_monthly_10_hypolimnetic_ave_rcp60 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_df_monthly_10_hypolimnetic_ave_rcp60=glue_df_monthly_10_hypolimnetic_ave_rcp60.set_index(timeseries_year_rcp60)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory
glue_df_monthly_10_hypolimnetic_ave_rcp60.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/rcp60/glue_nov_hypolimnetic_ave_rcp60.csv')
        

#%%month dec

# monthly anoxic duration  
timeseries_year_rcp60= all_monthly_do_rcp60_11.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_monthly_do_rcp60_11.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights))

# Build glue df
glue_df_monthly_11_hypolimnetic_ave_rcp60 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_df_monthly_11_hypolimnetic_ave_rcp60=glue_df_monthly_11_hypolimnetic_ave_rcp60.set_index(timeseries_year_rcp60)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory
glue_df_monthly_11_hypolimnetic_ave_rcp60.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/rcp60/glue_dec_hypolimnetic_ave_rcp60.csv')
        

#%%RCP8.5
#%% monthly hypolimnetic_ave_rcp85
all_weights= np.array([])
all_monthly_do_rcp85_0=pd.DataFrame([])
all_monthly_do_rcp85_1=pd.DataFrame([])
all_monthly_do_rcp85_2=pd.DataFrame([])
all_monthly_do_rcp85_3=pd.DataFrame([])
all_monthly_do_rcp85_4=pd.DataFrame([])
all_monthly_do_rcp85_5=pd.DataFrame([])
all_monthly_do_rcp85_6=pd.DataFrame([])
all_monthly_do_rcp85_7=pd.DataFrame([])
all_monthly_do_rcp85_8=pd.DataFrame([])
all_monthly_do_rcp85_9=pd.DataFrame([])
all_monthly_do_rcp85_10=pd.DataFrame([])
all_monthly_do_rcp85_11=pd.DataFrame([])
#gfdl

# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp85'

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
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the monthly_hypolimnetic_ave function
        result = monthly_hypolimnetic_ave(C, Vr, time_series )

        
        all_monthly_do_rcp85_0 = pd.concat([all_monthly_do_rcp85_0 , result.iloc[:, 0]], axis=1)
        all_monthly_do_rcp85_1 = pd.concat([all_monthly_do_rcp85_1 , result.iloc[:, 1]], axis=1)
        all_monthly_do_rcp85_2 = pd.concat([all_monthly_do_rcp85_2 , result.iloc[:, 2]], axis=1)
        all_monthly_do_rcp85_3 = pd.concat([all_monthly_do_rcp85_3 , result.iloc[:, 3]], axis=1)
        all_monthly_do_rcp85_4 = pd.concat([all_monthly_do_rcp85_4 , result.iloc[:, 4]], axis=1)
        all_monthly_do_rcp85_5 = pd.concat([all_monthly_do_rcp85_5 , result.iloc[:, 5]], axis=1)
        all_monthly_do_rcp85_6 = pd.concat([all_monthly_do_rcp85_6 , result.iloc[:, 6]], axis=1)
        all_monthly_do_rcp85_7 = pd.concat([all_monthly_do_rcp85_7 , result.iloc[:, 7]], axis=1)
        all_monthly_do_rcp85_8 = pd.concat([all_monthly_do_rcp85_8 , result.iloc[:, 8]], axis=1)
        all_monthly_do_rcp85_9 = pd.concat([all_monthly_do_rcp85_9 , result.iloc[:, 9]], axis=1)
        all_monthly_do_rcp85_10 = pd.concat([all_monthly_do_rcp85_10 , result.iloc[:, 10]], axis=1)
        all_monthly_do_rcp85_11 = pd.concat([all_monthly_do_rcp85_11 , result.iloc[:, 11]], axis=1)



        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_hypolimnetic_ave_gfdl_rcp85_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, header=['monthly_hypolimnetic_ave'])
        
#hadgem               
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
        
        all_weights= np.append(all_weights , weights) 
        
        
        
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the monthly_hypolimnetic_ave function
        result = monthly_hypolimnetic_ave(C, Vr, time_series )

        
        all_monthly_do_rcp85_0 = pd.concat([all_monthly_do_rcp85_0 , result.iloc[:, 0]], axis=1)
        all_monthly_do_rcp85_1 = pd.concat([all_monthly_do_rcp85_1 , result.iloc[:, 1]], axis=1)
        all_monthly_do_rcp85_2 = pd.concat([all_monthly_do_rcp85_2 , result.iloc[:, 2]], axis=1)
        all_monthly_do_rcp85_3 = pd.concat([all_monthly_do_rcp85_3 , result.iloc[:, 3]], axis=1)
        all_monthly_do_rcp85_4 = pd.concat([all_monthly_do_rcp85_4 , result.iloc[:, 4]], axis=1)
        all_monthly_do_rcp85_5 = pd.concat([all_monthly_do_rcp85_5 , result.iloc[:, 5]], axis=1)
        all_monthly_do_rcp85_6 = pd.concat([all_monthly_do_rcp85_6 , result.iloc[:, 6]], axis=1)
        all_monthly_do_rcp85_7 = pd.concat([all_monthly_do_rcp85_7 , result.iloc[:, 7]], axis=1)
        all_monthly_do_rcp85_8 = pd.concat([all_monthly_do_rcp85_8 , result.iloc[:, 8]], axis=1)
        all_monthly_do_rcp85_9 = pd.concat([all_monthly_do_rcp85_9 , result.iloc[:, 9]], axis=1)
        all_monthly_do_rcp85_10 = pd.concat([all_monthly_do_rcp85_10 , result.iloc[:, 10]], axis=1)
        all_monthly_do_rcp85_11 = pd.concat([all_monthly_do_rcp85_11 , result.iloc[:, 11]], axis=1)



        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_hypolimnetic_ave_hadgem_rcp85_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, header=['monthly_hypolimnetic_ave'])
      
#ipsl       
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
        
        all_weights= np.append(all_weights , weights) 
        
        
        
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the monthly_hypolimnetic_ave function
        result = monthly_hypolimnetic_ave(C, Vr, time_series )

        
        all_monthly_do_rcp85_0 = pd.concat([all_monthly_do_rcp85_0 , result.iloc[:, 0]], axis=1)
        all_monthly_do_rcp85_1 = pd.concat([all_monthly_do_rcp85_1 , result.iloc[:, 1]], axis=1)
        all_monthly_do_rcp85_2 = pd.concat([all_monthly_do_rcp85_2 , result.iloc[:, 2]], axis=1)
        all_monthly_do_rcp85_3 = pd.concat([all_monthly_do_rcp85_3 , result.iloc[:, 3]], axis=1)
        all_monthly_do_rcp85_4 = pd.concat([all_monthly_do_rcp85_4 , result.iloc[:, 4]], axis=1)
        all_monthly_do_rcp85_5 = pd.concat([all_monthly_do_rcp85_5 , result.iloc[:, 5]], axis=1)
        all_monthly_do_rcp85_6 = pd.concat([all_monthly_do_rcp85_6 , result.iloc[:, 6]], axis=1)
        all_monthly_do_rcp85_7 = pd.concat([all_monthly_do_rcp85_7 , result.iloc[:, 7]], axis=1)
        all_monthly_do_rcp85_8 = pd.concat([all_monthly_do_rcp85_8 , result.iloc[:, 8]], axis=1)
        all_monthly_do_rcp85_9 = pd.concat([all_monthly_do_rcp85_9 , result.iloc[:, 9]], axis=1)
        all_monthly_do_rcp85_10 = pd.concat([all_monthly_do_rcp85_10 , result.iloc[:, 10]], axis=1)
        all_monthly_do_rcp85_11 = pd.concat([all_monthly_do_rcp85_11 , result.iloc[:, 11]], axis=1)



        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_hypolimnetic_ave_ipsl_rcp85_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, header=['monthly_hypolimnetic_ave'])
        

#miroc       
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
        
        all_weights= np.append(all_weights , weights) 
        
        
        
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the monthly_hypolimnetic_ave function
        result = monthly_hypolimnetic_ave(C, Vr, time_series )

        
        all_monthly_do_rcp85_0 = pd.concat([all_monthly_do_rcp85_0 , result.iloc[:, 0]], axis=1)
        all_monthly_do_rcp85_1 = pd.concat([all_monthly_do_rcp85_1 , result.iloc[:, 1]], axis=1)
        all_monthly_do_rcp85_2 = pd.concat([all_monthly_do_rcp85_2 , result.iloc[:, 2]], axis=1)
        all_monthly_do_rcp85_3 = pd.concat([all_monthly_do_rcp85_3 , result.iloc[:, 3]], axis=1)
        all_monthly_do_rcp85_4 = pd.concat([all_monthly_do_rcp85_4 , result.iloc[:, 4]], axis=1)
        all_monthly_do_rcp85_5 = pd.concat([all_monthly_do_rcp85_5 , result.iloc[:, 5]], axis=1)
        all_monthly_do_rcp85_6 = pd.concat([all_monthly_do_rcp85_6 , result.iloc[:, 6]], axis=1)
        all_monthly_do_rcp85_7 = pd.concat([all_monthly_do_rcp85_7 , result.iloc[:, 7]], axis=1)
        all_monthly_do_rcp85_8 = pd.concat([all_monthly_do_rcp85_8 , result.iloc[:, 8]], axis=1)
        all_monthly_do_rcp85_9 = pd.concat([all_monthly_do_rcp85_9 , result.iloc[:, 9]], axis=1)
        all_monthly_do_rcp85_10 = pd.concat([all_monthly_do_rcp85_10 , result.iloc[:, 10]], axis=1)
        all_monthly_do_rcp85_11 = pd.concat([all_monthly_do_rcp85_11 , result.iloc[:, 11]], axis=1)



        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_hypolimnetic_ave_miroc_rcp85_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, header=['monthly_hypolimnetic_ave'])
        



#%%

all_monthly_do_rcp85_0 = all_monthly_do_rcp85_0.rename_axis('Datetime')
all_monthly_do_rcp85_1 = all_monthly_do_rcp85_1.rename_axis('Datetime')
all_monthly_do_rcp85_2 = all_monthly_do_rcp85_2.rename_axis('Datetime')
all_monthly_do_rcp85_3 = all_monthly_do_rcp85_3.rename_axis('Datetime')
all_monthly_do_rcp85_4 = all_monthly_do_rcp85_4.rename_axis('Datetime')
all_monthly_do_rcp85_5 = all_monthly_do_rcp85_5.rename_axis('Datetime')
all_monthly_do_rcp85_6 = all_monthly_do_rcp85_6.rename_axis('Datetime')
all_monthly_do_rcp85_7 = all_monthly_do_rcp85_7.rename_axis('Datetime')
all_monthly_do_rcp85_8 = all_monthly_do_rcp85_8.rename_axis('Datetime')
all_monthly_do_rcp85_9 = all_monthly_do_rcp85_9.rename_axis('Datetime')
all_monthly_do_rcp85_10 = all_monthly_do_rcp85_10.rename_axis('Datetime')
all_monthly_do_rcp85_11 = all_monthly_do_rcp85_11.rename_axis('Datetime')

#%%Uncertainity partitioning on all_monthly_do_rcp85

anova_monthly_do_rcp85_0=annova_uncertainity(all_monthly_do_rcp85_0)

anova_monthly_do_rcp85_0.describe().loc['mean', :]
"""
GCMs           1.000000e+02
param          2.563458e-25
interaction    4.631951e-16
GCMs/param              inf
year           2.052500e+03
Name: mean, dtype: float64
"""

anova_monthly_do_rcp85_1=annova_uncertainity(all_monthly_do_rcp85_1)

anova_monthly_do_rcp85_1.describe().loc['mean', :]
"""
GCMs           1.000000e+02
param          6.839876e-24
interaction    7.887759e-17
GCMs/param              inf
year           2.052500e+03
Name: mean, dtype: float64
"""

anova_monthly_do_rcp85_2=annova_uncertainity(all_monthly_do_rcp85_2)

anova_monthly_do_rcp85_2.describe().loc['mean', :]
"""
GCMs           1.000000e+02
param          4.706030e-07
interaction    1.411809e-06
GCMs/param              inf
year           2.052500e+03
Name: mean, dtype: float64
"""
#March 
anova_monthly_do_rcp85_3=annova_uncertainity(all_monthly_do_rcp85_3)

anova_monthly_do_rcp85_3.describe().loc['mean', :]
"""
GCMs           9.945727e+01
param          2.648133e-01
interaction    2.779212e-01
GCMs/param     1.498066e+26
year           2.052500e+03
Name: mean, dtype: float64
"""
anova_monthly_do_rcp85_3.describe().loc['std', :]
"""
GCMs           8.543255e-01
param          4.563303e-01
interaction    4.465510e-01
GCMs/param     1.143307e+27
year           2.727942e+01
Name: std, dtype: float64
"""
anova_monthly_do_rcp85_4=annova_uncertainity(all_monthly_do_rcp85_4)

anova_monthly_do_rcp85_4.describe().loc['mean', :]
"""
GCMs             87.274009
param            10.951089
interaction       1.774903
GCMs/param      837.467904
year           2052.500000
Name: mean, dtype: float64
"""

anova_monthly_do_rcp85_4.describe().loc['std', :]
"""
GCMs             15.189644
param            14.383059
interaction       1.511315
GCMs/param     7881.357360
year             27.279418
Name: std, dtype: float64
"""


anova_monthly_do_rcp85_5=annova_uncertainity(all_monthly_do_rcp85_5)

anova_monthly_do_rcp85_5.describe().loc['mean', :]
"""
GCMs             69.15327
param            29.71097
interaction       1.13576
GCMs/param        5.46217
year           2052.50000
Name: mean, dtype: float64
"""


anova_monthly_do_rcp85_5.describe().loc['std', :]

"""
GCMs           22.602448
param          21.948932
interaction     2.291045
GCMs/param      6.392812
year           27.279418
Name: std, dtype: float64

"""
anova_monthly_do_rcp85_6=annova_uncertainity(all_monthly_do_rcp85_6)

anova_monthly_do_rcp85_6.describe().loc['mean', :]
"""
GCMs             52.059745
param            37.304405
interaction      10.635850
GCMs/param        3.579564
year           2052.500000
Name: mean, dtype: float64
"""


anova_monthly_do_rcp85_6.describe().loc['std', :]
"""
GCMs           23.766289
param          21.848560
interaction     9.612972
GCMs/param      7.297067
year           27.279418
Name: std, dtype: float64
"""
anova_monthly_do_rcp85_7=annova_uncertainity(all_monthly_do_rcp85_7)

anova_monthly_do_rcp85_7.describe().loc['mean', :]
"""
GCMs             92.177818
param             2.807112
interaction       5.015070
GCMs/param             inf
year           2052.500000
Name: mean, dtype: float64
"""


anova_monthly_do_rcp85_7.describe().loc['std', :]
"""
GCMs           23.361870
param           9.026550
interaction    15.445162
GCMs/param           NaN
year           27.279418
Name: std, dtype: float64
"""

anova_monthly_do_rcp85_8=annova_uncertainity(all_monthly_do_rcp85_8)

anova_monthly_do_rcp85_8.describe().loc['mean', :]
"""
GCMs           1.000000e+02
param          1.230210e-27
interaction   -4.438619e-16
GCMs/param              inf
year           2.052500e+03
Name: mean, dtype: float64
"""


anova_monthly_do_rcp85_8.describe().loc['std', :]
"""
GCMs           2.145590e-14
param          4.386726e-27
interaction    1.617391e-14
GCMs/param              NaN
year           2.727942e+01
Name: std, dtype: float64
"""

anova_monthly_do_rcp85_9=annova_uncertainity(all_monthly_do_rcp85_9)

anova_monthly_do_rcp85_9.describe().loc['mean', :]
"""
GCMs           1.000000e+02
param          2.645254e-25
interaction   -8.584870e-16
GCMs/param              inf
year           2.052500e+03
Name: mean, dtype: float64
"""



anova_monthly_do_rcp85_10=annova_uncertainity(all_monthly_do_rcp85_10)

anova_monthly_do_rcp85_10.describe().loc['mean', :]
"""
GCMs           1.000000e+02
param          1.459178e-25
interaction   -1.184275e-15
GCMs/param              inf
year           2.052500e+03
Name: mean, dtype: float64
"""

anova_monthly_do_rcp85_11=annova_uncertainity(all_monthly_do_rcp85_11)

anova_monthly_do_rcp85_11.describe().loc['mean', :]
"""
GCMs           1.000000e+02
param          1.740563e-25
interaction    1.136179e-15
GCMs/param              inf
year           2.052500e+03
Name: mean, dtype: float64
"""




#%% GLUE method on all_monthly_do_rcp85 for each depth 
          
#month 0 : jan

# monthly anoxic duration  
timeseries_year_rcp85= all_monthly_do_rcp85_0.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_monthly_do_rcp85_0.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights))

# Build glue df
glue_df_monthly_0_hypolimnetic_ave_rcp85 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_df_monthly_0_hypolimnetic_ave_rcp85=glue_df_monthly_0_hypolimnetic_ave_rcp85.set_index(timeseries_year_rcp85)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory
glue_df_monthly_0_hypolimnetic_ave_rcp85.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/rcp85/glue_jan_hypolimnetic_ave_rcp85.csv')
        
#%%month feb

# monthly anoxic duration  
timeseries_year_rcp85= all_monthly_do_rcp85_1.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_monthly_do_rcp85_1.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights))

# Build glue df
glue_df_monthly_1_hypolimnetic_ave_rcp85 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_df_monthly_1_hypolimnetic_ave_rcp85=glue_df_monthly_1_hypolimnetic_ave_rcp85.set_index(timeseries_year_rcp85)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory
glue_df_monthly_1_hypolimnetic_ave_rcp85.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/rcp85/glue_feb_hypolimnetic_ave_rcp85.csv')
        

#%%month mar

# monthly anoxic duration  
timeseries_year_rcp85= all_monthly_do_rcp85_2.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_monthly_do_rcp85_2.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights))

# Build glue df
glue_df_monthly_2_hypolimnetic_ave_rcp85 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_df_monthly_2_hypolimnetic_ave_rcp85=glue_df_monthly_2_hypolimnetic_ave_rcp85.set_index(timeseries_year_rcp85)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory
glue_df_monthly_2_hypolimnetic_ave_rcp85.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/rcp85/glue_mar_hypolimnetic_ave_rcp85.csv')
        


#%%month apr

# monthly anoxic duration  
timeseries_year_rcp85= all_monthly_do_rcp85_3.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_monthly_do_rcp85_3.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights))

# Build glue df
glue_df_monthly_3_hypolimnetic_ave_rcp85 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_df_monthly_3_hypolimnetic_ave_rcp85=glue_df_monthly_3_hypolimnetic_ave_rcp85.set_index(timeseries_year_rcp85)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory
glue_df_monthly_3_hypolimnetic_ave_rcp85.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/rcp85/glue_apr_hypolimnetic_ave_rcp85.csv')
        


#%%month may

# monthly anoxic duration  
timeseries_year_rcp85= all_monthly_do_rcp85_4.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_monthly_do_rcp85_4.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights))

# Build glue df
glue_df_monthly_4_hypolimnetic_ave_rcp85 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_df_monthly_4_hypolimnetic_ave_rcp85=glue_df_monthly_4_hypolimnetic_ave_rcp85.set_index(timeseries_year_rcp85)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory
glue_df_monthly_4_hypolimnetic_ave_rcp85.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/rcp85/glue_may_hypolimnetic_ave_rcp85.csv')
        

#%%month jun

# monthly anoxic duration  
timeseries_year_rcp85= all_monthly_do_rcp85_5.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_monthly_do_rcp85_5.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights))

# Build glue df
glue_df_monthly_5_hypolimnetic_ave_rcp85 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_df_monthly_5_hypolimnetic_ave_rcp85=glue_df_monthly_5_hypolimnetic_ave_rcp85.set_index(timeseries_year_rcp85)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory
glue_df_monthly_5_hypolimnetic_ave_rcp85.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/rcp85/glue_jun_hypolimnetic_ave_rcp85.csv')
        


#%%month jul

# monthly anoxic duration  
timeseries_year_rcp85= all_monthly_do_rcp85_6.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_monthly_do_rcp85_6.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights))

# Build glue df
glue_df_monthly_6_hypolimnetic_ave_rcp85 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_df_monthly_6_hypolimnetic_ave_rcp85=glue_df_monthly_6_hypolimnetic_ave_rcp85.set_index(timeseries_year_rcp85)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory
glue_df_monthly_6_hypolimnetic_ave_rcp85.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/rcp85/glue_jul_hypolimnetic_ave_rcp85.csv')
        


#%%month aug

# monthly anoxic duration  
timeseries_year_rcp85= all_monthly_do_rcp85_7.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_monthly_do_rcp85_7.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights))

# Build glue df
glue_df_monthly_7_hypolimnetic_ave_rcp85 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_df_monthly_7_hypolimnetic_ave_rcp85=glue_df_monthly_7_hypolimnetic_ave_rcp85.set_index(timeseries_year_rcp85)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory
glue_df_monthly_7_hypolimnetic_ave_rcp85.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/rcp85/glue_aug_hypolimnetic_ave_rcp85.csv')
        


#%%month sep

# monthly anoxic duration  
timeseries_year_rcp85= all_monthly_do_rcp85_8.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_monthly_do_rcp85_8.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights))

# Build glue df
glue_df_monthly_8_hypolimnetic_ave_rcp85 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_df_monthly_8_hypolimnetic_ave_rcp85=glue_df_monthly_8_hypolimnetic_ave_rcp85.set_index(timeseries_year_rcp85)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory
glue_df_monthly_8_hypolimnetic_ave_rcp85.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/rcp85/glue_sep_hypolimnetic_ave_rcp85.csv')
        


#%%month oct

# monthly anoxic duration  
timeseries_year_rcp85= all_monthly_do_rcp85_9.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_monthly_do_rcp85_9.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights))

# Build glue df
glue_df_monthly_9_hypolimnetic_ave_rcp85 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_df_monthly_9_hypolimnetic_ave_rcp85=glue_df_monthly_9_hypolimnetic_ave_rcp85.set_index(timeseries_year_rcp85)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory
glue_df_monthly_9_hypolimnetic_ave_rcp85.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/rcp85/glue_oct_hypolimnetic_ave_rcp85.csv')
        

#%%month nov

# monthly anoxic duration  
timeseries_year_rcp85= all_monthly_do_rcp85_10.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_monthly_do_rcp85_10.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights))

# Build glue df
glue_df_monthly_10_hypolimnetic_ave_rcp85 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_df_monthly_10_hypolimnetic_ave_rcp85=glue_df_monthly_10_hypolimnetic_ave_rcp85.set_index(timeseries_year_rcp85)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory
glue_df_monthly_10_hypolimnetic_ave_rcp85.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/rcp85/glue_nov_hypolimnetic_ave_rcp85.csv')
        

#%%month dec

# monthly anoxic duration  
timeseries_year_rcp85= all_monthly_do_rcp85_11.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_monthly_do_rcp85_11.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights))

# Build glue df
glue_df_monthly_11_hypolimnetic_ave_rcp85 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_df_monthly_11_hypolimnetic_ave_rcp85=glue_df_monthly_11_hypolimnetic_ave_rcp85.set_index(timeseries_year_rcp85)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory
glue_df_monthly_11_hypolimnetic_ave_rcp85.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/rcp85/glue_dec_hypolimnetic_ave_rcp85.csv')
        

#%%Subseting all months for:
    
# baseline [1976-2005]


glue_df_monthly_0_hypolimnetic_ave_his_baseline=glue_df_monthly_0_hypolimnetic_ave_his[glue_df_monthly_0_hypolimnetic_ave_his.index>1975]

glue_df_monthly_0_hypolimnetic_ave_his_baseline['50%'].mean()
#14.599659441389198


glue_df_monthly_1_hypolimnetic_ave_his_baseline=glue_df_monthly_1_hypolimnetic_ave_his[glue_df_monthly_1_hypolimnetic_ave_his.index>1975]

glue_df_monthly_1_hypolimnetic_ave_his_baseline['50%'].mean()
#14.614558546395328


glue_df_monthly_2_hypolimnetic_ave_his_baseline=glue_df_monthly_2_hypolimnetic_ave_his[glue_df_monthly_2_hypolimnetic_ave_his.index>1975]

glue_df_monthly_2_hypolimnetic_ave_his_baseline['50%'].mean()
#14.462144638100522




glue_df_monthly_3_hypolimnetic_ave_his_baseline=glue_df_monthly_3_hypolimnetic_ave_his[glue_df_monthly_3_hypolimnetic_ave_his.index>1975]

glue_df_monthly_3_hypolimnetic_ave_his_baseline['50%'].mean()
#13.497100432299748



glue_df_monthly_4_hypolimnetic_ave_his_baseline=glue_df_monthly_4_hypolimnetic_ave_his[glue_df_monthly_4_hypolimnetic_ave_his.index>1975]

glue_df_monthly_4_hypolimnetic_ave_his_baseline['50%'].mean()
#11.521502499739341




glue_df_monthly_5_hypolimnetic_ave_his_baseline=glue_df_monthly_5_hypolimnetic_ave_his[glue_df_monthly_5_hypolimnetic_ave_his.index>1975]

glue_df_monthly_5_hypolimnetic_ave_his_baseline['50%'].mean()
#7.590215123145209



glue_df_monthly_6_hypolimnetic_ave_his_baseline=glue_df_monthly_6_hypolimnetic_ave_his[glue_df_monthly_6_hypolimnetic_ave_his.index>1975]

glue_df_monthly_6_hypolimnetic_ave_his_baseline['50%'].mean()
#2.4542480551858303




glue_df_monthly_7_hypolimnetic_ave_his_baseline=glue_df_monthly_7_hypolimnetic_ave_his[glue_df_monthly_7_hypolimnetic_ave_his.index>1975]

glue_df_monthly_7_hypolimnetic_ave_his_baseline['50%'].mean()
#0.8281325816676314


glue_df_monthly_8_hypolimnetic_ave_his_baseline=glue_df_monthly_8_hypolimnetic_ave_his[glue_df_monthly_8_hypolimnetic_ave_his.index>1975]

glue_df_monthly_8_hypolimnetic_ave_his_baseline['50%'].mean()
#9.245528035915298


glue_df_monthly_9_hypolimnetic_ave_his_baseline=glue_df_monthly_9_hypolimnetic_ave_his[glue_df_monthly_9_hypolimnetic_ave_his.index>1975]

glue_df_monthly_9_hypolimnetic_ave_his_baseline['50%'].mean()
#11.389365036711101


glue_df_monthly_10_hypolimnetic_ave_his_baseline=glue_df_monthly_10_hypolimnetic_ave_his[glue_df_monthly_10_hypolimnetic_ave_his.index>1975]

glue_df_monthly_10_hypolimnetic_ave_his_baseline['50%'].mean()
#12.877935426720995


glue_df_monthly_11_hypolimnetic_ave_his_baseline=glue_df_monthly_11_hypolimnetic_ave_his[glue_df_monthly_11_hypolimnetic_ave_his.index>1975]

glue_df_monthly_11_hypolimnetic_ave_his_baseline['50%'].mean()
#14.253560719275978 mg L-1


#%%near future [2030-2059]

#RCP26
glue_df_monthly_0_hypolimnetic_ave_rcp26_nearfu=glue_df_monthly_0_hypolimnetic_ave_rcp26[(glue_df_monthly_0_hypolimnetic_ave_rcp26.index>2029) & (glue_df_monthly_0_hypolimnetic_ave_rcp26.index<2060)]

glue_df_monthly_0_hypolimnetic_ave_rcp26_nearfu['50%'].mean()
#14.389255719652068

glue_df_monthly_1_hypolimnetic_ave_rcp26_nearfu=glue_df_monthly_1_hypolimnetic_ave_rcp26[(glue_df_monthly_1_hypolimnetic_ave_rcp26.index>2029) & (glue_df_monthly_1_hypolimnetic_ave_rcp26.index<2060)]

glue_df_monthly_1_hypolimnetic_ave_rcp26_nearfu['50%'].mean()
#14.539021624001757

glue_df_monthly_2_hypolimnetic_ave_rcp26_nearfu=glue_df_monthly_2_hypolimnetic_ave_rcp26[(glue_df_monthly_2_hypolimnetic_ave_rcp26.index>2029) & (glue_df_monthly_2_hypolimnetic_ave_rcp26.index<2060)]

glue_df_monthly_2_hypolimnetic_ave_rcp26_nearfu['50%'].mean()
#14.277546216106904

glue_df_monthly_3_hypolimnetic_ave_rcp26_nearfu=glue_df_monthly_3_hypolimnetic_ave_rcp26[(glue_df_monthly_3_hypolimnetic_ave_rcp26.index>2029) & (glue_df_monthly_3_hypolimnetic_ave_rcp26.index<2060)]

glue_df_monthly_3_hypolimnetic_ave_rcp26_nearfu['50%'].mean()
#13.076462054856977

glue_df_monthly_4_hypolimnetic_ave_rcp26_nearfu=glue_df_monthly_4_hypolimnetic_ave_rcp26[(glue_df_monthly_4_hypolimnetic_ave_rcp26.index>2029) & (glue_df_monthly_4_hypolimnetic_ave_rcp26.index<2060)]

glue_df_monthly_4_hypolimnetic_ave_rcp26_nearfu['50%'].mean()
#10.496357930632943

glue_df_monthly_5_hypolimnetic_ave_rcp26_nearfu=glue_df_monthly_5_hypolimnetic_ave_rcp26[(glue_df_monthly_5_hypolimnetic_ave_rcp26.index>2029) & (glue_df_monthly_5_hypolimnetic_ave_rcp26.index<2060)]

glue_df_monthly_5_hypolimnetic_ave_rcp26_nearfu['50%'].mean()
#6.210267069245595


glue_df_monthly_6_hypolimnetic_ave_rcp26_nearfu=glue_df_monthly_6_hypolimnetic_ave_rcp26[(glue_df_monthly_6_hypolimnetic_ave_rcp26.index>2029) & (glue_df_monthly_6_hypolimnetic_ave_rcp26.index<2060)]

glue_df_monthly_6_hypolimnetic_ave_rcp26_nearfu['50%'].mean()
#1.179493251464825


glue_df_monthly_7_hypolimnetic_ave_rcp26_nearfu=glue_df_monthly_7_hypolimnetic_ave_rcp26[(glue_df_monthly_7_hypolimnetic_ave_rcp26.index>2029) & (glue_df_monthly_7_hypolimnetic_ave_rcp26.index<2060)]

glue_df_monthly_7_hypolimnetic_ave_rcp26_nearfu['50%'].mean()
#0.13711425120822002

glue_df_monthly_8_hypolimnetic_ave_rcp26_nearfu=glue_df_monthly_8_hypolimnetic_ave_rcp26[(glue_df_monthly_8_hypolimnetic_ave_rcp26.index>2029) & (glue_df_monthly_8_hypolimnetic_ave_rcp26.index<2060)]

glue_df_monthly_8_hypolimnetic_ave_rcp26_nearfu['50%'].mean()
#8.219190889617765

glue_df_monthly_9_hypolimnetic_ave_rcp26_nearfu=glue_df_monthly_9_hypolimnetic_ave_rcp26[(glue_df_monthly_9_hypolimnetic_ave_rcp26.index>2029) & (glue_df_monthly_9_hypolimnetic_ave_rcp26.index<2060)]

glue_df_monthly_9_hypolimnetic_ave_rcp26_nearfu['50%'].mean()
#10.980044868441238

glue_df_monthly_10_hypolimnetic_ave_rcp26_nearfu=glue_df_monthly_10_hypolimnetic_ave_rcp26[(glue_df_monthly_10_hypolimnetic_ave_rcp26.index>2029) & (glue_df_monthly_10_hypolimnetic_ave_rcp26.index<2060)]

glue_df_monthly_10_hypolimnetic_ave_rcp26_nearfu['50%'].mean()
#12.368126799052328

glue_df_monthly_11_hypolimnetic_ave_rcp26_nearfu=glue_df_monthly_11_hypolimnetic_ave_rcp26[(glue_df_monthly_11_hypolimnetic_ave_rcp26.index>2029) & (glue_df_monthly_11_hypolimnetic_ave_rcp26.index<2060)]

glue_df_monthly_11_hypolimnetic_ave_rcp26_nearfu['50%'].mean()
#13.723982813902063


#%%near future [2030-2059]

#RCP60
glue_df_monthly_0_hypolimnetic_ave_rcp60_nearfu=glue_df_monthly_0_hypolimnetic_ave_rcp60[(glue_df_monthly_0_hypolimnetic_ave_rcp60.index>2029) & (glue_df_monthly_0_hypolimnetic_ave_rcp60.index<2060)]

glue_df_monthly_0_hypolimnetic_ave_rcp60_nearfu['50%'].mean()
#14.364807543447869

glue_df_monthly_1_hypolimnetic_ave_rcp60_nearfu=glue_df_monthly_1_hypolimnetic_ave_rcp60[(glue_df_monthly_1_hypolimnetic_ave_rcp60.index>2029) & (glue_df_monthly_1_hypolimnetic_ave_rcp60.index<2060)]

glue_df_monthly_1_hypolimnetic_ave_rcp60_nearfu['50%'].mean()
#14.522563690362126

glue_df_monthly_2_hypolimnetic_ave_rcp60_nearfu=glue_df_monthly_2_hypolimnetic_ave_rcp60[(glue_df_monthly_2_hypolimnetic_ave_rcp60.index>2029) & (glue_df_monthly_2_hypolimnetic_ave_rcp60.index<2060)]

glue_df_monthly_2_hypolimnetic_ave_rcp60_nearfu['50%'].mean()
#14.28625405435156

glue_df_monthly_3_hypolimnetic_ave_rcp60_nearfu=glue_df_monthly_3_hypolimnetic_ave_rcp60[(glue_df_monthly_3_hypolimnetic_ave_rcp60.index>2029) & (glue_df_monthly_3_hypolimnetic_ave_rcp60.index<2060)]

glue_df_monthly_3_hypolimnetic_ave_rcp60_nearfu['50%'].mean()
#13.146479933210825

glue_df_monthly_4_hypolimnetic_ave_rcp60_nearfu=glue_df_monthly_4_hypolimnetic_ave_rcp60[(glue_df_monthly_4_hypolimnetic_ave_rcp60.index>2029) & (glue_df_monthly_4_hypolimnetic_ave_rcp60.index<2060)]

glue_df_monthly_4_hypolimnetic_ave_rcp60_nearfu['50%'].mean()
#10.561755110486375

glue_df_monthly_5_hypolimnetic_ave_rcp60_nearfu=glue_df_monthly_5_hypolimnetic_ave_rcp60[(glue_df_monthly_5_hypolimnetic_ave_rcp60.index>2029) & (glue_df_monthly_5_hypolimnetic_ave_rcp60.index<2060)]

glue_df_monthly_5_hypolimnetic_ave_rcp60_nearfu['50%'].mean()
#5.921148325262593


glue_df_monthly_6_hypolimnetic_ave_rcp60_nearfu=glue_df_monthly_6_hypolimnetic_ave_rcp60[(glue_df_monthly_6_hypolimnetic_ave_rcp60.index>2029) & (glue_df_monthly_6_hypolimnetic_ave_rcp60.index<2060)]

glue_df_monthly_6_hypolimnetic_ave_rcp60_nearfu['50%'].mean()
#0.9090992617373232


glue_df_monthly_7_hypolimnetic_ave_rcp60_nearfu=glue_df_monthly_7_hypolimnetic_ave_rcp60[(glue_df_monthly_7_hypolimnetic_ave_rcp60.index>2029) & (glue_df_monthly_7_hypolimnetic_ave_rcp60.index<2060)]

glue_df_monthly_7_hypolimnetic_ave_rcp60_nearfu['50%'].mean()
#0.27285077517110634

glue_df_monthly_8_hypolimnetic_ave_rcp60_nearfu=glue_df_monthly_8_hypolimnetic_ave_rcp60[(glue_df_monthly_8_hypolimnetic_ave_rcp60.index>2029) & (glue_df_monthly_8_hypolimnetic_ave_rcp60.index<2060)]

glue_df_monthly_8_hypolimnetic_ave_rcp60_nearfu['50%'].mean()
#8.678824899363546

glue_df_monthly_9_hypolimnetic_ave_rcp60_nearfu=glue_df_monthly_9_hypolimnetic_ave_rcp60[(glue_df_monthly_9_hypolimnetic_ave_rcp60.index>2029) & (glue_df_monthly_9_hypolimnetic_ave_rcp60.index<2060)]

glue_df_monthly_9_hypolimnetic_ave_rcp60_nearfu['50%'].mean()
#10.969570510202853

glue_df_monthly_10_hypolimnetic_ave_rcp60_nearfu=glue_df_monthly_10_hypolimnetic_ave_rcp60[(glue_df_monthly_10_hypolimnetic_ave_rcp60.index>2029) & (glue_df_monthly_10_hypolimnetic_ave_rcp60.index<2060)]

glue_df_monthly_10_hypolimnetic_ave_rcp60_nearfu['50%'].mean()
# 12.41026870026796

glue_df_monthly_11_hypolimnetic_ave_rcp60_nearfu=glue_df_monthly_11_hypolimnetic_ave_rcp60[(glue_df_monthly_11_hypolimnetic_ave_rcp60.index>2029) & (glue_df_monthly_11_hypolimnetic_ave_rcp60.index<2060)]

glue_df_monthly_11_hypolimnetic_ave_rcp60_nearfu['50%'].mean()
#13.775422979714802

#%%near future [2030-2059]

#RCP85
glue_df_monthly_0_hypolimnetic_ave_rcp85_nearfu=glue_df_monthly_0_hypolimnetic_ave_rcp85[(glue_df_monthly_0_hypolimnetic_ave_rcp85.index>2029) & (glue_df_monthly_0_hypolimnetic_ave_rcp85.index<2060)]

glue_df_monthly_0_hypolimnetic_ave_rcp85_nearfu['50%'].mean()
#14.259631106209595

glue_df_monthly_1_hypolimnetic_ave_rcp85_nearfu=glue_df_monthly_1_hypolimnetic_ave_rcp85[(glue_df_monthly_1_hypolimnetic_ave_rcp85.index>2029) & (glue_df_monthly_1_hypolimnetic_ave_rcp85.index<2060)]

glue_df_monthly_1_hypolimnetic_ave_rcp85_nearfu['50%'].mean()
#14.42750210295078

glue_df_monthly_2_hypolimnetic_ave_rcp85_nearfu=glue_df_monthly_2_hypolimnetic_ave_rcp85[(glue_df_monthly_2_hypolimnetic_ave_rcp85.index>2029) & (glue_df_monthly_2_hypolimnetic_ave_rcp85.index<2060)]

glue_df_monthly_2_hypolimnetic_ave_rcp85_nearfu['50%'].mean()
#14.169809551113804

glue_df_monthly_3_hypolimnetic_ave_rcp85_nearfu=glue_df_monthly_3_hypolimnetic_ave_rcp85[(glue_df_monthly_3_hypolimnetic_ave_rcp85.index>2029) & (glue_df_monthly_3_hypolimnetic_ave_rcp85.index<2060)]

glue_df_monthly_3_hypolimnetic_ave_rcp85_nearfu['50%'].mean()
#12.953729168102036

glue_df_monthly_4_hypolimnetic_ave_rcp85_nearfu=glue_df_monthly_4_hypolimnetic_ave_rcp85[(glue_df_monthly_4_hypolimnetic_ave_rcp85.index>2029) & (glue_df_monthly_4_hypolimnetic_ave_rcp85.index<2060)]

glue_df_monthly_4_hypolimnetic_ave_rcp85_nearfu['50%'].mean()
#10.31301374970588

glue_df_monthly_5_hypolimnetic_ave_rcp85_nearfu=glue_df_monthly_5_hypolimnetic_ave_rcp85[(glue_df_monthly_5_hypolimnetic_ave_rcp85.index>2029) & (glue_df_monthly_5_hypolimnetic_ave_rcp85.index<2060)]

glue_df_monthly_5_hypolimnetic_ave_rcp85_nearfu['50%'].mean()
#5.63045749325675


glue_df_monthly_6_hypolimnetic_ave_rcp85_nearfu=glue_df_monthly_6_hypolimnetic_ave_rcp85[(glue_df_monthly_6_hypolimnetic_ave_rcp85.index>2029) & (glue_df_monthly_6_hypolimnetic_ave_rcp85.index<2085)]

glue_df_monthly_6_hypolimnetic_ave_rcp85_nearfu['50%'].mean()
#0.5456301829511836


glue_df_monthly_7_hypolimnetic_ave_rcp85_nearfu=glue_df_monthly_7_hypolimnetic_ave_rcp85[(glue_df_monthly_7_hypolimnetic_ave_rcp85.index>2029) & (glue_df_monthly_7_hypolimnetic_ave_rcp85.index<2060)]

glue_df_monthly_7_hypolimnetic_ave_rcp85_nearfu['50%'].mean()
#0.14267854774255123

glue_df_monthly_8_hypolimnetic_ave_rcp85_nearfu=glue_df_monthly_8_hypolimnetic_ave_rcp85[(glue_df_monthly_8_hypolimnetic_ave_rcp85.index>2029) & (glue_df_monthly_8_hypolimnetic_ave_rcp85.index<2060)]

glue_df_monthly_8_hypolimnetic_ave_rcp85_nearfu['50%'].mean()
#7.804183696633273
glue_df_monthly_9_hypolimnetic_ave_rcp85_nearfu=glue_df_monthly_9_hypolimnetic_ave_rcp85[(glue_df_monthly_9_hypolimnetic_ave_rcp85.index>2029) & (glue_df_monthly_9_hypolimnetic_ave_rcp85.index<2060)]

glue_df_monthly_9_hypolimnetic_ave_rcp85_nearfu['50%'].mean()
#10.847473216632602

glue_df_monthly_10_hypolimnetic_ave_rcp85_nearfu=glue_df_monthly_10_hypolimnetic_ave_rcp85[(glue_df_monthly_10_hypolimnetic_ave_rcp85.index>2029) & (glue_df_monthly_10_hypolimnetic_ave_rcp85.index<2060)]

glue_df_monthly_10_hypolimnetic_ave_rcp85_nearfu['50%'].mean()
#12.153424863321895

glue_df_monthly_11_hypolimnetic_ave_rcp85_nearfu=glue_df_monthly_11_hypolimnetic_ave_rcp85[(glue_df_monthly_11_hypolimnetic_ave_rcp85.index>2029) & (glue_df_monthly_11_hypolimnetic_ave_rcp85.index<2060)]

glue_df_monthly_11_hypolimnetic_ave_rcp85_nearfu['50%'].mean()
#13.554671563639907



#%%distant future [2070-2099]

#RCP26
glue_df_monthly_0_hypolimnetic_ave_rcp26_distantfu=glue_df_monthly_0_hypolimnetic_ave_rcp26[(glue_df_monthly_0_hypolimnetic_ave_rcp26.index>2069) & (glue_df_monthly_0_hypolimnetic_ave_rcp26.index<2100)]

glue_df_monthly_0_hypolimnetic_ave_rcp26_distantfu['50%'].mean()
#14.43540797483572

glue_df_monthly_1_hypolimnetic_ave_rcp26_distantfu=glue_df_monthly_1_hypolimnetic_ave_rcp26[(glue_df_monthly_1_hypolimnetic_ave_rcp26.index>2069) & (glue_df_monthly_1_hypolimnetic_ave_rcp26.index<2100)]

glue_df_monthly_1_hypolimnetic_ave_rcp26_distantfu['50%'].mean()
#14.534663769830868

glue_df_monthly_2_hypolimnetic_ave_rcp26_distantfu=glue_df_monthly_2_hypolimnetic_ave_rcp26[(glue_df_monthly_2_hypolimnetic_ave_rcp26.index>2069) & (glue_df_monthly_2_hypolimnetic_ave_rcp26.index<2100)]

glue_df_monthly_2_hypolimnetic_ave_rcp26_distantfu['50%'].mean()
#14.278747968022476

glue_df_monthly_3_hypolimnetic_ave_rcp26_distantfu=glue_df_monthly_3_hypolimnetic_ave_rcp26[(glue_df_monthly_3_hypolimnetic_ave_rcp26.index>2069) & (glue_df_monthly_3_hypolimnetic_ave_rcp26.index<2100)]

glue_df_monthly_3_hypolimnetic_ave_rcp26_distantfu['50%'].mean()
#13.114064906980133

glue_df_monthly_4_hypolimnetic_ave_rcp26_distantfu=glue_df_monthly_4_hypolimnetic_ave_rcp26[(glue_df_monthly_4_hypolimnetic_ave_rcp26.index>2069) & (glue_df_monthly_4_hypolimnetic_ave_rcp26.index<2100)]

glue_df_monthly_4_hypolimnetic_ave_rcp26_distantfu['50%'].mean()
#10.377417451006458

glue_df_monthly_5_hypolimnetic_ave_rcp26_distantfu=glue_df_monthly_5_hypolimnetic_ave_rcp26[(glue_df_monthly_5_hypolimnetic_ave_rcp26.index>2069) & (glue_df_monthly_5_hypolimnetic_ave_rcp26.index<2100)]

glue_df_monthly_5_hypolimnetic_ave_rcp26_distantfu['50%'].mean()
#6.271301146289508


glue_df_monthly_6_hypolimnetic_ave_rcp26_distantfu=glue_df_monthly_6_hypolimnetic_ave_rcp26[(glue_df_monthly_6_hypolimnetic_ave_rcp26.index>2069) & (glue_df_monthly_6_hypolimnetic_ave_rcp26.index<2100)]

glue_df_monthly_6_hypolimnetic_ave_rcp26_distantfu['50%'].mean()
#1.2537612649893248


glue_df_monthly_7_hypolimnetic_ave_rcp26_distantfu=glue_df_monthly_7_hypolimnetic_ave_rcp26[(glue_df_monthly_7_hypolimnetic_ave_rcp26.index>2069) & (glue_df_monthly_7_hypolimnetic_ave_rcp26.index<2100)]

glue_df_monthly_7_hypolimnetic_ave_rcp26_distantfu['50%'].mean()
#0.08201215855321435

glue_df_monthly_8_hypolimnetic_ave_rcp26_distantfu=glue_df_monthly_8_hypolimnetic_ave_rcp26[(glue_df_monthly_8_hypolimnetic_ave_rcp26.index>2069) & (glue_df_monthly_8_hypolimnetic_ave_rcp26.index<2100)]

glue_df_monthly_8_hypolimnetic_ave_rcp26_distantfu['50%'].mean()
#8.224446477713602

glue_df_monthly_9_hypolimnetic_ave_rcp26_distantfu=glue_df_monthly_9_hypolimnetic_ave_rcp26[(glue_df_monthly_9_hypolimnetic_ave_rcp26.index>2069) & (glue_df_monthly_9_hypolimnetic_ave_rcp26.index<2100)]

glue_df_monthly_9_hypolimnetic_ave_rcp26_distantfu['50%'].mean()
#11.010036855384127

glue_df_monthly_10_hypolimnetic_ave_rcp26_distantfu=glue_df_monthly_10_hypolimnetic_ave_rcp26[(glue_df_monthly_10_hypolimnetic_ave_rcp26.index>2069) & (glue_df_monthly_10_hypolimnetic_ave_rcp26.index<2100)]

glue_df_monthly_10_hypolimnetic_ave_rcp26_distantfu['50%'].mean()
#12.32507259928121

glue_df_monthly_11_hypolimnetic_ave_rcp26_distantfu=glue_df_monthly_11_hypolimnetic_ave_rcp26[(glue_df_monthly_11_hypolimnetic_ave_rcp26.index>2069) & (glue_df_monthly_11_hypolimnetic_ave_rcp26.index<2100)]

glue_df_monthly_11_hypolimnetic_ave_rcp26_distantfu['50%'].mean()
#13.73194775411505


#%%distant future [2070-2099]

#RCP60
glue_df_monthly_0_hypolimnetic_ave_rcp60_distantfu=glue_df_monthly_0_hypolimnetic_ave_rcp60[(glue_df_monthly_0_hypolimnetic_ave_rcp60.index>2069) & (glue_df_monthly_0_hypolimnetic_ave_rcp60.index<2100)]

glue_df_monthly_0_hypolimnetic_ave_rcp60_distantfu['50%'].mean()
#14.06997494023245

glue_df_monthly_1_hypolimnetic_ave_rcp60_distantfu=glue_df_monthly_1_hypolimnetic_ave_rcp60[(glue_df_monthly_1_hypolimnetic_ave_rcp60.index>2069) & (glue_df_monthly_1_hypolimnetic_ave_rcp60.index<2100)]

glue_df_monthly_1_hypolimnetic_ave_rcp60_distantfu['50%'].mean()
#14.283411216289313

glue_df_monthly_2_hypolimnetic_ave_rcp60_distantfu=glue_df_monthly_2_hypolimnetic_ave_rcp60[(glue_df_monthly_2_hypolimnetic_ave_rcp60.index>2069) & (glue_df_monthly_2_hypolimnetic_ave_rcp60.index<2100)]

glue_df_monthly_2_hypolimnetic_ave_rcp60_distantfu['50%'].mean()
#13.946094506856866

glue_df_monthly_3_hypolimnetic_ave_rcp60_distantfu=glue_df_monthly_3_hypolimnetic_ave_rcp60[(glue_df_monthly_3_hypolimnetic_ave_rcp60.index>2069) & (glue_df_monthly_3_hypolimnetic_ave_rcp60.index<2100)]

glue_df_monthly_3_hypolimnetic_ave_rcp60_distantfu['50%'].mean()
#12.736941912874393

glue_df_monthly_4_hypolimnetic_ave_rcp60_distantfu=glue_df_monthly_4_hypolimnetic_ave_rcp60[(glue_df_monthly_4_hypolimnetic_ave_rcp60.index>2069) & (glue_df_monthly_4_hypolimnetic_ave_rcp60.index<2100)]

glue_df_monthly_4_hypolimnetic_ave_rcp60_distantfu['50%'].mean()
#9.651783955994231

glue_df_monthly_5_hypolimnetic_ave_rcp60_distantfu=glue_df_monthly_5_hypolimnetic_ave_rcp60[(glue_df_monthly_5_hypolimnetic_ave_rcp60.index>2069) & (glue_df_monthly_5_hypolimnetic_ave_rcp60.index<2100)]

glue_df_monthly_5_hypolimnetic_ave_rcp60_distantfu['50%'].mean()
#4.812436686722321


glue_df_monthly_6_hypolimnetic_ave_rcp60_distantfu=glue_df_monthly_6_hypolimnetic_ave_rcp60[(glue_df_monthly_6_hypolimnetic_ave_rcp60.index>2069) & (glue_df_monthly_6_hypolimnetic_ave_rcp60.index<2100)]

glue_df_monthly_6_hypolimnetic_ave_rcp60_distantfu['50%'].mean()
#0.34991906568895464


glue_df_monthly_7_hypolimnetic_ave_rcp60_distantfu=glue_df_monthly_7_hypolimnetic_ave_rcp60[(glue_df_monthly_7_hypolimnetic_ave_rcp60.index>2069) & (glue_df_monthly_7_hypolimnetic_ave_rcp60.index<2100)]

glue_df_monthly_7_hypolimnetic_ave_rcp60_distantfu['50%'].mean()
#0.00017141281152630968

glue_df_monthly_8_hypolimnetic_ave_rcp60_distantfu=glue_df_monthly_8_hypolimnetic_ave_rcp60[(glue_df_monthly_8_hypolimnetic_ave_rcp60.index>2069) & (glue_df_monthly_8_hypolimnetic_ave_rcp60.index<2100)]

glue_df_monthly_8_hypolimnetic_ave_rcp60_distantfu['50%'].mean()
#6.761263436196113

glue_df_monthly_9_hypolimnetic_ave_rcp60_distantfu=glue_df_monthly_9_hypolimnetic_ave_rcp60[(glue_df_monthly_9_hypolimnetic_ave_rcp60.index>2069) & (glue_df_monthly_9_hypolimnetic_ave_rcp60.index<2100)]

glue_df_monthly_9_hypolimnetic_ave_rcp60_distantfu['50%'].mean()
#10.720250034543257

glue_df_monthly_10_hypolimnetic_ave_rcp60_distantfu=glue_df_monthly_10_hypolimnetic_ave_rcp60[(glue_df_monthly_10_hypolimnetic_ave_rcp60.index>2069) & (glue_df_monthly_10_hypolimnetic_ave_rcp60.index<2100)]

glue_df_monthly_10_hypolimnetic_ave_rcp60_distantfu['50%'].mean()
#11.974157512319382

glue_df_monthly_11_hypolimnetic_ave_rcp60_distantfu=glue_df_monthly_11_hypolimnetic_ave_rcp60[(glue_df_monthly_11_hypolimnetic_ave_rcp60.index>2069) & (glue_df_monthly_11_hypolimnetic_ave_rcp60.index<2100)]

glue_df_monthly_11_hypolimnetic_ave_rcp60_distantfu['50%'].mean()
#13.25102392923405

#%%distant future [2070-2099]

#RCP85
glue_df_monthly_0_hypolimnetic_ave_rcp85_distantfu=glue_df_monthly_0_hypolimnetic_ave_rcp85[(glue_df_monthly_0_hypolimnetic_ave_rcp85.index>2069) & (glue_df_monthly_0_hypolimnetic_ave_rcp85.index<2100)]

glue_df_monthly_0_hypolimnetic_ave_rcp85_distantfu['50%'].mean()
#13.487724533162394

glue_df_monthly_1_hypolimnetic_ave_rcp85_distantfu=glue_df_monthly_1_hypolimnetic_ave_rcp85[(glue_df_monthly_1_hypolimnetic_ave_rcp85.index>2069) & (glue_df_monthly_1_hypolimnetic_ave_rcp85.index<2100)]

glue_df_monthly_1_hypolimnetic_ave_rcp85_distantfu['50%'].mean()
# 13.890617622486314

glue_df_monthly_2_hypolimnetic_ave_rcp85_distantfu=glue_df_monthly_2_hypolimnetic_ave_rcp85[(glue_df_monthly_2_hypolimnetic_ave_rcp85.index>2069) & (glue_df_monthly_2_hypolimnetic_ave_rcp85.index<2100)]

glue_df_monthly_2_hypolimnetic_ave_rcp85_distantfu['50%'].mean()
#13.621258956079119

glue_df_monthly_3_hypolimnetic_ave_rcp85_distantfu=glue_df_monthly_3_hypolimnetic_ave_rcp85[(glue_df_monthly_3_hypolimnetic_ave_rcp85.index>2069) & (glue_df_monthly_3_hypolimnetic_ave_rcp85.index<2100)]

glue_df_monthly_3_hypolimnetic_ave_rcp85_distantfu['50%'].mean()
#12.25450540154844

glue_df_monthly_4_hypolimnetic_ave_rcp85_distantfu=glue_df_monthly_4_hypolimnetic_ave_rcp85[(glue_df_monthly_4_hypolimnetic_ave_rcp85.index>2069) & (glue_df_monthly_4_hypolimnetic_ave_rcp85.index<2100)]

glue_df_monthly_4_hypolimnetic_ave_rcp85_distantfu['50%'].mean()
#9.228259416137178

glue_df_monthly_5_hypolimnetic_ave_rcp85_distantfu=glue_df_monthly_5_hypolimnetic_ave_rcp85[(glue_df_monthly_5_hypolimnetic_ave_rcp85.index>2069) & (glue_df_monthly_5_hypolimnetic_ave_rcp85.index<2100)]

glue_df_monthly_5_hypolimnetic_ave_rcp85_distantfu['50%'].mean()
#4.132773782343418


glue_df_monthly_6_hypolimnetic_ave_rcp85_distantfu=glue_df_monthly_6_hypolimnetic_ave_rcp85[(glue_df_monthly_6_hypolimnetic_ave_rcp85.index>2069) & (glue_df_monthly_6_hypolimnetic_ave_rcp85.index<2100)]

glue_df_monthly_6_hypolimnetic_ave_rcp85_distantfu['50%'].mean()
#0.1953704568581028


glue_df_monthly_7_hypolimnetic_ave_rcp85_distantfu=glue_df_monthly_7_hypolimnetic_ave_rcp85[(glue_df_monthly_7_hypolimnetic_ave_rcp85.index>2069) & (glue_df_monthly_7_hypolimnetic_ave_rcp85.index<2100)]

glue_df_monthly_7_hypolimnetic_ave_rcp85_distantfu['50%'].mean()
#0.0

glue_df_monthly_8_hypolimnetic_ave_rcp85_distantfu=glue_df_monthly_8_hypolimnetic_ave_rcp85[(glue_df_monthly_8_hypolimnetic_ave_rcp85.index>2069) & (glue_df_monthly_8_hypolimnetic_ave_rcp85.index<2100)]

glue_df_monthly_8_hypolimnetic_ave_rcp85_distantfu['50%'].mean()
#4.858908516212328

glue_df_monthly_9_hypolimnetic_ave_rcp85_distantfu=glue_df_monthly_9_hypolimnetic_ave_rcp85[(glue_df_monthly_9_hypolimnetic_ave_rcp85.index>2069) & (glue_df_monthly_9_hypolimnetic_ave_rcp85.index<2100)]

glue_df_monthly_9_hypolimnetic_ave_rcp85_distantfu['50%'].mean()
#10.33179232718159

glue_df_monthly_10_hypolimnetic_ave_rcp85_distantfu=glue_df_monthly_10_hypolimnetic_ave_rcp85[(glue_df_monthly_10_hypolimnetic_ave_rcp85.index>2069) & (glue_df_monthly_10_hypolimnetic_ave_rcp85.index<2100)]

glue_df_monthly_10_hypolimnetic_ave_rcp85_distantfu['50%'].mean()
#11.550059873057153

glue_df_monthly_11_hypolimnetic_ave_rcp85_distantfu=glue_df_monthly_11_hypolimnetic_ave_rcp85[(glue_df_monthly_11_hypolimnetic_ave_rcp85.index>2069) & (glue_df_monthly_11_hypolimnetic_ave_rcp85.index<2100)]

glue_df_monthly_11_hypolimnetic_ave_rcp85_distantfu['50%'].mean()
#12.702468292395716
 
    
    
#%%
glue_df_monthly_11_hypolimnetic_ave_his_baseline['50%']

   
#%% Plotting of monthly DO 


import matplotlib.pyplot as plt

################# Assuming the necessary data arrays are defined
data0_his=glue_df_monthly_0_hypolimnetic_ave_his_baseline['50%']
data0_near_rcp26 = glue_df_monthly_0_hypolimnetic_ave_rcp26_nearfu['50%']
data0_far_rcp26 = glue_df_monthly_0_hypolimnetic_ave_rcp26_distantfu['50%']

data1_his=glue_df_monthly_1_hypolimnetic_ave_his_baseline['50%']
data1_near_rcp26 = glue_df_monthly_1_hypolimnetic_ave_rcp26_nearfu['50%']
data1_far_rcp26 = glue_df_monthly_1_hypolimnetic_ave_rcp26_distantfu['50%']

data2_his=glue_df_monthly_2_hypolimnetic_ave_his_baseline['50%']
data2_near_rcp26 = glue_df_monthly_2_hypolimnetic_ave_rcp26_nearfu['50%']
data2_far_rcp26 = glue_df_monthly_2_hypolimnetic_ave_rcp26_distantfu['50%']

data3_his=glue_df_monthly_3_hypolimnetic_ave_his_baseline['50%']
data3_near_rcp26 = glue_df_monthly_3_hypolimnetic_ave_rcp26_nearfu['50%']
data3_far_rcp26 = glue_df_monthly_3_hypolimnetic_ave_rcp26_distantfu['50%']


data4_his=glue_df_monthly_4_hypolimnetic_ave_his_baseline['50%']
data4_near_rcp26 = glue_df_monthly_4_hypolimnetic_ave_rcp26_nearfu['50%']
data4_far_rcp26 = glue_df_monthly_4_hypolimnetic_ave_rcp26_distantfu['50%']

data5_his=glue_df_monthly_5_hypolimnetic_ave_his_baseline['50%']
data5_near_rcp26 = glue_df_monthly_5_hypolimnetic_ave_rcp26_nearfu['50%']
data5_far_rcp26 = glue_df_monthly_5_hypolimnetic_ave_rcp26_distantfu['50%']

data6_his=glue_df_monthly_6_hypolimnetic_ave_his_baseline['50%']
data6_near_rcp26 = glue_df_monthly_6_hypolimnetic_ave_rcp26_nearfu['50%']
data6_far_rcp26 = glue_df_monthly_6_hypolimnetic_ave_rcp26_distantfu['50%']

data7_his=glue_df_monthly_7_hypolimnetic_ave_his_baseline['50%']
data7_near_rcp26 = glue_df_monthly_7_hypolimnetic_ave_rcp26_nearfu['50%']
data7_far_rcp26 = glue_df_monthly_7_hypolimnetic_ave_rcp26_distantfu['50%']

data8_his=glue_df_monthly_8_hypolimnetic_ave_his_baseline['50%']
data8_near_rcp26 = glue_df_monthly_8_hypolimnetic_ave_rcp26_nearfu['50%']
data8_far_rcp26 = glue_df_monthly_8_hypolimnetic_ave_rcp26_distantfu['50%']

data9_his=glue_df_monthly_9_hypolimnetic_ave_his_baseline['50%']
data9_near_rcp26 = glue_df_monthly_9_hypolimnetic_ave_rcp26_nearfu['50%']
data9_far_rcp26 = glue_df_monthly_9_hypolimnetic_ave_rcp26_distantfu['50%']

data10_his=glue_df_monthly_10_hypolimnetic_ave_his_baseline['50%']
data10_near_rcp26 = glue_df_monthly_10_hypolimnetic_ave_rcp26_nearfu['50%']
data10_far_rcp26 = glue_df_monthly_10_hypolimnetic_ave_rcp26_distantfu['50%']

data11_his=glue_df_monthly_11_hypolimnetic_ave_his_baseline['50%']
data11_near_rcp26 = glue_df_monthly_11_hypolimnetic_ave_rcp26_nearfu['50%']
data11_far_rcp26 = glue_df_monthly_11_hypolimnetic_ave_rcp26_distantfu['50%']
########################################################################
#%%rcp60
data0_his=glue_df_monthly_0_hypolimnetic_ave_his_baseline['50%']
data0_near_rcp60 = glue_df_monthly_0_hypolimnetic_ave_rcp60_nearfu['50%']
data0_far_rcp60 = glue_df_monthly_0_hypolimnetic_ave_rcp60_distantfu['50%']

data1_his=glue_df_monthly_1_hypolimnetic_ave_his_baseline['50%']
data1_near_rcp60 = glue_df_monthly_1_hypolimnetic_ave_rcp60_nearfu['50%']
data1_far_rcp60 = glue_df_monthly_1_hypolimnetic_ave_rcp60_distantfu['50%']

data2_his=glue_df_monthly_2_hypolimnetic_ave_his_baseline['50%']
data2_near_rcp60 = glue_df_monthly_2_hypolimnetic_ave_rcp60_nearfu['50%']
data2_far_rcp60 = glue_df_monthly_2_hypolimnetic_ave_rcp60_distantfu['50%']

data3_his=glue_df_monthly_3_hypolimnetic_ave_his_baseline['50%']
data3_near_rcp60 = glue_df_monthly_3_hypolimnetic_ave_rcp60_nearfu['50%']
data3_far_rcp60 = glue_df_monthly_3_hypolimnetic_ave_rcp60_distantfu['50%']


data4_his=glue_df_monthly_4_hypolimnetic_ave_his_baseline['50%']
data4_near_rcp60 = glue_df_monthly_4_hypolimnetic_ave_rcp60_nearfu['50%']
data4_far_rcp60 = glue_df_monthly_4_hypolimnetic_ave_rcp60_distantfu['50%']

data5_his=glue_df_monthly_5_hypolimnetic_ave_his_baseline['50%']
data5_near_rcp60 = glue_df_monthly_5_hypolimnetic_ave_rcp60_nearfu['50%']
data5_far_rcp60 = glue_df_monthly_5_hypolimnetic_ave_rcp60_distantfu['50%']

data6_his=glue_df_monthly_6_hypolimnetic_ave_his_baseline['50%']
data6_near_rcp60 = glue_df_monthly_6_hypolimnetic_ave_rcp60_nearfu['50%']
data6_far_rcp60 = glue_df_monthly_6_hypolimnetic_ave_rcp60_distantfu['50%']

data7_his=glue_df_monthly_7_hypolimnetic_ave_his_baseline['50%']
data7_near_rcp60 = glue_df_monthly_7_hypolimnetic_ave_rcp60_nearfu['50%']
data7_far_rcp60 = glue_df_monthly_7_hypolimnetic_ave_rcp60_distantfu['50%']

data8_his=glue_df_monthly_8_hypolimnetic_ave_his_baseline['50%']
data8_near_rcp60 = glue_df_monthly_8_hypolimnetic_ave_rcp60_nearfu['50%']
data8_far_rcp60 = glue_df_monthly_8_hypolimnetic_ave_rcp60_distantfu['50%']

data9_his=glue_df_monthly_9_hypolimnetic_ave_his_baseline['50%']
data9_near_rcp60 = glue_df_monthly_9_hypolimnetic_ave_rcp60_nearfu['50%']
data9_far_rcp60 = glue_df_monthly_9_hypolimnetic_ave_rcp60_distantfu['50%']

data10_his=glue_df_monthly_10_hypolimnetic_ave_his_baseline['50%']
data10_near_rcp60 = glue_df_monthly_10_hypolimnetic_ave_rcp60_nearfu['50%']
data10_far_rcp60 = glue_df_monthly_10_hypolimnetic_ave_rcp60_distantfu['50%']

data11_his=glue_df_monthly_11_hypolimnetic_ave_his_baseline['50%']
data11_near_rcp60 = glue_df_monthly_11_hypolimnetic_ave_rcp60_nearfu['50%']
data11_far_rcp60 = glue_df_monthly_11_hypolimnetic_ave_rcp60_distantfu['50%']

#%%rcp85

data0_his=glue_df_monthly_0_hypolimnetic_ave_his_baseline['50%']
data0_near_rcp85 = glue_df_monthly_0_hypolimnetic_ave_rcp85_nearfu['50%']
data0_far_rcp85 = glue_df_monthly_0_hypolimnetic_ave_rcp85_distantfu['50%']

data1_his=glue_df_monthly_1_hypolimnetic_ave_his_baseline['50%']
data1_near_rcp85 = glue_df_monthly_1_hypolimnetic_ave_rcp85_nearfu['50%']
data1_far_rcp85 = glue_df_monthly_1_hypolimnetic_ave_rcp85_distantfu['50%']

data2_his=glue_df_monthly_2_hypolimnetic_ave_his_baseline['50%']
data2_near_rcp85 = glue_df_monthly_2_hypolimnetic_ave_rcp85_nearfu['50%']
data2_far_rcp85 = glue_df_monthly_2_hypolimnetic_ave_rcp85_distantfu['50%']

data3_his=glue_df_monthly_3_hypolimnetic_ave_his_baseline['50%']
data3_near_rcp85 = glue_df_monthly_3_hypolimnetic_ave_rcp85_nearfu['50%']
data3_far_rcp85 = glue_df_monthly_3_hypolimnetic_ave_rcp85_distantfu['50%']


data4_his=glue_df_monthly_4_hypolimnetic_ave_his_baseline['50%']
data4_near_rcp85 = glue_df_monthly_4_hypolimnetic_ave_rcp85_nearfu['50%']
data4_far_rcp85 = glue_df_monthly_4_hypolimnetic_ave_rcp85_distantfu['50%']

data5_his=glue_df_monthly_5_hypolimnetic_ave_his_baseline['50%']
data5_near_rcp85 = glue_df_monthly_5_hypolimnetic_ave_rcp85_nearfu['50%']
data5_far_rcp85 = glue_df_monthly_5_hypolimnetic_ave_rcp85_distantfu['50%']

data6_his=glue_df_monthly_6_hypolimnetic_ave_his_baseline['50%']
data6_near_rcp85 = glue_df_monthly_6_hypolimnetic_ave_rcp85_nearfu['50%']
data6_far_rcp85 = glue_df_monthly_6_hypolimnetic_ave_rcp85_distantfu['50%']

data7_his=glue_df_monthly_7_hypolimnetic_ave_his_baseline['50%']
data7_near_rcp85 = glue_df_monthly_7_hypolimnetic_ave_rcp85_nearfu['50%']
data7_far_rcp85 = glue_df_monthly_7_hypolimnetic_ave_rcp85_distantfu['50%']

data8_his=glue_df_monthly_8_hypolimnetic_ave_his_baseline['50%']
data8_near_rcp85 = glue_df_monthly_8_hypolimnetic_ave_rcp85_nearfu['50%']
data8_far_rcp85 = glue_df_monthly_8_hypolimnetic_ave_rcp85_distantfu['50%']

data9_his=glue_df_monthly_9_hypolimnetic_ave_his_baseline['50%']
data9_near_rcp85 = glue_df_monthly_9_hypolimnetic_ave_rcp85_nearfu['50%']
data9_far_rcp85 = glue_df_monthly_9_hypolimnetic_ave_rcp85_distantfu['50%']

data10_his=glue_df_monthly_10_hypolimnetic_ave_his_baseline['50%']
data10_near_rcp85 = glue_df_monthly_10_hypolimnetic_ave_rcp85_nearfu['50%']
data10_far_rcp85 = glue_df_monthly_10_hypolimnetic_ave_rcp85_distantfu['50%']

data11_his=glue_df_monthly_11_hypolimnetic_ave_his_baseline['50%']
data11_near_rcp85 = glue_df_monthly_11_hypolimnetic_ave_rcp85_nearfu['50%']
data11_far_rcp85 = glue_df_monthly_11_hypolimnetic_ave_rcp85_distantfu['50%']
















#%%RCP26

# Create subplots
fig, axes = plt.subplots(1, 12, figsize=(15,5) , sharey=True)  # 2 rows, 1 column

# Plot for data0
boxes = axes[0].boxplot([data0_his , data0_near_rcp26, data0_far_rcp26], vert=True, patch_artist=True)  # vert=True specifies vertical orientation
# Set colors for the boxplots
colors = [ 'grey', 'lightgreen', 'green']
for box, color in zip(boxes['boxes'], colors):
    box.set(color='black', linewidth=2)  # Set edge color and thickness
    box.set(facecolor=color)  # Set fill color
    for median in boxes['medians']:
        median.set(color='black', linewidth=2)
        
    
axes[0].set_ylabel('Average of deep DO [mg L$^{-1}$]', fontsize=20)
axes[0].set_xlabel('Jan')
# Remove x-axis tick labels
axes[0].set_xticklabels([])


# Plot for data1
boxes = axes[1].boxplot([data1_his , data1_near_rcp26, data1_far_rcp26], vert=True, patch_artist=True)  # vert=True specifies vertical orientation
# Set colors for the boxplots
colors = [ 'grey', 'lightgreen', 'green']
for box, color in zip(boxes['boxes'], colors):
    box.set(color='black', linewidth=2)  # Set edge color and thickness
    box.set(facecolor=color)  # Set fill color
    for median in boxes['medians']:
        median.set(color='black', linewidth=2)

    

axes[1].set_xlabel('Feb')
# Remove x-axis tick labels
axes[1].set_xticklabels([])


# Plot for data2
boxes = axes[2].boxplot([data2_his , data2_near_rcp26, data2_far_rcp26], vert=True, patch_artist=True)  # vert=True specifies vertical orientation
# Set colors for the boxplots
colors = [ 'grey', 'lightgreen', 'green']
for box, color in zip(boxes['boxes'], colors):
    box.set(color='black', linewidth=2)  # Set edge color and thickness
    box.set(facecolor=color)  # Set fill color
    for median in boxes['medians']:
        median.set(color='black', linewidth=2)

    

axes[2].set_xlabel('Mar')
# Remove x-axis tick labels
axes[2].set_xticklabels([])



# Plot for data3
boxes = axes[3].boxplot([data3_his , data3_near_rcp26, data3_far_rcp26], vert=True, patch_artist=True)  # vert=True specifies vertical orientation
# Set colors for the boxplots
colors = [ 'grey', 'lightgreen', 'green']
for box, color in zip(boxes['boxes'], colors):
    box.set(color='black', linewidth=2)  # Set edge color and thickness
    box.set(facecolor=color)  # Set fill color
    for median in boxes['medians']:
        median.set(color='black', linewidth=2)

    

axes[3].set_xlabel('Apr')
# Remove x-axis tick labels
axes[3].set_xticklabels([])



# Plot for data4
boxes = axes[4].boxplot([data4_his , data4_near_rcp26, data4_far_rcp26], vert=True, patch_artist=True)  # vert=True specifies vertical orientation
# Set colors for the boxplots
colors = [ 'grey', 'lightgreen', 'green']
for box, color in zip(boxes['boxes'], colors):
    box.set(color='black', linewidth=2)  # Set edge color and thickness
    box.set(facecolor=color)  # Set fill color
    for median in boxes['medians']:
        median.set(color='black', linewidth=2)

    

axes[4].set_xlabel('May')
# Remove x-axis tick labels
axes[4].set_xticklabels([])



# Plot for data5
boxes = axes[5].boxplot([data5_his , data5_near_rcp26, data5_far_rcp26], vert=True, patch_artist=True)  # vert=True specifies vertical orientation
# Set colors for the boxplots
colors = [ 'grey', 'lightgreen', 'green']
for box, color in zip(boxes['boxes'], colors):
    box.set(color='black', linewidth=2)  # Set edge color and thickness
    box.set(facecolor=color)  # Set fill color
    for median in boxes['medians']:
        median.set(color='black', linewidth=2)
 

axes[5].set_xlabel('Jun')
# Remove x-axis tick labels
axes[5].set_xticklabels([])



# Plot for data6
boxes = axes[6].boxplot([data6_his , data6_near_rcp26, data6_far_rcp26], vert=True, patch_artist=True)  # vert=True specifies vertical orientation
# Set colors for the boxplots
colors = [ 'grey', 'lightgreen', 'green']
for box, color in zip(boxes['boxes'], colors):
    box.set(color='black', linewidth=2)  # Set edge color and thickness
    box.set(facecolor=color)  # Set fill color
    for median in boxes['medians']:
        median.set(color='black', linewidth=2)

    

axes[6].set_xlabel('Jul')
# Remove x-axis tick labels
axes[6].set_xticklabels([])



# Plot for data7
boxes = axes[7].boxplot([data7_his , data7_near_rcp26, data7_far_rcp26], vert=True, patch_artist=True)  # vert=True specifies vertical orientation
# Set colors for the boxplots
colors = [ 'grey', 'lightgreen', 'green']
for box, color in zip(boxes['boxes'], colors):
    box.set(color='black', linewidth=2)  # Set edge color and thickness
    box.set(facecolor=color)  # Set fill color
    for median in boxes['medians']:
        median.set(color='black', linewidth=2)

    

axes[7].set_xlabel('Aug')
# Remove x-axis tick labels
axes[7].set_xticklabels([])


# Plot for data8
boxes = axes[8].boxplot([data8_his , data8_near_rcp26, data8_far_rcp26], vert=True, patch_artist=True)  # vert=True specifies vertical orientation
# Set colors for the boxplots
colors = [ 'grey', 'lightgreen', 'green']
for box, color in zip(boxes['boxes'], colors):
    box.set(color='black', linewidth=2)  # Set edge color and thickness
    box.set(facecolor=color)  # Set fill color
    for median in boxes['medians']:
        median.set(color='black', linewidth=2)

    

axes[8].set_xlabel('Sep')
# Remove x-axis tick labels
axes[8].set_xticklabels([])



# Plot for data9
boxes = axes[9].boxplot([data9_his , data9_near_rcp26, data9_far_rcp26], vert=True, patch_artist=True)  # vert=True specifies vertical orientation
# Set colors for the boxplots
colors = [ 'grey', 'lightgreen', 'green']
for box, color in zip(boxes['boxes'], colors):
    box.set(color='black', linewidth=2)  # Set edge color and thickness
    box.set(facecolor=color)  # Set fill color
    for median in boxes['medians']:
        median.set(color='black', linewidth=2)

    

axes[9].set_xlabel('Oct')
# Remove x-axis tick labels
axes[9].set_xticklabels([])


# Plot for data10
boxes = axes[10].boxplot([data10_his , data10_near_rcp26, data10_far_rcp26], vert=True, patch_artist=True)  # vert=True specifies vertical orientation
# Set colors for the boxplots
colors = [ 'grey', 'lightgreen', 'green']
for box, color in zip(boxes['boxes'], colors):
    box.set(color='black', linewidth=2)  # Set edge color and thickness
    box.set(facecolor=color)  # Set fill color
    for median in boxes['medians']:
        median.set(color='black', linewidth=2)

    

axes[10].set_xlabel('Nov')
# Remove x-axis tick labels
axes[10].set_xticklabels([])


# Plot for data11
# Plot for data11
boxes = axes[11].boxplot([data11_his , data11_near_rcp26, data11_far_rcp26], vert=True, patch_artist=True)  # vert=True specifies vertical orientation
# Set colors for the boxplots
colors = [ 'grey', 'lightgreen', 'green']
labels = ['His 1976-2005', 'RCP2.6 2030-2059', 'RCP2.6 2070-2099']
for box, color, label in zip(boxes['boxes'], colors , labels):
    box.set(color='black', linewidth=2)  # Set edge color and thickness
    box.set(facecolor=color, label=label)  # Set fill color
    for median in boxes['medians']:
        median.set(color='black', linewidth=2)

    

axes[11].set_xlabel('Dec')
# Remove x-axis tick labels
axes[11].set_xticklabels([])

# Add legend
plt.legend(bbox_to_anchor=(1.05, 0.5), loc='center left')


# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()




#%%rcp60

# Create subplots
fig, axes = plt.subplots(1, 12, figsize=(15,5) , sharey=True)  # 2 rows, 1 column

# Plot for data0
boxes = axes[0].boxplot([data0_his , data0_near_rcp60, data0_far_rcp60], vert=True, patch_artist=True)  # vert=True specifies vertical orientation
# Set colors for the boxplots
colors = [ 'grey', 'yellow', 'orange']
for box, color in zip(boxes['boxes'], colors):
    box.set(color='black', linewidth=2)  # Set edge color and thickness
    box.set(facecolor=color)  # Set fill color
    for median in boxes['medians']:
        median.set(color='black', linewidth=2)

    
axes[0].set_ylabel('Average of deep DO [mg L$^{-1}$]', fontsize=20)
axes[0].set_xlabel('Jan')
# Remove x-axis tick labels
axes[0].set_xticklabels([])


# Plot for data1
boxes = axes[1].boxplot([data1_his , data1_near_rcp60, data1_far_rcp60], vert=True, patch_artist=True)  # vert=True specifies vertical orientation
# Set colors for the boxplots
colors = [ 'grey', 'yellow', 'orange']
for box, color in zip(boxes['boxes'], colors):
    box.set(color='black', linewidth=2)  # Set edge color and thickness
    box.set(facecolor=color)  # Set fill color
    for median in boxes['medians']:
        median.set(color='black', linewidth=2)

    

axes[1].set_xlabel('Feb')
# Remove x-axis tick labels
axes[1].set_xticklabels([])


# Plot for data2
boxes = axes[2].boxplot([data2_his , data2_near_rcp60, data2_far_rcp60], vert=True, patch_artist=True)  # vert=True specifies vertical orientation
# Set colors for the boxplots
colors = [ 'grey', 'yellow', 'orange']
for box, color in zip(boxes['boxes'], colors):
    box.set(color='black', linewidth=2)  # Set edge color and thickness
    box.set(facecolor=color)  # Set fill color
    for median in boxes['medians']:
        median.set(color='black', linewidth=2)

    

axes[2].set_xlabel('Mar')
# Remove x-axis tick labels
axes[2].set_xticklabels([])



# Plot for data3
boxes = axes[3].boxplot([data3_his , data3_near_rcp60, data3_far_rcp60], vert=True, patch_artist=True)  # vert=True specifies vertical orientation
# Set colors for the boxplots
colors = [ 'grey', 'yellow', 'orange']
for box, color in zip(boxes['boxes'], colors):
    box.set(color='black', linewidth=2)  # Set edge color and thickness
    box.set(facecolor=color)  # Set fill color
    for median in boxes['medians']:
        median.set(color='black', linewidth=2)

    

axes[3].set_xlabel('Apr')
# Remove x-axis tick labels
axes[3].set_xticklabels([])



# Plot for data4
boxes = axes[4].boxplot([data4_his , data4_near_rcp60, data4_far_rcp60], vert=True, patch_artist=True)  # vert=True specifies vertical orientation
# Set colors for the boxplots
colors = [ 'grey', 'yellow', 'orange']
for box, color in zip(boxes['boxes'], colors):
    box.set(color='black', linewidth=2)  # Set edge color and thickness
    box.set(facecolor=color)  # Set fill color
    for median in boxes['medians']:
        median.set(color='black', linewidth=2)

    

axes[4].set_xlabel('May')
# Remove x-axis tick labels
axes[4].set_xticklabels([])



# Plot for data5
boxes = axes[5].boxplot([data5_his , data5_near_rcp60, data5_far_rcp60], vert=True, patch_artist=True)  # vert=True specifies vertical orientation
# Set colors for the boxplots
colors = [ 'grey', 'yellow', 'orange']
for box, color in zip(boxes['boxes'], colors):
    box.set(color='black', linewidth=2)  # Set edge color and thickness
    box.set(facecolor=color)  # Set fill color
    for median in boxes['medians']:
        median.set(color='black', linewidth=2)
 

axes[5].set_xlabel('Jun')
# Remove x-axis tick labels
axes[5].set_xticklabels([])



# Plot for data6
boxes = axes[6].boxplot([data6_his , data6_near_rcp60, data6_far_rcp60], vert=True, patch_artist=True)  # vert=True specifies vertical orientation
# Set colors for the boxplots
colors = [ 'grey', 'yellow', 'orange']
for box, color in zip(boxes['boxes'], colors):
    box.set(color='black', linewidth=2)  # Set edge color and thickness
    box.set(facecolor=color)  # Set fill color
    for median in boxes['medians']:
        median.set(color='black', linewidth=2)

    

axes[6].set_xlabel('Jul')
# Remove x-axis tick labels
axes[6].set_xticklabels([])



# Plot for data7
boxes = axes[7].boxplot([data7_his , data7_near_rcp60, data7_far_rcp60], vert=True, patch_artist=True)  # vert=True specifies vertical orientation
# Set colors for the boxplots
colors = [ 'grey', 'yellow', 'orange']
for box, color in zip(boxes['boxes'], colors):
    box.set(color='black', linewidth=2)  # Set edge color and thickness
    box.set(facecolor=color)  # Set fill color
    for median in boxes['medians']:
        median.set(color='black', linewidth=2)

    

axes[7].set_xlabel('Aug')
# Remove x-axis tick labels
axes[7].set_xticklabels([])


# Plot for data8
boxes = axes[8].boxplot([data8_his , data8_near_rcp60, data8_far_rcp60], vert=True, patch_artist=True)  # vert=True specifies vertical orientation
# Set colors for the boxplots
colors = [ 'grey', 'yellow', 'orange']
for box, color in zip(boxes['boxes'], colors):
    box.set(color='black', linewidth=2)  # Set edge color and thickness
    box.set(facecolor=color)  # Set fill color
    for median in boxes['medians']:
        median.set(color='black', linewidth=2)

    

axes[8].set_xlabel('Sep')
# Remove x-axis tick labels
axes[8].set_xticklabels([])



# Plot for data9
boxes = axes[9].boxplot([data9_his , data9_near_rcp60, data9_far_rcp60], vert=True, patch_artist=True)  # vert=True specifies vertical orientation
# Set colors for the boxplots
colors = [ 'grey', 'yellow', 'orange']
for box, color in zip(boxes['boxes'], colors):
    box.set(color='black', linewidth=2)  # Set edge color and thickness
    box.set(facecolor=color)  # Set fill color
    for median in boxes['medians']:
        median.set(color='black', linewidth=2)

    

axes[9].set_xlabel('Oct')
# Remove x-axis tick labels
axes[9].set_xticklabels([])


# Plot for data10
boxes = axes[10].boxplot([data10_his , data10_near_rcp60, data10_far_rcp60], vert=True, patch_artist=True)  # vert=True specifies vertical orientation
# Set colors for the boxplots
colors = [ 'grey', 'yellow', 'orange']
for box, color in zip(boxes['boxes'], colors):
    box.set(color='black', linewidth=2)  # Set edge color and thickness
    box.set(facecolor=color)  # Set fill color
    for median in boxes['medians']:
        median.set(color='black', linewidth=2)

    

axes[10].set_xlabel('Nov')
# Remove x-axis tick labels
axes[10].set_xticklabels([])


# Plot for data11
boxes = axes[11].boxplot([data11_his , data11_near_rcp60, data11_far_rcp60], vert=True, patch_artist=True)  # vert=True specifies vertical orientation
# Set colors for the boxplots
colors = [ 'grey', 'yellow', 'orange']
labels = ['His 1976-2005', 'RCP6.0 2030-2059', 'RCP6.0 2070-2099']
for box, color, label in zip(boxes['boxes'], colors , labels):
    box.set(color='black', linewidth=2)  # Set edge color and thickness
    box.set(facecolor=color, label=label)  # Set fill color
    for median in boxes['medians']:
        median.set(color='black', linewidth=2)

    

axes[11].set_xlabel('Dec')
# Remove x-axis tick labels
axes[11].set_xticklabels([])

# Add legend
plt.legend(bbox_to_anchor=(1.05, 0.5), loc='center left')


# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()




#%%rcp85

# Create subplots
fig, axes = plt.subplots(1, 12, figsize=(15,5) , sharey=True)  # 2 rows, 1 column

# Plot for data0
boxes = axes[0].boxplot([data0_his , data0_near_rcp85, data0_far_rcp85], vert=True, patch_artist=True)  # vert=True specifies vertical orientation
# Set colors for the boxplots
colors = [ 'grey', 'red', 'darkred']
for box, color in zip(boxes['boxes'], colors):
    box.set(color='black', linewidth=2)  # Set edge color and thickness
    box.set(facecolor=color)  # Set fill color
    for median in boxes['medians']:
        median.set(color='black', linewidth=2)

    
axes[0].set_ylabel('Average of deep DO [mg L$^{-1}$]', fontsize=20)
axes[0].set_xlabel('Jan')
# Remove x-axis tick labels
axes[0].set_xticklabels([])


# Plot for data1
boxes = axes[1].boxplot([data1_his , data1_near_rcp85, data1_far_rcp85], vert=True, patch_artist=True)  # vert=True specifies vertical orientation
# Set colors for the boxplots
colors = [ 'grey', 'red', 'darkred']
for box, color in zip(boxes['boxes'], colors):
    box.set(color='black', linewidth=2)  # Set edge color and thickness
    box.set(facecolor=color)  # Set fill color
    for median in boxes['medians']:
        median.set(color='black', linewidth=2)

    

axes[1].set_xlabel('Feb')
# Remove x-axis tick labels
axes[1].set_xticklabels([])


# Plot for data2
boxes = axes[2].boxplot([data2_his , data2_near_rcp85, data2_far_rcp85], vert=True, patch_artist=True)  # vert=True specifies vertical orientation
# Set colors for the boxplots
colors = [ 'grey', 'red', 'darkred']
for box, color in zip(boxes['boxes'], colors):
    box.set(color='black', linewidth=2)  # Set edge color and thickness
    box.set(facecolor=color)  # Set fill color
    for median in boxes['medians']:
        median.set(color='black', linewidth=2)

    

axes[2].set_xlabel('Mar')
# Remove x-axis tick labels
axes[2].set_xticklabels([])



# Plot for data3
boxes = axes[3].boxplot([data3_his , data3_near_rcp85, data3_far_rcp85], vert=True, patch_artist=True)  # vert=True specifies vertical orientation
# Set colors for the boxplots
colors = [ 'grey', 'red', 'darkred']
for box, color in zip(boxes['boxes'], colors):
    box.set(color='black', linewidth=2)  # Set edge color and thickness
    box.set(facecolor=color)  # Set fill color
    for median in boxes['medians']:
        median.set(color='black', linewidth=2)

    

axes[3].set_xlabel('Apr')
# Remove x-axis tick labels
axes[3].set_xticklabels([])



# Plot for data4
boxes = axes[4].boxplot([data4_his , data4_near_rcp85, data4_far_rcp85], vert=True, patch_artist=True)  # vert=True specifies vertical orientation
# Set colors for the boxplots
colors = [ 'grey', 'red', 'darkred']
for box, color in zip(boxes['boxes'], colors):
    box.set(color='black', linewidth=2)  # Set edge color and thickness
    box.set(facecolor=color)  # Set fill color
    for median in boxes['medians']:
        median.set(color='black', linewidth=2)

    

axes[4].set_xlabel('May')
# Remove x-axis tick labels
axes[4].set_xticklabels([])



# Plot for data5
boxes = axes[5].boxplot([data5_his , data5_near_rcp85, data5_far_rcp85], vert=True, patch_artist=True)  # vert=True specifies vertical orientation
# Set colors for the boxplots
colors = [ 'grey', 'red', 'darkred']
for box, color in zip(boxes['boxes'], colors):
    box.set(color='black', linewidth=2)  # Set edge color and thickness
    box.set(facecolor=color)  # Set fill color
    for median in boxes['medians']:
        median.set(color='black', linewidth=2)
 

axes[5].set_xlabel('Jun')
# Remove x-axis tick labels
axes[5].set_xticklabels([])



# Plot for data6
boxes = axes[6].boxplot([data6_his , data6_near_rcp85, data6_far_rcp85], vert=True, patch_artist=True)  # vert=True specifies vertical orientation
# Set colors for the boxplots
colors = [ 'grey', 'red', 'darkred']
for box, color in zip(boxes['boxes'], colors):
    box.set(color='black', linewidth=2)  # Set edge color and thickness
    box.set(facecolor=color)  # Set fill color
    for median in boxes['medians']:
        median.set(color='black', linewidth=2)

    

axes[6].set_xlabel('Jul')
# Remove x-axis tick labels
axes[6].set_xticklabels([])



# Plot for data7
boxes = axes[7].boxplot([data7_his , data7_near_rcp85, data7_far_rcp85], vert=True, patch_artist=True)  # vert=True specifies vertical orientation
# Set colors for the boxplots
colors = [ 'grey', 'red', 'darkred']
for box, color in zip(boxes['boxes'], colors):
    box.set(color='black', linewidth=2)  # Set edge color and thickness
    box.set(facecolor=color)  # Set fill color
    for median in boxes['medians']:
        median.set(color='black', linewidth=2)

    

axes[7].set_xlabel('Aug')
# Remove x-axis tick labels
axes[7].set_xticklabels([])


# Plot for data8
boxes = axes[8].boxplot([data8_his , data8_near_rcp85, data8_far_rcp85], vert=True, patch_artist=True)  # vert=True specifies vertical orientation
# Set colors for the boxplots
colors = [ 'grey', 'red', 'darkred']
for box, color in zip(boxes['boxes'], colors):
    box.set(color='black', linewidth=2)  # Set edge color and thickness
    box.set(facecolor=color)  # Set fill color
    for median in boxes['medians']:
        median.set(color='black', linewidth=2)

    

axes[8].set_xlabel('Sep')
# Remove x-axis tick labels
axes[8].set_xticklabels([])



# Plot for data9
boxes = axes[9].boxplot([data9_his , data9_near_rcp85, data9_far_rcp85], vert=True, patch_artist=True)  # vert=True specifies vertical orientation
# Set colors for the boxplots
colors = [ 'grey', 'red', 'darkred']
for box, color in zip(boxes['boxes'], colors):
    box.set(color='black', linewidth=2)  # Set edge color and thickness
    box.set(facecolor=color)  # Set fill color
    for median in boxes['medians']:
        median.set(color='black', linewidth=2)

    

axes[9].set_xlabel('Oct')
# Remove x-axis tick labels
axes[9].set_xticklabels([])


# Plot for data10
boxes = axes[10].boxplot([data10_his , data10_near_rcp85, data10_far_rcp85], vert=True, patch_artist=True)  # vert=True specifies vertical orientation
# Set colors for the boxplots
colors = [ 'grey', 'red', 'darkred']
for box, color in zip(boxes['boxes'], colors):
    box.set(color='black', linewidth=2)  # Set edge color and thickness
    box.set(facecolor=color)  # Set fill color
    for median in boxes['medians']:
        median.set(color='black', linewidth=2)

    

axes[10].set_xlabel('Nov')
# Remove x-axis tick labels
axes[10].set_xticklabels([])


# Plot for data11
boxes = axes[11].boxplot([data11_his , data11_near_rcp85, data11_far_rcp85], vert=True, patch_artist=True)  # vert=True specifies vertical orientation
# Set colors for the boxplots
colors = [ 'grey', 'red', 'darkred']
labels = ['His 1976-2005', 'RCP8.5 2030-2059', 'RCP8.5 2070-2099']
for box, color, label in zip(boxes['boxes'], colors , labels):
    box.set(color='black', linewidth=2)  # Set edge color and thickness
    box.set(facecolor=color, label=label)  # Set fill color
    for median in boxes['medians']:
        median.set(color='black', linewidth=2)

    

axes[11].set_xlabel('Dec')
# Remove x-axis tick labels
axes[11].set_xticklabels([])

# Add legend
plt.legend(bbox_to_anchor=(1.05, 0.5), loc='center left')


# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()










#%%
# the whole years


######his_annual_DO

#years
contributions_annual_do_his_years=anova_annual_do_his['year']
#GCMs
gcm_contributions_annual_do_his= anova_annual_do_his['GCMs']
#Param
param_contributions_annual_do_his=anova_annual_do_his['param']
#interaction
interact_contributions_annual_do_his =anova_annual_do_his['interaction']

######his_monthly_DO

#years
contributions_monthly_do_his_years=anova_monthly_do_his['year']
#GCMs
gcm_contributions_monthly_do_his = anova_monthly_do_his['GCMs']
#Param
param_contributions_monthly_do_his =anova_monthly_do_his['param']
#interaction
interact_contributions_monthly_do_his =anova_monthly_do_his['interaction']



"""
######his_summer_DO

#years
contributions_summer_do_his_years=anova_summer_do_his['year']
#GCMs
gcm_contributions_summer_do_his = anova_summer_do_his['GCMs']
#Param
param_contributions_summer_do_his =anova_summer_do_his['param']
#interaction
interact_contributions_summer_do_his =anova_summer_do_his['interaction']
"""


######Plotting:

# Define the directory path
directory_path = r'C:\Users\mahta\OneDrive\Documents\PhD_py_code\Future_simulation_results\all_4_models\uncertainty'

# Change the current working directory
os.chdir(directory_path)    


import matplotlib.pyplot as plt
from matplotlib.patches import Patch

# Define colors explicitly as RGB tuples
colors = [(0.96, 0.80, 0.69), (0.6, 0.4, 0.8), (0, 0, 1)]  # Flesh, Dark Orchid, Blue

# Create a figure with three subplots
fig, axs = plt.subplots(1, 2, figsize=(24, 5), sharey=True)

# Define data for each subplot (assuming you have defined your data earlier)

# Subplot for rcp26
axs[0].fill_between(contributions_annual_do_his_years, 0, gcm_contributions_annual_do_his , label='GCMs', alpha=0.7, color=colors[0], edgecolor='black')
axs[0].fill_between(contributions_annual_do_his_years, gcm_contributions_annual_do_his , gcm_contributions_annual_do_his + param_contributions_annual_do_his, label='Parameters', alpha=0.7, color=colors[1], edgecolor='black')
axs[0].fill_between(contributions_annual_do_his_years, gcm_contributions_annual_do_his  + param_contributions_annual_do_his, gcm_contributions_annual_do_his + param_contributions_annual_do_his + interact_contributions_annual_do_his, label='Interactions', alpha=0.7, color=colors[2], edgecolor='black')
axs[0].set_title('(a) DO in deoxygenation period', fontsize=20)
axs[0].set_ylim(0,100)
axs[0].set_xlim(1861, 2005)
axs[0].tick_params(axis='both', which='major', labelsize=20)

# Subplot for rcp60
axs[1].fill_between(contributions_monthly_do_his_years, 0, gcm_contributions_monthly_do_his, label='GCMs', alpha=0.7, color=colors[0], edgecolor='black')
axs[1].fill_between(contributions_monthly_do_his_years, gcm_contributions_monthly_do_his, gcm_contributions_monthly_do_his + param_contributions_monthly_do_his, label='Parameters', alpha=0.7, color=colors[1], edgecolor='black')
axs[1].fill_between(contributions_monthly_do_his_years, gcm_contributions_monthly_do_his + param_contributions_monthly_do_his, gcm_contributions_monthly_do_his + param_contributions_monthly_do_his + interact_contributions_monthly_do_his, label='Interactions', alpha=0.7, color=colors[2], edgecolor='black')
axs[1].set_title('(b) Apr-Oct DO', fontsize=20)
axs[1].set_ylim(0,100)
axs[1].set_xlim(1861, 2005)
axs[1].tick_params(axis='both', which='major', labelsize=20)
"""
# Subplot for rcp85
axs[2].fill_between(contributions_summer_do_his_years, 0, gcm_contributions_summer_do_his, label='GCMs', alpha=0.7, color=colors[0], edgecolor='black')
axs[2].fill_between(contributions_summer_do_his_years, gcm_contributions_summer_do_his, gcm_contributions_summer_do_his + param_contributions_summer_do_his, label='Parameters', alpha=0.7, color=colors[1], edgecolor='black')
axs[2].fill_between(contributions_summer_do_his_years, gcm_contributions_summer_do_his + param_contributions_summer_do_his, gcm_contributions_summer_do_his + param_contributions_summer_do_his + interact_contributions_summer_do_his, label='Interactions', alpha=0.7, color=colors[2], edgecolor='black')
axs[2].set_title('Summer DO', fontsize=20)
axs[2].set_ylim(0,100)
axs[2].set_xlim(1861, 2005)
axs[2].tick_params(axis='both', which='major', labelsize=20)
"""
# Adding labels and title with increased font size
# fig.text(0.5, 0.08, 'Year', ha='center', fontsize=20)
fig.text(0.08, 0.5, 'Uncertainty sources in hypolimnetic DO [%]', va='center', rotation='vertical', fontsize=22)

# Create legend handles and labels
legend_handles = [Patch(facecolor=colors[0], edgecolor='black'), 
                  Patch(facecolor=colors[1], edgecolor='black'), 
                  Patch(facecolor=colors[2], edgecolor='black')]
legend_labels = ['GCMs', 'Parameters', 'Interactions']

# Add a single legend outside the subplots
fig.legend(legend_handles, legend_labels,bbox_to_anchor=(0.57, 0.06), fontsize=22)


# Save the plot
plt.savefig('uncertainty_hypolimnetic_annual_monthly_DO_allyears_his.png', dpi=300, bbox_inches='tight')

plt.show()






#%%Plot of Anova test on all_annual_do_rcps




# the whole RCPs years


######rcp26

#years
contributions_annual_do_rcp26_years=anova_annual_do_rcp26['year']
#GCMs
gcm_contributions_annual_do_rcp26 = anova_annual_do_rcp26['GCMs']
#Param
param_contributions_annual_do_rcp26 =anova_annual_do_rcp26['param']
#interaction
interact_contributions_annual_do_rcp26 =anova_annual_do_rcp26['interaction']

######rcp60

#years
contributions_annual_do_rcp60_years=anova_annual_do_rcp60['year']
#GCMs
gcm_contributions_annual_do_rcp60 = anova_annual_do_rcp60['GCMs']
#Param
param_contributions_annual_do_rcp60 =anova_annual_do_rcp60['param']
#interaction
interact_contributions_annual_do_rcp60 =anova_annual_do_rcp60['interaction']




######rcp85

#years
contributions_annual_do_rcp85_years=anova_annual_do_rcp85['year']
#GCMs
gcm_contributions_annual_do_rcp85 = anova_annual_do_rcp85['GCMs']
#Param
param_contributions_annual_do_rcp85 =anova_annual_do_rcp85['param']
#interaction
interact_contributions_annual_do_rcp85 =anova_annual_do_rcp85['interaction']




######Plotting:

    
# Define the directory path
directory_path = r'C:\Users\mahta\OneDrive\Documents\PhD_py_code\Future_simulation_results\all_4_models\uncertainty'

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
axs[0].fill_between(contributions_annual_do_rcp26_years, 0, gcm_contributions_annual_do_rcp26, label='GCMs', alpha=0.7, color=colors[0], edgecolor='black')
axs[0].fill_between(contributions_annual_do_rcp26_years, gcm_contributions_annual_do_rcp26, gcm_contributions_annual_do_rcp26 + param_contributions_annual_do_rcp26, label='Parameters', alpha=0.7, color=colors[1], edgecolor='black')
axs[0].fill_between(contributions_annual_do_rcp26_years, gcm_contributions_annual_do_rcp26 + param_contributions_annual_do_rcp26, gcm_contributions_annual_do_rcp26 + param_contributions_annual_do_rcp26 + interact_contributions_annual_do_rcp26, label='Interactions', alpha=0.7, color=colors[2], edgecolor='black')
axs[0].set_title('(a) RCP2.6', fontsize=20)
axs[0].set_ylim(0,100)
axs[0].set_xlim(2006, 2099)
axs[0].tick_params(axis='both', which='major', labelsize=20)

# Subplot for rcp60
axs[1].fill_between(contributions_annual_do_rcp60_years, 0, gcm_contributions_annual_do_rcp60, label='GCMs', alpha=0.7, color=colors[0], edgecolor='black')
axs[1].fill_between(contributions_annual_do_rcp60_years, gcm_contributions_annual_do_rcp60, gcm_contributions_annual_do_rcp60 + param_contributions_annual_do_rcp60, label='Parameters', alpha=0.7, color=colors[1], edgecolor='black')
axs[1].fill_between(contributions_annual_do_rcp60_years, gcm_contributions_annual_do_rcp60 + param_contributions_annual_do_rcp60, gcm_contributions_annual_do_rcp60 + param_contributions_annual_do_rcp60 + interact_contributions_annual_do_rcp60, label='Interactions', alpha=0.7, color=colors[2], edgecolor='black')
axs[1].set_title('(b) RCP6.0', fontsize=20)
axs[1].set_ylim(0,100)
axs[1].set_xlim(2006, 2099)
axs[1].tick_params(axis='both', which='major', labelsize=20)

# Subplot for rcp85
axs[2].fill_between(contributions_annual_do_rcp85_years, 0, gcm_contributions_annual_do_rcp85, label='GCMs', alpha=0.7, color=colors[0], edgecolor='black')
axs[2].fill_between(contributions_annual_do_rcp85_years, gcm_contributions_annual_do_rcp85, gcm_contributions_annual_do_rcp85 + param_contributions_annual_do_rcp85, label='Parameters', alpha=0.7, color=colors[1], edgecolor='black')
axs[2].fill_between(contributions_annual_do_rcp85_years, gcm_contributions_annual_do_rcp85 + param_contributions_annual_do_rcp85, gcm_contributions_annual_do_rcp85 + param_contributions_annual_do_rcp85 + interact_contributions_annual_do_rcp85, label='Interactions', alpha=0.7, color=colors[2], edgecolor='black')
axs[2].set_title('(c) RCP8.5', fontsize=20)
axs[2].set_ylim(0,100)
axs[2].set_xlim(2006, 2099)
axs[2].tick_params(axis='both', which='major', labelsize=20)

# Adding labels and title with increased font size
# fig.text(0.5, 0.08, 'Year', ha='center', fontsize=20)
fig.text(0.08, 0.5, 'Uncertainty sources in hypolimnetic DO\n over deoxygenation period [%]', va='center', rotation='vertical', fontsize=22)

# Create legend handles and labels
legend_handles = [Patch(facecolor=colors[0], edgecolor='black'), 
                  Patch(facecolor=colors[1], edgecolor='black'), 
                  Patch(facecolor=colors[2], edgecolor='black')]
legend_labels = ['GCMs', 'Parameters', 'Interactions']

# Add a single legend outside the subplots
fig.legend(legend_handles, legend_labels,bbox_to_anchor=(0.57, 0.06), fontsize=22)


# Save the plot
plt.savefig('uncertainty_annualDO_allyears_rcps.png', dpi=300, bbox_inches='tight')

plt.show()




#%% analyses onley for 80 years


########rcp26

#year
contributions_80years_annual_do_rcp26_years=anova_annual_do_rcp26[anova_annual_do_rcp26.year>2019].year
#gcms
gcm_contributions_80years_annual_do_rcp26 = anova_annual_do_rcp26[anova_annual_do_rcp26.year>2019]['GCMs']
#param
param_contributions_80years_annual_do_rcp26 =anova_annual_do_rcp26[anova_annual_do_rcp26.year>2019]['param']
#interaction
interact_contributions_80years_annual_do_rcp26 =anova_annual_do_rcp26[anova_annual_do_rcp26.year>2019]['interaction']



#########rcp60

#year
contributions_80years_annual_do_rcp60_years=anova_annual_do_rcp60[anova_annual_do_rcp60.year>2019].year
#gcms
gcm_contributions_80years_annual_do_rcp60 = anova_annual_do_rcp60[anova_annual_do_rcp60.year>2019]['GCMs']
#param
param_contributions_80years_annual_do_rcp60 =anova_annual_do_rcp60[anova_annual_do_rcp60.year>2019]['param']
#interaction
interact_contributions_80years_annual_do_rcp60 =anova_annual_do_rcp60[anova_annual_do_rcp60.year>2019]['interaction']


##########rcp85
#year
contributions_80years_annual_do_rcp85_years=anova_annual_do_rcp85[anova_annual_do_rcp85.year>2019].year
#gcms
gcm_contributions_80years_annual_do_rcp85 = anova_annual_do_rcp85[anova_annual_do_rcp85.year>2019]['GCMs']
#param
param_contributions_80years_annual_do_rcp85 =anova_annual_do_rcp85[anova_annual_do_rcp85.year>2019]['param']
#interaction
interact_contributions_80years_annual_do_rcp85 =anova_annual_do_rcp85[anova_annual_do_rcp85.year>2019]['interaction']


######Plotting:
    
# Define the directory path
directory_path = r'C:\Users\mahta\OneDrive\Documents\PhD_py_code\Future_simulation_results\all_4_models\uncertainty'

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
axs[0].fill_between(contributions_80years_annual_do_rcp26_years, 0, gcm_contributions_80years_annual_do_rcp26, label='GCMs', alpha=0.7, color=colors[0], edgecolor='black')
axs[0].fill_between(contributions_80years_annual_do_rcp26_years, gcm_contributions_80years_annual_do_rcp26, gcm_contributions_80years_annual_do_rcp26 + param_contributions_80years_annual_do_rcp26, label='Parameters', alpha=0.7, color=colors[1], edgecolor='black')
axs[0].fill_between(contributions_80years_annual_do_rcp26_years, gcm_contributions_80years_annual_do_rcp26 + param_contributions_80years_annual_do_rcp26, gcm_contributions_80years_annual_do_rcp26 + param_contributions_80years_annual_do_rcp26 + interact_contributions_80years_annual_do_rcp26, label='Interactions', alpha=0.7, color=colors[2], edgecolor='black')
axs[0].set_title('(a) RCP2.6', fontsize=20)
axs[0].set_ylim(0,100)
axs[0].set_xlim(2020, 2099)
axs[0].tick_params(axis='both', which='major', labelsize=20)
#axs[0].set_xticks(np.arange(2020, 2100, 10),fontsize=20)

# Subplot for rcp60
axs[1].fill_between(contributions_80years_annual_do_rcp60_years, 0, gcm_contributions_80years_annual_do_rcp60, label='GCMs', alpha=0.7, color=colors[0], edgecolor='black')
axs[1].fill_between(contributions_80years_annual_do_rcp60_years, gcm_contributions_80years_annual_do_rcp60, gcm_contributions_80years_annual_do_rcp60 + param_contributions_80years_annual_do_rcp60, label='Parameters', alpha=0.7, color=colors[1], edgecolor='black')
axs[1].fill_between(contributions_80years_annual_do_rcp60_years, gcm_contributions_80years_annual_do_rcp60 + param_contributions_80years_annual_do_rcp60, gcm_contributions_80years_annual_do_rcp60 + param_contributions_80years_annual_do_rcp60 + interact_contributions_80years_annual_do_rcp60, label='Interactions', alpha=0.7, color=colors[2], edgecolor='black')
axs[1].set_title('(b) RCP6.0', fontsize=20)
axs[1].set_ylim(0,100)
axs[1].set_xlim(2020, 2099)
axs[1].tick_params(axis='both', which='major', labelsize=20)
#axs[1].set_xticks(np.arange(2020, 2100, 20),fontsize=20)


# Subplot for rcp85
axs[2].fill_between(contributions_80years_annual_do_rcp85_years, 0, gcm_contributions_80years_annual_do_rcp85, label='GCMs', alpha=0.7, color=colors[0], edgecolor='black')
axs[2].fill_between(contributions_80years_annual_do_rcp85_years, gcm_contributions_80years_annual_do_rcp85, gcm_contributions_80years_annual_do_rcp85 + param_contributions_80years_annual_do_rcp85, label='Parameters', alpha=0.7, color=colors[1], edgecolor='black')
axs[2].fill_between(contributions_80years_annual_do_rcp85_years, gcm_contributions_80years_annual_do_rcp85 + param_contributions_80years_annual_do_rcp85, gcm_contributions_80years_annual_do_rcp85 + param_contributions_80years_annual_do_rcp85 + interact_contributions_80years_annual_do_rcp85, label='Interactions', alpha=0.7, color=colors[2], edgecolor='black')
axs[2].set_title('(c) RCP8.5', fontsize=20)
axs[2].set_ylim(0,100)
axs[2].set_xlim(2020, 2099)
axs[2].tick_params(axis='both', which='major', labelsize=20)
#axs[2].set_xticks(np.arange(2020, 2100, 20),fontsize=20)


# Adding labels and title with increased font size
fig.text(0.08, 0.5, 'Uncertainty sources in hypolimnetic DO\n over deoxygenation period [%]', va='center', rotation='vertical', fontsize=22)

# Create legend handles and labels
legend_handles = [Patch(facecolor=colors[0], edgecolor='black'), 
                  Patch(facecolor=colors[1], edgecolor='black'), 
                  Patch(facecolor=colors[2], edgecolor='black')]
legend_labels = ['GCMs', 'Parameters', 'Interactions']

# Add a single legend outside the subplots
fig.legend(legend_handles, legend_labels,bbox_to_anchor=(0.57, 0.06), fontsize=22)



# Save the plot
plt.savefig('uncertainty_annual_do_80years_rcps.png', dpi=300, bbox_inches='tight')

plt.show()









#%%Plotting of monthly do


#%%Plot of Anova test on all_monthly_do_rcps




# the whole RCPs years


######rcp26

#years
contributions_monthly_do_rcp26_years=anova_monthly_do_rcp26['year']
#GCMs
gcm_contributions_monthly_do_rcp26 = anova_monthly_do_rcp26['GCMs']
#Param
param_contributions_monthly_do_rcp26 =anova_monthly_do_rcp26['param']
#interaction
interact_contributions_monthly_do_rcp26 =anova_monthly_do_rcp26['interaction']

######rcp60

#years
contributions_monthly_do_rcp60_years=anova_monthly_do_rcp60['year']
#GCMs
gcm_contributions_monthly_do_rcp60 = anova_monthly_do_rcp60['GCMs']
#Param
param_contributions_monthly_do_rcp60 =anova_monthly_do_rcp60['param']
#interaction
interact_contributions_monthly_do_rcp60 =anova_monthly_do_rcp60['interaction']




######rcp85

#years
contributions_monthly_do_rcp85_years=anova_monthly_do_rcp85['year']
#GCMs
gcm_contributions_monthly_do_rcp85 = anova_monthly_do_rcp85['GCMs']
#Param
param_contributions_monthly_do_rcp85 =anova_monthly_do_rcp85['param']
#interaction
interact_contributions_monthly_do_rcp85 =anova_monthly_do_rcp85['interaction']




######Plotting:

# Define the directory path
directory_path = r'C:\Users\mahta\OneDrive\Documents\PhD_py_code\Future_simulation_results\all_4_models\uncertainty'

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
axs[0].fill_between(contributions_monthly_do_rcp26_years, 0, gcm_contributions_monthly_do_rcp26, label='GCMs', alpha=0.7, color=colors[0], edgecolor='black')
axs[0].fill_between(contributions_monthly_do_rcp26_years, gcm_contributions_monthly_do_rcp26, gcm_contributions_monthly_do_rcp26 + param_contributions_monthly_do_rcp26, label='Parameters', alpha=0.7, color=colors[1], edgecolor='black')
axs[0].fill_between(contributions_monthly_do_rcp26_years, gcm_contributions_monthly_do_rcp26 + param_contributions_monthly_do_rcp26, gcm_contributions_monthly_do_rcp26 + param_contributions_monthly_do_rcp26 + interact_contributions_monthly_do_rcp26, label='Interactions', alpha=0.7, color=colors[2], edgecolor='black')
axs[0].set_title('(a) RCP2.6', fontsize=20)
axs[0].set_ylim(0,100)
axs[0].set_xlim(2006, 2099)
axs[0].tick_params(axis='both', which='major', labelsize=20)
#axs[0].set_xticks(np.arange(2006, 2100, 10),fontsize=20)

# Subplot for rcp60
axs[1].fill_between(contributions_monthly_do_rcp60_years, 0, gcm_contributions_monthly_do_rcp60, label='GCMs', alpha=0.7, color=colors[0], edgecolor='black')
axs[1].fill_between(contributions_monthly_do_rcp60_years, gcm_contributions_monthly_do_rcp60, gcm_contributions_monthly_do_rcp60 + param_contributions_monthly_do_rcp60, label='Parameters', alpha=0.7, color=colors[1], edgecolor='black')
axs[1].fill_between(contributions_monthly_do_rcp60_years, gcm_contributions_monthly_do_rcp60 + param_contributions_monthly_do_rcp60, gcm_contributions_monthly_do_rcp60 + param_contributions_monthly_do_rcp60 + interact_contributions_monthly_do_rcp60, label='Interactions', alpha=0.7, color=colors[2], edgecolor='black')
axs[1].set_title('(b) RCP6.0', fontsize=20)
axs[1].set_ylim(0,100)
axs[1].set_xlim(2006, 2099)
axs[1].tick_params(axis='both', which='major', labelsize=20)
#axs[1].set_xticks(np.arange(2006, 2100, 20),fontsize=20)


# Subplot for rcp85
axs[2].fill_between(contributions_monthly_do_rcp85_years, 0, gcm_contributions_monthly_do_rcp85, label='GCMs', alpha=0.7, color=colors[0], edgecolor='black')
axs[2].fill_between(contributions_monthly_do_rcp85_years, gcm_contributions_monthly_do_rcp85, gcm_contributions_monthly_do_rcp85 + param_contributions_monthly_do_rcp85, label='Parameters', alpha=0.7, color=colors[1], edgecolor='black')
axs[2].fill_between(contributions_monthly_do_rcp85_years, gcm_contributions_monthly_do_rcp85 + param_contributions_monthly_do_rcp85, gcm_contributions_monthly_do_rcp85 + param_contributions_monthly_do_rcp85 + interact_contributions_monthly_do_rcp85, label='Interactions', alpha=0.7, color=colors[2], edgecolor='black')
axs[2].set_title('(c) RCP8.5', fontsize=20)
axs[2].set_ylim(0,100)
axs[2].set_xlim(2006, 2099)
axs[2].tick_params(axis='both', which='major', labelsize=20)
#axs[2].set_xticks(np.arange(2006, 2100, 20),fontsize=20)


# Adding labels and title with increased font size
# fig.text(0.5, 0.08, 'Year', ha='center', fontsize=20)
fig.text(0.07, 0.5, 'Uncertainty sources in \n Apr-Oct deep DO [%]', va='center', rotation='vertical', fontsize=22)

# Create legend handles and labels
legend_handles = [Patch(facecolor=colors[0], edgecolor='black'), 
                  Patch(facecolor=colors[1], edgecolor='black'), 
                  Patch(facecolor=colors[2], edgecolor='black')]
legend_labels = ['GCMs', 'Parameters', 'Interactions']

# Add a single legend outside the subplots
fig.legend(legend_handles, legend_labels,bbox_to_anchor=(0.57, 0.06), fontsize=22)


# Save the plot
plt.savefig('uncertainty_monthly_do_allyears_rcps.png', dpi=300, bbox_inches='tight')

plt.show()




#%% analyses onley for 80 years


########rcp26

#year
contributions_80years_monthly_do_rcp26_years=anova_monthly_do_rcp26[anova_monthly_do_rcp26.year>2019].year
#gcms
gcm_contributions_80years_monthly_do_rcp26 = anova_monthly_do_rcp26[anova_monthly_do_rcp26.year>2019]['GCMs']
#param
param_contributions_80years_monthly_do_rcp26 =anova_monthly_do_rcp26[anova_monthly_do_rcp26.year>2019]['param']
#interaction
interact_contributions_80years_monthly_do_rcp26 =anova_monthly_do_rcp26[anova_monthly_do_rcp26.year>2019]['interaction']



#########rcp60

#year
contributions_80years_monthly_do_rcp60_years=anova_monthly_do_rcp60[anova_monthly_do_rcp60.year>2019].year
#gcms
gcm_contributions_80years_monthly_do_rcp60 = anova_monthly_do_rcp60[anova_monthly_do_rcp60.year>2019]['GCMs']
#param
param_contributions_80years_monthly_do_rcp60 =anova_monthly_do_rcp60[anova_monthly_do_rcp60.year>2019]['param']
#interaction
interact_contributions_80years_monthly_do_rcp60 =anova_monthly_do_rcp60[anova_monthly_do_rcp60.year>2019]['interaction']


##########rcp85
#year
contributions_80years_monthly_do_rcp85_years=anova_monthly_do_rcp85[anova_monthly_do_rcp85.year>2019].year
#gcms
gcm_contributions_80years_monthly_do_rcp85 = anova_monthly_do_rcp85[anova_monthly_do_rcp85.year>2019]['GCMs']
#param
param_contributions_80years_monthly_do_rcp85 =anova_monthly_do_rcp85[anova_monthly_do_rcp85.year>2019]['param']
#interaction
interact_contributions_80years_monthly_do_rcp85 =anova_monthly_do_rcp85[anova_monthly_do_rcp85.year>2019]['interaction']


######Plotting:
    
# Define the directory path
directory_path = r'C:\Users\mahta\OneDrive\Documents\PhD_py_code\Future_simulation_results\all_4_models\uncertainty'

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
axs[0].fill_between(contributions_80years_monthly_do_rcp26_years, 0, gcm_contributions_80years_monthly_do_rcp26, label='GCMs', alpha=0.7, color=colors[0], edgecolor='black')
axs[0].fill_between(contributions_80years_monthly_do_rcp26_years, gcm_contributions_80years_monthly_do_rcp26, gcm_contributions_80years_monthly_do_rcp26 + param_contributions_80years_monthly_do_rcp26, label='Parameters', alpha=0.7, color=colors[1], edgecolor='black')
axs[0].fill_between(contributions_80years_monthly_do_rcp26_years, gcm_contributions_80years_monthly_do_rcp26 + param_contributions_80years_monthly_do_rcp26, gcm_contributions_80years_monthly_do_rcp26 + param_contributions_80years_monthly_do_rcp26 + interact_contributions_80years_monthly_do_rcp26, label='Interactions', alpha=0.7, color=colors[2], edgecolor='black')
axs[0].set_title('(a) RCP2.6', fontsize=20)
axs[0].set_ylim(0,100)
axs[0].set_xlim(2020, 2099)
axs[0].tick_params(axis='both', which='major', labelsize=20)
#axs[0].set_xticks(np.arange(2020, 2100, 10),fontsize=20)

# Subplot for rcp60
axs[1].fill_between(contributions_80years_monthly_do_rcp60_years, 0, gcm_contributions_80years_monthly_do_rcp60, label='GCMs', alpha=0.7, color=colors[0], edgecolor='black')
axs[1].fill_between(contributions_80years_monthly_do_rcp60_years, gcm_contributions_80years_monthly_do_rcp60, gcm_contributions_80years_monthly_do_rcp60 + param_contributions_80years_monthly_do_rcp60, label='Parameters', alpha=0.7, color=colors[1], edgecolor='black')
axs[1].fill_between(contributions_80years_monthly_do_rcp60_years, gcm_contributions_80years_monthly_do_rcp60 + param_contributions_80years_monthly_do_rcp60, gcm_contributions_80years_monthly_do_rcp60 + param_contributions_80years_monthly_do_rcp60 + interact_contributions_80years_monthly_do_rcp60, label='Interactions', alpha=0.7, color=colors[2], edgecolor='black')
axs[1].set_title('(b) RCP6.0', fontsize=20)
axs[1].set_ylim(0,100)
axs[1].set_xlim(2020, 2099)
axs[1].tick_params(axis='both', which='major', labelsize=20)
#axs[1].set_xticks(np.arange(2020, 2100, 20),fontsize=20)


# Subplot for rcp85
axs[2].fill_between(contributions_80years_monthly_do_rcp85_years, 0, gcm_contributions_80years_monthly_do_rcp85, label='GCMs', alpha=0.7, color=colors[0], edgecolor='black')
axs[2].fill_between(contributions_80years_monthly_do_rcp85_years, gcm_contributions_80years_monthly_do_rcp85, gcm_contributions_80years_monthly_do_rcp85 + param_contributions_80years_monthly_do_rcp85, label='Parameters', alpha=0.7, color=colors[1], edgecolor='black')
axs[2].fill_between(contributions_80years_monthly_do_rcp85_years, gcm_contributions_80years_monthly_do_rcp85 + param_contributions_80years_monthly_do_rcp85, gcm_contributions_80years_monthly_do_rcp85 + param_contributions_80years_monthly_do_rcp85 + interact_contributions_80years_monthly_do_rcp85, label='Interactions', alpha=0.7, color=colors[2], edgecolor='black')
axs[2].set_title('(c) RCP8.5', fontsize=20)
axs[2].set_ylim(0,100)
axs[2].set_xlim(2020, 2099)
axs[2].tick_params(axis='both', which='major', labelsize=20)
#axs[2].set_xticks(np.arange(2020, 2100, 20),fontsize=20)


# Adding labels and title with increased font size
# fig.text(0.5, 0.08, 'Year', ha='center', fontsize=20)
fig.text(0.08, 0.5, 'Uncertainty sources in\n Apr-Oct deep DO [%]', va='center', rotation='vertical', fontsize=22)

# Create legend handles and labels
legend_handles = [Patch(facecolor=colors[0], edgecolor='black'), 
                  Patch(facecolor=colors[1], edgecolor='black'), 
                  Patch(facecolor=colors[2], edgecolor='black')]
legend_labels = ['GCMs', 'Parameters', 'Interactions']

# Add a single legend outside the subplots
fig.legend(legend_handles, legend_labels,bbox_to_anchor=(0.57, 0.06), fontsize=22)



# Save the plot
plt.savefig('uncertainty_monthly_do_80years_rcps.png', dpi=300, bbox_inches='tight')

plt.show()









#%%Plotting of summer DO rcp26, rcp60, and rcp85

#%%Plot of Anova test on all_summer_do_rcps

"""



# the whole RCPs years


######rcp26

#years
contributions_summer_do_rcp26_years=anova_summer_do_rcp26['year']
#GCMs
gcm_contributions_summer_do_rcp26 = anova_summer_do_rcp26['GCMs']
#Param
param_contributions_summer_do_rcp26 =anova_summer_do_rcp26['param']
#interaction
interact_contributions_summer_do_rcp26 =anova_summer_do_rcp26['interaction']

######rcp60

#years
contributions_summer_do_rcp60_years=anova_summer_do_rcp60['year']
#GCMs
gcm_contributions_summer_do_rcp60 = anova_summer_do_rcp60['GCMs']
#Param
param_contributions_summer_do_rcp60 =anova_summer_do_rcp60['param']
#interaction
interact_contributions_summer_do_rcp60 =anova_summer_do_rcp60['interaction']




######rcp85

#years
contributions_summer_do_rcp85_years=anova_summer_do_rcp85['year']
#GCMs
gcm_contributions_summer_do_rcp85 = anova_summer_do_rcp85['GCMs']
#Param
param_contributions_summer_do_rcp85 =anova_summer_do_rcp85['param']
#interaction
interact_contributions_summer_do_rcp85 =anova_summer_do_rcp85['interaction']




######Plotting:
    
# Define the directory path
directory_path = r'C:\Users\mahta\OneDrive\Documents\PhD_py_code\Future_simulation_results\all_4_models\uncertainty'

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
axs[0].fill_between(contributions_summer_do_rcp26_years, 0, gcm_contributions_summer_do_rcp26, label='GCMs', alpha=0.7, color=colors[0], edgecolor='black')
axs[0].fill_between(contributions_summer_do_rcp26_years, gcm_contributions_summer_do_rcp26, gcm_contributions_summer_do_rcp26 + param_contributions_summer_do_rcp26, label='Parameters', alpha=0.7, color=colors[1], edgecolor='black')
axs[0].fill_between(contributions_summer_do_rcp26_years, gcm_contributions_summer_do_rcp26 + param_contributions_summer_do_rcp26, gcm_contributions_summer_do_rcp26 + param_contributions_summer_do_rcp26 + interact_contributions_summer_do_rcp26, label='Interactions', alpha=0.7, color=colors[2], edgecolor='black')
axs[0].set_title('RCP2.6', fontsize=20)
axs[0].set_ylim(0,100)
axs[0].set_xlim(2006, 2099)
axs[0].tick_params(axis='both', which='major', labelsize=20)
#axs[0].set_xticks(np.arange(2006, 2100, 10),fontsize=20)

# Subplot for rcp60
axs[1].fill_between(contributions_summer_do_rcp60_years, 0, gcm_contributions_summer_do_rcp60, label='GCMs', alpha=0.7, color=colors[0], edgecolor='black')
axs[1].fill_between(contributions_summer_do_rcp60_years, gcm_contributions_summer_do_rcp60, gcm_contributions_summer_do_rcp60 + param_contributions_summer_do_rcp60, label='Parameters', alpha=0.7, color=colors[1], edgecolor='black')
axs[1].fill_between(contributions_summer_do_rcp60_years, gcm_contributions_summer_do_rcp60 + param_contributions_summer_do_rcp60, gcm_contributions_summer_do_rcp60 + param_contributions_summer_do_rcp60 + interact_contributions_summer_do_rcp60, label='Interactions', alpha=0.7, color=colors[2], edgecolor='black')
axs[1].set_title('RCP6.0', fontsize=20)
axs[1].set_ylim(0,100)
axs[1].set_xlim(2006, 2099)
axs[1].tick_params(axis='both', which='major', labelsize=20)
#axs[1].set_xticks(np.arange(2006, 2100, 20),fontsize=20)


# Subplot for rcp85
axs[2].fill_between(contributions_summer_do_rcp85_years, 0, gcm_contributions_summer_do_rcp85, label='GCMs', alpha=0.7, color=colors[0], edgecolor='black')
axs[2].fill_between(contributions_summer_do_rcp85_years, gcm_contributions_summer_do_rcp85, gcm_contributions_summer_do_rcp85 + param_contributions_summer_do_rcp85, label='Parameters', alpha=0.7, color=colors[1], edgecolor='black')
axs[2].fill_between(contributions_summer_do_rcp85_years, gcm_contributions_summer_do_rcp85 + param_contributions_summer_do_rcp85, gcm_contributions_summer_do_rcp85 + param_contributions_summer_do_rcp85 + interact_contributions_summer_do_rcp85, label='Interactions', alpha=0.7, color=colors[2], edgecolor='black')
axs[2].set_title('RCP8.5', fontsize=20)
axs[2].set_ylim(0,100)
axs[2].set_xlim(2006, 2099)
axs[2].tick_params(axis='both', which='major', labelsize=20)
#axs[2].set_xticks(np.arange(2006, 2100, 20),fontsize=20)


# Adding labels and title with increased font size
# fig.text(0.5, 0.08, 'Year', ha='center', fontsize=20)
fig.text(0.08, 0.5, 'Uncertainty sources in summer hypolimnetic DO [%]', va='center', rotation='vertical', fontsize=22)

# Create legend handles and labels
legend_handles = [Patch(facecolor=colors[0], edgecolor='black'), 
                  Patch(facecolor=colors[1], edgecolor='black'), 
                  Patch(facecolor=colors[2], edgecolor='black')]
legend_labels = ['GCMs', 'Parameters', 'Interactions']

# Add a single legend outside the subplots
fig.legend(legend_handles, legend_labels,bbox_to_anchor=(0.57, 0.06), fontsize=22)


# Save the plot
plt.savefig('uncertainty_summerdo_allyears_rcps.png', dpi=300, bbox_inches='tight')

plt.show()





#%% analyses onley for 80 years


########rcp26

#year
contributions_80years_summer_do_rcp26_years=anova_summer_do_rcp26[anova_summer_do_rcp26.year>2019].year
#gcms
gcm_contributions_80years_summer_do_rcp26 = anova_summer_do_rcp26[anova_summer_do_rcp26.year>2019]['GCMs']
#param
param_contributions_80years_summer_do_rcp26 =anova_summer_do_rcp26[anova_summer_do_rcp26.year>2019]['param']
#interaction
interact_contributions_80years_summer_do_rcp26 =anova_summer_do_rcp26[anova_summer_do_rcp26.year>2019]['interaction']



#########rcp60

#year
contributions_80years_summer_do_rcp60_years=anova_summer_do_rcp60[anova_summer_do_rcp60.year>2019].year
#gcms
gcm_contributions_80years_summer_do_rcp60 = anova_summer_do_rcp60[anova_summer_do_rcp60.year>2019]['GCMs']
#param
param_contributions_80years_summer_do_rcp60 =anova_summer_do_rcp60[anova_summer_do_rcp60.year>2019]['param']
#interaction
interact_contributions_80years_summer_do_rcp60 =anova_summer_do_rcp60[anova_summer_do_rcp60.year>2019]['interaction']


##########rcp85
#year
contributions_80years_summer_do_rcp85_years=anova_summer_do_rcp85[anova_summer_do_rcp85.year>2019].year
#gcms
gcm_contributions_80years_summer_do_rcp85 = anova_summer_do_rcp85[anova_summer_do_rcp85.year>2019]['GCMs']
#param
param_contributions_80years_summer_do_rcp85 =anova_summer_do_rcp85[anova_summer_do_rcp85.year>2019]['param']
#interaction
interact_contributions_80years_summer_do_rcp85 =anova_summer_do_rcp85[anova_summer_do_rcp85.year>2019]['interaction']


######Plotting:
# Define the directory path
directory_path = r'C:\Users\mahta\OneDrive\Documents\PhD_py_code\Future_simulation_results\all_4_models\uncertainty'

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
axs[0].fill_between(contributions_80years_summer_do_rcp26_years, 0, gcm_contributions_80years_summer_do_rcp26, label='GCMs', alpha=0.7, color=colors[0], edgecolor='black')
axs[0].fill_between(contributions_80years_summer_do_rcp26_years, gcm_contributions_80years_summer_do_rcp26, gcm_contributions_80years_summer_do_rcp26 + param_contributions_80years_summer_do_rcp26, label='Parameters', alpha=0.7, color=colors[1], edgecolor='black')
axs[0].fill_between(contributions_80years_summer_do_rcp26_years, gcm_contributions_80years_summer_do_rcp26 + param_contributions_80years_summer_do_rcp26, gcm_contributions_80years_summer_do_rcp26 + param_contributions_80years_summer_do_rcp26 + interact_contributions_80years_summer_do_rcp26, label='Interactions', alpha=0.7, color=colors[2], edgecolor='black')
axs[0].set_title('RCP2.6', fontsize=20)
axs[0].set_ylim(0,100)
axs[0].set_xlim(2020, 2099)
axs[0].tick_params(axis='both', which='major', labelsize=20)
#axs[0].set_xticks(np.arange(2020, 2100, 10),fontsize=20)

# Subplot for rcp60
axs[1].fill_between(contributions_80years_summer_do_rcp60_years, 0, gcm_contributions_80years_summer_do_rcp60, label='GCMs', alpha=0.7, color=colors[0], edgecolor='black')
axs[1].fill_between(contributions_80years_summer_do_rcp60_years, gcm_contributions_80years_summer_do_rcp60, gcm_contributions_80years_summer_do_rcp60 + param_contributions_80years_summer_do_rcp60, label='Parameters', alpha=0.7, color=colors[1], edgecolor='black')
axs[1].fill_between(contributions_80years_summer_do_rcp60_years, gcm_contributions_80years_summer_do_rcp60 + param_contributions_80years_summer_do_rcp60, gcm_contributions_80years_summer_do_rcp60 + param_contributions_80years_summer_do_rcp60 + interact_contributions_80years_summer_do_rcp60, label='Interactions', alpha=0.7, color=colors[2], edgecolor='black')
axs[1].set_title('RCP6.0', fontsize=20)
axs[1].set_ylim(0,100)
axs[1].set_xlim(2020, 2099)
axs[1].tick_params(axis='both', which='major', labelsize=20)
#axs[1].set_xticks(np.arange(2020, 2100, 20),fontsize=20)


# Subplot for rcp85
axs[2].fill_between(contributions_80years_summer_do_rcp85_years, 0, gcm_contributions_80years_summer_do_rcp85, label='GCMs', alpha=0.7, color=colors[0], edgecolor='black')
axs[2].fill_between(contributions_80years_summer_do_rcp85_years, gcm_contributions_80years_summer_do_rcp85, gcm_contributions_80years_summer_do_rcp85 + param_contributions_80years_summer_do_rcp85, label='Parameters', alpha=0.7, color=colors[1], edgecolor='black')
axs[2].fill_between(contributions_80years_summer_do_rcp85_years, gcm_contributions_80years_summer_do_rcp85 + param_contributions_80years_summer_do_rcp85, gcm_contributions_80years_summer_do_rcp85 + param_contributions_80years_summer_do_rcp85 + interact_contributions_80years_summer_do_rcp85, label='Interactions', alpha=0.7, color=colors[2], edgecolor='black')
axs[2].set_title('RCP8.5', fontsize=20)
axs[2].set_ylim(0,100)
axs[2].set_xlim(2020, 2099)
axs[2].tick_params(axis='both', which='major', labelsize=20)
#axs[2].set_xticks(np.arange(2020, 2100, 20),fontsize=20)


# Adding labels and title with increased font size
# fig.text(0.5, 0.08, 'Year', ha='center', fontsize=20)
fig.text(0.08, 0.5, 'Uncertainty sources in summer hypolimnetic DO [%]', va='center', rotation='vertical', fontsize=22)

# Create legend handles and labels
legend_handles = [Patch(facecolor=colors[0], edgecolor='black'), 
                  Patch(facecolor=colors[1], edgecolor='black'), 
                  Patch(facecolor=colors[2], edgecolor='black')]
legend_labels = ['GCMs', 'Parameters', 'Interactions']

# Add a single legend outside the subplots
fig.legend(legend_handles, legend_labels,bbox_to_anchor=(0.57, 0.06), fontsize=22)



# Save the plot
plt.savefig('uncertainty_summer_do_80years_rcps.png', dpi=300, bbox_inches='tight')

plt.show()

"""
















#%%monthly_hypolimnetic_ave

#%%monthly_do_gfdl_his

# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/his'

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
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = monthly_hypolimnetic_ave(C, Vr, time_series )

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_hypolimnetic_ave_gfdl_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        


#%%monthly_hypolimnetic_ave_gfdl_rcp26

# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp26'

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
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = monthly_hypolimnetic_ave(C, Vr, time_series )

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_hypolimnetic_ave_gfdl_rcp26_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
 

#%%monthly_hypolimnetic_ave_gfdl_rcp60

# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp60'

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
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = monthly_hypolimnetic_ave(C, Vr, time_series )

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_hypolimnetic_ave_gfdl_rcp60_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        

#%%monthly_hypolimnetic_ave_gfdl_rcp85

# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp85'

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
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = monthly_hypolimnetic_ave(C, Vr, time_series )

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_hypolimnetic_ave_gfdl_rcp85_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                
#%%hadgem

#%%monthly_hypolimnetic_ave_hadgem_his

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
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = monthly_hypolimnetic_ave(C, Vr, time_series )

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_hypolimnetic_ave_hadgem_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
 
#%%monthly_hypolimnetic_ave_hadgem_rcp26

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
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = monthly_hypolimnetic_ave(C, Vr, time_series )

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_hypolimnetic_ave_hadgem_rcp26_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                

#%%monthly_hypolimnetic_ave_hadgem_rcp60

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
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = monthly_hypolimnetic_ave(C, Vr, time_series )

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_hypolimnetic_ave_hadgem_rcp60_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
   
#%%monthly_hypolimnetic_ave_hadgem_rcp85

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
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = monthly_hypolimnetic_ave(C, Vr, time_series )

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_hypolimnetic_ave_hadgem_rcp85_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
            
#%%ipsl

#%%monthly_hypolimnetic_ave_ipsl_his

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
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = monthly_hypolimnetic_ave(C, Vr, time_series )

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_hypolimnetic_ave_ipsl_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        

#%%monthly_hypolimnetic_ave_ipsl_rcp26

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
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = monthly_hypolimnetic_ave(C, Vr, time_series )

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_hypolimnetic_ave_ipsl_rcp26_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                

#%%monthly_hypolimnetic_ave_ipsl_rcp60

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
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = monthly_hypolimnetic_ave(C, Vr, time_series )

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_hypolimnetic_ave_ipsl_rcp60_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                


#%%monthly_hypolimnetic_ave_ipsl_rcp85

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
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = monthly_hypolimnetic_ave(C, Vr, time_series )

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_hypolimnetic_ave_ipsl_rcp85_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
  
#%%monthly_hypolimnetic_ave_miroc_his

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
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = monthly_hypolimnetic_ave(C, Vr, time_series )

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_hypolimnetic_ave_miroc_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
 
#%%monthly_hypolimnetic_ave_miroc_rcp26

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
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = monthly_hypolimnetic_ave(C, Vr, time_series )

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_hypolimnetic_ave_miroc_rcp26_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                

#%%monthly_hypolimnetic_ave_miroc_rcp60

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
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = monthly_hypolimnetic_ave(C, Vr, time_series )

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_hypolimnetic_ave_miroc_rcp60_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                



#%%monthly_hypolimnetic_ave_miroc_rcp85

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
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = monthly_hypolimnetic_ave(C, Vr, time_series )

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_hypolimnetic_ave_miroc_rcp85_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        


#%%sorting the indexs_annual_hypolimnetic_ave 

glue_df_annual_hypolimnetic_ave_his= glue_df_annual_hypolimnetic_ave_his.sort_index()
glue_df_annual_hypolimnetic_ave_rcp26= glue_df_annual_hypolimnetic_ave_rcp26.sort_index()
glue_df_annual_hypolimnetic_ave_rcp60= glue_df_annual_hypolimnetic_ave_rcp60.sort_index()
glue_df_annual_hypolimnetic_ave_rcp85= glue_df_annual_hypolimnetic_ave_rcp85.sort_index()


#%%sorting the indexs_monthly_hypolimnetic_ave 

glue_df_monthly_hypolimnetic_ave_his= glue_df_monthly_hypolimnetic_ave_his.sort_index()
glue_df_monthly_hypolimnetic_ave_rcp26= glue_df_monthly_hypolimnetic_ave_rcp26.sort_index()
glue_df_monthly_hypolimnetic_ave_rcp60= glue_df_monthly_hypolimnetic_ave_rcp60.sort_index()
glue_df_monthly_hypolimnetic_ave_rcp85= glue_df_monthly_hypolimnetic_ave_rcp85.sort_index()




#%%sorting the indexs_summer_hypolimnetic_ave 

glue_df_summer_hypolimnetic_ave_his= glue_df_summer_hypolimnetic_ave_his.sort_index()
glue_df_summer_hypolimnetic_ave_rcp26= glue_df_summer_hypolimnetic_ave_rcp26.sort_index()
glue_df_summer_hypolimnetic_ave_rcp60= glue_df_summer_hypolimnetic_ave_rcp60.sort_index()
glue_df_summer_hypolimnetic_ave_rcp85= glue_df_summer_hypolimnetic_ave_rcp85.sort_index()













#%%Plotting and analyses 



#%%########annual do

#%%ploting annual do

os.chdir('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/')

import matplotlib.pyplot as plt

fig =plt.figure(figsize=(15, 10))
ax= plt.subplot(111)


ax=plt.fill_between(glue_df_annual_hypolimnetic_ave_his.index.astype(float), glue_df_annual_hypolimnetic_ave_his['5%'], glue_df_annual_hypolimnetic_ave_his['95%'], color='grey', alpha=0.2 ,  label= 'His 90% CI')
ax=plt.plot(glue_df_annual_hypolimnetic_ave_his.index.astype(float), glue_df_annual_hypolimnetic_ave_his['50%'].astype(float), 'k', label='His median', alpha=0.9, linewidth=3  )



ax=plt.fill_between(glue_df_annual_hypolimnetic_ave_rcp26.index.astype(float), glue_df_annual_hypolimnetic_ave_rcp26['5%'], glue_df_annual_hypolimnetic_ave_rcp26['95%'], color='darkgreen', alpha=0.3 ,  label= 'RCP2.6 90% CI')
ax=plt.plot(glue_df_annual_hypolimnetic_ave_rcp26.index.astype(float), glue_df_annual_hypolimnetic_ave_rcp26['50%'], 'darkgreen', label='RCP2.6 median', alpha=0.9, linewidth=3  )


ax=plt.fill_between(glue_df_annual_hypolimnetic_ave_rcp60.index.astype(float), glue_df_annual_hypolimnetic_ave_rcp60['5%'], glue_df_annual_hypolimnetic_ave_rcp60['95%'], color='yellow', alpha=0.2 ,  label= 'RCP6.0 90% CI')
ax=plt.plot(glue_df_annual_hypolimnetic_ave_rcp60.index.astype(float), glue_df_annual_hypolimnetic_ave_rcp60['50%'], 'yellow', label='RCP6.0 median', alpha=0.9, linewidth=3  )

ax=plt.fill_between(glue_df_annual_hypolimnetic_ave_rcp85.index.astype(float), glue_df_annual_hypolimnetic_ave_rcp85['5%'], glue_df_annual_hypolimnetic_ave_rcp85['95%'], color='r', alpha=0.2 ,  label= 'RCP8.5 90% CI')
ax=plt.plot(glue_df_annual_hypolimnetic_ave_rcp85.index.astype(float), glue_df_annual_hypolimnetic_ave_rcp85['50%'], 'r', label='RCP8.5 median', alpha=0.9, linewidth=3  )

ax=plt.ylabel('Hypolimnetic DO per each deoxygenation period [mg L$^{-1}$]' , fontsize=26)
ax=plt.xlabel('Year' , fontsize=26)
ax=plt.yticks(fontsize= 22)
ax=plt.xticks(rotation=45 , fontsize=22)
ax=plt.legend(bbox_to_anchor=(1.1, -0.2), fontsize=22, ncol=4)   
fig.savefig("GLUE_Timeseries_annual_hypolimnetic_ave.png",  dpi=300, bbox_inches='tight')




#%%
np.mean(glue_df_annual_hypolimnetic_ave_his['50%'])#4.609596756177265
np.mean(glue_df_annual_hypolimnetic_ave_rcp26['50%'])#4.184518602288504
np.mean(glue_df_annual_hypolimnetic_ave_rcp60['50%'])#3.971564759760348
np.mean(glue_df_annual_hypolimnetic_ave_rcp85['50%'])#3.8434305500383124

#%%anoxic_factor 30 yerars from each scenarios compare 



#anormaly 
# baseline [1976-2005]
glue_base_annual_hypolimnetic_ave_his=glue_df_annual_hypolimnetic_ave_his[1975 < glue_df_annual_hypolimnetic_ave_his.index]['50%']
annual_hypolimnetic_ave_ref=np.mean(glue_base_annual_hypolimnetic_ave_his)
#4.613891885145245


#near future [2030-2059]

glue_near_future_annual_hypolimnetic_ave_rcp26=glue_df_annual_hypolimnetic_ave_rcp26[(2029 < glue_df_annual_hypolimnetic_ave_rcp26.index) & (glue_df_annual_hypolimnetic_ave_rcp26.index < 2060)]['50%']
np.mean(glue_near_future_annual_hypolimnetic_ave_rcp26)
#  4.174146060868154
glue_near_future_annual_hypolimnetic_ave_rcp60=glue_df_annual_hypolimnetic_ave_rcp60[(2029 < glue_df_annual_hypolimnetic_ave_rcp60.index) & (glue_df_annual_hypolimnetic_ave_rcp60.index < 2060)]['50%']
np.mean(glue_near_future_annual_hypolimnetic_ave_rcp60)
#4.058613738110313
glue_near_future_annual_hypolimnetic_ave_rcp85=glue_df_annual_hypolimnetic_ave_rcp85[(2029 < glue_df_annual_hypolimnetic_ave_rcp85.index) & (glue_df_annual_hypolimnetic_ave_rcp85.index < 2060)]['50%']
np.mean(glue_near_future_annual_hypolimnetic_ave_rcp85)
# 3.9832593182266893

 
#Distant future [2070-2099]

glue_distant_future_annual_hypolimnetic_ave_rcp26=glue_df_annual_hypolimnetic_ave_rcp26[(2069 < glue_df_annual_hypolimnetic_ave_rcp26.index) & (glue_df_annual_hypolimnetic_ave_rcp26.index < 2100)]['50%']
np.mean(glue_distant_future_annual_hypolimnetic_ave_rcp26)
#4.217150264508205
glue_distant_future_annual_hypolimnetic_ave_rcp60=glue_df_annual_hypolimnetic_ave_rcp60[(2069 < glue_df_annual_hypolimnetic_ave_rcp60.index) & (glue_df_annual_hypolimnetic_ave_rcp60.index< 2100)]['50%']
np.mean(glue_distant_future_annual_hypolimnetic_ave_rcp60)
#3.690863672475098
glue_distant_future_annual_hypolimnetic_ave_rcp85=glue_df_annual_hypolimnetic_ave_rcp85[(2069 < glue_df_annual_hypolimnetic_ave_rcp85.index) & (glue_df_annual_hypolimnetic_ave_rcp85.index < 2100)]['50%']
np.mean(glue_distant_future_annual_hypolimnetic_ave_rcp85)
# 3.4556821721461737
   


###====over 30 years in his and each RCPs 

# baseline [1976-2005]
autocorr_MK_org_modif_sens_slope_test(glue_base_annual_hypolimnetic_ave_his)
(0.024889050164759213,
 'positively autocorrelated',
 'no trend',
 0.6737680588269763,
 0,
 0)


#near future [2030-2059]


autocorr_MK_org_modif_sens_slope_test(glue_near_future_annual_hypolimnetic_ave_rcp26)
(0.01564847901234311,
 'positively autocorrelated',
 'no trend',
 0.45968986302260806,
 0,
 0)

autocorr_MK_org_modif_sens_slope_test(glue_near_future_annual_hypolimnetic_ave_rcp60)
(0.013811164267201246,
 'positively autocorrelated',
 'no trend',
 0.05860441886618495,
 0,
 0)

autocorr_MK_org_modif_sens_slope_test(glue_near_future_annual_hypolimnetic_ave_rcp85)
(0.024200079051438957,
 'positively autocorrelated',
 'no trend',
 0.1434770815195705,
 0,
 0)



#Distant future [2070-2099]


autocorr_MK_org_modif_sens_slope_test(glue_distant_future_annual_hypolimnetic_ave_rcp26)
(0.014006453046156905,
 'positively autocorrelated',
 'no trend',
 0.4324504235358999,
 0,
 0)

autocorr_MK_org_modif_sens_slope_test(glue_distant_future_annual_hypolimnetic_ave_rcp60)
(0.019728764803858295,
 'positively autocorrelated',
 'no trend',
 0.9147523390847367,
 0,
 0)
autocorr_MK_org_modif_sens_slope_test(glue_distant_future_annual_hypolimnetic_ave_rcp85)

(0.024277783906209317,
 'positively autocorrelated',
 'no trend',
 0.617392769071009,
 0,
 0)





#%% 80 years from 2020 for annual_hypolimnetic_ave


glue_80years_annual_hypolimnetic_ave_rcp26=glue_df_annual_hypolimnetic_ave_rcp26[2019 < glue_df_annual_hypolimnetic_ave_rcp26.index]

glue_80years_annual_hypolimnetic_ave_rcp60=glue_df_annual_hypolimnetic_ave_rcp60[2019 < glue_df_annual_hypolimnetic_ave_rcp60.index]

glue_80years_annual_hypolimnetic_ave_rcp85=glue_df_annual_hypolimnetic_ave_rcp85[2019 < glue_df_annual_hypolimnetic_ave_rcp85.index]


#============= mean of first 10 yaers over 80 years 

#rcp2.6
np.mean(glue_80years_annual_hypolimnetic_ave_rcp26[glue_80years_annual_hypolimnetic_ave_rcp26.index<2030]['50%'])
4.075227960784212

#rcp6.0
np.mean(glue_80years_annual_hypolimnetic_ave_rcp60[glue_80years_annual_hypolimnetic_ave_rcp60.index<2030]['50%'])
4.267678912848086

#rcp8.5
np.mean(glue_80years_annual_hypolimnetic_ave_rcp85[glue_80years_annual_hypolimnetic_ave_rcp85.index<2030]['50%'])
 4.101546754158499

#============== mean of last 10 yaers over 80 years 

#rcp2.6
np.mean(glue_80years_annual_hypolimnetic_ave_rcp26[glue_80years_annual_hypolimnetic_ave_rcp26.index>2079]['50%'])
4.2130729481914235

#rcp6.0
np.mean(glue_80years_annual_hypolimnetic_ave_rcp60[glue_80years_annual_hypolimnetic_ave_rcp60.index>2079]['50%'])
3.7141909010679006

#rcp8.5
np.mean(glue_80years_annual_hypolimnetic_ave_rcp85[glue_80years_annual_hypolimnetic_ave_rcp85.index>2079]['50%'])
3.4778668896763256

#=========== trendline # Over the 80 years


autocorr_MK_org_modif_sens_slope_test(glue_80years_annual_hypolimnetic_ave_rcp26['50%'])
(0.020437372056957975,
 'positively autocorrelated',
 'no trend',
 0.6465146170427558,
 0,
 0)
autocorr_MK_org_modif_sens_slope_test(glue_80years_annual_hypolimnetic_ave_rcp60['50%'])

(0.017656470550551733,
 'positively autocorrelated',
 'decreasing',
 4.269529974010311e-08,
 -0.00955520515995046,
 4.294398532888216)

autocorr_MK_org_modif_sens_slope_test(glue_80years_annual_hypolimnetic_ave_rcp85['50%'])
(0.022833788524830017,
 'positively autocorrelated',
 'decreasing',
 1.7660877249525697e-07,
 -0.010995355387484442,
 4.2255920752661025)



#%%If there is a trend in entire 

# in whole his
autocorr_MK_org_modif_sens_slope_test(glue_df_annual_hypolimnetic_ave_his['50%'])
(0.03620882677974085,
 'positively autocorrelated',
 'no trend',
 0.5531533662908403,
 0,
 0)

#in intire rcp2.6
autocorr_MK_org_modif_sens_slope_test(glue_df_annual_hypolimnetic_ave_rcp26['50%'])
(0.01875570448782784,
 'positively autocorrelated',
 'no trend',
 0.4505722805611243,
 0,
 0)

#in entire rcp6.0
autocorr_MK_org_modif_sens_slope_test(glue_df_annual_hypolimnetic_ave_rcp60['50%'])
(0.017258975018624268,
 'positively autocorrelated',
 'decreasing',
 3.820487819217178e-06,
 -0.007687167867926738,
 4.290304701873718)


#in entire rcp8.5
autocorr_MK_org_modif_sens_slope_test(glue_df_annual_hypolimnetic_ave_rcp85['50%'])
(0.023626023381098597,
 'positively autocorrelated',
 'decreasing',
 0.0,
 -0.010971782425621801,
 4.347534599132159)

#slope in entire RCP8.5> RCP6.0>RCP2.6 # his no trend 



 
#%%do_anormaly 
os.chdir('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/')

import matplotlib.pyplot as plt

fig =plt.figure(figsize=(15, 10))
ax= plt.subplot(111)


ax=plt.fill_between(glue_df_annual_hypolimnetic_ave_his[(1975 < glue_df_annual_hypolimnetic_ave_his.index)].index.astype(float),
                      glue_df_annual_hypolimnetic_ave_his[(1975 < glue_df_annual_hypolimnetic_ave_his.index)]['5%'] - annual_hypolimnetic_ave_ref,
                      glue_df_annual_hypolimnetic_ave_his[(1975 < glue_df_annual_hypolimnetic_ave_his.index) ]['95%'] - annual_hypolimnetic_ave_ref,
                      color='grey', alpha=0.2, label='His 90% CI')


ax=plt.plot(glue_df_annual_hypolimnetic_ave_his[(1975 < glue_df_annual_hypolimnetic_ave_his.index) ].index.astype(float),
            glue_df_annual_hypolimnetic_ave_his[(1975 < glue_df_annual_hypolimnetic_ave_his.index)]['50%'] - annual_hypolimnetic_ave_ref,
            'k', label='His median', alpha=0.9, linewidth=3   )

ax=plt.fill_between(glue_df_annual_hypolimnetic_ave_rcp26.index.astype(float), glue_df_annual_hypolimnetic_ave_rcp26['5%']-annual_hypolimnetic_ave_ref, glue_df_annual_hypolimnetic_ave_rcp26['95%']-annual_hypolimnetic_ave_ref, color='darkgreen', alpha=0.3 ,  label= 'RCP6.0 90% CI')
ax=plt.plot(glue_df_annual_hypolimnetic_ave_rcp26.index.astype(float), glue_df_annual_hypolimnetic_ave_rcp26['50%']-annual_hypolimnetic_ave_ref, 'darkgreen', label='RCP6.0 median', alpha=0.9, linewidth=3  )
                      
                     
ax=plt.fill_between(glue_df_annual_hypolimnetic_ave_rcp60.index.astype(float), glue_df_annual_hypolimnetic_ave_rcp60['5%']-annual_hypolimnetic_ave_ref, glue_df_annual_hypolimnetic_ave_rcp60['95%']-annual_hypolimnetic_ave_ref, color='yellow', alpha=0.2 ,  label= 'RCP6.0 90% CI')
ax=plt.plot(glue_df_annual_hypolimnetic_ave_rcp60.index.astype(float), glue_df_annual_hypolimnetic_ave_rcp60['50%']-annual_hypolimnetic_ave_ref, 'yellow', label='RCP6.0 median', alpha=0.9, linewidth=3  )

ax=plt.fill_between(glue_df_annual_hypolimnetic_ave_rcp85.index.astype(float), glue_df_annual_hypolimnetic_ave_rcp85['5%']-annual_hypolimnetic_ave_ref, glue_df_annual_hypolimnetic_ave_rcp85['95%']-annual_hypolimnetic_ave_ref, color='r', alpha=0.2 ,  label= 'RCP8.5 90% CI')
ax=plt.plot(glue_df_annual_hypolimnetic_ave_rcp85.index.astype(float), glue_df_annual_hypolimnetic_ave_rcp85['50%']-annual_hypolimnetic_ave_ref, 'r', label='RCP8.5 median', alpha=0.9, linewidth=3  )

ax=plt.ylabel('Anormaly of DO in deoxygenation period [mg L$^{-1}$]' , fontsize=26)
ax=plt.xlabel('Year' , fontsize=26)
ax=plt.yticks(fontsize= 22)
ax=plt.xticks(rotation=45 , fontsize=22)
ax=plt.legend(bbox_to_anchor=(1.1, -0.2), fontsize=22, ncol=4)
fig.savefig("GLUE_Timeseries_annual_hypolimnetic_ave_anormaly.png",  dpi=300, bbox_inches='tight')











#%%===========Apr-Oct average do


#%%ploting monthly do

os.chdir('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/')

import matplotlib.pyplot as plt

fig =plt.figure(figsize=(15, 10))
ax= plt.subplot(111)


ax=plt.fill_between(glue_df_monthly_hypolimnetic_ave_his.index.astype(float), glue_df_monthly_hypolimnetic_ave_his['5%'], glue_df_monthly_hypolimnetic_ave_his['95%'], color='grey', alpha=0.2 ,  label= 'His 90% CI')
ax=plt.plot(glue_df_monthly_hypolimnetic_ave_his.index.astype(float), glue_df_monthly_hypolimnetic_ave_his['50%'].astype(float), 'k', label='His median', alpha=0.9, linewidth=3  )



ax=plt.fill_between(glue_df_monthly_hypolimnetic_ave_rcp26.index.astype(float), glue_df_monthly_hypolimnetic_ave_rcp26['5%'], glue_df_monthly_hypolimnetic_ave_rcp26['95%'], color='darkgreen', alpha=0.3 ,  label= 'RCP2.6 90% CI')
ax=plt.plot(glue_df_monthly_hypolimnetic_ave_rcp26.index.astype(float), glue_df_monthly_hypolimnetic_ave_rcp26['50%'], 'darkgreen', label='RCP2.6 median', alpha=0.9, linewidth=3  )


ax=plt.fill_between(glue_df_monthly_hypolimnetic_ave_rcp60.index.astype(float), glue_df_monthly_hypolimnetic_ave_rcp60['5%'], glue_df_monthly_hypolimnetic_ave_rcp60['95%'], color='yellow', alpha=0.2 ,  label= 'RCP6.0 90% CI')
ax=plt.plot(glue_df_monthly_hypolimnetic_ave_rcp60.index.astype(float), glue_df_monthly_hypolimnetic_ave_rcp60['50%'], 'yellow', label='RCP6.0 median', alpha=0.9, linewidth=3  )

ax=plt.fill_between(glue_df_monthly_hypolimnetic_ave_rcp85.index.astype(float), glue_df_monthly_hypolimnetic_ave_rcp85['5%'], glue_df_monthly_hypolimnetic_ave_rcp85['95%'], color='r', alpha=0.2 ,  label= 'RCP8.5 90% CI')
ax=plt.plot(glue_df_monthly_hypolimnetic_ave_rcp85.index.astype(float), glue_df_monthly_hypolimnetic_ave_rcp85['50%'], 'r', label='RCP8.5 median', alpha=0.9, linewidth=3  )

ax=plt.ylabel('Deep DO in Apr-Oct [mg L$^{-1}$]' , fontsize=26)
ax=plt.xlabel('Year' , fontsize=26)
ax=plt.yticks(fontsize= 22)
ax=plt.xticks(rotation=45 , fontsize=22)
ax=plt.legend(bbox_to_anchor=(1.1, -0.2), fontsize=22, ncol=4)
fig.savefig("GLUE_Timeseries_monthly_hypolimnetic_ave.png",  dpi=300, bbox_inches='tight')




#%%
np.mean(glue_df_monthly_hypolimnetic_ave_his['50%'])# 7.66120828881849
np.mean(glue_df_monthly_hypolimnetic_ave_rcp26['50%'])#6.618663963770041
np.mean(glue_df_monthly_hypolimnetic_ave_rcp60['50%'])#6.320917663879071
np.mean(glue_df_monthly_hypolimnetic_ave_rcp85['50%'])# 6.046266677458798

#%% DO ave 30 yerars from each scenarios compare 



#anormaly 
# baseline [1976-2005]
glue_base_monthly_hypolimnetic_ave_his=glue_df_monthly_hypolimnetic_ave_his[1975 < glue_df_monthly_hypolimnetic_ave_his.index]['50%']
monthly_hypolimnetic_ave_ref=np.mean(glue_base_monthly_hypolimnetic_ave_his)
#7.465172317841294


#near future [2030-2059]

glue_near_future_monthly_hypolimnetic_ave_rcp26=glue_df_monthly_hypolimnetic_ave_rcp26[(2029 < glue_df_monthly_hypolimnetic_ave_rcp26.index) & (glue_df_monthly_hypolimnetic_ave_rcp26.index < 2060)]['50%']
np.mean(glue_near_future_monthly_hypolimnetic_ave_rcp26)
#6.574537233503323
glue_near_future_monthly_hypolimnetic_ave_rcp60=glue_df_monthly_hypolimnetic_ave_rcp60[(2029 < glue_df_monthly_hypolimnetic_ave_rcp60.index) & (glue_df_monthly_hypolimnetic_ave_rcp60.index < 2060)]['50%']
np.mean(glue_near_future_monthly_hypolimnetic_ave_rcp60)
#6.561144009819908
glue_near_future_monthly_hypolimnetic_ave_rcp85=glue_df_monthly_hypolimnetic_ave_rcp85[(2029 < glue_df_monthly_hypolimnetic_ave_rcp85.index) & (glue_df_monthly_hypolimnetic_ave_rcp85.index < 2060)]['50%']
np.mean(glue_near_future_monthly_hypolimnetic_ave_rcp85)
#6.299591511076445

 
#Distant future [2070-2099]

glue_distant_future_monthly_hypolimnetic_ave_rcp26=glue_df_monthly_hypolimnetic_ave_rcp26[(2069 < glue_df_monthly_hypolimnetic_ave_rcp26.index) & (glue_df_monthly_hypolimnetic_ave_rcp26.index < 2100)]['50%']
np.mean(glue_distant_future_monthly_hypolimnetic_ave_rcp26)
# 6.54711884303469
glue_distant_future_monthly_hypolimnetic_ave_rcp60=glue_df_monthly_hypolimnetic_ave_rcp60[(2069 < glue_df_monthly_hypolimnetic_ave_rcp60.index) & (glue_df_monthly_hypolimnetic_ave_rcp60.index< 2100)]['50%']
np.mean(glue_distant_future_monthly_hypolimnetic_ave_rcp60)
#5.731843635207613
glue_distant_future_monthly_hypolimnetic_ave_rcp85=glue_df_monthly_hypolimnetic_ave_rcp85[(2069 < glue_df_monthly_hypolimnetic_ave_rcp85.index) & (glue_df_monthly_hypolimnetic_ave_rcp85.index < 2100)]['50%']
np.mean(glue_distant_future_monthly_hypolimnetic_ave_rcp85)
#5.1425077069543
   


###====over 30 years in his and each RCPs 

# baseline [1976-2005]
autocorr_MK_org_modif_sens_slope_test(glue_base_monthly_hypolimnetic_ave_his)

(0.0049689279926895735,
 'positively autocorrelated',
 'decreasing',
 0.00021835210907172886,
 -0.025659289968822507,
 7.789681561684974)

#near future [2030-2059]


autocorr_MK_org_modif_sens_slope_test(glue_near_future_monthly_hypolimnetic_ave_rcp26)
(0.0054211386881630776,
 'positively autocorrelated',
 'no trend',
 0.12494881685497083,
 0,
 0)

autocorr_MK_org_modif_sens_slope_test(glue_near_future_monthly_hypolimnetic_ave_rcp60)
(0.0033649474535589335,
 'positively autocorrelated',
 'decreasing',
 0.00010051524183496419,
 -0.03319383060779364,
 7.021021889499194)

autocorr_MK_org_modif_sens_slope_test(glue_near_future_monthly_hypolimnetic_ave_rcp85)

(0.005930259590855618,
 'positively autocorrelated',
 'decreasing',
 0.003060340147684304,
 -0.025921780375820342,
 6.7187425682525035)



#Distant future [2070-2099]


autocorr_MK_org_modif_sens_slope_test(glue_distant_future_monthly_hypolimnetic_ave_rcp26)
(0.0052981790674006815,
 'positively autocorrelated',
 'no trend',
 0.12494881685497083,
 0,
 0)
autocorr_MK_org_modif_sens_slope_test(glue_distant_future_monthly_hypolimnetic_ave_rcp60)
(0.007255670863577943,
 'positively autocorrelated',
 'no trend',
 0.17512514633807807,
 0,
 0)

autocorr_MK_org_modif_sens_slope_test(glue_distant_future_monthly_hypolimnetic_ave_rcp85)
(0.01356930182943364,
 'positively autocorrelated',
 'no trend',
 0.13396533563924473,
 0,
 0)





#%% 80 years from 2020 for monthly_hypolimnetic_ave


glue_80years_monthly_hypolimnetic_ave_rcp26=glue_df_monthly_hypolimnetic_ave_rcp26[2019 < glue_df_monthly_hypolimnetic_ave_rcp26.index]

glue_80years_monthly_hypolimnetic_ave_rcp60=glue_df_monthly_hypolimnetic_ave_rcp60[2019 < glue_df_monthly_hypolimnetic_ave_rcp60.index]

glue_80years_monthly_hypolimnetic_ave_rcp85=glue_df_monthly_hypolimnetic_ave_rcp85[2019 < glue_df_monthly_hypolimnetic_ave_rcp85.index]


#============= mean of first 10 yaers over 80 years 

#rcp2.6
np.mean(glue_80years_monthly_hypolimnetic_ave_rcp26[glue_80years_monthly_hypolimnetic_ave_rcp26.index<2030]['50%'])
6.780510509648041

#rcp6.0
np.mean(glue_80years_monthly_hypolimnetic_ave_rcp60[glue_80years_monthly_hypolimnetic_ave_rcp60.index<2030]['50%'])
6.668492432706732

#rcp8.5
np.mean(glue_80years_monthly_hypolimnetic_ave_rcp85[glue_80years_monthly_hypolimnetic_ave_rcp85.index<2030]['50%'])
6.80574306302246

#============== mean of last 10 yaers over 80 years 

#rcp2.6
np.mean(glue_80years_monthly_hypolimnetic_ave_rcp26[glue_80years_monthly_hypolimnetic_ave_rcp26.index>2079]['50%'])
6.478420701054451

#rcp6.0
np.mean(glue_80years_monthly_hypolimnetic_ave_rcp60[glue_80years_monthly_hypolimnetic_ave_rcp60.index>2079]['50%'])
5.66996281068427

#rcp8.5
np.mean(glue_80years_monthly_hypolimnetic_ave_rcp85[glue_80years_monthly_hypolimnetic_ave_rcp85.index>2079]['50%'])
5.0637219573407135

#=========== trendline # Over the 80 years


autocorr_MK_org_modif_sens_slope_test(glue_80years_monthly_hypolimnetic_ave_rcp26['50%'])
(0.007228641245169112,
 'positively autocorrelated',
 'no trend',
 0.05036557719433388,
 0,
 0)


autocorr_MK_org_modif_sens_slope_test(glue_80years_monthly_hypolimnetic_ave_rcp60['50%'])
(0.005149619971573371,
 'positively autocorrelated',
 'decreasing',
 8.659739592076221e-15,
 -0.017910365763886014,
 6.865669521780572)

autocorr_MK_org_modif_sens_slope_test(glue_80years_monthly_hypolimnetic_ave_rcp85['50%'])
(0.00919092892308748,
 'positively autocorrelated',
 'decreasing',
 0.0,
 -0.028238858285751206,
 7.015950418686367)

#%%plotting monthly anoxic factor over 80 years 





os.chdir('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/')

import matplotlib.pyplot as plt

fig =plt.figure(figsize=(15, 10))
ax= plt.subplot(111)



ax=plt.fill_between(glue_80years_monthly_hypolimnetic_ave_rcp26.index.astype(float), glue_80years_monthly_hypolimnetic_ave_rcp26['5%'], glue_80years_monthly_hypolimnetic_ave_rcp26['95%'], color='darkgreen', alpha=0.3 ,  label= 'RCP2.6 90% CI')
ax=plt.plot(glue_80years_monthly_hypolimnetic_ave_rcp26.index.astype(float), glue_80years_monthly_hypolimnetic_ave_rcp26['50%'], 'darkgreen', label='RCP2.6 median', alpha=0.9, linewidth=3  )


ax=plt.fill_between(glue_80years_monthly_hypolimnetic_ave_rcp60.index.astype(float), glue_80years_monthly_hypolimnetic_ave_rcp60['5%'], glue_80years_monthly_hypolimnetic_ave_rcp60['95%'], color='yellow', alpha=0.3 ,  label= 'RCP6.0 90% CI')
ax=plt.plot(glue_80years_monthly_hypolimnetic_ave_rcp60.index.astype(float), glue_80years_monthly_hypolimnetic_ave_rcp60['50%'], 'yellow', label='RCP6.0 median', alpha=0.9, linewidth=3  )
trendline_rcp60=autocorr_MK_org_modif_sens_slope_test(glue_80years_monthly_hypolimnetic_ave_rcp60['50%'])
ax=plt.text(2020, 4, f'y = {trendline_rcp60[-2]:.3f}x + {trendline_rcp60[-1]:.3f}, p <0.0001', color='gold', fontsize= 20 )

ax=plt.plot(glue_80years_monthly_hypolimnetic_ave_rcp60.index.astype(float),
        trendline_rcp60[-2] * np.arange(80) + trendline_rcp60[-1],
        linestyle='--', color='yellow', alpha=0.9, linewidth=3)


ax=plt.fill_between(glue_80years_monthly_hypolimnetic_ave_rcp85.index.astype(float), glue_80years_monthly_hypolimnetic_ave_rcp85['5%'], glue_80years_monthly_hypolimnetic_ave_rcp85['95%'], color='r', alpha=0.2 ,  label= 'RCP8.5 90% CI')
ax=plt.plot(glue_80years_monthly_hypolimnetic_ave_rcp85.index.astype(float), glue_80years_monthly_hypolimnetic_ave_rcp85['50%'], 'r', label='RCP8.5 median', alpha=0.9, linewidth=3  )
trendline_rcp85=autocorr_MK_org_modif_sens_slope_test(glue_80years_monthly_hypolimnetic_ave_rcp85['50%'])
ax=plt.text(2020, 3.5, f'y = {trendline_rcp85[-2]:.3f}x + {trendline_rcp85[-1]:.3f},  p<0.0001', color='r', fontsize= 20 )


ax=plt.plot(glue_80years_monthly_hypolimnetic_ave_rcp85.index.astype(float),
        trendline_rcp85[-2] * np.arange(80) + trendline_rcp85[-1],
        linestyle='--', color='r', alpha=0.9, linewidth=3)



ax=plt.ylabel('Deep DO in Apr-Oct [mg L$^{-1}$]' , fontsize=26)
ax=plt.xlabel('Year' , fontsize=26)
ax=plt.yticks(fontsize= 22)
ax=plt.xticks(rotation=45 , fontsize=22)
ax=plt.legend(bbox_to_anchor=(0.95, -0.2), fontsize=22 , ncol= 3)   
fig.savefig("GLUE_Timeseries_80years_monthly_hypolimnetic_ave.png",  dpi=300, bbox_inches='tight')





#%%If there is a trend in entire 

# in whole his
autocorr_MK_org_modif_sens_slope_test(glue_df_monthly_hypolimnetic_ave_his['50%'])
(0.007529054652727127,
 'positively autocorrelated',
 'no trend',
 0.06551783432281777,
 0,
 0)
#in entire rcp2.6
autocorr_MK_org_modif_sens_slope_test(glue_df_monthly_hypolimnetic_ave_rcp26['50%'])
(0.006678617276411054,
 'positively autocorrelated',
 'decreasing',
 8.905891291033363e-05,
 -0.004229394071897694,
 6.807528520339308)

#in entire rcp6.0
autocorr_MK_org_modif_sens_slope_test(glue_df_monthly_hypolimnetic_ave_rcp60['50%'])
(0.005889288906858956,
 'positively autocorrelated',
 'decreasing',
 7.616129948928574e-14,
 -0.01685782626572829,
 7.124335972586037)

#in entire rcp8.5
autocorr_MK_org_modif_sens_slope_test(glue_df_monthly_hypolimnetic_ave_rcp85['50%'])
(0.008701602458554215,
 'positively autocorrelated',
 'decreasing',
 0.0,
 -0.02784969700079465,
 7.363125668936894)
#slope in entire RCP8.5> RCP6.0>RCP2.6 # his no trend 



 
#%%DO_anormaly 
os.chdir('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/')

import matplotlib.pyplot as plt

fig =plt.figure(figsize=(15, 10))
ax= plt.subplot(111)


ax=plt.fill_between(glue_df_monthly_hypolimnetic_ave_his[(1975 < glue_df_monthly_hypolimnetic_ave_his.index)].index.astype(float),
                      glue_df_monthly_hypolimnetic_ave_his[(1975< glue_df_monthly_hypolimnetic_ave_his.index)]['5%'] - monthly_hypolimnetic_ave_ref,
                      glue_df_monthly_hypolimnetic_ave_his[(1975 < glue_df_monthly_hypolimnetic_ave_his.index) ]['95%'] - monthly_hypolimnetic_ave_ref,
                      color='grey', alpha=0.2, label='His 90% CI')


ax=plt.plot(glue_df_monthly_hypolimnetic_ave_his[(1975 < glue_df_monthly_hypolimnetic_ave_his.index) ].index.astype(float),
            glue_df_monthly_hypolimnetic_ave_his[(1975 < glue_df_monthly_hypolimnetic_ave_his.index)]['50%'] - monthly_hypolimnetic_ave_ref,
            'k', label='His median', alpha=0.9, linewidth=3   )

ax=plt.fill_between(glue_df_monthly_hypolimnetic_ave_rcp26.index.astype(float), glue_df_monthly_hypolimnetic_ave_rcp26['5%']-monthly_hypolimnetic_ave_ref, glue_df_monthly_hypolimnetic_ave_rcp26['95%']-monthly_hypolimnetic_ave_ref, color='darkgreen', alpha=0.3 ,  label= 'RCP6.0 90% CI')
ax=plt.plot(glue_df_monthly_hypolimnetic_ave_rcp26.index.astype(float), glue_df_monthly_hypolimnetic_ave_rcp26['50%']-monthly_hypolimnetic_ave_ref, 'darkgreen', label='RCP6.0 median', alpha=0.9, linewidth=3  )
                      
                     
ax=plt.fill_between(glue_df_monthly_hypolimnetic_ave_rcp60.index.astype(float), glue_df_monthly_hypolimnetic_ave_rcp60['5%']-monthly_hypolimnetic_ave_ref, glue_df_monthly_hypolimnetic_ave_rcp60['95%']-monthly_hypolimnetic_ave_ref, color='yellow', alpha=0.3 ,  label= 'RCP6.0 90% CI')
ax=plt.plot(glue_df_monthly_hypolimnetic_ave_rcp60.index.astype(float), glue_df_monthly_hypolimnetic_ave_rcp60['50%']-monthly_hypolimnetic_ave_ref, 'yellow', label='RCP6.0 median', alpha=0.9, linewidth=3  )

ax=plt.fill_between(glue_df_monthly_hypolimnetic_ave_rcp85.index.astype(float), glue_df_monthly_hypolimnetic_ave_rcp85['5%']-monthly_hypolimnetic_ave_ref, glue_df_monthly_hypolimnetic_ave_rcp85['95%']-monthly_hypolimnetic_ave_ref, color='r', alpha=0.2 ,  label= 'RCP8.5 90% CI')
ax=plt.plot(glue_df_monthly_hypolimnetic_ave_rcp85.index.astype(float), glue_df_monthly_hypolimnetic_ave_rcp85['50%']-monthly_hypolimnetic_ave_ref, 'r', label='RCP8.5 median', alpha=0.9, linewidth=3  )

ax=plt.ylabel('Anormaly of Deep DO in Apr-Oct [mg L$^{-1}$]' , fontsize=26)
ax=plt.xlabel('Year' , fontsize=26)
ax=plt.yticks(fontsize= 22)
ax=plt.xticks(rotation=45 , fontsize=22)
ax=plt.legend(bbox_to_anchor=(1.1, -0.2), fontsize=22, ncol=4)  
fig.savefig("GLUE_Timeseries_monthly_hypolimnetic_ave_anormaly.png",  dpi=300, bbox_inches='tight')













#%%===========summer average of DO
"""

#%%########summer DO

#%%ploting summer DO

os.chdir('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/')

import matplotlib.pyplot as plt

fig =plt.figure(figsize=(15, 10))
ax= plt.subplot(111)


ax=plt.fill_between(glue_df_summer_hypolimnetic_ave_his.index.astype(float), glue_df_summer_hypolimnetic_ave_his['5%'], glue_df_summer_hypolimnetic_ave_his['95%'], color='grey', alpha=0.2 ,  label= 'His 90% CI')
ax=plt.plot(glue_df_summer_hypolimnetic_ave_his.index.astype(float), glue_df_summer_hypolimnetic_ave_his['50%'].astype(float), 'k', label='His median', alpha=0.9, linewidth=3  )



ax=plt.fill_between(glue_df_summer_hypolimnetic_ave_rcp26.index.astype(float), glue_df_summer_hypolimnetic_ave_rcp26['5%'], glue_df_summer_hypolimnetic_ave_rcp26['95%'], color='darkgreen', alpha=0.3 ,  label= 'RCP2.6 90% CI')
ax=plt.plot(glue_df_summer_hypolimnetic_ave_rcp26.index.astype(float), glue_df_summer_hypolimnetic_ave_rcp26['50%'], 'darkgreen', label='RCP2.6 median', alpha=0.9, linewidth=3  )


ax=plt.fill_between(glue_df_summer_hypolimnetic_ave_rcp60.index.astype(float), glue_df_summer_hypolimnetic_ave_rcp60['5%'], glue_df_summer_hypolimnetic_ave_rcp60['95%'], color='yellow', alpha=0.2 ,  label= 'RCP6.0 90% CI')
ax=plt.plot(glue_df_summer_hypolimnetic_ave_rcp60.index.astype(float), glue_df_summer_hypolimnetic_ave_rcp60['50%'], 'yellow', label='RCP6.0 median', alpha=0.9, linewidth=3  )

ax=plt.fill_between(glue_df_summer_hypolimnetic_ave_rcp85.index.astype(float), glue_df_summer_hypolimnetic_ave_rcp85['5%'], glue_df_summer_hypolimnetic_ave_rcp85['95%'], color='r', alpha=0.2 ,  label= 'RCP8.5 90% CI')
ax=plt.plot(glue_df_summer_hypolimnetic_ave_rcp85.index.astype(float), glue_df_summer_hypolimnetic_ave_rcp85['50%'], 'r', label='RCP8.5 median', alpha=0.9, linewidth=3  )

ax=plt.ylabel('Hypolimnetic DO in summer [mg L$^{-1}$]' , fontsize=26)
ax=plt.xlabel('Year' , fontsize=26)
ax=plt.yticks(fontsize= 22)
ax=plt.xticks(rotation=45 , fontsize=22)
ax=plt.legend(bbox_to_anchor=(0.7, -0.2), fontsize=22)#)   
fig.savefig("GLUE_Timeseries_summer_hypolimnetic_ave.png",  dpi=300, bbox_inches='tight')




#%%
np.mean(glue_df_summer_hypolimnetic_ave_his['50%'])#3.3877648031141754
np.mean(glue_df_summer_hypolimnetic_ave_rcp26['50%'])#2.4731856742174827
np.mean(glue_df_summer_hypolimnetic_ave_rcp60['50%'])#2.1550693101618354
np.mean(glue_df_summer_hypolimnetic_ave_rcp85['50%'])#2.0216371732488216

#%%anoxic_factor 30 yerars from each scenarios compare 



#anormaly 
# baseline [1976-2005]
glue_base_summer_hypolimnetic_ave_his=glue_df_summer_hypolimnetic_ave_his[1975 < glue_df_summer_hypolimnetic_ave_his.index]['50%']
summer_hypolimnetic_ave_ref=np.mean(glue_base_summer_hypolimnetic_ave_his)
#3.405313623842368


#near future [2030-2059]

glue_near_future_summer_hypolimnetic_ave_rcp26=glue_df_summer_hypolimnetic_ave_rcp26[(2029 < glue_df_summer_hypolimnetic_ave_rcp26.index) & (glue_df_summer_hypolimnetic_ave_rcp26.index < 2060)]['50%']
np.mean(glue_near_future_summer_hypolimnetic_ave_rcp26)
# 2.442836677609118
glue_near_future_summer_hypolimnetic_ave_rcp60=glue_df_summer_hypolimnetic_ave_rcp60[(2029 < glue_df_summer_hypolimnetic_ave_rcp60.index) & (glue_df_summer_hypolimnetic_ave_rcp60.index < 2060)]['50%']
np.mean(glue_near_future_summer_hypolimnetic_ave_rcp60)
# 2.284296650730716
glue_near_future_summer_hypolimnetic_ave_rcp85=glue_df_summer_hypolimnetic_ave_rcp85[(2029 < glue_df_summer_hypolimnetic_ave_rcp85.index) & (glue_df_summer_hypolimnetic_ave_rcp85.index < 2060)]['50%']
np.mean(glue_near_future_summer_hypolimnetic_ave_rcp85)
#  2.12983053408194

 
#Distant future [2070-2099]

glue_distant_future_summer_hypolimnetic_ave_rcp26=glue_df_summer_hypolimnetic_ave_rcp26[(2069 < glue_df_summer_hypolimnetic_ave_rcp26.index) & (glue_df_summer_hypolimnetic_ave_rcp26.index < 2100)]['50%']
np.mean(glue_distant_future_summer_hypolimnetic_ave_rcp26)
#2.4802458923822894
glue_distant_future_summer_hypolimnetic_ave_rcp60=glue_df_summer_hypolimnetic_ave_rcp60[(2069 < glue_df_summer_hypolimnetic_ave_rcp60.index) & (glue_df_summer_hypolimnetic_ave_rcp60.index< 2100)]['50%']
np.mean(glue_distant_future_summer_hypolimnetic_ave_rcp60)
#1.689415770106308
glue_distant_future_summer_hypolimnetic_ave_rcp85=glue_df_summer_hypolimnetic_ave_rcp85[(2069 < glue_df_summer_hypolimnetic_ave_rcp85.index) & (glue_df_summer_hypolimnetic_ave_rcp85.index < 2100)]['50%']
np.mean(glue_distant_future_summer_hypolimnetic_ave_rcp85)
#1.4371589966037255
   


###====over 30 years in his and each RCPs 

# baseline [1976-2005]
autocorr_MK_org_modif_sens_slope_test(glue_base_summer_hypolimnetic_ave_his)
(0.031019579516014202,
 'positively autocorrelated',
 'no trend',
 0.31774734769908775,
 0,
 0)


#near future [2030-2059]


autocorr_MK_org_modif_sens_slope_test(glue_near_future_summer_hypolimnetic_ave_rcp26)
(0.05682632419306522,
 'positively autocorrelated',
 'no trend',
 0.4754490495282657,
 0,
 0)
autocorr_MK_org_modif_sens_slope_test(glue_near_future_summer_hypolimnetic_ave_rcp60)
(0.05219898587244871,
 'positively autocorrelated',
 'decreasing',
 0.0021502307218466132,
 -0.016953890759819783,
 2.40141707693214)
autocorr_MK_org_modif_sens_slope_test(glue_near_future_summer_hypolimnetic_ave_rcp85)

(0.03832191743597291,
 'positively autocorrelated',
 'decreasing',
 0.0021502307218466132,
 -0.020959827900911027,
 2.4141430334696334)


#Distant future [2070-2099]

#rcp26
autocorr_MK_org_modif_sens_slope_test(glue_distant_future_summer_hypolimnetic_ave_rcp26)
(0.04482308242625801,
 'positively autocorrelated',
 'decreasing',
 0.026946782463489027,
 -0.023917748930890097,
 2.790762223592984)

#rcp60
autocorr_MK_org_modif_sens_slope_test(glue_distant_future_summer_hypolimnetic_ave_rcp60)
(0.0456967488175919,
 'positively autocorrelated',
 'no trend',
 0.7752944295177846,
 0,
 0)

#rcp85
autocorr_MK_org_modif_sens_slope_test(glue_distant_future_summer_hypolimnetic_ave_rcp85)
(0.11218537402374852,
 'positively autocorrelated',
 'no trend',
 0.18675613776082578,
 0,
 0)




#%% 80 years from 2020 for summer_hypolimnetic_ave


glue_80years_summer_hypolimnetic_ave_rcp26=glue_df_summer_hypolimnetic_ave_rcp26[2019 < glue_df_summer_hypolimnetic_ave_rcp26.index]

glue_80years_summer_hypolimnetic_ave_rcp60=glue_df_summer_hypolimnetic_ave_rcp60[2019 < glue_df_summer_hypolimnetic_ave_rcp60.index]

glue_80years_summer_hypolimnetic_ave_rcp85=glue_df_summer_hypolimnetic_ave_rcp85[2019 < glue_df_summer_hypolimnetic_ave_rcp85.index]


#============= mean of first 10 yaers over 80 years 

#rcp2.6
np.mean(glue_80years_summer_hypolimnetic_ave_rcp26[glue_80years_summer_hypolimnetic_ave_rcp26.index<2030]['50%'])
2.4180066251627204

#rcp6.0
np.mean(glue_80years_summer_hypolimnetic_ave_rcp60[glue_80years_summer_hypolimnetic_ave_rcp60.index<2030]['50%'])
2.5254198256447875

#rcp8.5
np.mean(glue_80years_summer_hypolimnetic_ave_rcp85[glue_80years_summer_hypolimnetic_ave_rcp85.index<2030]['50%'])
2.5022468009157883

#============== mean of last 10 yaers over 80 years 

#rcp2.6
np.mean(glue_80years_summer_hypolimnetic_ave_rcp26[glue_80years_summer_hypolimnetic_ave_rcp26.index>2079]['50%'])
2.3967191677896356

#rcp6.0
np.mean(glue_80years_summer_hypolimnetic_ave_rcp60[glue_80years_summer_hypolimnetic_ave_rcp60.index>2079]['50%'])
1.695719305767162

#rcp8.5
np.mean(glue_80years_summer_hypolimnetic_ave_rcp85[glue_80years_summer_hypolimnetic_ave_rcp85.index>2079]['50%'])
1.4096391938251762

#=========== trendline # Over the 80 years


autocorr_MK_org_modif_sens_slope_test(glue_80years_summer_hypolimnetic_ave_rcp26['50%'])
(0.05183371297244382,
 'positively autocorrelated',
 'no trend',
 0.7871194357602034,
 0,
 0)

autocorr_MK_org_modif_sens_slope_test(glue_80years_summer_hypolimnetic_ave_rcp60['50%'])
(0.0515504405602805,
 'positively autocorrelated',
 'decreasing',
 0.0,
 -0.013130707423988409,
 2.543645550696846)


autocorr_MK_org_modif_sens_slope_test(glue_80years_summer_hypolimnetic_ave_rcp85['50%'])
(0.07002175830344304,
 'positively autocorrelated',
 'decreasing',
 1.7563728249569976e-13,
 -0.01737490807443354,
 2.5716138716171484)



#%%plotting summer anoxic factor over 80 years 





os.chdir('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/')

import matplotlib.pyplot as plt

fig =plt.figure(figsize=(15, 10))
ax= plt.subplot(111)



ax=plt.fill_between(glue_80years_summer_hypolimnetic_ave_rcp26.index.astype(float), glue_80years_summer_hypolimnetic_ave_rcp26['5%'], glue_80years_summer_hypolimnetic_ave_rcp26['95%'], color='darkgreen', alpha=0.3 ,  label= 'RCP2.6 90% CI')
ax=plt.plot(glue_80years_summer_hypolimnetic_ave_rcp26.index.astype(float), glue_80years_summer_hypolimnetic_ave_rcp26['50%'], 'darkgreen', label='RCP2.6 median', alpha=0.9, linewidth=3  )


ax=plt.fill_between(glue_80years_summer_hypolimnetic_ave_rcp60.index.astype(float), glue_80years_summer_hypolimnetic_ave_rcp60['5%'], glue_80years_summer_hypolimnetic_ave_rcp60['95%'], color='yellow', alpha=0.2 ,  label= 'RCP6.0 90% CI')
ax=plt.plot(glue_80years_summer_hypolimnetic_ave_rcp60.index.astype(float), glue_80years_summer_hypolimnetic_ave_rcp60['50%'], 'yellow', label='RCP6.0 median', alpha=0.9, linewidth=3  )
trendline_rcp60=autocorr_MK_org_modif_sens_slope_test(glue_80years_summer_hypolimnetic_ave_rcp60['50%'])
ax=plt.text(2020, 7.5, f'y = {trendline_rcp60[-2]:.3f}x + {trendline_rcp60[-1]:.3f}, p = {trendline_rcp60[-3]:.3f}', color='gold', fontsize= 20 )

ax=plt.plot(glue_80years_summer_hypolimnetic_ave_rcp60.index.astype(float),
        trendline_rcp60[-2] * np.arange(80) + trendline_rcp60[-1],
        linestyle='--', color='yellow', alpha=0.9, linewidth=3)


ax=plt.fill_between(glue_80years_summer_hypolimnetic_ave_rcp85.index.astype(float), glue_80years_summer_hypolimnetic_ave_rcp85['5%'], glue_80years_summer_hypolimnetic_ave_rcp85['95%'], color='r', alpha=0.2 ,  label= 'RCP8.5 90% CI')
ax=plt.plot(glue_80years_summer_hypolimnetic_ave_rcp85.index.astype(float), glue_80years_summer_hypolimnetic_ave_rcp85['50%'], 'r', label='RCP8.5 median', alpha=0.9, linewidth=3  )
trendline_rcp85=autocorr_MK_org_modif_sens_slope_test(glue_80years_summer_hypolimnetic_ave_rcp85['50%'])
ax=plt.text(2020, 7, f'y = {trendline_rcp85[-2]:.3f}x + {trendline_rcp85[-1]:.3f},  p = {trendline_rcp85[-3]:.3f}', color='r', fontsize= 20 )

ax=plt.plot(glue_80years_summer_hypolimnetic_ave_rcp85.index.astype(float),
        trendline_rcp85[-2] * np.arange(80) + trendline_rcp85[-1],
        linestyle='--', color='r', alpha=0.9, linewidth=3)


ax=plt.ylabel('Hypolimnetic DO in summer [mg L$^{-1}$]' , fontsize=26)
ax=plt.xlabel('Year' , fontsize=26)
ax=plt.yticks(fontsize= 22)
ax=plt.xticks(rotation=45 , fontsize=22)
ax=plt.legend(bbox_to_anchor=(0.7, -0.2), fontsize=22)#)   
fig.savefig("GLUE_Timeseries_80years_summer_hypolimnetic_ave.png",  dpi=300, bbox_inches='tight')





#%%If there is a trend in entire scenario

# in whole his
autocorr_MK_org_modif_sens_slope_test(glue_df_summer_hypolimnetic_ave_his['50%'])
(0.06159841953286706,
 'positively autocorrelated',
 'no trend',
 0.9414027070186699,
 0,
 0)
#in intire rcp2.6
autocorr_MK_org_modif_sens_slope_test(glue_df_summer_hypolimnetic_ave_rcp26['50%'])
(0.04644270972932335,
 'positively autocorrelated',
 'no trend',
 0.14546212346892773,
 0,
 0)
#in entire rcp6.0
autocorr_MK_org_modif_sens_slope_test(glue_df_summer_hypolimnetic_ave_rcp60['50%'])
(0.051817592017632405,
 'positively autocorrelated',
 'decreasing',
 0.0,
 -0.013175385343608388,
 2.7227019069401925)

#in entire rcp8.5
autocorr_MK_org_modif_sens_slope_test(glue_df_summer_hypolimnetic_ave_rcp85['50%'])
(0.07264701310648392,
 'positively autocorrelated',
 'decreasing',
 0.0,
 -0.017930312930872327,
 2.859156895471733)

#slope in entire RCP8.5> RCP6.0>RCP2.6 # his no trend 



 
#%%anoxic_factor_anormaly 
os.chdir('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/')

import matplotlib.pyplot as plt

fig =plt.figure(figsize=(15, 10))
ax= plt.subplot(111)


ax=plt.fill_between(glue_df_summer_hypolimnetic_ave_his[(1960 < glue_df_summer_hypolimnetic_ave_his.index)].index.astype(float),
                      glue_df_summer_hypolimnetic_ave_his[(1960 < glue_df_summer_hypolimnetic_ave_his.index)]['5%'] - summer_hypolimnetic_ave_ref,
                      glue_df_summer_hypolimnetic_ave_his[(1960 < glue_df_summer_hypolimnetic_ave_his.index) ]['95%'] - summer_hypolimnetic_ave_ref,
                      color='grey', alpha=0.2, label='His 90% CI')


ax=plt.plot(glue_df_summer_hypolimnetic_ave_his[(1960 < glue_df_summer_hypolimnetic_ave_his.index) ].index.astype(float),
            glue_df_summer_hypolimnetic_ave_his[(1960 < glue_df_summer_hypolimnetic_ave_his.index)]['50%'] - summer_hypolimnetic_ave_ref,
            'k', label='His median', alpha=0.9, linewidth=3   )

ax=plt.fill_between(glue_df_summer_hypolimnetic_ave_rcp26.index.astype(float), glue_df_summer_hypolimnetic_ave_rcp26['5%']-summer_hypolimnetic_ave_ref, glue_df_summer_hypolimnetic_ave_rcp26['95%']-summer_hypolimnetic_ave_ref, color='darkgreen', alpha=0.3 ,  label= 'RCP6.0 90% CI')
ax=plt.plot(glue_df_summer_hypolimnetic_ave_rcp26.index.astype(float), glue_df_summer_hypolimnetic_ave_rcp26['50%']-summer_hypolimnetic_ave_ref, 'darkgreen', label='RCP6.0 median', alpha=0.9, linewidth=3  )
                      
                     
ax=plt.fill_between(glue_df_summer_hypolimnetic_ave_rcp60.index.astype(float), glue_df_summer_hypolimnetic_ave_rcp60['5%']-summer_hypolimnetic_ave_ref, glue_df_summer_hypolimnetic_ave_rcp60['95%']-summer_hypolimnetic_ave_ref, color='yellow', alpha=0.2 ,  label= 'RCP6.0 90% CI')
ax=plt.plot(glue_df_summer_hypolimnetic_ave_rcp60.index.astype(float), glue_df_summer_hypolimnetic_ave_rcp60['50%']-summer_hypolimnetic_ave_ref, 'yellow', label='RCP6.0 median', alpha=0.9, linewidth=3  )

ax=plt.fill_between(glue_df_summer_hypolimnetic_ave_rcp85.index.astype(float), glue_df_summer_hypolimnetic_ave_rcp85['5%']-summer_hypolimnetic_ave_ref, glue_df_summer_hypolimnetic_ave_rcp85['95%']-summer_hypolimnetic_ave_ref, color='r', alpha=0.2 ,  label= 'RCP8.5 90% CI')
ax=plt.plot(glue_df_summer_hypolimnetic_ave_rcp85.index.astype(float), glue_df_summer_hypolimnetic_ave_rcp85['50%']-summer_hypolimnetic_ave_ref, 'r', label='RCP8.5 median', alpha=0.9, linewidth=3  )

ax=plt.ylabel('Anormaly of hypolimnetic DO in summer [mg L$^{-1}$]' , fontsize=26)
ax=plt.xlabel('Year' , fontsize=26)
ax=plt.yticks(fontsize= 22)
ax=plt.xticks(rotation=45 , fontsize=22)
ax=plt.legend(bbox_to_anchor=(0.7, -0.2), fontsize=22)  
fig.savefig("GLUE_Timeseries_summer_hypolimnetic_ave_anormaly.png",  dpi=300, bbox_inches='tight')

"""


#%%Anlyses on the RCP2.6 with constant inital condition as 12.298 mg/L

#annual/monthly
#gfdl


all_annual_do_rcp26_test= pd.DataFrame([])
all_monthly_do_rcp26_test= pd.DataFrame([])
#all_summer_do_rcp26_test= pd.DataFrame([])
all_weights= np.array([])

directory = "C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp26_initialcond_attribution"


# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("DO_prof_gfdl_rcp26"):
        
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
        Vr= hypo_morpho_vriables_gotm_grid[0]
        # Apply the  function
        result_annual =annual_hypolimnetic_ave (C, Vr, time_series )
        result_monthly =monthly_hypolimnetic_ave (C, Vr, time_series )
        result_summer =summer_hypolimnetic_ave (C, Vr, time_series )
        
        
        all_annual_do_rcp26_test = pd.concat([all_annual_do_rcp26_test , result_annual], axis=1)


        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result annual to a new CSV file
        result_annual_filename = f'annual_do_gfdl_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_annual_filename))#, index=False)
       

        result_annual.to_csv(os.path.join(directory, result_annual_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_AF'])
        
        
        
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
        Vr= hypo_morpho_vriables_gotm_grid[0]
        # Apply the  function
        result_monthly =monthly_hypolimnetic_ave (C, Vr, time_series )
        #result_summer =summer_hypolimnetic_ave (C, Vr, time_series )
        
        
        all_monthly_do_rcp26_test= pd.concat([all_monthly_do_rcp26_test , result_monthly], axis=1)
        #all_summer_do_rcp26_test= pd.concat([all_summer_do_rcp26_test , result_summer], axis=1)


        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }

        
        # Save the result monthly to a new CSV file
        result_monthly_filename = f'monthly_do_gfdl_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_monthly_filename))#, index=False)
       

        result_monthly.to_csv(os.path.join(directory, result_monthly_filename) , mode='a' , index_label='year', na_rep='NaN', header=['monthly_AF'])
    
"""        
        # Save the result summer to a new CSV file
        result_summer_filename = f'summer_do_gfdl_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_summer_filename))#, index=False)
       

        result_summer.to_csv(os.path.join(directory, result_summer_filename) , mode='a' , index_label='year', na_rep='NaN', header=['summer_AF'])
"""    
        
#hadgem

directory = "C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp26_initialcond_attribution"


# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("DO_prof_hadgem_rcp26"):
        
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
        Vr= hypo_morpho_vriables_gotm_grid[0]
        # Apply the  function
        result_annual =annual_hypolimnetic_ave (C, Vr, time_series )
        result_monthly =monthly_hypolimnetic_ave (C, Vr, time_series )
        result_summer =summer_hypolimnetic_ave (C, Vr, time_series )
        
        
        all_annual_do_rcp26_test = pd.concat([all_annual_do_rcp26_test , result_annual], axis=1)


        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result annual to a new CSV file
        result_annual_filename = f'annual_do_hadgem_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_annual_filename))#, index=False)
       

        result_annual.to_csv(os.path.join(directory, result_annual_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_AF'])
        
        
        
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
        Vr= hypo_morpho_vriables_gotm_grid[0]
        # Apply the  function
        result_monthly =monthly_hypolimnetic_ave (C, Vr, time_series )
        #result_summer =summer_hypolimnetic_ave (C, Vr, time_series )
        
        
        all_monthly_do_rcp26_test= pd.concat([all_monthly_do_rcp26_test , result_monthly], axis=1)
        #all_summer_do_rcp26_test= pd.concat([all_summer_do_rcp26_test , result_summer], axis=1)


        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }

        
        # Save the result monthly to a new CSV file
        result_monthly_filename = f'monthly_do_hadgem_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_monthly_filename))#, index=False)
       

        result_monthly.to_csv(os.path.join(directory, result_monthly_filename) , mode='a' , index_label='year', na_rep='NaN', header=['monthly_AF'])
    
"""        
        # Save the result summer to a new CSV file
        result_summer_filename = f'summer_do_hadgem_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_summer_filename))#, index=False)
       

        result_summer.to_csv(os.path.join(directory, result_summer_filename) , mode='a' , index_label='year', na_rep='NaN', header=['summer_AF'])
"""    
        
        
#ipsl

directory = "C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp26_initialcond_attribution"


# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("DO_prof_ipsl_rcp26"):
        
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
        Vr= hypo_morpho_vriables_gotm_grid[0]
        # Apply the  function
        result_annual =annual_hypolimnetic_ave (C, Vr, time_series )
        result_monthly =monthly_hypolimnetic_ave (C, Vr, time_series )
        result_summer =summer_hypolimnetic_ave (C, Vr, time_series )
        
        
        all_annual_do_rcp26_test = pd.concat([all_annual_do_rcp26_test , result_annual], axis=1)


        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result annual to a new CSV file
        result_annual_filename = f'annual_do_ipsl_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_annual_filename))#, index=False)
       

        result_annual.to_csv(os.path.join(directory, result_annual_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_AF'])
        
        
        
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
        Vr= hypo_morpho_vriables_gotm_grid[0]
        # Apply the  function
        result_monthly =monthly_hypolimnetic_ave (C, Vr, time_series )
        #result_summer =summer_hypolimnetic_ave (C, Vr, time_series )
        
        
        all_monthly_do_rcp26_test= pd.concat([all_monthly_do_rcp26_test , result_monthly], axis=1)
        #all_summer_do_rcp26_test= pd.concat([all_summer_do_rcp26_test , result_summer], axis=1)


        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }

        
        # Save the result monthly to a new CSV file
        result_monthly_filename = f'monthly_do_ipsl_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_monthly_filename))#, index=False)
       

        result_monthly.to_csv(os.path.join(directory, result_monthly_filename) , mode='a' , index_label='year', na_rep='NaN', header=['monthly_AF'])
    
"""        
        # Save the result summer to a new CSV file
        result_summer_filename = f'summer_do_ipsl_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_summer_filename))#, index=False)
       

        result_summer.to_csv(os.path.join(directory, result_summer_filename) , mode='a' , index_label='year', na_rep='NaN', header=['summer_AF'])
"""    
            
        
#miroc

directory = "C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp26_initialcond_attribution"


# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("DO_prof_miroc_rcp26"):
        
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
        Vr= hypo_morpho_vriables_gotm_grid[0]
        # Apply the  function
        result_annual =annual_hypolimnetic_ave (C, Vr, time_series )
        result_monthly =monthly_hypolimnetic_ave (C, Vr, time_series )
        result_summer =summer_hypolimnetic_ave (C, Vr, time_series )
        
        
        all_annual_do_rcp26_test = pd.concat([all_annual_do_rcp26_test , result_annual], axis=1)


        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result annual to a new CSV file
        result_annual_filename = f'annual_do_miroc_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_annual_filename))#, index=False)
       

        result_annual.to_csv(os.path.join(directory, result_annual_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_AF'])
        
        
        
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
        Vr= hypo_morpho_vriables_gotm_grid[0]
        # Apply the  function
        result_monthly =monthly_hypolimnetic_ave (C, Vr, time_series )
        #result_summer =summer_hypolimnetic_ave (C, Vr, time_series )
        
        
        all_monthly_do_rcp26_test= pd.concat([all_monthly_do_rcp26_test , result_monthly], axis=1)
        #all_summer_do_rcp26_test= pd.concat([all_summer_do_rcp26_test , result_summer], axis=1)


        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }

        
        # Save the result monthly to a new CSV file
        result_monthly_filename = f'monthly_do_miroc_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_monthly_filename))#, index=False)
       

        result_monthly.to_csv(os.path.join(directory, result_monthly_filename) , mode='a' , index_label='year', na_rep='NaN', header=['monthly_AF'])
    
"""        
        # Save the result summer to a new CSV file
        result_summer_filename = f'summer_do_miroc_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_summer_filename))#, index=False)
       

        result_summer.to_csv(os.path.join(directory, result_summer_filename) , mode='a' , index_label='year', na_rep='NaN', header=['summer_AF'])
"""    
        


    
    
    
    
    
    
    
        
#%% GLUE of diff of test rcp26 scenarios for annual/monthly/summer do


all_annual_do_rcp26_test
all_monthly_do_rcp26_test
#all_summer_do_rcp26_test

all_annual_do_rcp26
all_monthly_do_rcp26
#all_summer_do_rcp26


diff_base_test_annual_do_rcp26= pd.DataFrame(np.array(all_annual_do_rcp26)-np.array(all_annual_do_rcp26_test))

diff_base_test_monthly_do_rcp26= pd.DataFrame(np.array(all_monthly_do_rcp26)-np.array(all_monthly_do_rcp26_test))

#diff_base_test_summer_do_rcp26= pd.DataFrame(np.array(all_summer_do_rcp26)-np.array(all_summer_do_rcp26_test))



all_weights


# annual DO hypolimnion 
timeseries_year_rcp26= all_annual_do_rcp26_test.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in diff_base_test_annual_do_rcp26.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights))

# Build glue df
glue_diff_base_test_annual_do_rcp26 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_diff_base_test_annual_do_rcp26=glue_diff_base_test_annual_do_rcp26.set_index(timeseries_year_rcp26)    
glue_diff_base_test_annual_do_rcp26=glue_diff_base_test_annual_do_rcp26.sort_index()
glue_diff_base_test_annual_do_rcp26_80years=glue_diff_base_test_annual_do_rcp26[glue_diff_base_test_annual_do_rcp26.index>2019]


# monthly DO hypolimnion 
timeseries_year_rcp26= all_monthly_do_rcp26_test.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in diff_base_test_monthly_do_rcp26.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights))

# Build glue df
glue_diff_base_test_monthly_do_rcp26 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_diff_base_test_monthly_do_rcp26=glue_diff_base_test_monthly_do_rcp26.set_index(timeseries_year_rcp26)    
glue_diff_base_test_monthly_do_rcp26=glue_diff_base_test_monthly_do_rcp26.sort_index()
glue_diff_base_test_monthly_do_rcp26_80years=glue_diff_base_test_monthly_do_rcp26[glue_diff_base_test_monthly_do_rcp26.index>2019]
"""
# summer DO hypolimnion 
timeseries_year_rcp26= all_summer_do_rcp26_test.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in diff_base_test_summer_do_rcp26.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights))

# Build glue df
glue_diff_base_test_summer_do_rcp26 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_diff_base_test_summer_do_rcp26=glue_diff_base_test_summer_do_rcp26.set_index(timeseries_year_rcp26)    
glue_diff_base_test_summer_do_rcp26=glue_diff_base_test_summer_do_rcp26.sort_index()
glue_diff_base_test_summer_do_rcp26_80years=glue_diff_base_test_summer_do_rcp26[glue_diff_base_test_summer_do_rcp26.index>2019]
"""




#%%GLUE for rcp26 test 
all_weights


# annual DO hypolimnion 
timeseries_year_rcp26= all_annual_do_rcp26_test.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_annual_do_rcp26_test.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights))

# Build glue df
glue_annual_do_rcp26_test = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_annual_do_rcp26_test=glue_annual_do_rcp26_test.set_index(timeseries_year_rcp26)    
glue_annual_do_rcp26_test=glue_annual_do_rcp26_test.sort_index()
glue_annual_do_rcp26_test_80years=glue_annual_do_rcp26_test[glue_annual_do_rcp26_test.index>2019]


# monthly DO hypolimnion 
timeseries_year_rcp26= all_monthly_do_rcp26_test.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_monthly_do_rcp26_test.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights))

# Build glue df
glue_monthly_do_rcp26_test = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_monthly_do_rcp26_test=glue_monthly_do_rcp26_test.set_index(timeseries_year_rcp26)    
glue_monthly_do_rcp26_test=glue_monthly_do_rcp26_test.sort_index()
glue_monthly_do_rcp26_test_80years=glue_monthly_do_rcp26_test[glue_monthly_do_rcp26_test.index>2019]

"""
# summer DO hypolimnion 
timeseries_year_rcp26= all_summer_do_rcp26_test.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_summer_do_rcp26_test.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights))

# Build glue df
glue_summer_do_rcp26_test = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_summer_do_rcp26_test=glue_summer_do_rcp26_test.set_index(timeseries_year_rcp26)    
glue_summer_do_rcp26_test=glue_summer_do_rcp26_test.sort_index()
glue_summer_do_rcp26_test_80years=glue_summer_do_rcp26_test[glue_summer_do_rcp26_test.index>2019]
"""





#%% Diff of test and baseline->only for onset
### test->only for stratification duration 

#%% analysing the difference of baseline scenarios and test with fixed inital condition 

#%%annual do over 80 years

glue_diff_base_test_annual_do_rcp26_80years=glue_diff_base_test_annual_do_rcp26[glue_diff_base_test_annual_do_rcp26.index>2019]
autocorr_MK_org_modif_sens_slope_test(glue_diff_base_test_annual_do_rcp26_80years['50%'])

(2.0, 'non autocorrelated', 'no trend', 0.21949168333305025, 0, 0)



#%%monthly do

glue_diff_base_test_monthly_do_rcp26_80years=glue_diff_base_test_monthly_do_rcp26[glue_diff_base_test_monthly_do_rcp26.index>2019]
autocorr_MK_org_modif_sens_slope_test(glue_diff_base_test_monthly_do_rcp26_80years['50%'])

(1.9541331705984653,
 'positively autocorrelated',
 'increasing',
 0.023556221727703885,
 0.0012630089848214674,
 -0.012353727295478636)






#%%summer do

"""
autocorr_MK_org_modif_sens_slope_test(glue_diff_base_test_summer_do_rcp26[glue_diff_base_test_summer_do_rcp26.index>2019]['50%'])
(1.9999999999999996,
 'positively autocorrelated',
 'no trend',
 0.635340267384636,
 0,
 0)
"""




#%% trendline in test scenario of rcp26 over 80 years 


#%% annual do
autocorr_MK_org_modif_sens_slope_test(glue_annual_do_rcp26_test_80years['50%'])
(0.014500132581905217,
 'positively autocorrelated',
 'no trend',
 0.693069521433799,
 0,
 0)

os.chdir('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/')

import matplotlib.pyplot as plt

fig =plt.figure(figsize=(15, 10))
ax= plt.subplot(111)


ax=plt.fill_between(glue_annual_do_rcp26_test_80years.index.astype(float), glue_annual_do_rcp26_test_80years['5%'], glue_annual_do_rcp26_test_80years['95%'], color='green', alpha=0.2 ,  label= '90% CI')
ax=plt.plot(glue_annual_do_rcp26_test_80years.index.astype(float), glue_annual_do_rcp26_test_80years['50%'].astype(float), 'green', label='Median', alpha=0.9, linewidth=3  )




#trendline_rcp26=autocorr_MK_org_modif_sens_slope_test(glue_annual_do_rcp26_test_80years['50%'])
#ax=plt.text(2020, 2, f'y = {trendline_rcp26[-2]:.3f}x + {trendline_rcp26[-1]:.3f}, p = {trendline_rcp26[-3]:.3f}', color='green', fontsize= 20 )

#ax=plt.plot(glue_annual_do_rcp26_test_80years.index.astype(float),
#        trendline_rcp26[-2] * np.arange(80) + trendline_rcp26[-1],
#        linestyle='--', color='green', alpha=0.9, linewidth=3)




ax=plt.ylabel('DO in deoxygenation period of RCP2.6\n with fixed inital condition [mg L$^{-1}$]' , fontsize=26)
ax=plt.xlabel('Year' , fontsize=26)
ax=plt.yticks(fontsize= 22)
ax=plt.xticks(rotation=45 , fontsize=22)
ax=plt.legend(bbox_to_anchor=(0.7, -0.2), fontsize=22 , ncol=2)#)   
fig.savefig("test_initalcondition_fixed_annual_do_80years_rcp26.png",  dpi=300, bbox_inches='tight')



#%% monthly do:


autocorr_MK_org_modif_sens_slope_test(glue_monthly_do_rcp26_test_80years['50%'])
(0.00890653300478083,
 'positively autocorrelated',
 'decreasing',
 0.022066631696961325,
 -0.004649058434895062,
 6.744952492601289)





#%% No trend for during deoxygenation for neither test nor the difference 

#%%for paper both plot of diff and test of monthly rcp26 in one plot 

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MaxNLocator

# Create figure and axes for subplots
fig, axs = plt.subplots(1, 2, figsize=(25, 10))

# Plot for the first subplot
ax = axs[1]
ax.fill_between(glue_diff_base_test_monthly_do_rcp26_80years.index,
                glue_diff_base_test_monthly_do_rcp26_80years['5%'],
                glue_diff_base_test_monthly_do_rcp26_80years['95%'],
                color='green', alpha=0.2, label='90% CI')
ax.plot(glue_diff_base_test_monthly_do_rcp26_80years.index,
        glue_diff_base_test_monthly_do_rcp26_80years['50%'],
        'green', label='Median', alpha=0.9, linewidth=3)

# Add trendline
trendline_rcp26_1 = autocorr_MK_org_modif_sens_slope_test(glue_diff_base_test_monthly_do_rcp26_80years['50%'])
ax.text(0.95, 0.95, '(b)', transform=ax.transAxes, fontsize=22,
        verticalalignment='top', horizontalalignment='right')
ax.text(2020, 0.5, f'y = {trendline_rcp26_1[-2]:.3f}x + {trendline_rcp26_1[-1]:.3f}, p = {trendline_rcp26_1[-3]:.3f}',
        color='green', fontsize=20)
ax.plot(glue_diff_base_test_monthly_do_rcp26_80years.index.astype(float),
        trendline_rcp26_1[-2] * np.arange(80) + trendline_rcp26_1[-1],
        linestyle='--', color='green', alpha=0.9, linewidth=3)

# Set labels for the first subplot
ax.set_ylabel('Deep DO in Apr-Oct of RCP2.6 \n difference between fixed initial condition \n and original scenario  [mg L$^{-1}$]', fontsize=26)
ax.set_xlabel('Year', fontsize=26)
ax.tick_params(axis='y', labelsize=22)
ax.set_xticks(glue_diff_base_test_monthly_do_rcp26_80years.index)
ax.set_xticklabels(glue_diff_base_test_monthly_do_rcp26_80years.index, rotation=45, fontsize=22)
ax.xaxis.set_major_locator(MaxNLocator(prune='both'))

# Plot for the second subplot
ax = axs[0]
ax.fill_between(glue_monthly_do_rcp26_test_80years.index,
                glue_monthly_do_rcp26_test_80years['5%'],
                glue_monthly_do_rcp26_test_80years['95%'],
                color='green', alpha=0.2)#, label='90% CI')
ax.plot(glue_monthly_do_rcp26_test_80years.index,
        glue_monthly_do_rcp26_test_80years['50%'].astype(float),
        'green', alpha=0.9, linewidth=3)# label='Median',

# Add trendline
trendline_rcp26_0 = autocorr_MK_org_modif_sens_slope_test(glue_monthly_do_rcp26_test_80years['50%'])
ax.text(0.95, 0.95, '(a)', transform=ax.transAxes, fontsize=22,
        verticalalignment='top', horizontalalignment='right')
ax.text(2020, 10, f'y = {trendline_rcp26_0[-2]:.3f}x + {trendline_rcp26_0[-1]:.3f}, p = {trendline_rcp26_0[-3]:.3f}',
        color='green', fontsize=20)
ax.plot(glue_monthly_do_rcp26_test_80years.index,
        trendline_rcp26_0[-2] * np.arange(80) + trendline_rcp26_0[-1],
        linestyle='--', color='green', alpha=0.9, linewidth=3)

# Set labels for the second subplot
ax.set_ylabel('Deep DO in Apr-Oct of RCP2.6 with\n fixed initial condition [mg L$^{-1}$]', fontsize=26)
ax.set_xlabel('Year', fontsize=26)
ax.tick_params(axis='y', labelsize=22)
ax.set_xticks(glue_monthly_do_rcp26_test_80years.index)
ax.set_xticklabels(glue_monthly_do_rcp26_test_80years.index, rotation=45, fontsize=22)
ax.xaxis.set_major_locator(MaxNLocator(prune='both'))

# Add a single legend for both subplots in the center bottom
fig.legend(loc='lower center', fontsize=22, ncol=1)

plt.tight_layout()

plt.savefig("atttest_difference_test_initalcondition_fixed_monthly_do_80years_rcp26.png",  dpi=300, bbox_inches='tight')




#%%
glue_diff_base_test_monthly_do_rcp26_80years
glue_monthly_do_rcp26_test_80years


os.chdir('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/')

import matplotlib.pyplot as plt

fig =plt.figure(figsize=(15, 10))
ax= plt.subplot(111)


ax=plt.fill_between(glue_monthly_do_rcp26_test_80years.index.astype(float), glue_monthly_do_rcp26_test_80years['5%'], glue_monthly_do_rcp26_test_80years['95%'], color='green', alpha=0.2 ,  label= '90% CI')
ax=plt.plot(glue_monthly_do_rcp26_test_80years.index.astype(float), glue_monthly_do_rcp26_test_80years['50%'].astype(float), 'green', label='Median', alpha=0.9, linewidth=3  )




trendline_rcp26=autocorr_MK_org_modif_sens_slope_test(glue_monthly_do_rcp26_test_80years['50%'])
ax=plt.text(2020, 2, f'y = {trendline_rcp26[-2]:.3f}x + {trendline_rcp26[-1]:.3f}, p = {trendline_rcp26[-3]:.3f}', color='green', fontsize= 20 )

ax=plt.plot(glue_monthly_do_rcp26_test_80years.index.astype(float),
        trendline_rcp26[-2] * np.arange(80) + trendline_rcp26[-1],
        linestyle='--', color='green', alpha=0.9, linewidth=3)




ax=plt.ylabel('Deep DO in Apr-Oct of RCP2.6 with fixed inital condition [mg L$^{-1}$]' , fontsize=26)
ax=plt.xlabel('Year' , fontsize=26)
ax=plt.yticks(fontsize= 22)
ax=plt.xticks(rotation=45 , fontsize=22)
ax=plt.legend(bbox_to_anchor=(0.7, -0.2), fontsize=22)#)   
fig.savefig("test_initalcondition_fixed_monthly_do_80years_rcp26.png",  dpi=300, bbox_inches='tight')

#%% summer do
"""
autocorr_MK_org_modif_sens_slope_test(glue_summer_do_rcp26_test_80years['50%'])

(0.0443638104024983,
 'positively autocorrelated',
 'no trend',
 0.08159993472744387,
 0,



#%%summer do

os.chdir('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/')


import matplotlib.pyplot as plt

fig =plt.figure(figsize=(15, 10))
ax= plt.subplot(111)


ax=plt.fill_between(glue_summer_do_rcp26_test_80years.index.astype(float), glue_summer_do_rcp26_test_80years['5%'], glue_summer_do_rcp26_test_80years['95%'], color='green', alpha=0.2 ,  label= '90% CI')
ax=plt.plot(glue_summer_do_rcp26_test_80years.index.astype(float), glue_summer_do_rcp26_test_80years['50%'].astype(float), 'green', label='Median', alpha=0.9, linewidth=3  )




trendline_rcp26=autocorr_MK_org_modif_sens_slope_test(glue_summer_do_rcp26_test_80years['50%'])
ax=plt.text(2020, 2, f'y = {trendline_rcp26[-2]:.3f}x + {trendline_rcp26[-1]:.3f}, p = {trendline_rcp26[-3]:.3f}', color='green', fontsize= 20 )

ax=plt.plot(glue_summer_do_rcp26_test_80years.index.astype(float),
        trendline_rcp26[-2] * np.arange(80) + trendline_rcp26[-1],
        linestyle='--', color='green', alpha=0.9, linewidth=3)




ax=plt.ylabel('Hypolimnetic DO in summer of RCP2.6 with fixed inital condition [mg L$^{-1}$]' , fontsize=26)
ax=plt.xlabel('Year' , fontsize=26)
ax=plt.yticks(fontsize= 22)
ax=plt.xticks(rotation=45 , fontsize=22)
ax=plt.legend(bbox_to_anchor=(0.7, -0.2), fontsize=22)#)   
fig.savefig("test_initalcondition_fixed_summer_do_80years_rcp26.png",  dpi=300, bbox_inches='tight')

"""




#%%%%%%%%======================
#============OLD
#############
#%% Annual anoxic factor_gfdl_his
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/his'

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
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = annual_hypolimnetic_ave(C, Vr, time_series A0=23.67*10**6 , threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_hypolimnetic_ave_gfdl_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_hypolimnetic_ave'])
        
                

#%% monthly anoxic factor_gfdl_his
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/his'

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
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = monthly_hypolimnetic_ave(C, Vr, time_series A0=23.67*10**6 , threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_hypolimnetic_ave_gfdl_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['monthly_hypolimnetic_ave'])
        
                
#%% summer anoxic factor_gfdl_his
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/his'

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
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = summer_hypolimnetic_ave(C, Vr, time_series A0=23.67*10**6 , threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'summer_hypolimnetic_ave_gfdl_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['summer_hypolimnetic_ave'])
        
                




#%%monthly_hypolimnetic_ave_gfdl_his

# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/his'

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
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = monthly_hypolimnetic_ave(C, Vr, time_series A0=23.67*10**6 , threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_hypolimnetic_ave_gfdl_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                
#%% Annual anoxic factor_gfdl_rcp26
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp26'

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
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = annual_hypolimnetic_ave(C, Vr, time_series A0=23.67*10**6 , threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_hypolimnetic_ave_gfdl_rcp26_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_hypolimnetic_ave'])
        
#%% monthly anoxic factor_gfdl_rcp26
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp26'

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
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = monthly_hypolimnetic_ave(C, Vr, time_series A0=23.67*10**6 , threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_hypolimnetic_ave_gfdl_rcp26_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['monthly_hypolimnetic_ave'])
        
                
#%% summer anoxic factor_gfdl_rcp26
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp26'

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
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = summer_hypolimnetic_ave(C, Vr, time_series A0=23.67*10**6 , threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'summer_hypolimnetic_ave_gfdl_rcp26_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['summer_hypolimnetic_ave'])
        
                


                


#%%monthly_hypolimnetic_ave_gfdl_rcp26

# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp26'

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
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = monthly_hypolimnetic_ave(C, Vr, time_series A0=23.67*10**6 , threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_hypolimnetic_ave_gfdl_rcp26_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                

#%% Annual anoxic factor_gfdl_rcp60
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp60'

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
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = annual_hypolimnetic_ave(C, Vr, time_series A0=23.67*10**6 , threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_hypolimnetic_ave_gfdl_rcp60_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_hypolimnetic_ave'])
        
                
#%% monthly anoxic factor_gfdl_rcp60
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp60'

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
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = monthly_hypolimnetic_ave(C, Vr, time_series A0=23.67*10**6 , threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_hypolimnetic_ave_gfdl_rcp60_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['monthly_hypolimnetic_ave'])
        
                
#%% summer anoxic factor_gfdl_rcp60
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp60'

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
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = summer_hypolimnetic_ave(C, Vr, time_series A0=23.67*10**6 , threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'summer_hypolimnetic_ave_gfdl_rcp60_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['summer_hypolimnetic_ave'])
        
                










#%%monthly_hypolimnetic_ave_gfdl_rcp60

# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp60'

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
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = monthly_hypolimnetic_ave(C, Vr, time_series A0=23.67*10**6 , threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_hypolimnetic_ave_gfdl_rcp60_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                



#%% Annual anoxic factor_gfdl_rcp85
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp85'

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
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = annual_hypolimnetic_ave(C, Vr, time_series A0=23.67*10**6 , threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_hypolimnetic_ave_gfdl_rcp85_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_hypolimnetic_ave'])
        
                
#%% monthly anoxic factor_gfdl_rcp85
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp85'

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
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = monthly_hypolimnetic_ave(C, Vr, time_series A0=23.67*10**6 , threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_hypolimnetic_ave_gfdl_rcp85_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['monthly_hypolimnetic_ave'])
        
                
#%% summer anoxic factor_gfdl_rcp85
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp85'

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
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = summer_hypolimnetic_ave(C, Vr, time_series A0=23.67*10**6 , threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'summer_hypolimnetic_ave_gfdl_rcp85_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['summer_hypolimnetic_ave'])
        
                




#%%monthly_hypolimnetic_ave_gfdl_rcp85

# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp85'

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
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = monthly_hypolimnetic_ave(C, Vr, time_series A0=23.67*10**6 , threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_hypolimnetic_ave_gfdl_rcp85_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                
#%%hadgem

#%% Annual anoxic factor_hadgem_his
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/his'

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
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = annual_hypolimnetic_ave(C, Vr, time_series A0=23.67*10**6 , threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_hypolimnetic_ave_hadgem_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_hypolimnetic_ave'])
        
                

#%% monthly anoxic factor_hadgem_his
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/his'

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
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = monthly_hypolimnetic_ave(C, Vr, time_series A0=23.67*10**6 , threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_hypolimnetic_ave_hadgem_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['monthly_hypolimnetic_ave'])
        
                
#%% summer anoxic factor_hadgem_his
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/his'

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
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = summer_hypolimnetic_ave(C, Vr, time_series A0=23.67*10**6 , threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'summer_hypolimnetic_ave_hadgem_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['summer_hypolimnetic_ave'])
        
                




#%%monthly_hypolimnetic_ave_hadgem_his

# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/his'

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
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = monthly_hypolimnetic_ave(C, Vr, time_series A0=23.67*10**6 , threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_hypolimnetic_ave_hadgem_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                
#%% Annual anoxic factor_hadgem_rcp26
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp26'

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
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = annual_hypolimnetic_ave(C, Vr, time_series A0=23.67*10**6 , threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_hypolimnetic_ave_hadgem_rcp26_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_hypolimnetic_ave'])
        
#%% monthly anoxic factor_hadgem_rcp26
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp26'

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
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = monthly_hypolimnetic_ave(C, Vr, time_series A0=23.67*10**6 , threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_hypolimnetic_ave_hadgem_rcp26_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['monthly_hypolimnetic_ave'])
        
                
#%% summer anoxic factor_hadgem_rcp26
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp26'

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
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = summer_hypolimnetic_ave(C, Vr, time_series A0=23.67*10**6 , threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'summer_hypolimnetic_ave_hadgem_rcp26_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['summer_hypolimnetic_ave'])
        
                


                


#%%monthly_hypolimnetic_ave_hadgem_rcp26

# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp26'

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
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = monthly_hypolimnetic_ave(C, Vr, time_series A0=23.67*10**6 , threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_hypolimnetic_ave_hadgem_rcp26_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                

#%% Annual anoxic factor_hadgem_rcp60
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp60'

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
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = annual_hypolimnetic_ave(C, Vr, time_series A0=23.67*10**6 , threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_hypolimnetic_ave_hadgem_rcp60_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_hypolimnetic_ave'])
        
                
#%% monthly anoxic factor_hadgem_rcp60
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp60'

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
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = monthly_hypolimnetic_ave(C, Vr, time_series A0=23.67*10**6 , threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_hypolimnetic_ave_hadgem_rcp60_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['monthly_hypolimnetic_ave'])
        
                
#%% summer anoxic factor_hadgem_rcp60
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp60'

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
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = summer_hypolimnetic_ave(C, Vr, time_series A0=23.67*10**6 , threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'summer_hypolimnetic_ave_hadgem_rcp60_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['summer_hypolimnetic_ave'])
        
                










#%%monthly_hypolimnetic_ave_hadgem_rcp60

# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp60'

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
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = monthly_hypolimnetic_ave(C, Vr, time_series A0=23.67*10**6 , threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_hypolimnetic_ave_hadgem_rcp60_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                



#%% Annual anoxic factor_hadgem_rcp85
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp85'

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
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = annual_hypolimnetic_ave(C, Vr, time_series A0=23.67*10**6 , threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_hypolimnetic_ave_hadgem_rcp85_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_hypolimnetic_ave'])
        
                
#%% monthly anoxic factor_hadgem_rcp85
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp85'

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
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = monthly_hypolimnetic_ave(C, Vr, time_series A0=23.67*10**6 , threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_hypolimnetic_ave_hadgem_rcp85_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['monthly_hypolimnetic_ave'])
        
                
#%% summer anoxic factor_hadgem_rcp85
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp85'

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
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = summer_hypolimnetic_ave(C, Vr, time_series A0=23.67*10**6 , threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'summer_hypolimnetic_ave_hadgem_rcp85_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['summer_hypolimnetic_ave'])
        
                




#%%monthly_hypolimnetic_ave_hadgem_rcp85

# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp85'

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
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = monthly_hypolimnetic_ave(C, Vr, time_series A0=23.67*10**6 , threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_hypolimnetic_ave_hadgem_rcp85_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
            
#%%ipsl
#%% Annual anoxic factor_ipsl_his
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/his'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("DO_prof_ipsl_his_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = annual_hypolimnetic_ave(C, Vr, time_series A0=23.67*10**6 , threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_hypolimnetic_ave_ipsl_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_hypolimnetic_ave'])
        
                

#%% monthly anoxic factor_ipsl_his
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/his'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("DO_prof_ipsl_his_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = monthly_hypolimnetic_ave(C, Vr, time_series A0=23.67*10**6 , threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_hypolimnetic_ave_ipsl_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['monthly_hypolimnetic_ave'])
        
                
#%% summer anoxic factor_ipsl_his
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/his'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("DO_prof_ipsl_his_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = summer_hypolimnetic_ave(C, Vr, time_series A0=23.67*10**6 , threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'summer_hypolimnetic_ave_ipsl_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['summer_hypolimnetic_ave'])
        
                




#%%monthly_hypolimnetic_ave_ipsl_his

# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/his'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("DO_prof_ipsl_his_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = monthly_hypolimnetic_ave(C, Vr, time_series A0=23.67*10**6 , threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_hypolimnetic_ave_ipsl_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                
#%% Annual anoxic factor_ipsl_rcp26
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp26'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("DO_prof_ipsl_rcp26_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = annual_hypolimnetic_ave(C, Vr, time_series A0=23.67*10**6 , threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_hypolimnetic_ave_ipsl_rcp26_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_hypolimnetic_ave'])
        
#%% monthly anoxic factor_ipsl_rcp26
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp26'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("DO_prof_ipsl_rcp26_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = monthly_hypolimnetic_ave(C, Vr, time_series A0=23.67*10**6 , threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_hypolimnetic_ave_ipsl_rcp26_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['monthly_hypolimnetic_ave'])
        
                
#%% summer anoxic factor_ipsl_rcp26
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp26'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("DO_prof_ipsl_rcp26_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = summer_hypolimnetic_ave(C, Vr, time_series A0=23.67*10**6 , threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'summer_hypolimnetic_ave_ipsl_rcp26_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['summer_hypolimnetic_ave'])
        
                


                


#%%monthly_hypolimnetic_ave_ipsl_rcp26

# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp26'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("DO_prof_ipsl_rcp26_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = monthly_hypolimnetic_ave(C, Vr, time_series A0=23.67*10**6 , threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_hypolimnetic_ave_ipsl_rcp26_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                

#%% Annual anoxic factor_ipsl_rcp60
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp60'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("DO_prof_ipsl_rcp60_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = annual_hypolimnetic_ave(C, Vr, time_series A0=23.67*10**6 , threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_hypolimnetic_ave_ipsl_rcp60_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_hypolimnetic_ave'])
        
                
#%% monthly anoxic factor_ipsl_rcp60
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp60'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("DO_prof_ipsl_rcp60_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = monthly_hypolimnetic_ave(C, Vr, time_series A0=23.67*10**6 , threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_hypolimnetic_ave_ipsl_rcp60_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['monthly_hypolimnetic_ave'])
        
                
#%% summer anoxic factor_ipsl_rcp60
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp60'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("DO_prof_ipsl_rcp60_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = summer_hypolimnetic_ave(C, Vr, time_series A0=23.67*10**6 , threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'summer_hypolimnetic_ave_ipsl_rcp60_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['summer_hypolimnetic_ave'])
        
                










#%%monthly_hypolimnetic_ave_ipsl_rcp60

# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp60'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("DO_prof_ipsl_rcp60_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = monthly_hypolimnetic_ave(C, Vr, time_series A0=23.67*10**6 , threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_hypolimnetic_ave_ipsl_rcp60_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                



#%% Annual anoxic factor_ipsl_rcp85
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp85'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("DO_prof_ipsl_rcp85_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = annual_hypolimnetic_ave(C, Vr, time_series A0=23.67*10**6 , threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_hypolimnetic_ave_ipsl_rcp85_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_hypolimnetic_ave'])
        
                
#%% monthly anoxic factor_ipsl_rcp85
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp85'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("DO_prof_ipsl_rcp85_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = monthly_hypolimnetic_ave(C, Vr, time_series A0=23.67*10**6 , threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_hypolimnetic_ave_ipsl_rcp85_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['monthly_hypolimnetic_ave'])
        
                
#%% summer anoxic factor_ipsl_rcp85
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp85'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("DO_prof_ipsl_rcp85_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = summer_hypolimnetic_ave(C, Vr, time_series A0=23.67*10**6 , threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'summer_hypolimnetic_ave_ipsl_rcp85_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['summer_hypolimnetic_ave'])
        
                




#%%monthly_hypolimnetic_ave_ipsl_rcp85

# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp85'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("DO_prof_ipsl_rcp85_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = monthly_hypolimnetic_ave(C, Vr, time_series A0=23.67*10**6 , threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_hypolimnetic_ave_ipsl_rcp85_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
            
#%%miroc 
#%% Annual anoxic factor_miroc_his
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/his'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("DO_prof_miroc_his_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = annual_hypolimnetic_ave(C, Vr, time_series A0=23.67*10**6 , threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_hypolimnetic_ave_miroc_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_hypolimnetic_ave'])
        
                

#%% monthly anoxic factor_miroc_his
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/his'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("DO_prof_miroc_his_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = monthly_hypolimnetic_ave(C, Vr, time_series A0=23.67*10**6 , threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_hypolimnetic_ave_miroc_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['monthly_hypolimnetic_ave'])
        
                
#%% summer anoxic factor_miroc_his
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/his'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("DO_prof_miroc_his_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = summer_hypolimnetic_ave(C, Vr, time_series A0=23.67*10**6 , threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'summer_hypolimnetic_ave_miroc_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['summer_hypolimnetic_ave'])
        
                




#%%monthly_hypolimnetic_ave_miroc_his

# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/his'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("DO_prof_miroc_his_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = monthly_hypolimnetic_ave(C, Vr, time_series A0=23.67*10**6 , threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_hypolimnetic_ave_miroc_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                
#%% Annual anoxic factor_miroc_rcp26
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp26'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("DO_prof_miroc_rcp26_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = annual_hypolimnetic_ave(C, Vr, time_series A0=23.67*10**6 , threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_hypolimnetic_ave_miroc_rcp26_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_hypolimnetic_ave'])
        
#%% monthly anoxic factor_miroc_rcp26
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp26'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("DO_prof_miroc_rcp26_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = monthly_hypolimnetic_ave(C, Vr, time_series A0=23.67*10**6 , threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_hypolimnetic_ave_miroc_rcp26_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['monthly_hypolimnetic_ave'])
        
                
#%% summer anoxic factor_miroc_rcp26
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp26'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("DO_prof_miroc_rcp26_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = summer_hypolimnetic_ave(C, Vr, time_series A0=23.67*10**6 , threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'summer_hypolimnetic_ave_miroc_rcp26_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['summer_hypolimnetic_ave'])
        
                


                


#%%monthly_hypolimnetic_ave_miroc_rcp26

# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp26'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("DO_prof_miroc_rcp26_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = monthly_hypolimnetic_ave(C, Vr, time_series A0=23.67*10**6 , threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_hypolimnetic_ave_miroc_rcp26_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                

#%% Annual anoxic factor_miroc_rcp60
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp60'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("DO_prof_miroc_rcp60_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = annual_hypolimnetic_ave(C, Vr, time_series A0=23.67*10**6 , threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_hypolimnetic_ave_miroc_rcp60_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_hypolimnetic_ave'])
        
                
#%% monthly anoxic factor_miroc_rcp60
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp60'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("DO_prof_miroc_rcp60_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = monthly_hypolimnetic_ave(C, Vr, time_series A0=23.67*10**6 , threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_hypolimnetic_ave_miroc_rcp60_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['monthly_hypolimnetic_ave'])
        
                
#%% summer anoxic factor_miroc_rcp60
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp60'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("DO_prof_miroc_rcp60_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = summer_hypolimnetic_ave(C, Vr, time_series A0=23.67*10**6 , threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'summer_hypolimnetic_ave_miroc_rcp60_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['summer_hypolimnetic_ave'])
        
                










#%%monthly_hypolimnetic_ave_miroc_rcp60

# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp60'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("DO_prof_miroc_rcp60_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = monthly_hypolimnetic_ave(C, Vr, time_series A0=23.67*10**6 , threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_hypolimnetic_ave_miroc_rcp60_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                



#%% Annual anoxic factor_miroc_rcp85
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp85'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("DO_prof_miroc_rcp85_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = annual_hypolimnetic_ave(C, Vr, time_series A0=23.67*10**6 , threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_hypolimnetic_ave_miroc_rcp85_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_hypolimnetic_ave'])
        
                
#%% monthly anoxic factor_miroc_rcp85
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp85'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("DO_prof_miroc_rcp85_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = monthly_hypolimnetic_ave(C, Vr, time_series A0=23.67*10**6 , threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_hypolimnetic_ave_miroc_rcp85_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['monthly_hypolimnetic_ave'])
        
                
#%% summer anoxic factor_miroc_rcp85
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp85'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("DO_prof_miroc_rcp85_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = summer_hypolimnetic_ave(C, Vr, time_series A0=23.67*10**6 , threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'summer_hypolimnetic_ave_miroc_rcp85_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['summer_hypolimnetic_ave'])
        
                




#%%monthly_hypolimnetic_ave_miroc_rcp85

# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp85'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("DO_prof_miroc_rcp85_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = monthly_hypolimnetic_ave(C, Vr, time_series A0=23.67*10**6 , threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_hypolimnetic_ave_miroc_rcp85_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
            
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%GLUE method raeding again these files %%%%%%%%%%%%%%%%%%%

#%%his_annual_hypolimnetic_ave


# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/his'
all_annual_hypolimnetic_ave_his= pd.DataFrame([])
all_weights= np.array([])


# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("annual_hypolimnetic_ave_gfdl_his"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        annual_hypolimnetic_ave = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        annual_hypolimnetic_ave=annual_hypolimnetic_ave.set_index(annual_hypolimnetic_ave.index)
        
        all_annual_hypolimnetic_ave_his = pd.concat([all_annual_hypolimnetic_ave_his , annual_hypolimnetic_ave['annual_hypolimnetic_ave']], axis=1)
        

directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/his'
        

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("annual_hypolimnetic_ave_hadgem_his"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        annual_hypolimnetic_ave = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        annual_hypolimnetic_ave=annual_hypolimnetic_ave.set_index(annual_hypolimnetic_ave.index)
        
        all_annual_hypolimnetic_ave_his = pd.concat([all_annual_hypolimnetic_ave_his , annual_hypolimnetic_ave['annual_hypolimnetic_ave']], axis=1)
        
        
        

directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/his'
        

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("annual_hypolimnetic_ave_ipsl_his"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        annual_hypolimnetic_ave = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        annual_hypolimnetic_ave=annual_hypolimnetic_ave.set_index(annual_hypolimnetic_ave.index)
        
        all_annual_hypolimnetic_ave_his = pd.concat([all_annual_hypolimnetic_ave_his , annual_hypolimnetic_ave['annual_hypolimnetic_ave']], axis=1)
        
        
        

directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/his'
        

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("annual_hypolimnetic_ave_miroc_his"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        annual_hypolimnetic_ave = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        annual_hypolimnetic_ave=annual_hypolimnetic_ave.set_index(annual_hypolimnetic_ave.index)
        
        all_annual_hypolimnetic_ave_his = pd.concat([all_annual_hypolimnetic_ave_his , annual_hypolimnetic_ave['annual_hypolimnetic_ave']], axis=1)
        
        
        
        
all_annual_hypolimnetic_ave_his= all_annual_hypolimnetic_ave_his.set_index(annual_hypolimnetic_ave['year'])


# annual anoxic duration  
timeseries_year_his= all_annual_hypolimnetic_ave_his.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_annual_hypolimnetic_ave_his.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights))

# Build glue df
glue_df_annual_hypolimnetic_ave_his = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_df_annual_hypolimnetic_ave_his=glue_df_annual_hypolimnetic_ave_his.set_index(timeseries_year_his)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory
glue_df_annual_hypolimnetic_ave_his.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/his/glue_df_anoxic_factor_his.csv')


#%%rcp26_annual_hypolimnetic_ave


# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp26'
all_annual_hypolimnetic_ave_rcp26= pd.DataFrame([])
all_weights= np.array([])


# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("annual_hypolimnetic_ave_gfdl_rcp26"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        annual_hypolimnetic_ave = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        annual_hypolimnetic_ave=annual_hypolimnetic_ave.set_index(annual_hypolimnetic_ave.index)
        
        all_annual_hypolimnetic_ave_rcp26 = pd.concat([all_annual_hypolimnetic_ave_rcp26 , annual_hypolimnetic_ave['annual_hypolimnetic_ave']], axis=1)
        

directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp26'
        

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("annual_hypolimnetic_ave_hadgem_rcp26"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        annual_hypolimnetic_ave = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        annual_hypolimnetic_ave=annual_hypolimnetic_ave.set_index(annual_hypolimnetic_ave.index)
        
        all_annual_hypolimnetic_ave_rcp26 = pd.concat([all_annual_hypolimnetic_ave_rcp26 , annual_hypolimnetic_ave['annual_hypolimnetic_ave']], axis=1)
        
        
        

directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp26'
        

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("annual_hypolimnetic_ave_ipsl_rcp26"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        annual_hypolimnetic_ave = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        annual_hypolimnetic_ave=annual_hypolimnetic_ave.set_index(annual_hypolimnetic_ave.index)
        
        all_annual_hypolimnetic_ave_rcp26 = pd.concat([all_annual_hypolimnetic_ave_rcp26 , annual_hypolimnetic_ave['annual_hypolimnetic_ave']], axis=1)
        
        
        

directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp26'
        

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("annual_hypolimnetic_ave_miroc_rcp26"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        annual_hypolimnetic_ave = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        annual_hypolimnetic_ave=annual_hypolimnetic_ave.set_index(annual_hypolimnetic_ave.index)
        
        all_annual_hypolimnetic_ave_rcp26 = pd.concat([all_annual_hypolimnetic_ave_rcp26 , annual_hypolimnetic_ave['annual_hypolimnetic_ave']], axis=1)
        
        
        
        

all_annual_hypolimnetic_ave_rcp26= all_annual_hypolimnetic_ave_rcp26.set_index(annual_hypolimnetic_ave['year'])

# annual anoxic duration  
timeseries_year_rcp26= all_annual_hypolimnetic_ave_rcp26.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_annual_hypolimnetic_ave_rcp26.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights))

# Build glue df
glue_df_annual_hypolimnetic_ave_rcp26 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_df_annual_hypolimnetic_ave_rcp26=glue_df_annual_hypolimnetic_ave_rcp26.set_index(timeseries_year_rcp26)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory
glue_df_annual_hypolimnetic_ave_rcp26.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/rcp26/glue_df_anoxic_factor_rcp26.csv')


#%%rcp60_annual_hypolimnetic_ave


# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp60'
all_annual_hypolimnetic_ave_rcp60= pd.DataFrame([])
all_weights= np.array([])


# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("annual_hypolimnetic_ave_gfdl_rcp60"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        annual_hypolimnetic_ave = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        annual_hypolimnetic_ave=annual_hypolimnetic_ave.set_index(annual_hypolimnetic_ave.index)
        
        all_annual_hypolimnetic_ave_rcp60 = pd.concat([all_annual_hypolimnetic_ave_rcp60 , annual_hypolimnetic_ave['annual_hypolimnetic_ave']], axis=1)
        

directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp60'
        

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("annual_hypolimnetic_ave_hadgem_rcp60"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        annual_hypolimnetic_ave = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        annual_hypolimnetic_ave=annual_hypolimnetic_ave.set_index(annual_hypolimnetic_ave.index)
        
        all_annual_hypolimnetic_ave_rcp60 = pd.concat([all_annual_hypolimnetic_ave_rcp60 , annual_hypolimnetic_ave['annual_hypolimnetic_ave']], axis=1)
        
        
        

directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp60'
        

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("annual_hypolimnetic_ave_ipsl_rcp60"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        annual_hypolimnetic_ave = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        annual_hypolimnetic_ave=annual_hypolimnetic_ave.set_index(annual_hypolimnetic_ave.index)
        
        all_annual_hypolimnetic_ave_rcp60 = pd.concat([all_annual_hypolimnetic_ave_rcp60 , annual_hypolimnetic_ave['annual_hypolimnetic_ave']], axis=1)
        
        
        

directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp60'
        

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("annual_hypolimnetic_ave_miroc_rcp60"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        annual_hypolimnetic_ave = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        annual_hypolimnetic_ave=annual_hypolimnetic_ave.set_index(annual_hypolimnetic_ave.index)
        
        all_annual_hypolimnetic_ave_rcp60 = pd.concat([all_annual_hypolimnetic_ave_rcp60 , annual_hypolimnetic_ave['annual_hypolimnetic_ave']], axis=1)
        
        
        
        

all_annual_hypolimnetic_ave_rcp60= all_annual_hypolimnetic_ave_rcp60.set_index(annual_hypolimnetic_ave['year'])

# annual anoxic duration  
timeseries_year_rcp60= all_annual_hypolimnetic_ave_rcp60.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_annual_hypolimnetic_ave_rcp60.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights))

# Build glue df
glue_df_annual_hypolimnetic_ave_rcp60 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_df_annual_hypolimnetic_ave_rcp60=glue_df_annual_hypolimnetic_ave_rcp60.set_index(timeseries_year_rcp60)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory
glue_df_annual_hypolimnetic_ave_rcp60.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/rcp60/glue_df_anoxic_factor_rcp60.csv')

#%%rcp85_annual_hypolimnetic_ave


# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp85'
all_annual_hypolimnetic_ave_rcp85= pd.DataFrame([])
all_weights= np.array([])


# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("annual_hypolimnetic_ave_gfdl_rcp85"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        annual_hypolimnetic_ave = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        annual_hypolimnetic_ave=annual_hypolimnetic_ave.set_index(annual_hypolimnetic_ave.index)
        
        all_annual_hypolimnetic_ave_rcp85 = pd.concat([all_annual_hypolimnetic_ave_rcp85 , annual_hypolimnetic_ave['annual_hypolimnetic_ave']], axis=1)
        

directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp85'
        

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("annual_hypolimnetic_ave_hadgem_rcp85"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        annual_hypolimnetic_ave = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        annual_hypolimnetic_ave=annual_hypolimnetic_ave.set_index(annual_hypolimnetic_ave.index)
        
        all_annual_hypolimnetic_ave_rcp85 = pd.concat([all_annual_hypolimnetic_ave_rcp85 , annual_hypolimnetic_ave['annual_hypolimnetic_ave']], axis=1)
        
        
        

directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp85'
        

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("annual_hypolimnetic_ave_ipsl_rcp85"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        annual_hypolimnetic_ave = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        annual_hypolimnetic_ave=annual_hypolimnetic_ave.set_index(annual_hypolimnetic_ave.index)
        
        all_annual_hypolimnetic_ave_rcp85 = pd.concat([all_annual_hypolimnetic_ave_rcp85 , annual_hypolimnetic_ave['annual_hypolimnetic_ave']], axis=1)
        
        
        

directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp85'
        

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("annual_hypolimnetic_ave_miroc_rcp85"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        annual_hypolimnetic_ave = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        annual_hypolimnetic_ave=annual_hypolimnetic_ave.set_index(annual_hypolimnetic_ave.index)
        
        all_annual_hypolimnetic_ave_rcp85 = pd.concat([all_annual_hypolimnetic_ave_rcp85 , annual_hypolimnetic_ave['annual_hypolimnetic_ave']], axis=1)
        
        
        
        
all_annual_hypolimnetic_ave_rcp85= all_annual_hypolimnetic_ave_rcp85.set_index(annual_hypolimnetic_ave['year'])


# annual anoxic duration  
timeseries_year_rcp85= all_annual_hypolimnetic_ave_rcp85.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_annual_hypolimnetic_ave_rcp85.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights))

# Build glue df
glue_df_annual_hypolimnetic_ave_rcp85 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_df_annual_hypolimnetic_ave_rcp85=glue_df_annual_hypolimnetic_ave_rcp85.set_index(timeseries_year_rcp85)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory
glue_df_annual_hypolimnetic_ave_rcp85.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/rcp85/glue_df_anoxic_factor_rcp85.csv')




#%%sorting the indexs_annual_hypolimnetic_ave 

glue_df_annual_hypolimnetic_ave_his= glue_df_annual_hypolimnetic_ave_his.sort_index()
glue_df_annual_hypolimnetic_ave_rcp26= glue_df_annual_hypolimnetic_ave_rcp26.sort_index()
glue_df_annual_hypolimnetic_ave_rcp60= glue_df_annual_hypolimnetic_ave_rcp60.sort_index()
glue_df_annual_hypolimnetic_ave_rcp85= glue_df_annual_hypolimnetic_ave_rcp85.sort_index()


#%% monthly anoxic factor
#%%his_monthly_hypolimnetic_ave


# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/his'
all_monthly_hypolimnetic_ave_his= pd.DataFrame([])
all_weights= np.array([])


# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("monthly_hypolimnetic_ave_gfdl_his"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        monthly_hypolimnetic_ave = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        monthly_hypolimnetic_ave=monthly_hypolimnetic_ave.set_index(monthly_hypolimnetic_ave.index)
        
        all_monthly_hypolimnetic_ave_his = pd.concat([all_monthly_hypolimnetic_ave_his , monthly_hypolimnetic_ave['monthly_hypolimnetic_ave']], axis=1)
        

directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/his'
        

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("monthly_hypolimnetic_ave_hadgem_his"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        monthly_hypolimnetic_ave = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        monthly_hypolimnetic_ave=monthly_hypolimnetic_ave.set_index(monthly_hypolimnetic_ave.index)
        
        all_monthly_hypolimnetic_ave_his = pd.concat([all_monthly_hypolimnetic_ave_his , monthly_hypolimnetic_ave['monthly_hypolimnetic_ave']], axis=1)
        
        
        

directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/his'
        

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("monthly_hypolimnetic_ave_ipsl_his"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        monthly_hypolimnetic_ave = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        monthly_hypolimnetic_ave=monthly_hypolimnetic_ave.set_index(monthly_hypolimnetic_ave.index)
        
        all_monthly_hypolimnetic_ave_his = pd.concat([all_monthly_hypolimnetic_ave_his , monthly_hypolimnetic_ave['monthly_hypolimnetic_ave']], axis=1)
        
        
        

directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/his'
        

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("monthly_hypolimnetic_ave_miroc_his"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        monthly_hypolimnetic_ave = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        monthly_hypolimnetic_ave=monthly_hypolimnetic_ave.set_index(monthly_hypolimnetic_ave.index)
        
        all_monthly_hypolimnetic_ave_his = pd.concat([all_monthly_hypolimnetic_ave_his , monthly_hypolimnetic_ave['monthly_hypolimnetic_ave']], axis=1)
        
        
        
        
all_monthly_hypolimnetic_ave_his= all_monthly_hypolimnetic_ave_his.set_index(monthly_hypolimnetic_ave['year'])


# monthly anoxic duration  
timeseries_year_his= all_monthly_hypolimnetic_ave_his.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_monthly_hypolimnetic_ave_his.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights))

# Build glue df
glue_df_monthly_hypolimnetic_ave_his = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_df_monthly_hypolimnetic_ave_his=glue_df_monthly_hypolimnetic_ave_his.set_index(timeseries_year_his)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory
glue_df_monthly_hypolimnetic_ave_his.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/his/glue_df_anoxic_factor_his.csv')


#%%rcp26_monthly_hypolimnetic_ave


# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp26'
all_monthly_hypolimnetic_ave_rcp26= pd.DataFrame([])
all_weights= np.array([])


# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("monthly_hypolimnetic_ave_gfdl_rcp26"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        monthly_hypolimnetic_ave = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        monthly_hypolimnetic_ave=monthly_hypolimnetic_ave.set_index(monthly_hypolimnetic_ave.index)
        
        all_monthly_hypolimnetic_ave_rcp26 = pd.concat([all_monthly_hypolimnetic_ave_rcp26 , monthly_hypolimnetic_ave['monthly_hypolimnetic_ave']], axis=1)
        

directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp26'
        

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("monthly_hypolimnetic_ave_hadgem_rcp26"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        monthly_hypolimnetic_ave = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        monthly_hypolimnetic_ave=monthly_hypolimnetic_ave.set_index(monthly_hypolimnetic_ave.index)
        
        all_monthly_hypolimnetic_ave_rcp26 = pd.concat([all_monthly_hypolimnetic_ave_rcp26 , monthly_hypolimnetic_ave['monthly_hypolimnetic_ave']], axis=1)
        
        
        

directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp26'
        

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("monthly_hypolimnetic_ave_ipsl_rcp26"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        monthly_hypolimnetic_ave = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        monthly_hypolimnetic_ave=monthly_hypolimnetic_ave.set_index(monthly_hypolimnetic_ave.index)
        
        all_monthly_hypolimnetic_ave_rcp26 = pd.concat([all_monthly_hypolimnetic_ave_rcp26 , monthly_hypolimnetic_ave['monthly_hypolimnetic_ave']], axis=1)
        
        
        

directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp26'
        

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("monthly_hypolimnetic_ave_miroc_rcp26"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        monthly_hypolimnetic_ave = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        monthly_hypolimnetic_ave=monthly_hypolimnetic_ave.set_index(monthly_hypolimnetic_ave.index)
        
        all_monthly_hypolimnetic_ave_rcp26 = pd.concat([all_monthly_hypolimnetic_ave_rcp26 , monthly_hypolimnetic_ave['monthly_hypolimnetic_ave']], axis=1)
        
        
        
        

all_monthly_hypolimnetic_ave_rcp26= all_monthly_hypolimnetic_ave_rcp26.set_index(monthly_hypolimnetic_ave['year'])

# monthly anoxic duration  
timeseries_year_rcp26= all_monthly_hypolimnetic_ave_rcp26.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_monthly_hypolimnetic_ave_rcp26.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights))

# Build glue df
glue_df_monthly_hypolimnetic_ave_rcp26 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_df_monthly_hypolimnetic_ave_rcp26=glue_df_monthly_hypolimnetic_ave_rcp26.set_index(timeseries_year_rcp26)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory
glue_df_monthly_hypolimnetic_ave_rcp26.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/rcp26/glue_df_anoxic_factor_rcp26.csv')


#%%rcp60_monthly_hypolimnetic_ave


# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp60'
all_monthly_hypolimnetic_ave_rcp60= pd.DataFrame([])
all_weights= np.array([])


# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("monthly_hypolimnetic_ave_gfdl_rcp60"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        monthly_hypolimnetic_ave = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        monthly_hypolimnetic_ave=monthly_hypolimnetic_ave.set_index(monthly_hypolimnetic_ave.index)
        
        all_monthly_hypolimnetic_ave_rcp60 = pd.concat([all_monthly_hypolimnetic_ave_rcp60 , monthly_hypolimnetic_ave['monthly_hypolimnetic_ave']], axis=1)
        

directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp60'
        

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("monthly_hypolimnetic_ave_hadgem_rcp60"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        monthly_hypolimnetic_ave = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        monthly_hypolimnetic_ave=monthly_hypolimnetic_ave.set_index(monthly_hypolimnetic_ave.index)
        
        all_monthly_hypolimnetic_ave_rcp60 = pd.concat([all_monthly_hypolimnetic_ave_rcp60 , monthly_hypolimnetic_ave['monthly_hypolimnetic_ave']], axis=1)
        
        
        

directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp60'
        

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("monthly_hypolimnetic_ave_ipsl_rcp60"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        monthly_hypolimnetic_ave = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        monthly_hypolimnetic_ave=monthly_hypolimnetic_ave.set_index(monthly_hypolimnetic_ave.index)
        
        all_monthly_hypolimnetic_ave_rcp60 = pd.concat([all_monthly_hypolimnetic_ave_rcp60 , monthly_hypolimnetic_ave['monthly_hypolimnetic_ave']], axis=1)
        
        
        

directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp60'
        

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("monthly_hypolimnetic_ave_miroc_rcp60"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        monthly_hypolimnetic_ave = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        monthly_hypolimnetic_ave=monthly_hypolimnetic_ave.set_index(monthly_hypolimnetic_ave.index)
        
        all_monthly_hypolimnetic_ave_rcp60 = pd.concat([all_monthly_hypolimnetic_ave_rcp60 , monthly_hypolimnetic_ave['monthly_hypolimnetic_ave']], axis=1)
        
        
        
        

all_monthly_hypolimnetic_ave_rcp60= all_monthly_hypolimnetic_ave_rcp60.set_index(monthly_hypolimnetic_ave['year'])

# monthly anoxic duration  
timeseries_year_rcp60= all_monthly_hypolimnetic_ave_rcp60.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_monthly_hypolimnetic_ave_rcp60.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights))

# Build glue df
glue_df_monthly_hypolimnetic_ave_rcp60 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_df_monthly_hypolimnetic_ave_rcp60=glue_df_monthly_hypolimnetic_ave_rcp60.set_index(timeseries_year_rcp60)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory
glue_df_monthly_hypolimnetic_ave_rcp60.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/rcp60/glue_df_anoxic_factor_rcp60.csv')

#%%rcp85_monthly_hypolimnetic_ave


# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp85'
all_monthly_hypolimnetic_ave_rcp85= pd.DataFrame([])
all_weights= np.array([])


# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("monthly_hypolimnetic_ave_gfdl_rcp85"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        monthly_hypolimnetic_ave = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        monthly_hypolimnetic_ave=monthly_hypolimnetic_ave.set_index(monthly_hypolimnetic_ave.index)
        
        all_monthly_hypolimnetic_ave_rcp85 = pd.concat([all_monthly_hypolimnetic_ave_rcp85 , monthly_hypolimnetic_ave['monthly_hypolimnetic_ave']], axis=1)
        

directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp85'
        

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("monthly_hypolimnetic_ave_hadgem_rcp85"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        monthly_hypolimnetic_ave = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        monthly_hypolimnetic_ave=monthly_hypolimnetic_ave.set_index(monthly_hypolimnetic_ave.index)
        
        all_monthly_hypolimnetic_ave_rcp85 = pd.concat([all_monthly_hypolimnetic_ave_rcp85 , monthly_hypolimnetic_ave['monthly_hypolimnetic_ave']], axis=1)
        
        
        

directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp85'
        

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("monthly_hypolimnetic_ave_ipsl_rcp85"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        monthly_hypolimnetic_ave = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        monthly_hypolimnetic_ave=monthly_hypolimnetic_ave.set_index(monthly_hypolimnetic_ave.index)
        
        all_monthly_hypolimnetic_ave_rcp85 = pd.concat([all_monthly_hypolimnetic_ave_rcp85 , monthly_hypolimnetic_ave['monthly_hypolimnetic_ave']], axis=1)
        
        
        

directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp85'
        

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("monthly_hypolimnetic_ave_miroc_rcp85"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        monthly_hypolimnetic_ave = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        monthly_hypolimnetic_ave=monthly_hypolimnetic_ave.set_index(monthly_hypolimnetic_ave.index)
        
        all_monthly_hypolimnetic_ave_rcp85 = pd.concat([all_monthly_hypolimnetic_ave_rcp85 , monthly_hypolimnetic_ave['monthly_hypolimnetic_ave']], axis=1)
        
        
        
        
all_monthly_hypolimnetic_ave_rcp85= all_monthly_hypolimnetic_ave_rcp85.set_index(monthly_hypolimnetic_ave['year'])


# monthly anoxic duration  
timeseries_year_rcp85= all_monthly_hypolimnetic_ave_rcp85.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_monthly_hypolimnetic_ave_rcp85.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights))

# Build glue df
glue_df_monthly_hypolimnetic_ave_rcp85 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_df_monthly_hypolimnetic_ave_rcp85=glue_df_monthly_hypolimnetic_ave_rcp85.set_index(timeseries_year_rcp85)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory
glue_df_monthly_hypolimnetic_ave_rcp85.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/rcp85/glue_df_anoxic_factor_rcp85.csv')



#%%sorting the indexs_monthly_hypolimnetic_ave 

glue_df_monthly_hypolimnetic_ave_his= glue_df_monthly_hypolimnetic_ave_his.sort_index()
glue_df_monthly_hypolimnetic_ave_rcp26= glue_df_monthly_hypolimnetic_ave_rcp26.sort_index()
glue_df_monthly_hypolimnetic_ave_rcp60= glue_df_monthly_hypolimnetic_ave_rcp60.sort_index()
glue_df_monthly_hypolimnetic_ave_rcp85= glue_df_monthly_hypolimnetic_ave_rcp85.sort_index()



#%%===== summer anoxic factor Glue dataframe 

#%%his_summer_hypolimnetic_ave


# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/his'
all_summer_hypolimnetic_ave_his= pd.DataFrame([])
all_weights= np.array([])


# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("summer_hypolimnetic_ave_gfdl_his"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        summer_hypolimnetic_ave = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        summer_hypolimnetic_ave=summer_hypolimnetic_ave.set_index(summer_hypolimnetic_ave.index)
        
        all_summer_hypolimnetic_ave_his = pd.concat([all_summer_hypolimnetic_ave_his , summer_hypolimnetic_ave['summer_hypolimnetic_ave']], axis=1)
        

directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/his'
        

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("summer_hypolimnetic_ave_hadgem_his"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        summer_hypolimnetic_ave = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        summer_hypolimnetic_ave=summer_hypolimnetic_ave.set_index(summer_hypolimnetic_ave.index)
        
        all_summer_hypolimnetic_ave_his = pd.concat([all_summer_hypolimnetic_ave_his , summer_hypolimnetic_ave['summer_hypolimnetic_ave']], axis=1)
        
        
        

directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/his'
        

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("summer_hypolimnetic_ave_ipsl_his"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        summer_hypolimnetic_ave = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        summer_hypolimnetic_ave=summer_hypolimnetic_ave.set_index(summer_hypolimnetic_ave.index)
        
        all_summer_hypolimnetic_ave_his = pd.concat([all_summer_hypolimnetic_ave_his , summer_hypolimnetic_ave['summer_hypolimnetic_ave']], axis=1)
        
        
        

directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/his'
        

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("summer_hypolimnetic_ave_miroc_his"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        summer_hypolimnetic_ave = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        summer_hypolimnetic_ave=summer_hypolimnetic_ave.set_index(summer_hypolimnetic_ave.index)
        
        all_summer_hypolimnetic_ave_his = pd.concat([all_summer_hypolimnetic_ave_his , summer_hypolimnetic_ave['summer_hypolimnetic_ave']], axis=1)
        
        
        
        
all_summer_hypolimnetic_ave_his= all_summer_hypolimnetic_ave_his.set_index(summer_hypolimnetic_ave['year'])


# summer anoxic duration  
timeseries_year_his= all_summer_hypolimnetic_ave_his.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_summer_hypolimnetic_ave_his.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights))

# Build glue df
glue_df_summer_hypolimnetic_ave_his = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_df_summer_hypolimnetic_ave_his=glue_df_summer_hypolimnetic_ave_his.set_index(timeseries_year_his)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory
glue_df_summer_hypolimnetic_ave_his.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/his/glue_df_anoxic_factor_his.csv')


#%%rcp26_summer_hypolimnetic_ave


# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp26'
all_summer_hypolimnetic_ave_rcp26= pd.DataFrame([])
all_weights= np.array([])


# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("summer_hypolimnetic_ave_gfdl_rcp26"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        summer_hypolimnetic_ave = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        summer_hypolimnetic_ave=summer_hypolimnetic_ave.set_index(summer_hypolimnetic_ave.index)
        
        all_summer_hypolimnetic_ave_rcp26 = pd.concat([all_summer_hypolimnetic_ave_rcp26 , summer_hypolimnetic_ave['summer_hypolimnetic_ave']], axis=1)
        

directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp26'
        

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("summer_hypolimnetic_ave_hadgem_rcp26"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        summer_hypolimnetic_ave = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        summer_hypolimnetic_ave=summer_hypolimnetic_ave.set_index(summer_hypolimnetic_ave.index)
        
        all_summer_hypolimnetic_ave_rcp26 = pd.concat([all_summer_hypolimnetic_ave_rcp26 , summer_hypolimnetic_ave['summer_hypolimnetic_ave']], axis=1)
        
        
        

directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp26'
        

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("summer_hypolimnetic_ave_ipsl_rcp26"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        summer_hypolimnetic_ave = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        summer_hypolimnetic_ave=summer_hypolimnetic_ave.set_index(summer_hypolimnetic_ave.index)
        
        all_summer_hypolimnetic_ave_rcp26 = pd.concat([all_summer_hypolimnetic_ave_rcp26 , summer_hypolimnetic_ave['summer_hypolimnetic_ave']], axis=1)
        
        
        

directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp26'
        

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("summer_hypolimnetic_ave_miroc_rcp26"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        summer_hypolimnetic_ave = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        summer_hypolimnetic_ave=summer_hypolimnetic_ave.set_index(summer_hypolimnetic_ave.index)
        
        all_summer_hypolimnetic_ave_rcp26 = pd.concat([all_summer_hypolimnetic_ave_rcp26 , summer_hypolimnetic_ave['summer_hypolimnetic_ave']], axis=1)
        
        
        
        

all_summer_hypolimnetic_ave_rcp26= all_summer_hypolimnetic_ave_rcp26.set_index(summer_hypolimnetic_ave['year'])

# summer anoxic duration  
timeseries_year_rcp26= all_summer_hypolimnetic_ave_rcp26.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_summer_hypolimnetic_ave_rcp26.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights))

# Build glue df
glue_df_summer_hypolimnetic_ave_rcp26 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_df_summer_hypolimnetic_ave_rcp26=glue_df_summer_hypolimnetic_ave_rcp26.set_index(timeseries_year_rcp26)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory
glue_df_summer_hypolimnetic_ave_rcp26.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/rcp26/glue_df_anoxic_factor_rcp26.csv')


#%%rcp60_summer_hypolimnetic_ave


# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp60'
all_summer_hypolimnetic_ave_rcp60= pd.DataFrame([])
all_weights= np.array([])


# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("summer_hypolimnetic_ave_gfdl_rcp60"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        summer_hypolimnetic_ave = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        summer_hypolimnetic_ave=summer_hypolimnetic_ave.set_index(summer_hypolimnetic_ave.index)
        
        all_summer_hypolimnetic_ave_rcp60 = pd.concat([all_summer_hypolimnetic_ave_rcp60 , summer_hypolimnetic_ave['summer_hypolimnetic_ave']], axis=1)
        

directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp60'
        

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("summer_hypolimnetic_ave_hadgem_rcp60"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        summer_hypolimnetic_ave = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        summer_hypolimnetic_ave=summer_hypolimnetic_ave.set_index(summer_hypolimnetic_ave.index)
        
        all_summer_hypolimnetic_ave_rcp60 = pd.concat([all_summer_hypolimnetic_ave_rcp60 , summer_hypolimnetic_ave['summer_hypolimnetic_ave']], axis=1)
        
        
        

directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp60'
        

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("summer_hypolimnetic_ave_ipsl_rcp60"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        summer_hypolimnetic_ave = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        summer_hypolimnetic_ave=summer_hypolimnetic_ave.set_index(summer_hypolimnetic_ave.index)
        
        all_summer_hypolimnetic_ave_rcp60 = pd.concat([all_summer_hypolimnetic_ave_rcp60 , summer_hypolimnetic_ave['summer_hypolimnetic_ave']], axis=1)
        
        
        

directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp60'
        

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("summer_hypolimnetic_ave_miroc_rcp60"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        summer_hypolimnetic_ave = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        summer_hypolimnetic_ave=summer_hypolimnetic_ave.set_index(summer_hypolimnetic_ave.index)
        
        all_summer_hypolimnetic_ave_rcp60 = pd.concat([all_summer_hypolimnetic_ave_rcp60 , summer_hypolimnetic_ave['summer_hypolimnetic_ave']], axis=1)
        
        
        
        

all_summer_hypolimnetic_ave_rcp60= all_summer_hypolimnetic_ave_rcp60.set_index(summer_hypolimnetic_ave['year'])

# summer anoxic duration  
timeseries_year_rcp60= all_summer_hypolimnetic_ave_rcp60.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_summer_hypolimnetic_ave_rcp60.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights))

# Build glue df
glue_df_summer_hypolimnetic_ave_rcp60 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_df_summer_hypolimnetic_ave_rcp60=glue_df_summer_hypolimnetic_ave_rcp60.set_index(timeseries_year_rcp60)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory
glue_df_summer_hypolimnetic_ave_rcp60.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/rcp60/glue_df_anoxic_factor_rcp60.csv')

#%%rcp85_summer_hypolimnetic_ave


# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp85'
all_summer_hypolimnetic_ave_rcp85= pd.DataFrame([])
all_weights= np.array([])


# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("summer_hypolimnetic_ave_gfdl_rcp85"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        summer_hypolimnetic_ave = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        summer_hypolimnetic_ave=summer_hypolimnetic_ave.set_index(summer_hypolimnetic_ave.index)
        
        all_summer_hypolimnetic_ave_rcp85 = pd.concat([all_summer_hypolimnetic_ave_rcp85 , summer_hypolimnetic_ave['summer_hypolimnetic_ave']], axis=1)
        

directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp85'
        

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("summer_hypolimnetic_ave_hadgem_rcp85"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        summer_hypolimnetic_ave = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        summer_hypolimnetic_ave=summer_hypolimnetic_ave.set_index(summer_hypolimnetic_ave.index)
        
        all_summer_hypolimnetic_ave_rcp85 = pd.concat([all_summer_hypolimnetic_ave_rcp85 , summer_hypolimnetic_ave['summer_hypolimnetic_ave']], axis=1)
        
        
        

directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp85'
        

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("summer_hypolimnetic_ave_ipsl_rcp85"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        summer_hypolimnetic_ave = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        summer_hypolimnetic_ave=summer_hypolimnetic_ave.set_index(summer_hypolimnetic_ave.index)
        
        all_summer_hypolimnetic_ave_rcp85 = pd.concat([all_summer_hypolimnetic_ave_rcp85 , summer_hypolimnetic_ave['summer_hypolimnetic_ave']], axis=1)
        
        
        

directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp85'
        

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("summer_hypolimnetic_ave_miroc_rcp85"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        summer_hypolimnetic_ave = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        summer_hypolimnetic_ave=summer_hypolimnetic_ave.set_index(summer_hypolimnetic_ave.index)
        
        all_summer_hypolimnetic_ave_rcp85 = pd.concat([all_summer_hypolimnetic_ave_rcp85 , summer_hypolimnetic_ave['summer_hypolimnetic_ave']], axis=1)
        
        
        
        
all_summer_hypolimnetic_ave_rcp85= all_summer_hypolimnetic_ave_rcp85.set_index(summer_hypolimnetic_ave['year'])


# summer anoxic duration  
timeseries_year_rcp85= all_summer_hypolimnetic_ave_rcp85.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_summer_hypolimnetic_ave_rcp85.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights))

# Build glue df
glue_df_summer_hypolimnetic_ave_rcp85 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_df_summer_hypolimnetic_ave_rcp85=glue_df_summer_hypolimnetic_ave_rcp85.set_index(timeseries_year_rcp85)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory
glue_df_summer_hypolimnetic_ave_rcp85.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/rcp85/glue_df_anoxic_factor_rcp85.csv')


#%%sorting the indexs_summer_hypolimnetic_ave 

glue_df_summer_hypolimnetic_ave_his= glue_df_summer_hypolimnetic_ave_his.sort_index()
glue_df_summer_hypolimnetic_ave_rcp26= glue_df_summer_hypolimnetic_ave_rcp26.sort_index()
glue_df_summer_hypolimnetic_ave_rcp60= glue_df_summer_hypolimnetic_ave_rcp60.sort_index()
glue_df_summer_hypolimnetic_ave_rcp85= glue_df_summer_hypolimnetic_ave_rcp85.sort_index()













#%%Plotting and analyses 



#%%########annual anoxic factor 

#%%ploting annual anoxic factor 

os.chdir('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/')

import matplotlib.pyplot as plt

fig =plt.figure(figsize=(15, 10))
ax= plt.subplot(111)


ax=plt.fill_between(glue_df_annual_hypolimnetic_ave_his.index.astype(float), glue_df_annual_hypolimnetic_ave_his['5%'], glue_df_annual_hypolimnetic_ave_his['95%'], color='grey', alpha=0.2 ,  label= 'His 90% CI')
ax=plt.plot(glue_df_annual_hypolimnetic_ave_his.index.astype(float), glue_df_annual_hypolimnetic_ave_his['50%'].astype(float), 'k', label='His median', alpha=0.9, linewidth=3  )



ax=plt.fill_between(glue_df_annual_hypolimnetic_ave_rcp26.index.astype(float), glue_df_annual_hypolimnetic_ave_rcp26['5%'], glue_df_annual_hypolimnetic_ave_rcp26['95%'], color='darkgreen', alpha=0.3 ,  label= 'RCP2.6 90% CI')
ax=plt.plot(glue_df_annual_hypolimnetic_ave_rcp26.index.astype(float), glue_df_annual_hypolimnetic_ave_rcp26['50%'], 'darkgreen', label='RCP2.6 median', alpha=0.9, linewidth=3  )


ax=plt.fill_between(glue_df_annual_hypolimnetic_ave_rcp60.index.astype(float), glue_df_annual_hypolimnetic_ave_rcp60['5%'], glue_df_annual_hypolimnetic_ave_rcp60['95%'], color='yellow', alpha=0.2 ,  label= 'RCP6.0 90% CI')
ax=plt.plot(glue_df_annual_hypolimnetic_ave_rcp60.index.astype(float), glue_df_annual_hypolimnetic_ave_rcp60['50%'], 'yellow', label='RCP6.0 median', alpha=0.9, linewidth=3  )

ax=plt.fill_between(glue_df_annual_hypolimnetic_ave_rcp85.index.astype(float), glue_df_annual_hypolimnetic_ave_rcp85['5%'], glue_df_annual_hypolimnetic_ave_rcp85['95%'], color='r', alpha=0.2 ,  label= 'RCP8.5 90% CI')
ax=plt.plot(glue_df_annual_hypolimnetic_ave_rcp85.index.astype(float), glue_df_annual_hypolimnetic_ave_rcp85['50%'], 'r', label='RCP8.5 median', alpha=0.9, linewidth=3  )

ax=plt.ylabel('anoxic factor per each deoxygenation period [d/year]' , fontsize=26)
ax=plt.xlabel('Year' , fontsize=26)
ax=plt.yticks(fontsize= 22)
ax=plt.xticks(rotation=45 , fontsize=22)
ax=plt.legend(bbox_to_anchor=(0.7, -0.2), fontsize=22)#)   
fig.savefig("GLUE_Timeseries_annual_hypolimnetic_ave.png",  dpi=300, bbox_inches='tight')




#%%
np.mean(glue_df_annual_hypolimnetic_ave_his['50%'])#6.077082662821386
np.mean(glue_df_annual_hypolimnetic_ave_rcp26['50%'])#7.992767795524755
np.mean(glue_df_annual_hypolimnetic_ave_rcp60['50%'])#8.585258963812871
np.mean(glue_df_annual_hypolimnetic_ave_rcp85['50%'])#9.156680524881311

#%%anoxic_factor 30 yerars from each scenarios compare 



#anormaly 
# baseline [1976-2005]
glue_base_annual_hypolimnetic_ave_his=glue_df_annual_hypolimnetic_ave_his[1975 < glue_df_annual_hypolimnetic_ave_his.index]['50%']
annual_hypolimnetic_ave_ref=np.mean(glue_base_annual_hypolimnetic_ave_his)
#6.389027950812897


#near future [2030-2059]

glue_near_future_annual_hypolimnetic_ave_rcp26=glue_df_annual_hypolimnetic_ave_rcp26[(2029 < glue_df_annual_hypolimnetic_ave_rcp26.index) & (glue_df_annual_hypolimnetic_ave_rcp26.index < 2060)]['50%']
np.mean(glue_near_future_annual_hypolimnetic_ave_rcp26)
# 8.070525139552648
glue_near_future_annual_hypolimnetic_ave_rcp60=glue_df_annual_hypolimnetic_ave_rcp60[(2029 < glue_df_annual_hypolimnetic_ave_rcp60.index) & (glue_df_annual_hypolimnetic_ave_rcp60.index < 2060)]['50%']
np.mean(glue_near_future_annual_hypolimnetic_ave_rcp60)
# 8.107889314159742
glue_near_future_annual_hypolimnetic_ave_rcp85=glue_df_annual_hypolimnetic_ave_rcp85[(2029 < glue_df_annual_hypolimnetic_ave_rcp85.index) & (glue_df_annual_hypolimnetic_ave_rcp85.index < 2060)]['50%']
np.mean(glue_near_future_annual_hypolimnetic_ave_rcp85)
# 8.63044924136971

 
#Distant future [2070-2099]

glue_distant_future_annual_hypolimnetic_ave_rcp26=glue_df_annual_hypolimnetic_ave_rcp26[(2069 < glue_df_annual_hypolimnetic_ave_rcp26.index) & (glue_df_annual_hypolimnetic_ave_rcp26.index < 2100)]['50%']
np.mean(glue_distant_future_annual_hypolimnetic_ave_rcp26)
#8.153608896799094
glue_distant_future_annual_hypolimnetic_ave_rcp60=glue_df_annual_hypolimnetic_ave_rcp60[(2069 < glue_df_annual_hypolimnetic_ave_rcp60.index) & (glue_df_annual_hypolimnetic_ave_rcp60.index< 2100)]['50%']
np.mean(glue_distant_future_annual_hypolimnetic_ave_rcp60)
#9.787975473676404
glue_distant_future_annual_hypolimnetic_ave_rcp85=glue_df_annual_hypolimnetic_ave_rcp85[(2069 < glue_df_annual_hypolimnetic_ave_rcp85.index) & (glue_df_annual_hypolimnetic_ave_rcp85.index < 2100)]['50%']
np.mean(glue_distant_future_annual_hypolimnetic_ave_rcp85)
#10.985644903398574
   


###====over 30 years in his and each RCPs 

# baseline [1976-2005]
autocorr_MK_org_modif_sens_slope_test(glue_base_annual_hypolimnetic_ave_his)
(0.03791672471698212,
 'positively autocorrelated',
 'increasing',
 0.004067701513906119,
 0.04887120166082099,
 5.685266536515649)


#near future [2030-2059]


autocorr_MK_org_modif_sens_slope_test(glue_near_future_annual_hypolimnetic_ave_rcp26)
(0.018345477426765625,
 'positively autocorrelated',
 'no trend',
 0.09353135296636017,
 0,
 0)

autocorr_MK_org_modif_sens_slope_test(glue_near_future_annual_hypolimnetic_ave_rcp60)
(0.011313156566510486,
 'positively autocorrelated',
 'increasing',
 0.0007961960227531595,
 0.0470080311379157,
 7.4730648265627355)

autocorr_MK_org_modif_sens_slope_test(glue_near_future_annual_hypolimnetic_ave_rcp85)

(0.01548644557384171,
 'positively autocorrelated',
 'increasing',
 0.0048191095611576085,
 0.05773266804253006,
 7.722484654253696)



#Distant future [2070-2099]


autocorr_MK_org_modif_sens_slope_test(glue_distant_future_annual_hypolimnetic_ave_rcp26)
(0.015039983618369416,
 'positively autocorrelated',
 'no trend',
 0.1989481007752456,
 0,
 0)

autocorr_MK_org_modif_sens_slope_test(glue_distant_future_annual_hypolimnetic_ave_rcp60)
(0.012394095955031883,
 'positively autocorrelated',
 'no trend',
 0.41182433473249125,
 0,
 0)
autocorr_MK_org_modif_sens_slope_test(glue_distant_future_annual_hypolimnetic_ave_rcp85)
(0.014499198182054042,
 'positively autocorrelated',
 'increasing',
 0.026946782463489027,
 0.05377923636923881,
 10.323144222989352)






#%% 80 years from 2020 for annual_hypolimnetic_ave


glue_80years_annual_hypolimnetic_ave_rcp26=glue_df_annual_hypolimnetic_ave_rcp26[2019 < glue_df_annual_hypolimnetic_ave_rcp26.index]

glue_80years_annual_hypolimnetic_ave_rcp60=glue_df_annual_hypolimnetic_ave_rcp60[2019 < glue_df_annual_hypolimnetic_ave_rcp60.index]

glue_80years_annual_hypolimnetic_ave_rcp85=glue_df_annual_hypolimnetic_ave_rcp85[2019 < glue_df_annual_hypolimnetic_ave_rcp85.index]


#============= mean of first 10 yaers over 80 years 

#rcp2.6
np.mean(glue_80years_annual_hypolimnetic_ave_rcp26[glue_80years_annual_hypolimnetic_ave_rcp26.index<2030]['50%'])
7.781968220542252

#rcp6.0
np.mean(glue_80years_annual_hypolimnetic_ave_rcp60[glue_80years_annual_hypolimnetic_ave_rcp60.index<2030]['50%'])
7.835574478598173

#rcp8.5
np.mean(glue_80years_annual_hypolimnetic_ave_rcp85[glue_80years_annual_hypolimnetic_ave_rcp85.index<2030]['50%'])
7.7236229767454985

#============== mean of last 10 yaers over 80 years 

#rcp2.6
np.mean(glue_80years_annual_hypolimnetic_ave_rcp26[glue_80years_annual_hypolimnetic_ave_rcp26.index>2079]['50%'])
8.243966830565041

#rcp6.0
np.mean(glue_80years_annual_hypolimnetic_ave_rcp60[glue_80years_annual_hypolimnetic_ave_rcp60.index>2079]['50%'])
9.864621453257977

#rcp8.5
np.mean(glue_80years_annual_hypolimnetic_ave_rcp85[glue_80years_annual_hypolimnetic_ave_rcp85.index>2079]['50%'])
11.160292464667199

#=========== trendline # Over the 80 years


autocorr_MK_org_modif_sens_slope_test(glue_80years_annual_hypolimnetic_ave_rcp26['50%'])
(0.02031492443906448,
 'positively autocorrelated',
 'no trend',
 0.11371844918011509,
 0,
 0)


autocorr_MK_org_modif_sens_slope_test(glue_80years_annual_hypolimnetic_ave_rcp60['50%'])
(0.012504340139489645,
 'positively autocorrelated',
 'increasing',
 1.4566126083082054e-13,
 0.036058805989694846,
 7.282950340706922)



autocorr_MK_org_modif_sens_slope_test(glue_80years_annual_hypolimnetic_ave_rcp85['50%'])
(0.015711631920486826,
 'positively autocorrelated',
 'increasing',
 0.0,
 0.05742827331247126,
 7.128166722990812)





#%%If there is a trend in entire 

# in whole his
autocorr_MK_org_modif_sens_slope_test(glue_df_annual_hypolimnetic_ave_his['50%'])
(0.054103668580385816,
 'positively autocorrelated',
 'no trend',
 0.07068845447209426,
 0,
 0)

#in intire rcp2.6
autocorr_MK_org_modif_sens_slope_test(glue_df_annual_hypolimnetic_ave_rcp26['50%'])
(0.02002132148516097,
 'positively autocorrelated',
 'increasing',
 0.0012506240636172006,
 0.009277291512717471,
 7.539997545595559)

#in entire rcp6.0
autocorr_MK_org_modif_sens_slope_test(glue_df_annual_hypolimnetic_ave_rcp60['50%'])
(0.01438079345143515,
 'positively autocorrelated',
 'increasing',
 2.6645352591003757e-13,
 0.03278504999647535,
 6.993374854517668)

#in entire rcp8.5
autocorr_MK_org_modif_sens_slope_test(glue_df_annual_hypolimnetic_ave_rcp85['50%'])
(0.01670964657273115,
 'positively autocorrelated',
 'increasing',
 0.0,
 0.05615663487366421,
 6.386209763383056)

#slope in entire RCP8.5> RCP6.0>RCP2.6 # his no trend 



 
#%%anoxic_factor_anormaly 
os.chdir('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/')

import matplotlib.pyplot as plt

fig =plt.figure(figsize=(15, 10))
ax= plt.subplot(111)


ax=plt.fill_between(glue_df_annual_hypolimnetic_ave_his[(1960 < glue_df_annual_hypolimnetic_ave_his.index)].index.astype(float),
                      glue_df_annual_hypolimnetic_ave_his[(1960 < glue_df_annual_hypolimnetic_ave_his.index)]['5%'] - annual_hypolimnetic_ave_ref,
                      glue_df_annual_hypolimnetic_ave_his[(1960 < glue_df_annual_hypolimnetic_ave_his.index) ]['95%'] - annual_hypolimnetic_ave_ref,
                      color='grey', alpha=0.2, label='His 90% CI')


ax=plt.plot(glue_df_annual_hypolimnetic_ave_his[(1960 < glue_df_annual_hypolimnetic_ave_his.index) ].index.astype(float),
            glue_df_annual_hypolimnetic_ave_his[(1960 < glue_df_annual_hypolimnetic_ave_his.index)]['50%'] - annual_hypolimnetic_ave_ref,
            'k', label='His median', alpha=0.9, linewidth=3   )

ax=plt.fill_between(glue_df_annual_hypolimnetic_ave_rcp26.index.astype(float), glue_df_annual_hypolimnetic_ave_rcp26['5%']-annual_hypolimnetic_ave_ref, glue_df_annual_hypolimnetic_ave_rcp26['95%']-annual_hypolimnetic_ave_ref, color='darkgreen', alpha=0.3 ,  label= 'RCP6.0 90% CI')
ax=plt.plot(glue_df_annual_hypolimnetic_ave_rcp26.index.astype(float), glue_df_annual_hypolimnetic_ave_rcp26['50%']-annual_hypolimnetic_ave_ref, 'darkgreen', label='RCP6.0 median', alpha=0.9, linewidth=3  )
                      
                     
ax=plt.fill_between(glue_df_annual_hypolimnetic_ave_rcp60.index.astype(float), glue_df_annual_hypolimnetic_ave_rcp60['5%']-annual_hypolimnetic_ave_ref, glue_df_annual_hypolimnetic_ave_rcp60['95%']-annual_hypolimnetic_ave_ref, color='yellow', alpha=0.2 ,  label= 'RCP6.0 90% CI')
ax=plt.plot(glue_df_annual_hypolimnetic_ave_rcp60.index.astype(float), glue_df_annual_hypolimnetic_ave_rcp60['50%']-annual_hypolimnetic_ave_ref, 'yellow', label='RCP6.0 median', alpha=0.9, linewidth=3  )

ax=plt.fill_between(glue_df_annual_hypolimnetic_ave_rcp85.index.astype(float), glue_df_annual_hypolimnetic_ave_rcp85['5%']-annual_hypolimnetic_ave_ref, glue_df_annual_hypolimnetic_ave_rcp85['95%']-annual_hypolimnetic_ave_ref, color='r', alpha=0.2 ,  label= 'RCP8.5 90% CI')
ax=plt.plot(glue_df_annual_hypolimnetic_ave_rcp85.index.astype(float), glue_df_annual_hypolimnetic_ave_rcp85['50%']-annual_hypolimnetic_ave_ref, 'r', label='RCP8.5 median', alpha=0.9, linewidth=3  )

ax=plt.ylabel('Anormaly of annual anoxic factor [d year$^{-1}$]' , fontsize=26)
ax=plt.xlabel('Year' , fontsize=26)
ax=plt.yticks(fontsize= 22)
ax=plt.xticks(rotation=45 , fontsize=22)
ax=plt.legend(bbox_to_anchor=(0.7, -0.2), fontsize=22)  
fig.savefig("GLUE_Timeseries_annual_hypolimnetic_ave_anormaly.png",  dpi=300, bbox_inches='tight')











#%%===========Apr-Oct average of anoxic afctor 


#%%ploting monthly anoxic factor 

os.chdir('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/')

import matplotlib.pyplot as plt

fig =plt.figure(figsize=(15, 10))
ax= plt.subplot(111)


ax=plt.fill_between(glue_df_monthly_hypolimnetic_ave_his.index.astype(float), glue_df_monthly_hypolimnetic_ave_his['5%'], glue_df_monthly_hypolimnetic_ave_his['95%'], color='grey', alpha=0.2 ,  label= 'His 90% CI')
ax=plt.plot(glue_df_monthly_hypolimnetic_ave_his.index.astype(float), glue_df_monthly_hypolimnetic_ave_his['50%'].astype(float), 'k', label='His median', alpha=0.9, linewidth=3  )



ax=plt.fill_between(glue_df_monthly_hypolimnetic_ave_rcp26.index.astype(float), glue_df_monthly_hypolimnetic_ave_rcp26['5%'], glue_df_monthly_hypolimnetic_ave_rcp26['95%'], color='darkgreen', alpha=0.3 ,  label= 'RCP2.6 90% CI')
ax=plt.plot(glue_df_monthly_hypolimnetic_ave_rcp26.index.astype(float), glue_df_monthly_hypolimnetic_ave_rcp26['50%'], 'darkgreen', label='RCP2.6 median', alpha=0.9, linewidth=3  )


ax=plt.fill_between(glue_df_monthly_hypolimnetic_ave_rcp60.index.astype(float), glue_df_monthly_hypolimnetic_ave_rcp60['5%'], glue_df_monthly_hypolimnetic_ave_rcp60['95%'], color='yellow', alpha=0.2 ,  label= 'RCP6.0 90% CI')
ax=plt.plot(glue_df_monthly_hypolimnetic_ave_rcp60.index.astype(float), glue_df_monthly_hypolimnetic_ave_rcp60['50%'], 'yellow', label='RCP6.0 median', alpha=0.9, linewidth=3  )

ax=plt.fill_between(glue_df_monthly_hypolimnetic_ave_rcp85.index.astype(float), glue_df_monthly_hypolimnetic_ave_rcp85['5%'], glue_df_monthly_hypolimnetic_ave_rcp85['95%'], color='r', alpha=0.2 ,  label= 'RCP8.5 90% CI')
ax=plt.plot(glue_df_monthly_hypolimnetic_ave_rcp85.index.astype(float), glue_df_monthly_hypolimnetic_ave_rcp85['50%'], 'r', label='RCP8.5 median', alpha=0.9, linewidth=3  )

ax=plt.ylabel('Anoxic factor Apr-Oct [d]' , fontsize=26)
ax=plt.xlabel('Year' , fontsize=26)
ax=plt.yticks(fontsize= 22)
ax=plt.xticks(rotation=45 , fontsize=22)
ax=plt.legend(bbox_to_anchor=(0.7, -0.2), fontsize=22)#)   
fig.savefig("GLUE_Timeseries_monthly_hypolimnetic_ave.png",  dpi=300, bbox_inches='tight')




#%%
np.mean(glue_df_monthly_hypolimnetic_ave_his['50%'])#6.077082662821386
np.mean(glue_df_monthly_hypolimnetic_ave_rcp26['50%'])#7.992767795524755
np.mean(glue_df_monthly_hypolimnetic_ave_rcp60['50%'])#8.585258963812871
np.mean(glue_df_monthly_hypolimnetic_ave_rcp85['50%'])#9.149586881905822

#%%anoxic_factor 30 yerars from each scenarios compare 



#anormaly 
# baseline [1976-2005]
glue_base_monthly_hypolimnetic_ave_his=glue_df_monthly_hypolimnetic_ave_his[1975 < glue_df_monthly_hypolimnetic_ave_his.index]['50%']
monthly_hypolimnetic_ave_ref=np.mean(glue_base_monthly_hypolimnetic_ave_his)
#6.389027950812897


#near future [2030-2059]

glue_near_future_monthly_hypolimnetic_ave_rcp26=glue_df_monthly_hypolimnetic_ave_rcp26[(2029 < glue_df_monthly_hypolimnetic_ave_rcp26.index) & (glue_df_monthly_hypolimnetic_ave_rcp26.index < 2060)]['50%']
np.mean(glue_near_future_monthly_hypolimnetic_ave_rcp26)
# 8.070525139552648
glue_near_future_monthly_hypolimnetic_ave_rcp60=glue_df_monthly_hypolimnetic_ave_rcp60[(2029 < glue_df_monthly_hypolimnetic_ave_rcp60.index) & (glue_df_monthly_hypolimnetic_ave_rcp60.index < 2060)]['50%']
np.mean(glue_near_future_monthly_hypolimnetic_ave_rcp60)
# 8.107889314159742
glue_near_future_monthly_hypolimnetic_ave_rcp85=glue_df_monthly_hypolimnetic_ave_rcp85[(2029 < glue_df_monthly_hypolimnetic_ave_rcp85.index) & (glue_df_monthly_hypolimnetic_ave_rcp85.index < 2060)]['50%']
np.mean(glue_near_future_monthly_hypolimnetic_ave_rcp85)
# 8.63044924136971

 
#Distant future [2070-2099]

glue_distant_future_monthly_hypolimnetic_ave_rcp26=glue_df_monthly_hypolimnetic_ave_rcp26[(2069 < glue_df_monthly_hypolimnetic_ave_rcp26.index) & (glue_df_monthly_hypolimnetic_ave_rcp26.index < 2100)]['50%']
np.mean(glue_distant_future_monthly_hypolimnetic_ave_rcp26)
#8.153608896799094
glue_distant_future_monthly_hypolimnetic_ave_rcp60=glue_df_monthly_hypolimnetic_ave_rcp60[(2069 < glue_df_monthly_hypolimnetic_ave_rcp60.index) & (glue_df_monthly_hypolimnetic_ave_rcp60.index< 2100)]['50%']
np.mean(glue_distant_future_monthly_hypolimnetic_ave_rcp60)
#9.787975473676404
glue_distant_future_monthly_hypolimnetic_ave_rcp85=glue_df_monthly_hypolimnetic_ave_rcp85[(2069 < glue_df_monthly_hypolimnetic_ave_rcp85.index) & (glue_df_monthly_hypolimnetic_ave_rcp85.index < 2100)]['50%']
np.mean(glue_distant_future_monthly_hypolimnetic_ave_rcp85)
#10.963418155408705
   


###====over 30 years in his and each RCPs 

# baseline [1976-2005]
autocorr_MK_org_modif_sens_slope_test(glue_base_monthly_hypolimnetic_ave_his)
(0.03791672471698212,
 'positively autocorrelated',
 'increasing',
 0.004067701513906119,
 0.04887120166082099,
 5.685266536515649)

#near future [2030-2059]


autocorr_MK_org_modif_sens_slope_test(glue_near_future_monthly_hypolimnetic_ave_rcp26)
(0.018345477426765625,
 'positively autocorrelated',
 'no trend',
 0.09353135296636017,
 0,
 0)

autocorr_MK_org_modif_sens_slope_test(glue_near_future_monthly_hypolimnetic_ave_rcp60)
(0.011313156566510486,
 'positively autocorrelated',
 'increasing',
 0.0007961960227531595,
 0.0470080311379157,
 7.4730648265627355)

autocorr_MK_org_modif_sens_slope_test(glue_near_future_monthly_hypolimnetic_ave_rcp85)

(0.01548644557384171,
 'positively autocorrelated',
 'increasing',
 0.0048191095611576085,
 0.05773266804253006,
 7.722484654253696)



#Distant future [2070-2099]


autocorr_MK_org_modif_sens_slope_test(glue_distant_future_monthly_hypolimnetic_ave_rcp26)
(0.015039983618369416,
 'positively autocorrelated',
 'no trend',
 0.1989481007752456,
 0,
 0)

autocorr_MK_org_modif_sens_slope_test(glue_distant_future_monthly_hypolimnetic_ave_rcp60)
(0.012394095955031883,
 'positively autocorrelated',
 'no trend',
 0.41182433473249125,
 0,
 0)


autocorr_MK_org_modif_sens_slope_test(glue_distant_future_monthly_hypolimnetic_ave_rcp85)
(0.014377923696788013,
 'positively autocorrelated',
 'increasing',
 0.0322801899241516,
 0.04781875151369361,
 10.409571253394757)






#%% 80 years from 2020 for monthly_hypolimnetic_ave


glue_80years_monthly_hypolimnetic_ave_rcp26=glue_df_monthly_hypolimnetic_ave_rcp26[2019 < glue_df_monthly_hypolimnetic_ave_rcp26.index]

glue_80years_monthly_hypolimnetic_ave_rcp60=glue_df_monthly_hypolimnetic_ave_rcp60[2019 < glue_df_monthly_hypolimnetic_ave_rcp60.index]

glue_80years_monthly_hypolimnetic_ave_rcp85=glue_df_monthly_hypolimnetic_ave_rcp85[2019 < glue_df_monthly_hypolimnetic_ave_rcp85.index]


#============= mean of first 10 yaers over 80 years 

#rcp2.6
np.mean(glue_80years_monthly_hypolimnetic_ave_rcp26[glue_80years_monthly_hypolimnetic_ave_rcp26.index<2030]['50%'])
7.781968220542252

#rcp6.0
np.mean(glue_80years_monthly_hypolimnetic_ave_rcp60[glue_80years_monthly_hypolimnetic_ave_rcp60.index<2030]['50%'])
7.835574478598173

#rcp8.5
np.mean(glue_80years_monthly_hypolimnetic_ave_rcp85[glue_80years_monthly_hypolimnetic_ave_rcp85.index<2030]['50%'])
7.7236229767454985

#============== mean of last 10 yaers over 80 years 

#rcp2.6
np.mean(glue_80years_monthly_hypolimnetic_ave_rcp26[glue_80years_monthly_hypolimnetic_ave_rcp26.index>2079]['50%'])
8.243966830565041

#rcp6.0
np.mean(glue_80years_monthly_hypolimnetic_ave_rcp60[glue_80years_monthly_hypolimnetic_ave_rcp60.index>2079]['50%'])
9.864621453257977

#rcp8.5
np.mean(glue_80years_monthly_hypolimnetic_ave_rcp85[glue_80years_monthly_hypolimnetic_ave_rcp85.index>2079]['50%'])
11.12826268210691

#=========== trendline # Over the 80 years


autocorr_MK_org_modif_sens_slope_test(glue_80years_monthly_hypolimnetic_ave_rcp26['50%'])
(0.02031492443906448,
 'positively autocorrelated',
 'no trend',
 0.11371844918011509,
 0,
 0)


autocorr_MK_org_modif_sens_slope_test(glue_80years_monthly_hypolimnetic_ave_rcp60['50%'])
(0.012504340139489645,
 'positively autocorrelated',
 'increasing',
 1.4566126083082054e-13,
 0.036058805989694846,
 7.282950340706922)


autocorr_MK_org_modif_sens_slope_test(glue_80years_monthly_hypolimnetic_ave_rcp85['50%'])
(0.015654880429522035,
 'positively autocorrelated',
 'increasing',
 0.0,
 0.05661191309631117,
 7.160412951529136)

#%%plotting monthly anoxic factor over 80 years 





os.chdir('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/')

import matplotlib.pyplot as plt

fig =plt.figure(figsize=(15, 10))
ax= plt.subplot(111)



ax=plt.fill_between(glue_80years_monthly_hypolimnetic_ave_rcp26.index.astype(float), glue_80years_monthly_hypolimnetic_ave_rcp26['5%'], glue_80years_monthly_hypolimnetic_ave_rcp26['95%'], color='darkgreen', alpha=0.3 ,  label= 'RCP2.6 90% CI')
ax=plt.plot(glue_80years_monthly_hypolimnetic_ave_rcp26.index.astype(float), glue_80years_monthly_hypolimnetic_ave_rcp26['50%'], 'darkgreen', label='RCP2.6 median', alpha=0.9, linewidth=3  )


ax=plt.fill_between(glue_80years_monthly_hypolimnetic_ave_rcp60.index.astype(float), glue_80years_monthly_hypolimnetic_ave_rcp60['5%'], glue_80years_monthly_hypolimnetic_ave_rcp60['95%'], color='yellow', alpha=0.2 ,  label= 'RCP6.0 90% CI')
ax=plt.plot(glue_80years_monthly_hypolimnetic_ave_rcp60.index.astype(float), glue_80years_monthly_hypolimnetic_ave_rcp60['50%'], 'yellow', label='RCP6.0 median', alpha=0.9, linewidth=3  )
trendline_rcp60=autocorr_MK_org_modif_sens_slope_test(glue_80years_monthly_hypolimnetic_ave_rcp60['50%'])
ax=plt.text(2020, 14, f'y = {trendline_rcp60[-2]:.3f}x + {trendline_rcp60[-1]:.3f}, p = {trendline_rcp60[-3]:.3f}', color='gold', fontsize= 20 )



ax=plt.fill_between(glue_80years_monthly_hypolimnetic_ave_rcp85.index.astype(float), glue_80years_monthly_hypolimnetic_ave_rcp85['5%'], glue_80years_monthly_hypolimnetic_ave_rcp85['95%'], color='r', alpha=0.2 ,  label= 'RCP8.5 90% CI')
ax=plt.plot(glue_80years_monthly_hypolimnetic_ave_rcp85.index.astype(float), glue_80years_monthly_hypolimnetic_ave_rcp85['50%'], 'r', label='RCP8.5 median', alpha=0.9, linewidth=3  )
trendline_rcp85=autocorr_MK_org_modif_sens_slope_test(glue_80years_monthly_hypolimnetic_ave_rcp85['50%'])
ax=plt.text(2020, 13, f'y = {trendline_rcp85[-2]:.3f}x + {trendline_rcp85[-1]:.3f},  p = {trendline_rcp85[-3]:.3f}', color='r', fontsize= 20 )




ax=plt.ylabel('anoxic factor in monthly [d/year]' , fontsize=26)
ax=plt.xlabel('Year' , fontsize=26)
ax=plt.yticks(fontsize= 22)
ax=plt.xticks(rotation=45 , fontsize=22)
ax=plt.legend(bbox_to_anchor=(0.7, -0.2), fontsize=22)#)   
fig.savefig("GLUE_Timeseries_80years_monthly_hypolimnetic_ave.png",  dpi=300, bbox_inches='tight')





#%%If there is a trend in entire 

# in whole his
autocorr_MK_org_modif_sens_slope_test(glue_df_monthly_hypolimnetic_ave_his['50%'])
(0.054103668580385816,
 'positively autocorrelated',
 'no trend',
 0.07068845447209426,
 0,
 0)

#in entire rcp2.6
autocorr_MK_org_modif_sens_slope_test(glue_df_monthly_hypolimnetic_ave_rcp26['50%'])
(0.02002132148516097,
 'positively autocorrelated',
 'increasing',
 0.0012506240636172006,
 0.009277291512717471,
 7.539997545595559)


#in entire rcp6.0
autocorr_MK_org_modif_sens_slope_test(glue_df_monthly_hypolimnetic_ave_rcp60['50%'])
(0.01438079345143515,
 'positively autocorrelated',
 'increasing',
 2.6645352591003757e-13,
 0.03278504999647535,
 6.993374854517668)

#in entire rcp8.5
autocorr_MK_org_modif_sens_slope_test(glue_df_monthly_hypolimnetic_ave_rcp85['50%'])
(0.016659625265317696,
 'positively autocorrelated',
 'increasing',
 0.0,
 0.05578367086692144,
 6.403552589696595)
#slope in entire RCP8.5> RCP6.0>RCP2.6 # his no trend 



 
#%%anoxic_factor_anormaly 
os.chdir('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/')

import matplotlib.pyplot as plt

fig =plt.figure(figsize=(15, 10))
ax= plt.subplot(111)


ax=plt.fill_between(glue_df_monthly_hypolimnetic_ave_his[(1960 < glue_df_monthly_hypolimnetic_ave_his.index)].index.astype(float),
                      glue_df_monthly_hypolimnetic_ave_his[(1960 < glue_df_monthly_hypolimnetic_ave_his.index)]['5%'] - monthly_hypolimnetic_ave_ref,
                      glue_df_monthly_hypolimnetic_ave_his[(1960 < glue_df_monthly_hypolimnetic_ave_his.index) ]['95%'] - monthly_hypolimnetic_ave_ref,
                      color='grey', alpha=0.2, label='His 90% CI')


ax=plt.plot(glue_df_monthly_hypolimnetic_ave_his[(1960 < glue_df_monthly_hypolimnetic_ave_his.index) ].index.astype(float),
            glue_df_monthly_hypolimnetic_ave_his[(1960 < glue_df_monthly_hypolimnetic_ave_his.index)]['50%'] - monthly_hypolimnetic_ave_ref,
            'k', label='His median', alpha=0.9, linewidth=3   )

ax=plt.fill_between(glue_df_monthly_hypolimnetic_ave_rcp26.index.astype(float), glue_df_monthly_hypolimnetic_ave_rcp26['5%']-monthly_hypolimnetic_ave_ref, glue_df_monthly_hypolimnetic_ave_rcp26['95%']-monthly_hypolimnetic_ave_ref, color='darkgreen', alpha=0.3 ,  label= 'RCP6.0 90% CI')
ax=plt.plot(glue_df_monthly_hypolimnetic_ave_rcp26.index.astype(float), glue_df_monthly_hypolimnetic_ave_rcp26['50%']-monthly_hypolimnetic_ave_ref, 'darkgreen', label='RCP6.0 median', alpha=0.9, linewidth=3  )
                      
                     
ax=plt.fill_between(glue_df_monthly_hypolimnetic_ave_rcp60.index.astype(float), glue_df_monthly_hypolimnetic_ave_rcp60['5%']-monthly_hypolimnetic_ave_ref, glue_df_monthly_hypolimnetic_ave_rcp60['95%']-monthly_hypolimnetic_ave_ref, color='yellow', alpha=0.2 ,  label= 'RCP6.0 90% CI')
ax=plt.plot(glue_df_monthly_hypolimnetic_ave_rcp60.index.astype(float), glue_df_monthly_hypolimnetic_ave_rcp60['50%']-monthly_hypolimnetic_ave_ref, 'yellow', label='RCP6.0 median', alpha=0.9, linewidth=3  )

ax=plt.fill_between(glue_df_monthly_hypolimnetic_ave_rcp85.index.astype(float), glue_df_monthly_hypolimnetic_ave_rcp85['5%']-monthly_hypolimnetic_ave_ref, glue_df_monthly_hypolimnetic_ave_rcp85['95%']-monthly_hypolimnetic_ave_ref, color='r', alpha=0.2 ,  label= 'RCP8.5 90% CI')
ax=plt.plot(glue_df_monthly_hypolimnetic_ave_rcp85.index.astype(float), glue_df_monthly_hypolimnetic_ave_rcp85['50%']-monthly_hypolimnetic_ave_ref, 'r', label='RCP8.5 median', alpha=0.9, linewidth=3  )

ax=plt.ylabel('Anormaly of anoxic factor in Apr-Oct [d year$^{-1}$]' , fontsize=26)
ax=plt.xlabel('Year' , fontsize=26)
ax=plt.yticks(fontsize= 22)
ax=plt.xticks(rotation=45 , fontsize=22)
ax=plt.legend(bbox_to_anchor=(0.7, -0.2), fontsize=22)  
fig.savefig("GLUE_Timeseries_monthly_hypolimnetic_ave_anormaly.png",  dpi=300, bbox_inches='tight')













#%%===========summer average of anoxic afctor 


#%%########summer anoxic factor 

#%%ploting summer anoxic factor 

os.chdir('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/')

import matplotlib.pyplot as plt

fig =plt.figure(figsize=(15, 10))
ax= plt.subplot(111)


ax=plt.fill_between(glue_df_summer_hypolimnetic_ave_his.index.astype(float), glue_df_summer_hypolimnetic_ave_his['5%'], glue_df_summer_hypolimnetic_ave_his['95%'], color='grey', alpha=0.2 ,  label= 'His 90% CI')
ax=plt.plot(glue_df_summer_hypolimnetic_ave_his.index.astype(float), glue_df_summer_hypolimnetic_ave_his['50%'].astype(float), 'k', label='His median', alpha=0.9, linewidth=3  )



ax=plt.fill_between(glue_df_summer_hypolimnetic_ave_rcp26.index.astype(float), glue_df_summer_hypolimnetic_ave_rcp26['5%'], glue_df_summer_hypolimnetic_ave_rcp26['95%'], color='darkgreen', alpha=0.3 ,  label= 'RCP2.6 90% CI')
ax=plt.plot(glue_df_summer_hypolimnetic_ave_rcp26.index.astype(float), glue_df_summer_hypolimnetic_ave_rcp26['50%'], 'darkgreen', label='RCP2.6 median', alpha=0.9, linewidth=3  )


ax=plt.fill_between(glue_df_summer_hypolimnetic_ave_rcp60.index.astype(float), glue_df_summer_hypolimnetic_ave_rcp60['5%'], glue_df_summer_hypolimnetic_ave_rcp60['95%'], color='yellow', alpha=0.2 ,  label= 'RCP6.0 90% CI')
ax=plt.plot(glue_df_summer_hypolimnetic_ave_rcp60.index.astype(float), glue_df_summer_hypolimnetic_ave_rcp60['50%'], 'yellow', label='RCP6.0 median', alpha=0.9, linewidth=3  )

ax=plt.fill_between(glue_df_summer_hypolimnetic_ave_rcp85.index.astype(float), glue_df_summer_hypolimnetic_ave_rcp85['5%'], glue_df_summer_hypolimnetic_ave_rcp85['95%'], color='r', alpha=0.2 ,  label= 'RCP8.5 90% CI')
ax=plt.plot(glue_df_summer_hypolimnetic_ave_rcp85.index.astype(float), glue_df_summer_hypolimnetic_ave_rcp85['50%'], 'r', label='RCP8.5 median', alpha=0.9, linewidth=3  )

ax=plt.ylabel('anoxic factor in summer [d/year]' , fontsize=26)
ax=plt.xlabel('Year' , fontsize=26)
ax=plt.yticks(fontsize= 22)
ax=plt.xticks(rotation=45 , fontsize=22)
ax=plt.legend(bbox_to_anchor=(0.7, -0.2), fontsize=22)#)   
fig.savefig("GLUE_Timeseries_summer_hypolimnetic_ave.png",  dpi=300, bbox_inches='tight')




#%%
np.mean(glue_df_summer_hypolimnetic_ave_his['50%'])#5.7419538116211175
np.mean(glue_df_summer_hypolimnetic_ave_rcp26['50%'])#7.164633836912792
np.mean(glue_df_summer_hypolimnetic_ave_rcp60['50%'])#7.660016638342764
np.mean(glue_df_summer_hypolimnetic_ave_rcp85['50%'])#7.798265277646058

#%%anoxic_factor 30 yerars from each scenarios compare 



#anormaly 
# baseline [1976-2005]
glue_base_summer_hypolimnetic_ave_his=glue_df_summer_hypolimnetic_ave_his[1975 < glue_df_summer_hypolimnetic_ave_his.index]['50%']
summer_hypolimnetic_ave_ref=np.mean(glue_base_summer_hypolimnetic_ave_his)
#5.830216997377137


#near future [2030-2059]

glue_near_future_summer_hypolimnetic_ave_rcp26=glue_df_summer_hypolimnetic_ave_rcp26[(2029 < glue_df_summer_hypolimnetic_ave_rcp26.index) & (glue_df_summer_hypolimnetic_ave_rcp26.index < 2060)]['50%']
np.mean(glue_near_future_summer_hypolimnetic_ave_rcp26)
# 7.189791199644448
glue_near_future_summer_hypolimnetic_ave_rcp60=glue_df_summer_hypolimnetic_ave_rcp60[(2029 < glue_df_summer_hypolimnetic_ave_rcp60.index) & (glue_df_summer_hypolimnetic_ave_rcp60.index < 2060)]['50%']
np.mean(glue_near_future_summer_hypolimnetic_ave_rcp60)
# 7.408290028941934
glue_near_future_summer_hypolimnetic_ave_rcp85=glue_df_summer_hypolimnetic_ave_rcp85[(2029 < glue_df_summer_hypolimnetic_ave_rcp85.index) & (glue_df_summer_hypolimnetic_ave_rcp85.index < 2060)]['50%']
np.mean(glue_near_future_summer_hypolimnetic_ave_rcp85)
# 7.577321792421727

 
#Distant future [2070-2099]

glue_distant_future_summer_hypolimnetic_ave_rcp26=glue_df_summer_hypolimnetic_ave_rcp26[(2069 < glue_df_summer_hypolimnetic_ave_rcp26.index) & (glue_df_summer_hypolimnetic_ave_rcp26.index < 2100)]['50%']
np.mean(glue_distant_future_summer_hypolimnetic_ave_rcp26)
#7.182315856408658
glue_distant_future_summer_hypolimnetic_ave_rcp60=glue_df_summer_hypolimnetic_ave_rcp60[(2069 < glue_df_summer_hypolimnetic_ave_rcp60.index) & (glue_df_summer_hypolimnetic_ave_rcp60.index< 2100)]['50%']
np.mean(glue_distant_future_summer_hypolimnetic_ave_rcp60)
#8.404224632950019
glue_distant_future_summer_hypolimnetic_ave_rcp85=glue_df_summer_hypolimnetic_ave_rcp85[(2069 < glue_df_summer_hypolimnetic_ave_rcp85.index) & (glue_df_summer_hypolimnetic_ave_rcp85.index < 2100)]['50%']
np.mean(glue_distant_future_summer_hypolimnetic_ave_rcp85)
#8.844476856722357
   


###====over 30 years in his and each RCPs 

# baseline [1976-2005]
autocorr_MK_org_modif_sens_slope_test(glue_base_summer_hypolimnetic_ave_his)
(0.03384344872449237,
 'positively autocorrelated',
 'no trend',
 0.2389927879015219,
 0,
 0)


#near future [2030-2059]


autocorr_MK_org_modif_sens_slope_test(glue_near_future_summer_hypolimnetic_ave_rcp26)
(0.017426799559486894,
 'positively autocorrelated',
 'no trend',
 0.2686642304239091,
 0,
 0)
autocorr_MK_org_modif_sens_slope_test(glue_near_future_summer_hypolimnetic_ave_rcp60)
(0.011027838419972513,
 'positively autocorrelated',
 'no trend',
 0.08039114754218035,
 0,
 0)

autocorr_MK_org_modif_sens_slope_test(glue_near_future_summer_hypolimnetic_ave_rcp85)

(0.010531400508757774,
 'positively autocorrelated',
 'increasing',
 0.0053825476031263975,
 0.0337942438328447,
 7.0319428173255965)


#Distant future [2070-2099]

#rcp26
autocorr_MK_org_modif_sens_slope_test(glue_distant_future_summer_hypolimnetic_ave_rcp26)
(0.007455597611559313,
 'positively autocorrelated',
 'increasing',
 0.011479484705922305,
 0.03254964585051723,
 6.704083850293537)
#rcp60
autocorr_MK_org_modif_sens_slope_test(glue_distant_future_summer_hypolimnetic_ave_rcp60)
(0.005218209926031563,
 'positively autocorrelated',
 'no trend',
 0.7752944295177846,
 0,
 0)
#rcp85
autocorr_MK_org_modif_sens_slope_test(glue_distant_future_summer_hypolimnetic_ave_rcp85)
(0.011260089055346817,
 'positively autocorrelated',
 'no trend',
 0.2844114676220473,
 0,
 0)





#%% 80 years from 2020 for summer_hypolimnetic_ave


glue_80years_summer_hypolimnetic_ave_rcp26=glue_df_summer_hypolimnetic_ave_rcp26[2019 < glue_df_summer_hypolimnetic_ave_rcp26.index]

glue_80years_summer_hypolimnetic_ave_rcp60=glue_df_summer_hypolimnetic_ave_rcp60[2019 < glue_df_summer_hypolimnetic_ave_rcp60.index]

glue_80years_summer_hypolimnetic_ave_rcp85=glue_df_summer_hypolimnetic_ave_rcp85[2019 < glue_df_summer_hypolimnetic_ave_rcp85.index]


#============= mean of first 10 yaers over 80 years 

#rcp2.6
np.mean(glue_80years_summer_hypolimnetic_ave_rcp26[glue_80years_summer_hypolimnetic_ave_rcp26.index<2030]['50%'])
7.236131611808827

#rcp6.0
np.mean(glue_80years_summer_hypolimnetic_ave_rcp60[glue_80years_summer_hypolimnetic_ave_rcp60.index<2030]['50%'])
7.0480838080216754

#rcp8.5
np.mean(glue_80years_summer_hypolimnetic_ave_rcp85[glue_80years_summer_hypolimnetic_ave_rcp85.index<2030]['50%'])
6.92973720099211

#============== mean of last 10 yaers over 80 years 

#rcp2.6
np.mean(glue_80years_summer_hypolimnetic_ave_rcp26[glue_80years_summer_hypolimnetic_ave_rcp26.index>2079]['50%'])
7.284732847455828

#rcp6.0
np.mean(glue_80years_summer_hypolimnetic_ave_rcp60[glue_80years_summer_hypolimnetic_ave_rcp60.index>2079]['50%'])
8.376808940760498

#rcp8.5
np.mean(glue_80years_summer_hypolimnetic_ave_rcp85[glue_80years_summer_hypolimnetic_ave_rcp85.index>2079]['50%'])
8.902897713112784

#=========== trendline # Over the 80 years


autocorr_MK_org_modif_sens_slope_test(glue_80years_summer_hypolimnetic_ave_rcp26['50%'])
(0.012431261551918694,
 'positively autocorrelated',
 'no trend',
 0.4722909038902814,
 0,
 0)

autocorr_MK_org_modif_sens_slope_test(glue_80years_summer_hypolimnetic_ave_rcp60['50%'])
(0.009054412557226742,
 'positively autocorrelated',
 'increasing',
 0.0,
 0.021466406502838986,
 6.936654760438897)


autocorr_MK_org_modif_sens_slope_test(glue_80years_summer_hypolimnetic_ave_rcp85['50%'])
(0.012767144112602902,
 'positively autocorrelated',
 'increasing',
 0.0,
 0.031086674796400225,
 6.7697952941890875)



#%%plotting summer anoxic factor over 80 years 





os.chdir('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/')

import matplotlib.pyplot as plt

fig =plt.figure(figsize=(15, 10))
ax= plt.subplot(111)



ax=plt.fill_between(glue_80years_summer_hypolimnetic_ave_rcp26.index.astype(float), glue_80years_summer_hypolimnetic_ave_rcp26['5%'], glue_80years_summer_hypolimnetic_ave_rcp26['95%'], color='darkgreen', alpha=0.3 ,  label= 'RCP2.6 90% CI')
ax=plt.plot(glue_80years_summer_hypolimnetic_ave_rcp26.index.astype(float), glue_80years_summer_hypolimnetic_ave_rcp26['50%'], 'darkgreen', label='RCP2.6 median', alpha=0.9, linewidth=3  )


ax=plt.fill_between(glue_80years_summer_hypolimnetic_ave_rcp60.index.astype(float), glue_80years_summer_hypolimnetic_ave_rcp60['5%'], glue_80years_summer_hypolimnetic_ave_rcp60['95%'], color='yellow', alpha=0.2 ,  label= 'RCP6.0 90% CI')
ax=plt.plot(glue_80years_summer_hypolimnetic_ave_rcp60.index.astype(float), glue_80years_summer_hypolimnetic_ave_rcp60['50%'], 'yellow', label='RCP6.0 median', alpha=0.9, linewidth=3  )
trendline_rcp60=autocorr_MK_org_modif_sens_slope_test(glue_80years_summer_hypolimnetic_ave_rcp60['50%'])
ax=plt.text(2020, 12, f'y = {trendline_rcp60[-2]:.3f}x + {trendline_rcp60[-1]:.3f}, p = {trendline_rcp60[-3]:.3f}', color='gold', fontsize= 20 )



ax=plt.fill_between(glue_80years_summer_hypolimnetic_ave_rcp85.index.astype(float), glue_80years_summer_hypolimnetic_ave_rcp85['5%'], glue_80years_summer_hypolimnetic_ave_rcp85['95%'], color='r', alpha=0.2 ,  label= 'RCP8.5 90% CI')
ax=plt.plot(glue_80years_summer_hypolimnetic_ave_rcp85.index.astype(float), glue_80years_summer_hypolimnetic_ave_rcp85['50%'], 'r', label='RCP8.5 median', alpha=0.9, linewidth=3  )
trendline_rcp85=autocorr_MK_org_modif_sens_slope_test(glue_80years_summer_hypolimnetic_ave_rcp85['50%'])
ax=plt.text(2020, 11, f'y = {trendline_rcp85[-2]:.3f}x + {trendline_rcp85[-1]:.3f},  p = {trendline_rcp85[-3]:.3f}', color='r', fontsize= 20 )




ax=plt.ylabel('Anoxic factor in summer [d/year]' , fontsize=26)
ax=plt.xlabel('Year' , fontsize=26)
ax=plt.yticks(fontsize= 22)
ax=plt.xticks(rotation=45 , fontsize=22)
ax=plt.legend(bbox_to_anchor=(0.7, -0.2), fontsize=22)#)   
fig.savefig("GLUE_Timeseries_80years_summer_hypolimnetic_ave.png",  dpi=300, bbox_inches='tight')





#%%If there is a trend in entire scenario

# in whole his
autocorr_MK_org_modif_sens_slope_test(glue_df_summer_hypolimnetic_ave_his['50%'])
(0.050102399473259764,
 'positively autocorrelated',
 'no trend',
 0.15346389188435516,
 0,
 0)

#in intire rcp2.6
autocorr_MK_org_modif_sens_slope_test(glue_df_summer_hypolimnetic_ave_rcp26['50%'])
(0.011480536925277993,
 'positively autocorrelated',
 'increasing',
 0.030392451085676786,
 0.0039129273367328335,
 6.963469344761228)

#in entire rcp6.0
autocorr_MK_org_modif_sens_slope_test(glue_df_summer_hypolimnetic_ave_rcp60['50%'])
(0.010198727721089741,
 'positively autocorrelated',
 'increasing',
 0.0,
 0.02131982928372496,
 6.689481345978918)

#in entire rcp8.5
autocorr_MK_org_modif_sens_slope_test(glue_df_summer_hypolimnetic_ave_rcp85['50%'])
(0.014688565156364046,
 'positively autocorrelated',
 'increasing',
 0.0,
 0.031748328950495945,
 6.343632396381782)

#slope in entire RCP8.5> RCP6.0>RCP2.6 # his no trend 



 
#%%anoxic_factor_anormaly 
os.chdir('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/')

import matplotlib.pyplot as plt

fig =plt.figure(figsize=(15, 10))
ax= plt.subplot(111)


ax=plt.fill_between(glue_df_summer_hypolimnetic_ave_his[(1960 < glue_df_summer_hypolimnetic_ave_his.index)].index.astype(float),
                      glue_df_summer_hypolimnetic_ave_his[(1960 < glue_df_summer_hypolimnetic_ave_his.index)]['5%'] - summer_hypolimnetic_ave_ref,
                      glue_df_summer_hypolimnetic_ave_his[(1960 < glue_df_summer_hypolimnetic_ave_his.index) ]['95%'] - summer_hypolimnetic_ave_ref,
                      color='grey', alpha=0.2, label='His 90% CI')


ax=plt.plot(glue_df_summer_hypolimnetic_ave_his[(1960 < glue_df_summer_hypolimnetic_ave_his.index) ].index.astype(float),
            glue_df_summer_hypolimnetic_ave_his[(1960 < glue_df_summer_hypolimnetic_ave_his.index)]['50%'] - summer_hypolimnetic_ave_ref,
            'k', label='His median', alpha=0.9, linewidth=3   )

ax=plt.fill_between(glue_df_summer_hypolimnetic_ave_rcp26.index.astype(float), glue_df_summer_hypolimnetic_ave_rcp26['5%']-summer_hypolimnetic_ave_ref, glue_df_summer_hypolimnetic_ave_rcp26['95%']-summer_hypolimnetic_ave_ref, color='darkgreen', alpha=0.3 ,  label= 'RCP6.0 90% CI')
ax=plt.plot(glue_df_summer_hypolimnetic_ave_rcp26.index.astype(float), glue_df_summer_hypolimnetic_ave_rcp26['50%']-summer_hypolimnetic_ave_ref, 'darkgreen', label='RCP6.0 median', alpha=0.9, linewidth=3  )
                      
                     
ax=plt.fill_between(glue_df_summer_hypolimnetic_ave_rcp60.index.astype(float), glue_df_summer_hypolimnetic_ave_rcp60['5%']-summer_hypolimnetic_ave_ref, glue_df_summer_hypolimnetic_ave_rcp60['95%']-summer_hypolimnetic_ave_ref, color='yellow', alpha=0.2 ,  label= 'RCP6.0 90% CI')
ax=plt.plot(glue_df_summer_hypolimnetic_ave_rcp60.index.astype(float), glue_df_summer_hypolimnetic_ave_rcp60['50%']-summer_hypolimnetic_ave_ref, 'yellow', label='RCP6.0 median', alpha=0.9, linewidth=3  )

ax=plt.fill_between(glue_df_summer_hypolimnetic_ave_rcp85.index.astype(float), glue_df_summer_hypolimnetic_ave_rcp85['5%']-summer_hypolimnetic_ave_ref, glue_df_summer_hypolimnetic_ave_rcp85['95%']-summer_hypolimnetic_ave_ref, color='r', alpha=0.2 ,  label= 'RCP8.5 90% CI')
ax=plt.plot(glue_df_summer_hypolimnetic_ave_rcp85.index.astype(float), glue_df_summer_hypolimnetic_ave_rcp85['50%']-summer_hypolimnetic_ave_ref, 'r', label='RCP8.5 median', alpha=0.9, linewidth=3  )

ax=plt.ylabel('Anormaly of anoxic factor in summer [d year$^{-1}$]' , fontsize=26)
ax=plt.xlabel('Year' , fontsize=26)
ax=plt.yticks(fontsize= 22)
ax=plt.xticks(rotation=45 , fontsize=22)
ax=plt.legend(bbox_to_anchor=(0.7, -0.2), fontsize=22)  
fig.savefig("GLUE_Timeseries_summer_hypolimnetic_ave_anormaly.png",  dpi=300, bbox_inches='tight')










#%%
####################################old one
############################################
############################################

#%% Annual anoxic factor_gfdl_his
# Specify the directory where the CSV files are located


#########original test with variable theta:
#########directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/his'


######## fixed theta both in calib and simulation 
#######directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/his_fixedtheta'




####### test with fixed theta in calibration but variable for GOTM simulation 
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/his_calibinfixedtheta_simuvartheta'




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
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = annual_hypolimnetic_ave(C, Vr, time_series )

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_hypolimnetic_ave_gfdl_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_hypolimnetic_ave'])
        
                


#%%monthly_hypolimnetic_ave_gfdl_his

# Specify the directory where the CSV files are located
#########original test with variable theta:
#########directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/his'


######## fixed theta both in calib and simulation 
#######directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/his_fixedtheta'




####### test with fixed theta in calibration but variable for GOTM simulation 
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/his_calibinfixedtheta_simuvartheta'


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
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = monthly_hypolimnetic_ave(C, Vr, time_series )

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_hypolimnetic_ave_gfdl_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                
#%% Annual anoxic factor_gfdl_rcp26
# Specify the directory where the CSV files are located
#########original test with variable theta:
#########directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp26'


######## fixed theta both in calib and simulation 
######## directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp26_fixedtheta'


###### test with fixed theta in calibration a temp ave hypo in gfdl rcp26 for years 2020 and 2021
#######directory='C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp26_fixedthetaincalib_simurcp26temp20202021'



####### test with fixed theta in calibration but variable for GOTM simulation 
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp26_calibinfixedtheta_simuvartheta'


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
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = annual_hypolimnetic_ave(C, Vr, time_series )

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_hypolimnetic_ave_gfdl_rcp26_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_hypolimnetic_ave'])
        
                


#%%monthly_hypolimnetic_ave_gfdl_rcp26

# Specify the directory where the CSV files are located
#########original test with variable theta:
#########directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp26'


######## fixed theta both in calib and simulation 
######## directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp26_fixedtheta'


###### test with fixed theta in calibration a temp ave hypo in gfdl rcp26 for years 2020 and 2021
#######directory='C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp26_fixedthetaincalib_simurcp26temp20202021'



####### test with fixed theta in calibration but variable for GOTM simulation 
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp26_calibinfixedtheta_simuvartheta'



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
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = monthly_hypolimnetic_ave(C, Vr, time_series )

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_hypolimnetic_ave_gfdl_rcp26_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                

#%% Annual anoxic factor_gfdl_rcp60
# Specify the directory where the CSV files are located
#########original test with variable theta:
#########directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp60'


######## fixed theta both in calib and simulation 
######## directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp60_fixedtheta'


###### test with fixed theta in calibration a temp ave hypo in gfdl rcp60 for years 2020 and 2021
#######directory='C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp60_fixedthetaincalib_simurcp60temp20202021'



####### test with fixed theta in calibration but variable for GOTM simulation 
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp60_calibinfixedtheta_simuvartheta'

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
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = annual_hypolimnetic_ave(C, Vr, time_series )

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_hypolimnetic_ave_gfdl_rcp60_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_hypolimnetic_ave'])
        
                


#%%monthly_hypolimnetic_ave_gfdl_rcp60

# Specify the directory where the CSV files are located
#########original test with variable theta:
#########directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp60'


######## fixed theta both in calib and simulation 
######## directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp60_fixedtheta'


###### test with fixed theta in calibration a temp ave hypo in gfdl rcp60 for years 2020 and 2021
#######directory='C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp60_fixedthetaincalib_simurcp60temp20202021'



####### test with fixed theta in calibration but variable for GOTM simulation 
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp60_calibinfixedtheta_simuvartheta'

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
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = monthly_hypolimnetic_ave(C, Vr, time_series )

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_hypolimnetic_ave_gfdl_rcp60_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                



#%% Annual anoxic factor_gfdl_rcp85
# Specify the directory where the CSV files are located
#########original test with variable theta:
#########directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp85'


######## fixed theta both in calib and simulation 
######## directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp85_fixedtheta'


###### test with fixed theta in calibration a temp ave hypo in gfdl rcp85 for years 2020 and 2021
#######directory='C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp85_fixedthetaincalib_simurcp85temp20202021'



####### test with fixed theta in calibration but variable for GOTM simulation 
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp85_calibinfixedtheta_simuvartheta'



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
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = annual_hypolimnetic_ave(C, Vr, time_series )

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_hypolimnetic_ave_gfdl_rcp85_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_hypolimnetic_ave'])
        
                


#%%monthly_hypolimnetic_ave_gfdl_rcp85

# Specify the directory where the CSV files are located
#########original test with variable theta:
#########directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp85'


######## fixed theta both in calib and simulation 
######## directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp85_fixedtheta'


###### test with fixed theta in calibration a temp ave hypo in gfdl rcp85 for years 2020 and 2021
#######directory='C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp85_fixedthetaincalib_simurcp85temp20202021'



####### test with fixed theta in calibration but variable for GOTM simulation 
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp85_calibinfixedtheta_simuvartheta'



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
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = monthly_hypolimnetic_ave(C, Vr, time_series )

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_hypolimnetic_ave_gfdl_rcp85_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                


#%% Annual anoxic factor_hadgem_his
# Specify the directory where the CSV files are located

#########original test with variable theta:
#########directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/his'


######## fixed theta both in calib and simulation 
#######directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/his_fixedtheta'




####### test with fixed theta in calibration but variable for GOTM simulation 
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/his_calibinfixedtheta_simuvartheta'


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
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = annual_hypolimnetic_ave(C, Vr, time_series )

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_hypolimnetic_ave_hadgem_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_hypolimnetic_ave'])
        
                


#%%monthly_hypolimnetic_ave_hadgem_his

# Specify the directory where the CSV files are located
#########original test with variable theta:
#########directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/his'


######## fixed theta both in calib and simulation 
#######directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/his_fixedtheta'




####### test with fixed theta in calibration but variable for GOTM simulation 
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/his_calibinfixedtheta_simuvartheta'

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
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = monthly_hypolimnetic_ave(C, Vr, time_series )

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_hypolimnetic_ave_hadgem_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                
#%% Annual anoxic factor_hadgem_rcp26
# Specify the directory where the CSV files are located

#########original test with variable theta:
#########directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp26'


######## fixed theta both in calib and simulation 
######## directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp26_fixedtheta'


###### test with fixed theta in calibration a temp ave hypo in hadgem rcp26 for years 2020 and 2021
#######directory='C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp26_fixedthetaincalib_simurcp26temp20202021'



####### test with fixed theta in calibration but variable for GOTM simulation 
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp26_calibinfixedtheta_simuvartheta'




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
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = annual_hypolimnetic_ave(C, Vr, time_series )

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_hypolimnetic_ave_hadgem_rcp26_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_hypolimnetic_ave'])
        
                


#%%monthly_hypolimnetic_ave_hadgem_rcp26

# Specify the directory where the CSV files are located
#########original test with variable theta:
#########directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp26'


######## fixed theta both in calib and simulation 
######## directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp26_fixedtheta'


###### test with fixed theta in calibration a temp ave hypo in hadgem rcp26 for years 2020 and 2021
#######directory='C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp26_fixedthetaincalib_simurcp26temp20202021'



####### test with fixed theta in calibration but variable for GOTM simulation 
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp26_calibinfixedtheta_simuvartheta'


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
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = monthly_hypolimnetic_ave(C, Vr, time_series )

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_hypolimnetic_ave_hadgem_rcp26_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                

#%% Annual anoxic factor_hadgem_rcp60
# Specify the directory where the CSV files are located
#########original test with variable theta:
#########directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp60'


######## fixed theta both in calib and simulation 
######## directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp60_fixedtheta'


###### test with fixed theta in calibration a temp ave hypo in hadgem rcp60 for years 2020 and 2021
#######directory='C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp60_fixedthetaincalib_simurcp60temp20202021'



####### test with fixed theta in calibration but variable for GOTM simulation 
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp60_calibinfixedtheta_simuvartheta'




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
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = annual_hypolimnetic_ave(C, Vr, time_series )

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_hypolimnetic_ave_hadgem_rcp60_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_hypolimnetic_ave'])
        
                


#%%monthly_hypolimnetic_ave_hadgem_rcp60

# Specify the directory where the CSV files are located

#########original test with variable theta:
#########directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp60'


######## fixed theta both in calib and simulation 
######## directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp60_fixedtheta'


###### test with fixed theta in calibration a temp ave hypo in hadgem rcp60 for years 2020 and 2021
#######directory='C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp60_fixedthetaincalib_simurcp60temp20202021'



####### test with fixed theta in calibration but variable for GOTM simulation 
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp60_calibinfixedtheta_simuvartheta'



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
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = monthly_hypolimnetic_ave(C, Vr, time_series )

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_hypolimnetic_ave_hadgem_rcp60_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                



#%% Annual anoxic factor_hadgem_rcp85
# Specify the directory where the CSV files are located


#########original test with variable theta:
#########directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp85'


######## fixed theta both in calib and simulation 
######## directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp85_fixedtheta'


###### test with fixed theta in calibration a temp ave hypo in hadgem rcp85 for years 2020 and 2021
#######directory='C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp85_fixedthetaincalib_simurcp85temp20202021'



####### test with fixed theta in calibration but variable for GOTM simulation 
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp85_calibinfixedtheta_simuvartheta'




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
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = annual_hypolimnetic_ave(C, Vr, time_series )

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_hypolimnetic_ave_hadgem_rcp85_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_hypolimnetic_ave'])
        
                


#%%monthly_hypolimnetic_ave_hadgem_rcp85

# Specify the directory where the CSV files are located

#########original test with variable theta:
#########directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp85'


######## fixed theta both in calib and simulation 
######## directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp85_fixedtheta'


###### test with fixed theta in calibration a temp ave hypo in hadgem rcp85 for years 2020 and 2021
#######directory='C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp85_fixedthetaincalib_simurcp85temp20202021'



####### test with fixed theta in calibration but variable for GOTM simulation 
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp85_calibinfixedtheta_simuvartheta'




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
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = monthly_hypolimnetic_ave(C, Vr, time_series )

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_hypolimnetic_ave_hadgem_rcp85_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                


#%% Annual anoxic factor_ipsl_his
# Specify the directory where the CSV files are located
#########original test with variable theta:
#########directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/his'


######## fixed theta both in calib and simulation 
#######directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/his_fixedtheta'




####### test with fixed theta in calibration but variable for GOTM simulation 
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/his_calibinfixedtheta_simuvartheta'


# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("DO_prof_ipsl_his_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = annual_hypolimnetic_ave(C, Vr, time_series )

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_hypolimnetic_ave_ipsl_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_hypolimnetic_ave'])
        
                


#%%monthly_hypolimnetic_ave_ipsl_his

# Specify the directory where the CSV files are located
#########original test with variable theta:
#########directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/his'


######## fixed theta both in calib and simulation 
#######directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/his_fixedtheta'




####### test with fixed theta in calibration but variable for GOTM simulation 
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/his_calibinfixedtheta_simuvartheta'


# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("DO_prof_ipsl_his_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = monthly_hypolimnetic_ave(C, Vr, time_series )

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_hypolimnetic_ave_ipsl_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                
#%% Annual anoxic factor_ipsl_rcp26
# Specify the directory where the CSV files are located

#########original test with variable theta:
#########directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp26'


######## fixed theta both in calib and simulation 
######## directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp26_fixedtheta'


###### test with fixed theta in calibration a temp ave hypo in ipcl rcp26 for years 2020 and 2021
#######directory='C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp26_fixedthetaincalib_simurcp26temp20202021'



####### test with fixed theta in calibration but variable for GOTM simulation 
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp26_calibinfixedtheta_simuvartheta'



# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("DO_prof_ipsl_rcp26_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = annual_hypolimnetic_ave(C, Vr, time_series )

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_hypolimnetic_ave_ipsl_rcp26_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_hypolimnetic_ave'])
        
                


#%%monthly_hypolimnetic_ave_ipsl_rcp26

# Specify the directory where the CSV files are located

#########original test with variable theta:
#########directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp26'


######## fixed theta both in calib and simulation 
######## directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp26_fixedtheta'


###### test with fixed theta in calibration a temp ave hypo in ipcl rcp26 for years 2020 and 2021
#######directory='C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp26_fixedthetaincalib_simurcp26temp20202021'



####### test with fixed theta in calibration but variable for GOTM simulation 
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp26_calibinfixedtheta_simuvartheta'


# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("DO_prof_ipsl_rcp26_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = monthly_hypolimnetic_ave(C, Vr, time_series )

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_hypolimnetic_ave_ipsl_rcp26_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                

#%% Annual anoxic factor_ipsl_rcp60
# Specify the directory where the CSV files are located

#########original test with variable theta:
#########directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp60'


######## fixed theta both in calib and simulation 
######## directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp60_fixedtheta'


###### test with fixed theta in calibration a temp ave hypo in ipcl rcp60 for years 2020 and 2021
#######directory='C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp60_fixedthetaincalib_simurcp60temp20202021'



####### test with fixed theta in calibration but variable for GOTM simulation 
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp60_calibinfixedtheta_simuvartheta'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("DO_prof_ipsl_rcp60_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = annual_hypolimnetic_ave(C, Vr, time_series )

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_hypolimnetic_ave_ipsl_rcp60_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_hypolimnetic_ave'])
        
                


#%%monthly_hypolimnetic_ave_ipsl_rcp60

# Specify the directory where the CSV files are located
#########original test with variable theta:
#########directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp60'


######## fixed theta both in calib and simulation 
######## directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp60_fixedtheta'


###### test with fixed theta in calibration a temp ave hypo in ipcl rcp60 for years 2020 and 2021
#######directory='C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp60_fixedthetaincalib_simurcp60temp20202021'



####### test with fixed theta in calibration but variable for GOTM simulation 
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp60_calibinfixedtheta_simuvartheta'


# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("DO_prof_ipsl_rcp60_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = monthly_hypolimnetic_ave(C, Vr, time_series )

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_hypolimnetic_ave_ipsl_rcp60_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                



#%% Annual anoxic factor_ipsl_rcp85
# Specify the directory where the CSV files are located

#########original test with variable theta:
#########directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp85'


######## fixed theta both in calib and simulation 
######## directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp85_fixedtheta'


###### test with fixed theta in calibration a temp ave hypo in ipcl rcp85 for years 2020 and 2021
#######directory='C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp85_fixedthetaincalib_simurcp85temp20202021'



####### test with fixed theta in calibration but variable for GOTM simulation 
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp85_calibinfixedtheta_simuvartheta'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("DO_prof_ipsl_rcp85_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = annual_hypolimnetic_ave(C, Vr, time_series )

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_hypolimnetic_ave_ipsl_rcp85_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_hypolimnetic_ave'])
        
                


#%%monthly_hypolimnetic_ave_ipsl_rcp85

# Specify the directory where the CSV files are located

#########original test with variable theta:
#########directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp85'


######## fixed theta both in calib and simulation 
######## directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp85_fixedtheta'


###### test with fixed theta in calibration a temp ave hypo in ipcl rcp85 for years 2020 and 2021
#######directory='C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp85_fixedthetaincalib_simurcp85temp20202021'



####### test with fixed theta in calibration but variable for GOTM simulation 
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp85_calibinfixedtheta_simuvartheta'


# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("DO_prof_ipsl_rcp85_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = monthly_hypolimnetic_ave(C, Vr, time_series )

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_hypolimnetic_ave_ipsl_rcp85_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                

#%% Annual anoxic factor_miroc_his
# Specify the directory where the CSV files are located

#########original test with variable theta:
#########directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/his'


######## fixed theta both in calib and simulation 
#######directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/his_fixedtheta'




####### test with fixed theta in calibration but variable for GOTM simulation 
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/his_calibinfixedtheta_simuvartheta'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("DO_prof_miroc_his_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = annual_hypolimnetic_ave(C, Vr, time_series )

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_hypolimnetic_ave_miroc_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_hypolimnetic_ave'])
        
                


#%%monthly_hypolimnetic_ave_miroc_his

# Specify the directory where the CSV files are located

#########original test with variable theta:
#########directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/his'


######## fixed theta both in calib and simulation 
#######directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/his_fixedtheta'



####### test with fixed theta in calibration but variable for GOTM simulation 
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/his_calibinfixedtheta_simuvartheta'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("DO_prof_miroc_his_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = monthly_hypolimnetic_ave(C, Vr, time_series )

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_hypolimnetic_ave_miroc_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                
#%% Annual anoxic factor_miroc_rcp26
# Specify the directory where the CSV files are located

#########original test with variable theta:
#########directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp26'


######## fixed theta both in calib and simulation 
######## directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp26_fixedtheta'


###### test with fixed theta in calibration a temp ave hypo in ipcl rcp26 for years 2020 and 2021
#######directory='C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp26_fixedthetaincalib_simurcp26temp20202021'



####### test with fixed theta in calibration but variable for GOTM simulation 
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp26_calibinfixedtheta_simuvartheta'



# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("DO_prof_miroc_rcp26_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = annual_hypolimnetic_ave(C, Vr, time_series )

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_hypolimnetic_ave_miroc_rcp26_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_hypolimnetic_ave'])
        
                


#%%monthly_hypolimnetic_ave_miroc_rcp26

# Specify the directory where the CSV files are located

#########original test with variable theta:
#########directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp26'


######## fixed theta both in calib and simulation 
######## directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp26_fixedtheta'


###### test with fixed theta in calibration a temp ave hypo in ipcl rcp26 for years 2020 and 2021
#######directory='C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp26_fixedthetaincalib_simurcp26temp20202021'



####### test with fixed theta in calibration but variable for GOTM simulation 
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp26_calibinfixedtheta_simuvartheta'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("DO_prof_miroc_rcp26_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = monthly_hypolimnetic_ave(C, Vr, time_series )

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_hypolimnetic_ave_miroc_rcp26_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                

#%% Annual anoxic factor_miroc_rcp60
# Specify the directory where the CSV files are located

#########original test with variable theta:
#########directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp60'


######## fixed theta both in calib and simulation 
######## directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp60_fixedtheta'


###### test with fixed theta in calibration a temp ave hypo in ipcl rcp60 for years 2020 and 2021
#######directory='C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp60_fixedthetaincalib_simurcp60temp20202021'



####### test with fixed theta in calibration but variable for GOTM simulation 
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp60_calibinfixedtheta_simuvartheta'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("DO_prof_miroc_rcp60_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = annual_hypolimnetic_ave(C, Vr, time_series )

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_hypolimnetic_ave_miroc_rcp60_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_hypolimnetic_ave'])
        
                


#%%monthly_hypolimnetic_ave_miroc_rcp60

# Specify the directory where the CSV files are located
#########original test with variable theta:
#########directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp60'


######## fixed theta both in calib and simulation 
######## directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp60_fixedtheta'


###### test with fixed theta in calibration a temp ave hypo in ipcl rcp60 for years 2020 and 2021
#######directory='C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp60_fixedthetaincalib_simurcp60temp20202021'



####### test with fixed theta in calibration but variable for GOTM simulation 
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp60_calibinfixedtheta_simuvartheta'



# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("DO_prof_miroc_rcp60_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = monthly_hypolimnetic_ave(C, Vr, time_series )

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_hypolimnetic_ave_miroc_rcp60_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                



#%% Annual anoxic factor_miroc_rcp85
# Specify the directory where the CSV files are located

#########original test with variable theta:
#########directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp85'


######## fixed theta both in calib and simulation 
######## directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp85_fixedtheta'


###### test with fixed theta in calibration a temp ave hypo in ipcl rcp85 for years 2020 and 2021
#######directory='C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp85_fixedthetaincalib_simurcp85temp20202021'



####### test with fixed theta in calibration but variable for GOTM simulation 
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp85_calibinfixedtheta_simuvartheta'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("DO_prof_miroc_rcp85_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = annual_hypolimnetic_ave(C, Vr, time_series )

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_hypolimnetic_ave_miroc_rcp85_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_hypolimnetic_ave'])
        
                


#%%monthly_hypolimnetic_ave_miroc_rcp85

# Specify the directory where the CSV files are located

#########original test with variable theta:
#########directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp85'


######## fixed theta both in calib and simulation 
######## directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp85_fixedtheta'


###### test with fixed theta in calibration a temp ave hypo in ipcl rcp85 for years 2020 and 2021
#######directory='C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp85_fixedthetaincalib_simurcp85temp20202021'



####### test with fixed theta in calibration but variable for GOTM simulation 
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp85_calibinfixedtheta_simuvartheta'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("DO_prof_miroc_rcp85_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = monthly_hypolimnetic_ave(C, Vr, time_series )

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_hypolimnetic_ave_miroc_rcp85_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%GLUE method raeding again these files %%%%%%%%%%%%%%%%%%%

#%%his


# Specify the directory where the CSV files are located


#########original test with variable theta:
#########directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/his'


######## fixed theta both in calib and simulation 
#######directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/his_fixedtheta'




####### test with fixed theta in calibration but variable for GOTM simulation 
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/his_calibinfixedtheta_simuvartheta'



all_annual_hypolimnetic_ave= pd.DataFrame([])
all_weights= np.array([])


# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("annual_hypolimnetic_ave_gfdl_his"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        annual_hypolimnetic_ave = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        annual_hypolimnetic_ave=annual_hypolimnetic_ave.set_index(annual_hypolimnetic_ave['year'])
        
        all_annual_hypolimnetic_ave = pd.concat([all_annual_hypolimnetic_ave , annual_hypolimnetic_ave['annual_hypolimnetic_ave']], axis=1)
        

#########original test with variable theta:
#########directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/his'


######## fixed theta both in calib and simulation 
#######directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/his_fixedtheta'


####### test with fixed theta in calibration but variable for GOTM simulation 
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/his_calibinfixedtheta_simuvartheta'


# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("annual_hypolimnetic_ave_hadgem_his"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        annual_hypolimnetic_ave = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        annual_hypolimnetic_ave=annual_hypolimnetic_ave.set_index(annual_hypolimnetic_ave['year'])
        
        all_annual_hypolimnetic_ave = pd.concat([all_annual_hypolimnetic_ave , annual_hypolimnetic_ave['annual_hypolimnetic_ave']], axis=1)
        
        
        

#########original test with variable theta:
#########directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/his'


######## fixed theta both in calib and simulation 
#######directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/his_fixedtheta'


####### test with fixed theta in calibration but variable for GOTM simulation 
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/his_calibinfixedtheta_simuvartheta'     

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("annual_hypolimnetic_ave_ipsl_his"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        annual_hypolimnetic_ave = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        annual_hypolimnetic_ave=annual_hypolimnetic_ave.set_index(annual_hypolimnetic_ave['year'])
        
        all_annual_hypolimnetic_ave = pd.concat([all_annual_hypolimnetic_ave , annual_hypolimnetic_ave['annual_hypolimnetic_ave']], axis=1)
        
        
        

#########original test with variable theta:
#########directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/his'


######## fixed theta both in calib and simulation 
#######directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/his_fixedtheta'


####### test with fixed theta in calibration but variable for GOTM simulation 
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/his_calibinfixedtheta_simuvartheta'     

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("annual_hypolimnetic_ave_miroc_his"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        annual_hypolimnetic_ave = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        annual_hypolimnetic_ave=annual_hypolimnetic_ave.set_index(annual_hypolimnetic_ave['year'])
        
        all_annual_hypolimnetic_ave = pd.concat([all_annual_hypolimnetic_ave , annual_hypolimnetic_ave['annual_hypolimnetic_ave']], axis=1)
        
        
        
        


# annual anoxic duration  
timeseries_year_his= all_annual_hypolimnetic_ave.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_annual_hypolimnetic_ave.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights))

# Build glue df
glue_df_annual_hypolimnetic_ave_his = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_df_annual_hypolimnetic_ave_his=glue_df_annual_hypolimnetic_ave_his.set_index(timeseries_year_his)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory

#########original test with variable theta:
#########glue_df_annual_hypolimnetic_ave_his.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/his/glue_df_anoxic_factor_his.csv')


######## fixed theta both in calib and simulation 
#########glue_df_annual_hypolimnetic_ave_his.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/his_fixedtheta/glue_df_anoxic_factor_his.csv')



####### test with fixed theta in calibration but variable for GOTM simulation 
glue_df_annual_hypolimnetic_ave_his.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/his_calibinfixedtheta_simuvartheta/glue_df_anoxic_factor_his.csv')

#%%rcp26


# Specify the directory where the CSV files are located


#########original test with variable theta:
#########directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp26'


######## fixed theta both in calib and simulation 
######## directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp26_fixedtheta'


###### test with fixed theta in calibration a temp ave hypo in ipcl rcp26 for years 2020 and 2021
#######directory='C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp26_fixedthetaincalib_simurcp26temp20202021'



####### test with fixed theta in calibration but variable for GOTM simulation 
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp26_calibinfixedtheta_simuvartheta'



all_annual_hypolimnetic_ave= pd.DataFrame([])
all_weights= np.array([])


# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("annual_hypolimnetic_ave_gfdl_rcp26"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        annual_hypolimnetic_ave = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        annual_hypolimnetic_ave=annual_hypolimnetic_ave.set_index(annual_hypolimnetic_ave['year'])
        
        all_annual_hypolimnetic_ave = pd.concat([all_annual_hypolimnetic_ave , annual_hypolimnetic_ave['annual_hypolimnetic_ave']], axis=1)
        

#########original test with variable theta:
#########directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp26'


######## fixed theta both in calib and simulation 
######## directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp26_fixedtheta'


###### test with fixed theta in calibration a temp ave hypo in ipcl rcp26 for years 2020 and 2021
#######directory='C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp26_fixedthetaincalib_simurcp26temp20202021'



####### test with fixed theta in calibration but variable for GOTM simulation 
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp26_calibinfixedtheta_simuvartheta'


# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("annual_hypolimnetic_ave_hadgem_rcp26"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        annual_hypolimnetic_ave = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        annual_hypolimnetic_ave=annual_hypolimnetic_ave.set_index(annual_hypolimnetic_ave['year'])
        
        all_annual_hypolimnetic_ave = pd.concat([all_annual_hypolimnetic_ave , annual_hypolimnetic_ave['annual_hypolimnetic_ave']], axis=1)
        
        
        

#########original test with variable theta:
#########directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp26'


######## fixed theta both in calib and simulation 
######## directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp26_fixedtheta'


###### test with fixed theta in calibration a temp ave hypo in ipcl rcp26 for years 2020 and 2021
#######directory='C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp26_fixedthetaincalib_simurcp26temp20202021'



####### test with fixed theta in calibration but variable for GOTM simulation 
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp26_calibinfixedtheta_simuvartheta'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("annual_hypolimnetic_ave_ipsl_rcp26"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        annual_hypolimnetic_ave = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        annual_hypolimnetic_ave=annual_hypolimnetic_ave.set_index(annual_hypolimnetic_ave['year'])
        
        all_annual_hypolimnetic_ave = pd.concat([all_annual_hypolimnetic_ave , annual_hypolimnetic_ave['annual_hypolimnetic_ave']], axis=1)
        
        
        

#########original test with variable theta:
#########directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp26'


######## fixed theta both in calib and simulation 
######## directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp26_fixedtheta'


###### test with fixed theta in calibration a temp ave hypo in ipcl rcp26 for years 2020 and 2021
#######directory='C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp26_fixedthetaincalib_simurcp26temp20202021'



####### test with fixed theta in calibration but variable for GOTM simulation 
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp26_calibinfixedtheta_simuvartheta'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("annual_hypolimnetic_ave_miroc_rcp26"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        annual_hypolimnetic_ave = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        annual_hypolimnetic_ave=annual_hypolimnetic_ave.set_index(annual_hypolimnetic_ave['year'])
        
        all_annual_hypolimnetic_ave = pd.concat([all_annual_hypolimnetic_ave , annual_hypolimnetic_ave['annual_hypolimnetic_ave']], axis=1)
        
        
        
        


# annual anoxic duration  
timeseries_year_rcp26= all_annual_hypolimnetic_ave.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_annual_hypolimnetic_ave.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights))

# Build glue df
glue_df_annual_hypolimnetic_ave_rcp26 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_df_annual_hypolimnetic_ave_rcp26=glue_df_annual_hypolimnetic_ave_rcp26.set_index(timeseries_year_rcp26)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory

#########original test with variable theta:
#########glue_df_annual_hypolimnetic_ave_rcp26.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/alltogther/glue_df_anoxic_factor_rcp26.csv')


######## fixed theta both in calib and simulation 
#########glue_df_annual_hypolimnetic_ave_rcp26.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/alltogther_fixedtheta/glue_df_anoxic_factor_rcp26.csv')


###### test with fixed theta in calibration a temp ave hypo in ipcl rcp26 for years 2020 and 2021
#########glue_df_annual_hypolimnetic_ave_rcp26.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/alltogther_fixedtheta_temp_gcms_2020_2021/glue_df_anoxic_factor_rcp26.csv')


####### test with fixed theta in calibration but variable for GOTM simulation 
glue_df_annual_hypolimnetic_ave_rcp26.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/alltogther_calibinfixedtheta_simuvartheta/glue_df_anoxic_factor_rcp26.csv')



#%%rcp60


# Specify the directory where the CSV files are located


#########original test with variable theta:
#########directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp60'


######## fixed theta both in calib and simulation 
######## directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp60_fixedtheta'


###### test with fixed theta in calibration a temp ave hypo in ipcl rcp60 for years 2020 and 2021
#######directory='C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp60_fixedthetaincalib_simurcp60temp20202021'



####### test with fixed theta in calibration but variable for GOTM simulation 
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp60_calibinfixedtheta_simuvartheta'



all_annual_hypolimnetic_ave= pd.DataFrame([])
all_weights= np.array([])


# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("annual_hypolimnetic_ave_gfdl_rcp60"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        annual_hypolimnetic_ave = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        annual_hypolimnetic_ave=annual_hypolimnetic_ave.set_index(annual_hypolimnetic_ave['year'])
        
        all_annual_hypolimnetic_ave = pd.concat([all_annual_hypolimnetic_ave , annual_hypolimnetic_ave['annual_hypolimnetic_ave']], axis=1)
        

#########original test with variable theta:
#########directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp60'


######## fixed theta both in calib and simulation 
######## directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp60_fixedtheta'


###### test with fixed theta in calibration a temp ave hypo in ipcl rcp60 for years 2020 and 2021
#######directory='C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp60_fixedthetaincalib_simurcp60temp20202021'



####### test with fixed theta in calibration but variable for GOTM simulation 
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp60_calibinfixedtheta_simuvartheta'


# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("annual_hypolimnetic_ave_hadgem_rcp60"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        annual_hypolimnetic_ave = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        annual_hypolimnetic_ave=annual_hypolimnetic_ave.set_index(annual_hypolimnetic_ave['year'])
        
        all_annual_hypolimnetic_ave = pd.concat([all_annual_hypolimnetic_ave , annual_hypolimnetic_ave['annual_hypolimnetic_ave']], axis=1)
        
        
        

#########original test with variable theta:
#########directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp60'


######## fixed theta both in calib and simulation 
######## directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp60_fixedtheta'


###### test with fixed theta in calibration a temp ave hypo in ipcl rcp60 for years 2020 and 2021
#######directory='C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp60_fixedthetaincalib_simurcp60temp20202021'



####### test with fixed theta in calibration but variable for GOTM simulation 
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp60_calibinfixedtheta_simuvartheta'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("annual_hypolimnetic_ave_ipsl_rcp60"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        annual_hypolimnetic_ave = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        annual_hypolimnetic_ave=annual_hypolimnetic_ave.set_index(annual_hypolimnetic_ave['year'])
        
        all_annual_hypolimnetic_ave = pd.concat([all_annual_hypolimnetic_ave , annual_hypolimnetic_ave['annual_hypolimnetic_ave']], axis=1)
        
        
        

#########original test with variable theta:
#########directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp60'


######## fixed theta both in calib and simulation 
######## directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp60_fixedtheta'


###### test with fixed theta in calibration a temp ave hypo in ipcl rcp60 for years 2020 and 2021
#######directory='C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp60_fixedthetaincalib_simurcp60temp20202021'



####### test with fixed theta in calibration but variable for GOTM simulation 
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp60_calibinfixedtheta_simuvartheta'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("annual_hypolimnetic_ave_miroc_rcp60"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        annual_hypolimnetic_ave = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        annual_hypolimnetic_ave=annual_hypolimnetic_ave.set_index(annual_hypolimnetic_ave['year'])
        
        all_annual_hypolimnetic_ave = pd.concat([all_annual_hypolimnetic_ave , annual_hypolimnetic_ave['annual_hypolimnetic_ave']], axis=1)
        
        
        
        


# annual anoxic duration  
timeseries_year_rcp60= all_annual_hypolimnetic_ave.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_annual_hypolimnetic_ave.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights))

# Build glue df
glue_df_annual_hypolimnetic_ave_rcp60 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_df_annual_hypolimnetic_ave_rcp60=glue_df_annual_hypolimnetic_ave_rcp60.set_index(timeseries_year_rcp60)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory

#########original test with variable theta:
#########glue_df_annual_hypolimnetic_ave_rcp60.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/alltogther/glue_df_anoxic_factor_rcp60.csv')


######## fixed theta both in calib and simulation 
#########glue_df_annual_hypolimnetic_ave_rcp60.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/alltogther_fixedtheta/glue_df_anoxic_factor_rcp60.csv')


###### test with fixed theta in calibration a temp ave hypo in ipcl rcp60 for years 2020 and 2021
#########glue_df_annual_hypolimnetic_ave_rcp60.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/alltogther_fixedtheta_temp_gcms_2020_2021/glue_df_anoxic_factor_rcp60.csv')


####### test with fixed theta in calibration but variable for GOTM simulation 
glue_df_annual_hypolimnetic_ave_rcp60.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/alltogther_calibinfixedtheta_simuvartheta/glue_df_anoxic_factor_rcp60.csv')



#%%rcp85


# Specify the directory where the CSV files are located


#########original test with variable theta:
#########directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp85'


######## fixed theta both in calib and simulation 
######## directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp85_fixedtheta'


###### test with fixed theta in calibration a temp ave hypo in ipcl rcp85 for years 2020 and 2021
#######directory='C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp85_fixedthetaincalib_simurcp85temp20202021'



####### test with fixed theta in calibration but variable for GOTM simulation 
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp85_calibinfixedtheta_simuvartheta'



all_annual_hypolimnetic_ave= pd.DataFrame([])
all_weights= np.array([])


# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("annual_hypolimnetic_ave_gfdl_rcp85"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        annual_hypolimnetic_ave = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        annual_hypolimnetic_ave=annual_hypolimnetic_ave.set_index(annual_hypolimnetic_ave['year'])
        
        all_annual_hypolimnetic_ave = pd.concat([all_annual_hypolimnetic_ave , annual_hypolimnetic_ave['annual_hypolimnetic_ave']], axis=1)
        

#########original test with variable theta:
#########directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp85'


######## fixed theta both in calib and simulation 
######## directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp85_fixedtheta'


###### test with fixed theta in calibration a temp ave hypo in ipcl rcp85 for years 2020 and 2021
#######directory='C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp85_fixedthetaincalib_simurcp85temp20202021'



####### test with fixed theta in calibration but variable for GOTM simulation 
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp85_calibinfixedtheta_simuvartheta'


# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("annual_hypolimnetic_ave_hadgem_rcp85"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        annual_hypolimnetic_ave = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        annual_hypolimnetic_ave=annual_hypolimnetic_ave.set_index(annual_hypolimnetic_ave['year'])
        
        all_annual_hypolimnetic_ave = pd.concat([all_annual_hypolimnetic_ave , annual_hypolimnetic_ave['annual_hypolimnetic_ave']], axis=1)
        
        
        

#########original test with variable theta:
#########directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp85'


######## fixed theta both in calib and simulation 
######## directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp85_fixedtheta'


###### test with fixed theta in calibration a temp ave hypo in ipcl rcp85 for years 2020 and 2021
#######directory='C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp85_fixedthetaincalib_simurcp85temp20202021'



####### test with fixed theta in calibration but variable for GOTM simulation 
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp85_calibinfixedtheta_simuvartheta'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("annual_hypolimnetic_ave_ipsl_rcp85"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        annual_hypolimnetic_ave = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        annual_hypolimnetic_ave=annual_hypolimnetic_ave.set_index(annual_hypolimnetic_ave['year'])
        
        all_annual_hypolimnetic_ave = pd.concat([all_annual_hypolimnetic_ave , annual_hypolimnetic_ave['annual_hypolimnetic_ave']], axis=1)
        
        
        

#########original test with variable theta:
#########directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp85'


######## fixed theta both in calib and simulation 
######## directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp85_fixedtheta'


###### test with fixed theta in calibration a temp ave hypo in ipcl rcp85 for years 2020 and 2021
#######directory='C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp85_fixedthetaincalib_simurcp85temp20202021'



####### test with fixed theta in calibration but variable for GOTM simulation 
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp85_calibinfixedtheta_simuvartheta'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("annual_hypolimnetic_ave_miroc_rcp85"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        annual_hypolimnetic_ave = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        annual_hypolimnetic_ave=annual_hypolimnetic_ave.set_index(annual_hypolimnetic_ave['year'])
        
        all_annual_hypolimnetic_ave = pd.concat([all_annual_hypolimnetic_ave , annual_hypolimnetic_ave['annual_hypolimnetic_ave']], axis=1)
        
        
        
        


# annual anoxic duration  
timeseries_year_rcp85= all_annual_hypolimnetic_ave.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_annual_hypolimnetic_ave.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights))

# Build glue df
glue_df_annual_hypolimnetic_ave_rcp85 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_df_annual_hypolimnetic_ave_rcp85=glue_df_annual_hypolimnetic_ave_rcp85.set_index(timeseries_year_rcp85)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory

#########original test with variable theta:
#########glue_df_annual_hypolimnetic_ave_rcp85.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/alltogther/glue_df_anoxic_factor_rcp85.csv')


######## fixed theta both in calib and simulation 
#########glue_df_annual_hypolimnetic_ave_rcp85.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/alltogther_fixedtheta/glue_df_anoxic_factor_rcp85.csv')


###### test with fixed theta in calibration a temp ave hypo in ipcl rcp85 for years 2020 and 2021
#########glue_df_annual_hypolimnetic_ave_rcp85.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/alltogther_fixedtheta_temp_gcms_2020_2021/glue_df_anoxic_factor_rcp85.csv')


####### test with fixed theta in calibration but variable for GOTM simulation 
glue_df_annual_hypolimnetic_ave_rcp85.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/alltogther_calibinfixedtheta_simuvartheta/glue_df_anoxic_factor_rcp85.csv')


#%%#######fixed theta:
    
#######glue_df_annual_hypolimnetic_ave_his_fixedtheta=  glue_df_annual_hypolimnetic_ave_his.copy()

glue_df_annual_hypolimnetic_ave_his= glue_df_annual_hypolimnetic_ave_his_fixedtheta.copy()

#######glue_df_annual_hypolimnetic_ave_rcp26_fixedtheta=  glue_df_annual_hypolimnetic_ave_rcp26.copy()

glue_df_annual_hypolimnetic_ave_rcp26= glue_df_annual_hypolimnetic_ave_rcp26_fixedtheta.copy()

#######glue_df_annual_hypolimnetic_ave_rcp60_fixedtheta=  glue_df_annual_hypolimnetic_ave_rcp60.copy()

glue_df_annual_hypolimnetic_ave_rcp60= glue_df_annual_hypolimnetic_ave_rcp60_fixedtheta.copy()

#######glue_df_annual_hypolimnetic_ave_rcp85_fixedtheta=  glue_df_annual_hypolimnetic_ave_rcp85.copy()

glue_df_annual_hypolimnetic_ave_rcp85= glue_df_annual_hypolimnetic_ave_rcp85_fixedtheta.copy()



#%%_vartheta

glue_df_annual_hypolimnetic_ave_his_vartheta= glue_df_annual_hypolimnetic_ave_his.copy()



glue_df_annual_hypolimnetic_ave_rcp26_vartheta= glue_df_annual_hypolimnetic_ave_rcp26.copy()


glue_df_annual_hypolimnetic_ave_rcp60_vartheta= glue_df_annual_hypolimnetic_ave_rcp60.copy()


glue_df_annual_hypolimnetic_ave_rcp85_vartheta= glue_df_annual_hypolimnetic_ave_rcp85.copy()


#%%difference of Vartheta model and fixed theta 


diff_median_annual_hypolimnetic_ave_vartheta_fixedtheta_his=glue_df_annual_hypolimnetic_ave_his_vartheta['50%']-glue_df_annual_hypolimnetic_ave_his['50%']
np.mean(diff_median_annual_hypolimnetic_ave_vartheta_fixedtheta_his)
-1.521539830552154

autocorr_MK_org_modif_sens_slope_test(diff_median_annual_hypolimnetic_ave_vartheta_fixedtheta_his)
(0.4102745697759908,
 'positively autocorrelated',
 'no trend',
 0.08641995700155558,
 0,
 0)




diff_median_annual_hypolimnetic_ave_vartheta_fixedtheta_rcp26=glue_df_annual_hypolimnetic_ave_rcp26_vartheta['50%']-glue_df_annual_hypolimnetic_ave_rcp26['50%']
np.mean(diff_median_annual_hypolimnetic_ave_vartheta_fixedtheta_rcp26)
-2.3009426195783225
autocorr_MK_org_modif_sens_slope_test(diff_median_annual_hypolimnetic_ave_vartheta_fixedtheta_rcp26)

(0.2471291056619972,
 'positively autocorrelated',
 'no trend',
 0.5406757306713583,
 0,
 0)



diff_median_annual_hypolimnetic_ave_vartheta_fixedtheta_rcp60=glue_df_annual_hypolimnetic_ave_rcp60_vartheta['50%']-glue_df_annual_hypolimnetic_ave_rcp60['50%']
np.mean(diff_median_annual_hypolimnetic_ave_vartheta_fixedtheta_rcp60)
-1.3593195664094877

autocorr_MK_org_modif_sens_slope_test(diff_median_annual_hypolimnetic_ave_vartheta_fixedtheta_rcp60)
(0.45142216245912026,
 'positively autocorrelated',
 'no trend',
 0.24575216426645285,
 0,
 0)



diff_median_annual_hypolimnetic_ave_vartheta_fixedtheta_rcp85=glue_df_annual_hypolimnetic_ave_rcp85_vartheta['50%']-glue_df_annual_hypolimnetic_ave_rcp85['50%']
np.mean(diff_median_annual_hypolimnetic_ave_vartheta_fixedtheta_rcp85)
-1.8403265395237618

autocorr_MK_org_modif_sens_slope_test(diff_median_annual_hypolimnetic_ave_vartheta_fixedtheta_rcp85)
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


ax=plt.plot(diff_median_annual_hypolimnetic_ave_vartheta_fixedtheta_his.index, diff_median_annual_hypolimnetic_ave_vartheta_fixedtheta_his, 'grey', label='His median', alpha=1, linewidth=3 )


ax=plt.plot(diff_median_annual_hypolimnetic_ave_vartheta_fixedtheta_rcp26.index, diff_median_annual_hypolimnetic_ave_vartheta_fixedtheta_rcp26, 'green', label='RCP2.6 median', alpha=1, linewidth=3 )

ax=plt.plot(diff_median_annual_hypolimnetic_ave_vartheta_fixedtheta_rcp60.index, diff_median_annual_hypolimnetic_ave_vartheta_fixedtheta_rcp60, 'yellow', label='RCP6.0 median',alpha=1, linewidth=3 )

ax=plt.plot(diff_median_annual_hypolimnetic_ave_vartheta_fixedtheta_rcp85.index, diff_median_annual_hypolimnetic_ave_vartheta_fixedtheta_rcp85, 'r', label='RCP8.5 median', alpha=0.9, linewidth=3 )



ax=plt.ylabel('Difference of fixed and variable Ktemp assumption in simulating annual anoxic factor [d year$^{-1}$]' , fontsize=26)
ax=plt.xlabel('Year' , fontsize=26)
ax=plt.yticks(np.arange(-4, 3, 1) , fontsize= 22)
ax=plt.xticks(rotation=45 , fontsize=22)
ax=plt.legend(bbox_to_anchor=(0.7, -0.15), fontsize=22)


####### test with fixed theta in calibration but variable for GOTM simulation 
fig.savefig("GLUE_Timeseries_hypolimnetic_DO_6combinationJaJv_ave_obs_4models_diff_fixed_var_theta.png", dpi=300, bbox_inches='tight')




#%% first 10 years 2020-2029

#rcp26
glue_df_annual_hypolimnetic_ave_median_1st_10years_rcp26=glue_df_annual_hypolimnetic_ave_rcp26[(2019<glue_df_annual_hypolimnetic_ave_rcp26.index) & (glue_df_annual_hypolimnetic_ave_rcp26.index<2030)]['50%']
np.mean(glue_df_annual_hypolimnetic_ave_median_1st_10years_rcp26)
#7.470031426050075

glue_df_annual_hypolimnetic_ave_median_1st_10years_rcp26_vartheta=glue_df_annual_hypolimnetic_ave_rcp26_vartheta[(2019<glue_df_annual_hypolimnetic_ave_rcp26_vartheta.index) & (glue_df_annual_hypolimnetic_ave_rcp26_vartheta.index<2030)]['50%']
np.mean(glue_df_annual_hypolimnetic_ave_median_1st_10years_rcp26_vartheta)
#5.655030434919324


#rcp60

glue_df_annual_hypolimnetic_ave_median_1st_10years_rcp60=glue_df_annual_hypolimnetic_ave_rcp60[(2019<glue_df_annual_hypolimnetic_ave_rcp60.index) & (glue_df_annual_hypolimnetic_ave_rcp60.index<2030)]['50%']
np.mean(glue_df_annual_hypolimnetic_ave_median_1st_10years_rcp60)
#7.077280785340525



glue_df_annual_hypolimnetic_ave_median_1st_10years_rcp60_vartheta=glue_df_annual_hypolimnetic_ave_rcp60_vartheta[(2019<glue_df_annual_hypolimnetic_ave_rcp60_vartheta.index) & (glue_df_annual_hypolimnetic_ave_rcp60_vartheta.index<2030)]['50%']
np.mean(glue_df_annual_hypolimnetic_ave_median_1st_10years_rcp60_vartheta)
#5.442294872796134

#rcp85

glue_df_annual_hypolimnetic_ave_median_1st_10years_rcp85=glue_df_annual_hypolimnetic_ave_rcp85[(2019<glue_df_annual_hypolimnetic_ave_rcp85.index) & (glue_df_annual_hypolimnetic_ave_rcp85.index<2030)]['50%']
np.mean(glue_df_annual_hypolimnetic_ave_median_1st_10years_rcp85)
#6.80621601212993

glue_df_annual_hypolimnetic_ave_median_1st_10years_rcp85_vartheta=glue_df_annual_hypolimnetic_ave_rcp85_vartheta[(2019<glue_df_annual_hypolimnetic_ave_rcp85_vartheta.index) & (glue_df_annual_hypolimnetic_ave_rcp85_vartheta.index<2030)]['50%']
np.mean(glue_df_annual_hypolimnetic_ave_median_1st_10years_rcp85_vartheta)
#5.589130553716512

#%%last 10 years 2090-2099

#rcp26
glue_df_annual_hypolimnetic_ave_median_last_10years_rcp26=glue_df_annual_hypolimnetic_ave_rcp26[glue_df_annual_hypolimnetic_ave_rcp26.index>2089]['50%']
np.mean(glue_df_annual_hypolimnetic_ave_median_last_10years_rcp26)
#8.613753815447875

glue_df_annual_hypolimnetic_ave_median_last_10years_rcp26_vartheta=glue_df_annual_hypolimnetic_ave_rcp26_vartheta[glue_df_annual_hypolimnetic_ave_rcp26_vartheta.index>2089]['50%']
np.mean(glue_df_annual_hypolimnetic_ave_median_last_10years_rcp26_vartheta)
#5.99974215818178

#rcp60
glue_df_annual_hypolimnetic_ave_median_last_10years_rcp60=glue_df_annual_hypolimnetic_ave_rcp60[glue_df_annual_hypolimnetic_ave_rcp60.index>2089]['50%']
np.mean(glue_df_annual_hypolimnetic_ave_median_last_10years_rcp60)
#8.840670784774442

glue_df_annual_hypolimnetic_ave_median_last_10years_rcp60_vartheta=glue_df_annual_hypolimnetic_ave_rcp60_vartheta[glue_df_annual_hypolimnetic_ave_rcp60_vartheta.index>2089]['50%']
np.mean(glue_df_annual_hypolimnetic_ave_median_last_10years_rcp60_vartheta)
#7.461205289215991
#rcp85
glue_df_annual_hypolimnetic_ave_median_last_10years_rcp85=glue_df_annual_hypolimnetic_ave_rcp85[glue_df_annual_hypolimnetic_ave_rcp85.index>2089]['50%']
np.mean(glue_df_annual_hypolimnetic_ave_median_last_10years_rcp85)
#10.848450635366076

glue_df_annual_hypolimnetic_ave_median_last_10years_rcp85_vartheta=glue_df_annual_hypolimnetic_ave_rcp85_vartheta[glue_df_annual_hypolimnetic_ave_rcp85_vartheta.index>2089]['50%']
np.mean(glue_df_annual_hypolimnetic_ave_median_last_10years_rcp85_vartheta)
#9.225106418152142

#%% 100 years for rcps 

#rcp26

#fixed theta
glue_df_annual_hypolimnetic_ave_4models_100years_rcp26=pd.concat([glue_df_annual_hypolimnetic_ave_his[glue_df_annual_hypolimnetic_ave_his.index>1999] , glue_df_annual_hypolimnetic_ave_rcp26])
autocorr_MK_org_modif_sens_slope_test( glue_df_annual_hypolimnetic_ave_4models_100years_rcp26 ['50%'])  

(0.03233165257593502,
 'positively autocorrelated',
 'increasing',
 1.235052435877293e-07,
 0.0121937938499866,
 7.255097746966682)





#Var theta
glue_df_annual_hypolimnetic_ave_4models_100years_rcp26_vartheta=pd.concat([glue_df_annual_hypolimnetic_ave_his_vartheta[glue_df_annual_hypolimnetic_ave_his_vartheta.index>1999] , glue_df_annual_hypolimnetic_ave_rcp26_vartheta])
autocorr_MK_org_modif_sens_slope_test( glue_df_annual_hypolimnetic_ave_4models_100years_rcp26_vartheta ['50%'])  

(0.03955505915646442,
 'positively autocorrelated',
 'increasing',
 0.0006010992236442636,
 0.010497984593900105,
 5.030834333984101)



#rcp60

#fixed theta
glue_df_annual_hypolimnetic_ave_4models_100years_rcp60=pd.concat([glue_df_annual_hypolimnetic_ave_his[glue_df_annual_hypolimnetic_ave_his.index>1999] , glue_df_annual_hypolimnetic_ave_rcp60])
autocorr_MK_org_modif_sens_slope_test( glue_df_annual_hypolimnetic_ave_4models_100years_rcp60 ['50%'])  
(0.02795672807292709,
 'positively autocorrelated',
 'increasing',
 2.220446049250313e-16,
 0.0332750689583886,
 5.986757230735907)




#Var theta
glue_df_annual_hypolimnetic_ave_4models_100years_rcp60_vartheta=pd.concat([glue_df_annual_hypolimnetic_ave_his_vartheta[glue_df_annual_hypolimnetic_ave_his_vartheta.index>1999] , glue_df_annual_hypolimnetic_ave_rcp60_vartheta])
autocorr_MK_org_modif_sens_slope_test( glue_df_annual_hypolimnetic_ave_4models_100years_rcp60_vartheta ['50%'])  
(0.029177475988549587,
 'positively autocorrelated',
 'increasing',
 2.970956813896919e-13,
 0.03420571640423424,
 4.397863069746866)


#rcp85

#fixed theta
glue_df_annual_hypolimnetic_ave_4models_100years_rcp85=pd.concat([glue_df_annual_hypolimnetic_ave_his[glue_df_annual_hypolimnetic_ave_his.index>1999] , glue_df_annual_hypolimnetic_ave_rcp85])
autocorr_MK_org_modif_sens_slope_test( glue_df_annual_hypolimnetic_ave_4models_100years_rcp85 ['50%'])  
(0.031072004914250547,
 'positively autocorrelated',
 'increasing',
 0.0,
 0.05455817956023478,
 5.832292270455436)




#Var theta
glue_df_annual_hypolimnetic_ave_4models_100years_rcp85_vartheta=pd.concat([glue_df_annual_hypolimnetic_ave_his_vartheta[glue_df_annual_hypolimnetic_ave_his_vartheta.index>1999] , glue_df_annual_hypolimnetic_ave_rcp85_vartheta])
autocorr_MK_org_modif_sens_slope_test( glue_df_annual_hypolimnetic_ave_4models_100years_rcp85_vartheta ['50%'])  

(0.035580951696717295,
 'positively autocorrelated',
 'increasing',
 0.0,
 0.05165045008766002,
 3.9207344560109947)

#%% trendline sen's slope 

autocorr_MK_org_modif_sens_slope_test(glue_df_annual_hypolimnetic_ave_his['50%']) 

Out[1243]: 
(0.08861134396877238,
 'positively autocorrelated',
 'no trend',
 0.10192618852194646,
 0,
 0)



autocorr_MK_org_modif_sens_slope_test(glue_df_annual_hypolimnetic_ave_his_vartheta['50%']) 

(0.1383412609645987,
 'positively autocorrelated',
 'no trend',
 0.31072008139962315,
 0,
 0)



autocorr_MK_org_modif_sens_slope_test(glue_df_annual_hypolimnetic_ave_rcp26['50%']) 
(0.03379118006876991,
 'positively autocorrelated',
 'increasing',
 6.908279212325397e-05,
 0.010564337601135008,
 7.4785025189153735)
autocorr_MK_org_modif_sens_slope_test(glue_df_annual_hypolimnetic_ave_rcp26_vartheta['50%']) 
(0.039507716688300144,
 'positively autocorrelated',
 'increasing',
 0.022504355893704142,
 0.008218111766768784,
 5.1831384217248875)



autocorr_MK_org_modif_sens_slope_test(glue_df_annual_hypolimnetic_ave_rcp60['50%']) 
(0.028720309370685593,
 'positively autocorrelated',
 'increasing',
 0.0,
 0.03880652178553318,
 5.88161432295651)
autocorr_MK_org_modif_sens_slope_test(glue_df_annual_hypolimnetic_ave_rcp60_vartheta['50%']) 
(0.028883853368500165,
 'positively autocorrelated',
 'increasing',
 7.286293790542686e-10,
 0.033514404467106934,
 4.616452079764355)


autocorr_MK_org_modif_sens_slope_test(glue_df_annual_hypolimnetic_ave_rcp85['50%']) 
(0.03167796451466309,
 'positively autocorrelated',
 'increasing',
 0.0,
 0.059792750353943616,
 5.873773932605548)
autocorr_MK_org_modif_sens_slope_test(glue_df_annual_hypolimnetic_ave_rcp85_vartheta['50%']) 
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
#########os.chdir('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/alltogther/')


######## fixed theta both in calib and simulation 
########os.chdir('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/alltogther_fixedtheta/')


###### test with fixed theta in calibration a temp ave hypo in GCMs in 2020 2021
######os.chdir('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/alltogther_fixedtheta_temp_gcms_2020_2021/')


####### test with fixed theta in calibration but variable for GOTM simulation 
os.chdir('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/alltogther_calibinfixedtheta_simuvartheta/')


import matplotlib.pyplot as plt

fig = plt.figure(figsize=(15, 10))
ax= plt.subplot(111)


#ax=plt.fill_between(glue_df_annual_hypolimnetic_ave_his.index.astype(float), glue_df_annual_hypolimnetic_ave_his['5%'], glue_df_annual_hypolimnetic_ave_his['95%'], color='grey', alpha=0.2 ,  label= 'His 90% CI')
#ax=plt.plot(glue_df_annual_hypolimnetic_ave_his.index.astype(float), glue_df_annual_hypolimnetic_ave_his['50%'].astype(float), 'k', label='His median', alpha=0.9, linewidth=3  )



ax=plt.fill_between(glue_df_annual_hypolimnetic_ave_4models_100years_rcp26_vartheta.index.astype(float), glue_df_annual_hypolimnetic_ave_4models_100years_rcp26_vartheta['5%'], glue_df_annual_hypolimnetic_ave_4models_100years_rcp26_vartheta['95%'], color='darkgreen', alpha=0.3 ,  label= 'RCP2.6 90% CI')
ax=plt.plot(glue_df_annual_hypolimnetic_ave_4models_100years_rcp26_vartheta.index.astype(float), glue_df_annual_hypolimnetic_ave_4models_100years_rcp26_vartheta['50%'], 'darkgreen', label='RCP2.6 median', alpha=0.9, linewidth=3  )
trendline_rcp26=autocorr_MK_org_modif_sens_slope_test(glue_df_annual_hypolimnetic_ave_4models_100years_rcp26_vartheta['50%'])
ax=plt.text(2020, 10, f'y = {trendline_rcp26[-2]:.3f}x + {trendline_rcp26[-1]:.3f}, p < 0.05', color='green', fontsize= 20 )


ax=plt.fill_between(glue_df_annual_hypolimnetic_ave_4models_100years_rcp60_vartheta.index.astype(float), glue_df_annual_hypolimnetic_ave_4models_100years_rcp60_vartheta['5%'], glue_df_annual_hypolimnetic_ave_4models_100years_rcp60_vartheta['95%'], color='yellow', alpha=0.2 ,  label= 'RCP6.0 90% CI')
ax=plt.plot(glue_df_annual_hypolimnetic_ave_4models_100years_rcp60_vartheta.index.astype(float), glue_df_annual_hypolimnetic_ave_4models_100years_rcp60_vartheta['50%'], 'yellow', label='RCP6.0 median', alpha=0.9, linewidth=3  )
trendline_rcp60=autocorr_MK_org_modif_sens_slope_test(glue_df_annual_hypolimnetic_ave_4models_100years_rcp60_vartheta['50%'])
ax=plt.text(2020, 11, f'y = {trendline_rcp60[-2]:.3f}x + {trendline_rcp60[-1]:.3f}, p < 0.05', color='gold', fontsize= 20 )



ax=plt.fill_between(glue_df_annual_hypolimnetic_ave_4models_100years_rcp85_vartheta.index.astype(float), glue_df_annual_hypolimnetic_ave_4models_100years_rcp85_vartheta['5%'], glue_df_annual_hypolimnetic_ave_4models_100years_rcp85_vartheta['95%'], color='r', alpha=0.2 ,  label= 'RCP8.5 90% CI')
ax=plt.plot(glue_df_annual_hypolimnetic_ave_4models_100years_rcp85_vartheta.index.astype(float), glue_df_annual_hypolimnetic_ave_4models_100years_rcp85_vartheta['50%'], 'r', label='RCP8.5 median', alpha=0.9, linewidth=3  )
trendline_rcp85=autocorr_MK_org_modif_sens_slope_test(glue_df_annual_hypolimnetic_ave_4models_100years_rcp85_vartheta['50%'])
ax=plt.text(2020, 12, f'y = {trendline_rcp85[-2]:.3f}x + {trendline_rcp85[-1]:.3f}, p < 0.05', color='r', fontsize= 20 )



ax=plt.ylabel('Anoxic factor per each deoxygenation period [d/year]' , fontsize=26)
ax=plt.xlabel('Year' , fontsize=26)
ax=plt.yticks(fontsize= 22)
ax=plt.xticks(fontsize=22)#rotation=45 , 
ax=plt.legend(bbox_to_anchor=(0.7, -0.2), fontsize=22)#)   
fig.savefig("GLUE_100years_Timeseries_anoxic_factor_7combinationJaJv_ave_obs_4models_4scenarios.png",  dpi=300, bbox_inches='tight')


#%%fixed theta




#########original test with variable theta:
#########os.chdir('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/alltogther/')


######## fixed theta both in calib and simulation 
########os.chdir('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/alltogther_fixedtheta/')


###### test with fixed theta in calibration a temp ave hypo in GCMs in 2020 2021
os.chdir('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/alltogther_fixedtheta_temp_gcms_2020_2021/')


####### test with fixed theta in calibration but variable for GOTM simulation 
######os.chdir('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/alltogther_calibinfixedtheta_simuvartheta/')


import matplotlib.pyplot as plt

fig = plt.figure(figsize=(15, 10))
ax= plt.subplot(111)


#ax=plt.fill_between(glue_df_annual_hypolimnetic_ave_his.index.astype(float), glue_df_annual_hypolimnetic_ave_his['5%'], glue_df_annual_hypolimnetic_ave_his['95%'], color='grey', alpha=0.2 ,  label= 'His 90% CI')
#ax=plt.plot(glue_df_annual_hypolimnetic_ave_his.index.astype(float), glue_df_annual_hypolimnetic_ave_his['50%'].astype(float), 'k', label='His median', alpha=0.9, linewidth=3  )



ax=plt.fill_between(glue_df_annual_hypolimnetic_ave_4models_100years_rcp26.index.astype(float), glue_df_annual_hypolimnetic_ave_4models_100years_rcp26['5%'], glue_df_annual_hypolimnetic_ave_4models_100years_rcp26['95%'], color='darkgreen', alpha=0.3 ,  label= 'RCP2.6 90% CI')
ax=plt.plot(glue_df_annual_hypolimnetic_ave_4models_100years_rcp26.index.astype(float), glue_df_annual_hypolimnetic_ave_4models_100years_rcp26['50%'], 'darkgreen', label='RCP2.6 median', alpha=0.9, linewidth=3  )
trendline_rcp26=autocorr_MK_org_modif_sens_slope_test(glue_df_annual_hypolimnetic_ave_4models_100years_rcp26['50%'])
ax=plt.text(2020, 15, f'y = {trendline_rcp26[-2]:.3f}x + {trendline_rcp26[-1]:.3f}, p < 0.05', color='green', fontsize= 20 )


ax=plt.fill_between(glue_df_annual_hypolimnetic_ave_4models_100years_rcp60.index.astype(float), glue_df_annual_hypolimnetic_ave_4models_100years_rcp60['5%'], glue_df_annual_hypolimnetic_ave_4models_100years_rcp60['95%'], color='yellow', alpha=0.2 ,  label= 'RCP6.0 90% CI')
ax=plt.plot(glue_df_annual_hypolimnetic_ave_4models_100years_rcp60.index.astype(float), glue_df_annual_hypolimnetic_ave_4models_100years_rcp60['50%'], 'yellow', label='RCP6.0 median', alpha=0.9, linewidth=3  )
trendline_rcp60=autocorr_MK_org_modif_sens_slope_test(glue_df_annual_hypolimnetic_ave_4models_100years_rcp60['50%'])
ax=plt.text(2020, 14, f'y = {trendline_rcp60[-2]:.3f}x + {trendline_rcp60[-1]:.3f}, p < 0.05', color='gold', fontsize= 20 )



ax=plt.fill_between(glue_df_annual_hypolimnetic_ave_4models_100years_rcp85.index.astype(float), glue_df_annual_hypolimnetic_ave_4models_100years_rcp85['5%'], glue_df_annual_hypolimnetic_ave_4models_100years_rcp85['95%'], color='r', alpha=0.2 ,  label= 'RCP8.5 90% CI')
ax=plt.plot(glue_df_annual_hypolimnetic_ave_4models_100years_rcp85.index.astype(float), glue_df_annual_hypolimnetic_ave_4models_100years_rcp85['50%'], 'r', label='RCP8.5 median', alpha=0.9, linewidth=3  )
trendline_rcp85=autocorr_MK_org_modif_sens_slope_test(glue_df_annual_hypolimnetic_ave_4models_100years_rcp85['50%'])
ax=plt.text(2020, 13, f'y = {trendline_rcp85[-2]:.3f}x + {trendline_rcp85[-1]:.3f}, p < 0.05', color='r', fontsize= 20 )



ax=plt.ylabel('Anoxic factor per each deoxygenation period [d/year]' , fontsize=26)
ax=plt.xlabel('Year' , fontsize=26)
ax=plt.yticks(fontsize= 22)
ax=plt.xticks(fontsize=22)#rotation=45 , 
ax=plt.legend(bbox_to_anchor=(0.7, -0.2), fontsize=22)#)   
fig.savefig("GLUE_100years_Timeseries_anoxic_factor_7combinationJaJv_ave_obs_4models_4scenarios.png",  dpi=300, bbox_inches='tight')




#%%
# original # fixed gcm temp in 2020 and 2021
np.mean(glue_df_annual_hypolimnetic_ave_his['50%'])#5.118056494914366# 5.371846482897608
np.mean(glue_df_annual_hypolimnetic_ave_rcp26['50%'])#7.009871810216667# 7.960074150018018
np.mean(glue_df_annual_hypolimnetic_ave_rcp60['50%'])#7.599031745432739# 7.661889247294462
np.mean(glue_df_annual_hypolimnetic_ave_rcp85['50%'])#8.15444840073441#8.680607289244922

np.mean(glue_df_annual_hypolimnetic_ave_his_vartheta['50%'])#3.8503066523454508
np.mean(glue_df_annual_hypolimnetic_ave_rcp26_vartheta['50%'])#5.659131530439698
np.mean(glue_df_annual_hypolimnetic_ave_rcp60_vartheta['50%'])#6.302569680884974
np.mean(glue_df_annual_hypolimnetic_ave_rcp85_vartheta['50%'])#6.840280749721157



#%%anoxic_factor 30 yerars from each scenarios compare 


#Sorting the glue dataframe according to the index (year)

glue_df_annual_hypolimnetic_ave_his=glue_df_annual_hypolimnetic_ave_his.sort_index()

glue_df_annual_hypolimnetic_ave_rcp26=glue_df_annual_hypolimnetic_ave_rcp26.sort_index()

glue_df_annual_hypolimnetic_ave_rcp60=glue_df_annual_hypolimnetic_ave_rcp60.sort_index()

glue_df_annual_hypolimnetic_ave_rcp85=glue_df_annual_hypolimnetic_ave_rcp85.sort_index()





#anormaly 

# baseline [1976-2005]
annual_hypolimnetic_ave_ref=glue_df_annual_hypolimnetic_ave_his[1975 < glue_df_annual_hypolimnetic_ave_his.index]['50%'].mean()

#5.410877320721374
#5.914740063212032


#near future [2030-2059] 

glue_df_annual_hypolimnetic_ave_rcp26[(2029 < glue_df_annual_hypolimnetic_ave_rcp26.index) & (glue_df_annual_hypolimnetic_ave_rcp26.index < 2060)]['50%'].mean()
# 7.072947718287684
# 7.950218353351354
glue_df_annual_hypolimnetic_ave_rcp60[(2029 < glue_df_annual_hypolimnetic_ave_rcp60.index) & (glue_df_annual_hypolimnetic_ave_rcp60.index < 2060)]['50%'].mean()
# 7.156265572954701
# 7.139975067233944

glue_df_annual_hypolimnetic_ave_rcp85[(2029 < glue_df_annual_hypolimnetic_ave_rcp85.index) & (glue_df_annual_hypolimnetic_ave_rcp85.index < 2060)]['50%'].mean()
# 7.630745663516447
# 8.223867040126178
 
#Distant future [2070-2099]

glue_df_annual_hypolimnetic_ave_rcp26[(2069 < glue_df_annual_hypolimnetic_ave_rcp26.index) & (glue_df_annual_hypolimnetic_ave_rcp26.index < 2100)]['50%'].mean()
#7.17035474380281
#8.221226628944514


glue_df_annual_hypolimnetic_ave_rcp60[(2069 < glue_df_annual_hypolimnetic_ave_rcp60.index) & (glue_df_annual_hypolimnetic_ave_rcp60.index < 2100)]['50%'].mean()
#8.781804641713899
#8.984771173520228

glue_df_annual_hypolimnetic_ave_rcp85[(2069 < glue_df_annual_hypolimnetic_ave_rcp85.index) & (glue_df_annual_hypolimnetic_ave_rcp85.index < 2100)]['50%'].mean()
#7.630745663516447
# 10.612461480324987



#%%anoxic_factor_anormaly 
os.chdir('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/')

import matplotlib.pyplot as plt

fig =plt.figure(figsize=(15, 10))
ax= plt.subplot(111)


ax=plt.fill_between(glue_df_annual_hypolimnetic_ave_his[1975 < glue_df_annual_hypolimnetic_ave_his.index].index.astype(float),
                      glue_df_annual_hypolimnetic_ave_his[1975 < glue_df_annual_hypolimnetic_ave_his.index]['5%'].astype(float) - annual_hypolimnetic_ave_ref,
                      glue_df_annual_hypolimnetic_ave_his[1975 < glue_df_annual_hypolimnetic_ave_his.index ]['95%'].astype(float) - annual_hypolimnetic_ave_ref,
                      color='grey', alpha=0.2, label='His 90% CI')


ax=plt.plot(glue_df_annual_hypolimnetic_ave_his[(1975 < glue_df_annual_hypolimnetic_ave_his.index) ].index.astype(float),
            glue_df_annual_hypolimnetic_ave_his[(1975 < glue_df_annual_hypolimnetic_ave_his.index)]['50%'].astype(float) - annual_hypolimnetic_ave_ref,
            'k', label='His median', alpha=0.9, linewidth=3   )

ax=plt.fill_between(glue_df_annual_hypolimnetic_ave_rcp26.index.astype(float), glue_df_annual_hypolimnetic_ave_rcp26['5%'].astype(float)-annual_hypolimnetic_ave_ref, glue_df_annual_hypolimnetic_ave_rcp26['95%'].astype(float)-annual_hypolimnetic_ave_ref, color='darkgreen', alpha=0.3 ,  label= 'RCP6.0 90% CI')
ax=plt.plot(glue_df_annual_hypolimnetic_ave_rcp26.index.astype(float), glue_df_annual_hypolimnetic_ave_rcp26['50%'].astype(float)-annual_hypolimnetic_ave_ref, 'darkgreen', label='RCP6.0 median', alpha=0.9, linewidth=3  )
                      
                     
ax=plt.fill_between(glue_df_annual_hypolimnetic_ave_rcp60.index.astype(float), glue_df_annual_hypolimnetic_ave_rcp60['5%'].astype(float)-annual_hypolimnetic_ave_ref, glue_df_annual_hypolimnetic_ave_rcp60['95%'].astype(float)-annual_hypolimnetic_ave_ref, color='b', alpha=0.27 ,  label= 'RCP6.0 90% CI')
ax=plt.plot(glue_df_annual_hypolimnetic_ave_rcp60.index.astype(float), glue_df_annual_hypolimnetic_ave_rcp60['50%'].astype(float)-annual_hypolimnetic_ave_ref, 'b', label='RCP6.0 median', alpha=0.9, linewidth=3  )

ax=plt.fill_between(glue_df_annual_hypolimnetic_ave_rcp85.index.astype(float), glue_df_annual_hypolimnetic_ave_rcp85['5%'].astype(float)-annual_hypolimnetic_ave_ref, glue_df_annual_hypolimnetic_ave_rcp85['95%'].astype(float)-annual_hypolimnetic_ave_ref, color='r', alpha=0.2 ,  label= 'RCP8.5 90% CI')
ax=plt.plot(glue_df_annual_hypolimnetic_ave_rcp85.index.astype(float), glue_df_annual_hypolimnetic_ave_rcp85['50%'].astype(float)-annual_hypolimnetic_ave_ref, 'r', label='RCP8.5 median', alpha=0.9, linewidth=3  )

ax=plt.ylabel('Anormaly of anoxic factor [d year$^{-1}$]' , fontsize=26)
ax=plt.xlabel('Year' , fontsize=26)
ax=plt.yticks(fontsize= 22)
ax=plt.xticks(rotation=45 , fontsize=22)
ax=plt.legend(bbox_to_anchor=(0.7, -0.2), fontsize=22)  
fig.savefig("GLUE_Timeseries_anoxic_factor_anormaly_16combinationJaJv_ave_obs_4models_4scenarios.png",  dpi=300, bbox_inches='tight')


