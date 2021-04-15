# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 CERN.
# Copyright (C) 2021 TU Wien.
#
# Invenio-RDM-Records is free software; you can redistribute it and/or modify
# it under the terms of the MIT License; see LICENSE file for more details.

"""Communities UI views."""

from flask import Blueprint
from flask_menu import current_menu

from .communities import communities_detail, communities_index, \
    communities_new, communities_search


#
# Registration
#
def create_ui_blueprint(app):
    """Register blueprint routes on app."""
    routes = app.config.get("COMMUNITIES_ROUTES")

    blueprint = Blueprint(
        "invenio_communities",
        __name__,
        template_folder="../templates",
    )

    # Communities URL rules
    blueprint.add_url_rule(
        routes["index"],
        view_func=communities_index,
    )

    blueprint.add_url_rule(
        routes["search"],
        view_func=communities_search,
    )

    blueprint.add_url_rule(
        routes["new"],
        view_func=communities_new,
    )

    blueprint.add_url_rule(
        routes["details"],
        view_func=communities_detail,
    )

    def register_menu():
        """."""
        item = current_menu.submenu('main.communities')
        item.register(
            'invenio_communities.communities_index',
            'Communities',
            order=3,
        )
        return item

    blueprint.before_app_first_request(register_menu)

    return blueprint