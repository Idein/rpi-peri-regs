from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
from Cython.Build import cythonize

# Note:
#   - For packaging, see http://www.diveintopython3.net/packaging.html
#   - Calculate version by using https://www.pakin.org/~scott/ltver.html
#   - https://docs.python.org/3/extending/building.html
#   - https://cython.readthedocs.io/en/latest/src/userguide/source_files_and_compilation.html

ext_modules = [
        Extension("rpi_peri_regs.periaccess", ["rpi_peri_regs/periaccess.c"]),
        Extension("rpi_peri_regs.buffer", ["rpi_peri_regs/buffer.pyx"]),
]

setup(
        name = "rpi-peri-regs",
        packages = ["rpi_peri_regs"],
        version = "0.0.0",
        description = "Peripheral memory mapper for Raspberry Pi",
        cmdclass = {'build_ext': build_ext},
        ext_modules = cythonize(ext_modules),
        author = "Sugizaki Yukimasa",
        author_email = "ysugi@idein.inc",
        url = "https://github.com/Idein/rpi-peri-regs",
)
