label exploration_distant:
    "Você começou a se preparar para explorar regiões mais distantes de seu acampamento"
    menu:
        "O que fazer a seguir?"
        "Iniciar Exploração":
            $ world_state.advance_time(minutes=90)
            $ player.change_needs(hunger=-6, thirst=-12, sleep=-15)
            ""

        "Desistir da Exploração":
            "Você desistiu da ideia de explorar e permaneceu no acampamento"
            return