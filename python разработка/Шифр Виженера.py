tabula_recta = ["".join([ chr(x) for x in (range(97+y, 123+y)) if x < 123 ] + [ chr(x-123+97) for x in (range(97+y, 123+y)) if x >= 123 ]) for y in (range(26)) ]
 
def norm_key(key, word):
	return key * (len(word)//len(key)) + key[:len(word)%len(key)]
 
def coder(word, key):
	return "".join([ tabula_recta[ord(x)-97][ord(y)-97] for (i,x) in enumerate(word) for (n,y) in enumerate(norm_key(key, word)) if n == i ])
 
def decoder(word, key):
	return "".join([ chr(tabula_recta[ord(x)-97].index(y)+97) for (i,x) in enumerate(norm_key(key, word)) for (n,y) in enumerate(word) if n == i ])

print("Шифрование с использованием системы шифрования Вижинера:")
print(coder("ivanov", "biology"))

print("Расшифровка с использованием системы шифрования Вижинера:")
print(decoder("jdoycb", "biology"))

