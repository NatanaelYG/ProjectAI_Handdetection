import os
import cv2
import sys

print(sys.path)

DATA_DIR = './data'
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

number_of_classes = 1
dataset_size = 1000

cap = cv2.VideoCapture(0)  # Coba dengan 0 jika 2 tidak bekerja
if not cap.isOpened():
    print("Error: Could not open camera.")
    sys.exit()

folder_number = 25

class_dir = os.path.join(DATA_DIR, str(folder_number))
if not os.path.exists(class_dir):
    os.makedirs(class_dir)

print('Collecting data for class {}'.format(folder_number))

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to capture image")
        break
    cv2.putText(frame, 'Ready? Press "Q" to start!', (100, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)
    cv2.imshow('frame', frame)
    if cv2.waitKey(25) == ord('q'):
        break

counter = 0
while counter < 200:
    ret, frame = cap.read()
    if not ret:
        print("Failed to capture image")
        break

    cv2.putText(frame, f'Collecting image {counter+1}/{dataset_size}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)
    cv2.imshow('frame', frame)
    cv2.waitKey(25)
    cv2.imwrite(os.path.join(class_dir, '{}.jpg'.format(counter)), frame)
    counter += 1

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to capture image")
        break
    cv2.putText(frame, 'Ready? Press "Q" to start!', (100, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)
    cv2.imshow('frame', frame)
    if cv2.waitKey(25) == ord('q'):
        break

while counter < 400:
    ret, frame = cap.read()
    if not ret:
        print("Failed to capture image")
        break

    cv2.putText(frame, f'Collecting image {counter+1}/{dataset_size}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)
    cv2.imshow('frame', frame)
    cv2.waitKey(25)
    cv2.imwrite(os.path.join(class_dir, '{}.jpg'.format(counter)), frame)
    counter += 1

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to capture image")
        break
    cv2.putText(frame, 'Ready? Press "Q" to start!', (100, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)
    cv2.imshow('frame', frame)
    if cv2.waitKey(25) == ord('q'):
        break

while counter < 600:
    ret, frame = cap.read()
    if not ret:
        print("Failed to capture image")
        break

    cv2.putText(frame, f'Collecting image {counter+1}/{dataset_size}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)
    cv2.imshow('frame', frame)
    cv2.waitKey(25)
    cv2.imwrite(os.path.join(class_dir, '{}.jpg'.format(counter)), frame)
    counter += 1

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to capture image")
        break
    cv2.putText(frame, 'Ready? Press "Q" to start!', (100, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)
    cv2.imshow('frame', frame)
    if cv2.waitKey(25) == ord('q'):
        break

while counter < 800:
    ret, frame = cap.read()
    if not ret:
        print("Failed to capture image")
        break

    cv2.putText(frame, f'Collecting image {counter+1}/{dataset_size}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)
    cv2.imshow('frame', frame)
    cv2.waitKey(25)
    cv2.imwrite(os.path.join(class_dir, '{}.jpg'.format(counter)), frame)
    counter += 1

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to capture image")
        break
    cv2.putText(frame, 'Ready? Press "Q" to start!', (100, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)
    cv2.imshow('frame', frame)
    if cv2.waitKey(25) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
