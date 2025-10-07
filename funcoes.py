from classes import *

def interagir_no_zoologico(animais):
    for animal in animais:
        print(animal.descrever())
        print("Som:", animal.emitir_som())

        if isinstance(animal, IVoador):
            print(animal.voar())

        if isinstance(animal, INadador):
            print(animal.nadar())

        print("-" * 40)
