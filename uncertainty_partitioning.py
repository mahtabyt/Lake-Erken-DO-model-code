# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 15:53:47 2024

@author: mahta
"""


import numpy as np
import pandas as pd
import pingouin as pg 

#pip install pingouin

# input dataframe of this function is before applying the GLUE method 

def annova_uncertainity(df, num_parm=16):
    
    index_years=df.index
    # MultiIndex for columns
    gcms_models = ['GFDL', 'Hadgem', 'Ipsl', 'Miroc']
    parameters = list(map(str, range(num_parm)))
    columns_multiindex = pd.MultiIndex.from_product([gcms_models, parameters], names=['GCMS_Model', 'Parameter'])
    # Create a new DataFrame with the MultiIndex columns
    df_multiindex = pd.DataFrame(columns=columns_multiindex, index=index_years)
    # Assign the values from the original DataFrame to the new DataFrame
    df_multiindex[df_multiindex.columns] = df.values
    # Resetting the index to make it part of the data
    df_multiindex_reset = df_multiindex.reset_index()

    # Melting the DataFrame
    melted_df = pd.melt(df_multiindex_reset, id_vars='Datetime', var_name=['GCMs', 'param'])
    #previously it was id_vars='index'
    #melted_df = pd.melt(df_multiindex_reset, id_vars='index',var_name=['GCMs', 'param'], value_name='annual_do')



    # Renaming the columns
    melted_df.columns = ['year', 'GCMs', 'param', 'value']
    # Assuming melted_df is your initial DataFrame
    melted_df= melted_df.set_index('year')

    # Group by index and perform operations
    grouped_df= melted_df.groupby(melted_df.index)
    
    # Initialize the result DataFrame
    all_year_anova = pd.DataFrame([], columns=['GCMs', 'param', 'interaction', 'GCMs/param', 'year'])
    
    
    
    # Iterate through groups
    for i, group_df in grouped_df:
        annual_anova = group_df.anova(dv="value", between=["GCMs", "param"])
        
        annova_ss_percentage = 100 * (annual_anova['SS'] / sum(annual_anova['SS']))
        
        ratio_uncer = (annova_ss_percentage[0] / annova_ss_percentage[1]).round(3)
        
        annova_ss_percentage[3] = ratio_uncer
        annova_ss_percentage[4] = i
        
        data = np.array(annova_ss_percentage)
        data_df = pd.DataFrame(data, index=['GCMs', 'param', 'interaction', 'GCMs/param', 'year']).T
        all_year_anova = pd.concat([all_year_anova, data_df], axis=0, ignore_index=True)
    
    return(all_year_anova)# mean and std should be interesting to be mentioned 
    
    



