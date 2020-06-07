#!/usr/bin/python
import os
os.system("systemctl stop mysqld")
os.system("shutdown -r now")
