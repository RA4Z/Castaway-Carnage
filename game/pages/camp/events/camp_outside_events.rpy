label camp_outside_random_events:
    "Ao andar no lado de fora do seu acampamento você percebe algo fora do comum"

label camp_outside_faint:
    "Você se sente esgotado"
    "Todas as suas energias se foram"
    "Você então dá uma piscada mais longa, ao abrir os olhos percebe que está deitado no chão"
    "Sem perceber você desmaiou enquanto caminhava para o acampamento"
    $ player.change_needs(hunger=-6, thirst=-10, sleep=+15)
    $ world_state.advance_time(hours=2)
    return