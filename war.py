class Card(object):
    suits = ('clubs', 'diamonds', 'hearts', 'spades')
    values = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')
    def __init__(self, rank):
        self.rank = rank
    def get_suit(self):
        return Card.suits[self.rank // 13]
    def get_value(self):
        return Card.values[self.rank % 13]
    def __str__(self):
        return '{suit} {value}'.format(suit=self.get_suit(),value=self.get_value())

def higher_in_rank(base_card):
    for rank in range(base_card.rank, 52):
        yield Card(rank)

base_card = Card(0 * 13 + 5)
for card in higher_in_rank(base_card):
    print (card)
