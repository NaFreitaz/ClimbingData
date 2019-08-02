from all_comps import requests, pd, np, competition_overview_df
from support_functions import climbing_category, competition_stage

for comp in competition_overview_df.iterrows():
    base_url = 'http://egw.ifsc-climbing.org/egw/ranking/json.php?'
    competition_id = comp[1]['compId']
    # competition_id = '7923'

    # if competition_overview_df[competition_overview_df['compId'] == competition_id]['isBoulderingComp'].any() == 1:
    if comp[1]['isBoulderingComp'] == 1:
        for category in ['5', '6']:
            df_category = climbing_category(category)

            for stage in ['0', '1', '2', '3']:
                df_stage = competition_stage(stage)

                url = base_url + 'comp=' + competition_id + '&cat=' + category + '&route=' + stage
                comp_json = requests.get(url).json()

                # Adding stage information to main competition overview dataframe
                competition_overview_df.loc[competition_overview_df['compId'] == competition_id, 'isoOpen' + df_stage + df_category] = comp_json.get('route_iso_open')
                competition_overview_df.loc[competition_overview_df['compId'] == competition_id, 'isoClose' + df_stage + df_category] = comp_json.get('route_iso_close')
                competition_overview_df.loc[competition_overview_df['compId'] == competition_id, 'stageStart' + df_stage + df_category] = comp_json.get('route_start')
                competition_overview_df.loc[competition_overview_df['compId'] == competition_id, 'numProblems' + df_stage + df_category] = comp_json.get('route_num_problems')
                competition_overview_df.loc[competition_overview_df['compId'] == competition_id, 'climbingTime' + df_stage + df_category] = comp_json.get('route_climbing_time')

print(competition_overview_df)
# comp_json


def get_stage_results(url_json):
    new_stage_rows = []
    for climber in comp_json['participants']:
        new_comp_stage = dict()

        # This same information needs to be in the row for every climber
        new_comp_stage.update({
            'compId': comp_json.get('WetId'),
            'category': climbing_category(comp_json.get('GrpId')),
            'stage': competition_stage(comp_json['route_order'])
        })

        # Get climber's results for this stage
        new_comp_stage.update({
            'climberID': climber.get('PerId'),
            'startOrder': climber.get('start_order'),
            'rankAfterStage' : climber.get('result_rank'),
            'boulder1': climber.get('boulder1'),
            'boulder2': climber.get('boulder2'),
            'boulder3': climber.get('boulder3'),
            'boulder4': climber.get('boulder4'),
            'boulder5': climber.get('boulder5'),
        })

        # Append new row dictionary, (representing a stage of a comp), in the new_stage_rows list
        new_stage_rows.append(new_comp_stage)

    # Return new rows to insert in dataframe
    return new_stage_rows
