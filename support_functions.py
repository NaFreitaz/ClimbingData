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

# Looking up the competition stage, whether for internal use or external
def competition_stage(stage, intext=1):
    external_stages = {
        '-1': 'General result',
        '0': '1. Qualification',
        '1': '2. Qualification',
        '2': 'Semi-Final',
        '3': 'Final'
    }
    df_stages = {
        '0': 'Q1',
        '1': 'Q2',
        '2': 'SF',
        '3': 'F'
    }
    return df_stages.get(stage, 'Other') if intext == 1 else external_stages.get(stage, 'Other')
