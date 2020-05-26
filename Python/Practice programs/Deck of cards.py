import random
suits=('Heart','Clubs','Diamond','Spades')
ranks=['Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','King','Queen','Ace','Jack']
values={'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'Ten':10,'King':10,'Queen':10,'Ace':11,'Jack':10}


playing=True

class Card:
    def __init__(self,suits,ranks):
        self.suits=suits
        self.ranks=ranks

    def __str__(self):
        return self.ranks + ' of ' + self.suits


class Deck:
    def __init__(self):
        self.deck=[]
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suits,ranks))


    def __str__(self):
        deck_comp=''
        for card in self.deck:
            deck_comp+='\n' + card.__str__()
        return 'The deck has:'+ deck_comp    

    def shuffle(self):
        return random.shuffle(self.deck)  

    def deal(self):
        single_card=self.deck.pop()
        return single_card


class Hand:
    def __init__(self):
        self.cards=[]
        self.values=0
        self.aces=0

    def add_card(self,card):
        self.cards.append(card)  
        self.value+=value[card.rank] 
        if card.rank=='Aces':
            self.aces+=1

                
    def adjust_for_ace(self):
        while self.value>21 and self.aces>0:
            self.value-=10
            self.aces-=1

class Chips:
    def __init__(self,total=100):
        self.total=total
        self.bet=0


    def win_bet(self):
        self.total+=self.bet

    def lose_bet(self):
        self.total-=self.bet



    def take_bet(Chips):

        while True:
            try:
                chips.bet=int(input('How many chips would you like to bet:'))
            except:
                print('Sorry provide integer')
            else:
                if chips.bet>chips.total:
                    print('Sorry you do not have enough chips'.format(chips.total))
                else:
                    break

    def hit(deck,hand):
        single_card=card.deal()
        hand.add_card(single_card)
        hand.adjust_for_ace() 


    def hit_or_stand(deck,hand):
        global playing

        while True:
            x=input('Hit or Stand?Enter h or s:')
            if x[0].lower()='h':
                hit(deck,hand)
            elif x[0].lower()=='s':
                print('Players stand dealers turn')
                playing=False
            else:
                print('Sorry I did not understand that,Please enter h or s only!')    
            








