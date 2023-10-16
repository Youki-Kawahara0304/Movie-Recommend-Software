import movie_list
import linkedlist

def populate_list():
    movie_list = LinkedList()
    for genre in movie_lists.genres:
        sublist = LinkedList()
        for movie in movie_lists.movies:
            if genre in movie[1]:
                sublist.insert_beginning(movie)
        sublist.insert_beginning(genre)
        movie_list.insert_beginning(sublist)
    return movie_list

def search_movies(title = None, genre = None, keyword = None):
    desired_movies = []
    if genre != None:
        current_node = movie_list.search_by_value(genre)
        while current_node.get_next_node():
            desired_movies.append(current_node.get_value())
            current_node = current_node.get_next_node()

    else:
        movie_genre = movie_list.head_node
        while movie_genre.next_node:
            movie = movie_genre.get_value()
            current_node = movie.head_node
            while current_node.next_node:
                if not current_node.get_value() in desired_movies:
                    desired_movies.append(current_node.get_value())
                current_node = current_node.get_next_node()
        movie_genre = movie_genre.get_next_node()
    

