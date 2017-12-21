''' 


Arbitrage Bot
by : Oğuz VURUŞKANER
by : Doğukaan  SATIR


 '''





TIMEZONE = "Etc/GMT+3"
site =  "https://bittrex.com/api/v1.1/public/getmarkethistory?market=BTC-"





from threading import Thread
import pytz
import requests
from time import sleep
from user import User
import datetime as dt
from sys import argv,stdin
from math import ceil
from datetime import timedelta
"""
This file should include your secret and private key
"""
import secret
markets = []
you = User(secret.KEY,secret.SECRET)
#getticker 
#getmarketsummaries
response = None


while not response or response.json()["success"] == "False" or response.json()["message"] == "INVALID_MARKET":
	nese = input()
	response = requests.get(site+nese)

markets.append(nese)
class Bittrex:
	pass



def doggyistek(coin,json):
	if not json: 
		return None
	minPrize = float("inf")
	maxPrize = float("-inf")
	total = 0.0
	fill = 0
	partial = 0
	buy = 0
	sell = 0
	minimum = min((i for i in json),key=timeStamp)
	maximum = max((i for i in json),key=timeStamp)

	if not Comparer.datetime:
		print("Between "  ,timeStamp(minimum).strftime("%H:%M:%S"),end =" ")
		Comparer.datetime = timeStamp(minimum) 
		Comparer.delta = minimum["Price"]
		n = Comparer()
		for i in json:
			if  n(i):
				continue
			if i["Price"] < minPrize:
				minPrize = i["Price"]
			if i["Price"] > maxPrize:
				maxPrize = i["Price"]
			if i["FillType"] == "PARTIAL_FILL":
				partial += 1
			elif i["FillType"] == "FILL":
				fill += 1 
			if i["OrderType"] == "SELL":
				sell += 1
			elif i["OrderType"] == "BUY":
				buy += 1
				
			total += i["Price"]
	
		
	elif Comparer.datetime >= timeStamp(maximum):
		
		return None


	else:
		Comparer.datetime = findSuccessor(Comparer.datetime,[i for i in json])
		print("Between ",Comparer.datetime.strftime("%H:%M:%S"),end =" ")
		n = Comparer()
		for i in json:
			if  n(i):
				continue
			if i["Price"] < minPrize:
				minPrize = i["Price"]
			if i["Price"] > maxPrize:
				maxPrize = i["Price"]
			if i["FillType"] == "PARTIAL_FILL":
				partial += 1
			elif i["FillType"] == "FILL":
				fill += 1 
			if i["OrderType"] == "SELL":
				sell += 1
			elif i["OrderType"] == "BUY":
				buy += 1
				
			total += i["Price"]




	Comparer.datetime = timeStamp(maximum)
	print("and",Comparer.datetime.strftime("%H:%M:%S"))
	k = Comparer.delta
	Comparer.delta = maximum["Price"]
	return (coin,buy,sell,round(minPrize,8),round(Comparer.delta- k,	8),round(total,8))

	
	

	



class Comparer:
	datetime = None
	delta = 0
	def __init__(self):
		pass
		
	def __call__(self,x):
		stampTime = timeStamp(x)
		if  Comparer.datetime <  stampTime:
			
			return False
		else:
			
			
			return True


def findSuccessor(current,stampList):
	successor = current
	for rasa in stampList:
		rasa = timeStamp(rasa)
		if rasa > current and current < successor:
			successor = rasa

	return successor 

def timeStamp(stamp):
	stamp = stamp["TimeStamp"]
	stamp = stamp.split("T")
	date = [int(i) for i in stamp[0].split("-") ]
	timeSecond = [int(ceil(float(i))) for i in stamp[1].split(":") ]
	finalList = date+timeSecond
	return dt.datetime(finalList[0],finalList[1],finalList[2],finalList[3],finalList[4],finalList[5]%60)




def pretty(coin,nese):
	x = doggyistek(coin,nese)
	if not x:
		return
	
	coin,buy,sell,minPrize,change,total = x
	if minPrize == float("inf"):
		return
	print(coin.upper() , "\t","Buy :",buy ,"\t","Sell :",sell,"\t","Start Price :",minPrize,"\t","Change : ",change,"\t","Sum (total BTC)",total )





if __name__ == "__main__":
	while True:
		for market in markets:
			response = requests.get(site+market)
			json = response.json()["result"]
			
			pretty(market,json)
			
			
		
		sleep(3)