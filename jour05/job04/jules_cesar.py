def lettres(message, decalage):
  alphabet = "abcdefghijklmnopqrstuvwxyz"
  message_decale = ""
  for lettre in message:
    if lettre.lower() in alphabet:
      indice = alphabet.index(lettre.lower())
      indice_decale = (indice + decalage) % 26
      if lettre.isupper():
        message_decale += alphabet[indice_decale].upper()
      else:
        message_decale += alphabet[indice_decale]
    else:
      message_decale += lettre
  return message_decale


message = "Bonjour"
decalage = 3
print(lettres(message, decalage))