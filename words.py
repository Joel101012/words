meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "CREEPY": "Algo aterrador i que provoca escalofrios",
            "XD": "Una forma de expressar que te estas riendo de algo gracioso",
            }
            
word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")


if word in meme_dict.keys():
    print(meme_dict[word])
else:
    print("Esa palabra no se encuentra en el diccionario")
