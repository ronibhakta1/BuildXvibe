from e2b import Template, wait_for_url
from dotenv import load_dotenv
load_dotenv()

template = (
    Template()
    .from_node_image("22-slim") 
    .set_workdir("/home/user/nextjs-app")
    # --- create Next.js project in a non-interactive way ---
    .run_cmd(
    'npx --yes create-next-app@latest . '
    '--ts --tailwind --no-eslint '
    '--import-alias "@/*" '
    '--use-npm --no-app --no-src-dir '
    '--no-react-compiler --no-turbopack'
)
    # --- ensure package.json exists before shadcn commands ---
    .run_cmd('test -f package.json || echo "{\\"name\\":\\"my-app\\",\\"private\\":true}" > package.json')
    # --- initialize shadcn ---
    .run_cmd('npx --yes shadcn@3.5.0 init -d')
    # --- add components ---
    .run_cmd('npx --yes shadcn@3.5.0 add --all')
    # --- move finished project out ---
    .run_cmd('mv /home/user/nextjs-app/* /home/user/ && rm -rf /home/user/nextjs-app')
    .set_workdir("/home/user")
    # --- add Next.js config ---
    .run_cmd("cat > next.config.ts << 'EOF'\nimport type { NextConfig } from 'next';\n\nconst nextConfig: NextConfig = {\n  /* config options here */\n};\n\nexport default nextConfig;\nEOF")
    .set_start_cmd("npm run dev -- -H 0.0.0.0", wait_for_url('http://localhost:3000'))
)
