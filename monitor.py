from utils import sleep_func


def vitals_ok(temperature, pulseRate, spo2):
    if temperature not in range(95,102):
        print('Temperature critical!')
        sleep_func()
    elif pulseRate not in range(60,100):
        print('Pulse Rate is out of range!')
        sleep_func()
    elif spo2 < 90:
        print('Oxygen Saturation out of range!')
        sleep_func()
    else:
        return True
