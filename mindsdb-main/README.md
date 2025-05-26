

<a name="readme-top"></a>

<div align="center">
	<a href="https://pypi.org/project/MindsDB/" target="_blank"><img src="https://badge.fury.io/py/MindsDB.svg" alt="MindsDB Release"></a>
	<a href="https://www.python.org/downloads/" target="_blank"><img src="https://img.shields.io/badge/python-3.10.x%7C%203.11.x-brightgreen.svg" alt="Python supported"></a>
	<a href="https://ossrank.com/p/630"><img src="https://shields.io/endpoint?url=https://ossrank.com/shield/630"></a>
	<img alt="PyPI - Downloads" src="https://img.shields.io/pypi/dm/Mindsdb">
	<a href="https://hub.docker.com/u/mindsdb" target="_blank"><img src="https://img.shields.io/docker/pulls/mindsdb/mindsdb" alt="Docker pulls"></a>

  <br />
  <br />

  <a href="https://github.com/mindsdb/mindsdb">
    <img src="/docs/assets/mindsdb_logo.png" alt="MindsDB" width="300">
  </a>

  <p align="center">
    <br />
    <a href="https://www.mindsdb.com?utm_medium=community&utm_source=github&utm_campaign=mindsdb%20repo">Website</a>
    ·
    <a href="https://docs.mindsdb.com?utm_medium=community&utm_source=github&utm_campaign=mindsdb%20repo">Docs</a>
    ·
    <a href="https://mdb.ai/register">Demo</a>
    ·
    <a href="https://mindsdb.com/joincommunity?utm_medium=community&utm_source=github&utm_campaign=mindsdb%20repo">Community Slack</a>
  </p>
</div>

----------------------------------------


MindsDB is an AI data solution that enables humans, AI, agents, and applications to query data in natural language and SQL, and get highly accurate answers across disparate data sources and types.

![image](https://github.com/user-attachments/assets/03b779e8-7008-485e-989a-e8733cb94e4c)

A federated query engine that tidies up your data-sprawl chaos while meticulously answering every single question you throw at it. 

[MindsDB has an MCP server built in](https://docs.mindsdb.com/mcp/overview) that enables your MCP applications to connect, unify and respond to questions over large-scale federated data—spanning databases, data warehouses, and SaaS applications.

## Minds [Demo](https://mdb.ai/register)
Play with [Minds demo](https://mdb.ai/register), and see the power of MindsDB at answering questions from structured to unstructured data, whether it's scattered across SaaS applications, databases, or... hibernating in data warehouses like that $100 bill in your tuxedo pocket from prom night, lost, waiting to be discovered.
 
## Install MindsDB Server 

MindsDB is an open-source server that can be deployed anywhere - from your laptop to the cloud, and everywhere in between. And yes, you can customize it to your heart's content.

  * [Using Docker Desktop](https://docs.mindsdb.com/setup/self-hosted/docker-desktop). This is the fastest and recommended way to get started and have it all running.
  * [Using Docker](https://docs.mindsdb.com/setup/self-hosted/docker). This is also simple, but gives you more flexibility on how to further customize your server.
  * [Using PyPI](https://docs.mindsdb.com/contribute/install). This option enables you to contribute to MindsDB.

## MindsDB Integration

This repository includes a `mindsdb-main` folder containing the MindsDB server code.
To get it working locally:

1. Copy `.env.example` to `.env` and add your OAuth and Snowflake credentials.
2. Run the server and try the `custom_llm` engine.

For full setup instructions see [docs/mindsdb_setup.md](../docs/mindsdb_setup.md).

## Connect Your Data

You can connect to hundreds of [data sources (learn more)](https://docs.mindsdb.com/integrations/data-overview). This is just an example of a Postgres database.