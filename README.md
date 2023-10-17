# Movie-Recommend-Software
A portfolio project at my coding bootcamp
## Description
This program returns users recommanded *1990's movies* as the output of listing node's value. The program takes in three inputs as conditions of serach that are movie genre, movie title, and keyword, 
then it searches movies stored in nested linked lists which meet the conditions of the three inputs. 

The program is consited of three files:
- movie_list.py   Contains the data of 1990's movies
- linkelist.py    Node class and LinkeList class are written on
- main.py         Performs receiving user inputs and searches for the movies stored in node calss as values.

The original movie data is stored in movielist.py, and they are each stored as values of node class in linkedlists.py. Nodes are separetely instanciated by movie genres in Linked List class from 
linkedlist.py, and each of those linked lists has the head node that contains the name of the genre as its value. Those head nodes are also separately contained in another linked list. This 
chaining of head nodes enables quick retreaving the movies which are in the genre users input. For the searches of using movie title and keyword, pattern serach algorim is employeed that is in 
main.py. My version of pattern search itelates through every element which is an array of strings from a given movie data, and compared the given value(pattern) and the strings in the array in 
order to find a match pattern. This function doesn't mordifies the input movie data, it only returns boolean value. 

Program is written only by python. *Linkelist* Data Structure and a *Patter Search Algorithm* are applied.

## Usage
main.py automatically starts the program as it is run, hence clone this repositry and run the main are only needed to start.
