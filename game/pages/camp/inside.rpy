label camp_inside:
    "Você entra no acampamento cambaleando desajeitadamente"
    menu:
        "Você está dentro de seu abrigo"
        "Sair do abrigo":
            jump camp_outside
        
        "Ir para a cama":
            jump camp_inside_sleep

label camp_inside_sleep:
    menu:
        "Você está de frente para sua cama"
        "Sair":
            jump camp_inside

        "Dormir":
            "Você dormiu"

    jump camp_inside_sleep
