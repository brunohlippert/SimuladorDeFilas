import time

def current_milli_time():
    return round(time.time() * 1000)

def muda_base_de_numero(a, b, numero):
    return (b - a) * numero + a