class GameSprite(sprite.Sprite):
#создание класса
    def __init__(self, player_image, player_x, player_y, player_speed, width, hight):
    #создание функции для характеристик
        super().__init__()
        #для характеристик
        self.image = transform.scale(image.load(player_image), (width, hight))
        #задать картинку
        self.speed = player_speed
        #задать скорость
        self.rect = self.image.get_rect()
        #задать прямоугольник в который вписан спрайт
        self.rect.x = player_x
        #задать координаты x
        self.rect.y = player_y
        #задать координаты y
    def reset(self):
    #создание функции для отображения
        window.blit(self.image, (self.rect.x, self.rect.y))
        #отображение картинки

class Player(GameSprite):
#создание класса
    def update(self):
    #функция для пердвижения
        keys_pressed = key.get_pressed()
        #получение событии клавиатуры
        if keys_pressed[K_RIGHT] and self.rect.x <650:
        #если нажата кнопка право и координаты меньше 650
            self.rect.x += self.speed
            #сдвинуться вправо
        if keys_pressed[K_LEFT] and self.rect.x >0:
        #если нажата кнопка лево и координаты больше 0
            self.rect.x -= self.speed
            #сдвинуться влево
