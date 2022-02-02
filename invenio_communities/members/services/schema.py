# -*- coding: utf-8 -*-
#
# Copyright (C) 2022 Northwestern University.
#
# Invenio-Communities is free software; you can redistribute it and/or modify
# it under the terms of the MIT License; see LICENSE file for more details.

"""Member schema."""

from flask_babelex import lazy_gettext as _
from invenio_records_resources.services.records.schema import BaseRecordSchema
from marshmallow import fields, validates_schema, ValidationError
from marshmallow_utils.fields import SanitizedUnicode


class MemberSchema(BaseRecordSchema):
    """Schema for a community member."""

    # input and output
    community = SanitizedUnicode(required=True)
    user = fields.Integer()
    # TODO: add group
    # group = SanitizedUnicode()
    # TODO: add role
    # role = SanitizedUnicode(
    #     required=True,
    #     validate=validate.OneOf(ROLE_TYPES)
    # )
    # TODO: add visibility
    # visibility = SanitizedUnicode(
    #   required=True, validate=_not_blank(max=100))

    # output only
    # TODO: add name
    # name = SanitizedUnicode(dump_only=True)

    @validates_schema
    def validate_member_entity(self, data, **kwargs):
        """Check that at least one member entity is passed."""
        valid_entities = ['user', 'group']

        # TODO?: Could maybe use something like ?
        # validate.OneOf(valid_entities)
        if not any(e in data for e in valid_entities):
            raise ValidationError(
                _("There must be one of {}".format(valid_entities))
            )