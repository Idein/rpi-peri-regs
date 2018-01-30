# rpi-peri-regs

A Python driver for accessing peripheral memory (e.g. V3D) on Raspberry Pi.

The register definitions are derived from
<code>[Brcm_Android_ICS_Graphics_Stack](https://docs.broadcom.com/docs/12358546)/brcm_usrlib/dag/vmcsx/vcinclude/bcm2708_chip/</code>.

## Requirements

Because it accesses the peripheral through `/dev/mem`, you need to be root to
run this driver.


## Installation

```
$ git clone https://github.com/Idein/rpi-peri-regs.git
$ cd rpi-peri-regs/
$ python setup.py build
$ sudo python setup.py install
```


## Testing

```
$ pip install nose
$ sudo nosetests -v -s
```
