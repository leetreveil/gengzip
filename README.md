[![Build Status](https://secure.travis-ci.org/leetreveil/gengzip.png)](http://travis-ci.org/leetreveil/gengzip)

gengzip
------------
Python generators are cool. The ``` compress() ``` function returns a python generator with the gzipped data.


usage
-----------------

```python
input = ['123', '45']
# compress() returns a python generator object
for compressed in gengzip.compress(input):
    print compressed
```

gzip data and write to file:

```python
input = ['123', '45']
with open('output.gz', 'w') as f:
    for compressed in gengzip.compress(input):
        f.write(compressed)
```

licence
-----------------

(The MIT License)

Copyright (c) 2012 Lee Treveil <leetreveil@gmail.com>

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the 'Software'), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
