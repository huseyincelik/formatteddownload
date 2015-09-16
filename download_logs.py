import urllib
import sys
import itertools
import time
import os

start_time = time.time()

file_count = 1
url_with_format = sys.argv[1]
times = 10
if len(sys.argv) > 2:
    times = int(sys.argv[2])

generated_range = range(1, times + 1)
argument_count = url_with_format.count("d}")
arg_space = itertools.permutations(generated_range, argument_count)
sample = itertools.permutations(range(0, argument_count), argument_count)
first_url = url_with_format.format(list(sample)[0])
filename, extension = os.path.splitext(first_url)
for args in arg_space:
    url = url_with_format.format(args)
    response = urllib.urlopen(url)
    if response.getcode() == 404:
        urllib.urlretrieve(url, "file" + str(file_count) + extension)
        file_count += 1
