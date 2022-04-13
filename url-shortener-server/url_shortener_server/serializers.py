from marshmallow import Schema, fields


class URLSchema(Schema):
    long_url = fields.Str()
    short_url = fields.Str()
