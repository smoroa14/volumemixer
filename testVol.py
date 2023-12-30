from __future__ import print_function

import struct

from pycaw.pycaw import AudioUtilities, ISimpleAudioVolume
import serial
import time

arduino = serial.Serial(port='COM3', baudrate=9600, timeout=.1)
first_value = 0.0
tolerance = 2


def setvolume(vol):
    sessions = AudioUtilities.GetAllSessions()
    for session in sessions:
        volume = session._ctl.QueryInterface(ISimpleAudioVolume)
        if session.Process and session.Process.name().lower() == "chrome.exe":
            # print("volume.GetMasterVolume(): %s" % volume.GetMasterVolume())
            volume.SetMasterVolume(vol, None)
            # print("volume.GetMasterVolume(): %s" % volume.GetMasterVolume())


def main():
    global first_value
    data = write_read()
    if len(data) > 3:
        # print(data)
        s = data.decode('utf-8')
        s = s[0:len(s) - 2:1]
        f = float(s)
        f = f / 97 * 100

        if f > first_value + tolerance or f < first_value - tolerance:
            first_value = f
            print("Set new sound volume: %.0f -- %f" % (first_value, f/100))
            if f > 100:
                f = 100
            if f < 0:
                f = 0
            setvolume(f/100)
        print(f)


def write_read():
    arduino.write(bytes("r", 'utf-8'))
    time.sleep(0.05)
    data = arduino.readline()
    return data


if __name__ == "__main__":
    while True:
        main()
        time.sleep(0.05)
