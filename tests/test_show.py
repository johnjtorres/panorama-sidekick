"""Testing show commands."""

from click.testing import CliRunner
from pytest import MonkeyPatch

from panorama_sidekick.cli import cli
from panorama_sidekick.panorama import Panorama
from testing.utils import read_test_data_file


def test_pano_show_device_groups(runner: CliRunner, monkeypatch: MonkeyPatch) -> None:
    """Test for listing device groups."""
    test_xml = read_test_data_file("show_devicegroups.xml")
    monkeypatch.setattr(Panorama, "get", lambda *args, **kwargs: test_xml)
    result = runner.invoke(cli, ["show", "device-groups"])
    assert "DG1\nDG2\nDG3\n" == result.output
