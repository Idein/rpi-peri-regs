import rpi_peri_regs.peri
from rpi_peri_regs.regs import *

def test_info():

    def b(v, msb, lsb):
        return (v >> lsb) & ((1<<(msb-lsb+1))-1)

    def show_info(peri):
        print('DBCFG:   0x%08x' % peri[V3D_DBCFG])
        print('DBSCS:   0x%08x' % peri[V3D_DBSCS])
        print('DBSCFG:  0x%08x' % peri[V3D_DBSCFG])
        print('DBSSR:   0x%08x' % peri[V3D_DBSSR])
        print('DBSDR0:  0x%08x' % peri[V3D_DBSDR0])
        print('DBSDR1:  0x%08x' % peri[V3D_DBSDR1])
        print('DBSDR2:  0x%08x' % peri[V3D_DBSDR2])
        print('DBSDR3:  0x%08x' % peri[V3D_DBSDR3])
        print('DBQRUN:  0x%08x' % peri[V3D_DBQRUN])
        print('DBQHLT:  0x%08x' % peri[V3D_DBQHLT])
        print('DBQSTP:  0x%08x' % peri[V3D_DBQSTP])
        print('DBQITE:  0x%08x' % peri[V3D_DBQITE])
        print('DBQITC:  0x%08x' % peri[V3D_DBQITC])
        print('DBQGHC:  0x%08x' % peri[V3D_DBQGHC])
        print('DBQGHG:  0x%08x' % peri[V3D_DBQGHG])
        print('DBQGHH:  0x%08x' % peri[V3D_DBQGHH])
        print('DBGE:    0x%08x' % peri[V3D_DBGE])
        print('FDBG0:   0x%08x' % peri[V3D_FDBG0])
        print('FDBGB:   0x%08x' % peri[V3D_FDBGB])
        print('FDBGR:   0x%08x' % peri[V3D_FDBGR])
        print('FDBGS:   0x%08x' % peri[V3D_FDBGS])
        print('ERRSTAT: 0x%08x' % peri[V3D_ERRSTAT])

    with rpi_peri_regs.peri.peri() as peri:
        v = peri[V3D_IDENT0]
        if v == (2<<24) | (ord('D')<<16) | (ord('3')<<8) | (ord('V')<<0):
            print('V3D is enabled')
            show_info(peri)
        else:
            print('V3D is NOT enabled: 0x%08x' % v)
