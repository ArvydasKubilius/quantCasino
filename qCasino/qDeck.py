import qHelpers
	
SUITS = ["Diamonds", "Clubs", "Hearts", "Spades"]
VALUES = ["2", "3", "4", "5", "6", "7", "8", "9","10",
         "Jack", "Queen", "King", "Ace"]
		 
POWER = 6
DrawnCards = set()


	
def shuffle():
    global DrawnCards 
    DrawnCards = set()
	
def draw():
    global DrawnCards
    n = qHelpers.random_int(POWER)
    while n > 51 or n in DrawnCards:
        n = qHelpers.random_int(POWER)
    DrawnCards.add(n)
    card = f"{VALUES[(n+1)%13]} of {SUITS[(n+1)//13]}"
    return card