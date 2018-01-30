from distutils.core import setup

# Note:
#   - For packaging, see http://www.diveintopython3.net/packaging.html
#   - Calculate version by using https://www.pakin.org/~scott/ltver.html

setup(
        name = "rpi-peri-regs",
        packages = ["rpi_peri_regs"],
        version = "0.0.0",
        description = "Peripheral memory mapper for Raspberry Pi",
        author = "Sugizaki Yukimasa",
        author_email = "ysugi@idein.inc",
        url = "https://github.com/Idein/rpi-peri-regs",
)
