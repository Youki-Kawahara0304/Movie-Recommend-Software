import movie_lists
import linkedlist

def populate_list():
    movie_list = linkedlist.LinkedList()
    for genre in movie_lists.genres:
        if genre == None:
            continue
        sublist = linkedlist.LinkedList()
        for movie in movie_lists.movies:
            if genre in movie[1]:
                sublist.insert_beginning(movie)
        sublist.insert_beginning(genre)
        movie_list.insert_beginning(sublist)
    return movie_list

def list_movie_genres():
    i = 1
    for movie_genre in movie_lists.genres:
        if movie_genre == None:
            continue
        print(i, ":", movie_genre)
        i += 1
    print("0: no specific genre\n")
    return i

def search_by_value(lst, value):
    outer_current_node = lst.head_node
    while outer_current_node:
        current_node = outer_current_node.get_value().head_node
        if current_node.get_value() == value:
            return current_node.get_next_node()
        outer_current_node = outer_current_node.get_next_node()

def broad_search(lst, genre):
    movies_in_genre = []
    current_node = search_by_value(lst, genre)
    while current_node:
        if current_node.get_value() != None:
            movies_in_genre.append(current_node.get_value())
        current_node = current_node.get_next_node()
    return movies_in_genre

def retreave_all_movies(lst):
    all_movies = ["All movies"]
    outer_current_node = lst.head_node
    while outer_current_node.get_value():
        current_node = outer_current_node.get_value().head_node
        while current_node.get_value():
            if type(current_node.get_value()) == list and current_node.get_value() not in all_movies:
                all_movies.append(current_node.get_value())
            current_node = current_node.get_next_node()
        outer_current_node = outer_current_node.get_next_node()
    return all_movies
    
def pattern_search(txt, pattern):
    for txt_idx in range(0, len(txt)):
        match_count = 0
        for char in range(0, len(pattern)):
            if pattern[char].upper() == txt[txt_idx + char]:
                match_count += 1
            else:
                break
        if match_count == len(pattern):
            return True
    return False

# greeting
print("""Hi, this is movie recommand software.
This software stores the famous movies that came out in 1990's in it,
If you're interested, it provides you some of those movies with/without a keyword,
or if you have a movie in mind, please tell me the name of that movie.
""")
current_stock = populate_list()

# run searches
print("First, let me know, if you have a specific genre of the movie/n")
num_genres = list_movie_genres()
movie_genre = ""
new_array_of_movies = []
correct_genre = False
while correct_genre == False:
    genre_number = int(input("Please enter the number that is printed on the left to the genre you preferred.\n"))
    if genre_number > num_genres:
        print("the number is not correct")
    else:
        movie_genre = movie_lists.genres[genre_number]
        correct_genre = True
if movie_genre != None:
    new_array_of_movies = broad_search(current_stock, movie_genre)
else:
    new_array_of_movies = retreave_all_movies(current_stock)

print("""
Thank you. Next, do you already have something in mind that you want to watch? 
If so, please type the name in the console or "n" for none 
""")
title = input().upper()
title_match = []
if title != "N":
    for movie in new_array_of_movies:
        if pattern_search(movie[0].upper(), title):
            title_match.append(movie)
    if title == None:
        print("Sorry, we don't have a movie that includes the keyword of {}".format(title))

print("""
Thank you again. Last but not least, if you have some attribute of the movie
such as \"Zombies\", \"Alians\", \"Dinosours\", and so on
Please type anything into the console, or press "n" for none
""")
keyword = input().upper()
keyword_match = []
if keyword != "N":
    for movie in new_array_of_movies:
        for txt in movie:
            if type(txt) == list:
                if keyword in txt:
                    keyword_match.append(movie)
            elif len(txt) >= len(keyword):
                if pattern_search(txt.upper(), keyword):
                    keyword_match.append(movie)
    if keyword_match == None:
        print("Sorry, we don't have a movie that has the title of {}".format(keyword))

print("Serach by genres")
print("--------------------------------------------------")
for movie in new_array_of_movies:
    print("check", movie)
    print(movie[0], "Year", movie[2])
    print("Rate ", movie[3], "Genre", movie[1])
    print(movie[4],"\n")

print("Serach title")
print("--------------------------------------------------")
for movie in title_match:
    print(movie[0], "Year", movie[2])
    print("Rate ", movie[3], "Genre", movie[1])
    print(movie[4], "\n")

print("Serach by keyword")
print("--------------------------------------------------")
for movie in keyword_match:
    print(movie[0], "Year", movie[2])
    print("Rate ", movie[3], "Genre", movie[1])
    print(movie[4], "\n")
            















        


            
        







    


    
    
    
    



