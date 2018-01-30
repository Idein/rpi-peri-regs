import rpi_peri_regs.peri
from rpi_peri_regs.regs import *

def test_info():

    def b(v, msb, lsb):
        return (v >> lsb) & ((1<<(msb-lsb+1))-1)

    def show_info(peri):
        print('V3D version:',              b(peri[V3D_IDENT0],  31, 24))
        print('VPM memory size:',          b(peri[V3D_IDENT1],  31, 28))
        print('HDR support:',              b(peri[V3D_IDENT1],  27, 24))
        print('Number of semaphores:',     b(peri[V3D_IDENT1],  23, 16))
        print('Number of TMUs per slice:', b(peri[V3D_IDENT1],  15, 12))
        print('Number of QPUs per slice:', b(peri[V3D_IDENT1],  11,  8))
        print('Number of slices:',         b(peri[V3D_IDENT1],   7,  4))
        print('V3D revision:',             b(peri[V3D_IDENT1],   3,  0))
        print('VPM reserved for user:',    b(peri[V3D_VPMBASE], 31,  0))
        print('L2 cache enable:',          b(peri[V3D_L2CACTL],  0,  0))
        print('QPU  0 reservation:',   hex(b(peri[V3D_SQRSV0],   3,  0)))
        print('QPU  1 reservation:',   hex(b(peri[V3D_SQRSV0],   7,  4)))
        print('QPU  2 reservation:',   hex(b(peri[V3D_SQRSV0],  11,  8)))
        print('QPU  3 reservation:',   hex(b(peri[V3D_SQRSV0],  15, 12)))
        print('QPU  4 reservation:',   hex(b(peri[V3D_SQRSV0],  19, 16)))
        print('QPU  5 reservation:',   hex(b(peri[V3D_SQRSV0],  23, 20)))
        print('QPU  6 reservation:',   hex(b(peri[V3D_SQRSV0],  27, 24)))
        print('QPU  7 reservation:',   hex(b(peri[V3D_SQRSV0],  31, 28)))
        print('QPU  8 reservation:',   hex(b(peri[V3D_SQRSV1],   3,  0)))
        print('QPU  9 reservation:',   hex(b(peri[V3D_SQRSV1],   7,  4)))
        print('QPU 10 reservation:',   hex(b(peri[V3D_SQRSV1],  11,  8)))
        print('QPU 11 reservation:',   hex(b(peri[V3D_SQRSV1],  15, 12)))
        print('QPU 12 reservation:',   hex(b(peri[V3D_SQRSV1],  19, 16)))
        print('QPU 13 reservation:',   hex(b(peri[V3D_SQRSV1],  23, 20)))
        print('QPU 14 reservation:',   hex(b(peri[V3D_SQRSV1],  27, 24)))
        print('QPU 15 reservation:',   hex(b(peri[V3D_SQRSV1],  31, 28)))

    with rpi_peri_regs.peri.peri() as peri:
        v = peri[V3D_IDENT0]
        if v == (2<<24) | (ord('D')<<16) | (ord('3')<<8) | (ord('V')<<0):
            print('V3D is enabled')
            show_info(peri)
        else:
            print('V3D is NOT enabled: 0x%08x' % v)
