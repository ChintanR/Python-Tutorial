# 1.Word Detection

This program practices reading data from a text file using file handling.
It checks whether a specific word exists in the file content or not.
The entire file is read at once and searched using a conditional statement.
It helps in understanding file reading and basic string searching.
The file is properly closed after use.

# 2.High Score

This code demonstrates reading and writing data to a file.
It generates a random score and compares it with a previously stored high score.
If the new score is higher, the file is updated with the latest value.
It helps in learning file update logic and conditional file writing.
The with statement ensures safe file handling.

# 3.Table Generator

This program generates multiplication tables and stores them in separate files.
Each table is written to a file using write mode.
It practices dynamic file creation and writing formatted content.
The program uses functions to organize file operations.
It improves understanding of looping with file handling.

# 4.Word Censor

This code reads content from a file and replaces a specific word.
The modified content is written back to the same file.
It demonstrates file reading, string replacement, and overwriting files.
This exercise helps understand content manipulation inside files.
It is useful for learning basic text processing.

# 5.Multiple Censor

This program extends word replacement to multiple words.
It reads file content once and replaces each unwanted word.
The updated content is written back to the file.
It helps practice looping combined with file operations.
This improves understanding of scalable text filtering.

# 6.Log Scanner

This program checks whether a particular keyword exists in a log file.
The entire file is read and searched using a conditional statement.
It practices file reading and keyword detection.
This exercise is useful for understanding basic log analysis.
It strengthens string search logic with file handling.

# 7.Line Finder

This code reads a file line by line to locate a keyword.
It prints the exact line number where the word is found.
The program stops searching once the word is detected.
It demonstrates line-wise file reading and loop control.
This is useful for debugging and log inspection tasks.

# 8.File Copy

This program copies content from one file to another.
It reads the source file and writes the same content into a new file.
It demonstrates basic file duplication using read and write operations.
This exercise strengthens understanding of file I/O flow.
It is a common real-world file handling use case.

# 9.Content Comparison

This code is designed to verify if two separate text files, file1.txt and file2.txt, are exactly the same. 
It reads the full data from both files and stores them into two distinct variables. 
Using a conditional if statement, it compares these strings for equality. 
Finally, it prints a message to the console confirming whether the files are identical or different.

# 10.File Reset

This concise script serves as a method to quickly clear or initialize a specific file. 
It opens Hi-score.txt using the "w" (write) mode, which automatically truncates or "wipes" the file if it already exists. 
By writing an empty string to the file, the script ensures that the target file is left completely blank. 
This is a common technique for resetting game scores or clearing logs.

# 11.File Cloning

This script demonstrates how to create a duplicate of an existing file. 
It opens a source file named old.txt to read its entire string content into memory. 
Subsequently, it opens (or creates) a second file called renamed_by_python.txt in write mode. 
By writing the stored content into this new file, the script effectively performs a manual "copy and rename" operation.
