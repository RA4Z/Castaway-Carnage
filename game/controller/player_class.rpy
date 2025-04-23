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

        def add_item(self, item_name):
            """Adiciona um item ao inventário."""
            if item_name not in self.inventory: # Evita duplicatas se não quiser
                self.inventory.append(item_name)
                renpy.notify(f"Adicionado: {item_name}") # Feedback visual opcional
            else:
                renpy.notify(f"Você já tem {item_name}.") # Ou aumente a quantidade se usar um dicionário

        def remove_item(self, item_name):
            """Remove um item do inventário."""
            if item_name in self.inventory:
                self.inventory.remove(item_name)
                renpy.notify(f"Removido: {item_name}") # Feedback visual opcional
                return True # Indica sucesso
            else:
                # renpy.notify(f"Você não tem {item_name}.") # Opcional: avisar se não tem
                return False # Indica falha

        def has_item(self, item_name):
            """Verifica se o jogador possui um item específico."""
            return item_name in self.inventory

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