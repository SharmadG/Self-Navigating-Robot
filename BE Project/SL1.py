import cv2
import mediapipe as mp
import pyttsx3

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()

# Initialize Text-to-Speech
tts_engine = pyttsx3.init()

# Define a lookup table for ISL signs
isl_signs = {
    '1': 'Hello',
    '2': 'Thank You',
    '3': 'Yes',
    '4': 'No',
    '5': 'Good',
    '6': 'Bad',
    '7': 'I Love You',
    '8': 'Sorry',
    '9': 'Help',
    '10': 'Please',
    '11': 'Closed Fist',
    '12': 'Open Palm',
    '13': 'Peace Sign',
    # Add more mappings as needed
}

def recognize_isl(frame):
    # Convert the frame to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the frame using MediaPipe Hands
    results = hands.process(rgb_frame)

    # Check if hands are detected
    if results.multi_hand_landmarks:
        hand_landmarks = results.multi_hand_landmarks[0]  # Assume only one hand for simplicity

        # Placeholder for gesture recognition based on hand landmarks
        detected_gesture = determine_gesture(hand_landmarks)

        return isl_signs.get(detected_gesture, 'Unknown Sign')
    else:
        return None  # Return None if no hands detected

def determine_gesture(hand_landmarks):
    # Example: Determine gesture based on landmark positions
    # Modify this function based on the gestures you want to detect

    # Example: Check if the index finger is up
    index_finger_up = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y < hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_MCP].y

    # Example: Check if the thumb is up
    thumb_up = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].y < hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_IP].y

    # Example: Check if the middle finger is up
    middle_finger_up = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].y < hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_MCP].y

    # Example: Check if the ring finger is up
    ring_finger_up = hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP].y < hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_MCP].y

    # Example: Check if the pinky finger is up
    pinky_finger_up = hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP].y < hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_MCP].y

    # Example: Check if all fingers are close to form a closed fist
    closed_fist = all(
        lm.y > hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].y
        for lm in hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP:mp_hands.HandLandmark.PINKY_TIP]
    )

    # Example: Check if all fingers are open to form an open palm
    open_palm = all(
        lm.y < hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].y
        for lm in hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP:mp_hands.HandLandmark.PINKY_TIP]
    )

    # Example: Check if the index and middle fingers are raised to form a peace sign
    peace_sign = index_finger_up and middle_finger_up and not thumb_up and not ring_finger_up and not pinky_finger_up

    # Add more conditions for other gestures
    if index_finger_up:
        return '1'
    elif thumb_up:
        return '2'
    elif middle_finger_up:
        return '3'
    elif ring_finger_up:
        return '4'
    elif pinky_finger_up:
        return '5'
    elif closed_fist:
        return '11'
    elif open_palm:
        return '12'
    elif peace_sign:
        return '13'
    # Add more conditions for other gestures

    # Default case
    return 'Unknown'

# Open the webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Unable to open the camera.")
    exit()

sentence = []  # List to store detected signs forming a sentence
detected_sign = None  # Variable to store the detected sign

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    if not ret:
        print("Error: Failed to capture a frame.")
        break

    # Recognize ISL from the current frame
    current_detected_sign = recognize_isl(frame)

    # Check if a new sign is detected
    if current_detected_sign and current_detected_sign != detected_sign:
        # Append the detected sign to the sentence
        sentence.append(current_detected_sign)
        detected_sign = current_detected_sign

    # Break the loop if 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcamq
cap.release()
cv2.destroyAllWindows()

# Convert the sentence to speech
tts_sentence = ' '.join(sentence)
print(f"\nGenerated Sentence: {tts_sentence}")
tts_engine.say(tts_sentence)
tts_engine.runAndWait()
