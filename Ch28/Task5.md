LDM #0 STO Count LDM #78 letter N STO Letter LOOP: LDD Count INC ACC STO Count IN CMP Letter JPN LOOP ENDLOOP:LDM #48 ADD Count digit to ASCII OUT

End of chapter questions

1 a AND compares two bits in the same position and if both are 1 it puts a 1 in this position of the result word, otherwise it puts a 0 in this position of the result word

b AND MASK MASK: #B00001111 // mask

2 Loop LDR #0 STI STRING INC IX CMP #33 JPN LOOP END