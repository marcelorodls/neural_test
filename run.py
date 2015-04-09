__author__ = 'bernardo'
import cv2
import cPickle
import json

class sinapse:
    next = None
    back = None
    peso = 0
    t_epoch = 0

class neuronio:
    sinap = []
    result = None
    received = 0
    t_epoch = 0
    bias = 1

epoch = 0
iteracoes = 0
entrada = []
meio = []
saida = []

def save_obj(obj, name):
    with open( str(name) + '.txt', 'wb') as f:
        cPickle.dump(obj, f, cPickle.HIGHEST_PROTOCOL)


def load_obj(name):
    with open( str(name) + '.txt', 'rb') as f:
        return cPickle.load(f)

def prepare():

    entrada = [neuronio(), neuronio()]
    for x in xrange(0,100):
        meio.append(neuronio())

    for x in xrange(0,100):
        novo = neuronio()
        novo.result = x
        saida.append(novo)

    for x in xrange(0, len(entrada)):
        for y in xrange(0, len(meio)):
            nova = sinapse()
            nova.back = entrada[x]
            nova.next = meio[y]
            nova.peso = 0.1
            entrada[x].sinap.append(nova)

    for x in xrange(0, len(meio)):
        for y in xrange(0, len(saida)):
            nova = sinapse()
            nova.back = meio[x]
            nova.next = saida[y]
            nova.peso = 0.1
            meio[x].sinap.append(nova)

    save_obj(saida, "saida")
    save_obj(meio, "meio")
    save_obj(entrada, "entrada")
    save_obj(iteracoes, "iteracoes")

def main():
    global epoch
    input = raw_input("qual? ")
    neuronios = [entrada, meio, saida]

    for y in entrada:
        for x in entrada.sinap:
            x.next.received += x.peso







prepare()
main()

