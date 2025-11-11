# build.py
from e2b import Template, default_build_logger
from template import template as nextjsTemplate

Template.build(nextjsTemplate,
    alias="nextjs-app-v2",
    cpu_count=4,
    memory_mb=4096,
    on_build_logs=default_build_logger(),
)