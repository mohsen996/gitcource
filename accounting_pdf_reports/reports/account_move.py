from odoo import api, fields, models
from odoo.exceptions import ValidationError



class Move_line(models.Model):
    _inherit='account.move'

    # request.env['ir.config_parameter'].get_param(
    #     'web.base.url') / web  # id=request.env['account.move'].search([('name','=',line['move_name'])]).id&amp;model=account.move&amp;view_type=form
    def get_url_for_pdf(self,move_name):
        move_id=self.env['account.move'].search([('name','=',move_name)],limit=1).id
        if move_id:
            base=self.env['ir.config_parameter'].get_param('web.base.url')
            base+="/web#id="+str(move_id)+"&model=account.move&view_type=form"
            print(">>>>>>>>>>>>>.", base)
            return base
        else:
            return ""



    def get_account_total(self,account_id,docs):

        domain=[]
        partners=[]
        if account_id:
            domain.append(('account_id','=',account_id))
        if docs:
            for doc in docs:
                partners.append(doc.id)
            domain.append(('partner_id', 'in', partners))

        print(">>mzzzzzzzzzzzzz>>>>",account_id,docs)

        moves = self.env['account.move.line'].read_group(
            domain=domain,
            fields=['debit','credit','balance'],
            groupby=['account_id'],
            lazy=False,
        )
        if moves:
            print("XXXXXXXXXXXXX>>",moves[0]['balance'])
            return moves[0]

        else:
            return 0



