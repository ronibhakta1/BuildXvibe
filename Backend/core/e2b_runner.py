from typing import Optional
from e2b import Sandbox
from dotenv import load_dotenv
from exceptions import SandboxNotFoundError
import logging

load_dotenv()

logger = logging.getLogger(__name__)

class E2BRunner:
    """Manages E2B sandbox lifecycle and operations."""
    
    DEFAULT_TIMEOUT = 600
    DEFAULT_PORT = 3000
    
    def __init__(self, port: int = DEFAULT_PORT, timeout: int = DEFAULT_TIMEOUT):
        """
        Initialize E2B runner with configurable settings.
        
        Args:
            port: The port number for the application (default: 3000)
            timeout: Sandbox timeout in seconds (default: 600)
        """
        self.port = port
        self.timeout = timeout

    def get_available_sandbox_id(self, template: Optional[str] = None) -> str:
        """
        Get the ID of the first available running sandbox, optionally filtered by template.
        
        Args:
            template: Optional template name to filter sandboxes by
        
        Returns:
            str: The sandbox ID
            
        Raises:
            SandboxNotFoundError: If no running sandboxes are found
        """
        try:
            paginator = Sandbox.list()
            running_sandboxes = paginator.next_items()
            
            if not running_sandboxes:
                raise SandboxNotFoundError("No running sandboxes found.")
            
            # Filter by template if specified
            if template:
                matching_sandboxes = [s for s in running_sandboxes if s.template_id == template]
                if not matching_sandboxes:
                    raise SandboxNotFoundError(f"No running sandboxes found for template: {template}")
                running_sandboxes = matching_sandboxes
            
            sandbox_id = running_sandboxes[0].sandbox_id
            logger.info(f"Found available sandbox: {sandbox_id}")
            return sandbox_id
            
        except SandboxNotFoundError:
            raise
        except Exception as e:
            logger.error(f"Error fetching available sandboxes: {e}")
            raise

    def create_sandbox(self, template: str) -> dict[str, str]:
        """
        Create a new sandbox from a template.
        
        Args:
            template: The template name to use for sandbox creation
            
        Returns:
            dict: Contains 'sandbox_id' and 'url' keys
            
        Raises:
            Exception: If sandbox creation fails
        """
        try:
            logger.info(f"Creating sandbox from template: {template}")
            sandbox = Sandbox.create(template=template, timeout=self.timeout)
            host = sandbox.get_host(self.port)
            url = f"https://{host}"
            
            logger.info(f"Sandbox created successfully. ID: {sandbox.sandbox_id}, URL: {url}")
            
            return {
                "sandbox_id": sandbox.sandbox_id,
                "url": url,
                "sandbox": sandbox
            }
            
        except Exception as e:
            logger.error(f"Failed to create sandbox: {e}")
            raise

    def connect_to_sandbox(self, sandbox_id: str) -> tuple[Sandbox, str]:
        """
        Connect to an existing sandbox by ID.
        
        Args:
            sandbox_id: The ID of the sandbox to connect to
            
        Returns:
            tuple: (Sandbox instance, URL string)
            
        Raises:
            Exception: If connection fails
        """
        try:
            logger.info(f"Connecting to sandbox: {sandbox_id}")
            sandbox = Sandbox.connect(sandbox_id=sandbox_id, timeout=self.timeout)
            host = sandbox.get_host(self.port)
            url = f"https://{host}"
            
            logger.info(f"Connected to sandbox. URL: {url}")
            return sandbox, url
            
        except Exception as e:
            logger.error(f"Failed to connect to sandbox {sandbox_id}: {e}")
            raise

    def get_or_create_sandbox(self, template: str, prefer_existing: bool = True) -> tuple[Sandbox, str]:
        """
        Try to connect to an existing sandbox, or create a new one if none exist.
        
        Args:
            template: The template name to use if creating a new sandbox
            prefer_existing: If True, try to reuse existing sandbox; if False, always create new
            
        Returns:
            tuple: (Sandbox instance, URL string)
        """
        if prefer_existing:
            try:
                sandbox_id = self.get_available_sandbox_id(template=template)
                logger.info(f"Reusing existing sandbox for template: {template}")
                return self.connect_to_sandbox(sandbox_id)
            except SandboxNotFoundError:
                logger.info(f"No existing sandbox found for template: {template}, creating new one...")
        else:
            logger.info("Creating new sandbox as requested...")
        
        result = self.create_sandbox(template)
        return result["sandbox"], result["url"]
    
    def get_sandbox_url(self, sandbox: Sandbox) -> str:
        """
        Get the URL of a given sandbox.
        
        Args:
            sandbox: The Sandbox instance
            
        Returns:
            str: The URL of the sandbox
        """
        host = sandbox.get_host(self.port)
        url = f"https://{host}"
        return url
    
    def delete_sandbox(self, sandbox: Sandbox) -> dict[str, str]:
        """
        Delete a sandbox.
        
        Args:
            sandbox: The Sandbox instance to delete
            
        Returns:
            dict: Contains 'status' and 'sandbox_id' keys
            
        Raises:
            Exception: If deletion fails
        """
        try:
            logger.info(f"Deleting sandbox: {sandbox.sandbox_id}")
            sandbox.kill()
            logger.info(f"Sandbox {sandbox.sandbox_id} deleted successfully.")
            
            return {
                "status": "deleted",
                "sandbox_id": sandbox.sandbox_id
            }
        except Exception as e:
            logger.error(f"Failed to delete sandbox {sandbox.sandbox_id}: {e}")
            raise


if __name__ == "__main__":
    # Configure logging
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    
    runner = E2BRunner(port=3000, timeout=600)
    
    try:
        # Try to get or create a sandbox (set prefer_existing=False to always create new)
        sandbox, url = runner.get_or_create_sandbox(
            template="nextjs-app-v2",
            prefer_existing=False  # Change to True to reuse existing sandboxes
        )
        print(f"\n✅ Sandbox ready!")
        print(f"Sandbox ID: {sandbox.sandbox_id}")
        print(f"URL: {url}\n")
        
        # Explicitly create a new one (alternative approach)
        # result = runner.create_sandbox(template="nextjs-app-v2")
        # print(f"New sandbox URL: {result['url']}")
        
        # Connect to existing by ID (alternative approach)
        # sandbox_id = runner.get_available_sandbox_id(template="nextjs-app-v2")
        # sandbox, url = runner.connect_to_sandbox(sandbox_id)
        # print(f"Connected to: {url}")
        
    except SandboxNotFoundError as e:
        logger.error(f"Sandbox error: {e}")
        print(f"\n❌ Error: {e}")
        print("Make sure you've built the template first with: uv run core/build.py\n")
    except Exception as e:
        logger.error(f"Unexpected error: {e}", exc_info=True)
        print(f"\n❌ Unexpected error: {e}\n")
