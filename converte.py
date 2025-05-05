class Converte:
    def __init__(self, valor):
        self.valor = valor
        self.lista = []

    def converte_binario_decimal(self):
        while self.valor != 0:
            if self.valor % 2 == 0:
                self.lista.append(0)
                self.valor = self.valor // 2
            else:
                self.lista.append(1)
                self.valor = self.valor // 2
        self.lista.reverse()
        resultado = "".join(str(x) for x in self.lista)
        print("(", resultado, ")", "2")

    def converte_decimal_binario(self):
        pass
