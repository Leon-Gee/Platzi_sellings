import click


@click.group()
def clients():
	""" Manages the client lifecycle"""
	pass

@click.command()
@click.pass_context
def create(ctx, name, company, email, position):
	"""Creates a new client"""
	pass


@click.command()
@click.pass_context
def list(ctx):
	"""List all clients"""
	pass


@click.command()
@click.pass_context
def update(ctx, client_uid):
	"""Updates a client"""
	pass


@click.command()
@click.pass_context
def delete(ctx, client):
	"""Deletes a client"""
	pass


all = clients


