# -*- coding: utf-8 -*-
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Copyright (c) 2026, Splunk ITSI Ansible Collection maintainers
"""Glass table utilities for Splunk ITSI Ansible modules."""


from typing import Any, Optional
from urllib.parse import quote_plus

from ansible_collections.splunk.itsi.plugins.module_utils.itsi_request import ItsiRequest

# API endpoint for ITSI glass tables
BASE_GLASS_TABLE_ENDPOINT = "servicesNS/nobody/SA-ITOA/itoa_interface/glass_table"


def get_glass_table_by_id(
    client: ItsiRequest,
    glass_table_id: str,
) -> Optional[dict[str, Any]]:
    """Fetch a single ITSI glass table by its _key.

    Args:
        client: ItsiRequest instance for API requests.
        glass_table_id: The glass table _key to retrieve.

    Returns:
        Glass table dictionary from the API response, or None if not found (404).
    """
    path = f"{BASE_GLASS_TABLE_ENDPOINT}/{quote_plus(glass_table_id)}"
    result = client.get(path)
    if result is None:
        return None
    _status, _headers, body = result
    return body if isinstance(body, dict) else None
