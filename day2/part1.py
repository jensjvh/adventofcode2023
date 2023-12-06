with open("input.txt", "r") as inputs:
    colours = {"red": 12, "green": 13, "blue": 14}
    res = []
    for game in inputs:
        game = game.strip().split(":")
        possible = True
        
        for round in game[1].split("; "):
            round = round.strip().split(", ")
            
            for colour in round:
                colour = colour.split(" ")
                if colours[colour[1]] < int(colour[0]):
                    print(f"{game[0]} not possible")
                    possible = False
            
        
        if possible == False:
            continue

        res.append(int(game[0].split(" ")[1]))
    
    print(sum(res))

    