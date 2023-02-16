# Spatic-Assignment
You are given a dataset which consists of entries with latitude, longitude, and name (link to the dataset file is given below along with some helpful materials).  Your task is to write a Python program that will identify entries which are within 200 meters of each other and have similar names i.e. strings that are similar, but not necessarily same 

For example: 
	Bangalore and Bangaloore
new delhi and NewDelhi

Similarity Criteria:
   Similar points should be within 200 meters distance from each other
   Maximum number of single-character edits (insertions, deletions or substitutions) required to change one word into the other should be less than 5
# Approach used by me
As given in the assignment I have to find the names that are similar and are around 200 metre in distance from each other. For this I sorted my csv file using .sort_values() function based on the name ,latitides and longitudes. After sorting the file I ran some test cases to find the distance between coordinates and I got to know that they are almost less than 200 metre in distance. After that I imported the difflib module of python that helped me in comparison of values of name column. I gave in the input of the name column. It gave me the output as 1 for the names that are similar and have minimum levensthien distance and it returned 0 as output for dissimilar names.
