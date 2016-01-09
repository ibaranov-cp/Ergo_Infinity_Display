# Ergo_Infinity_Display
These files are a quick and dirty way to get the ErgoDox Infinity LCD under user control.
Should work on all major systems with a few modifications, tested under windows (requires python, pyserial, etc)

# Setup
Ensure you have python, pyserial, and psutil (in Windows, after installing python, install pip, then run python -m pip install pyserial)
Connect The Ergodox Infinity to a USB port, and record the port that the keyboard connects to (in Windows, check the Device manager, my keyboard comes up on USB 29)
In CPU_GPU.py, edit the "ser = serial.Serial(28, 115200, timeout=0.5)" line to the port recorded above. In Linux this is usual /dev/ttyUSBXX, on Windows, you have to subtract 1, so I set mine to 28)
Save.

Now you can double click on CPU_GPU.py, the terminal window should remain open, and the display on the keyboard will show stats.

Should look like this:

![alt tag](http://tiny.cc/ttzz7x)

You CPU_GPU is meant to be a demo of the capabilities of the graphics library. 
Ergo_Infinity_Display.py contains the actual functions, if that file is run it does a quick test of abilites and times them.
Fonts.py stores custom fonts I created for the display, though only QuickType_5x8 is any good.
