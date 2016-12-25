import subprocess

handle = subprocess.Popen('ls',stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE,close_fds=True)

print handle.stdout.read()
