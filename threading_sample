import threading
from threading import Event, Thread
from time import sleep
from datetime import datetime as dt
import getpass


def print_sth(evt, evt_end):
    while evt_end.is_set():
        evt.wait()
        print(dt.now().time(), 'print_sth', evt.is_set(), password)
        evt.clear()


def sampler(evt, evt_end):

    i = 0
    con = lambda: i < 5
    while con():
        i += 1
        if not con():
            evt_end.clear()
        evt.set()
        sleep(2)


password = getpass.getpass()

evt = Event()
evt_end = Event()
evt_end.set()

p_sth = Thread(target=print_sth, args=[evt, evt_end])
p_sth.start()

sampler(evt, evt_end)
