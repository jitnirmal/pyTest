from dateutil import parser
import csv
import timeit
from memory_profiler import profile



class Data:
	def __init__(self,rowData):
		self.Symbol=rowData[0]
		self.Series=rowData[1]
		self.Open=float(rowData[2])
		self.High=float(rowData[3])
		self.Low=float(rowData[4])
		self.Close=float(rowData[5])
		self.Last=float(rowData[6])
		self.Prevclose=float(rowData[7])
		self.Tottrdqty=int(rowData[8])
		self.Tottrdval=float(rowData[9])
		self.Timestamp=parser.parse(rowData[10])
		self.Totaltrades=int(rowData[11])
		self.Isin=rowData[12]

	def __str__(self):
		return ', '.join(['{key}={value}'.format(key=key, value=self.__dict__.get(key)) for key in self.__dict__])

class DataHandler:
	def __init__(self):
		self.FileName = "data//bhavCopy.csv"
		self.Records = []
		self.readRecordsFromFile()

	@profile
	def readRecordsFromFile(self):
		with open(self.FileName, 'r') as csvfile:
			headerRead = False
			csv_reader = csv.reader(csvfile, delimiter=',')
			for row in csv_reader:
				if  headerRead == False:
					headerRead = True
					continue
				self.parseData(row)

	def parseData(self,rowData):
		data = Data(rowData)
		self.Records.append(data)


datahandler = DataHandler()
