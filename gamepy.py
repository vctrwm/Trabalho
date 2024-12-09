import pygame
import random

# Inicializa o pygame
pygame.init()

# Configurações da tela
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Fórmula 1: Desafio de Pistas')

# Cores
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Carregar imagens
car_image = pygame.image.load('carro.png')  # Carregar imagem do carro
car_width = 50
car_height = 100

# Posição inicial do carro
car_x = screen_width // 2 - car_width // 2
car_y = screen_height - car_height - 10

# Velocidade do carro
car_speed = 5

# Pontuação e tempo
score = 0
time_left = 30  # Tempo inicial em segundos
font = pygame.font.SysFont(None, 36)

# Função para exibir a pontuação
def show_score(score, time_left):
    score_text = font.render(f'Pontuação: {score}', True, WHITE)
    time_text = font.render(f'Tempo: {time_left}', True, WHITE)
    screen.blit(score_text, (10, 10))
    screen.blit(time_text, (screen_width - 150, 10))

# Função principal do jogo
def game_loop():
    global car_x, car_y, score, time_left
    clock = pygame.time.Clock()
    game_running = True
    start_ticks = pygame.time.get_ticks()  # Marca o tempo inicial

    while game_running:
        screen.fill(GREEN)  # Cor de fundo (pista)

        # Verificar eventos (fechar o jogo)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_running = False

        # Movimentação do carro
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            car_x -= car_speed
        if keys[pygame.K_RIGHT]:
            car_x += car_speed
        if keys[pygame.K_UP]:
            car_y -= car_speed
        if keys[pygame.K_DOWN]:
            car_y += car_speed

        # Impedir que o carro saia da tela
        if car_x < 0:
            car_x = 0
        elif car_x > screen_width - car_width:
            car_x = screen_width - car_width
        if car_y < 0:
            car_y = 0
        elif car_y > screen_height - car_height:
            car_y = screen_height - car_height

        # Atualizar a pontuação e tempo
        time_left = 30 - (pygame.time.get_ticks() - start_ticks) // 1000
        if time_left <= 0:
            time_left = 30  # Reiniciar o tempo
            score += 1  # Adicionar ponto a cada volta

        # Exibir pontuação e tempo
        show_score(score, time_left)

        # Desenhar o carro
        screen.blit(car_image, (car_x, car_y))

        # Atualizar a tela
        pygame.display.update()

        # Controle de FPS
        clock.tick(60)

    pygame.quit()

# Chamar a função principal para iniciar o jogo
game_loop()