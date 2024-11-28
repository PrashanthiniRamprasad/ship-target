import pgzrun

WIDTH = 1400
HEIGHT = 700
ship = Actor("ship")
bug = Actor("bug")
speed = 5
ship.pos = (WIDTH / 2, HEIGHT - 50)

enemies = []
hearts = []

for x in range(10):
    for y in range(3):
        enemies.append(Actor("bug"))
        enemies[-1].x = 100 + 50 * x
        enemies[-1].y = 80 + 50 * y

score = 0
direction = 1
ship.dead = False
ship.countdown = 90


def displayScore():
    screen.draw.text(str(score), (50, 30))


def gameover():
    screen.draw.text("game over", (200, 200))


def on_key_down(key):
    if ship.dead is False:
        hearts.append(Actor("heart"))
        hearts[-1].x = ship.x
        hearts[-1].y = ship.y - 50


def update():
    global score
    global direction
    move_down = False

    if ship.dead is False:
        if keyboard.left:
            ship.x -= speed
            if ship.x <= 0:
                ship.x = 0
        elif keyboard.right:
            ship.x += speed
            if ship.x >= WIDTH:
                ship.x = WIDTH
    for heart in hearts:
        if heart.y <= 0:
            hearts.remove(heart)
        else:
            heart.y -= 10
    if len(enemies) == 0:
        gameover()
    if len(enemies) > 0 and (enemies[-1].x > WIDTH - 80 or enemies[0].x > 80):
        move_down = True
        direction = direction * -1
    for enemy in enemies:
        enemy.x += 5 * direction
        if move_down is True:
            enemy.y += 0.5
        if enemy.y > HEIGHT:
            enemies.remove(enemy)

        for heart in hearts:
            if enemy.colliderect(heart):
                score += 100

                hearts.remove(heart)

                enemies.remove(enemy)
                if len(enemies) == 0:
                    gameover()

        if enemy.colliderect(ship):
            ship.dead = True
    if ship.dead:
        ship.countdown -= 1
    if ship.countdown == 0:
        ship.dead = False
        ship.countdown = 90


power_up_active = False


def draw():
    screen.clear()
    screen.fill("black")
    for heart in hearts:
        heart.draw()
    for enemy in enemies:
        enemy.draw()
    if ship.dead is False:
        ship.draw()
    displayScore()
    if len(enemies) == 0:
        gameover()


pgzrun.go()
