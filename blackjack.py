import random
import os
#Deck definition
suits=('Kier','Karo','Trefl','Pik')
ranks=('Dwa','Trzy','Cztery','Piec','Szesc','Siedem','Osiem','Dziewiec','Dziesiec','Walet','Dama','Krol','As')
values={'Dwa':2,'Trzy':3,'Cztery':4,'Piec':5,'Szesc':6,'Siedem':7,'Osiem':8,'Dziewiec':9,'Dziesiec':10,'Walet':10,'Dama':10,'Krol':10,'As':1}
value_apperance={'Dwa':2,'Trzy':3,'Cztery':4,'Piec':5,'Szesc':6,'Siedem':7,'Osiem':8,'Dziewiec':9,'Dziesiec':10,'Walet':'W','Dama':'D','Krol':'K','As':'A'}
suit_apperance={'Kier':'♥','Karo':'♦','Trefl':'♣','Pik':'♠'}

class Card():
    def __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank
        self.value=values[rank]
        self.apperance=value_apperance[rank]
        self.suit_apperance=suit_apperance[suit]
    def __str__(self):
        return f'{self.rank} {self.suit}'
class Deck():
    def __init__(self):
        self.all_cards=[]
        for a in suits:
            for b in ranks:
                self.all_cards.append(Card(a,b))
    def shuffling(self):
        random.shuffle(self.all_cards)
    def popping_card(self):
        return self.all_cards.pop()
class Player():
    def __init__(self,money):
        self.money=money
    def __str__(self):
        return(f'{self.money}')
    def adding_money(self,won_money):
        self.money+=2*won_money
    def betting_money(self,bet):
        self.money-=bet

#Printing cards procedure
def display(dealer_cards,player_cards):
    for i in dealer_cards:
        rank_dealer=[]
        suit_dealer=[]
        rank_dealer.append(i.apperance)
        suit_dealer.append(i.suit_apperance)
    a=''
    b=''
    c=''
    d=''
    e=''
    f=''
    g=''
    #Dealer cards print
    print('DEALER CARDS:\n')
    a=a+'    --------------------'
    b=b+f'   |{rank_dealer[0]}                  |'
    c=c+'   |                   |'
    d=d+f'   |         {suit_dealer[0]}         |'
    e=e+'   |                   |'
    f=f+f'   |                  {rank_dealer[0]}|'
    g=g+'    --------------------'
    print(a,'\n',b,'\n',c,'\n',d,'\n',e,'\n',f,'\n',g,'\n')
    
    print('PLAYER CARDS')
    #Player cards print
    a=''
    b=''
    c=''
    d=''
    e=''
    f=''
    g=''

    for i in player_cards:
        a=a+'    --------------------'
        b=b+f'   |{i.apperance}                  |'
        c=c+'   |                   |'
        d=d+f'   |         {i.suit_apperance}         |'
        e=e+'   |                   |'
        f=f+f'   |                  {i.apperance}|'
        g=g+'    --------------------'
    print(a,'\n',b,'\n',c,'\n',d,'\n',e,'\n',f,'\n',g,'\n')
    print(f'PLAYER SCORE: {calculating(player_cards)}')
    print(f'PLAYER ACCOUNT: {player1.money}')
#Card adding
def card_add(cards):
    cards.append(my_deck.popping_card())
#Value calculating (to decide A value)
def calculating(cards):
    value=0
    count=0
    for i in cards:
        if i.value==1:
            count+=1
        else:
            value+=i.value
        for i in range(0,count,1):
            if abs(value+1-21)<abs(value+10-21):
                value+=1
            else:
                value+=11
    return value

#--------------GAME LOGIC--------------
basic_value=input('How much do you want to spend: ?')
while True:
    if basic_value.isdigit():
        player1=Player(int(basic_value))
        break
    else:
        basic_value=input('Type ur number again: ')
        pass
game_on=True
while game_on==True:
    #Round preparation
    os.system('cls')
    player_value=0
    more=False
    bet=''
    while True:
        bet=input('How much do you wanna to bet?: ')
        if bet.isdigit(): 
            if int(bet)>player1.money:
                print('Not enough founds on account')
            else:
                player1.betting_money(int(bet))
                more=True
                break
        else:
            pass
    my_deck=Deck()
    my_deck.shuffling()
    dealer_cards=[]
    player_cards=[]
    for i in range(0,2,1):
        card_add(dealer_cards)
        card_add(player_cards)
    display(dealer_cards,player_cards)    
    player_hit_on=True
    
    #Hitting procedure
    while player_hit_on==True:
        player_value=calculating(player_cards)
        if player_value<21:
            while True:
                ask=input('Do you wanna hit? Y or N: ')
                if ask=='Y':
                    card_add(player_cards)
                    break
                elif ask=='N':
                    player_hit_on=False
                    break
                else:
                    print('Type again')
        else:
            player_hit_on=False
        os.system('cls')
        display(dealer_cards,player_cards)
    
    #Dealer turn
    player_value=calculating(player_cards)
    dealer_value=calculating(dealer_cards)
    
    while True:
        if dealer_value<17:
            card_add(dealer_cards)
            dealer_value=calculating(dealer_cards)
        else:
            break
    if abs(player_value-21)<=abs(dealer_value-21):
        print('PLAYER WON')
        print(f'Dealer Value: {dealer_value}')
        print(f'Player Value: {player_value}')
        player1.adding_money(int(bet))   
    else:
        print('Dealer WON')
        print(f'Dealer Value: {dealer_value}')
        print(f'Player Value: {player_value}')
    while True:
            play_again=input('Do you wanna play another round?:Y or N ')
            if play_again=='Y':
                break
            elif play_again=='N':
                game_on=False
            else:
                play_again=input('Type again?:Y or N ')
