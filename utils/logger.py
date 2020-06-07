#!/usr/bin/python
# -*- coding: utf-8 -*-

from config import settings
# from config import LOG_BASE_PATH

"""
Multiprocess logger
"""

from logging.handlers import RotatingFileHandler
import multiprocessing, threading, logging, sys, traceback
#logging.basicConfig(level=logging.ERROR)

class LoggerFactory(object):
    
    instances = {}
    
    @staticmethod
    def getInstance(logName):
        if not logName in LoggerFactory.instances:
            LoggerFactory.instances[logName] = create_logger(settings.LOG_BASE_PATH, logName, u'%s.log' % logName.lower())
        return LoggerFactory.instances[logName]
    
            
def create_logger(path, logger_name, logger_file_name):
    logger = logging.getLogger(logger_name)
    logger.propagate = False
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    handler = MultiProcessingLog("%s/%s" % (path, logger_file_name),
                                          maxBytes=1024 * 1024 * 50,  # 50 MB
                                          backupCount=5,  # num files 
                                          delay=1  # wait to create file 
                                          )
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    
    if settings.DEBUG and logger_name != 'downloader':
        logger.setLevel(logging.DEBUG)
        # add console output
        logger.addHandler(logging.StreamHandler(sys.stdout))
    
    return logger   


class MultiProcessingLog(logging.Handler):
    def __init__(self, filename, mode='a', maxBytes=0, backupCount=0, encoding=None, delay=0):
        logging.Handler.__init__(self)

        self._handler = RotatingFileHandler(filename, mode=mode, maxBytes=maxBytes,
                                            backupCount=backupCount, encoding=encoding, delay=delay)
        self.queue = multiprocessing.Queue(-1)

        t = threading.Thread(target=self.receive)
        t.daemon = True
        t.start()

    def setFormatter(self, fmt):
        logging.Handler.setFormatter(self, fmt)
        self._handler.setFormatter(fmt)

    def receive(self):
        while True:
            try:
                record = self.queue.get()
                self._handler.emit(record)
            except (KeyboardInterrupt, SystemExit):
                raise
            except EOFError:
                break
            except:
                traceback.print_exc(file=sys.stderr)

    def send(self, s):
        self.queue.put_nowait(s)

    def _format_record(self, record):
        # ensure that exc_info and args
        # have been stringified.  Removes any chance of
        # unpickleable things inside and possibly reduces
        # message size sent over the pipe
        if record.args:
            record.msg = record.msg % record.args
            record.args = None
        if record.exc_info:
            dummy = self.format(record)
            record.exc_info = None

        return record

    def emit(self, record):
        try:
            s = self._format_record(record)
            self.send(s)
        except (KeyboardInterrupt, SystemExit):
            raise
        except:
            self.handleError(record)

    def close(self):
        self._handler.close()
        logging.Handler.close(self)


