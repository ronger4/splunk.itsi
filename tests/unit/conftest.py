# -*- coding: utf-8 -*-
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Copyright (c) 2026 Splunk ITSI Ansible Collection maintainers
"""Shared test helpers for splunk.itsi unit tests."""

from typing import Optional
from unittest.mock import MagicMock


# ---------------------------------------------------------------------------
# Exception classes to simulate Ansible module exit / fail behaviour.
# Inherit from SystemExit so they are NOT caught by ``except Exception``
# blocks inside the modules under test.
# ---------------------------------------------------------------------------
class AnsibleExitJson(SystemExit):
    """Exception raised when module.exit_json() is called."""

    pass


class AnsibleFailJson(SystemExit):
    """Exception raised when module.fail_json() is called."""

    pass


# ---------------------------------------------------------------------------
# Mock helpers
# ---------------------------------------------------------------------------
def make_mock_conn(
    status: int = 200,
    body: str = "{}",
    headers: Optional[dict] = None,
) -> MagicMock:
    """Create a MagicMock connection with a canned send_request response.

    Args:
        status: HTTP status code to return.
        body: Response body string (usually JSON).
        headers: Optional response headers dict.

    Returns:
        A MagicMock whose ``send_request`` returns the configured response.
    """
    conn = MagicMock()
    conn.send_request.return_value = {
        "status": status,
        "body": body,
        "headers": headers or {},
    }
    return conn
