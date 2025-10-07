from classes import *

def interagir_no_zoologico(animais):
    for animal in animais:
        print(animal.descrever())
        print("Som:", animal.emitir_som())

