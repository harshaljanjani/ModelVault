# REVISITING THE BASICS, IN ORDER TO MOVE ON TO NETWORK PROGRAMMING AND OOPS:

# Strings - Task 1
'''Write code using find() and string slicing (see section 6.10) to extract the number at the end of the line below. Convert the extracted value to a floating point number and print it out.
'''
text = "X-DSPAM-Confidence:    0.8475"
spaceIndex = text.find(" ")
print(float(text[spaceIndex+4:]))

# File Handling - Task 1
'''Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
X-DSPAM-Confidence:    0.8475
Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below. Do not use the sum() function or a variable named sum in your solution.
You can download the sample data at http://www.py4e.com/code3/file-data.txt when you are testing below enter file-data.txt as the file name.
'''
# Use the file name file-data.txt as the file name
fname = input("Enter file name: ")
with open(fname) as f:
    total = 0
    count = 0
    for line in f:
        if line.startswith("X-DSPAM-Confidence:"):
            floatNum = float(line[line.find(" ")+1:])
            total += floatNum
            count += 1
print("Average spam confidence: "+ str(total/count))

# Lists - Task 1
'''Open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the split() method. The program should build a list of words. For each word on each line check to see if the word is already in the list and if not append it to the list. When the program completes, sort and print the resulting words in python sort() order as shown in the desired output.
'''
fname = input("Enter file name: ")
res = []
with open(fname) as file:
    l = file.readlines()
    for x in l:
        i = x.split()
        for y in i:
            if y not in res:
                res.append(y)
    res.sort()
    print(res)
    

# Lists - Task 2
'''Open the file file-data.txt and read it line by line. When you find a line that starts with 'From ' like the following line:
    From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
You will parse the From line using split() and print out the second word in the line (i.e. the entire address of the person who sent the message). Then print out a count at the end.
Hint: make sure not to include the lines that start with 'From:'. Also look at the last line of the sample output to see how to print the count.
You can download the sample data at http://www.py4e.com/code3/file-data.txt'''

fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "file-data.txt"
count = 0
fhand = open(fname, 'r')
for line in fhand:
    if line.startswith('From:'):
        print(line.split(' ')[1])
        count += 1
print("There were", count, "lines in the file with From as the first word")

# Dictionaries - Task 1
'''Write a program to read through the file-data.txt and figure out who has sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.'''

name = input("Enter file:")
if len(name) < 1:
    name = "file-data.txt"
master = dict()
with open(name) as fhand:
    x = fhand.readlines()
    for line in x:
        if(line.startswith('From ')):
            email = line.split()[1]
            master[email] = master.get(email, 0) + 1 # get(email,0) -> return '0' if the key does not exist in the dictionary
            # master[email] += 1 -> Incorrect
    k = max(master, key = lambda x: master[x])
    print(k + " " + str(master[k]))