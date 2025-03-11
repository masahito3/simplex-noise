# Simplex noise

## Overview

This is a Simplex noise implementation in Python.  
It is used in my blog about Simplex noise.  

[Take it easy with Simplex noise](https://sioramen.sub.jp/blog3/2025/02/01/take-it-easy-with-simplex-noise/)  
  
[ゆっくりSimplex noiseしていってね](https://sioramen.sub.jp/blog2/blog/2025/01/28/%e3%82%86%e3%81%a3%e3%81%8f%e3%82%8asimplex-noise-%e3%81%97%e3%81%a6%e3%81%84%e3%81%a3%e3%81%a6%e3%81%ad/)  

![image](etc/simplex2d-10x10.svg)  

## Requirement

It runs on Pyhton 3.8 or later and Linux. It hasn't been confirmed to run on Windows.  
The python modules Numpy, Matplotlib are required.  

## Usage

When used in a command terminal  
$ python3 ./simplex2d.py  

Or in a Python program, used as a module   
...  
from simplex2d import *  
v=simplex2d(0.5,0.5)  

## Reference


[https://userpages.cs.umbc.edu/olano/s2002c36/ch02.pdf](https://userpages.cs.umbc.edu/olano/s2002c36/ch02.pdf)  
[https://github.com/SRombauts/SimplexNoise/blob/master/references/SimplexNoise.java](https://github.com/SRombauts/SimplexNoise/blob/master/references/SimplexNoise.java)  
[https://github.com/stegu/perlin-noise/blob/master/simplexnoise.pdf](https://github.com/stegu/perlin-noise/blob/master/simplexnoise.pdf)  
[https://en.wikipedia.org/wiki/Simplex_noise](https://en.wikipedia.org/wiki/Simplex_noise)  
[https://catlikecoding.com/unity/tutorials/pseudorandom-noise/simplex-noise/](https://catlikecoding.com/unity/tutorials/pseudorandom-noise/simplex-noise/)  

## Author

masahito3  

## License

MIT license.  

## Disclaimer

This software is provided 'as is' without any express or implied warranties, including but not limited to warranties of merchantability or fitness for a particular purpose. The user accepts full responsibility for any damages, losses or liabilities resulting from its use.  



