import urllib
import sys
import itertools as it
import time
import os

# first parameter is the base link
# second parameter is the limit for generated numbers. default is 10
# example use: python http://arsiv.aa.com/abc/def{0:02d}/def{1:02d}fff.zip 3
# downloaded urls for example:
# http://arsiv.aa.com/abc/def00/def00fff.zip
# http://arsiv.aa.com/abc/def00/def01fff.zip
# http://arsiv.aa.com/abc/def00/def02fff.zip
# http://arsiv.aa.com/abc/def01/def00fff.zip
# http://arsiv.aa.com/abc/def01/def01fff.zip
# http://arsiv.aa.com/abc/def01/def02fff.zip
# http://arsiv.aa.com/abc/def02/def00fff.zip
# http://arsiv.aa.com/abc/def02/def01fff.zip
# http://arsiv.aa.com/abc/def02/def02fff.zip
start_time = time.time()

file_count = 1
url_with_format = sys.argv[1]
times = 10
if len(sys.argv) > 2:
    times = int(sys.argv[2])

generated_range = range(0, times)
argument_count = url_with_format.count("d}")

arg_space = []

for i in range(argument_count):
    arg_space.append(generated_range)

arguments = it.product(*arg_space)
sample = it.product(*arg_space)


params = list(sample)[0]
first_url = url_with_format.format(*params)
filename, extension = os.path.splitext(first_url)
for args in arguments:
    url = url_with_format.format(*args)
    response = urllib.urlopen(url)
    if response.getcode() == 404:
        urllib.urlretrieve(url, "file" + str(file_count) + extension)
        file_count += 1
