from challenge import *
import math 

def test_compare(AB,CD):
	if AB < CD: print "CABD is better path"
	elif AB == CD: print "Either is fine" 
	else: print "ACDB is better path "

def check():
	A = Solution()
	B = Solution()
	AB = Solution()
	C = Solution()
	D = Solution()
	CD = Solution()
	sol = Solution()
	A.coordinate(input("Longtitude for A: "),input("Latitude for A: "))
	B.coordinate(input("Longtitude for B: "),input("Latitude for B: "))
	C.coordinate(input("Longtitude for C: "),input("Latitude for C: "))
	D.coordinate(input("Longtitude for D: "),input("Latitude for D: "))
	AB.distance(A,B)
	CD.distance(C,D)
	AB = AB.Haversine(A,B)
	CD = CD.Haversine(C,D)
	return test_compare(AB,CD)

check()
