## Notes

# Python Regular Expression Quick Guide

^        Matches the beginning of a line
$        Matches the end of the line
.        Matches any character
\s       Matches whitespace
\S       Matches any non-whitespace character
*        Repeats a character zero or more times
*?       Repeats a character zero or more times 
         (non-greedy)
+        Repeats a character one or more times
+?       Repeats a character one or more times 
         (non-greedy)
[aeiou]  Matches a single character in the listed set
[^XYZ]   Matches a single character not in the listed set
[a-z0-9] The set of characters can include a range
(        Indicates where string extraction is to start
)        Indicates where string extraction is to end


from dataclasses import dataclass
import re

hand = open('mbox-short.txt')

for line in hand:
    line = line.rstrip()
    if line.find('From: ') >= 0:
        print('Method 1:', line)
    if re.search('From: ', line) :
        print('Method 2:', line)
        
    if line.startswith('From: '):
        print('Method 3:', line)
    if re.search('^From: ', line) :
        print('Method 4:', line)
        
import re

x = 'My 2 favourite numbers are 19 and 42'
y = re.findall('[0-9]+', x)
print(y)

y = re.findall('[AEIOU]+', x)
print(y)

'Greedy matching' = unless otherwise specified, the program tries to give you the largest possible matching string, non-greedy returns smallest


'Parentheses' = let you match on a larger sequence but only return part of the sequence

x = open('mbox-short.txt')
for line in x :
    if re.search('^From ', line) :
        y = re.findall('^From (\S+@\S+)', line)
        print(y)


# Method 1
data = 'From stephen.marquard@uct.ac.za Sat Jan   5 09:14:16 2008'

atpos = data.find('@')
print(atpos)
sppos = data.find(' ', atpos)
print(sspos)
host = data[atpos+1 : sppos]
print(host)

# Method 2
words = data.split()
email = words[1]
pieces = email.split('@')
print(pieces[1])

# Method 3
import re
y = re.findall('@([^ ]*)', data) #[^ ] = match a single non-blank character
print(y)
y = re.findall('^From .*@([^ ]*)', data)
print(y)


# Spam confidence exercise with regular expression
import re
hand = open('mbox-short.txt')
numlist = list()

for line in hand:
    line = line.rstrip()
    stuff = re.findall('^X-DSPAM-Confidence: ([0-9.]+)', line)
    if len(stuff) != 1 : continue
    num = float(stuff[0])
    numlist.append(num)
print('Maximum: ', max(numlist))


## Assignemnt Chapter 11

data = open('regex_sum_1654538.txt')
numlist = list()

for line in data :
    stuff = re.findall('[0-9]+', line)
    if len(stuff) == 0 : continue
    for eachnum in stuff :
        numlist.append(int(eachnum))
        
print(sum(numlist))