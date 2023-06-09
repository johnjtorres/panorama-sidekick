"""Pytest fixtures and configurations."""

import pytest
from click.testing import CliRunner


@pytest.fixture
def runner() -> CliRunner:
    """Imitate commands entered in the CLI."""
    env = {"PANORAMA_HOSTNAME": "TEST", "PANORAMA_KEY": "TEST"}
    return CliRunner(env=env)
