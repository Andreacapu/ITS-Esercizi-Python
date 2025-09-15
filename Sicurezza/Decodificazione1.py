m= 'Ciao Mondo!'

Mi=int(m.encode("utf-8").hex(), 16)

print(Mi)

n = '00c2c176c9164c99efa401ae3342ec'
'0721ce53b3f8d87ed3b1d0a52d7d50'
'4a080f7740384ebd89757ff3e9d1e6'
'91b2e590ae056991ec7350c471c120'
'bd0b04d00ebec0d0b895b7a7575912'
'444740d3ac9bba712c6341dc50880f'
'2ed702290859bad4c6b3662716ce28'
'a2ff4562a3bf2de8daf289f1e1b58a'
'7c6b068d18b9f42645650392ece45d'
'8aa8fd00a7e01a4480eb205db6ae79'
'12577a42fb221fa932cf9405c4a995'
'0b19d348766c3376c9b9bd9e0e2da7'
'b53a9c46f95af6935136ca2beba7b5'
'91b51c419faca3dddad6d4ed98099c'
'61471c0b4620141be61e52f2c75419'
'c709153258727adf92ca7ccc6efa8f'
'3e713ecf17e9b466ef60542f6a9333'
'22a7'

decimale = int(n, 16)

#cifra
M = 'Ciao, Mondo!'

Mi=int(M.encode("utf-8").hex(), 16)

e= 3

c=pow(Mi, e, decimale)
print(c)