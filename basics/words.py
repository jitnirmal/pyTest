from collections import Counter;

cnt = Counter ();

for line in open ('TEST.txt', 'r'):
  for word in line.split ():
    cnt [word] += 1

print cnt