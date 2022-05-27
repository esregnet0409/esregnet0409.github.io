#!/usr/bin/env python3

import subprocess
rc = subprocess.call('./get_category.sh')

import os
files = os.listdir(".")

if not os.path.isfile("_README.md"):
  print("There is no _README.md file")
  exit(1)

fp = open("_README.md", 'r')
lines = fp.readlines()

fp2 = open("README.md", 'w')
fp2.writelines(lines)

for file in files:
  if file[-3:] != ".md":
    continue
  elif "_category_" in file:
    fp2.write("{}\n".format(file))
    fp2.write("---\n")
    fp2.write("\n")
    fp2.write("\n")
    
    fp3 = open(file, 'r')
    lines = fp3.readlines()
    fp2.writelines(lines)
    fp2.write("\n")
    fp2.write("\n")
