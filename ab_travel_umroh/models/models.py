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
    _description = 'Travel Packageeeeee'
    
    tanggal_berangkat = fields.Date(string="Tanggal Berangkat")
    tanggal_kembali = fields.Date(string="Tanggal Kembali")
    product_id = fields.Many2one('product.product', string="Sale", tracking=True)
    bom_id = fields.Many2one('product.product', string="Package", tracking=True)
    quota = fields.Char(string="Quota")
    remaining_quota = fields.Char(string="Remaining Quota")
    quota_progress = fields.Char(string="Quota Progress")