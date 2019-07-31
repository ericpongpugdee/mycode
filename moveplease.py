#!/usr/bin/env python3

import shutil
import os

#force python to start in home user directory
os.chdir('/home/student/mycode/')

#move raynor into ceph storage same file name will be over written with new file

shutil.move('raynor.obj', 'ceph_storage/')

xname = input('what is the new name of kerrigan.obj? ')
shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)



