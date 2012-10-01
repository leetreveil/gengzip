gengzip
------------
Python generators are cool. The ``` compress() ``` function returns a python generator with the gzipped data.


usage
-----------------

```python
input = ['123', '45']
# compress() returns a python generator object
for compressed in compress(input):
    print compressed
```

gzip data and write to file:

```python
input = ['123', '45']
with open('output.gz', 'w') as f:
    for compressed in compress(input):
        f.write(compressed)
```