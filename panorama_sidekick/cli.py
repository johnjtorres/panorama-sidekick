import click

from panorama_sidekick.show import device_groups


@click.group()
def cli():
    """Main console script entry point."""
    pass


@cli.group()
def show():
    """Command group for showing lists of things."""
    pass


show.add_command(device_groups)
