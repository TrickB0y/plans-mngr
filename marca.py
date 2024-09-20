class Marca:
    def __init__(
            self,
            nome = "NAO_ESPECIFICADO"
            ):
        
        # declarações

        self.nome = "NAO_ESPECIFICADO"

        #

        self.set_nome(nome)

    # metodos set

    def set_nome(self,nome):
        self.nome = nome

    # metodos get

    def get_nome(self):
        return self.nome
