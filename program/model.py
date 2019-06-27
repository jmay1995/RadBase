# -*- coding: utf-8 -*-
"""
JRAD Show Tracker

Joseph May 
josephmay95@hotmail.com
919-600-4688
"""
import logging

from logging import debug, info, warning
from collections import OrderedDict

from program.params import DROP_COLS

class RadClass():
    '''Overall shell set up for model run'''
    def __init__(self, name, df):
        self.name = name
        self.df = df

        self.shows = self.get_showdata()

    def __str__(self):
        return self.name

    def __repr__(self):
        st = "Model({}, shows{})".format(self.name, self.shows)
        return st

    def get_showdata(self):
        '''
        Process through dataframe and extract show details
        '''
        info('Processing input file to extract show data')
        #Remove uneccesary rows so we can parse show data
        show_df = self.df.head(12).copy(deep = True)

        #drop columns that only contain NA's, from erroneous entry/read in
        show_df.dropna(axis = 1, how = 'all', inplace = True)

        #Delete the unecessary columns that only relate to song based data
        for col in DROP_COLS:
            try: #Put this within exception handling, since the input may vary
                show_df.drop(col, axis = 1, inplace = True)
            except: pass
                # debug('Process_shows: drop column failed for column', col)
                
        #Rotate Data 90 degrees and fix column names
        show_df = show_df.transpose().reset_index()
        show_df.columns = show_df.iloc[0]
        show_df = show_df.reindex(show_df.index.drop(0))
        show_df.dropna(axis = 1, how = 'all', inplace = True)

        #Give each show a unique ID
        show_df = show_df.rename(columns = {'Title': "Show Number"})

        # Loop through rows to extract data for Show objects
        showlist = []
        for _, row in show_df.iterrows():
            showdict = {}
            for col in show_df.columns:
                showdict[col] = row[col]

                # Send dictionary of show data to Show class to create an object
                show = Shows.create_show(showdict)
                showlist.append(show)
            
        del show_df 
        return showlist

class Shows():
    '''Contains show dates, details, and descriptions'''
    def __init__(self):
        pass

    @classmethod
    def create_show(cls, showdict):
        '''
        Classmethod that recieves a dictionary of information and creates
        an object of the show class
        '''
        print(showdict)