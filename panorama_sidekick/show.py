"""Defines the commands for showing lists of things."""

import xml.etree.ElementTree as ET

import click

from panorama_sidekick.panorama import Panorama


@click.command()
@click.pass_obj
def device_groups(panorama: Panorama) -> None:
    """Print a list of device groups.

    Args:
        panorama (Panorama): Panorama object
    """
    cmd = "<show><devicegroups/></show>"
    show_devicegroups = panorama.operational_command(cmd)
    tree = ET.fromstring(show_devicegroups)
    device_group_names = "\n".join(
        dg.attrib["name"] for dg in tree.findall(".//devicegroups/entry")
    )
    click.echo(device_group_names)
