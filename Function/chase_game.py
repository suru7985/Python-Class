#pip install pgzero
import pgzrun
HEIGHT=500
WIDTH=500

player = Actor('alien')
enemy = Actor('enemy' , pos=(400,400))


music.play('bg2')

def draw():
    screen.clear()
    screen.blit('background',(0,0))
    player.draw()
    enemy.draw()

  

def enemy_chase_logic():
    if enemy.x > player.x:
        enemy.x -=1
    if enemy.x < player.x:
        enemy.x +=1
    if enemy.y > player.y:
        enemy.y -=1
    if enemy.y < player.y:
        enemy.y +=1
    if enemy.colliderect(player):
        sounds.punch.play() 
        player.image = 'splat'


    
def player_control():
    if keyboard.left:
        player.x -= 2
    if keyboard.right:
        player.x += 2
    if keyboard.up:
        player.y -= 2
    if keyboard.down:
        player.y += 2

def player_limit_check():
    if player.x < 0:
        player.x = WIDTH
    if player.x > WIDTH:
        player.x = 0
    if player.y < 0:
        player.y = HEIGHT
    if player.y > HEIGHT:
        player.y = 0

def update():
    enemy_chase_logic()
    player_control()
    player_limit_check()

pgzrun.go()            

