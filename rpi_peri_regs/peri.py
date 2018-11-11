import os
import mmap
import ctypes
import rpi_peri_regs.buffer as buffer
import rpi_peri_regs.periaccess as periaccess

class peri(object):

    def __init__(self):
        bcm = ctypes.cdll.LoadLibrary("libbcm_host.so")
        addr = bcm.bcm_host_get_peripheral_address()
        size = bcm.bcm_host_get_peripheral_size()
        del(bcm)

        fd = os.open('/dev/mem', os.O_RDWR | os.O_SYNC)

        self.map = mmap.mmap(fileno = fd, length = size,
                flags = mmap.MAP_SHARED,
                prot = mmap.PROT_READ | mmap.PROT_WRITE, offset = addr)

        os.close(fd)
        del(fd)

        with buffer.buffer(self.map) as buf:
            self.periaddr = buf.get_addr()

    def close(self):
        del(self.periaddr)
        self.map.close()
        del(self.map)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, value, traceback):
        self.close()
        return exc_type is None

    def __getitem__(self, key):
        return periaccess.read4(self.periaddr + key)

    def __setitem__(self, key, value):
        periaccess.write4(self.periaddr + key, value)
