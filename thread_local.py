#  coding: utf-8
import time
from threading import local, Thread
from thread import get_ident

_my_threadlocal = local()


def thread_a():
    time.sleep(1)
    ident = get_ident()
    print "thread_a", ident
    _my_threadlocal.value = ident
    time.sleep(4)
    print "thread_a", _my_threadlocal.value


def thread_b():
    time.sleep(2)
    ident = get_ident()
    print "thread_b", ident
    _my_threadlocal.value = ident
    time.sleep(1)
    print "thread_b", _my_threadlocal.value


def parent():
    Thread(target=thread_a).start()
    Thread(target=thread_b).start()
    print "parent done"


if __name__ == "__main__":
    parent()
