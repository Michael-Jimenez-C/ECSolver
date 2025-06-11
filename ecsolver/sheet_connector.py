import random
import re
import numpy as np

class TestSheetConnector():
    def __init__(self):
        self.cache = {}

    def get_range(self, start, end):
        print(start, end)
        if f"{start}:{end}" in self.cache:
            return self.cache[f"{start}:{end}"]
        pattern = re.compile(r'([A-Z]+)([0-9]+)')
        start_val = pattern.match(start).groups()[:]
        end_val = pattern.match(end).groups()[:]

        start_col = sum([(ord(i)-ord('A')+1)*(ord('Z')-ord('A')+1)**j for j, i in enumerate(reversed(start_val[0]))])
        end_col = sum([(ord(i)-ord('A')+1)*(ord('Z')-ord('A')+1)**j for j, i in enumerate(reversed(end_val[0]))])
        range = (int(start_val[1]), start_col, int(end_val[1]), end_col)

        self.cache[f"{start}:{end}"]=np.random.randint(1, 255, (range[2]-range[0]+1, range[3]-range[1]+1))
        return self.cache[f"{start}:{end}"]
    def get(self, cell):
        if cell in self.cache:
            return self.cache[cell]
        self.cache[cell] = random.randint(1, 255)
        return self.cache[cell]