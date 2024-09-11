import numpy as np

class Shoe:
    amount_of_decks = 1
    cards_per_deck = 52
    running_count = float(0)
    true_count = float(0)

    def __init__(self,amount_of_decks):
        self.cards = {
            '11': 4 * self.amount_of_decks,
            '10': 16 * self.amount_of_decks,
            '9': 4 * self.amount_of_decks,
            '8': 4 * self.amount_of_decks,
            '7': 4 * self.amount_of_decks,
            '6': 4 * self.amount_of_decks,
            '5': 4 * self.amount_of_decks,
            '4': 4 * self.amount_of_decks,
            '3': 4 * self.amount_of_decks,
            '2': 4 * self.amount_of_decks
        }
        self.total_cards = self.amount_of_decks * self.cards_per_deck
        self.amount_of_decks = amount_of_decks

    def _update_cards(self, card):
        self.cards[card] -= 1
        self.total_cards -= 1

    def get_remaining_cards(self):
        return self.total_cards

    def _get_remaining_decks(self):
        return self.total_cards / self.cards_per_deck

  # using wong halves counting system
    def _calculate_count(self, card):
            match float(card):
                case 11:
                    return -1
                case 10:
                    return -1
                case 9:
                    return -0.5
                case 8:
                    return 0
                case 7:
                    return 0.5
                case 6:
                    return 1
                case 5:
                    return 1.5
                case 4:
                    return 1
                case 3:
                    return 1
                case 2:
                    return 0.5

    def update_count(self, card):
        self._update_cards(card)
        self.running_count = self.running_count + self._calculate_count(card)
        self.true_count = self.running_count / self._get_remaining_decks()
        if self.true_count < 0:
            print(f"{Style.RED}{self.true_count}{Style.RESET}")
        else:
            print(f"{Style.GREEN}{self.true_count}{Style.RESET}")

    def _calculate_hand(self,cards):
        best_hand_value = 0
        total = 0
        ace_count = 0

        for card in cards:
            if total >= best_hand_value:
                best_hand_value = total
            if card == 11:
                if total + 11 <= 21:
                    ace_count += 1
                    total += card
                elif total + 1 <= 21:
                    total += 1
            else:
                if total + card > 21 and ace_count > 0:
                    total -= 10
                    ace_count -= 1
                    total += card
                else:
                    if total + card > 21:
                        return total
                    total += card
        return best_hand_value if best_hand_value > total else total

    # player_hand = [[11,5,6], [8,5,3]] // single- or multidimensional np.array for player hand/splits
    # dealer_hand = [4,11,6] // one np.array for dealer hand
    def calculate_winning_hand(self, player_hand):
        player_hand = np.squeeze(player_hand) # Removes empty dimensions
        if player_hand.ndim == 1:
            print(self._calculate_hand(player_hand))
            pass

# colors for true count
class Style:
  RED = "\033[31m"
  GREEN = "\033[32m"
  BLUE = "\033[34m"
  RESET = "\033[0m"
