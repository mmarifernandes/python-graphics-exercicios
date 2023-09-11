import time
import graphics as gf
import random
# criando um objeto graphwin
janela = gf.GraphWin("bolinha", 500, 500)
centro = gf.Point(50, 50)
raio = 40
bolinha = gf.Circle(centro, raio)
quadrado = gf.Rectangle(gf.Point(10, 490), gf.Point(490, 10) )
texto = gf.Text(gf.Point(250,250),"bolinha")
texto.setSize(30)
texto.draw(janela)
quadrado.draw(janela)
bolinha.draw(janela)

# bolinha = gf.Point(10,10)
x = 0
y = 0

combinada = ''
anterior = ''
while True:
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    tecla = janela.checkKey()
    if tecla != '':
        if tecla == "space":
            bolinha.setFill(gf.color_rgb(r, g, b))
    if y <= 390:
        time.sleep(0.03)
        bolinha.move(0, 10)
        y+=10
    if y >= 391 and y < 800:
        time.sleep(0.03)
        bolinha.move(10,0)
        y += 10
    if y >= 800 and y < 1199:
        time.sleep(0.03)
        bolinha.move(0, -10)
        y+=10
    if y >= 1200 and y <= 1599:
        time.sleep(0.03)
        bolinha.move(-10,0)
        y+=10
        if y == 1600:
            y = 0
