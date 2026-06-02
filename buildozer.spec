[app]
title = Ecociclo
package.name = ecociclo
package.domain = org.ecociclo
source.dir = .
main.py = main.py
source.include_exts = py,png,jpg,kv,atlas,ttf
source.include_patterns = media/*, kv/*, screens/*
version = 0.1.0
requirements = python3, kivy==2.3.1
android.presplash_color = #fbfcfb
icon.filename = media/images/app_icon.png
presplash.filename = media/images/presplash.png
# android.permissions = INTERNET
android.api = 33
android.minapi = 21
orientation = portrait
fullscreen = 0
android.archs = arm64-v8a, armeabi-v7a
android.enable_androidx = True