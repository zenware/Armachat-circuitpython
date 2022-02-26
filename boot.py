#!/usr/bin/env python3
"""
ARMACHAT Boot Process

Initialize the hardware
- Display
- Buttons
- Radio
- Storage
Set the storage volume label
Hand off to ARMACHAT software

If any errors occur, write the logger contents to disk. Prompt for user input to continue.

"""
import time
import board
import busio
import gc
import displayio
import digitalio
import microcontroller
import storage
from adafruit_st7789 import ST7789

"""Initialize the available hardware"""
power_led = digitalio.DigitalInOut(board.LED)
power_led.direction = digitalio.Direction.OUTPUT

displayio.release_displays()  # Release any resources currently in use for the displays
# TODO: Move display initialization to ARMACHAT Model
tft_cs = board.GP21
tft_dc = board.GP16
spi_mosi = board.GP19
spi_clk = board.GP18
spi = busio.SPI(spi_clk, spi_mosi)
backlight = board.GP20
display_bus = displayio.FourWire(spi, command=tft_dc, chip_select=tft_cs)
display = ST7789(display_bus, rotation=270, width=320, height=240, backlight_pin=backlight)

safe_ground = digitalio.DigitalInOut(board.GP14)  # What do?
safe_ground.direction = digitalio.Direction.OUTPUT
safe_ground.value = False

usb_power = digitalio.DigitalInOut(board.VBUS_SENSE)  # Defaults to INPUT
usb_power.pull = digitalio.Pull.UP  # turn on internal pull-up resistor

safe = digitalio.DigitalInOut(board.GP7)  # Safe Mode Button Pin
safe.pull = digitalio.Pull.UP
wrp = digitalio.DigitalInOut(board.GP22)  # Write Mode Button Pin
wrp.pull = digitalio.Pull.UP

storage.remount("/", readonly=False)
storage.getmount("/").label = "ARMACHAT"

""" Start boot interface """
print(f"Free memory: {gc.mem_free()}")
if usb_power.value:
    print("USB Power Connected")
print("Press ESC for SAFE MODE")
print("Press ALT to disable WRITE mode")

power_led.value = False  # Turn off LED before entering loop
read_only = False  # Default
for _ in range(20):
    power_led.value = not power_led.value  # Toggle LED on/off to signal
    time.sleep(0.25)
    if safe.value is False:
        print("Safe Mode Enabled")
        time.sleep(1)
        microcontroller.on_next_reset(microcontroller.RunMode.SAFE_MODE)
        microcontroller.reset()
    if wrp.value is False:
        print("Write Mode Disabled")
        read_only = True
else:
    storage.remount("/", readonly=read_only)
    print("Starting ARMACHAT...")
    time.sleep(0.5)
