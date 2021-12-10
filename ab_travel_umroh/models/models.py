from odoo import api, fields, models
 
class UmrohTravel(models.Model):
    _name = 'umroh.travel'
    _description = 'Umroh Travel'
     
    name = fields.Char(string='Judul', required=True)
    description = fields.Text(string='Keterangan')

    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100
            
class PaketPerjalanan(models.Model):
    _name = 'paket.perjalanan'
    _description = 'Travel Package'
    
    tanggal_berangkat = fields.Date(string="Tanggal Berangkat")
    tanggal_kembali = fields.Date(string="Tanggal Kembali")
    product_id = fields.Many2one('product.product', string="Sale")
    bom_id = fields.Many2one('product.product', string="Package")
    quota = fields.Char(string="Quota")
    remaining_quota = fields.Char(string="Remaining Quota")
    quota_progress = fields.Char(string="Quota Progress")
    
#     hpp_line = field_name = fields.One2many('Bayar.paket.perjalanan', 'inverse_field_name', string='HPP Lines')
# class BayarPaketPerjalanan(models.Model):
#     _name = 'Bayar.paket.perjalanan'
#     _description = 'Cost Travel Package'
    
#     barang = fields.Char()
#     quantity = fields.Integer()
#     unit = fields.Integer()
#     unit_price = fields.Integer()
#     subtotal = fields.Integer()