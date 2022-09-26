from odoo import api, fields, models, _
from odoo.exceptions import UserError, ValidationError
from datetime import datetime


class PartnerLedgerReport(models.AbstractModel):
    _name = 'report.partner_ledg_prod_rpt.prtnr_ldgr_rpt_prod_wise'
    _description = "Partner ledger report product Wise"

    @api.model
    def _get_report_values(self, docids, data=None):
        if self.env.context.get('from_wizard'):
            docs = self.env['res.partner'].browse(data['active_id'])
            account_data = self.env['account.move.line'].search(
                [('partner_id', '=', docs.id), ('create_date', '>=', datetime.fromisoformat(data['date_from'])),
                 ('create_date', '<=', datetime.fromisoformat(data['to_date']))])
        else:
            docs = self.env['res.partner'].browse(docids)
            account_data = self.env['account.move.line'].search(
                [('partner_id', '=', docs.id)])

        ledger_data = []
        filter_rec = account_data.filtered(
            lambda x: x.account_id.user_type_id.name != 'Receivable'
        )
        for rec in filter_rec:
            ledger_data.append(
                {
                    'date': rec.date,
                    'journal': rec.move_id.name,
                    'account': rec.account_id.name,
                    'label': rec.name,
                    'debit': rec.debit,
                    'credit': rec.credit,
                    'balance': rec.balance,
                    'ref': rec.payment_id.ref
                }
            )

        return {
            'doc_ids': docids,
            'doc_model': 'res.partner',
            'docs': docs,
            'ledger_data': ledger_data
        }
