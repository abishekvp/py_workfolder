import time
import subprocess

def shutdown(t):
    time.sleep(t*60)
    subprocess.call([r'C:\Users\surya\OneDrive\Desktop\shutdown.bat'])

shutdown(23)