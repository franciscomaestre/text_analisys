from cache.file_storage import FileStorage
from config import settings
import sys

class FileStorageFactory(object):
    
    instances = {}
    fixed_instances = {}
    
    @staticmethod
    def getFileStorage(extraPath):
        # extraPath have to start by /
        if not extraPath in FileStorageFactory.instances:
            FileStorageFactory.instances[extraPath] = FileStorage(
                                                                  settings.STORAGE_CACHE_PATH + extraPath,
                                                                  {
                                                                   'timeout':settings.STORAGE_CACHE_TIMEOUT,
                                                                   'compress':settings.STORAGE_CACHE_COMPRESS,
                                                                   'max_entries': '99999',
                                                                   'cull_frequency': 10
                                                                   }
                                                                )
        return FileStorageFactory.instances[extraPath]

