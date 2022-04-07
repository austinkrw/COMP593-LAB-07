def main():
    dic_main = (
        ["name", "austin"], 
        ["student ID", 10258634], 
        ["pizza_toppings", ["maggot cheese", "tuna eyeballs", "sheep penis"]],
        ["movies", [("Pain and Gain", "action comedy"), ("Norbit", "comedy")]]
        )

    print(dic_main)

    dic_main[3]["movies"].append ("Four Brothers", "crime drama")
    
    print(dic_main)

main()