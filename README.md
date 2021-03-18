# MTG_UnpackSimulator
a mtg unpack simulator

## requirement
- bs4
- lxml
- requests
- matplotlib
- numpy

## usage
```shell
$ python simulator.py [-h] -v VERSION -t TIMES [-n PACK_NUM]
```
optional arguments:
  - -h, --help              show this help message and exit
  - -v VERSION, --version   VERSION
                          Version of pack
  - -t TIMES, --times       TIMES
                          times for simulates
  - -n PACK_NUM, --pack_num PACK_NUM
                          packs number in each box, default is 36 
## sample

```shell
$ python simulator.py -v M21 -t 1000
```
means unpack 1000 M21 booster boxes
