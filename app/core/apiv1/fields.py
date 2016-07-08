from flask_restful import fields

post_base_fields = dict(
    'id'=fields.Integer,
    'title'=fields.String,
    'slug'=fields.String,
    'body'=fields.String,
    'timestamp'=fields.String(
                    attribute=lambda x: x.timestamp.strftime("%F %H:%M:%S")
    )
)

category_base_fields = dict(
    'id'=fields.Integer,
    'title'=fields.String,
    'slug'=fields.String,
    'body'=fields.String,
    'timestamp'=fields.String(
                    attribute=lambda x: x.timestamp.strftime("%F %H:%M:%S")
    )
)
