import CredentialsProvider from "next-auth/providers/credentials"

export const Next_Auth = {
    providers:[
        CredentialsProvider({
            name:"Credentials",
            credentials:{
                username: {
                    label: "username",
                    type: "text",
                    placeholder: "roni bhakta"
                },
                password: {
                    label: "password",
                    type: "password",
                    placeholder: "your password"
                }
            },
            async authorize(credentials : any){

                if(credentials){
                    const username = credentials?.username;
                    const email = credentials?.username + '@gmail.com';
                    
                    return {
                        id: "1", 
                        username: username, 
                        email: email
                    }
                }
                return null;
            }
        })
    ],
    secret: process.env.NEXTAUTH_SECRET,
    callbacks:{
        async redirect({ url, baseUrl }: { url: string; baseUrl: string }) {
            try {
                const target = new URL(url, baseUrl);
                if (target.origin === baseUrl) return target.toString();
            } catch {
                /* noop */
            }
            if (url?.startsWith("/")) return `${baseUrl}${url}`;
            return baseUrl;
        },
    },
    pages:{
        signIn: '/signin',
    }
}