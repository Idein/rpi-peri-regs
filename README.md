# rpi-peri-regs

A Python driver for accessing peripheral memory (e.g. V3D) on Raspberry Pi.


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
$ nosetests -v -s
```
