## RP2040-Touch-LCD-1.28-GIF-Player
Enables the RP2040-Touch-LCD-1.28 to play multible GIFs using circuitpython

This is specificly made for [this board](https://www.waveshare.com/rp2040-touch-lcd-1.28.htm), I can't promise it will work for different screens or chipsets

# Table of Contents
1. [Setup](#setup)
2. [Edit the code](#edit)
3. [Changeing the brightness of the screen](#brightness)


# Setting Up the RP2040 with 1.28" Display <a name="setup"></a>

Follow these steps to install and set up the firmware on your RP2040 with a 1.28" display.

### 1. Connect the USB Cable
Connect the USB cable from your computer to the RP2040 board. While plugging it in, **hold down the BOOT button** on the board. This will put the board into bootloader mode.
The folder should look like this:

![alt text](https://cdn.discordapp.com/attachments/974938953947938846/1301511436152999966/FirmwareFolder.png?ex=6724be7b&is=67236cfb&hm=a7e89e824a1e989140cf4ef27fada1b31a1ea1f0c3f90adbae84af6877af6656&)

### 2. Copy Firmware File
After connecting the USB, a new folder called **RPI-RP2** should appear on your computer. Drag and drop the firmware file named: `adafruit-circuitpython-waveshare_rp2040_touch_lcd_1_28-en_US-9.x.x.uf2`
into this folder.

### 3. Automatic Installation
Once the file is copied, the firmware will automatically install. The display will reboot after installation.

### 4. Add Necessary Libraries
From the `library` folder in the download package, locate the files `cst816.py` and `gc9a01.py`. Copy these files to the **lib** folder on the **CIRCUITPY** drive that appears after the board restarts.

![image](https://github.com/user-attachments/assets/8e9caf76-7352-4c8b-9716-378696eb481d)

### 5. Add Optimized GIF Files
Prepare your GIF files for the display by ensuring they meet the following requirements to maintain optimal performance:

- **Resolution**: 240x240 pixels
- **Frame Rate**: Keep the frame rate low (e.g., 10–15 fps) to reduce file size and prevent performance issues.
- For optimization you can use [ezgif](https://ezgif.com) or similar software

Once optimized, place the GIF files on the **CIRCUITPY** drive. 


### 6. Rename GIF Files (optional)
The Display works no mater the names of the GIF, but if you want a certain order rename the GIF files as follows:
- `1.gif`
- `2.gif`
- `3.gif`
- `...`

### 7. Add Code
In the download package, find the `code.py` file. Copy this file and replace the existing `code.py` file on the **CIRCUITPY** drive with it.

At the end your Folder structure should look somthing like this:

![image](https://github.com/user-attachments/assets/4eb6c8fc-eb97-4498-b6eb-626feed10c1d)




After completing these steps, the display should begin to play the GIFs in sequence. Enjoy your setup!

---

# Editing the code <a name="edit"></a>

I'm not a professional coder, but I tried my best to make this work as well as I could. So if you have improvements for it let me know

## Follow these steps to connect your RP2040 to Thonny and open the `code.py` file for editing.

### 1. Install Thonny (if you haven't already)
- Download and install Thonny from the [official website](https://thonny.org/).

### 2. Connect the RP2040 to Your Computer
- Use a USB cable to connect the RP2040 to your computer.
- Ensure the **CIRCUITPY** drive appears on your computer; this confirms that the RP2040 is recognized.

### 3. Open Thonny
- Start Thonny on your computer.

### 4. Set the Interpreter to CircuitPython (RP2040)
1. In Thonny, go to **Tools > Options**.
2. In the **Interpreter** tab, select **CircuitPython (generic)** as the interpreter.
3. Make sure Thonny is set to communicate with the **CIRCUITPY** drive (RP2040) connected via USB.

> **Note:** If you do not see the **CircuitPython (generic)** option, check that you are using the latest version of Thonny.

### 5. Open `code.py`
1. In the **Files** pane on the left side of Thonny, navigate to the **CIRCUITPY** drive.
2. Locate `code.py` and double-click to open it in Thonny’s editor.
3. You can now view and edit the code directly in Thonny.

### 6. Save Your Changes
- Once you’ve made changes to `code.py`, press **Save** or use the shortcut **Ctrl+S** (or **Cmd+S** on macOS).
- Thonny will save the updated `code.py` file directly to your RP2040, and the board will automatically restart to run the new code.

---

# Changeing the brightness of the screen: <a name="brightness"></a>

You need to have thonny and the code open for you to change the brightness of the screen

- Find the line: 
  ```python
  pwm = pwmio.PWMOut(pin_backlight, frequency=5000, duty_cycle=65535)  # max 65535
  ```
  (That is line 33 in the current version)

- Now edit the `duty_cycle` value to anything from 0-65535
  -> 50% brightness would be about 32767
- Then safe the code and the changes should apply right away (or a reboot)




