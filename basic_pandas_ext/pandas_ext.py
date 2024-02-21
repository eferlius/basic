"""
date: 2022-12-22 15:03:12
note: extension of pandas operations
"""
import numpy as np
import pandas as pd
import datetime
import time

def this_moment(fmt = '%Y-%m-%d %H-%M-%S'):
    return datetime.datetime.fromtimestamp(time.time()).strftime(fmt)

def crop_df_wrt_column(df, start_val, end_val = np.nan, column_name = 'time', 
                 reset_zero = False, start_from_zero = False, reset_index = False):
    """
    Returns a copy of the dataframe where time is between start_val and end_val, 
    by default, keeps the original time.
    If reset_zero, the time column is decremented of start_val.
    As a result, the time column starts from 0 if start_val corresponds to the 
    first element, otherwise from slightly more than 0.
    If start_from_zero, the time column is decremented of the first element.
    As a result, the time column starts from 0.
    If reset_index, the indexes start from 0, otherwise the original indexing is kept
    

    Parameters
    ----------
    df : pandas dataframe
        The one to be cropped.
    start_val : float
        starting time for cropping.
    end_val : float, optional
        ending time for cropping. 
        The default is np.nan, which means no cutting of the end.
    column_name : string, optional
        name of the column containing the time. The default is 'time'.
    reset_zero : bool
        if True, the time starts from start_val.
        if False, the original time is kept.
        The default is False.
    start_from_zero : bool
        if True, the time starts from start_val.
        if False, the original time is kept.
        The default is False.
    reset_index : bool
        if True, the indexes start from 0
        if False, the original indexing is kept
        The default is False.

    Returns
    -------
    df_cropped : pandas dataframe
        The one with time between start_val and end_val.

    """
    if start_val < 0:
        start_val = np.max(df[column_name].values)+start_val
    if not np.isnan(end_val): # if end_val is defined
        if start_val < 0:
            end_val = np.max(df[column_name].values)+end_val

    df_cropped = df.copy()

    # consider only the part between start_val and end_val
    if not np.isnan(end_val): # if end_val is defined
        df_cropped = df_cropped[df_cropped[column_name] <= end_val]
    df_cropped = df_cropped[df_cropped[column_name] >= start_val]

    # the initial moment is start_val
    if reset_zero:
        df_cropped[column_name] -= start_val

    # the initial moment is the first available on the time array
    if start_from_zero:
        df_cropped[column_name] -= df_cropped[column_name].iloc[0]

    if reset_index:
        df_cropped.reset_index(drop = True, inplace = True)

    return df_cropped

def duplicate_first_n_cols(df, n):
    # Select first 5 columns of DataFrame
    first_n_cols = df.iloc[:, :n]
    # Create copy of first 5 columns
    first_n_cols_copy = first_n_cols.copy()
    return first_n_cols_copy

def add_array_as_column(df, arr, col_name, dec_round = 5):    
    df_add = pd.DataFrame({col_name: np.where(np.isnan(arr), arr, np.round(arr, dec_round))})
    df = pd.concat([df, df_add], axis = 1)
    return df

def print_description_in_txt(df, filename = 'this moment'):
    if filename == 'this moment':
        filename = '{}.txt'.format(this_moment())
    description = df.describe()
    with open(filename, "w") as file:
        # Write to the file
        file.write(description.to_string())
    return description

def print_description_in_csv(df, filename = 'this moment'):
    if filename == 'this moment':
        filename = '{}.csv'.format(this_moment())
    description = df.describe()
    description.to_csv(filename)
    return description