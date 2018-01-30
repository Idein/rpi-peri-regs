import random
import rpi_peri_regs.peri
from rpi_peri_regs.regs import *

def test_scratch():
    N = 512
    with rpi_peri_regs.peri.peri() as peri:
        for i in range(N):
            r = random.randint(0, 2**32-1)
            peri[V3D_SCRATCH] = r
            v = peri[V3D_SCRATCH]
            if v != r:
                raise RuntimeError("Differ at i=%d: "
                        "actual=0x%08x expected=0x%08x" % (i, v, r))
