import mediapipe as mp
import cv2
import streamlit as st
import datetime



def webcam_handTracking(cap_file, name):
    landmark_array = []

    dt_now = datetime.datetime.now()


    #各種描画したいものに合わせて空オブジェクトを生成
    image_container = st.empty()
    text_container = st.empty()


    #mediapipe內部のソリューションを扱いやすいように定義
    mp_hands = mp.solutions.hands
    mp_drawing = mp.solutions.drawing_utils
    mesh_drawing_spec = mp_drawing.DrawingSpec(thickness=2, color=(0, 128, 0))
    mark_drawing_spec = mp_drawing.DrawingSpec(thickness=3, circle_radius=3, color=(0,0,255))

    with mp_hands.Hands(
        max_num_hands=1,
        min_detection_confidence=0.5,
        static_image_mode=False) as hands_detection:

        while cap_file.isOpened():
            success, image = cap_file.read()
            if not success:
                continue

            image = cv2.flip(image,1)
            rgb_image = cv2.cvtColor( image, cv2.COLOR_BGR2RGB)
            width = rgb_image.shape[1]
            height = rgb_image.shape[0]

            #processにかけてhand_detectionを開始
            results = hands_detection.process( rgb_image )

            if not results.multi_hand_landmarks:

                #手をかざすように促すテキスト描画
                text_container.write('<span style="color:#33FFCC;">' + 'please hold your hand' + '</span>',unsafe_allow_html=True)

            else:

                #手は判定できるのでDetectionボタンを押すように促すテキスト描画
                if st.session_state['detection_state'] == False:
                    text_container.write('<span style="color:#FF6699;">' + 'push Detection button' + '</span>',unsafe_allow_html=True)

                for hand_landmarks in results.multi_hand_landmarks:
                    #描画するための初期値を宣言
                    mp_drawing.draw_landmarks(
                        image = image,
                        landmark_list = hand_landmarks,
                        connections = mp_hands.HAND_CONNECTIONS,
                        landmark_drawing_spec = mark_drawing_spec,
                        connection_drawing_spec = mesh_drawing_spec)

                    #############################################################################

                    #handTrackingが回っているときにDetectionボタンを押したとき一度だけループ
                    # index , landmark, annotated_imageを取得
                    if st.session_state['detection_state'] == True:

                        #trueになったときのimageをコピー
                        annotated_image = image

                        print( 'deteciton start at' + ' ' + dt_now.strftime('%Y年%m月%d日 %H:%M:%S\n'))
                        for ix, lm in enumerate(hand_landmarks.landmark):

                            gx = lm.x
                            gy = lm.y
                            gz = lm.z

                            print( f'ix : {ix}' )
                            print( f'x : {gx}' )
                            print( f'y : {gy}' )
                            print( f'z : {gz} \n' )

                            landmark_array.append(ix)
                            landmark_array.append(gx)
                            landmark_array.append(gy)
                            landmark_array.append(gz)

                            #loopを防ぐために手のすべての情報を取得したら止める
                            if ix == 20:
                                st.session_state['detection_state'] = False

                                st.session_state.date_time = dt_now.strftime('%Y年%m月%d日 %H:%M:%S') #terminalで実行日時を表示するために現在時刻を取得
                                results_img_path = 'results/sample.jpg'
                                cv2.imwrite(results_img_path, annotated_image)

                        print('...done')
                    ############################################################################


            #上のfor文で取得してきたデータを描画したり配列に格納したりするスコープ
            output_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            image_container.image( output_image )

            #取得したデータ群をここでsession_stateに渡す。
            st.session_state['index_array'] = landmark_array
            st.session_state['window_width'] = width
            st.session_state['window_height'] = height


    cap_file.release()

    return 0
