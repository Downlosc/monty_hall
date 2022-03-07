import deck as _d
import player as _p
from pprint import pprint


def launch_game():
  deck = _d.Cards()
  player = _p.Player()
  deck.prepareCards()
  pselection = player.getSelectedCard()
  deck.setSelection(pselection)
  data = deck.getData()
  deck.revealLosingCard()
  data = deck.getData()
  swap = player.swapCard()
  # if swap: deck.swapSelection()
  deck.swapSelection()
  data = deck.getData()
  wl = deck.isThereAWin()
  return wl


def count_wins(): 

  wins = 0
  loss = 0

  for i in range (0, 100000): 
    wl = launch_game()
    if wl.startswith('win'): wins = wins + 1
    else: loss = loss + 1

  print('wins', wins)
  print('loss', loss)
  
