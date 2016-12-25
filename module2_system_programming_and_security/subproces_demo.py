import subprocess

#subprocess.call(['ls','l'])
res = subprocess.check_output(['ls'])
print res.split('\n')
