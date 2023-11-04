import pandas as pd
import numpy as np
import streamlit as st

def get_midpint(landmark_df):
    #データがない場合は早期リターン
    if landmark_df.empty:
        return None

    width = st.session_state.window_width
    height = st.session_state.window_height

    landmark_data_13 = landmark_df.iloc[13]
    landmark_data_14 = landmark_df.iloc[14]

    x13, y13, z13 = landmark_data_13['landmark_x'],landmark_data_13['landmark_y'],\
        landmark_data_13['landmark_z']

    x14, y14, z14 = landmark_data_14['landmark_x'],landmark_data_14['landmark_y'], \
        landmark_data_14['landmark_z']

    xdiff = (x14 - x13)/2
    ydiff = (y14 - y13)/2
    zdiff = (z14 - z13)/2

    midpoint_x = (x13 + xdiff) * width
    midpoint_y = (y13 + ydiff) * height
    midpoint_z = (z13 + zdiff)

    st.session_state['midpoint_x'] = midpoint_x
    st.session_state['midpoint_y'] = midpoint_y
    st.session_state['midpoint_z'] = midpoint_z

    return midpoint_x, midpoint_y, midpoint_z