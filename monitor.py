from utils import sleep_func


def vitals_ok(temperature, pulseRate, spo2):
    if temperature not in range(95, 102) or pulseRate not in range(60, 100) or spo2 < 90:
        if temperature not in range(95, 102):
            print('Temperature critical!')
        if pulseRate not in range(60, 100):
            print('Pulse Rate is out of range!')
        if spo2 < 90:
            print('Oxygen Saturation out of range!')
        sleep_func()
        return False
    return True