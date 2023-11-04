import streamlit as st

#session_stateの初期化。
# streamlitでは変数の値を保持できないので session_state の中で管理することで
# タブがリロードされても値を保持できるようになる

def sessionState():
    #ボタン類のsession_stateの初期化
    if 'run_state' not in st.session_state:
        st.session_state['run_state'] = False
    if 'detection_state' not in  st.session_state:
        st.session_state['detection_state'] = False
    if 'plot_state' not in st.session_state:
        st.session_state['plot_state'] = False
    if 'measure_state' not in st.session_state:
        st.session_state['measure_state'] = False
    #画面の幅を保持する
    if 'window_width' not in st.session_state:
        st.session_state['window_width'] = None
    if 'window_height' not in st.session_state:
        st.session_state['window_height'] = None
    if 'user_name' not in st.session_state:
        st.session_state['user_name'] = None    #名前を保持する
    if 'date_time' not in st.session_state:
        st.session_state['date_time'] = None   #detectionした瞬間の日付を取得
    # 指のランドマークデータ類を格納する配列, 変数を容易
    if 'index_array' not in st.session_state:
        st.session_state['index_array'] = []
    if 'midpoint_x' not in st.session_state:
        st.session_state['midpoint_x'] = None
    if 'midpoint_y' not in st.session_state:
        st.session_state['midpoint_y'] = None
    if 'midpoint_z' not in st.session_state:
        st.session_state['midpoint_z'] = None
