from PIL import Image, ImageDraw

image = Image.open(input("Dans quelle image souhaitez-vous injecter texte.txt? (Tapez le nom du fichier) "))

texte_bin = ""
# On lit le fichier texte à injecter
with open("texte.txt", "r", encoding="utf-8") as f:
    lignes = f.readlines()
# On parcourt chaque caractère à injecter et on le sauvegarde sur 2 octets
for li in lignes:
    for char in li:
        texte_bin += bin(ord(char))[2:].zfill(16)
print(len(texte_bin), "bits à injecter.")

# On charge et prépare l'image
pixels = image.load()
width, height = image.size
pointeur = ImageDraw.Draw(image)

# On initialise les pointeurs
x = 0
y = 0
# Tant qu'il nous reste du texte à injecter,
while len(texte_bin) != 0:
    # On lit le pixel actuel
    cpixel = pixels[x, y]
    # On récupère et convertit en octets les canaux r, g et b
    r = bin(cpixel[0])[2:].zfill(8)
    g = bin(cpixel[1])[2:].zfill(8)
    b = bin(cpixel[2])[2:].zfill(8)
    # On vérifie qu'il reste au moins 6 bits à injecter car on les injecte 6 par 6 (on fait sur les 3 canaux et les 2 bits les moins significatifs et 3*2 = 6) donc s'il n'en reste pas assez ça risque de planter donc on remplit au besoin
    while len(texte_bin) < 6:
        texte_bin += "0"
    # On sépare les bits en trois groupes de deux car on travaille en trois channels et 2 bits par channels 
    un = texte_bin[0] + texte_bin[1]
    deux = texte_bin[2] + texte_bin[3]
    trois = texte_bin[4] + texte_bin[5]
    # On supprime du texte à injecter les 6 bits que l'on vient de préparer
    texte_bin = texte_bin[6:]
    # On remplace, dans chaque canal, les deux bits les moins significatifs par les paquets nouvellement créés et on les convertit en integer
    r = int(r[:6]+un, 2)
    g = int(g[:6]+deux, 2)
    b = int(b[:6]+trois, 2)
    # On réécrit LE pixel actuel avec les nouvelles valeurs RGB
    pointeur.point((x, y), (r, g, b))
    # On fait avancer les pointeurs
    y += 1
    if y == height:
        x += 1
        y = 0
print(y+x*height, "pixels remplis. Communiquez ce chiffre à votre correspondant pour qu'il le rentre dans le videur.")
# Une fois sortis de la boucle, le texte est complétement injecté donc on peut sauvegarder.
image.save("image_remplie.png")
