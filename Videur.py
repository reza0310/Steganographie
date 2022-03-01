from PIL import Image

# On initialise des variables
image = Image.open("image_remplie.png")
texte_bin = ""
texte = ""
taille = int(input("On lit combien de pixels? Je recommande 1000 si vous savez vraiment pas. "))

# On charge l'image et sa taille
pixels = image.load()
width, height = image.size

# On initialise les même pointeurs que le remplisseur
x = 0
y = 0
# Pour autant de pixels que renseignés par l'utilisateur,
for i in range(taille):
    # On lit le pixel
    cpixel = pixels[x, y]
    # On convertit chaque canal en octet
    r = bin(cpixel[0])[2:].zfill(8)
    g = bin(cpixel[1])[2:].zfill(8)
    b = bin(cpixel[2])[2:].zfill(8)
    # On concatène les 2 bits les moins significatifs de chaque canal
    texte_bin += r[6:] + g[6:] + b[6:]
    # On décale les même pointeurs que le remplisseur
    y += 1
    if y == height:
        x += 1
        y = 0

# On parcours tout le texte binaire ainsi récupéré 2 octets par 2 octets
parcours = 0
while parcours < len(texte_bin)-16:
    # On convertit chaque groupe de 2 octets en lettre
    char = chr(int(texte_bin[parcours:parcours+16], 2))
    try:
        # On essaie d'interpréter le binaire en texte et de l'ajouter
        char.encode("utf-8")
        texte += char
        parcours += 16
    except:
        # Si l'utilisateur a demandé de lire plus de pixels que le nombre de pixels contenant du texte, 
        # l'interprétation du binaire en texte peut planter auquel cas on considère que tout le texte est lu et on arrête.
        break
# Pour finir on affiche le texte
print(texte)
