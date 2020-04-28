
class Validation():

    def __init__(self,card_number):
        self.card_number = card_number


    '''def define_card_type(self):
        card = self.card_number

        card_numbers = list(str(card))
        card_numbers = list(map(int, card_numbers))
        x = card_numbers


        if x[0] == 5:
            print('Mastercard')

        if x[1:5] == [32180]:
            print('OTP-s Mastercard')'''


    def luhn_algorithm(self):
        card = self.card_number

        card_numbers = list(str(card))
        card_numbers = list(map(int,card_numbers))
        x = card_numbers[6::-1]

        #Algorithm logics applied here

        cards = []

        switch = None

        for i in x:

            if switch == None or switch == True:

                if i * 2 > 9:
                    num = i * 2 - 9
                    cards.insert(i, num)
                    switch = False

                else:
                    cards.insert(i, i)
                    switch = False

            else:
                cards.insert(i,i)
                switch = True


        print(cards)
        print(sum(cards))

        if sum(cards) % 10 == 0:
            print('card is valid')

        else:
            print('card is invalid')




mycard = Validation()
mycard.define_card_type()
mycard.luhn_algorithm()
