# import cv2
# import mediapipe as mp
# import pyautogui

# # Initialize mediapipe hands and drawing utils
# mp_hands = mp.solutions.hands
# mp_drawing = mp.solutions.drawing_utils
# hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
# cap = cv2.VideoCapture(0)

# # Get screen resolution
# screen_w, screen_h = pyautogui.size()

# def fingers_up(hand_landmarks):
#     """Returns a list [thumb, index, middle, ring, pinky] where 1=up, 0=down"""
#     fingers = []

#     # Thumb: check x-coordinates of tip and joint
#     if hand_landmarks.landmark[4].x < hand_landmarks.landmark[3].x:
#         fingers.append(1)
#     else:
#         fingers.append(0)

#     # Other 4 fingers: check y-coordinates of tip and pip
#     tips = [8, 12, 16, 20]
#     for tip in tips:
#         if hand_landmarks.landmark[tip].y < hand_landmarks.landmark[tip - 2].y:
#             fingers.append(1)
#         else:
#             fingers.append(0)

#     return fingers

# while True:
#     ret, frame = cap.read()
#     if not ret:
#         break

#     frame = cv2.flip(frame, 1)  # Mirror view
#     rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#     result = hands.process(rgb_frame)

#     if result.multi_hand_landmarks:
#         for hand_landmarks in result.multi_hand_landmarks:
#             # Draw landmarks on hand
#             mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

#             # Detect which fingers are up
#             fingers = fingers_up(hand_landmarks)
#             # print(fingers)  # Debug: [thumb, index, middle, ring, pinky]

#             # Index fingertip for cursor control
#             index_finger = hand_landmarks.landmark[8]
#             x = int(index_finger.x * screen_w)
#             y = int(index_finger.y * screen_h)

#             # Gesture controls
#             if fingers == [0, 1, 0, 0, 0]:  # Only index up → Move cursor
#                 pyautogui.moveTo(x, y)

#             elif fingers == [0, 1, 1, 0, 0]:  # Index + Middle → Left Click
#                 pyautogui.click()

#             elif fingers == [0, 1, 1, 1, 0]:  # Three fingers → Right Click
#                 pyautogui.click(button="right")

#             elif fingers == [0, 0, 0, 0, 0]:  # Fist → Scroll down
#                 pyautogui.scroll(-50)

#             elif fingers == [1, 1, 1, 1, 1]:  # All fingers up → Scroll up
#                 pyautogui.scroll(50)

#     cv2.imshow("Virtual Mouse", frame)

#     # Exit with ESC key
#     if cv2.waitKey(1) & 0xFF == 27:
#         break

# cap.release()
# cv2.destroyAllWindows()
import cv2
import mediapipe as mp
import pyautogui

# Initialize mediapipe hands
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
cap = cv2.VideoCapture(0)

# Screen size
screen_w, screen_h = pyautogui.size()

def fingers_up(hand_landmarks):
    """Returns list [thumb, index, middle, ring, pinky] (1=up, 0=down)."""
    fingers = []

    # Thumb: compare tip and MCP in x-axis (works for right hand)
    if hand_landmarks.landmark[4].x < hand_landmarks.landmark[3].x:
        fingers.append(1)
    else:
        fingers.append(0)

    # Other fingers: compare tip and PIP in y-axis
    tips = [8, 12, 16, 20]
    for tip in tips:
        if hand_landmarks.landmark[tip].y < hand_landmarks.landmark[tip - 2].y:
            fingers.append(1)
        else:
            fingers.append(0)

    return fingers

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb_frame)

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            fingers = fingers_up(hand_landmarks)
            # print(fingers)  # Debugging: check detected pattern

            # Index fingertip (for cursor)
            index_finger = hand_landmarks.landmark[8]
            x = int(index_finger.x * screen_w)
            y = int(index_finger.y * screen_h)

            # Cursor movement (index finger up)
            if fingers[1] == 1 and sum(fingers) == 1:
                pyautogui.moveTo(x, y)

            # Left click (index + middle)
            elif fingers[1] == 1 and fingers[2] == 1 and sum(fingers) == 2:
                pyautogui.click()

            # Right click (index + middle + ring)
            elif fingers[1] == 1 and fingers[2] == 1 and fingers[3] == 1 and sum(fingers) == 3:
                pyautogui.click(button="right")

            # Fist (all fingers down)
            elif sum(fingers) == 0:
                pyautogui.scroll(-50)

            # Open palm (all fingers up)
            elif sum(fingers) == 5:
                pyautogui.scroll(50)

    cv2.imshow("Virtual Mouse", frame)

    if cv2.waitKey(1) & 0xFF == 27:  # ESC
        break

cap.release()
cv2.destroyAllWindows()
