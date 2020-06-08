import threading


class CallbackWait(object):
    """
    Utility class. 
    Stop thread execution until external signal or timeout (seconds). 
    
    Usage:
          callbackWait = CallbackWait()
          ... call long time function or thread
              call_function(params, callbackWait)
              
          callbackWait.wait(timeout)  # wait timeout or release in call_function  
    """
    
    def __init__(self):
        self.cond = threading.Condition(threading.Lock())  
    def wait(self, timeout):
        self.cond.acquire()
        try:
            self.cond.wait(timeout)
        finally:
            self.cond.release()    
    def release(self):
        self.cond.acquire()
        try:
            self.cond.notify()
        finally:
            self.cond.release()
