{
    'name' : 'Mobile Management',
    'description' : 'Manage mobile',
    'author' : 'Vinh Nguyen',
    'depends' : ['base'],
    'application' : False,
    'data' : [
        'security/ir.model.access.csv',
        'views/mobile_info_menu.xml',
        'views/mobile_info_view.xml',
        # 'views/mobile_kanban_view.xml',
        'views/mobile_list_template.xml',
    ]
}