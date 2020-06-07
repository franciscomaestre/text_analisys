"File-based cache backend"
import errno
import io
import os
import tempfile
import zlib
import hashlib

try:
    from cache.utils.six.moves import cPickle as pickle
except ImportError:
    import pickle

from cache.utils.base import DEFAULT_TIMEOUT
from cache.utils.filebased import FileBasedCache
from cache.utils.move import file_move_safe
from cache.utils.encoding import force_bytes

from utils.logger import LoggerFactory
app_cache_logger = LoggerFactory.getInstance('SeoAppCache')


def keyFunction(key, key_prefix, version):
    """
    Default function to generate keys.

    Constructs the key used by all other methods. By default it prepends
    the `key_prefix'. KEY_FUNCTION can be used to specify an alternate
    function with custom key making behavior.
    """
    key = hashlib.md5(force_bytes(key)).hexdigest()
    return '%s:%s:%s' % (key_prefix, version, key)

class FileStorage(FileBasedCache):
    
    instance = None

    def __init__(self, path, params):
        '''
        Constructor
        '''
        params['KEY_FUNCTION'] = keyFunction
        super(FileStorage, self).__init__(path, params)
        self.compress = params.get('compress', False)
        self._subfolder = None
        
    def get(self, key, default=None, version=None):
        try:
            fname = self._key_to_file(key, version)
            if os.path.exists(fname):
                try:
                    with io.open(fname, 'rb') as f:
                        if not self._is_expired(f):
                            if self.compress:
                                return pickle.loads(zlib.decompress(f.read()))
                            else:
                                return f.read()
                except IOError as e:
                    if e.errno == errno.ENOENT:
                        pass  # Cache file was removed after the exists check
        except Exception as ex:
            pass
        return default

    def set(self, key, value, timeout=DEFAULT_TIMEOUT, version=None):
        self._createdir()  # Cache dir can be deleted at any time.
        fname = self._key_to_file(key, version)
        self._createSubFolder()
        self._cull()  # make some room if necessary
        fd, tmp_path = tempfile.mkstemp(dir=self._dir)
        renamed = False
        try:
            with io.open(fd, 'wb') as f:
                if self.compress:
                    expiry = self.get_backend_timeout(timeout)
                    f.write(pickle.dumps(expiry, protocol=pickle.HIGHEST_PROTOCOL))
                    f.write(zlib.compress(pickle.dumps(value, protocol=pickle.HIGHEST_PROTOCOL)))
                else:
                    expiry = self.get_backend_timeout(timeout)
                    f.write(pickle.dumps(expiry, protocol=pickle.HIGHEST_PROTOCOL))
                    f.write(value)
            file_move_safe(tmp_path, fname, allow_overwrite=True)
            renamed = True
            
        finally:
            if not renamed:
                os.remove(tmp_path)
                
    def _key_to_file_old(self, key, version=None):
        """
        Convert a key into a cache file path. Basically this is the
        root cache path joined with the md5sum of the key and a suffix.
        """
        key = self.make_key(key, version=version)
        self.validate_key(key)
        filename = ''.join([hashlib.md5(force_bytes(key)).hexdigest(), self.cache_suffix])
        return os.path.join(self._dir, filename)
    
    def _key_to_file(self, key, version=None):
        """
        Convert a key into a cache file path. Basically this is the
        root cache path joined with the md5sum of the key and a suffix.
        """
        key = self.make_key(key, version=version)
        self.validate_key(key)
        filename = ''.join([hashlib.md5(force_bytes(key)).hexdigest(), self.cache_suffix])
        self._subfolder = os.path.join(self._dir, filename[0:2], filename[2:4])
        return os.path.join(self._dir, filename[0:2], filename[2:4], filename)
    
    def _createSubFolder(self):
        if self._subfolder and not os.path.exists(self._subfolder):
            try:
                os.makedirs(self._subfolder, 0o700)
            except OSError as e:
                if e.errno != errno.EEXIST:
                    raise EnvironmentError(
                        "Cache directory '%s' does not exist "
                        "and could not be created'" % self._subfolder)
     
