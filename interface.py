from random import randint

from Hunter_Summons_warlock import Warlock
from Rogue_Paladin import Rogue, Paladin
from Shaman_Druid_Priest import Druid, Priest
from Warrior_Mage import Warrior, Mage

from Pvp_all import Pvp_all

words = {
    1: "Да будет Бой! Что же у нас по героям?",
    2: "Выбирайте персонажей на величайшую битву!",
    3: 'Ну, да начнется бой!',
    4: 'Это будет схваткой тысячелетия!'
}
units = {
    1: Warrior,
    2: Mage,
    3: Rogue,
    4: Paladin,
    # 5: Hunter,
    6: Warlock,
    # 7: Shaman,
    8: Druid,
    9: Priest

}
choice_end = True
while choice_end:
    print("Приветствую тебя, странник! Если желаешь сыграть в пвп, жми 1, если против мобов - 2.")
    choice1 = int(input())
    if choice1 == 1:
        print(words[randint(1, 4)])
        Pvp_all(list(map(int, input('Введите количество человек в каждой команде: ').split())))
    elif choice1 == 2:
        pass
    else:
        print('Incorrect choice')
    if int(input('if you want to close\end press 0: ')) == 0:
        choice_end = False
print('Bye!')
