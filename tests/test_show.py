"""Testing show commands."""

from click.testing import CliRunner

from panorama_sidekick.show import device_groups


def test_pano_show_device_groups():
    runner = CliRunner()
    result = runner.invoke(device_groups)
    assert "DG1\nDG2\nDG3\n" == result.output
