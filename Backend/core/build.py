# build.py
from e2b import Template, default_build_logger
from template import template as nextjsTemplate

class Build:
    """Handles the build process for the Next.js application."""
    DEFAULT_TEMPLATE_NAME = "nextjs-app-v2"
    DEFAULT_CPU_COUNT = 4
    DEFAULT_MEMORY_MB = 4096
    
    def __init__(self, template_name: str = DEFAULT_TEMPLATE_NAME, cpu_count: int = DEFAULT_CPU_COUNT, memory_mb: int = DEFAULT_MEMORY_MB):
        """Initialize the build configuration."""
        self.template_name = template_name
        self.cpu_count = cpu_count
        self.memory_mb = memory_mb
        
    def build_nextjs_app(self,template_name: str, cpu_count: int, memory_mb: int):
        """Builds the Next.js application using the defined template."""    
        Template.build(nextjsTemplate,
            alias=template_name,
            cpu_count=cpu_count,
            memory_mb=memory_mb,
            on_build_logs=default_build_logger(),
        )
        
if __name__ == "__main__":
    builder = Build()
    builder.build_nextjs_app(
        template_name=Build.DEFAULT_TEMPLATE_NAME,
        cpu_count=Build.DEFAULT_CPU_COUNT,
        memory_mb=Build.DEFAULT_MEMORY_MB
    )