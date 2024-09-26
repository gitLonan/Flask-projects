



class CombatText():
    message = []
    @staticmethod
    def get_combat_text(*args, decider='', character=None, enemy=None, hero_dmg=None, enemy_dmg=None, hero_spell=None, enemy_spell=None):
        if decider == "hero":
            CombatText.message.append([f"{character.name} dealt {hero_dmg} to {enemy.name}", decider])
        elif decider == "enemy":
            CombatText.message.append([f"{enemy.name} dealt {enemy_dmg} to Hero", decider])
        elif decider == "enemy-dead":
            CombatText.message.append([f"{character.name} killed {enemy.name}", decider])
        elif decider == "lvl-up":
            #print('ovo gledam', args[0])
            CombatText.message.append([f"{character.name} leveld up and got heald by {args[0]}", decider])
