import streamlit as st
import datetime

#streamlitのボタンについての関数
#この中でボタンについてのsession_stateの更新も行っている。
def main_button():
    #メイン画面のボタン類の描画処理
    col1, col2, col3 = st.columns(3)
    button_detection = col1.button( 'Detection' )
    button_plot = col2.button('Plot HandPose')
    button_delete = col3.button('Data Delete')
    # button_measure = col4.button('Measure')

    #Detectionボタンの状態遷移
    if button_detection:
        st.session_state['detection_state'] = True

    #Plot HandPoseボタンの状態遷移
    if button_plot:
        st.session_state['plot_state'] = not st.session_state['plot_state']

    #DELETEボタンを押されたとき配列の中身をクリア
    if button_delete:
        st.session_state['index_array'] = []
        st.session_state['plot_state'] = False
        st.session_state['window_width'] = None
        st.session_state['window_height'] = None
        st.session_state['user_name'] = None


    return button_detection, button_plot, button_delete,




def sidebar_button():
        # サイドバーのボタンの描画
    col1, col2, buff = st.sidebar.columns([1,1,1.5])
    button_run = col1.button('START')
    button_stop = col2.button('STOP')

    #STARTボタンの状態遷移
    if button_run:
        st.session_state['run_state'] = True
        st.session_state['index_array'] = []

    #STOPボタンを押したときの状態遷移
    if button_stop == True:
        st.session_state['run_state'] = False
        st.session_state['detection_state'] = False

    return button_run, button_stop



def download_button(landmark_df, name, mode):
    if not mode == 'Use CSV':

        dt_now = datetime.datetime.now()
        file_name = f'{name}{st.session_state.date_time}' + '' + '.csv'

        st.sidebar.download_button(label='Save data', data=landmark_df.to_csv(), file_name=file_name, mime='text/csv')

        return 0