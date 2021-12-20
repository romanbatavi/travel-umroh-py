
from typing_extensions import Required
from odoo import api, fields, models         
class PaketPerjalanan(models.Model):
    _name = 'paket.perjalanan'
    _description = 'Travel Package'
    
    tanggal_berangkat = fields.Date(string="Tanggal Berangkat", required=True)
    tanggal_kembali = fields.Date(string="Tanggal Kembali", required=True)
    product_id = fields.Many2one('product.product', string="Sale", required=True, tracking=True)
    bom_id = fields.Many2one('product.product', string="Package",required=True,  tracking=True)
    quota = fields.Integer(string="Quota")
    remaining_quota = fields.Integer(string="Remaining Quota", related='quota')
    quota_progress = fields.Integer(string="Quota Progress")
    
    hotels_line = fields.One2many('hotel.line', 'hotel_id', string='Hotel Lines')
    airlines_line = fields.One2many('airline.line', 'airline_id', string='Airline Lines') 
    schedules_line = fields.One2many('schedule.line', 'schedule_id', string='Schedule Lines')
    state = fields.Selection([('draft', 'Draft'), ('confirm', 'Confirm'), ('cancel', 'Cancelled'), ('done', 'Done')], string='Status', readonly=True, default='draft')
    hpp_line = fields.One2many('hpp.line', 'hpp_id', string='HPP Lines') 
    manifest_line = fields.One2many('manifest.line', 'manifest_id', string='Manifest')
    # total_cost = fields.Float(string='Total Cost: ', store=True)
    
    name = fields.Char(string='Referensi', readonly=True, default='-')
    
    @api.onchange('bom_id')
    def _onchange_bom_id(self):
        for rec in self:
            lines = [(5, 0, 0)]
            # total = 0
            print("self.bom_id", self.bom_id.bom_ids.bom_line_ids)
            for line in self.bom_id.bom_ids.bom_line_ids:
                # total += line.product_qty * line.product_id.standard_price
                vals = {
                    'barang_id': line.id,
                    'hpp_barang': line.display_name,
                    'hpp_qty': line.product_qty,
                    'hpp_unit': line.product_uom_id.id,
                    'hpp_price': line.product_id.standard_price,
                    'hpp_subtotal': line.product_id.standard_price,
                }
                lines.append((0, 0, vals))
            print("lines", lines)
            rec.hpp_line = lines
            # rec.total_cost = total
    
    @api.model
    def create(self, vals):
        vals['name'] = self.env['ir.sequence'].next_by_code('paket.perjalanan')
        return super(PaketPerjalanan, self).create(vals)
    
    def action_confirm(self):
        self.write({'state': 'confirm'})
      
    def action_done(self):
        self.write({'state': 'done'})
      
    def action_draft(self):
        self.write({'state': 'draft'})
        
    def action_cancel(self):
        self.write({'state': 'cancel'})
    
class HotelLines(models.Model):
    _name = 'hotel.line'
    _description = 'Hotel Lines'
    
    hotels_id = fields.Many2one('res.partner', string='Nama Hotel', domain=[('hotels', '=', True)])
    hotel_id = fields.Many2one('paket.perjalanan', string='Hotel Line')
    nama_kota = fields.Char(string='Nama Kota', related='hotels_id.city', tracking=True,)
    tanggal_masuk = fields.Date(string='Tanggal Masuk')
    tanggal_keluar = fields.Date(string='Tanggal Keluar')
    
class AirlineLines(models.Model):
    _name = 'airline.line'
    _description = 'Airline Lines'
    
    airlines_id = fields.Many2one('res.partner', string='Nama Pesawat', domain=[('airlines', '=', True)])
    airline_id = fields.Many2one('paket.perjalanan', String='Airlines Line')
    tanggal_berangkat = fields.Date(string='Tanggal Keberangkatan')
    kota_asal = fields.Char(string='Kota Asal')
    kota_tujuan = fields.Char(string='Kota Tujuan')
    
class ScheduleLine(models.Model):
    _name = 'schedule.line'
    _description = 'Schedule Lines'
    
    schedules_id = fields.Char(string='Nama Kegiatan')
    schedule_id = fields.Many2one('paket.perjalanan', string='Hotel Line')
    tanggal_kegiatan = fields.Date(string='Tanggal Kegiatan')
    
class ManifestLine(models.Model):
    _name = 'manifest.line'
    _description = 'Manifest Line'
    
    manifest_id = fields.Many2one('paket.perjalanan', string='Manifest')
    anggota_id = fields.Many2one('sale.order', string='Manifest')
    nama_jamaah_id = fields.Many2one('res.partner', string='Nama Jamaah')
    title = fields.Char(string='Title', Required=True, related='nama_jamaah_id.title.name')
    nama_passpor = fields.Char(string='Nama Passpor', related='nama_jamaah_id.nama_passpor')
    jenis_kelamin = fields.Char(string='Jenis Kelamin')
    no_ktp = fields.Char(string='No.KTP', related='nama_jamaah_id.ktp')
    passpor = fields.Integer(string='No.Passpor', related='nama_jamaah_id.no_passpor')
    tanggal_lahir = fields.Date(string='Tanggal Lahir', related='nama_jamaah_id.tanggal_lahir')
    tempat_lahir = fields.Char(string='Tempat Lahir', related='nama_jamaah_id.tempat_lahir')
    tanggal_berlaku = fields.Date(string='Tanggal Berlaku', related='nama_jamaah_id.tanggal_berlaku')
    tanggal_expired = fields.Date(string='Tanggal Expired', related='nama_jamaah_id.tanggal_habis')
    imigrasi = fields.Char(string='Imigrasi', related='nama_jamaah_id.imigrasi')
    tipe_kamar = fields.Selection([
        ('double', 'Double'), 
        ('triple', 'Triple'), 
        ('quad', 'Quad')], 
        string='Tipe Kamar', default='quad', Required=True)
    umur = fields.Integer(string='Umur')
    mahram = fields.Many2one('res.partner', string='Mahram')
    agent = fields.Char(string='Agent')
    notes = fields.Char(string='Notes')
    
    gambar_passpor = fields.Image(string="Scan Passpor")
    gambar_ktp = fields.Image(string="Scan KTP")
    gambar_bukuk_nikah = fields.Image(string="Scan Buku Nikah")
    gambar_kartu_keluarga = fields.Image(string="Scan Kartu Keluarga")
        
class HppLines(models.Model):
    _name = 'hpp.line'
    _description = 'HPP Lines'
    
    hpp_id = fields.Many2one('paket.perjalanan', string='HPP ID')
    barang_id = fields.Many2one('mrp.bom', string='Barang')
    hpp_barang = fields.Char(string='Nama Barang')
    hpp_qty = fields.Integer(string='Quantity')
    hpp_unit = fields.Many2one('uom.uom', string='Unit(s)')
    hpp_price = fields.Float(string='Unit Price')
    hpp_subtotal = fields.Float(string='Sub Total')
class SaleOrder(models.Model):
    _inherit = 'sale.order'
    
    paket_perjalanan_id = fields.Many2one('paket.perjalanan', string='Paket Perjalanan')
    form_manifest_line = fields.One2many('manifest.line', 'anggota_id', string='Passport Line')
    