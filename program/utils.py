import os
import sys
import logging
import pandas as pd

from logging import debug, info, warning

class FindAndReadInputFile():
    '''
    Helper class to identify input file either from a user input
    filepath or from most recent file found in inputs folder
    '''
    def __init__(self, filename):
        #inilialize blank dataframe, to return, will be overwritten later
        self.df = pd.DataFrame()

        #locate input file folder
        input_dir = os.path.join(os.getcwd(), "Inputs")
        info('Processing input files from {}'.format(input_dir))

        if not os.path.exists(input_dir):
            #Verify that input folder is a valid filepath
            info('ERROR: No such input directory exists.')
            sys.exit(0)
            
        if filename:
            #if there was a specific filename sent to the command line the read in file
            info('Filename ({}) sent as argument'.format(filename))

        else:
            #If there wasnt a specific filename sent to the command line then auto find it
            info('No filename sent as argument, searching for input files')
            input_files = os.listdir(input_dir)
            
            # Filter to only those files that have the required extension
            input_files = [k for k in input_files if '.xlsx' in k]
            info('Found {} files in folder: {}'
                .format(len(input_files), input_files))

            most_recent = 0
            for input_file in input_files:
                date = int(input_file[10:18])
                if date > most_recent:
                    filename = input_file
                
        file_dir = os.path.join(input_dir, filename)
        self.df = pd.read_excel(file_dir, "JRADBase")
        info('input file ({}) processed and read in'
            .format(file_dir))

        #Delete the first 6 columns, as they contain metadata that we will reestablish later
        self.df = self.df.drop(self.df.columns[0:7], axis=1)

        