python early:
    class Player:
        """
        Representa o personagem do jogador com seus atributos básicos.
        """
        def __init__(self, name="Protagonista", hp=100, max_hp=100, gold=0):
            """
            Inicializa um novo jogador.
            Args:
                name (str): O nome inicial do jogador.
                hp (int): Pontos de vida atuais.
                max_hp (int): Pontos de vida máximos.
                gold (int): Quantidade inicial de ouro/dinheiro.
            """
            self.name = name
            self.hp = hp
            self.max_hp = max_hp
            self.gold = gold
            self.inventory = [] # Lista para guardar itens (nomes como strings, por exemplo)
            # Adicione outros atributos que precisar: mana, força, inteligência, etc.
            # self.strength = 10
            # self.intelligence = 10

        def change_hp(self, amount):
            """
            Altera os pontos de vida do jogador.
            Garante que o HP não fique abaixo de 0 ou acima do max_hp.
            Args:
                amount (int): A quantidade a ser adicionada (positiva para curar, negativa para dano).
            """
            self.hp += amount
            if self.hp < 0:
                self.hp = 0
            elif self.hp > self.max_hp:
                self.hp = self.max_hp
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

        def change_gold(self, amount):
            """Altera a quantidade de ouro do jogador."""
            self.gold += amount
            if self.gold < 0:
                self.gold = 0 # Impede ouro negativo, a menos que seja intencional

        # Método opcional para facilitar a visualização (debug)
        def __str__(self):
            return f"Player(Nome: {self.name}, HP: {self.hp}/{self.max_hp}, Gold: {self.gold}, Inventário: {self.inventory})"