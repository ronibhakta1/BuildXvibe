import { Button } from "@/components/ui/button"
import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from "@/components/ui/card"
import {
  Field,
  FieldDescription,
  FieldGroup,
  FieldLabel,
} from "./ui/field"
import { Input } from "@/components/ui/input"

export function SigninForm({ ...props }: React.ComponentProps<typeof Card>) {
  return (
    <Card {...props} className="bg-zinc-100">
      <CardHeader>
        <CardTitle className="font-bold text-2xl">Sign in</CardTitle>
      </CardHeader>
      <CardContent>
        <form>
          <FieldGroup>
            <Field>
              <FieldLabel htmlFor="username">Username</FieldLabel>
              <Input
                id="username"
                type="username"
                required
              />
            </Field>
            <Field>
              <FieldLabel htmlFor="password">Password</FieldLabel>
              <Input id="password" type="password" required />
            </Field>
            <FieldGroup>
              <Field>
                <Button type="submit">Sign in</Button>
                <Button variant="outline" type="button" className=" bg-white/10">
                  Sign in with Google
                </Button>
                <FieldDescription className="px-6 text-center">
                  Don't have an account? <a href="/signup">Sign up</a>
                </FieldDescription>
              </Field>
            </FieldGroup>
          </FieldGroup>
        </form>
      </CardContent>
    </Card>
  )
}
