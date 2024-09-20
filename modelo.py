from marca import Marca

class Modelo:
    def __init__(
            self,
            marca = Marca(),
            nome = "NAO_ESPECIFICADO",
            ano = 0,
            versao = "NAO_ESPECIFICADO"
            ):
        
        # declarações

        self.marca = Marca()
        self.nome = "NAO_ESPECIFICADO"
        self.ano = 0
        self.versao = "NAO_ESPECIFICADO"

        #

        self.set_marca(marca)
        self.set_nome(nome)
        self.set_ano(ano)
        self.set_versao(versao)

    # metodos set

    def set_marca(self, marca):
        self.marca = marca

    def set_nome(self, nome):
        self.nome = nome

    def set_ano(self, ano):
        self.ano = ano

    def set_versao(self, versao):
        self.versao = versao

    # metodos get

    def get_marca(self):
        return self.marca

    def get_nome(self):
        return self.nome
    
    def get_ano(self):
        return self.ano
    
    def get_versao(self):
        return self.versao