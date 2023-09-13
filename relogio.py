import graphics as gf
from datetime import datetime


data = datetime.now()
hora_atual = data.strftime("%H:%M:%S")

janela = gf.GraphWin("bolinha", 500, 500)

hora_atual = hora_atual.split(":")
print(hora_atual)
centro = gf.Point(250, 250)
raio = 200
circulo = gf.Circle(centro, raio)
phora = gf.Line(gf.Point(250,250), gf.Point(180,350))

# doze = gf.Text(gf.Point(250,100), "12")
# um = gf.Text(gf.Point(300,140), "01")
# dois = gf.Text(gf.Point(350,180), "02")
# tres = gf.Text(gf.Point(400,220), "03")
# doze = gf.Text(gf.Point(250,100), "12")
# doze = gf.Text(gf.Point(250,100), "12")
phora.draw(janela)
circulo.draw(janela)
# doze.draw(janela)
# um.draw(janela)
# dois.draw(janela)
# tres.draw(janela)
janela.getMouse()