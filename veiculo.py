from modelo import Modelo

class Veiculo:
    def __init__(
            self,
            modelo = Modelo(),
            placa = "NAO_ESPECIFICADO",
            quilometragem = 0
            ):
        
        # declarações
    
        self.modelo = Modelo()
        self.placa = "NAO_ESPECIFICADO"
        self.quilometragem = 0

        #
        
        self.set_modelo(modelo)
        self.set_placa(placa)
        self.set_quilometragem(quilometragem)

    # metodos set

    def set_modelo(self, modelo):
        self.modelo = modelo

    def set_placa(self, placa):
        self.placa = placa

    def set_quilometragem(self, quilometragem):
        self.quilometragem = quilometragem

    # metodos get

    def get_modelo(self):
        return self.modelo
    
    def get_placa(self):
        return self.placa
    
    def get_quilometragem(self):
        return self.quilometragem