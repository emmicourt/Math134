import numpy as np


cipher= "U?DIPPWKCKIKFBWZERRXTV AXN,FG.SAYCHYVTMIMBG.LHTV KCPEAF?.FSGGZ.YOQMZQL.DWKLHYCHIVT,REEKQMJSLEAFXWWVFMKQQUQEWOQHI .BOG.UN.JGNIZQYESRMOQGNWMTVZHF,OKQYZQBLVNQ.MJSLMKQQUQRXKMJEG.ZH WRM.HYNDV,REE,RGBJR.F?NFHMHGHSFMKTZPDKA?EVJEM W?T MDOYU.FSFYCKWSHKNGEG.LH?NFHMHGHSFOQCCESRM?N,RZBE,.HZZQLIHWWCZ.KHIIJOWIHW..HQQUQUNRMJR.F?TWANUEGSEGTSHFXWZGHDOOQGNVFMKWE,MBFE,.H,XOQWKZBOTRZON.ECJQLWZFXWZQQUQ.GMZCIG.VZKWV.Q.NXVTG.QQUQ.USFMKBOBFEM WYCHIVTJR.FJLVZGNMJSL?Z QIOWCESRMSFSWSEYRWK"

alphabet = {'A':0, 'B':1, 'C':2,'D':3, 'E':4, 'F':5, 'G':6, 'H':7, 'I':8, 'J':9, 'K':10, 'L':11,'M':12, 'N':13, 'O':14, 'P':15, 'Q':16, 'R':17, 'S':18, 'T':19, 'U':20, 'V':21, 'W':22, 'X':23, 'Y':24, 'Z':25, ' ':26, ',':27, '.':28, '?':29 } 

alphaInverse =  ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
'S','T', 'U', 'V', 'W', 'X', 'Y', 'Z', ' ', ',', '.', '?']

def stringToMatrix(input):
	out = []
	i = 0  
	while i < len(cipher)-1: 
		out.append( [ alphabet.get(cipher[i]), alphabet.get(cipher[i+1])] )
		i += 2
	return out

def matrixToString(input):
	out = "" 
	for elem in input:
		out += alphaInverse[elem[0]]
		out += alphaInverse[elem[1]]
	return out

a = stringToMatrix(cipher)
print(matrixToString(a))
