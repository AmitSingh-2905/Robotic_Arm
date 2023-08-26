import cv2
import qrcode

# Initialize the webcam
cap = cv2.VideoCapture(0)

# Create a QR code reader instance
qr_decoder = cv2.QRCodeDetector()

while True:
    # Capture a frame from the webcam
    ret, frame = cap.read()

    # Detect QR codes in the frame
    retval, decoded_info, points, _ = qr_decoder.detectAndDecodeMulti(frame)

    # If QR code is detected, display the information
    if retval:
        print("Y")
        for i in range(len(decoded_info)):
            qr_data = decoded_info[i]
            qr_position = points[i]

        #     # Convert the points to integers and reshape for drawing
        #     qr_position = qr_position.reshape(-1, 1, 2).astype(int)

            # Draw a polygon around the QR code
        # cv2.polylines(frame, [qr_position], isClosed=True, color=(0, 255, 0), thickness=2)

            # Display the QR code data
        #     text_position = (qr_position[0][0][0], qr_position[0][0][1] - 10)
        #     cv2.putText(frame, qr_data, text_position, cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        #     print("yes")

    # Display the captured frame
    cv2.imshow("QR Code Scanner", frame)

    # Check for the 'q' key to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close all windows
cap.release()
cv2.destroyAllWindows()
