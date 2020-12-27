#encoded string in octal and not decimal
encoded = "152 162 152 145 162 167 150 172 153 162 145 170 141 162"
# to list
list_encoded = encoded.split(' ')
# convert to decimal from octal
decimal_encoded = [int(i, 8) for i in list_encoded]
# convert to char list
string_encoded = [chr(i) for i in decimal_encoded]
# to string
string_encoded  = ''.join(string_encoded)

print(string_encoded)

key = "110 157 167 040 155 165 143 150 040 144 151 144 040 115 141 147 147 151 145 040 157 162 151 147 151 156 141 154 154 171 040 143 157 163 164 077 040 050 104 151 166 151 144 145 144 040 142 171 040 070 054 040 164 157 040 164 150 145 040 156 145 141 162 145 163 164 040 151 156 164 145 147 145 162 054 040 141 156 144 040 164 150 145 156 040 160 154 165 163 040 146 157 165 162 051"

list_encoded1 = key.split(' ')
decimal_encoded1 = [int(i, 8) for i in list_encoded1]
string_encoded1 = [chr(i) for i in decimal_encoded1]
string_encoded1  = ''.join(string_encoded1)

print(string_encoded1)
print("result is", round(847.63 / 8) + 4)
print("key is", chr(110))
print("full key is", "n"+"n"+chr(ord('n')-4))
print("flag is wearenumberone")
