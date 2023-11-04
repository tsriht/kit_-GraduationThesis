
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.widgets import Slider
import numpy as np
import pandas as pd
import json
import streamlit as st

#自作のjsonを読み込んでぐる関数のインポート
import get_jsonFile


def plotHand(landmark_df):
    #jsonファイルを関数で取得。


    #プロットした3D画像を描画するための空コンテナの定義
    output_plot_container = st.empty()

    #手首, 各指の付け根から指先のデータの用意
    wrist_data = landmark_df[0:1]
    thumb_data = landmark_df[1:5]
    index_finger_data = landmark_df[5:9]
    middle_finger_data = landmark_df[9:13]
    ring_finger_data = landmark_df[13:17]
    pinky_data = landmark_df[17:21]

    lms_5_data = landmark_df[5:6]
    lms_9_data = landmark_df[9:10]
    lms_13_data = landmark_df[13:14]
    lms_17_data = landmark_df[17:18]

    #手首までのデータが必要なものにwrist_dataを追加
    thumb_data =  pd.concat([wrist_data, thumb_data])
    index_finger_data = pd.concat([wrist_data, index_finger_data])
    pinky_data = pd.concat([wrist_data, pinky_data])

    #手の根本のデータを結合
    root_hand_data = pd.concat([lms_5_data, lms_9_data, lms_13_data, lms_17_data])

    #データを代入
    wrist_x = wrist_data['landmark_x']
    wrist_y = wrist_data['landmark_y']
    wrist_z = wrist_data['landmark_z']

    thumb_x = thumb_data['landmark_x']
    thumb_y = thumb_data['landmark_y']
    thumb_z = thumb_data['landmark_z']

    index_finger_x = index_finger_data['landmark_x']
    index_finger_y = index_finger_data['landmark_y']
    index_finger_z = index_finger_data['landmark_z']

    middle_finger_x = middle_finger_data['landmark_x']
    middle_finger_y = middle_finger_data['landmark_y']
    middle_finger_z = middle_finger_data['landmark_z']

    ring_finger_x = ring_finger_data['landmark_x']
    ring_finger_y = ring_finger_data['landmark_y']
    ring_finger_z = ring_finger_data['landmark_z']

    pinky_x = pinky_data['landmark_x']
    pinky_y = pinky_data['landmark_y']
    pinky_z = pinky_data['landmark_z']

    root_x = root_hand_data['landmark_x']
    root_y = root_hand_data['landmark_y']
    root_z = root_hand_data['landmark_z']

    #グラフの枠を作成
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')


    # 軸ラベル
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")

    # 散布図の作成
    ax.plot(thumb_x, thumb_y, thumb_z, "o-", color="#FF66CC", ms=4, mew=0.5)
    ax.plot(index_finger_x, index_finger_y, index_finger_z, "o-", color="#0066FF", ms=4, mew=0.5)
    ax.plot(middle_finger_x, middle_finger_y, middle_finger_z, "o-", color="#33CC66", ms=4, mew=0.5)
    ax.plot(ring_finger_x, ring_finger_y, ring_finger_z, "o-", color="#9999FF", ms=4, mew=0.5)
    ax.plot(pinky_x, pinky_y, pinky_z, "o-", color="#FF3366", ms=4, mew=0.5)
    ax.plot(root_x, root_y, root_z, "o-", color="#CC99FF", ms=4, mew=0.5)

    #手の向きの調整のためにz軸のラベルを反転
    # ax.set_zlim(ax.get_zlim()[::-1])

    #後からFigureを見る角度を変更するため上下左右の値を持たせる。
    #一応plot_stateがTruのときのみ出現させている。
    if st.session_state.plot_state == True:
        st.sidebar.header("perspective")
        elevation = st.sidebar.slider("vertical", 0, 180, 90)
        azimuth = st.sidebar.slider("horizontal", 0, 360, 90)
        ax.view_init(elevation, azimuth)

        output_plot_container = st.empty()
        output_plot_container.pyplot(fig)

    return 0