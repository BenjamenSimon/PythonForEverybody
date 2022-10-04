
## Assignment 6.5

text = "X-DSPAM-Confidence:    0.8475"

loc = text.find(' ')

text_cut = text[loc:]

num = text_cut.strip()

print(float(num))



## Assignment 7.1

fname = input("Enter file name: ")

fh = open(fname)

for line in fh:
    line_stripped = line.rstrip()
    print(line_stripped.upper())


## Assignment 7.2

# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")

fh = open(fname)

count = 0
nums = 0

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    nums = nums + float(line[19:])
    count = count+1
    
print("Average spam confidence:", nums/count)


## Assignment 8.4

fname = input("Enter file name: ")
fh = open(fname)

lst = list()

for line in fh:
    line_split = line.split()
    for eachword in line_split :
        if eachword not in lst :
            lst.append(eachword)
    
lst.sort()
print(lst)


## Assignment 8.5

fname = input("Enter file name: ")
fh = open(fname)

count = 0

for line in fh:
    if line.startswith("From") :
        line_split = line.split()
        if line_split[0] == "From" :
            print(line_split[1])
            count = count + 1

print("There were", count, "lines in the file with From as the first word")


## Assignment 9.4

fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"
fh = open(fname)

counts = dict()

for line in fh:
    if line.startswith("From ") :
        line_split = line.split()
        if line_split[0] == "From" :
            counts[line_split[1]] = counts.get(line_split[1], 0)+1

max_count = max(counts.values())            
for k,v in counts.items() :
    if v == max_count :
        print(k, v)
    
    
## Assignment 10.2

fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"
fh = open(fname)

counts = dict()

for line in fh:
    if line.startswith("From ") :
        line_split = line.split()
        time_split = line_split[5].split(':')
        counts[time_split[0]] = counts.get(time_split[0], 0)+1

sorted_counts = sorted(counts.items())

for k,v in sorted_counts:
    print(k,v)
    