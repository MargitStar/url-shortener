from marshmallow import Schema, fields


class URLLongSchema(Schema):
    long_url = fields.Str()


class URLShortSchema(Schema):
    short_url = fields.Str()
