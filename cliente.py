class Cliente:
    def __init__(
            self,
            nome = "NAO_ESPECIFICADO",
            cpf = "NAO_ESPECIFICADO"
            ):
        
        # declarações

        self.nome = "NAO_ESPECIFICADO"
        self.cpf = "NAO_ESPECIFICADO"

        #
        
        self.set_nome(nome)
        self.set_cpf(cpf)

    # metodos set

    def set_nome(self, nome):
        self.nome = nome

    def set_cpf(self, cpf):
        self.cpf = cpf
    
    # metodos get
    
    def get_nome(self):
        return self.nome
    
    def get_cpf(self):
        return self.cpf