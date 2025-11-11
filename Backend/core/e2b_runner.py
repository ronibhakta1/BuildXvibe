from dotenv import load_dotenv
load_dotenv()
from e2b import Sandbox

sbx = Sandbox.create(template="node-npm-vite")
host = sbx.get_host(5173)
url = f"https://{host}"
print(f"Vite app running at: {url}")
