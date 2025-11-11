from dotenv import load_dotenv
load_dotenv()
from e2b import Sandbox

sbx = Sandbox.create(template="nextjs-app-v2", timeout=600)
host = sbx.get_host(3000)
url = f"https://{host}"
print(f"Vite app running at: {url}")
