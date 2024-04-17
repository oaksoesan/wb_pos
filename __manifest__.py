{
    'name': 'WB POS Addon',
    'version': '1.0',
    'summary': 'Add WB POS Settings',
    'sequence': 10,
    'depends': [
        'point_of_sale',

    ],
    'assets': {
        'point_of_sale.assets':[
            'wb_pos/static/src/js/wb_sample_button.js',
            'wb_pos/static/src/xml/wb_sample_button.xml',
        ]
    }
}