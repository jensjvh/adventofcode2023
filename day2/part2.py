with open("input.txt", "r") as inputs:
    res = []
    for game in inputs:
        #Initialise the powers of the cubes to 1
        powers = 1
        #The colours dictionary is used to keep track of the max value of the coloured cubes
        colours = {"red": 0, "green": 0, "blue": 0}
        game = game.strip().split(":")
        
        #Iterate over each round in a line, split by "; "
        for round in game[1].split("; "):
            round = round.strip().split(", ")
            
            #Iterate over each colour in each round
            for colour in round:
                colour = colour.split(" ")
                #Check if the number of cubes is greater than the value stored in the dictionary
                #If yes, set the dictionary value to be equal to the colour
                if colours[colour[1]] < int(colour[0]):
                    colours[colour[1]] = int(colour[0])

        #Iterate over the dictionary key-value pairs and
        #multiply the powers variable with each value.
        for _, value in colours.items():
            powers *= value

        res.append(powers)
    
    print(sum(res))

    