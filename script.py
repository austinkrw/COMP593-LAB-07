def main():
    dic_main = {
        "name": "austin",
        "student ID": 10258634, 
        "pizza toppings": ["maggot cheese", "tuna eyeballs", "sheep penis"],
        "movies": [{"Pain and Gain":"action comedy"}, {"Norbit": "comedy"}]
    }

    dic_main["movies"].append({"Four Brothers": "crime drama"})

    new_toppings = ("warthog anus", "cobra hearts")
    addToppings(dic_main, new_toppings)

    printing(dic_main)

def addToppings(structure, toppings):
    for n in toppings:
        structure["pizza toppings"].append(n)
    structure["pizza toppings"].sort()

def printing(structure):
    print("Hi Joe, my name is ", structure["name"], ", and my student ID is ", structure["student ID"], ".", "\n", end = "", sep = "")
    
    toppings_list_length = ((len(structure["pizza toppings"])) -1)
    last_topping = ((len(structure["pizza toppings"])) -1)
    print("My ideal pizza has ", end = "")
    for n in range(toppings_list_length):
        print(structure["pizza toppings"][n], ", ", end = "", sep = "")
    print("and ", structure["pizza toppings"][last_topping], ".", "\n", end = "", sep = "")
    
    genre_list_length = ((len(structure["movies"])) -1)
    last_genre = ((len(structure["movies"])) -1)
    print("I like to watch ", end = "")
    for n in range(genre_list_length):
        for key in structure["movies"][n].values():
            print(key, ", ", sep = "", end = "")
    for key in structure["movies"][last_genre].values():
        print("and ", key, " movies.", "\n", sep = "", end = "")
    
    movie_list_length = ((len(structure["movies"])) -1)
    last_movie = ((len(structure["movies"])) -1)
    print("Some of my favourites are ", sep = "", end = "")
    for n in range(movie_list_length):
        for key in structure["movies"][n].keys():
            print(key, ", ", sep = "", end = "")
    for key in structure["movies"][last_movie].keys():
        print("and ", key, "!", sep = "", end = "")


main()