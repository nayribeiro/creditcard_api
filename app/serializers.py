from marshmallow import Schema, fields, validate, post_dump
from .utils import format_date


class CardSchema(Schema):
    holder = fields.String(required=True, validate=validate.Length(min=2))
    exp_date = fields.String(required=True)
    number = fields.String(required=True, validate=validate.Length(min=16, max=16))
    cvv = fields.Integer(required=True, validate=validate.Range(min=100, max=9999))
