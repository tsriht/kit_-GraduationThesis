import json
import pandas as pd

def get_json():
    with open('json/landmark.json') as  f:
        landmark_data = json.load(f)

    #利用データ
    landmark_x     = landmark_data['x']
    landmark_y     = landmark_data['y']
    landmark_z     = landmark_data['z']
    # landmark_z = [-z for z in landmark_data['z']]
    landmark_index = landmark_data['index']

    landmark_df = pd.DataFrame({'landmark_x': landmark_x, 'landmark_y': landmark_y,'landmark_z': landmark_z}, index=landmark_index)

    return landmark_df

