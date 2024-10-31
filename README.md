# RP2040-Touch-LCD-1.28-GIF-Player
Enables the RP2040-Touch-LCD-1.28 to play multible GIFs using circuitpython


# Setting Up the RP2040 with 1.28" Display

Follow these steps to install and set up the firmware on your RP2040 with a 1.28" display.

### 1. Connect the USB Cable
Connect the USB cable from your computer to the RP2040 board. While plugging it in, **hold down the BOOT button** on the board. This will put the board into bootloader mode.

### 2. Copy Firmware File
After connecting the USB, a new folder called **RPI-RP2** should appear on your computer. Drag and drop the firmware file named: `adafruit-circuitpython-waveshare_rp2040_touch_lcd_1_28-en_US-9.x.x.uf2`
into this folder.

### 3. Automatic Installation
Once the file is copied, the firmware will automatically install. The display will reboot after installation.

### 4. Add Necessary Libraries
From the `library` folder in the download package, locate the files `cst816.py` and `gc9a01.py`. Copy these files to the **lib** folder on the **CIRCUITPY** drive that appears after the board restarts.

### 5. Add GIF Files
Place your desired GIF files on the **CIRCUITPY** drive. 

> **Note:** This code version requires exactly **5 GIF files** to avoid crashes.

### 6. Rename GIF Files
Rename the GIF files in sequence as follows:
- `1.gif`
- `2.gif`
- `3.gif`
- `4.gif`
- `5.gif`

### 7. Add Code
In the download package, find the `code.py` file. Copy this file and replace the existing `code.py` file on the **CIRCUITPY** drive with it.

---

After completing these steps, the display should begin to play the GIFs in sequence. Enjoy your setup!
