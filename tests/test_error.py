import rpi_peri_regs.peri
from rpi_peri_regs.regs import *

def test_info():

    def b(v, msb, lsb):
        return (v >> lsb) & ((1<<(msb-lsb+1))-1)

    def show_info(peri):
        print('L2C AXI receive FIFO overrun error:', b(peri[V3D_ERRSTAT], 15, 15))
        print('VCM error (binner):', b(peri[V3D_ERRSTAT], 14, 14))

    with rpi_peri_regs.peri.peri() as peri:
        v = peri[V3D_IDENT0]
        if v == (2<<24) | (ord('D')<<16) | (ord('3')<<8) | (ord('V')<<0):
            print('V3D is enabled')
            show_info(peri)
        else:
            print('V3D is NOT enabled: 0x%08x' % v)
