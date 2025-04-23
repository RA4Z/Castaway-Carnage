label surroundings_tronco_caido:
    "Enquanto você caminha aos seus arredores"
    "Você avista um tronco caído no chão"
    menu:
        "Como você irá agir?"
        "Aproximar-se":
            "Você se aproxima do tronco caído"
            "Ao chegar mais próximo você percebe que o mesmo está em estágios iniciais de decomposição"
            "É possível ver cogumelos vermelhos e marrons nesse tronco"
            menu:
                "O que fazer a seguir?"
                "Pegar os cogumelos marrons":
                    $ player.add_item('Brown Mushroom', 3)
                    $ player.change_needs(sanity=-0.5)
                
                "Pegar os cogumelos vermelhos":
                    $ player.add_item('Red Mushroom', 2)
                    $ player.change_needs(sanity=-0.5)
                
                "Pegar todos os cogumelos":
                    $ player.add_item('Brown Mushroom', 3)
                    $ player.add_item('Red Mushroom', 2)
                    $ player.change_needs(sanity=-1)
                
                "Não pegar nada e afastar-se":
                    "Você decide não arriscar e se afasta do tronco"
                
        "Afastar-se":
            "Você se afasta do tronco tentando evitar possíveis problemas"
    "Você retornou ao acampamento"
    return