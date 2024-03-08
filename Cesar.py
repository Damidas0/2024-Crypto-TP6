from random import randint

class Cesar :
  def __init__(self, key=None) :
    self.key = key
   
   
   
    #Cette fonction utilise la clé pour
    #faire un chifferement de Cesar par décalage
    #
    #Le chifferement de `plain` est retourné dans `cipher`
  def encode(self, plain:str):
    cipher = ""
    for letter in plain : 
        if (letter != ' ') :
            letter = ord(letter)
            print("================ : " +  str(self.key))

            letter = ((letter + key-65) % 26 ) + 65
            print(letter)
            cipher += chr(letter)
        else : 
            cipher += ' '
    return cipher


  def decode(self, cipher):
    plain = ""
    self.key = -self.key 
    print("================ : " +  str(self.key))
    plain = self.encode(cipher)
    self.key = -self.key 
    return plain
    #Cette fonction utilise la clé pour
    #faire un déchifferement de Cesar par décalage
    #
    #Le déchifferement de `cipher` est retourné dans `plain`


def bruteforce_decrypt(cesar, cipher):
    assert isinstance(cesar, Cesar)

    print("Les possibilités de déchiffrement de {} sont :".format(cipher))
    
    #La suite de la fontion doit imprimer toutes les possibilités de déchiffrement ligne par ligne

def chosen_cipher(cesar):
    assert isinstance(cesar, Cesar)
    #déduire la clé en utilisant cesar.decode()
    #key = 
    #

    print("la clé de chiffrement est : {}".format(key))
    return key

def chosen_plain(cesar):
    assert isinstance(cesar, Cesar)
    #déduire la clé en utilisant cesar.code() mais sans utiliser cesar.decode()
    #keyabs = 
    #

    print("la clé de chiffrement est : {}".format(key))
    return key

def known_plain(plain, cipher):
    #cipher est le message obtenu en chiffrant plain
    #déduire la clé à partir de plain et cipher
    #keyabs = 
    #

    print("la clé de chiffrement est : {}".format(key))
    return key

key = int(input("Veuillez saisir une clé de chiffrement ('-1' pour une clé aléatoire) :"))
cesar = Cesar() if key<0 else Cesar(key)

plain = input("Veuillez saisir un texte à chiffrer par la clé {}:".format(cesar.key))

print("Le chiffrement de {} par la clé {} est : {}".format(plain, cesar.key, cesar.encode(plain)))

cipher = input("Veuillez saisir un texte à déchiffrer par la clé {}:".format(cesar.key))

print("Le déchiffrement de {} par la clé {} est : {}".format(cipher, cesar.key, cesar.decode(cipher)))

# Ajoutez vos tests