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

            "Dormir":
                if player.needs['sleep'] > 80:
                    "Você não se sente cansado o suficiente para dormir!"
                else:
                    $ player.change_needs(sleep=+50)
                    "Você dormiu e recuperou suas energias!"
