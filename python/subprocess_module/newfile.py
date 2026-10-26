import subprocess as sp

cmd = "ls"
sp.call(cmd)

cmd = "ls -a"
sp.call(cmd, shell=True)

cmd = "python test.py"
sp.call(cmd, shell=True)

cmd = "ping www.google.com"
sp.call(cmd, shell=True)