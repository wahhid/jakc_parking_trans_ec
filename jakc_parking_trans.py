from openerp.osv import fields, osv
import datetime
import logging

_logger = logging.getLogger(__name__)


AVAILABLE_STATES = [
    ('draft','Draft'),
    ('open','Open'),
    ('done','Close'),
]

AVAILABLE_TRANS_TYPE = [
    ('0', 'Casual'),
    ('1', 'Member'),
    ('2', 'Pinalty'),    
]

class park_trans(osv.osv):
    _name = "park.trans"
    _description = "Parking Booth"
    _columns = {
        'trans_id': fields.char('Transaction ID', size=20, required=True),
        'trans_type_id': fields.selection(AVAILABLE_TRANS_TYPE,'Transaction Type', size=16, required=True),        
        'plat_number': fields.char('Plat Number', size=20),
        'member_card_id': fields.char('Member Card #', size=20),
        'vehicle_type_id': fields.many2one('park.vehicle.type',required=True),
        'date_time_in': fields.datetime('Date Time In', required=True),
        'booth_in_id': fields.many2one('park.booth','Booth In', required=True),
        'operator_in_id': fields.many2one('hr.employee','Employee In', required=True),
        'shift_in_id': fields.many2one('park.shift','Shift In'),            
        'date_time_out': fields.datetime('Date Time In'),
        'booth_out_id': fields.many2one('park.booth','Booth Out'),
        'operator_out_id': fields.many2one('hr.employee','Employee Out'),    
        'shift_out_id': fields.many2one('park.shift', 'Shift Out'),            
        'hours': fields.integer('Hours'),
        'minutes': fields.integer('Minutes'),
        'seconds': fields.integer('Seconds'),
        'pricing_id': fields.many2one('park.pricing','Pricing'),
        'parking_charge': fields.float('Parking Charge'),
        'service_charge': fields.float('Service Charge'),
        'missing_charge': fields.float('Missing Charge'),        
        'pinalty_charge': fields.float('Pinalty Charge'),
        'voucher_charge': fields.float('Voucher Charge'),                
        'total_amount': fields.float('Total Amount'),        
        'trans_image_ids': fields.one2many('park.trans.detail','trans_id','Details'),
        'trans_voucher_ids': fields.one2many('park.trans.voucher','trans_id','Vouchers'),            
        'state': fields.selection(AVAILABLE_STATES,size=16),        
    }
    _defaults = {
        'state': lambda *a: 'open',        
        'total_amount': lambda *a: 0.0,
    }
    
park_trans()

class park_trans_image(osv.osv):
    _name = "park.trans.image"
    _description = "Parking Transaction Image"
    _columns = {
        'trans_id': fields.many2one('park.trans','Transaction ID'),
        'image_type_id': fields.many2one('park.image.type','Imaget Type'),
        'image1': fields.char('Image', size=20),
    }
park_trans_image()

class park_trans_voucher(osv.osv):
    _name = "park.trans.voucher"
    _description = "Parking Transcation Voucher"
    _columns = {
        'trans_id': fields.many2one('park.trans','Transcation ID'),
        'voucher_id': fields.char('Voucher #', size=20),
        'amount': fields.float('Amount'),        
    }

park_trans_voucher()