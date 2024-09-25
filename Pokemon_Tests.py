HypnoID = "0097"
HypnoSpecie = "Hypnosis Pokemon"
HypnoType = "Psychic"
AboutHypno = "Hypno is a Psychic type Pokémon introduced in Generation 1."
HypnoAB1 = "[Insomnia]"
HypnoAB2 = "[Forerwarn]"
HypnoAB3 = "[Inner Focus]"
HypnoExp = int(6404)
ExpUp = int(input("Select EXP UP number: "))
HypnoHP = int(280)
DamageTaken = int(input("Hypno damage took: "))
HypnoLvl = 40
soma = HypnoExp + ExpUp
damage = HypnoHP - DamageTaken
Confusion = 50
Heabutt = 70
Fire_Punch = 75
# blue are variants, red are strings, purple are
print("HYPNO")
print("About:", AboutHypno)
print("HP: ", HypnoHP)
print("Pokedex ID:", HypnoID)
print("Type:", HypnoType)
print("Pokemon specie:", HypnoSpecie)
print("Abilities:", HypnoAB1, HypnoAB2, HypnoAB3)
print("Hypno LVL:", HypnoLvl)
print("Exp gained: {} "
      "Hypno have exp:{} "
      "now: {}".format(ExpUp, HypnoExp, soma))
print("Hypno takes {} of damage".format(DamageTaken))
print("Hypno HP is: {}".format(damage))
