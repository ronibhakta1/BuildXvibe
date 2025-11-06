"use client";

import { PlaceholdersAndVanishInput } from "./ui/placeholders-and-vanish-input";

export function PlaceholdersAndVanishInputDemo() {
    const placeholders = [
        "Build your dream website with BuildXvibe...",
        "What kind of website should we create today?",
        "Turn your website ideas into reality",
        "Create a stunning e-commerce site",
        "Design a beautiful portfolio website",
    ];

    const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
        console.log(e.target.value);
    };
    const onSubmit = (e: React.FormEvent<HTMLFormElement>) => {
        e.preventDefault();
        console.log("submitted");
    };
    return (
        <div className="h-[40rem] flex flex-col justify-center items-center px-4">
            <h2 className="mb-10 sm:mb-10 text-xl font-bold text-center sm:text-5xl dark:text-dark text-white ">
                Build something great
            </h2>
            <PlaceholdersAndVanishInput
                placeholders={placeholders}
                onChange={handleChange}
                onSubmit={onSubmit}
            />
        </div>
    );
}
