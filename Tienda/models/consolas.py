from openerp import models, fields, api

class consolas(models.Model):
    _name = 'juegos.consolas'
    marca = fields.Char('Marca', required=True)
    nombre = fields.Char('Nombre', required=True)
    descripcion = fields.Char('Descripcion', required=True)
    precio = fields.Char('Precio', required=True)


    @api.one
    def limpiar(self):
        self.marca = ""
        return True
