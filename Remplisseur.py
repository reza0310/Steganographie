from PIL import Image, ImageDraw

image = Image.open("image.jpg")
texte_bin = ""
with open("texte.txt", "r", encoding="utf-8") as f:
    lignes = f.readlines()
for li in lignes:
    for char in li:
        texte_bin += bin(ord(char))[2:].zfill(16)
print(len(texte_bin))

pixels = image.load()
width, height = image.size
pointeur = ImageDraw.Draw(image)

x = 0
y = 0
while len(texte_bin) != 0:
    cpixel = pixels[x, y]
    r = bin(cpixel[0])[2:].zfill(8)
    g = bin(cpixel[1])[2:].zfill(8)
    b = bin(cpixel[2])[2:].zfill(8)
    while len(texte_bin) < 6:
        texte_bin += "0"
    un = texte_bin[0] + texte_bin[1]
    deux = texte_bin[2] + texte_bin[3]
    trois = texte_bin[4] + texte_bin[5]
    texte_bin = texte_bin[6:]
    r = int(r[:6]+un, 2)
    g = int(g[:6]+deux, 2)
    b = int(b[:6]+trois, 2)
    pointeur.point((x, y), (r, g, b))
    y += 1
    if y == height:
        x += 1
        y = 0
image.save("image_remplie.png")