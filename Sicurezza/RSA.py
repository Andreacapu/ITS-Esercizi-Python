#Genero chiave privata forzando esponente pubblico a 3:
#openssl genrsa -out FAprivkey.pem -3 2048

#Genero chiave pubblica a partire da quella privata:
#openssl rsa -in FAprivkey.pem -out FApubkey.pem -pubout -RSAPublicKey_out

#Leggo chiave privata:
#openssl rsa -in FAprivkey.pem -noout -text
# (visto che la chiave pubblica si ottiene a partire da quella privata, nella chiave privata ci sono già tutte le informazioni necessarie)

#Se proprio voglio leggo anche la chiave pubblica:
#openssl rsa -in FApubkey.pem -pubin -noout -text


modulo = '''00:db:6e:a2:c0:f6:ca:f6:01:21:06:e4:3a:8b:d8:
    09:47:40:6e:13:b8:02:91:2b:dd:90:33:50:0d:19:
    a2:b9:44:bc:37:b7:8d:7f:7f:26:7d:2a:3e:22:70:
    1a:03:8e:ef:82:61:16:db:bf:a9:f0:3d:80:bf:01:
    c7:50:4f:34:13:67:75:cf:ed:77:08:9f:cc:6e:fb:
    c8:39:7a:2a:77:2c:3f:29:5d:9b:70:da:09:89:9e:
    5d:ab:de:b3:36:24:0f:19:72:94:fc:66:31:b4:2d:
    cf:6e:b0:bf:ec:b8:b7:c4:1e:46:c5:a5:3a:bc:e2:
    93:3c:94:a8:71:93:a5:85:5d:40:a4:15:02:f8:d7:
    39:6f:c3:13:de:6e:b8:3b:2a:49:4b:22:26:94:e1:
    da:49:9c:d4:5b:cf:3f:54:3f:5d:60:1a:13:60:dc:
    2f:f7:ed:64:26:0f:c7:fb:a4:15:f7:db:cd:a4:6a:
    6b:4f:dd:b8:ed:52:93:13:d6:70:34:0c:7e:0e:a0:
    da:68:8f:c5:89:3f:af:15:4d:38:28:74:a0:e9:b3:
    4b:6e:28:d4:0f:15:92:52:aa:34:a5:da:b4:02:88:
    d7:09:ab:85:cf:73:91:d5:cb:cb:57:75:c6:59:37:
    d6:66:d8:86:08:29:6d:21:72:34:c6:42:2c:df:65:
    85:e5'''


modulo = modulo.replace(" ", "").replace(":", "").replace("\n", "") # tolgo tutti gli spazi i due punti e gli a capo
modulo = int(modulo, 16) # converto in esadecimale
print("Modulo:", modulo, "\n")

plain_text = int("maremma se fallisco".encode("utf-8").hex(), 16) # creo il plain_text già convertito in hex

print("Messaggio in hex (da stringa a bytes e da bytes a hex):", plain_text, "\n")

messaggio_cifrato = pow(plain_text, 3, modulo)  # cifro il messaggio con esponente pubblico 3 e il modulo 

print("Messaggio cifrato pow(messaggio, esponente_pubblico (3), modulo):", messaggio_cifrato, "\n")

priv_exponent = '''00:92:49:c1:d5:f9:dc:a4:00:c0:af:42:d1:b2:90:
    06:2f:80:49:62:7a:ac:60:c7:e9:0a:cc:e0:08:bb:
    c1:d0:d8:7d:7a:7a:5e:54:ff:6e:fe:1c:29:6c:4a:
    bc:02:5f:4a:56:eb:64:92:7f:c6:a0:29:00:7f:56:
    84:e0:34:cd:62:44:f9:35:48:fa:05:bf:dd:9f:52:
    85:7b:a6:c6:fa:1d:7f:70:e9:12:4b:3c:06:5b:be:
    e9:1d:3f:22:24:18:0a:10:f7:0d:fd:99:76:78:1e:
    8a:49:cb:2a:9d:d0:7a:82:be:d9:d9:18:d1:d3:41:
    b7:7d:b8:70:4b:b7:c3:ae:3c:ee:32:07:53:a1:40:
    c3:2c:75:f4:a5:fa:cc:87:3a:ac:be:97:fe:ce:a8:
    42:95:63:11:ce:c0:3d:a5:1d:ad:9e:1f:f7:36:ba:
    2c:fb:f4:9c:75:ea:5c:4f:53:1e:b2:21:67:dd:21:
    49:fc:16:a2:a3:51:7f:cf:e3:c0:75:9b:2c:03:f8:
    d9:dd:f6:ec:52:be:4a:d2:ff:ee:90:2f:aa:5b:ab:
    ab:f9:48:e2:c3:d7:d3:07:4d:a7:00:31:a8:95:16:
    74:22:04:48:b3:2a:05:16:7d:b5:a4:45:42:42:1c:
    ca:0c:f7:19:f7:77:35:f7:4c:d2:0c:f8:88:1f:a8:
    86:6b'''


priv_exponent = priv_exponent.replace(" ", "").replace("\n", "").replace(":", "") # tolgo tutti gli spazi i due punti e gli a capo
priv_exponent = int(priv_exponent, 16) # converto in esadecimale

print("Esponente privato in hex:", priv_exponent, "\n")

messaggio_decifrato = pow(252676329762091345695747235427073948250209404101335094846151304930943939412755668701634706883710307826749733982244955176342178346297493109873504829388875833202859236424983757013508364970032858231339122293046610787342793484623454577902877400952962274287, priv_exponent, modulo) # cifro il messaggio con esponente privato e il modulo 

print("Messaggio decifrato pow(messaggio cifrato, esponente privato, modulo):", messaggio_decifrato, "\n")

print("Il messaggio originale (in hex) è uguale al messaggio decifrato (sempre in hex)?", plain_text == messaggio_decifrato, "\n")


# converisone da hex ad ascii fatta da chatgpt non spiegata dal prof probabilmente non serve

length = (messaggio_decifrato.bit_length() + 7) // 8
msg_bytes = messaggio_decifrato.to_bytes(length, "big")
plaintext = msg_bytes.decode("utf-8")
print(plaintext)