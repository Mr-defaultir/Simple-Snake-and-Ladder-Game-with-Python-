import random

# مکان شروعی بازیکن
player_position = 1

# مکان پایانی بازیکن
end_position = 100

# مکان پل ها در بازی
ladders = {2: 38, 7: 14, 8: 31, 15: 26, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 78: 98, 87: 94}

# مکان مار ها در بازی
snakes = {16: 6, 46: 25, 49: 11, 62: 19, 64: 60, 74: 53, 89: 68, 92: 88, 95: 75, 99: 80}

def roll_dice():
    """تاس را پرتاب کرده و نتیجه را برمی‌گرداند"""
    return random.randint(1, 6)

def move_player(player, spaces):
    """با توجه به فاصله مشخص شده، بازیکن را به موقعیت جدید منتقل می‌کند"""
    player += spaces
    if player > end_position:
        player = end_position - (player - end_position)
    if player in snakes:
        player = snakes[player]
        print("Oops! You hit a snake! You're now at position", player)
    elif player in ladders:
        player = ladders[player]
        print("Yay! You found a ladder! You're now at position", player)
    else:
        print("You're now at position", player)
    return player

# تاس نخستین برای شروع بازی
spaces = 0
while spaces != 6:
    input("Press Enter to roll the dice")
    spaces = roll_dice()
    if spaces == 6:
        print("You rolled a 6! Game started!")
        break
    else:
        print(f"You rolled a {spaces}. Roll again until you get a 6.")

# بازی شروع می‌شود
while True:
    input("Press Enter to roll the dice")
    spaces = roll_dice()
    player_position = move_player(player_position, spaces)
    if player_position == end_position:
        print("Congratulations! You Won!")
        break
    
