python early:
    class Player:
        """
        Representa o personagem do jogador com seus atributos básicos.
        """
        def __init__(self, name="Protagonista"):
            self.name = name
            self.hp = 100
            self.stats = {
                "strength": 5
            }
            self.needs = {
                # Necessidades básicas do jogo
                "hunger": 100,
                "thirst": 100,
                "sleep": 100,
                "sanity": 100,
            }
            self.experience_points = {
                # Quantidade de pontos de experiência atual e para o próximo nível
                "strength_next_level": (self.stats["strength"] + 1) * 10,
                "strength_xp": 0,
            }
            self.inventory = [] # Lista para guardar itens (nomes como strings, por exemplo)

        def change_needs(self, hunger=0, thirst=0, sleep=0, sanity=0):
            self.needs['hunger'] += hunger
            self.needs['thirst'] += thirst
            self.needs['sleep'] += sleep
            self.needs['sanity'] += sanity

            # Limit needs to 100
            self.needs['hunger'] = min(self.needs['hunger'], 100)
            self.needs['thirst'] = min(self.needs['thirst'], 100)
            self.needs['sleep'] = min(self.needs['sleep'], 100)
            self.needs['sanity'] = min(self.needs['sanity'], 100)

        def change_hp(self, amount):
            max_hp = self.stats["strength"] * 5
            self.hp += amount
            if self.hp < 0:
                self.hp = 0
            elif self.hp > max_hp:
                self.hp = max_hp
            # Você pode adicionar lógica aqui para verificar se o jogador morreu (hp <= 0)

        def add_item(self, item_name, qty):
            found_item = False
            for item in self.inventory:
                if item['name'] == item_name: # Check if the item is present
                    item['qty'] += qty
                    found_item = True
                    renpy.notify(f"{qty} {item_name} adicionado com sucesso ao inventário!") # Feedback visual opcional
                    renpy.pause(1.5)  # Wait for 0.5 seconds
                    break # Stop searching once the item is found
            if not found_item:
                self.inventory.append({'name': item_name, 'qty': qty})
                renpy.notify(f"{qty} {item_name} adicionado com sucesso ao inventário!") # Feedback visual opcional
                renpy.pause(1.5)  # Wait for 0.5 seconds

        def remove_item(self, item_name, qty):
            """Remove um item do inventário."""
            for item in self.inventory:
                if item['name'] == item_name: # Check if the item is present
                    if item['qty'] >= qty:
                        renpy.notify(f"{qty} {item_name} Removido do inventário!")
                        return True
                    else:
                        renpy.notify(f"Você não possui {item_name} o suficiente!")
                        return False

            renpy.notify(f"Você não possui nenhum {item_name} no inventário!")
            return False
                    
        def has_item(self, item_name, qty):
            for item in self.inventory:
                if item['name'] == item_name:
                    if item['qty'] >= qty:
                        return True
            return False

        # Regra para adicionar pontos de experiência, fazer a verificação e subir o nível da respectiva habilidade
        def lvl_up_skills(self, skill, xp):
            self.experience_points[f"{skill}_xp"] += xp
            if self.experience_points[f"{skill}_xp"] >= self.experience_points[f"{skill}_next_level"]:
                self.experience_points[f"{skill}_xp"] = self.experience_points[f"{skill}_xp"] - self.experience_points[f"{skill}_next_level"]
                self.stats[skill] += 1
                self.experience_points[f"{skill}_next_level"] = (self.stats[skill] + 1) * 10

        # Método opcional para facilitar a visualização (debug)
        def __str__(self):
            return f"Player(Nome: {self.name}, HP: {self.hp}/{self.max_hp}, Inventário: {self.inventory})"