[app]
title = CameraSpy
package.name = camsnap
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy,requests,opencv-python
android.permissions = INTERNET, CAMERA, READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE
orientation = portrait
fullscreen = 0
android.arch = armeabi-v7a

[buildozer]
log_level = 2
warn_on_root = 1
