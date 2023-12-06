with open("input.txt", "r") as inputs:
    #Represent amount of cubes in the bag in a dictionary
    colours = {"red": 12, "green": 13, "blue": 14}
    res = []
    
    for game in inputs:
        #Separate each line in the input file at ":"
        game = game.strip().split(":")
        possible = True
        
        #Iterate over rounds contained in game[1], split at ", "
        for round in game[1].split("; "):
            round = round.strip().split(", ")
            
            for colour in round:
                #In rounds, split the number of cubes and the colour
                colour = colour.split(" ")

                #Check if amount of coloured cubes is bigger
                #than the amount of cubes in the dictionary for the respective colour
                if colours[colour[1]] < int(colour[0]):
                    print(f"{game[0]} not possible")
                    possible = False
            
        if possible == False:
            continue

        #If the game is possible, append the ID of the game to the res array
        res.append(int(game[0].split(" ")[1]))
    
    print(sum(res))

    