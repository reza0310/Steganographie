from PIL import Image

image = Image.open("image_remplie.png")
texte_bin = ""
texte = ""
taille = int(input("On lit quelle taille? Je recommande 1000 si vous savez pas. "))

pixels = image.load()
width, height = image.size

x = 0
y = 0
for i in range(taille):
    cpixel = pixels[x, y]
    r = bin(cpixel[0])[2:].zfill(8)
    g = bin(cpixel[1])[2:].zfill(8)
    b = bin(cpixel[2])[2:].zfill(8)
    texte_bin += r[6:] + g[6:] + b[6:]
    y += 1
    if y == height:
        x += 1
        y = 0

parcours = 0
while parcours < len(texte_bin)-16:
    char = chr(int(texte_bin[parcours:parcours+16], 2))
    try:
        char.encode("utf-8")
        texte += char
        parcours += 16
    except:
        break
print(texte)
