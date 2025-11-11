from e2b import Template, default_build_logger
from template import template

Template.build(
    template,
    alias="node-npm-vite",
    cpu_count=2,
    memory_mb=2048,
    on_build_logs=default_build_logger(),
)