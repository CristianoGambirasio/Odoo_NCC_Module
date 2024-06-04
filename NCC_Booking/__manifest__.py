{
    'name': "ncc_booking",

    'summary': """
        Booking module for NCC""",

    'description': """
        Add new NCC service booking connected with fleet module and calendar module
    """,

    'author': "Cristiano Gambirasio",
    'website': "c.gambirasio6@studenti.unibg.it",

    'category': 'Sales',
    'version': '1.0',
    'installable': True,
    'application': True,

    'depends': ['base','fleet','web'],

    'data': [
        'security/ir.model.access.csv',
        'views/booking_view.xml',
        'views/calendar_view.xml',
        'views/assign_view.xml'
    ],
}
