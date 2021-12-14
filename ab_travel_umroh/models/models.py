
from odoo import api, fields, models         
class PaketPerjalanan(models.Model):
    _name = 'paket.perjalanan'
    _description = 'Travel Package'
    
    tanggal_berangkat = fields.Date(string="Tanggal Berangkat")
    tanggal_kembali = fields.Date(string="Tanggal Kembali")
    product_id = fields.Many2one('product.product', string="Sale", tracking=True)
    bom_id = fields.Many2one('product.product', string="Package", tracking=True)
    quota = fields.Char(string="Quota")
    remaining_quota = fields.Char(string="Remaining Quota", related='quota')
    quota_progress = fields.Char(string="Quota Progress")
    
    hotels_line = fields.One2many('hotel.line', 'hotel_id', string='Hotel Lines')
    
    airlines_line = fields.One2many('airline.lines', 'airline_id', string='Airline Lines')
    
    hpp_line = fields.One2many('hpp.line', 'hpp_id', string='HPP Lines')
    
class HotelLines(models.Model):
    _name = 'hotel.line'
    _description = 'Hotel Lines'
    
    hotels_id = fields.Many2one('res.partner', string='Nama Hotel', domain=[('hotels', '=', True)])
    hotel_id = fields.Many2one('paket.perjalanan', string='Hotel Line')
    nama_kota = fields.Char(string='Nama Kota', related='hotels_id.city', tracking=True,)
    tanggal_masuk = fields.Date(string='Tanggal Masuk')
    tanggal_keluar = fields.Date(string='Tanggal Keluar')
    
class AirlineLines(models.Model):
    _name = 'airline.lines'
    _description = 'Airline Lines'
    
    airlines_id = fields.Many2one('res.partner', string='Nama Pesawat', domain=[('airlines', '=', True)])
    airline_id = fields.Many2one('paket.perjalanan', String='Airlines Line')
    tanggal_berangkat = fields.Date(string='Tanggal Keberangkatan')
    kota_asal = fields.Char(string='Kota Asal')
    kota_tujuan = fields.Char(string='Kota Tujuan')
    
class HppLines(models.Model):
    _name = 'hpp.line'
    _description = 'HPP Lines'
    
    hpp_id = fields.Many2one('paket.perjalanan', string='HPP ID')
    barang_id = fields.Many2one('mrp.bom', string='Barang')
    hpp_barang = fields.Char(string='Barang')
    hpp_qty = fields.Char(string='Quantity')
    hpp_unit = fields.Char(string='Unit')
    hpp_price = fields.Char(string='Price')
    hpp_total = fields.Char(string='Total')