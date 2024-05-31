import cv2
from ultralytics import YOLO

# Load the YOLOv8 model
model = YOLO('/runs/detect/train5/weights/best.pt')

# Open the video file
video_path = "/Users/rewatiramansingh/Downloads/Mumbai Highway Running car view | HD Footage | No Copyright.mp4"
cap = cv2.VideoCapture(video_path)

# Get the frame rate and size of the video
fps = cap.get(cv2.CAP_PROP_FPS)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Define the output video writer
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
output_path = 'output.mp4'
out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

# Loop through the video frames
while cap.isOpened():
    # Read a frame from the video
    success, frame = cap.read()

    if success:
        # Run YOLOv8 inference on the frame
        results = model(frame)

        # Visualize the results on the frame
        annotated_frame = results[0].plot()

        # Write the annotated frame to the output video
        out.write(annotated_frame)

        # Display the annotated frame
        cv2.imshow("YOLOv8 Inference", annotated_frame)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        # Break the loop if the end of the video is reached
        break

# Release the video capture object and close the display window
cap.release()
cv2.destroyAllWindows()

# Release the output video writer
out.release()

# Play the output video
cap = cv2.VideoCapture(output_path)
while cap.isOpened():
    success, frame = cap.read()
    if success:
        cv2.imshow('Output Video', frame)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    else:
        break

cv2.destroyAllWindows()
