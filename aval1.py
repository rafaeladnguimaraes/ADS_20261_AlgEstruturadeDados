# -- VEÍCULO
class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.prox = None

    def __str__(self):
        txt = f"-- Veículo --\nMarca: {self.marca}; Modelo: {self.modelo}"
        return txt
    
    def imp_v(self):
        print( self )

# -- CARRO
class Carro(Veiculo):
    def __init__(self, marca, modelo, portas):
        super().__init__(marca, modelo)
        self._portas = portas 
    
    @property
    def port(self):
        return self._portas

    def __str__(self):
        txt = f"-- Carro --\nMarca: {self.marca}; Modelo: {self.modelo}; Quantidade de portas: {self._portas}"
        return txt
    
    def imp_c(self):
        print( self )

# -- DRONE
class Drone(Veiculo):
    def __init__(self, marca, modelo, qtd_helices):
        super().__init__(marca, modelo)
        self.__qtd_helices = qtd_helices
    
    @property
    def qtd_h(self):
        return self.__qtd_helices

    def __str__(self):
        txt = f"-- Drone --\nMarca: {self.marca}; Modelo: {self.modelo}; Quantidade de hélices: {self.__qtd_helices}"
        return txt
    
    def imp_d(self):
        print( self )

# -- PILHA -> Carro
class Pilha_C:

    def __init__(self):
        self.topo = None

    def add_c(self, carro):
        if self.topo is not None: 
            carro.prox = self.topo
        self.topo = carro
        self.impr_c()

    def rmv_c(self):
        if self.topo is not None:
            self.topo = self.topo.prox
        self.impr_c()

    def impr_c(self):
        print("--------------------")
        if self.topo is None:
            print("\nNão há carros na pilha")
        else:
            print("\n--Pilha de carrinhos Hothweels--")
            aux = self.topo
            cont = 1
            while aux:
                print( cont, aux )
                aux = aux.prox
                cont += 1
        print("--------------------")


# -- PILHA -> Drone

class Pilha_D:

    def __init__(self):
        self.topo = None

    def add_d(self, drone):
        if self.topo is not None: 
            drone.prox = self.topo
        self.topo = drone
        self.impr_d()

    def rmv_d(self):
        if self.topo is not None:
            self.topo = self.topo.prox
        self.impr_d()

    def impr_d(self):
        print("--------------------")
        if self.topo is None:
            print("\nNão há drones na pilha")
        else:
            print("\n--Pilha de drones radicais--")
            aux = self.topo
            cont = 1
            while aux:
                print( cont, aux )
                aux = aux.prox
                cont += 1
        print("--------------------")

# -- MENU

pilha_c = Pilha_C()
pilha_d = Pilha_D()


def menu():
    print(" ---- Arrumando pilhas ----- ")
    print("| 1) Adicionar carro        |")
    print("| 2) Adicionar drone        |")
    print("| 3) Remover carro          |")
    print("| 4) Remover drone          |")
    print("| 5) Ver pilha de carros    |")
    print("| 6) Ver pilha de drones    |")
    print("| 0) Sair                   |")
    print(" --------------------------- ")

op = -1
while op != 0:
    menu()
    op = int( input("O que quer fazer?") )
    if op == 1:
        mar = input("Qual a marca do carro? ")
        mod = input("Qual o modelo? ")
        port = input("Quantas portas tem? ")
        n_carro = Carro(mar, mod, port)
        pilha_c.add_c(n_carro)
    if op == 2:
        mar = input("Qual a marca do drone? ")
        mod = input("Qual modelo? ")
        qtd_h = input("Quantas hélices tem? ")
        n_drone = Drone(mar, mod, qtd_h)
        pilha_d.add_d(n_drone)
    if op == 3:
        pilha_c.rmv_c()
    if op == 4:
        pilha_d.rmv_d()
    if op == 5:
        pilha_c.impr_c()
    if op == 6:
        pilha_d.impr_d()
    if op < 0 or op > 6:
        print( "Opção inválida!")
    if op == 0:
        print( "Até a próxima!!")