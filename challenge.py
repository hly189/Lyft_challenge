import math 

class Solution(): 
	def __init__(self): 
		self.radius = 3959 #in miles according to www.google.com	

#Take coordinate of a point 
	def coordinate(self,longtitude,latitude): 
		self.longtitude = longtitude 
		self.latitude = latitude

#Change the coordinate to radians
	def to_radian(self,num): 
		return num* (math.pi/180)

#Calculate \phi_2 - \phi_1 and \lambda_2 - \lambda_1 in Haversine function
	def distance(self,x,y): 
		self.diff_lat = self.to_radian(y.latitude - x.latitude)
		self.diff_long = self.to_radian(y.longtitude - x.longtitude)

#Calculate the distance using Haversine function
	def Haversine(self,x,y): 
		self.a = math.pow(self.diff_lat/2,2) + math.cos(x.latitude)*math.cos(y.latitude)*math.pow(self.diff_lat/2,2)
		self.distance = 2*self.radius*math.asin(self.a)
		return self.distance





