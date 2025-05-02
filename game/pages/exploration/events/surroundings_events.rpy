label surroundings_event_lake:
    "Enquanto você força passagem pela vegetação densa, um som se destaca do zumbido constante da mata..."
    "Água. O som inconfundível de água corrente, não muito longe."
    player.name "Finalmente! Preciso achar... Com cuidado."
    "Você segue o som, o coração acelerando com uma mistura de esperança e cautela. O terreno desce ligeiramente, tornando-se mais úmido sob seus pés."
    "E então, você o vê. Um pequeno riacho serpenteia por entre rochas lisas e raízes expostas."
    "A água não é cristalina – tem um tom levemente amarronzado, com folhas e pequenas partículas flutuando na correnteza lenta – mas está se movendo."
    if world_state.daytime == 'Day':
        "A luz do sol filtra pelas folhas, criando reflexos dançantes na superfície da água. Apesar da turbidez, parece... vivo."
    else:
        "Ao luar, a água parece um fio de obsidiana líquida, o som do seu fluxo mais pronunciado no silêncio noturno. É difícil julgar sua clareza na penumbra."
    player.name "Água... Tanta água. Não parece perfeita, mas é melhor que nada. Muito melhor que nada."

    menu:
        "O que fazer?"
        "Beber Água":
            "Você bebe água."
            $ player.change_needs(thirst=+25, sanity=-3)
        "Armazenar Água":
            "Você guarda um pouco de água."
            $ player.add_item("River Water", 1)
        "Ignorar":
            "Você ignora essa lagoa."

    "Você marca mentalmente a localização deste riacho. É um recurso vital demais para perder de vista."
    $ camp.add_fast_travel("surroundings_lake")
    $ renpy.notify(f"Viagem rápida para a Lagoa desbloqueada com sucesso!")
    $ world_situation.remove_event("surrounding_events", "surroundings_event_lake")
    jump surroundings_return

label surroundings_event_roots:
    "A busca continua. O chão da floresta é um emaranhado de folhas úmidas, galhos caídos e raízes expostas que parecem garras tentando prender seus pés."
    "Seus olhos varrem o solo, procurando por qualquer coisa que se destaque, qualquer sinal de sustento."
    "Ali. Perto da base de uma árvore de casca grossa e escura, o solo parece ligeiramente remexido, e algumas pontas pálidas e finas se projetam timidamente."
    player.name "Isso... poderiam ser raízes comestíveis? Ou só mais madeira enterrada?"
    "Você se ajoelha, a umidade do chão penetrando em suas roupas. Com as mãos, começa a cavar cuidadosamente ao redor das pontas."
    "Elas cedem com alguma resistência. São raízes, de fato. Longas, nodosas, de uma cor pálida quase doentia e cobertas por uma fina camada de terra escura."
    menu:
        "O que fazer?"
        "Pegar Raízes":
            "Ao puxar uma delas completamente, você nota como é dura e fibrosa ao toque. Não parece particularmente apetitosa."
            player.name "Não é muito... e não parece fácil de comer. Mas é algo. Em um lugar como este, 'algo' pode ser a diferença."
            "Você junta um pequeno feixe dessas raízes, limpando o excesso de terra da melhor forma possível."
            $ player.add_item("Fibrous Roots", random.randint(1, 3))
        "Ignorar":
            "Você ignora completamente a existência dessas raízes"

    jump surroundings_return

label surroundings_event_bugs:
    "Seus olhos continuam varrendo o ambiente em busca de qualquer coisa que possa ser útil. Um tronco caído, coberto por um tapete espesso de musgo verde-escuro e salpicado de fungos pálidos, chama sua atenção."
    "A madeira parece macia, úmida, claramente em avançado estado de decomposição."
    player.name "Um lugar assim... talvez esconda algo? Cogumelos... ou... vida."
    "Com certa relutância em tocar na madeira podre, você usa um galho próximo para levantar um pedaço solto da casca."
    "O que está por baixo se revela em uma explosão de movimento frenético. Um formigueiro de vida fervilha na terra escura e úmida: larvas brancas e gordas se contorcendo, besouros de carapaça escura fugindo da luz repentina, centopeias ágeis desaparecendo em fendas."
    "Um cheiro forte de terra molhada e madeira em decomposição sobe do local perturbado."
    player.name "Argh... Tanta... agitação. Instintivamente, recuo um passo."
    "A visão é instintivamente repulsiva. Uma parte primitiva do seu cérebro grita 'errado', 'sujo', 'perigo'."
    "No entanto, uma outra parte, a pragmática, a que luta para sobreviver neste lugar, não pode deixar de registrar: aquilo é proteína. Energia ambulante."
    player.name "Comida... Tecnicamente. Poderia ser uma opção... se as coisas ficarem realmente ruins."
    menu:
        "O que fazer?"
        "Pegar Insetos":
            "Apesar do nojo inicial, você percebe que seria fácil coletar um punhado dessas criaturas antes que se dispersem completamente."
            $ player.add_item("Bugs", random.randint(3, 5))
        "Ignorar":
            "Você sente ânsias ao se imaginar comendo essas critaturas e abandona a ideia"

    jump surroundings_return

# Ponto de retorno para todos os eventos aleatórios das redondezas
label surroundings_return:
    if player.needs['sleep'] == 0:
        call camp_outside_faint
    menu:
        "Você terminou a exploração na região atual"
        "Retornar ao Acampamento":
            "Você retorna ao acampamento"
            return

        "Continuar Explorando":
            $ world_state.advance_time(minutes=30)
            $ player.change_needs(*action_costs_player.return_action_cost("surroundings_events_from_exploration"))
            $ random_event = random.choice(world_situation.surrounding_events)
            $ renpy.jump(random_event)
