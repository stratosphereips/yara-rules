#!/usr/bin/env python3
import sys,os
import tenjin
from tenjin.helpers import *

eng = tenjin.Engine(postfix='.pyyar', cache=tenjin.MemoryCacheStorage())

def die(s):
  sys.stderr.write(s)
  quit(1)

def main(cr):
  global eng
  path = 'countries/{}-ipv6.zone'.format(cr)
  
  if not os.path.exists(path):
    die('Error: {} doesn\'t exists\n'.format(path))

  addrs = []
  with open(path, 'r') as fd:
    lines = fd.readlines()
  for line in lines:
    if line[0] == '#' or len(line) == 0:
      continue
    addrs.append(line[0:line.find('::')] + ':')
  
  output = eng.render(':rule', context={
    'cr':cr, 'addrs': addrs
  })
  print(output)

if __name__ == '__main__':
  if len(sys.argv) != 2 or len(sys.argv[1]) != 2:
    die('{} <country_code>\n'.format(sys.argv[0]))
  main(sys.argv[1])
