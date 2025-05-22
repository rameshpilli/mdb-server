"""Integration plugins registration."""

# Import custom plugins so they register themselves when this package is imported.
from mindsdb.plugins import custom_llm  # noqa: F401
