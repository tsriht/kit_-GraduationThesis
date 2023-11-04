#手の姿勢推定についてのモジュール
import mediapipe as mp
import cv2
#GUIアプリを走らせるためのモジュール
import streamlit as st
#便利機能たち
import pandas as pd
import numpy as np
import json
from PIL import Image
import datetime
#自作の関数のインポート
import handTracking
import session
import plot
import get_jsonFile
import vector
import button
import midpoint
# import sample

# #handTrackingに関する関数の初期化
cap_file = cv2.VideoCapture(0)
img_path = 'img/'


def input_name():
    name = st.sidebar.text_input('name', '')
    st.session_state.user_name = name
    # if not name:
    #     st.warning('Please input a name.')
    #     st.stop()
    # st.session_state.user_name

    return name


#select modeの部品用の関数
def sidebar_param():

    selectList = ['Use WebCamera', 'Use Photo', 'Use CSV']
    imgExtansionList = ['jpg', 'jpeg', 'png']

    mode = st.sidebar.selectbox('select mode', selectList)
    uploaded_mv_file = None #指定された動画を保存する
    uploaded_img_file = None #指定された画像を保存する

    if  mode == 'Use Photo':
        st.sidebar.text("""
        写真を使用する場合は
        こちらで写真をアップロードしてください
        """)
        uploaded_img_file = st.sidebar.file_uploader("image file upload", type=imgExtansionList)
        if uploaded_img_file is not None:
            st.sidebar.image(uploaded_img_file)

    return mode, uploaded_img_file


#上のsidebar_param()で受け取った値をもとに写真、映像などの入力先をcap_fileとして出力できる関数
def read_path(img_path, uploaded_img_file):
    img_file_path = None
    cap_file = None #初期値をNoneにリセット

    if  mode == 'Use Photo':
        if uploaded_img_file == None :
             return

        img = Image.open(uploaded_img_file)
        img_file_path = img_path + uploaded_img_file.name
        img.save(img_file_path)
        cap_file = img_file_path
        # print(img_file_path)

    else:
        cap_file = cv2.VideoCapture(0)

    return cap_file





#STARTボタンを押したとき(ここの処理はsessionState()が担っている)のmodeをみて処理を変更する関数(特に弄ることはない)
def runHandTracking(mode):
    apology = 'Sorry... This mode is not ready.<br>Please select Use WebCamera.'

    if st.session_state['run_state'] == True:

        if mode == 'Use Photo':
            if uploaded_img_file is None:
                st.text('画像をアップロードしてください')
            else:
                st.write('<span style="color:#CC99FF;">' + apology + '</span>',unsafe_allow_html=True)
                # handTracking.img_handTracking(cap_file)

        else:
            handTracking.webcam_handTracking(cap_file, name)

    return 0


#handTracking()內部で取り出した配列をわかりやすいようにソートする関数
def sortData():
    index_data  = st.session_state.index_array[0::4]
    landmark_x = st.session_state.index_array[1::4]
    landmark_y = st.session_state.index_array[2::4]
    landmark_z = st.session_state.index_array[3::4]

    landmark_data = {'index' : index_data, 'x' : landmark_x, 'y' : landmark_y, 'z' : landmark_z}

    with open('json/landmark.json', 'w') as f:
        json.dump(landmark_data, f, ensure_ascii=False, indent=4)

    return landmark_data

def reDetection(mode):
    if mode == 'Use CSV':
        uploaded_csv_path = st.sidebar.file_uploader("csv file", type='csv')
        if uploaded_csv_path is not None:
            file_path = 'results/result_landmark/' + f'{uploaded_csv_path.name}'
            st.sidebar.text(file_path)






if __name__ == "__main__":

    #sidebar, main両方のsession_stateを更新するための関数をここで呼び出し
    session.sessionState()

#  sidebar ###############################################################
    #わかりやすいようにタイトルとインプットの明示
    st.sidebar.title('各種設定')

    #trackingの開始、終了
    st.sidebar.text('measurement')
    button_run, button_stop = button.sidebar_button()

    #利用するユーザーの名前を入力
    name = input_name()

    #計測するモードを選択
    mode, uploaded_img_file = sidebar_param()

    cap_file = read_path(img_path, uploaded_img_file)

    reDetection(mode)

#######################################################################


#  main  ##################################################################

    st.header('Detection HandPose  App')

    #main画面に必要なボタンを呼び出し
    button_detection, button_plot, button_delete = button.main_button()

    #ここでhandTrackingを回す位置を個々で決めている。
    selected_image = runHandTracking(mode)

    #handTrackingで受け取ったデータをソート
    landmark_data = sortData()

    #landmark_dfというデータフレームで所持
    landmark_df = get_jsonFile.get_json()

    #並べ替えたデータをもとに３D プロットを生成。
    plot.plotHand(landmark_df)

    # ダウンロードボタンを表示
    button.download_button(landmark_df, name, mode)

    #データからランドマーク間のxy平面のベクトルを取得。
    # vector.compute_finger_vectors(landmark_df)

    #指のmidpointを抽出
    midpoint.get_midpint(landmark_df)

    #確認系の関数。
    #index_arrayに数値が渡ったら描画
    if not st.session_state.index_array == []:
        st.sidebar.text("measurement")
        st.sidebar.dataframe(landmark_df)

    #確認のために表示。本番はいらない
    # st.session_state.index_array

########################################################################