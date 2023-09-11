import graphics as gf
import random
# criando um objeto graphwin
janela = gf.GraphWin("bolinha", 500, 500)
tamanho = 40
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
x = 50
y = 50
combinada = ''
anterior = ''
# print(bolinha)
while True:
    tecla = janela.checkKey()
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    combinada = anterior + tecla
    if tecla != '':
        # print(tecla)
        # if combinada == 'RightDown':
        #     print(combinada)
        #     print(tecla, anterior)
        #     bolinha.move(5, 10)
        if tecla == "Right" and x < 490 - raio:
            bolinha.move(10,0)
            x+=10
            # print(x)
        if tecla == "Left" and x >  raio + 10:
            bolinha.move(-10,0)
            x-=10
            # print(x)
        if tecla == "Up" and y >  raio + 10:
            bolinha.move(0,-10)
            y-=10
            # print(y)
        if tecla == "Down" and y <  490 - raio:
            bolinha.move(0,10)
            y+=10
            # print(y)
        if tecla == "plus":
            tamanho += 10
            print(tamanho)
            bolinha.undraw()
            raio = tamanho
            centro = gf.Point(x, y)
            bolinha = gf.Circle(centro, raio)

            bolinha.setFill(gf.color_rgb(r, g, b))
            bolinha.draw(janela)
        if tecla == "minus" and tamanho > 0:

            tamanho -= 10
            print(tamanho)
            bolinha.undraw()
            raio = tamanho
            centro = gf.Point(x, y)
            print(centro)
            bolinha = gf.Circle(centro, raio)
            bolinha.setFill(gf.color_rgb(r, g, b))
            bolinha.draw(janela)
        if tecla == "space":
            bolinha.setFill(gf.color_rgb(r, g, b))
        anterior = tecla



            

        

coordenadas = janela.getMouse()


janela.close()
