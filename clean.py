#!/usr/bin/env python

import os
from PIL import Image
rootdir = '/srv/johnwiseheart.me/projects/bom2/images/'

for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        try:
            im = Image.open(os.path.join(subdir, file))
            im.verify()
        except Exception as e:
            os.remove(os.path.join(subdir, file))
            print e
