#!/usr/bin/env python

#this is a prototype code, it needs to be slim lined using new repeatable methods

import random

CardList = [];

#First we open a text file of cards with an ID Number and value related to a card
#e.g. 2 of Spades is Card ID = 1 and Value = 2

try:
    f = open("cards.txt")
except IOError:
    print "That file does not exist"

#Now we place the cards into a list, each card is a dictionary, is this the best way? Probably Not

for line in f:
    list1 = line.strip().split("/")
    cardid = int(list1[0])

    if cardid%13 == 0:
        cardvalue = 11
    else:
        cardvalue = int(list1[2])

    cardid = cardid - 1

    CardList.append({'Card ID':cardid, 'Name':list1[1], 'Value':cardvalue})

CardNumbers = range(0,52)

#The Cards are shuffled, somewhere less than 25? cards can be used in a two player game
#random.sample will choose 25 unique numbers from the list CardNumbers
p = random.sample(CardNumbers,25)
#p[4] = 12; p[5] = 25; p[6] = 38; p[7]=51

#This indicates if an ace has been given the value of 11
AceFlag1 = 0
AceFlag2 = 0

#Four Cards are drawn, the first two to you and two to the dealer, we don't know what's in the dealers hand
#This is a bit ham fisted but a slicker approach would take more time and it's late

CardDict1 = CardList[p[0]]
Card1 = CardDict1['Name']
CardValue1 = CardDict1['Value']

CardDict2 = CardList[p[1]]
Card2 = CardDict2['Name']
CardValue2 = CardDict2['Value']

#If you happen to draw two Aces, the second ace is set to the value of 1
if CardValue1 == 11: 
    AceFlag1 = AceFlag1 + 1

if CardValue2 == 11:
    AceFlag1 = AceFlag1 + 1

if AceFlag1 == 2:
    AceFlag1 = 1
    CardValue2 = 1

YourTotal = CardValue1 + CardValue2

print "You have the cards the",Card1,"and the",Card2
print "Your total is",YourTotal  

CardDict3 = CardList[p[2]]
Card3 = CardDict3['Name']
CardValue3 = CardDict3['Value']

CardDict4 = CardList[p[3]]
Card4 = CardDict4['Name']
CardValue4 = CardDict4['Value'] 

#If you happen to draw two Aces, the second ace is set to the value of 1
if CardValue3 == 11:
    AceFlag2 = AceFlag2 + 1

if CardValue4 == 11:
    AceFlag2 = AceFlag2 + 1

if AceFlag2 == 2:
    AceFlag2 = 1
    CardValue4 = 1

TheirTotal = CardValue3 + CardValue4

#Card count is set at four, Cards 0,1,2 and 3 have been drawn
cardCount = 4
flagout = 1

# for some reason While True wasn't working with break, i need to understand better what happens with "break"
# I used a flag instead
while (flagout == 1):
    cardAnswer = raw_input("Do you want another card?(y/n)")
    if ((cardAnswer.lower() != "y") or cardCount > 14) or YourTotal > 22:
        flagout = 0
    else:
        CardDictX = CardList[p[cardCount]]
        cardCount = cardCount + 1
        CardX = CardDictX['Name']
        CardValueX = CardDictX['Value']
        if CardValueX == 11 and (11 + YourTotal)> 21:
                CardValueX = 1
        YourTotal = YourTotal + CardValueX
        if YourTotal > 21:
           if AceFlag1 == 1:
              YourTotal = YourTotal - 10
              AceFlag1 = 0
           else:
              flagout = 0 
        
        print "Your card is the",CardX,"and your total is",YourTotal
# The section above is to do with what happens after you see your two cards
# You can choose to pick another card, and another if you want until you're happy to stick or you go bust (>21)
# If an Ace valued at 11 pushes you over 21, then it's value is automatically set to 1


# The Next section is what happens once you've finished
# It's the dealer's turn to respond. S/he wins if they get the same or larger total without going bust

# S/he keeps drawing cards until the desired total is reached or surpassed, or if s/he goes bust
# Again an Ace is set to a value of 1 if it having a value of 11 would force them to go bust
if YourTotal > 21:
    print "You're Bust!, the dealer wins!"
else:
    if TheirTotal >= YourTotal and (TheirTotal < 22):
        print "The Dealer has the",Card3,"and",Card4
        print "Their total is",TheirTotal 
        print "The Dealer wins!!"
    else:
        print "The Dealer has the cards",Card3,"and the",Card4
        print "Their total is",TheirTotal
        if (YourTotal > TheirTotal) and (YourTotal < 22):
            while TheirTotal < YourTotal:
                CardDictX = CardList[p[cardCount]]
                cardCount = cardCount + 1
                CardX = CardDictX['Name']
                CardValueX = CardDictX['Value']
                if (CardValueX == 11) and ((11 + YourTotal)> 21):
                    CardValueX = 1
                if TheirTotal + CardValueX > 21 and AceFlag2 == 1:
                    TheirTotal = TheirTotal - 10
                    AceFlag2 = 0
                TheirTotal = TheirTotal + CardValueX
                print "The Dealer has drawn the",CardX
                print "The Dealer's total is",TheirTotal
        
#An Ace "flag" is needed, it is possible that if some other card makes the player go bust and they previously drew an
#ace then the ace can be reverted to a one (or reducing the total by 10)

if TheirTotal < 22:
    print "The Dealer Wins!!"
else:
    print "You win, the dealer went bust!"
