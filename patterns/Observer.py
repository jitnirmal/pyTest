from abc import ABCMeta, abstractmethod

class Observer(metaclass = ABCMeta):
	@abstractmethod
	def onEvent(self,observer):
		pass

class Observable:
	def __init__(self):
		self._observers = []

	def addObserver(self, observer):
		self._observers.append(observer);	
	
	def notifyAllObservers(self,event):
		for observer in self._observers:
			observer.onEvent(event);


class MarketData():
	def __init__(self,bid,ask):
		self._bid = bid
		self._ask = ask

class MarketBook(Observable):
	def update(self, marketData):
		super(MarketBook, self).notifyAllObservers(marketData)


class Strategy(Observer):
	def onEvent(self,marketData):
		print("Strategy got the update bid = %d, ask= %d " %(marketData._bid, marketData._ask))


class TradeBook(Observer):
	def onEvent(self,marketData):
		print("TradeBook got the update bid = %d, ask= %d " %(marketData._bid, marketData._ask))

class Client:
	def __init__(self):
		self._strategy = Strategy()
		self._tradeBook = TradeBook()
		self._marketBook = MarketBook()
		self.register()

	def register(self):
		self._marketBook.addObserver(self._strategy)
		self._marketBook.addObserver(self._tradeBook)

	def process(self):
		data = MarketData(200,205)
		self._marketBook.update(data)

client = Client()
client.process()