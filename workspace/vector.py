import pandas as pd
import numpy as np
import streamlit as st
import math

#自作のjsonファイルからデータフレームを出力する関数
import get_jsonFile

def compute_finger_vectors(landmark_df):

    #得たデータを格納する配列を生成
    vectors = []
    vector_lengths = []

    window_width = st.session_state.window_width
    window_height = st.session_state.window_height

    index_finger_data = {"vector" : [], "vector_length" : []}
    middle_finger_data = {"vector" : [], "vector_length" : []}
    ring_finger_data = {"vector" : [], "vector_length" : []}
    pinky_data = {"vector" : [], "vector_length" : []}

    #データがない場合は早期リターン
    if landmark_df.empty:
        return None

   #index_finger
    landmark_data_5 = landmark_df.iloc[5]
    landmark_data_6 = landmark_df.iloc[6]

    x5, y5, z5 = landmark_data_5['landmark_x'],landmark_data_5['landmark_y'], landmark_data_5['landmark_z']
    x6, y6, z6 = landmark_data_6['landmark_x'],landmark_data_6['landmark_y'], landmark_data_6['landmark_z']

    #middle_finger
    landmark_data_9 = landmark_df.iloc[9]
    landmark_data_10 = landmark_df.iloc[10]

    x9, y9, z9 = landmark_data_9['landmark_x'],landmark_data_9['landmark_y'], landmark_data_9['landmark_z']
    x10, y10, z10 = landmark_data_10['landmark_x'],landmark_data_10['landmark_y'], landmark_data_10['landmark_z']

    #ring_finger
    landmark_data_13 = landmark_df.iloc[13]
    landmark_data_14 = landmark_df.iloc[14]

    x13, y13, z13 = landmark_data_13['landmark_x'],landmark_data_13['landmark_y'], landmark_data_13['landmark_z']
    x14, y14, z14 = landmark_data_14['landmark_x'],landmark_data_14['landmark_y'], landmark_data_14['landmark_z']

    #pinky_finger
    landmark_data_17 = landmark_df.iloc[17]
    landmark_data_18 = landmark_df.iloc[18]

    x17, y17, z17 = landmark_data_17['landmark_x'],landmark_data_17['landmark_y'], landmark_data_17['landmark_z']
    x18, y18, z18 = landmark_data_18['landmark_x'],landmark_data_18['landmark_y'], landmark_data_18['landmark_z']


    # 各指のベクトルを計算
    index_vector = np.array([x6 * window_width - x5 * window_width,  y6 * window_height - y5 * window_height])
    middle_vector = np.array([x10 * window_width - x9 * window_width,  y10 * window_height - y9 * window_height])
    ring_vector = np.array([x14 * window_width - x13 * window_width, y14 * window_height - y13 * window_height])
    pinky_vector = np.array([x18 * window_width - x17 * window_width, y18 * window_height - y17 * window_height])

    # ベクトルの大きさを計算
    index_length = np.linalg.norm(index_vector)
    middle_length = np.linalg.norm(middle_vector)
    ring_length = np.linalg.norm(ring_vector)
    pinky_length = np.linalg.norm(pinky_vector)

    # 各指のベクトルと大きさを格納
    index_data = {"vector": [index_vector], "vector_length": [index_length]}
    middle_data = {"vector": [middle_vector], "vector_length": [middle_length]}
    ring_data = {"vector": [ring_vector], "vector_length": [ring_length]}
    pinky_data = {"vector": [pinky_vector], "vector_length": [pinky_length]}

    st.write(ring_data["vector"])
    st.write(ring_data["vector_length"])
    
    return ring_data
