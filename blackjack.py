
import random
class Card(object):
    rank_names = [None, "Ace", "2", "3", "4", "5", "6", "7", 
              "8", "9", "10", "Jack", "Queen", "King"]
    d = {None:0, 'Ace':1, '2': 2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'Jack':10, 'Queen':10, 'King':10}
    def __init__(self, rank=2):    
        self.rank = self.rank_names[rank] 
    def __str__(self):
        return self.rank
    def __int__(self):
        return self.d[self.rank]

class Deck(object):

    def __init__(self):
    	self.cards = []
        for suit in range(4):
            for rank in range(1,14):
                card = Card(rank)
                self.cards.append(card)
        random.shuffle(self.cards)

    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)

    def add_card(self, card):
        """Adds a card to the deck."""
        self.cards.append(card)

    def remove_card(self, card):
        """Removes a card from the deck."""
        self.cards.remove(card)

    def pop_card(self, i=-1):
        """Removes and returns a card from the deck.

        i: index of the card to pop; by default, pops the last card.
        """
        return self.cards.pop(i)

    def shuffle(self):
        """Shuffles the cards in this deck."""
        random.shuffle(self.cards)

    def sort(self):
        """Sorts the cards in ascending order."""
        self.cards.sort()

    def move_cards(self, hand, num):
        """Moves the given number of cards from the deck into the Hand.

        hand: destination Hand object
        num: integer number of cards to move
        """
        for i in range(num):
            hand.add_card(self.pop_card())


    def update_bank(self):
        if player_sum <=  21 and player_sum > dealer_sum:
            self.player.bankroll += self.player.bet
        elif player_sum > 21 or player_sum < dealer_sum:
            self.player.bankroll -= self.player.bet 



def hit_or_stay(player):
    if str(raw_input('hit or stay?')).lower() == 'hit':
        hit(masterDeck, player.hand, 1)
    else:
        print playerhand.sumCard()

def dealer_deal(deck, hand, num):
    for i in range(num):
        hand.add_card(deck.pop_card())
    print 'The dealers card value is %s' %(hand.sumCard())
    for card in hand.cards:
        return card
    

def deal(deck, hand, num):
    for i in range(num):
        hand.add_card(deck.pop_card())
    for card in hand.cards:
        print card
    print 'Your card value is %s' %(hand.sumCard())

def dealer_hit(deck, hand, num=1):
    for i in range(num):
        hand.add_card(deck.pop_card())
    print 'The dealers card value is %s' %(hand.sumCard())
    for card in hand.cards:
        return card
    
    

def hit(deck, hand, num=1):
    for i in range(num):
        hand.add_card(deck.pop_card())
    for card in hand.cards:
        print card
    print 'Your card value is %s' %(hand.sumCard())
    

def split(player):
    if str(raw_input('Split?')).lower() == 'yes':
        for card in player.hand:
            if card[0] == card[1]:
                otherHand = Hand()
                player.hands.append(otherHand)
                otherHand.cards.append(card[1])
                return player.hands
    else: 
        return 

def double_down(player):
        player.bet = player.bet*2
        print 'your new bet is %s' %(player.bet)



'''HAND CLASS'''
class Hand(Deck): 
	"""represents a hand of playing cards"""
	def __init__(self):
		self.cards = []
	def sumCard(self):
		val = 0
		for card in self.cards:
			val += int(card)
		return val



class Player(object):
    def __init__(self, hand, bankroll = 20, bet = 5):
        self.hand = hand
        self.bankroll = bankroll
        self.bet = bet


class Dealer(Player):
	def __init__(self, hand):
	   self.hand = hand
       #self.deck.cards.append(hand)




# def dealer_hos(self):
#         dealer_sum = self.dealer.hand.sumCard()
#         if compare <= 16:
#             hit(self.deck, self.dealer, 1)
#             dealer_sum = self.dealer.hand.sumCard()
#             print dealer_hit
#             for card in self.dealer.hand:
#                 return card
#         elif compare > 16:
#             print dealer_sum
#             for card in self.dealer.hand:
#                 return card


class Game(object):
    # deck = Deck()
    # dealer = Dealer()
    # players = [player1]
    def __init__(self, deck, player, dealer):
        self.deck = deck
        self.player = player
        self.dealer = dealer

    def play(self):
        
    
        print 'start game'
        print 'Bet = %s' %(self.player.bet)
        deal(masterDeck, self.player.hand, 2)
        dealer_deal(masterDeck, self.dealer.hand, 2)
        while self.player.hand.sumCard() < 21:
            choice = str(raw_input('hit, stay, double down? ')).lower()
            if choice == 'hit':
                hit(masterDeck, self.player.hand, 1)
            if choice == 'stay':
                print 'your card value is %s' %(self.player.hand.sumCard())
            if choice == 'double down':
                double_down(self.player)
            if self.dealer.hand.sumCard() < 17: 
                dealer_hit(masterDeck, self.dealer.hand, 1)
            gameEnd(self.player, self.dealer)
        
        #if self.dealer.hand.sumCard() == 21:
        #    Game.compare(self.player, self.dealer)
        


        

def gameEnd(player, dealer):
    if player.hand.sumCard == 21 and dealer.hand.sumCard != 21:
        player.bankroll += 2 * player.bet
        print 'congrats, you won! your bankroll is $%s and you won $%s' %(player.bankroll, 2*player.bet)
    if player.hand.sumCard == dealer.hand.sumCard: 
        print 'PUSH! '
          

    def compare(self, player, dealer):
        if self.player.hand.val <=21 and player.hand.sumCard > self.dealer.hand.sumCard:
            self.player.bankroll += self.player.bet
            return 'congrats, you won! your bankroll is $%s and you won $%s' %(self.player.bankroll, 2*self.player.bet)
        elif self.player.hand.sumCard < self.dealer.hand.sumCard:
            self.player.bankroll -= self.player.bet 
            return 'sorry, you lost $%s your bankroll is $%s'%(self.player.bet, self.player.bankroll)
        elif self.player.hand.sumCard <= 21 and self.dealer.hand.sumCard > 21:
            self.player.bankroll += self.player.bet
            return 'congrats, you won! your bankroll is $%s and you won $%s' %(self.player.bankroll, 2*self.player.bet)
        else: 
            return 'PUSH: you still have %s in your bankroll' %(self.player.bankroll)           

#print hit(deck, self.hand, 1)


masterDeck = Deck()
player1 = Player(hand = Hand(), bankroll = 20, bet = 5)
dealer1= Dealer(hand = Hand())
newgame = Game(deck = masterDeck, player = player1, dealer = dealer1)
print newgame.play()












