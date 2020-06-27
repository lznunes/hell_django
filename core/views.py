from django.shortcuts import render, HttpResponse

# Create your views here.
def hello(request, nome, idade):
    return HttpResponse('<h1>Hello {} de {} anos</h1>'.format(nome, idade))

def soma(request, numero1, numero2):
    resultado = numero1 + numero2
    return HttpResponse('<h1>A soma de {} mais {} é igual {}</h1>'.format(numero1, numero2, resultado))

def subtracao(request, numero1, numero2):
    resultado = numero1 - numero2
    return HttpResponse('<h1>A subtração de {} menos {} é igual {}</h1>'.format(numero1, numero2, resultado))

def multplicacao(request, numero1, numero2):
    resultado = numero1 * numero2
    return HttpResponse('<h1>A multiplicação de {} vezes {} é igual {}</h1>'.format(numero1, numero2, resultado))

def divisao(request, numero1, numero2):
    resultado = numero1 / numero2
    return HttpResponse('<h1>A divisão de {} por {} é igual {}</h1>'.format(numero1, numero2, resultado))
