import random

class Player(): 
  selected = None

  def getSelectedCard(self): 
    if not self.selected: return self.selectCard()
    return self.selected

  def selectCard(self): 
    self.selected = random.randint(0,2)
    return self.selected

  def swapCard(self):
    swap = random.randint(0,1)
    loptions = [True, False]
    return loptions[swap]
