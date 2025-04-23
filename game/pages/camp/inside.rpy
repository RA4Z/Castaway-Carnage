label camp_inside:
    "Você entra no acampamento cambaleando desajeitadamente"
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
                "Você sai de frente de sua cama"
                $ bedroom_visible = False

            "Descansar brevemente":
                if player.needs['sleep'] == 100:
                    "Você não sente necessidade de descansar no momento!"
                else:
                    "Você fez um breve descanso"
                    $ player.change_needs(hunger=-4, thirst=-7.5, sleep=+10)
                    $ world_state.advance_time(hours=1)


            "Dormir":
                if player.needs['sleep'] > 80:
                    "Você não se sente cansado o suficiente para dormir!"
                else:
                    $ player.change_needs(hunger=-20, thirst=-30, sleep=+45, sanity=+10)
                    $ world_state.advance_time(hours=4)
                    "Você dormiu e recuperou suas energias!"
