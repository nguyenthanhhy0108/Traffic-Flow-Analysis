import cv2
import torch
import numpy as np
from deep_sort_realtime.deepsort_tracker import DeepSort
from models.common import DetectMultiBackend, AutoShape

class video_tracking:
    def __init__(self):
        self.video_path = None
        self.output_video_path = None
        self.conf_threshold = 0.6
        self.tracking_class = 0

        self.tracker = DeepSort(max_age=5)
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

        self.model = DetectMultiBackend(weights="weight\\yolov9-c.pt",
                                        device=self.device,
                                        fuse=True)
        self.model = AutoShape(model=self.model)

        with open("data_ext\\classes.names") as f:
            self.class_names = f.read().strip().split('\n')

        self.colors = np.random.randint(0, 255, size=(len(self.class_names), 3))
        self.tracks = []
        self.output_images_folder = None
        self.out = None

    def tracking(self, input_video_path, output_video_path, output_images_path):
        output_video = '/output_video.mp4'
        cap = cv2.VideoCapture(input_video_path)

        self.output_video_path = output_video_path + output_video
        self.output_images_folder = output_images_path

        frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        fps = int(cap.get(cv2.CAP_PROP_FPS))

        fourcc = cv2.VideoWriter_fourcc(*'MP4V')
        self.out = cv2.VideoWriter(self.output_video_path, fourcc, fps, (frame_width, frame_height))
        tracked_ids = []

        frame_count = 0
        while True:
            ret, frame = cap.read()

            if not ret:
                break

            results = self.model(frame)

            detect = []

            for detect_object in results.pred[0]:
                label, confidence, bbox = detect_object[5], detect_object[4], detect_object[:4]
                x1, y1, x2, y2 = map(int, bbox)
                class_id = int(label)

                if class_id != 0:
                    continue

                if self.tracking_class is None:
                    if confidence < self.conf_threshold:
                        continue
                    else:
                        if class_id == self.tracking_class and confidence < self.conf_threshold:
                            continue
                
                detect.append([ [x1, y1, x2 - x1, y2 - y1], confidence, class_id ])

            tracks = self.tracker.update_tracks(detect, frame=frame)

            frame_for_cut = frame.copy()

            for track in tracks:
                if track.is_confirmed():
                    track_id = track.track_id

                    ltrb = track.to_ltrb()
                    class_id = track.get_det_class()
                    x1, y1, x2, y2 = map(int, ltrb)

                    if class_id == 0:
                        if track_id not in tracked_ids:
                            tracked_ids.append(track_id)
                            roi = frame_for_cut[y1:y2, x1:x2]

                            filename = output_images_path + f"\\{track_id}.jpg"
                            cv2.imwrite(filename, roi)

                    color = self.colors[class_id]
                    B, G, R = map(int, color)
                    label = "{}-{}".format(self.class_names[class_id], track_id)

                    cv2.rectangle(frame, (x1, y1), (x2, y2), (B, G, R), 2)
                    cv2.rectangle(frame, (x1 - 1, y1 - 20), (x1 + len(label) * 12, y1), (B, G, R), -1)
                    cv2.putText(frame, label, (x1 + 5, y1 - 8), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

            self.out.write(frame)
            resized_frame = cv2.resize(frame, (1040, 720))
            cv2.imshow("out", resized_frame)

            if cv2.waitKey(1) == ord("q"):
                break
            frame_count += 1
            print("Processing frame "+ f"{frame_count}")

    def tracking_on_image(self, input_image_path, output_images_path):
        frame = cv2.imread(input_image_path)

        results = self.model(frame)

        detect = []

        for detect_object in results.pred[0]:
            label, confidence, bbox = detect_object[5], detect_object[4], detect_object[:4]
            x1, y1, x2, y2 = map(int, bbox)
            class_id = int(label)

            if class_id != 0:
                continue

            if confidence < self.conf_threshold:
                continue
            
            detect.append([ [x1, y1, x2 - x1, y2 - y1], confidence, class_id ])

        tracks = self.tracker.update_tracks(detect, frame=frame)

        frame_for_cut = frame.copy()

        for track in tracks:
            track_id = track.track_id

            ltrb = track.to_ltrb()
            class_id = track.get_det_class()
            x1, y1, x2, y2 = map(int, ltrb)


            if class_id == 0:
                roi = frame_for_cut[y1:y2, x1:x2]

                temp = input_image_path.replace(".", "").replace("\\", "").replace(".jpg", "")

                temp = temp[32:-3]

                filename = output_images_path + f"\\{track_id}" + temp + ".jpg"
                print(filename)
                cv2.imwrite(filename, roi)

            color = self.colors[class_id]
            B, G, R = map(int, color)
            label = "{}-{}".format(self.class_names[class_id], track_id)

            cv2.rectangle(frame, (x1, y1), (x2, y2), (B, G, R), 2)
            cv2.rectangle(frame, (x1 - 1, y1 - 20), (x1 + len(label) * 12, y1), (B, G, R), -1)
            cv2.putText(frame, label, (x1 + 5, y1 - 8), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)