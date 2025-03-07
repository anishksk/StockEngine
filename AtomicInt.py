import threading
import requests

class AtomicInt:
    def __init__(self, val):
        self.val = val
        self.lock = threading.Lock() # a lock that is used to help with atomicity

    def get(self):
        """
        Helps retrieve the value safely.
        """
        return self.val

    def set(self, newVal):
        """
        The function allows for a new value to be set safely.
        """
        with self.lock:
            self.val = newVal

