import pygame
import random
import time
import os

# หา path ของโฟลเดอร์ที่ไฟล์ dice_game.py อยู่
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

pygame.init()
width, height = 400, 300
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Dice Game")     
font = pygame.font.Font(None, 48)
clock = pygame.time.Clock() 

# load dice images จากโฟลเดอร์ dice_imgs ที่อยู่ใต้ BASE_DIR
dice_imgs = []
for i in range(1, 7):
    img_path = os.path.join(BASE_DIR, "dice_imgs", f"dice_{i}.png")
    print("Loading image:", img_path)      # ตรวจสอบว่ารู้ path ถูกต้อง
    image = pygame.image.load(img_path)
    dice_imgs.append(pygame.transform.scale(image, (100, 100)))   

def roll_dice():
    for _ in range(10):
        roll = random.randint(0, 5)
        screen.fill((255, 255, 255))
        screen.blit(dice_imgs[roll], (150, 100))
        pygame.display.update()
        time.sleep(0.1)
    return roll + 1

running = True
dice_number = 1

while running:
    screen.fill((255, 255, 255))
    
    # แสดงลูกเต๋า
    screen.blit(dice_imgs[dice_number - 1], (150, 100))
    
    # แก้บรรทัดนี้ให้ถูกต้อง เป็น = ไม่ใช่ =- 
    text = font.render("Press SPACE to roll", True, (0, 0, 0))
    screen.blit(text, (60, 20))
    
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
          running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            dice_number = roll_dice()
                
    clock.tick(30)  

pygame.quit()
