file1 = open('sample.txt','r')
if file1:

    print(file1.read())
else:
    print("Error: the 'sample.text' was not found.")

file1.close()

#TASK 2
file2 = open('output.txt', 'w')
writting_file=file2.write('Enter text to write to the file: Hello, Python!\nData successfully written to output.txt.\nEnter additional text to append: Learning file handling in Python.\nData successfully appended.\nFinal content of output.txt:\nHello, Python!\nLearning file handling in Python.')
file2.close()



file2 = open('output.txt', 'r')
reading_file = file2.read()
print(reading_file)
file2.close()