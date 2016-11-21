from __future__ import unicode_literals
import multiprocessing

bind = "unix:/home/admin/mezzanine/webs/gunicorn.sock"
workers = multiprocessing.cpu_count() * 2 + 1
errorlog = "/home/admin/logs/webs_error.log"
loglevel = "error"
proc_name = "webs"
