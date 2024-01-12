import pandas as pd

"""
date: 2023-12-07 17:02:21
note: just collection of useful function to be reused
"""

def function_copy_paste_concat_df_for_loop_iteration(i, df_to_add, df_concat):
    if i == 0:
        df_concat = df_to_add.copy()
    else:
        df_concat = pd.concat([df_concat, df_to_add], axis=0)
    return df_concat

def function_copy_paste_apply_map_for_significant_digits(df, decimals):
    format_string = '{'+':.{}f'.format(decimals)+'}'
    df.applymap(format_string.format)