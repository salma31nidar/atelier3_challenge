def custom_hash(data):
    # Initialisation d'une valeur de hash (nombre premier choisi pour minimiser les collisions)
    hash_value = 5381

    # Parcours des caractères de la chaîne et application de transformations
    for char in data:
        # Décalage binaire et combinaison avec le caractère courant
        hash_value = ((hash_value << 5) + hash_value) ^ ord(char)

    # Retourne le hash en format hexadécimal
    return hex(hash_value & 0xFFFFFFFFFFFFFFFF)


# Test de la fonction de hachage personnalisée
data1 = "Bonjour"
data2 = "Hello"
data3 = "Bonjour tout le monde"
data4 = "Bonjour"  # Même texte que data1 pour vérifier la cohérence

print("Hash de 'Bonjour':", custom_hash(data1))
print("Hash de 'Hello':", custom_hash(data2))
print("Hash de 'Bonjour tout le monde':", custom_hash(data3))
print("Hash de 'Bonjour' (encore):", custom_hash(data4))
