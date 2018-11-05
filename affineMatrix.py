
cipher= "U?DIPPWKCKIKFBWZERRXTV AXN,FG.SAYCHYVTMIMBG.LHTV KCPEAF?.FSGGZ.YOQMZQL.DWKLHYCHIVT,REEKQMJSLEAFXWWVFMKQQUQEWOQHI .BOG.UN.JGNIZQYESRMOQGNWMTVZHF,OKQYZQBLVNQ.MJSLMKQQUQRXKMJEG.ZH WRM.HYNDV,REE,RGBJR.F?NFHMHGHSFMKTZPDKA?EVJEM W?T MDOYU.FSFYCKWSHKNGEG.LH?NFHMHGHSFOQCCESRM?N,RZBE,.HZZQLIHWWCZ.KHIIJOWIHW..HQQUQUNRMJR.F?TWANUEGSEGTSHFXWZGHDOOQGNVFMKWE,MBFE,.H,XOQWKZBOTRZON.ECJQLWZFXWZQQUQ.GMZCIG.VZKWV.Q.NXVTG.QQUQ.USFMKBOBFEM WYCHIVTJR.FJLVZGNMJSL?Z QIOWCESRMSFSWSEYRWK"

alphabet = {'A':0, 'B':1, 'C':2,'D':3, 'E':4, 'F':5, 'G':6, 'H':7, 'I':8, 'J':9, 'K':10, 'L':11,'M':12, 'N':13, 'O':14, 'P':15, 'Q':16, 'R':17, 'S':18, 'T':19, 'U':20, 'V':21, 'W':22, 'X':23, 'Y':24, 'Z':25, ' ':26, ',':27, '.':28, '?':29 } 

alphaInverse =  ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
'S','T', 'U', 'V', 'W', 'X', 'Y', 'Z', ' ', ',', '.', '?']

A = [[14, 5], [3, 11]]
Ainv = [[-1, -5], [3, -4]]

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

def matrixMult(mat1, mat2):
	return [(mat1[0][0]*mat2[0] + mat1[0][1]*mat2[1]) %30, (mat1[1][0]*mat2[0] + mat1[1][1]*mat2[1])%30] 

mat = stringToMatrix(cipher)

output = []
for elem in mat:
	output.append(matrixMult(Ainv, elem))

print(matrixToString(output))
