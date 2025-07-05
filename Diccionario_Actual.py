meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "XD": "Otra respuesta a algo gracioso o random",
            "BRO": "Forma de llamar a un amigo o un compañero",
            "RANDOM": "Una manera de decir algo aleatorio o raro"
            }

saludo = print("Bienvenido/a, estas aqui paera buscar una palabra que no entiendas, agradezco que estas aqui en vez de usar solo Google. Aqui podras preguntar unas palabras, solo 5 por ahora.")

# Bucle de los bucles de JH
for i in range(5):
    word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")
    if word in meme_dict.keys():
        # ¿Qué debemos hacer si se encuentra la palabra?
        print(meme_dict[word])
    else:
        # ¿Qué hacer si no se encuentra la palabra?
        print("Bro, esa palabra no esta en este diccionario (o al menos no la escribiste bien); para algo está gulugulu")
