import cv2
import time
import numpy as np
import mediapipe as mp
from openvino.runtime import Core

# -----------------------
# OpenVINO 전신 FP32 모델 로드
# -----------------------
ie = Core()
body_model = ie.read_model("intel/human-pose-estimation-0006/FP32/human-pose-estimation-0006.xml")
body_exec = ie.compile_model(body_model, "CPU")

# 모델 입력 크기 확인
input_layer = body_exec.input(0)
_, _, H, W = input_layer.shape
print(f"Model expects input: {H}x{W}")

# -----------------------
# 전신 전처리 함수
# -----------------------
def preprocess_body(frame):
    img_resized = cv2.resize(frame, (W, H))
    img_input = img_resized.transpose(2, 0, 1)[np.newaxis, :].astype(np.float32)
    return img_input

# -----------------------
# 전신 keypoints 시각화
# -----------------------
def draw_keypoints(img, keypoints, color=(0,255,0)):
    for x, y, conf in keypoints:
        if conf > 0.2:
            cv2.circle(img, (int(x), int(y)), 3, color, -1)

# -----------------------
# 전신 keypoints 추출
# -----------------------
def extract_keypoints(output, orig_w, orig_h):
    heatmaps = output[0]  # shape: [19, H, W]
    keypoints = []
    for i in range(heatmaps.shape[0]):
        hm = heatmaps[i]
        _, conf, _, point = cv2.minMaxLoc(hm)
        x, y = point
        # 모델 출력 크기 -> 원본 프레임 크기 변환
        x = int(x * orig_w / hm.shape[1])
        y = int(y * orig_h / hm.shape[0])
        keypoints.append((x, y, conf))
    return keypoints

# -----------------------
# 손 영역 추출 (손목 기준)
# -----------------------
def get_hand_regions_from_wrist(keypoints):
    left_wrist = keypoints[9]
    right_wrist = keypoints[10]
    hands = []
    for wrist in [left_wrist, right_wrist]:
        if wrist[2] > 0.3:
            x, y = int(wrist[0]), int(wrist[1])
            size = 128
            hands.append((x-size//2, y-size//2, x+size//2, y+size//2))
    return hands

# -----------------------
# MediaPipe Hands 초기화
# -----------------------
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands_detector = mp_hands.Hands(
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5,
    max_num_hands=4
)

# -----------------------
# 카메라 실행 및 FPS 계산
# -----------------------
cap = cv2.VideoCapture(4)
prev_time = 0

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    orig_h, orig_w = frame.shape[:2]

    # -----------------------
    # 전신 키포인트 추론
    # -----------------------
    input_tensor = preprocess_body(frame)
    body_output = body_exec([input_tensor])[body_exec.outputs[0]]
    keypoints = extract_keypoints(body_output, orig_w, orig_h)
    draw_keypoints(frame, keypoints)

    # -----------------------
    # 손 위치 추출
    # -----------------------
    hand_regions = get_hand_regions_from_wrist(keypoints)

    # -----------------------
    # MediaPipe Hands
    # -----------------------
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands_detector.process(frame_rgb)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    # -----------------------
    # FPS 계산 및 표시
    # -----------------------
    curr_time = time.time()
    fps = 1 / (curr_time - prev_time) if prev_time != 0 else 0
    prev_time = curr_time
    cv2.putText(frame, f"FPS: {int(fps)}", (10,30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)

    cv2.imshow("Full Body + Hand Pose FP32", frame)

    if cv2.waitKey(1) & 0xFF == 27:  # ESC 종료
        break

cap.release()
cv2.destroyAllWindows()
