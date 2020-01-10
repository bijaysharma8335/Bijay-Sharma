# OPTIMUS-LEARNING:
A repository for our day-to-day projects at OptimusLogic

# Problem Definition
Read words from a file and count the occurence of words in the file

# Solution:
-programming language used:python3
-import required  libraries
-open a file in read mode and display its content
-display the total counts in words
-function to count the occurance of words

# Algorithm:
Step 1:Open the text file in read mode.
Step 2:Read & store data in variable.
Step 3:Print contents of text file stored in variable.
Step 4:Declare a empty dictionary for holding count values of each word.
step 5:Remove whitespaces,change the words into lowercase.
Step 6:Remove punctuation by empty space and split the file data into words.
Step 7:Calculate the total number od words in file.
Step 8:Print the total number of words.
Step 9:for loop to iterate through the words.
        for word in words:
        
        if word in d:
            d[word]=d[word]+1
        else:
            d[word]=1
Step 10:Print the words along with their occurance.

# User manual:
1.Enter the text filename along  new.txt format when prompted for the filename.
2.The output will be displayed as follows:
-The contents of the given filename.
-Number of words in the file.
-A table form containing the words along with their occurance.
