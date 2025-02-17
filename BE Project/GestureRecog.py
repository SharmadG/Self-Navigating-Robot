import cv2
import mediapipe as mp
import RPi.GPIO as GPIO
import time

# config
debug = True
cam_source = 0  # Use 0 for USB camera, or specify the URL for webcam streaming

# Define GPIO pins for motor control
left_motor_forward_pin = 17
left_motor_backward_pin = 18
right_motor_forward_pin = 27
right_motor_backward_pin = 22

# Setup GPIO pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(left_motor_forward_pin, GPIO.OUT)
GPIO.setup(left_motor_backward_pin, GPIO.OUT)
GPIO.setup(right_motor_forward_pin, GPIO.OUT)
GPIO.setup(right_motor_backward_pin, GPIO.OUT)

# Helper function to move forward
def move_forward():
    GPIO.output(left_motor_forward_pin, GPIO.HIGH)
    GPIO.output(right_motor_forward_pin, GPIO.HIGH)

# Helper function to stop
def stop_motors():
    GPIO.output(left_motor_forward_pin, GPIO.LOW)
    GPIO.output(left_motor_backward_pin, GPIO.LOW)
    GPIO.output(right_motor_forward_pin, GPIO.LOW)
    GPIO.output(right_motor_backward_pin, GPIO.LOW)

# Helper function to process hand gestures
def process_gesture(hand_landmarks):
    # Get the landmark coordinates for the thumb tip (ID: 4) and the index finger tip (ID: 8)
    thumb_tip = hand_landmarks.landmark[4]
    index_tip = hand_landmarks.landmark[8]

    # Calculate the distance between the thumb tip and the index finger tip
    distance = ((index_tip.x - thumb_tip.x) ** 2 + (index_tip.y - thumb_tip.y) ** 2 + (
                index_tip.z - thumb_tip.z) ** 2) ** 0.5

    # If the distance is larger than a threshold, consider it an open hand gesture
    if distance > 0.1:
        move_forward()
    else:
        stop_motors()

# Initialize MediaPipe Hands
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5)

# Initialize camera
cap = cv2.VideoCapture(cam_source)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        continue

    # Convert the image to RGB
    image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the image
    results = hands.process(image_rgb)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Draw hand landmarks on the image
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Process hand gesture
            process_gesture(hand_landmarks)

    # Show the frame
    cv2.imshow('Hand Gesture Control', frame)

    # Check for 'q' key press to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()