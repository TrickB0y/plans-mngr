from cliente import Cliente
from veiculo import Veiculo

import datetime

class Servico:
    def __init__(
            self, 
            cliente = Cliente(),
            veiculo = Veiculo(),
            data = datetime.datetime.now(),

            manutencao_relacao = False,
            manutencao_oleo = False,
            manutencao_filtro = False,
            manutencao_pneu = False,
            manutencao_scanner = False,
            manutencao_filtr_ar = False,
            manutencao_vela = False,
            manutencao_fluido_freio = False,
            manutencao_past_lona = False,
            manutencao_cx_dir = False,
            manutencao_carburador_bico = False,
            manutencao_arranque = False,

            manutencao_descricao = "NAO_ESPECIFICADO"

            ):

        # declarações
        self.cliente = Cliente()
        self.veiculo = Veiculo()
        self.data = datetime.datetime.now()
        
        self.manutencao_relacao = False
        self.manutencao_oleo = False
        self.manutencao_filtro = False
        self.manutencao_pneu = False
        self.manutencao_scanner = False
        self.manutencao_filtr_ar = False
        self.manutencao_vela = False
        self.manutencao_fluido_freio = False
        self.manutencao_past_lona = False
        self.manutencao_cx_dir = False
        self.manutencao_carburador_bico = False
        self.manutencao_arranque = False

        self.manutencao_descricao = "NAO_ESPECIFICADO"

        #
        
        self.set_cliente(cliente)
        self.set_veiculo(veiculo)
        self.set_data(data)

        self.set_manutencao_relacao(manutencao_relacao)
        self.set_manutencao_oleo(manutencao_oleo)
        self.set_manutencao_filtro(manutencao_filtro)
        self.set_manutencao_pneu(manutencao_pneu)
        self.set_manutencao_scanner(manutencao_scanner)
        self.set_manutencao_filtr_ar(manutencao_filtr_ar)
        self.set_manutencao_vela(manutencao_vela)
        self.set_manutencao_fluido_freio(manutencao_fluido_freio)
        self.set_manutencao_past_lona(manutencao_past_lona)
        self.set_manutencao_cx_dir(manutencao_cx_dir)
        self.set_manutencao_carburador_bico(manutencao_carburador_bico)
        self.set_manutencao_arranque(manutencao_arranque)

        self.set_manutencao_descricao(manutencao_descricao)


    # metodos set

    def set_cliente(self, cliente):
        self.cliente = cliente

    def set_veiculo(self, veiculo):
        self.veiculo = veiculo

    def set_data(self, data):
        self.data = data



    def set_manutencao_relacao(self, manutencao_relacao):
        self.manutencao_relacao = manutencao_relacao

    def set_manutencao_oleo(self, manutencao_oleo):
        self.manutencao_oleo = manutencao_oleo

    def set_manutencao_filtro(self, manutencao_filtro):
        self.manutencao_filtro = manutencao_filtro

    def set_manutencao_pneu(self, manutencao_pneu):
        self.manutencao_pneu = manutencao_pneu

    def set_manutencao_scanner(self, manutencao_scanner):
        self.manutencao_scanner = manutencao_scanner
    
    def set_manutencao_filtr_ar(self, manutencao_filtr_ar):
        self.manutencao_filtr_ar = manutencao_filtr_ar

    def set_manutencao_vela(self, manutencao_vela):
        self.manutencao_vela = manutencao_vela

    def set_manutencao_fluido_freio(self, manutencao_fluido_freio):
        self.manutencao_fluido_freio = manutencao_fluido_freio

    def set_manutencao_past_lona(self, manutencao_past_lona):
        self.manutencao_past_lona = manutencao_past_lona

    def set_manutencao_cx_dir(self, manutencao_cx_dir):
        self.manutencao_cx_dir = manutencao_cx_dir

    def set_manutencao_carburador_bico(self, manutencao_carburador_bico):
        self.manutencao_carburador_bico = manutencao_carburador_bico
    
    def set_manutencao_arranque(self, manutencao_arranque):
        self.manutencao_arranque = manutencao_arranque



    def set_manutencao_descricao(self, manutencao_descricao):
        self.manutencao_descricao = manutencao_descricao

    # metodos get

    def get_cliente(self):
        return self.cliente
    
    def get_veiculo(self):
        return self.veiculo
    
    def get_data(self):
        return self.data
    


    def get_manutencao_relacao(self):
        return self.manutencao_relacao

    def get_manutencao_oleo(self):
        return self.manutencao_oleo

    def get_manutencao_filtro(self):
        return self.manutencao_filtro

    def get_manutencao_pneu(self):
        return self.manutencao_pneu

    def get_manutencao_scanner(self):
        return self.manutencao_scanner
    
    def get_manutencao_filtr_ar(self):
        return self.manutencao_filtr_ar

    def get_manutencao_vela(self):
        return self.manutencao_vela

    def get_manutencao_fluido_freio(self):
        return self.manutencao_fluido_freio

    def get_manutencao_past_lona(self):
        return self.manutencao_past_lona

    def get_manutencao_cx_dir(self):
        return self.manutencao_cx_dir

    def get_manutencao_carburador_bico(self):
        return self.manutencao_carburador_bico
    
    def get_manutencao_arranque(self):
        return self.manutencao_arranque



    def get_manutencao_descricao(self):
        return self.manutencao_descricao
