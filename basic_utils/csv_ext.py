import csv
import os

def write_row_csv(CSVfile, newRow, mode = 'a', delimiter = ','):
    '''
    Writes newRow in the csv file specified in CSVfile

    Parameters
    ----------
    CSVfile : string
        complete path to the csv file.
    newRow : list
        row to be added.

    Returns
    -------
    None.

    '''
    # eventually create the csv folder
    os.makedirs(os.path.split(CSVfile)[0], exist_ok= True)
    f = open(CSVfile, mode, encoding='UTF8', newline='')
    writer = csv.writer(f,  delimiter = delimiter)
    writer.writerow(newRow)
    f.close()

def write_rows_csv(CSVfile, rows, mode = 'a', delimiter = ','):
    '''
    Writes newRow in the csv file specified in CSVfile

    Parameters
    ----------
    CSVfile : string
        complete path to the csv file.
    newRow : list
        row to be added.

    Returns
    -------
    None.

    '''
    # eventually create the csv folder
    os.makedirs(os.path.split(CSVfile)[0], exist_ok= True)
    f = open(CSVfile, mode, encoding='UTF8', newline='')
    writer = csv.writer(f, delimiter = delimiter)
    writer.writerows(rows)
    f.close()