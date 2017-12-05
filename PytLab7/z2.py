import subprocess
import os

K1 = subprocess.Popen("mkdir K1", shell=True)
K1.wait()
os.chdir("K1")
K2 = subprocess.Popen("mkdir K2", shell=True)
K3 = subprocess.Popen("mkdir K3", shell=True)
K3.wait()
os.chdir("K3")
K4 = subprocess.Popen("mkdir K4", shell=True)
os.chdir("..")
os.chdir("..")
K5 = subprocess.Popen("mkdir K5", shell=True)
K5.wait()
os.chdir("K5")
K6 = subprocess.Popen("mkdir K6", shell=True)

