import cv2
from fer import FER

# Create emotion detector
detector = FER(mtcnn=True)

# Open webcam
cap = cv2.VideoCapture(0)
print("🎥 Starting Emotion Detection... Press 'q' to quit")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Detect emotions in the current frame
    result = detector.detect_emotions(frame)

    if result:
        emotions = result[0]["emotions"]
        top_emotion = max(emotions, key=emotions.get)
        confidence = emotions[top_emotion]
        text = f"{top_emotion} ({confidence:.2f})"
        print(text)

        # Display emotion on the frame
        cv2.putText(frame, text, (50, 50), cv2.FONT_HERSHEY_SIMPLEX,
                    1, (0, 255, 0), 2, cv2.LINE_AA)

    # Show the frame
    cv2.imshow("Emotion Detection", frame)

    # Quit when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
print("👋 Stopped Emotion Detection.")
