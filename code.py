import gc
import time
import board
import busio
import pwmio
import gifio
import displayio
import struct
from gc9a01 import GC9A01
import cst816

# Variables
# Pins
pin_SDA = board.IMU_SDA
pin_SDL = board.IMU_SCL
pin_cs = board.LCD_CS  
pin_dc = board.LCD_DC
pin_clk = board.LCD_CLK
pin_mosi = board.LCD_DIN
pin_reset = board.LCD_RST
pin_backlight = board.LCD_BL

# List of GIF files
gif_files = ["/1.gif", "/2.gif", "/3.gif", "/4.gif", "/5.gif"]  # Add as many GIF files as you like here
current_gif_index = 0  # Current GIF in the list

# Setup display
displayio.release_displays()
spi = busio.SPI(pin_clk, MOSI=pin_mosi)
display_bus = displayio.FourWire(spi, command=pin_dc, chip_select=pin_cs, reset=pin_reset)
display = GC9A01(display_bus, width=240, height=240)
pwm = pwmio.PWMOut(pin_backlight, frequency=5000, duty_cycle=65535)  # max 65535

splash = displayio.Group()
display.root_group = splash
display.auto_refresh = False
display_bus = display.bus

# Initialize I2C
i2c = busio.I2C(board.IMU_SCL, board.IMU_SDA, frequency=100000)
touch = cst816.CST816(i2c)

# Double-click detection variables
last_touch_time = 0
click_count = 0
double_click_delay = 0.8  # Time window for double-click (500 ms)

# Function to load a GIF
def load_gif(file_path):
    global face, odg, splash
    # Remove current GIF from the splash group if any
    if splash:
        splash.pop()
    # Load new GIF
    odg = gifio.OnDiskGif(file_path)
    face = displayio.TileGrid(
        odg.bitmap,
        pixel_shader=displayio.ColorConverter(
            input_colorspace=displayio.Colorspace.RGB565_SWAPPED
        ),
    )
    splash.append(face)

# Load the first GIF first
load_gif(gif_files[current_gif_index])

# Timing for the frames
start = time.monotonic()
next_delay = odg.next_frame()  # Load the first frame
end = time.monotonic()
overhead = end - start

# Function to detect double-click
def detect_double_click():
    global last_touch_time, click_count
    current_time = time.monotonic()
    press = touch.get_touch()
    
    if press:
        # If there is the first click
        if click_count == 0:
            last_touch_time = current_time
            click_count = 1
        elif click_count == 1 and (current_time - last_touch_time) <= double_click_delay:
            # Second click within the time window -> double-click detected
            click_count = 0
            return True
    # Time window expired or not touched in time
    if (current_time - last_touch_time) > double_click_delay:
        click_count = 0
    
    return False

# Loop to display GIF and switch on double-click
while True:
    # Display frame of the current GIF
    time.sleep(max(0, next_delay - overhead))
    next_delay = odg.next_frame()

    display_bus.send(42, struct.pack(">hh", 0, odg.bitmap.width - 1))
    display_bus.send(43, struct.pack(">hh", 0, odg.bitmap.height - 1))
    display_bus.send(44, odg.bitmap)
    
    if detect_double_click():
        # Short pause to prevent multiple triggers
        time.sleep(0.5)
        # Switch GIF
        odg.deinit()
        odg = None
        gc.collect()
        current_gif_index = (current_gif_index + 1) % len(gif_files)
        load_gif(gif_files[current_gif_index])
