import time
import gc  # Garbage Collector hinzufügen
from micropython import const
from adafruit_bus_device import i2c_device

# I2C ADDRESS
_CST816_ADDR = const(0x15)

# Register Addresses
_CST816_GestureID = const(0x01)
_CST816_FingerNum = const(0x02)
_CST816_XposH = const(0x03)
_CST816_XposL = const(0x04)
_CST816_YposH = const(0x05)
_CST816_YposL = const(0x06)

_CST816_ChipID = const(0xA7)
_CST816_FwVersion = const(0xA9)

# Modes
_CST816_Point_Mode = const(1)
_CST816_Gesture_Mode = const(2)

class CST816:
    """Driver for the CST816 Touchscreen connected over I2C."""

    def __init__(self, i2c):
        self.i2c_device = i2c_device.I2CDevice(i2c, _CST816_ADDR)
        self.prev_x = 0
        self.prev_y = 0
        self.prev_touch = False
        self.x_point = 0
        self.y_point = 0
        self.x_dist = 0
        self.y_dist = 0
        self.mode = 0

    def _i2c_write(self, reg, value):
        """Write to I2C"""
        with self.i2c_device as i2c:
            i2c.write(bytes([reg, value]))

    def _i2c_read(self, reg):
        """Read from I2C"""
        with self.i2c_device as i2c:
            data = bytearray(1)
            i2c.write_then_readinto(bytes([reg]), data)
            return data[0]

    def who_am_i(self):
        """Check the Chip ID"""
        return bool(self._i2c_read(_CST816_ChipID) == 0xB5)

    def reset(self):
        """Reset the Chip"""
        self._i2c_write(0xFE, 0x00)  # Disable sleep mode
        time.sleep(0.1)
        self._i2c_write(0xFE, 0x01)  # Enable sleep mode
        time.sleep(0.1)
        gc.collect()  # Garbage Collection nach dem Reset

    def read_revision(self):
        """Read Firmware Version"""
        return self._i2c_read(_CST816_FwVersion)

    def get_point(self):
        """Get the Pointer Position"""
        with self.i2c_device as i2c:
            data = bytearray(4)
            i2c.write_then_readinto(bytes([_CST816_XposH]), data)  # Read all position registers at once

        x_point_h = data[0]
        x_point_l = data[1]
        y_point_h = data[2]
        y_point_l = data[3]
        self.x_point = ((x_point_h & 0x0F) << 8) + x_point_l
        self.y_point = ((y_point_h & 0x0F) << 8) + y_point_l

        return self

    def get_touch(self):
        """Detect User Presence"""
        return self._i2c_read(_CST816_FingerNum) > 0

    def get_distance(self):
        """Get the Distance Between Readings, only while touched"""
        touch_data = self.get_point()  # Call get_point once

        x = touch_data.x_point
        y = touch_data.y_point

        if not self.prev_touch and self.get_touch():
            self.x_dist = 0
            self.y_dist = 0
        else:
            self.x_dist = x - self.prev_x
            self.y_dist = y - self.prev_y

        self.prev_touch = self.get_touch()
        self.prev_x = x
        self.prev_y = y

        gc.collect()  # Garbage Collection nach dem Lesen der Daten
        return self
