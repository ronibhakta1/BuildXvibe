from dotenv import load_dotenv
from e2b_code_interpreter import Sandbox, FilesystemEventType
from config import E2B_KEY

from time import sleep

load_dotenv()
print(E2B_KEY)
class E2BSandbox:
    @classmethod
    def create_sandbox(clx, sandbox_id: str) -> Sandbox:
        sbx = Sandbox(
            api_key=E2B_KEY,
            sandbox_id=sandbox_id,
            language="python",
            timeout=10,
            memory_limit=256,
        )
        return sbx
    
    @classmethod
    def run_code(clx, code: str) -> Sandbox:
        Sandbox.connect()

sbx = E2BSandbox().run_code("print('hello world')")
print(sbx.logs)


sandbox = Sandbox.create()
dirname = '/home/user'

handle = sandbox.files.watch_dir(dirname)
sandbox.files.write(f"{dirname}/my-file", "hello")
sandbox.files.write(f"{dirname}/my-file2", "hello whats up")

events = handle.get_new_events()

contents = sandbox.files.read(f"{dirname}/my-file")
contents = sandbox.files.read(f"{dirname}/my-file2")

sandbox.files.write(f"{dirname}/my-file", "hello world changes 2")
print("File contents:", contents)


for event in events:
    print(event)
    if event.type == FilesystemEventType.WRITE:
        print(f"wrote to file {event.name}")


sandbox.kill()