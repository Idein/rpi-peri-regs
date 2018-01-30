import rpi_peri_regs.peri
from rpi_peri_regs.regs import *

def test_ident():
    with rpi_peri_regs.peri.peri() as peri:
        v = peri[V3D_IDENT0]
        if v == (2<<24) | (ord('D')<<16) | (ord('3')<<8) | (ord('V')<<0):
            print('V3D is enabled')
        else:
            print('V3D is NOT enabled: 0x%08x' % v)
