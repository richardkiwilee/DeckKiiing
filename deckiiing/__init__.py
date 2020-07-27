import click


@click.group()
def cli():
    pass


@click.command()
def fs():
    click.echo('Wanna make your dream comes true? This is the first step!')
