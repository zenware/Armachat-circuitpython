import board
import time
from armachat import config
from pwmio import PWMOut
from analogio import AnalogIn


def beep():
    audioPin = PWMOut(board.GP0, duty_cycle=0, frequency=440, variable_frequency=True)
    audioPin.frequency = 5000
    audioPin.duty_cycle = 1000 * config.volume
    time.sleep(0.002)
    audioPin.duty_cycle = 0
    audioPin.deinit()


def ring():
    audioPin = PWMOut(board.GP0, duty_cycle=0, frequency=440, variable_frequency=True)
    audioPin.frequency = 2000
    audioPin.duty_cycle = 1000 * config.volume
    time.sleep(0.1)
    audioPin.frequency = 3000
    audioPin.duty_cycle = 1000 * config.volume
    time.sleep(0.1)
    audioPin.frequency = 6000
    audioPin.duty_cycle = 1000 * config.volume
    time.sleep(0.1)
    audioPin.duty_cycle = 0
    audioPin.deinit()


def get_vsys_voltage():
    VSYS_voltage = AnalogIn(board.VOLTAGE_MONITOR)
    VSYSin = ((VSYS_voltage.value * 3.3) / 65536) * 3
    return VSYSin
