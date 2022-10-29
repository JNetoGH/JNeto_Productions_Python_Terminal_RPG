from char_and_squad.battle_entities import Character, Squad

squad1 = Squad("player squad", [Character("Joao", 10, 5, 5, 5, 10), Character("Dani", 10, 5, 5, 5, 10), Character("Lulu", 0, 5, 5, 5, 10)])
squad2 = Squad("enemy squad", [Character("Monstrinho", 10, 5, 5, 5, 10), Character("Lobao", 10, 5, 5, 5, 10)])

print(squad1.to_string())
print()
print()
print(squad2.to_string())


