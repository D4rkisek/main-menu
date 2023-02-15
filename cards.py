class Cards:
    def __init__(self):
        self.cards = {}
        for i in range(2, 13):
            if i != 7:
                self.cards[i] = []

    def add_card(self, number, resource):
        self.cards[number].append(resource)

    def remove_card(self, number, resource):
        self.cards[number].remove(resource)

    def get_cards_for_number(self, number):
        return self.cards[number]

    def distribute_resources(self, number, players):
        for player in players:
            count = 0
            for resource in self.cards[number]:
                if player.has_resource(resource):
                    count += 1
            player.add_resources(self.cards[number][0], count)
