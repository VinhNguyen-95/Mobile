from odoo import models, api, fields
class mobile_info(models.Model):
    _name = 'mobile.info'
    _description = 'Mobile Information'

    name = fields.Char(string="Tên điện thoại", required=True)
    producer = fields.Many2one('res.partner',string="Nhà sản xuất")
    date_manufacturing = fields.Date("Ngày sản xuất")
    length = fields.Float("Chiều dài")
    width = fields.Float("Chiều rộng")
    thinkness = fields.Float("Độ dày")
    screen_size = fields.Float("Kích thước màn hình")
    screen_resolution = fields.Float("Độ phân giải màn hình")
    operating_system = fields.Char("Hệ điều hành")
    CPU = fields.Float()
    RAM = fields.Float()
    price = fields.Float('Giá bán')

    color = fields.Integer('Color Index')
    priority = fields.Selection(
        [('0', 'Low'),
         ('1', 'Normal'),
         ('2', 'High')],
        'Priority',
        default='1')
    kanban_state = fields.Selection(
        [('normal', 'In progress'),
         ('blocked', 'Blocked'),
         ('done', 'Ready for next stage')],
        'Kanban Stage',
        default = 'normal')


