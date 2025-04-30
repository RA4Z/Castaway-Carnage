image image_camp_inside = "images/camp_inside.png"

label camp_inside:
    $ show_only_image("image_camp_inside")
    if player.needs['sleep'] < 10:
        "Você entra no acampamento cambaleando desajeitadamente"
        $ player.change_needs(sanity=-0.1)
    else:
        "Você entra no acampamento"
    while True:
        menu:
            "Você está dentro de seu abrigo"
            "Sair do abrigo":
                jump camp_outside
            
            "Ir para a cama":
                call camp_inside_sleep

label camp_inside_sleep:
    $ bedroom_visible = True
    while bedroom_visible:
        menu:
            "Você está de frente para sua cama"
            "Sair":
                "Você saiu da frente de sua cama"
                $ bedroom_visible = False

            "Descansar brevemente":
                if player.needs['sleep'] == 100:
                    "Você não sente necessidade de descansar no momento!"
                else:
                    "Você fez um breve descanso"
                    $ player.change_needs(*action_costs_player.return_action_cost("short_rest"))
                    $ world_state.advance_time(hours=1)


            "Dormir":
                if player.needs['sleep'] > 80:
                    "Você não se sente cansado o suficiente para dormir!"
                else:
                    $ player.change_needs(*action_costs_player.return_action_cost("long_rest"))
                    $ world_state.advance_time(hours=4)
                    "Você dormiu e recuperou suas energias!"
