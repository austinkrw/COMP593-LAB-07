def main():

    dic_main = {
        "name": "austin",
        "student ID": 10258634, 
        "pizza toppings": ["maggot cheese", "tuna eyeballs", "sheep penis"],
        "movies": [{"Pain and Gain":"action comedy"}, {"Norbit": "comedy"}]
    }

    # add a dictionary to the "movies" list of dictionaries
    dic_main["movies"].append({"Four Brothers": "crime drama"})

    # define a tuple with two new pizza toppings
    new_toppings = ("warthog anus", "cobra hearts")

    # call the addTopings function to add the contents of the tuple to the "pizza toppings" list
    addToppings(dic_main, new_toppings)

    # call the printing function to print out sentences containing values from dic_main
    printing(dic_main)

def addToppings(structure, toppings):

    # add each topping in the specified tuple parameter to the "pizza toppings" list
    for n in toppings:
        structure["pizza toppings"].append(n)
    # sort the "pizza toppings" list alphabetically
    structure["pizza toppings"].sort()

def printing(structure):

    print("Hi Joe, my name is ", structure["name"], ", and my student ID is ", structure["student ID"], ".", "\n", end = "", sep = "")
    
    # retrieve the length of the "toppings list" so it can be iterated through fully even if more toppings have been added
    toppings_list_length = ((len(structure["pizza toppings"])) -1)
    # retrieve the index of the last pizza topping to specifically format it when it is printed later
    last_topping = ((len(structure["pizza toppings"])) -1)
    print("My ideal pizza has ", end = "")
    # iterate through each index in the "pizza toppings" list and print each respective topping
    for n in range(toppings_list_length):
        print(structure["pizza toppings"][n], ", ", end = "", sep = "")
    # print an "and" before the last topping to be gramatically correct
    print("and ", structure["pizza toppings"][last_topping], ".", "\n", end = "", sep = "")
    
    # retrieve the length of the "movies" list of dictionaries so it can be iterated through fully even if more dictionaries are added
    genre_list_length = ((len(structure["movies"])) -1)
    # retrieve the index of the last dictionary in the list to specifically format it when it is printed later
    last_genre = ((len(structure["movies"])) -1)
    print("I like to watch ", end = "")
    # iterate through each index in the "movies" list
    for n in range(genre_list_length):
    # for each index in the list of dictionaries, each dictionary key value is printed
        for key in structure["movies"][n].values():
            print(key, ", ", sep = "", end = "")
    # for the last index in the list of dictionaries, print an "and" before printing the key value to be gramatically correct
    for key in structure["movies"][last_genre].values():
        print("and ", key, " movies.", "\n", sep = "", end = "")
    
    # retrieve the length of the "movies" list of dictionaries so it can be iterated through fully even if more dictionaries are added
    movie_list_length = ((len(structure["movies"])) -1)
    # retrieve the index of the last dictionary in the list to specifically format it when it is printed later
    last_movie = ((len(structure["movies"])) -1)
    print("Some of my favourites are ", sep = "", end = "")
    # iterate through each index in the "movies" list
    for n in range(movie_list_length):
    # for each index in the list of dictionaries, each dictionary key is printed
        for key in structure["movies"][n].keys():
            print(key, ", ", sep = "", end = "")
    # for the last index in the list of dictionaries, print an "and" before printing the key to be gramatically correct
    for key in structure["movies"][last_movie].keys():
        print("and ", key, "!", sep = "", end = "")

main()