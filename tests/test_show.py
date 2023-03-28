"""Testing show commands."""

from panorama_sidekick.cli import cli
from panorama_sidekick.panorama import Panorama


def test_pano_show_device_groups(runner, monkeypatch):
    """Test for listing device groups."""
    test_xml = """\
    <response>
      <result>
        <devicegroups>
          <entry name="DG1"></entry>
          <entry name="DG2"></entry>
          <entry name="DG3"></entry>
        </devicegroups>
      </result>
    </response>
    """

    monkeypatch.setattr(Panorama, "get", lambda *args, **kwargs: test_xml)
    result = runner.invoke(cli, ["show", "device-groups"])
    assert "DG1\nDG2\nDG3\n" == result.output
