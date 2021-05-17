from __future__ import unicode_literals
import io
import pyqrcode
from base64 import b64encode
import eel
import os
import youtube_dl
eel.init('web')

@eel.expose
def validate():
   os.system('Python Criminal-Identification-System/j.py')

eel.start('index.html', size=(1000, 600))
