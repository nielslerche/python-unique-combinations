import sys
import json
import itertools

argLst = sys.argv

inp_arg = argLst[1]
out_arg = argLst[2]

inp_file = open(str(inp_arg), 'r').read()
inp = json.loads(inp_file)

out_file = open(str(out_arg), 'w')

def unique_combinations(*args):

    out = None

    for combination in itertools.product(*args):
        out = combination
        print(combination)
        out_file.write(str(out) + "\n")

    out_file.close()

lst = []

for i in inp:

    val = inp.get(i)

    wowLst = []

    for string in val:
        wow = str(string)
        wowLst.append(wow)

    lst.append(wowLst)

print(inp)

unique_combinations(*lst)
