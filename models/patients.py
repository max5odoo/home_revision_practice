from odoo import api, fields, models


class Patients(models.Model):
    _name = 'patient.patient'
    _description = 'This is the description of all patients'
    _rec_name = "email"

    name = fields.Char()
    email = fields.Char()
    phoneno = fields.Char()
    address = fields.Text()
