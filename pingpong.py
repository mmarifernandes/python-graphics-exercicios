import time
import graphics as gf
import random

janela = gf.GraphWin("bolinha", 800, 500)


centro = gf.Point(400, 250)
raio = 10
bolinha = gf.Circle(centro, raio)

quadrado = gf.Rectangle(gf.Point(10, 490), gf.Point(790, 10))
middle = gf.Line(gf.Point(400, 10), gf.Point(400, 490))

ret1 = gf.Rectangle(gf.Point(20, 100), gf.Point(40, 200))
ret2 = gf.Rectangle(gf.Point(780, 100), gf.Point(760, 200))
ret1.setFill("pink")
ret2.setFill("blue")
# quadrado.setFill("black")
ret1.draw(janela)
ret2.draw(janela)
quadrado.draw(janela)
bolinha.draw(janela)
middle.draw(janela)

score1 = 0
score2 = 0

p1 = gf.Text(gf.Point(200, 50), score1)
p2 = gf.Text(gf.Point(600, 50), score2)
p1.setSize(20)
p2.setSize(20)
p1.draw(janela)
p2.draw(janela)
print(ret2.getCenter())

x = 50
y = 50
bx = 10
by = 0


while True:
    tecla = janela.checkKey()
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    if bolinha.getCenter().x < 780 and bolinha.getCenter().x > 20:
        bolinha.move(bx, by)
        time.sleep(0.03)
        if bolinha.getCenter().x == ret2.getP2().x and bolinha.getCenter().y < ret2.getP2().y and bolinha.getCenter().y > ret2.getP1().y:
            bx = -10
            by = random.randint(-1, 1)
        if bolinha.getCenter().x == ret1.getP2().x and bolinha.getCenter().y < ret1.getP2().y and bolinha.getCenter().y > ret1.getP1().y:
            bx = 10
            by = random.randint(-1, 1)
    else:
        if bolinha.getCenter().x >= 780:
            score1 += 1
            p1.undraw()
            bolinha.undraw()
            p1 = gf.Text(gf.Point(200, 50), score1)
            p1.setSize(20)
            p1.draw(janela)
            bolinha = gf.Circle(centro, raio)
            bolinha.draw(janela)
            by = random.randint(-1, 1)
            bx = -10
        if bolinha.getCenter().x <= 20:
            score2 += 1
            p2.undraw()
            bolinha.undraw()
            p2 = gf.Text(gf.Point(600, 50), score2)
            p2.setSize(20)
            p2.draw(janela)
            bolinha = gf.Circle(centro, raio)
            bolinha.draw(janela)
            by = random.randint(-1, 1)
            bx = 10

    if tecla != '':
        if tecla == "Up" and x < 130:
            ret2.move(0, -10)
            x += 10
            # print(x)
        if tecla == "Down" and x > -230:
            ret2.move(0, 10)
            x -= 10
        if tecla == "w" and y > -30:
            ret1.move(0, -10)
            y -= 10
            # print(y)
        if tecla == "s" and y < 330:
            ret1.move(0, 10)
            y += 10
            # print(y)
        if tecla == "space":
            bolinha.setFill(gf.color_rgb(r, g, b))
        anterior = tecla
