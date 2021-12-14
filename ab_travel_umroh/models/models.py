
from odoo import api, fields, models         
class PaketPerjalanan(models.Model):
    _name = 'paket.perjalanan'
    _description = 'Travel Package'
    
    tanggal_berangkat = fields.Date(string="Tanggal Berangkat")
    tanggal_kembali = fields.Date(string="Tanggal Kembali")
    product_id = fields.Many2one('product.product', string="Sale", tracking=True)
    bom_id = fields.Many2one('product.product', string="Package", tracking=True)
    quota = fields.Char(string="Quota")
    remaining_quota = fields.Char(string="Remaining Quota", compute="remaining_quota")
    quota_progress = fields.Char(string="Quota Progress" ,compute="quota_progress")
    
    
    #NOTEBOOK HOTEL
    partner_id = fields.Many2one('res.partner', string='Nama Hotel', domain=[('hotels', '=', True)])
    nama_kota = fields.Char(string='Nama Kota', related='partner_id.city', tracking=True,)
    tanggal_masuk = fields.Date(string='Tanggal Masuk')
    tanggal_keluar = fields.Date(string='Tanggal Keluar')
    hotel_line = fields.One2many('paket.perjalanan', 'hotel_id', string='Hotel')
    hotel_id = fields.Many2one('paket.perjalanan', string='Hotel Line')