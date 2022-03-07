import random
import card as _c

LOSING = 0
WINNING = 1
DISABLED = 2

PERMUTATIONS = {
    0 : [1 , 0, 0],
    1 : [0 , 1, 0],
    2 : [0 , 0, 1],
    }

class Cards(): 
  cds = {}

  def selectPermutation(self): 
    sel = random.randint(0, 2)
    permutation = PERMUTATIONS[sel]
    return permutation

  def prepareCards(self): 
    permutation = self.selectPermutation()
    for i in range(0,len(permutation)): 
      status = permutation[i]
      self.cds[i] = _c.Card(status)

  def getCards(self): 
    if self.cds: return self.cds
    self.prepareCards()
    return self.cds

  def revealLosingCard(self):
    for c in self.cds: 
      card = self.cds[c]
      card_satus = card.getStatus()
      card_sel   = card.getSelected()
      if card_satus == WINNING  or card_sel : continue
      card.setStatus(DISABLED)
      return

  def setSelection(self, pselection): 
    self.cds[pselection].setSelected(True)

  def swapSelection(self): 
    for c in self.cds: 
      card = self.cds[c]
      isSelected = card.getSelected()
      status     = card.getStatus()
      if isSelected or status == DISABLED: card.setSelected(False)
      else: card.setSelected(True)

  def getData(self):
    d = {}
    for  key, val in self.cds.items(): 
      p = {}
      card_status = val.getStatus()
      card_selected = val.getSelected()
      p['card_status'] = card_status
      p['card_selected'] = card_selected
      d[key] = p
    return d


  def isThereAWin(self): 
    w = False; 
    for c in self.cds: 
      card = self.cds[c]
      w = card.isAwin()
      if not w: continue
      return 'win!!'

    return 'lost!'

    
