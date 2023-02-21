#Number cards count as their face value (2 through 10). Jack, Queen and King count as 10. An Ace can be counted as either 1 or 11.

#Return the highest score of the cards that is less than or equal to 21. If there is no score less than or euqal to 21 return the smallest score more than 21.

def score_hand(cards):
    # your code here
    soma = 0
    for c in cards:
        if c.isdigit(): soma+=int(c)
        elif 
        else: soma+= oth[c.lower()]  
    return soma