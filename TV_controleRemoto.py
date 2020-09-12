"""
    Criar uma classe TV com classes compostas para controle de Volume e Canal

    Ex:
    #teste de volume
    >>> volume = Volume()
    >>> volume.mostrar
    0
    >>> volume.aumentar()
    >>> volume.mostrar
    1
    >>> volume.aumentar()
    >>> volume.mostrar
    2
    >>> volume.aumentar()
    >>> volume.mostrar
    3
    >>> volume.diminuir()
    >>> volume.mostrar
    1
    >>> volume.diminuir()
    >>> volume.mostrar
    0

    # teste mudar canal
    >>> canal = Canal()
    >>> canal.mostrar
    'Globo'
    >>> canal.mudar()
    >>> canal.mostrar
    'SBT'
    >>> canal.mudar()
    >>> canal.mostrar
    'Band'

    # testando TV
    >>> tv = TV(volume, canal)
    >>> tv.mostrar_canal()
    'Band'
    >>> tv.mudar_canal()
    >>> tv.mostrar_canal()
    'Globo'
    >>> tv.mostrar_volume()
    0
    >>> tv.aumentar_volume()
    >>> tv.mostrar_volume()
    1
    >>> tv.aumentar_volume()
    >>> tv.mostrar_volume()
    2
    >>> tv.diminuir_volume()
    >>> tv.mostrar_volume()
    0
"""

GLOBO = 'Globo'
SBT = 'SBT'
BAND = 'Band'


class Volume:
    #_mostrar = 0

    def __init__(self):
        self.mostrar = 0

    def aumentar(self):
        self.mostrar += 1

    def diminuir(self):
        if self.mostrar > 1:
            self.mostrar -= 2
        else:
            self.mostrar -= 1


class Canal:
    _canais = {GLOBO: SBT, SBT: BAND, BAND: GLOBO}

    def __init__(self):
        self.mostrar = GLOBO

    def mudar(self):
        self.mostrar = self._canais[self.mostrar]


class TV:
    def __init__(self, volume, canal):
        super()
        self.volume = volume
        self.canal = canal

    def mostrar_canal(self):
        return self.canal.mostrar

    def mudar_canal(self):
        self.canal.mudar()

    def mostrar_volume(self):
        return self.volume.mostrar

    def aumentar_volume(self):
        self.volume.aumentar()

    def diminuir_volume(self):
        self.volume.diminuir()
