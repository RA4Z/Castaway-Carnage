label exploration_surroundings:
    "Você começou a se preparar para explorar os arredores de seu acampamento"
    while True:
        menu:
            "O que fazer a seguir?"
            "Iniciar Exploração":
                $ world_state.advance_time(minutes=30)
                $ player.change_needs(hunger=-2, thirst=-4, sleep=-5)
                call surroundings_tronco_caido

            "Cancelar a Exploração":
                "Você desistiu da ideia de explorar e permaneceu no acampamento"
                return