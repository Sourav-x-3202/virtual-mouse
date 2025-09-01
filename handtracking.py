import cv2
import mediapipe as mp

class HandTracker:
    def __init__(self, maxHands=1, detectionCon=0.7, trackCon=0.7):
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.trackCon = trackCon

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(
            static_image_mode=False,
            max_num_hands=self.maxHands,
            min_detection_confidence=self.detectionCon,
            min_tracking_confidence=self.trackCon,
        )
        self.mpDraw = mp.solutions.drawing_utils
        self.results = None
        self.lmList = []

    def detect(self, frame):
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(rgb)
        self.lmList = []
        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                for id, lm in enumerate(handLms.landmark):
                    h, w, _ = frame.shape
                    cx, cy = int(lm.x * w), int(lm.y * h)
                    self.lmList.append((cx, cy))
        return self.lmList

    def fingersUp(self):
        """Returns a list of 5 ints (0/1) for each finger state"""
        if len(self.lmList) == 0:
            return [0, 0, 0, 0, 0]

        tips = [4, 8, 12, 16, 20]
        fingers = []

        # Thumb
        fingers.append(1 if self.lmList[tips[0]][0] < self.lmList[tips[0] - 1][0] else 0)

        # Fingers (Index to Pinky)
        for id in range(1, 5):
            fingers.append(1 if self.lmList[tips[id]][1] < self.lmList[tips[id] - 2][1] else 0)

        return fingers

    def findDistance(self, p1, p2, frame=None, draw=True):
        x1, y1 = self.lmList[p1]
        x2, y2 = self.lmList[p2]
        cx, cy = (x1 + x2) // 2, (y1 + y2) // 2
        length = ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5

        if draw and frame is not None:
            cv2.line(frame, (x1, y1), (x2, y2), (255, 0, 255), 2)
            cv2.circle(frame, (x1, y1), 5, (255, 0, 255), cv2.FILLED)
            cv2.circle(frame, (x2, y2), 5, (255, 0, 255), cv2.FILLED)
            cv2.circle(frame, (cx, cy), 5, (0, 0, 255), cv2.FILLED)

        return length, (x1, y1, x2, y2, cx, cy)
