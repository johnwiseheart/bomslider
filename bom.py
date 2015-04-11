#!/usr/bin/env python
import urllib
from datetime import datetime, timedelta
import os
from PIL import Image
base_url = "http://wac.72dd.edgecastcdn.net/8072DD/radimg/radar/IDR712.T."
rootdir = '/srv/p.jcaw.me/bomslide/images/'

today = datetime.utcnow()
d = today - timedelta(hours=24)

minuted = timedelta(minutes=1)
while d.minute % 6 != 0:
    d += minuted

delta = timedelta(minutes=6)
while d <= today:

    urllib.urlretrieve(str(base_url) +  d.strftime("%Y%m%d%H%M") + ".png",  "images/" + d.strftime("%Y%m%d%H%M") + ".png")
    file = d.strftime("%Y%m%d%H%M") + ".png"
    try:
        im = Image.open(os.path.join(rootdir, file))
    except Exception:
        os.remove(os.path.join(rootdir, file))
    print "Got " + d.strftime("%Y%m%d %H%M")
    d += delta


