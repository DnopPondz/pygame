# ส่วนบนสุดของโค้ด (import เดิมๆ)
import pygame
import random
import time
import os

# ==== เพิ่มฟังก์ชันวาดปุ่ม ====
def draw_button(text, x, y, w, h, inactive_color, active_color, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x < mouse[0] < x+w and y < mouse[1] < y+h:
        pygame.draw.rect(screen, active_color, (x, y, w, h), border_radius=10)
        if click[0] == 1 and action is not None:
            action()
    else:
        pygame.draw.rect(screen, inactive_color, (x, y, w, h), border_radius=10)

    button_text = font.render(text, True, (255, 255, 255))
    text_rect = button_text.get_rect(center=(x + w/2, y + h/2))
    screen.blit(button_text, text_rect)


# หา path ของโฟลเดอร์ที่ไฟล์ dice_game.py อยู่
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

pygame.init()
width, height = 400, 300
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Dice Game")
font = pygame.font.Font(None, 36)
clock = pygame.time.Clock()

# โหลดภาพลูกเต๋า
dice_imgs = []
for i in range(1, 7):
    img_path = os.path.join(BASE_DIR, "dice_imgs", f"dice_{i}.png")
    print("Loading image:", img_path)
    image = pygame.image.load(img_path)
    dice_imgs.append(pygame.transform.scale(image, (100, 100)))

# ทอยเต๋าแบบแอนิเมชัน
def roll_dice():
    for _ in range(10):
        roll = random.randint(0, 5)
        screen.fill((255, 255, 255))
        screen.blit(dice_imgs[roll], (150, 100))
        pygame.display.update()
        time.sleep(0.1)
    return roll + 1

# ฟังก์ชันที่เรียกเมื่อต้องการทอยเต๋าจริง ๆ
def roll():
    global dice_number
    dice_number = roll_dice()

# ตัวแปรเริ่มต้น
running = True
dice_number = 1

# ลูปหลักของเกม
while running:
    screen.fill((255, 255, 255))
    screen.blit(dice_imgs[dice_number - 1], (150, 100))

    draw_button("ROLL DICE", 130, 220, 140, 50, (0, 180, 0), (0, 255, 0), action=roll)

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    clock.tick(30)

pygame.quit()
