from odoo import api, fields, models         
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
