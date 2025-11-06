"use client"
import { Button } from "./ui/button";
import Link from "next/link";
import { useRouter } from "next/navigation";

export default function Navbar() {
    const router = useRouter();

    return (
        <div className="fixed top-0 left-0 w-full h-16 backdrop-blur-md bg-white/0 text-white flex items-center justify-between p-4 border-b border-white/10 z-50">
            <div className="flex-row-reverse ml-15"></div>
            <div className="flex text-md items-center gap-10">
            <div className="gap-2 text-2xl font-bold ">BuildXvibe</div>
                <div>
                    <Link href={"/"}>Home</Link>
                </div>
                <div>
                    <Link href={"/about"}>About</Link>
                </div>
            </div>
            <div className="flex-1 flex justify-end mr-20 gap-3.5">
                <Button className="bg-zinc-700 text-white" onClick={() => router.push("/signin")}>Sign In</Button>
                <Button className="bg-zinc-800 text-white" onClick={() => router.push("/signup")}>Sign Up</Button>
            </div>
        </div>
    );
}