#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
import datetime
import numpy as np
import pandas as pd


# In[2]:


# Make a category lookup
def climbing_category(cat, intext=1):
    external_categories = {
        '1': 'menLead',
        '2': 'womenLead',
        '5': 'womenBouldering',
        '6': 'menBouldering',
        '23': 'menSpeed',
        '24': 'womenSpeed'
    }
    df_categories = {
        '1': 'Men',
        '2': 'Women',
        '5': 'Women',
        '6': 'Men',
        '23': 'Men',
        '24': 'Women'
    }
    return df_categories.get(cat, 'Men') if intext == 1 else external_categories.get(cat, 'otherCategory')


# In[3]:


# Get overall information for all competitions in a season
def add_season_competitions(url_json):
    new_rows = []
    for comp in url_json['competitions']:
        new_comp = dict()
        
        # Add a dictionary with the information for each comp
        new_comp.update({
            'compId': comp.get('WetId'),
            'longCompName': comp.get('name'),
            'shortCompName': comp.get('short'),
            'hostNation': comp.get('host_nation'),
            'openComp': comp.get('open_comp'),
            'dateStart': comp.get('date'),
            'dateEnd': comp.get('date_end')
        })

        # Get all categories in this competition
        for cat in comp.get('cats'):
            new_comp.update({climbing_category(cat['GrpId'],2): 1})

        # Append new row dictionary, (representing a comp), in the new_rows list
        new_rows.append(new_comp)  
    
    # Return all new rows for the season
    return new_rows


# In[4]:


# Today's date
today = datetime.datetime.now()

# Creating a competition overview dataframe
competition_overview_df = pd.DataFrame()

# Generate the link for all WCs and get all comp ids
for season in range(int(str(today.year)[-2:]) + 1):
    
    # Generating URLs for world cups since 2000 until this year
    url = 'http://egw.ifsc-climbing.org/egw/ranking/json.php?type=event&year='
    url = url + str(today.year - season)
    season_json = requests.get(url).json()
    
    # Getting all information for a dataframe with all comp overall figures
    competition_overview_df = competition_overview_df.append(add_season_competitions(season_json), ignore_index=True)
    
    # Adding what type of competitions are taking place
    competition_overview_df['isBoulderingComp'] = np.where(
        (competition_overview_df['menBouldering'] == 1) | 
        (competition_overview_df['womenBouldering'] == 1), 1, 0)
    
    competition_overview_df['isLeadComp'] = np.where(
        (competition_overview_df['menLead'] == 1) | 
        (competition_overview_df['womenLead'] == 1), 1, 0)
    
    competition_overview_df['isSpeedComp'] = np.where(
        (competition_overview_df['menSpeed'] == 1) | 
        (competition_overview_df['womenSpeed'] == 1), 1, 0)
    
competition_overview_df

