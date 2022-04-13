def quack(p1, p2):
    p1 = p1.lower()
    p2 = p2.lower()
    shitList = ["rock", "paper", "scissor", "lizard", "spock"]
    if(p1 in shitList and p2 in shitList):
        if(p1 == p2):
            return "Draw!"
        
        elif(p1 == "rock"):
            if (p2 == "scissors" or p2 == "lizard"):
                return "Player 1 won!"
            elif(p2 == "paper" or p2 == "spock"):
                return "Player 2 won!"
            
        elif(p1 == "paper"):
            if (p2 == "rock" or p2 == "spock"):
                return "Player 1 won!"
            elif(p2 == "scissors" or p2 == "lizard"):
                return "Player 2 won!"
            
        elif(p1 == "scissors"):
            if (p2 == "paper" or p2 == "lizard"):
                return "Player 1 won!"
            elif(p2 == "rock" or p2 == "spock"):
                return "Player 2 won!"
            
        elif(p1 == "lizard"):
            if (p2 == "paper" or p2 == "spock"):
                return "Player 1 won!"
            elif(p2 == "rock" or p2 == "scissors"):
                return "Player 2 won!"
            
        elif(p1 == "spock"):
            if (p2 == "scissors" or p2 == "rock"):
                return "Player 1 won!"
            elif(p2 == "paper" or p2 == "lizard"):
                return "Player 2 won!"
    else:
        return"Oh, Unknown Thing"


print(quack("Spock", "Quack"))