#Pygame:
# pip install pygame

#1. Import .............
import pygame
import random

from ghost import Ghost
from bat import Bat
from shoot import Shoot

#2. INicializacao ........

#2.1 Iniciar o Pygame
pygame.init()

#2.2 Iniciar a janela com a configuracao de resolucao de 840x480

#2.2..1 Constante de largura e Altura da Tela
WIDTH_SCREEN = 840     # Largura
HEIGHT_SCREEN = 480    # Altura

#2.2.2 Criar a janela
display = pygame.display.set_mode ([WIDTH_SCREEN, HEIGHT_SCREEN])

#2.2..3 Preencher o fundo da janela com cor RGB
display.fill([52, 70, 235])


#2.2.4 Mudar o titulo da janela
pygame.display.set_caption('Game L.F.S Senai-Python')

#2.2.5 Carregar a imagem para craiar icone
icone = pygame.image.load('data/icone.png')
pygame.display.set_icon(icone)

#3. Elementod da Tela .........

#3.1 Personagens

#Criar um grupo de imagens para carregar todas imagens e desenha de uma vez

objectGroup = pygame.sprite.Group()
batGroup = pygame.sprite.Group()
shootGroup = pygame.sprite.Group()

# Criar um cenario ou fundo  (bachgroud) para o fantasma
bg =pygame.sprite.Sprite(objectGroup)
bg.image = pygame.image.load("data/background.jpg")
bg.image = pygame.transform.scale(bg.image, [840,840])
bg.rect = bg .image.get_rect()

# Criar um objeto Sprite para manipular a imagem  -Fantasma
ghost = Ghost(objectGroup)

# 3.2 Fontes............
score_font = pygame.font.Font("font/Pixeltype.ttf", 50)
GAMEOVER_font = pygame.font.Font("font/Pixeltype.ttf", 200)

# 3.3 Musica ---------
pygame.mixer_music.load("data/alienblues.wav")
pygame.mixer_music.play(-1)

# 3.4 Som (sfx)
attack =pygame.mixer.Sound("data/magic1.wav")


#4. Variaveis Globais .........
GAMELOOP = True
GAMEOVER = False

timer =20
pontos =0



# 4.1 Criar um clock para ajustar os frames por segundo (FPS)
clock = pygame.time.Clock()

#5. Funcao Principal
def main():
    global GAMELOOP
    global GAMEOVER
    global timer
    global pontos

    #CRIAR O GAME lOOP
    while GAMELOOP:

        #Clock para 60fps
        clock .tick (80)



        # verificacao dos eventos possiveis 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                GAMELOOP = False
            elif event.type ==pygame.KEYDOWN:
                if event.key == pygame. K_SPACE:
                    newShoot = Shoot(objectGroup, shootGroup)
                    newShoot.rect.center = ghost.rect.center
                    attack.play()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                newShoot = Shoot(objectGroup, shootGroup)
                newShoot.rect.center = ghost.rect.center
                attack.play()


        if not GAMEOVER:    
            
            display.fill([52, 70, 235])           

            # Criar os varios morcegos
            timer+= 1
            if timer > 30:
                    timer = 0
                    if random.random() < 0.3:
                        meuBat = Bat(objectGroup, batGroup)

            # Colisao dos Morcegos com Fantasma    
            colisao = pygame.sprite.spritecollide(ghost, batGroup, False, pygame.sprite.collide_mask )    

            if colisao:
               print("GAME OVER !!!")   
               GAMEOVER =True

            # Colisao do tiro com morcego
            tiros = pygame.sprite.groupcollide(shootGroup,batGroup,True,True, pygame.sprite.collide_mask)

            # Contagem de morcegos mortos
            if tiros:
                pontos += 1
                print("Score:",pontos)
                
            objectGroup.update()

       

        # Desenhando os elementos dos grupos na minha janela

        objectGroup.draw(display)

        score_render = score_font.render(f'Score: {pontos}',False,'White')
        display.blit(score_render,(650 , 50))

        #iNSERINDO O GAME OVER NA TELA
        if GAMEOVER:
            GAMEOVERMsg = GAMEOVER_font.render('GAME OVER',False,'White')
            display.blit(GAMEOVERMsg,(100,150))



        # Atualizaçao de tela
        pygame.display.update()

if __name__ == "__main__":
    main()


