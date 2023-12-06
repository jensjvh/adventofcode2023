with open("input.txt", "r") as inputs:
    res = []
    for game in inputs:
        powers = 1
        colours = {"red": 0, "green": 0, "blue": 0}
        game = game.strip().split(":")
        
        for round in game[1].split("; "):
            round = round.strip().split(", ")
            
            for colour in round:
                colour = colour.split(" ")
                if colours[colour[1]] < int(colour[0]):
                    colours[colour[1]] = int(colour[0])

        for _, value in colours.items():
            powers *= value

        res.append(powers)
    
    print(sum(res))

    