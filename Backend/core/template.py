from dotenv import load_dotenv
load_dotenv()
from e2b import Template, wait_for_url

template = (
    Template()
    .from_node_image("21-slim")
    .set_workdir("/home/user/nextjs-app")
    .run_cmd(
        'npx create-next-app@14.2.30 . --ts --tailwind --no-eslint --import-alias "@/*" --use-npm --no-app --no-src-dir'
    )
    .run_cmd("npx shadcn@2.1.7 init -d")
    .run_cmd("npx shadcn@2.1.7 add --all")
    .run_cmd("mv /home/user/nextjs-app/* /home/user/ && rm -rf /home/user/nextjs-app")
    .set_workdir("/home/user")
    .set_start_cmd("npx next --turbo", wait_for_url('http://localhost:3000'))
)