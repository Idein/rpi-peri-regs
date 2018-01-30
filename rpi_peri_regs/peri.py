import os
import mmap
import ctypes
import struct

class peri(mmap.mmap):

    def __new__(self):
        bcm = ctypes.cdll.LoadLibrary("libbcm_host.so")
        addr = bcm.bcm_host_get_peripheral_address()
        size = bcm.bcm_host_get_peripheral_size()
        del(bcm)

        fd = os.open('/dev/mem', os.O_RDWR | os.O_SYNC)

        peri = super().__new__(self, fileno = fd, length = size,
                flags = mmap.MAP_SHARED,
                prot = mmap.PROT_READ | mmap.PROT_WRITE, offset = addr)

        os.close(fd)
        del(fd)

        return peri

    def __getitem__(self, key):
        self.seek(key)
        return struct.unpack('I', self.read(4))[0]

    def __setitem__(self, key, value):
        self.seek(key)
        self.write(struct.pack('I', value))
