#Aluna: Maria Eduarda Nogueira Freitas

import random #importação do módulo para gerar os itens em locais pseudoaleatórios
import turtle #importação do módulo que permite a criação do jogo


#Criação da arena do jogo
def start():
    pen = turtle.Turtle()#criação da variável da caneta para desenhar a arena
    pen.shapesize(1.6)#tamanho personagem que irá desenhar
    pen.speed(8)#a velocidade que sera feita
    pen.shape('turtle')#forma do personagem que irá desenhar
    pen.up()#comando para a caneta não riscar a tela
    pen.goto(-330,-180)#cordenada que ela vai iniciar
    pen.down()#comando para a ceneta riscar a tela
    pen.pensize(5)#a espessura da linha
    pen.forward(650)#comando para ir para a frente
    pen.left(90)#comando para ir para cima
    pen.forward(450)
    pen.left(90)
    pen.forward(650)
    pen.left(90)
    pen.forward(450)
    pen.left(90)

    #Fim da caneta
    pen.hideturtle()

#Coloração da janela
janela = turtle.Screen()
janela.bgcolor('#DA70D6')

#Espaço destinado para a chamada de função de criação da janela
start()

#Importação dos ítens do jogo
caveira = 'caveira.gif'
coracao = 'coracao.gif'

#Comando para executar a entrada dos GIF's na janela do jogo
janela.addshape(caveira)
janela.addshape(coracao)

#Atribuições aos pontos de vida do personagem principal
#vida01
life1 = turtle.Turtle()#criar o objeto
life1.shapesize(1.1)#escolha do tamanho da imagem
life1.shape('turtle')#modelo do personagem
life1.color('#C71585')#cor
life1.speed(8)#a velocidade de locomoção
life1.up()#comando para o personagem não riscar a tela
life1.goto(-270,285)#cordenada que ele ficará na tela do jogo
life1.left(90)#angulação

#vida02
life2 = turtle.Turtle()
life2.shapesize(1.1)
life2.shape('turtle')
life2.color('#C71585')
life2.speed(8)
life2.up()
life2.goto(-295, 285)
life2.left(90)

#vida03
life3 = turtle. Turtle()
life3.shapesize(1.1)
life3.shape('turtle')
life3.color('#C71585')
life3.speed(8)
life3.up()
life3.goto(-320,285)
life3.left(90)

#Criação do personagem principal do jogo
tartaruga = turtle.Turtle()
tartaruga.shapesize(1.8)
tartaruga.speed(15)
tartaruga.shape('turtle')
tartaruga.left(90)
tartaruga.up()

#Criação do ítem utilizado para simular a perca de vidas do personagem (caveira)
poison = turtle.Turtle()
poison.shapesize(0.8)
poison.speed(5)
poison.up()
poison.goto(random.randint(-315, 310), random.randint(-155, 250))#Comando Random utilizado para o ítem iniciar em locais pseudoaleatórios da tela
poison.shape(caveira)

#Criação do ítem utilizado para a adicionar pontos ao personagem (coração)
score = turtle.Turtle()
score.shapesize(0.8)
score.speed(5)
score.up()
score.goto(random.randint(-315, 310), random.randint(-155, 250))
score.shape(coracao)

#Criação do placar utilizado para mostrar a pontuação
pontos = turtle.Turtle()
pontos.pencolor('black')
pontos.shape('turtle')
pontos.shapesize(0.8)
pontos.penup()
pontos.speed(0)
pontos.hideturtle()
pontos.goto(180,280)

#Criação da numeração do placar
s = 0 #Variavel zerada que será utilizada na somatória de pontos
numero = turtle.Turtle()
numero.pencolor('black')
numero.shape('turtle')
numero.shapesize(0.5)
numero.penup()
numero.speed(0)
numero.hideturtle()

#Comando de escrita da palavra 'Pontos'
pontos.write('Pontos = ', font=('Verdana',14,'normal'))

#Funções atribuídas para a movimentação do persosnagem principal
def tartarugasobe():
    y = tartaruga.ycor()
    y += 5 #velocidade de locomoção
    tartaruga.sety(y)#cordenada da movimentação

def tartarugadesce():
    y = tartaruga.ycor()
    y += -5
    tartaruga.sety(y)

def tartarugadireita():
    x = tartaruga.xcor()
    x += 5
    tartaruga.setx(x)

def tartarugaesquerda():
    x = tartaruga.xcor()
    x += -5
    tartaruga.setx(x)

#Comando de movimentação a partir do teclado (w,s,d,a)
janela.listen()
janela.onkeypress(tartarugasobe,"w")
janela.onkeypress(tartarugadesce,"s")
janela.onkeypress(tartarugadireita,"d")
janela.onkeypress(tartarugaesquerda,"a")

#Colisão dos ítens de dano e pontuação
while poison and score:
    poison.forward(5) #movimentação do ítem de dano (caveira)
    score.forward(5) #movimentação do ítem de pontos (coração)

    if poison.xcor() >= 310: #cordenadas do eixo 'x' da arena de jogo
        poison.speed(0)
        poison.setpos(310, poison.ycor())
        poison.left(random.randint(0,360))

    elif poison.xcor() <= -315:
        poison.speed(0)
        poison.setpos(-315, poison.ycor())
        poison.left(random.randint(0,360))

    elif poison.ycor() >= 250: #cordenadas do eixo 'y' da arena de jogo
        poison.speed(0)
        poison.setpos(poison.xcor(), 250)
        poison.left(random.randint(0,360))

    elif poison.ycor() <= -155:
        poison.speed(0)
        poison.setpos(poison.xcor(), -155)
        poison.left(random.randint(0,360))

    if score.xcor() >= 310: #cordenadas do eixo 'x' da arena de jogo
        score.speed(0)
        score.setpos(310, score.ycor())
        score.left(random.randint(0,360))

    elif score.xcor() <= -310:
        score.speed(0)
        score.setpos(-310, score.ycor())
        score.left(random.randint(0,360))

    elif score.ycor() >= 250: #cordenadas do eixo 'y' da arena de jogo
        score.speed(0)
        score.setpos(score.xcor(), 250)
        score.left(random.randint(0,360))

    elif score.ycor() <= -160:
        score.speed(0)
        score.setpos(score.xcor(), -160)
        score.left(random.randint(0,360))


    #Colisão do personagem principal
    if tartaruga.xcor() >= 295: #cordenadas do eixo 'x' de ate onde o porsonagem pode se mover dentro da arena
        tartaruga.speed(0)
        tartaruga.setpos(295, tartaruga.ycor())


    if tartaruga.xcor() <= -310:
        tartaruga.speed(0)
        tartaruga.setpos(-310, tartaruga.ycor())


    if tartaruga.ycor() >= 230:  # cordenadas do eixo 'y' de ate onde o personagem pode se mover dentro da arena
        tartaruga.speed(0)
        tartaruga.setpos(tartaruga.xcor(), 230)

    if tartaruga.ycor() <= -160:
        tartaruga.speed(0)
        tartaruga.setpos(tartaruga.xcor(), -160)

#Comando para subitrair uma vida ao encostar no elemento 'poison'
    if tartaruga.distance(poison)<=30 and life1.isvisible()== True:
        life1.hideturtle()
        poison.speed(0)
        poison.goto(random.randint(-295,295), random.randint(-250,150))

    if tartaruga.distance(poison)<=30 and life2.isvisible()== True:
        life2.hideturtle()
        poison.speed(0)
        poison.goto(random.randint(-295,295), random.randint(-250,150))

    if tartaruga.distance(poison)<=30 and life3.isvisible()== True:
        life3.hideturtle()
        turtle.bye()#quando a última vida for subtraída o programa Turtle será encerrado

#Comando para adicionar pontos ao encostar no elemento 'score'
    if tartaruga.distance(score)<= 30:
        numero.clear()#limpar o número anterior do placar
        s += 10
        numero.goto(280, 280)
        numero.write(s, font=('Verdana' , 14, ' normal'))
        score.speed(0)
        score.goto(random.randint(-310, 295), random.randint(-160, 230))


#Espaço destinado a chamada de funções de movimentação do personagem
tartarugasobe()
tartarugadesce()
tartarugadireita()
tartarugaesquerda()



#Comando para a janela permanecer aberta
janela.mainloop()