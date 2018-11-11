import rpi_peri_regs.peri
from rpi_peri_regs.regs import *

def test_ident():
    with rpi_peri_regs.peri.peri() as peri:
        v0 = peri[V3D_IDENT0]
        v1 = peri[V3D_IDENT1]
        v2 = peri[V3D_IDENT2]
        v3 = peri[V3D_IDENT3]

        if v0 == (2<<24) | (ord('D')<<16) | (ord('3')<<8) | (ord('V')<<0):
            print('V3D is enabled')
        else:
            raise RuntimeError('V3D is NOT enabled: 0x%08x' % v0)

        if v0 == v1:
            raise RuntimeError('error: IDENT0 and IDENT1 is the same ' +
                    '(maybe because accessing peripheral with vld/vst (NEON))')

        print("V3D Identification 0 = 0x%08x" % v0)
        print("V3D Identification 1 = 0x%08x" % v1)
        print("V3D Identification 2 = 0x%08x" % v2)
        print("V3D Identification 3 = 0x%08x" % v3)
