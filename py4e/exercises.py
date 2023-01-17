#Strings:
'''Write code using find() and string slicing (see section 6.10) to extract the number at the end of the line below. Convert the extracted value to a floating point number and print it out.
'''
text = "X-DSPAM-Confidence:    0.8475"
spaceIndex = text.find(" ")
print(float(text[spaceIndex+4:]))

#File Handling
'''
Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
X-DSPAM-Confidence:    0.8475
Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below. Do not use the sum() function or a variable named sum in your solution.
You can download the sample data at http://www.py4e.com/code3/mbox-short.txt when you are testing below enter mbox-short.txt as the file name.
'''
# Use the file name mbox-short.txt as the file name
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