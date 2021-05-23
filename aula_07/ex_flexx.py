from flexx import flx


class Exemplo(flx.Widget):

    def init(self):
        flx.Button(text='Ola')
        flx.Button(text='Mundo')


flx.App(Exemplo, title='Flexx demonstração').launch()
flx.run()
