from odoo import models, fields, api, _ ,SUPERUSER_ID
from odoo.tools.safe_eval import safe_eval


class CRMTeam(models.Model):
    _inherit = 'crm.team'

    @api.model
    def _action_update_to_pipeline(self, action):
        res = super(CRMTeam, self)._action_update_to_pipeline(action)
    #     user_team_id = self.env.user.sale_team_id.id
    #     if user_team_id:
    #         # To ensure that the team is readable in multi company
    #         user_team_id = self.search([('id', '=', user_team_id)], limit=1).id
    #     else:
    #         user_team_id = self.search([], limit=1).id
    #         action['help'] = _("""<p class='o_view_nocontent_smiling_face'>Add new opportunities</p><p>
    #     Looks like you are not a member of a Sales Team. You should add yourself
    #     as a member of one of the Sales Team.
    # </p>""")
    #         if user_team_id:
    #             action['help'] += _(
    #                 "<p>As you don't belong to any Sales Team, Odoo opens the first one by default.</p>")
    #
    #     # action_context = safe_eval(action['context'], {'uid': self.env.uid})
    #     action_context = safe_eval(action['context'], {'uid': self.env.uid})
    #     if user_team_id:
    #         # action['context'].update({'default_team_id': user_team_id})
    #         action_context['default_team_id'] = user_team_id
        kanban_view_id = self.env.ref('crm.crm_case_kanban_view_leads').id
        tree_view_id = self.env.ref('crm.crm_case_tree_view_oppor').id
        calendar_view_id = self.env.ref('crm.crm_case_calendar_view_leads').id
        pivot_view_id = self.env.ref('crm.crm_lead_view_pivot').id
        graph_view_id = self.env.ref('crm.crm_lead_view_graph').id
        res['views'] = [(tree_view_id, 'tree'),
                              (kanban_view_id, 'kanban'),
                              (calendar_view_id, 'calendar'),
                              (pivot_view_id, 'pivot'),
                              (graph_view_id, 'graph'),
                              (False, 'form'),
                              (False, 'activity')]
        res['domain'] = [('is_converted_declined_stage', '=', False)]
        return res