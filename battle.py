from entities import hero, villian
from dodges import gadget

player1 = hero.Batman()
print(player1)
batarang = gadget.Batarang()
player1.equip(batarang)
print(player1)
player2 = villian.Darkside()
print(player2)

player2.attack(player1)
print(player1)
print(player2)
player1.attack(player2)
print(player2)


player1 = hero.Superman()
player2 = villian.Bane()
bane_venom = gadget.BaneVenom()
player2.equip(bane_venom)
print(player1)
print(player2)

for i in range(10):
    player2.attack(player1)
print(player1)
player1.attack(player2)
print(player2)
