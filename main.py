import math as m

# FUNÇÃO DO SEGUNDO GRAU (f(x) = ax²+bx+c)
def funcao_segundograu():
    ax2 = int(input("\nMe diga o valor de ax²: "))
    bx = int(input("Me diga o valor de bx: "))
    c = int(input("Me diga o valor de c: "))

    # Cálculo do Δ
    delta = (m.pow(bx,2)) - (4*ax2*c)
    print("\nValor do delta: {}".format(delta))
    if (delta<=0):
        print("A função não tem raizes reais!\n")
        return 0

    # Cálculo da função, -b +- √Δ / 2a
    resultado_positivo = (-bx + m.sqrt(delta)) / (2*ax2)
    resultado_negativo = (-bx - m.sqrt(delta)) / (2*ax2)
    print("\nRaiz positiva (x1): {}\nRaiz negativa (x2): {}".format(resultado_positivo, resultado_negativo))
    if (resultado_positivo == resultado_negativo):
        print("A função tem raizes iguais!\n")
    elif (resultado_negativo>=-1 and resultado_positivo>=1):
        print("A função tem raizes diferentes!\n")

funcao_segundograu()
