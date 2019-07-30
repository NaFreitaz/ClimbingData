#!/usr/bin/env python
# coding: utf-8

# In[226]:


import requests
import datetime
import pandas as pd

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
    


# In[222]:


# Make a category lookup
def category(cat):
    categories = {
        '1': 'menLead',
        '2': 'womenLead',
        '5': 'womenBouldering',
        '6': 'menBouldering',
        '23': 'menSpeed',
        '24': 'womenSpeed'}
    return categories.get(cat, 'otherCategory')


# In[223]:


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
            new_comp.update({category(cat['GrpId']): 1})

        # Append new row dictionary, (representing a comp), in the new_rows list
        new_rows.append(new_comp)  
    
    # Return all new rows for the season
    return new_rows


# In[80]:


for competition_id in competition_ids:
    url = 'http://egw.ifsc-climbing.org/egw/ranking/json.php?'
    competition_id = competition_ids[-15]
    category = 5
    route = 3
    
    # Adding competition, category and route to url
    url = url + 'comp=' + str(competition_id) + '&cat=' + str(category) + '&route=' + str(route)
    comp_json = requests.get(url).json()
    


# In[85]:


url = 'http://egw.ifsc-climbing.org/egw/ranking/json.php?'
competition_id = competition_ids[-15]
category = 5
route = 3

# competitions = {competition_id:}

# Adding competition, category and route to url
url = url + 'comp=' + str(competition) + '&cat=' + str(category) + '&route=' + str(route)
url
comp_json = requests.get(url).json()
comp_json


# In[86]:


url

