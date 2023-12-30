import subprocess
import sounddevice as sd


def ps():
    cmd = 'powershell "gps | where {$_.MainWindowTitle } | select Path'
    proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    for line in proc.stdout:
        if line.rstrip():
            path = line.decode().rstrip()
            print(path[path.rfind('\\')+1:len(path):1])


def ps2():
    cmd = 'powershell "gps | where {$_.MainWindowTitle }'
    proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    for line in proc.stdout:
        if line.rstrip():
            path = line.decode().rstrip()
            print(path)


def sounddevice():
    sd.query_devices()


ps2()
