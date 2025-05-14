label surroundings_event_day_mushroom:
    "Seus olhos são atraídos para um ponto de cor vibrante rompendo a monotonia verde e marrom do chão da floresta."
    "É um cogumelo, diferente de todos que você já viu. Seu chapéu tem um tom de roxo profundo, quase luminoso, com manchas irregulares de um amarelo doentio que parecem... pulsar levemente sob a luz filtrada."
    player.name "Que cores... É lindo, de uma forma perturbadora. Mas parece gritar 'perigo'. Ou... talvez seja especial?"
    "Ele cresce solitário, emanando um odor adocicado, quase enjoativo, que se mistura ao cheiro de terra úmida. Não há outros cogumelos parecidos por perto."
    "Uma parte de você sente uma forte curiosidade misturada com apreensão. Seria comestível? Teria algum efeito estranho?"
    player.name "Arriscar? A fome não está tão desesperadora ainda... mas se for algo bom? Ou algo... alucinógeno? Pode ser útil? Ou fatal?"
    menu:
        "O que fazer?"
        "Pegar Cogumelo":
            $ player.add_item("Suspect Mushroom", 1)
            "Você pondera por um momento antes de decidir colher cuidadosamente o cogumelo de aparência bizarra, sua haste liberando um líquido leitoso e espesso."

        "Ignorar":
            "Você deixa o medo tomar conta e ignora a existência do cogumelo"
            
    jump surroundings_return


label surroundings_event_day_rotten_fruits:
    "Você avista outro arbusto com frutas, semelhante aos que já encontrou antes, mas algo está diferente."
    "As frutas neste arbusto têm uma cor mais pálida, quase translúcida, como se a cor tivesse sido drenada delas. A pele parece fina e tem uma textura estranhamente oleosa ao toque."
    player.name "São parecidas com as outras... mas ao mesmo tempo, tão diferentes. Estão doentes? Ou são apenas... outra coisa?"
    "Elas não têm o mesmo aroma adocicado das frutas comuns, emitindo um cheiro fraco, quase metálico."
    player.name "Comida é comida... certo? Mas meu instinto está gritando que há algo errado aqui."
    menu:
        "O que fazer?"
        "Pegar Cogumelo":
            $ player.add_item("Rotten Fruit", random.randint(4, 6))
            "Hesitante, você colhe algumas. Elas parecem estranhamente pesadas e frias em sua mão."

        "Ignorar":
            "Com nojo, você ignora essas frutas"
            
    jump surroundings_return


label surroundings_event_day_branch_breaking:
    "Um galho estala alto, muito perto, logo atrás de você. Você se vira num sobressalto, o coração disparado."
    "Não há nada ali. Nada que você possa ver. Apenas as árvores imóveis e o silêncio que se segue ao som."
    player.name "O vento? Um animal pequeno? Ou...?"
    "A incerteza deixa um gosto amargo na boca."
    "A tensão drena um pouco da sua compostura."
    $ player.change_needs(*action_costs_player.return_action_cost("surroundings_event_day_branch_breaking"))
    jump surroundings_return


label surroundings_event_day_complete_silence:
    "De repente, você percebe. O fundo constante de sons da floresta – o zumbido dos insetos, o farfalhar das folhas, o canto distante de um pássaro – desapareceu completamente."
    "Um silêncio absoluto toma conta, tão pesado que parece pressionar seus tímpanos. Não é paz, é ausência. Uma sensação de que o próprio mundo prendeu a respiração."
    "Dura apenas alguns segundos, talvez dez, mas o tempo parece se esticar de forma nauseante nesse vácuo sonoro."
    player.name "Isso não é normal... O que aconteceu? Onde foram todos os sons?"
    "Quando os ruídos da mata retornam gradualmente, eles soam estranhamente artificiais por um momento, e a sensação de que algo fundamental está errado permanece com você."
    $ player.change_needs(*action_costs_player.return_action_cost("surroundings_event_day_complete_silence"))


label surroundings_event_day_goodbird:
    "Em meio à quietude tensa da mata, um som inesperado e claro rompe o silêncio. É o canto de um pássaro, uma melodia complexa e vibrante, cheia de trinados e chamados alegres."
    "Você para instintivamente para ouvir. É um som tão normal, tão cheio de vida... quase esquecido neste lugar."
    player.name "Que som bonito... Por um instante, quase parece que estou em outro lugar, em outro tempo."
    "A melodia simples lava um pouco da tensão acumulada em seus ombros."
    "Um breve momento de serenidade."
    $ player.change_needs(*action_costs_player.return_action_cost("surroundings_event_day_goodbird"))


label surroundings_event_day_butterfly:
    "Sentado em um tronco caído para recuperar o fôlego por um instante, algo pequeno e colorido pousa delicadamente em sua mão estendida."
    "É uma borboleta. Suas asas são de um azul e preto iridescente, quase metálico, e pulsam suavemente. Ela permanece ali por vários segundos, imóvel, quase como se reconhecesse sua presença."
    player.name "Inacreditável... Tão frágil, mas tão viva. Voando livremente..."
    "O pequeno momento de conexão inesperada com outra criatura viva, um momento de confiança mútua e beleza natural, aquece algo dentro de você que você pensou ter congelado."
    "Uma faísca de calor em meio ao frio."
    $ player.change_needs(*action_costs_player.return_action_cost("surroundings_event_day_butterfly"))

