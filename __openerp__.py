{
    'name' : 'Parking Management System - Transaction Module',
    'version' : '1.0',
    'author' : 'JakC',
    'category' : 'Generic Modules/Parking Transaction Module',
    'depends' : ['base_setup','base','hr'],
    'init_xml' : [],
    'data' : [			        
        'security/ir.model.access.csv',             
        'jakc_parking_trans_view.xml',
        'jakc_parking_trans_menu.xml',        
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}