import datetime
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import re
from itertools import tee, filterfalse

datepattern = re.compile('(Mon|Tue|Wed|Thu|Fri|Sat|Sun) \d+ (Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec) \d{4} \d{2}:\d{2}:\d{2} (AM|PM) .*')
resultpattern = re.compile('.*(\d+) received.*')

def load_dataset(log_file):
    lines = open(log_file).readlines()
    lines = [l.strip() for l in lines]

    result = []
    dt = None
    for line in lines:
        #print (line)  
        if datepattern.match(line) is not None:
            date = line
            date_notz = date[:date.rfind(' ')]
            dt = datetime.datetime.strptime(date_notz, '%a %d %b %Y %I:%M:%S %p')
        result_match = resultpattern.match(line)
        if result_match is not None:
            received = int(result_match.group(1))
            result.append((dt, received))

    return result
