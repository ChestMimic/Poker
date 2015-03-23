class Card:
	def __init__(self, c):
		self.c = c
		if ('A' in c):
			self.val = 14
		elif ('K' in c):
			self.val = 13
		elif('Q' in c):
			self.val = 12
		elif('J' in c):
			self.val = 11
		elif('T' in c):
			self.val = 10
		else:
			self.val = int(self.c[0])
		self.suit = self.c[1]
	def __str__(self):
		return self.c
	def __lt__(self, other):
		return self.val < other.val
	def __eq__(self, other):
		return ((self.val, self.suit) == (other.val, other.h)) 

class Hand:
	high = -1 #default to impossible card
	type = 10 #default to type 10, associated with High card
	cards = []
	def __init__(self, handString):
		isFlush = 0
		isStraight = 0
		self.s = handString
		self.strArr = self.s.split()
		#ensure there are 5 cards, make hand useless otherwise
		if(len(self.strArr) != 5) :
			self.high = -1 #invalid hands always lose
			return
		else:
			
			suites = []
			for x in self.strArr:
				y = Card(x)
				self.cards.append(y)
				
			#confirm cards in ascending order
			self.cards.sort()
			#check for flush
			#get number of suites
			for x in self.cards:
				if(suites.count(x.suit) == 0):
					suites.append(x.suit)
			#if number of suites only 1, has to be one of the flush hands
			if(len(suites) == 1):
				isFlush = 1
				
			#check for straight (consecutive cards)
			#if range between first and last is 5, straight
			print(self.cards[4].val)
			rng = range(self.cards[0].val, self.cards[4].val)
			if(len(rng) == 5):
				isStraight = 1;
			if(isFlush ==1):
				if( isStraight == 1):
					if(self.cards[4].val == 14):
						self.type = 1 #Royal Flush
					else:
						self.type = 2 #Straight Flush
				else:
					self.type = 5 #Standard Flush
			
			if(isStraight == 1):
				self.type = 6 #Standard Straight
				
			##TODO##

if __name__ == '__main__' :
	x = Hand("4D 6S 9H QH QC")
	print(x.cards[0])
	print("TEST")