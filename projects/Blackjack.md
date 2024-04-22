# Blackjack
* computer deals 2 cards to each player (dealer / player)
  * one of the dealer's cards is face down, i.e., can't be seen by player
* the rank of the cards is all that matter, suits are ignored
* J, Q, K count as 10
* A counts as 1 or 11
* the value of a hand is the total of all the cards, e.g., 4 and K total 14, A and 5 total 16 (or 6)
* if the player has an A and a K/Q/J/10, it's called a "natural" or "Blackjack" and the player wins as long as dealer doesn't have one too
* player can "hit" (ask for another card) or "stand"
   * at this point the dealer's second card is revealed
* dealer must hit on a hand below 17 and stand on 17+
* player with higher hand wins
* 21 is a "blackjack" 
* hands over 21 are a "bust" and the other player wins

## Implementation ideas
* use a Class to represent the deck of cards
* can use a Class to represent each card, or just use a __`namedtuple`__ with two fields
* build your solution incremenetally
* once it's working, consider adding ability for player to split pairs
   * that is, if player has two cards of the same denomination (e.g., two 8s, two As, etc.) they can choose to split the into two separate hands
