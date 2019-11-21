from odoo import http
class Mobiles(http.Controller):
    @http.route('/mobile/info', auth='user')
    def list(self, **kwargs):
        _Mobile = http.request.env['mobile.info']
        mobiles = _Mobile.search([])
        return http.request.render('Mobile.mobile_list_template', {'mobiles': mobiles})