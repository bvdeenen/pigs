from network import LoRa
import socket
import machine
import time
from binascii import hexlify

name = hexlify(machine.unique_id()).decode('ascii')

def recv():
    print("receiving on {}".format(name))

    lora = LoRa(mode=LoRa.LORA, region=LoRa.EU868)

    s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
    s.settimeout(1.0)

    s.setblocking(True)
    while True:
        # get any data received...
        data = s.recv(64)
        if data:
            print("{}: {}".format(time.time(), data))
        else:
            print("nothing")

def send():
    print("sending on {}".format(name))
    lora = LoRa(mode=LoRa.LORA, region=LoRa.EU868)
    s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
    s.settimeout(1.0)

    s.setblocking(True)
    while True:
        s.send('Hello from {} at {}'.format(name, time.time()))
        # wait a random amount of time
        time.sleep(3 * float(machine.rng()) / 2**24)
        print(time.time())

if __name__ == '__main__':
    run()
