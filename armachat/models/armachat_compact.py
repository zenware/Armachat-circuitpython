import board
import busio
from armachat.models import DeviceModel


class ARMACHATCompact(DeviceModel):
    """

    """
    def __init__(self):
        self.model_name = 'ARMACHAT Compact'
        self.display, self.display_bus = self.init_display()
        super().__init__()

    def init_display(self):
        import displayio
        import adafruit_st7789

        display_bus = displayio.FourWire(busio.SPI(board.GP18, board.GP19), command=board.GP16, chip_select=board.GP21)
        display = adafruit_st7789.ST7789(display_bus, rotation=270, width=320, height=240, backlight_pin=board.GP20)

        return display, display_bus

    def init_speaker(self):
        pass

    def init_radio(self):
        pass

    def get_radio_status(self):
        pass
