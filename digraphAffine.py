alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
'S','T', 'U', 'V', 'W', 'X', 'Y', 'Z', ' ']

message = "PSQIUF" 
a = 320
b = 155 
a_ = 344 % 729


PS = 27*15 + 18
QI = 27*16 + 8
UF = 27*20 + 5 

PS_ = (a_*PS - b*a_) % 729
QI_ = (a_*QI - b*a_) % 729 
UF_ = (a_*UF - b*a_) % 729


message_ = ""


message_ += alpha[PS_ //27] 
message_ += alpha[PS_ % 27]

message_ += alpha[QI_ //27]
message_ += alpha[QI_ % 27]

message_ += alpha[UF_ //27]
message_ += alpha[UF_ % 27]


print(message_) 
