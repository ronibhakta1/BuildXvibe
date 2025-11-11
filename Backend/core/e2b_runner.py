from dotenv import load_dotenv
load_dotenv()
from e2b import Sandbox

# sbx = Sandbox.create(template="nextjs-app-v2", timeout=600)
# host = sbx.get_host(3000)
# url = f"https://{host}"
# print(f"Vite app running at: {url}")

class E2BRunner:
    
    @staticmethod
    def avaliable_sandboxes():
        sandboxes = Sandbox.list()
        return sandboxes
    
    @classmethod
    def create_sandbox(clx,template):
        sbx = Sandbox.create(template=template, timeout=600)
        host = sbx.get_host(3000)
        url = f"https://{host}"
        return url
    
    @classmethod
    def connect_e2b(clx,sandbox_id : str):
        sbx = Sandbox.connect(sandbox_id=sandbox_id, timeout=600)
        host = sbx.get_host(3000)
        url = f"https://{host}"
        print(f"Next.js app running at: {url}")
        return sbx

if __name__ == "__main__":
    # url = E2BRunner.create_sandbox("nextjs-app-v2")
    # print(url)
    paginator = E2BRunner.avaliable_sandboxes()
    running_sbx = paginator.next_items()
    if len(running_sbx) == 0:
        print("No running sandboxes found.")
    sandbox_id = running_sbx[0].sandbox_id
    print(sandbox_id)