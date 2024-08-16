








class Battlefild():
     def __init__(self):
          self.selected_enemy_id = ''
          self.char_and_enemies_in_battle = {}
          self.current_battle_enemies = []

          #ovim indexom cu ici po listi battle_after_speed_check i na taj nacin odradjivati stvari
          self.index = 0

          self.battle_before_speed_check = []
          self.battle_after_speed_check = []

     def speed_check(self) -> None:
        print(self.battle_before_speed_check)
        check = sorted(self.battle_before_speed_check, key=lambda char: char.speed, reverse=True)
        for i in check:
            print(i)
            self.battle_after_speed_check.append(i)

     def dmg_calculation(self):
         for object in self.battle_after_speed_check:
              pass
             
     
     
          