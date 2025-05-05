from converte import Converte


class Main:
    lista = []
    conversao = int(input("Digite: "))
    dado = Converte(conversao)
    dado.converte_binario_decimal()


if __name__ == "__main__":
    main = Main()
