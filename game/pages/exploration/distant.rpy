label exploration_distant:
    "Você começou a se preparar para explorar regiões mais distantes de seu acampamento"
    while True:
        if player.needs['sleep'] == 0:
            call camp_outside_faint
        menu:
            "O que fazer a seguir?"
            "Iniciar Exploração":
                $ world_state.advance_time(minutes=90)
                $ player.change_needs(*action_costs_player.return_action_cost("distant_events_from_camp"))
                $ random_event = random.choice(world_situation.distant_events)
                $ renpy.call(random_event)

            "Desistir da Exploração":
                "Você desistiu da ideia de explorar e permaneceu no acampamento"
                return