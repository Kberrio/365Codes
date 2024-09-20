class Spell:
    def __init__(self, name, mana_cost, effect):
        self.name = name
        self.mana_cost = mana_cost
        self.effect = effect

    def cast(self):
        return f"Casting {self.name}: {self.effect}"

class Mage:
    def __init__(self, name, mana):
        self.name = name
        self.mana = mana
        self.spells = {}

    def learn_spell(self, spell):
        self.spells[spell.name] = spell
        print(f"{self.name} learned {spell.name}!")

    def cast_spell(self, spell_name):
        if spell_name not in self.spells:
            return f"{self.name} doesn't know the spell {spell_name}."
        
        spell = self.spells[spell_name]
        if self.mana < spell.mana_cost:
            return f"{self.name} doesn't have enough mana to cast {spell_name}."
        
        self.mana -= spell.mana_cost
        return f"{self.name} {spell.cast()} (Mana left: {self.mana})"

# Create some spells
fireball = Spell("Fireball", 20, "Hurls a ball of fire at the target.")
ice_lance = Spell("Ice Lance", 15, "Shoots a lance of ice at the enemy.")
heal = Spell("Heal", 30, "Restores health to the caster or an ally.")

# Create a mage
merlin = Mage("Merlin", 100)

# Merlin learns spells
merlin.learn_spell(fireball)
merlin.learn_spell(ice_lance)
merlin.learn_spell(heal)

# Merlin casts some spells
print(merlin.cast_spell("Fireball"))
print(merlin.cast_spell("Ice Lance"))
print(merlin.cast_spell("Heal"))
print(merlin.cast_spell("Lightning Bolt"))  # Spell not learned
print(merlin.cast_spell("Fireball"))  # Not enough mana