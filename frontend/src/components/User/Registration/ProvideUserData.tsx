import { FormEvent, useState } from "react"
import UsersHandler from "@/ApiCalls/UsersHandler"
import Link from "next/link"
import { RegisterDTO } from "@/ApiCalls/DTOs/User/RegisterDTO"
//@ts-expect-error
// Providing a function and can not specify the type
export default function ProvdeUserData({ language, registration, translations }) {
    const [email, setEmail] = useState("")
    const [password, setPassword] = useState("")
    const [username, setUsername] = useState("")
    const usersAPI = new UsersHandler()

    async function submit(e: FormEvent<HTMLFormElement>) {
        e.preventDefault()
        localStorage.setItem("email", email)
        const data: RegisterDTO = {
            email: email,
            password: password,
            username: username,
            language: language
        }
        const response = await usersAPI.register(data, translations)
        registration(e, response.tag, response.message)
    }

    return (
        <form onSubmit={(e) => { submit(e) }} className="bg-white border-1 border-gray-200 w-82 h-82 rounded-lg drop-shadow-md">
            <div className="w-full h-2/3 flex flex-col items-center justify-center space-y-3">
                <div className="flex flex-col space-y-1">
                    <label htmlFor="email">{translations.email}</label>
                    <div className="flex w-full border-2 border-solid">
                        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth="1.5" stroke="currentColor" className="size-6 border-r-2 border-black bg-orange-600 text-white">
                            <path strokeLinecap="round" strokeLinejoin="round" d="M21.75 6.75v10.5a2.25 2.25 0 0 1-2.25 2.25h-15a2.25 2.25 0 0 1-2.25-2.25V6.75m19.5 0A2.25 2.25 0 0 0 19.5 4.5h-15a2.25 2.25 0 0 0-2.25 2.25m19.5 0v.243a2.25 2.25 0 0 1-1.07 1.916l-7.5 4.615a2.25 2.25 0 0 1-2.36 0L3.32 8.91a2.25 2.25 0 0 1-1.07-1.916V6.75" />
                        </svg>
                        <input
                            className="pl-2"
                            type="email"
                            name="email"
                            placeholder={translations.exampple}
                            value={email}
                            onChange={(e) => { setEmail(e.target.value) }} />
                    </div>
                </div>
                <div className="flex flex-col space-y-1">
                    <label htmlFor="password">{translations.password}</label>
                    <div className="flex w-full border-2 border-solid">
                        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth="1.5" stroke="currentColor" className="size-6 border-r-2 border-black bg-orange-600 text-white">
                            <path strokeLinecap="round" strokeLinejoin="round" d="M16.5 10.5V6.75a4.5 4.5 0 1 0-9 0v3.75m-.75 11.25h10.5a2.25 2.25 0 0 0 2.25-2.25v-6.75a2.25 2.25 0 0 0-2.25-2.25H6.75a2.25 2.25 0 0 0-2.25 2.25v6.75a2.25 2.25 0 0 0 2.25 2.25Z" />
                        </svg>
                        <input
                            className="pl-2"
                            type="password"
                            name="password"
                            placeholder={translations.password}
                            value={password}
                            onChange={(e) => setPassword(e.target.value)} />
                    </div>
                </div>
                <div className="flex flex-col space-y-1">
                    <label htmlFor="username">{translations.username}</label>
                    <div className="flex w-full border-2 border-solid">
                        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth="1.5" stroke="currentColor" className="size-6 border-r-2 border-black bg-orange-600 text-white">
                            <path strokeLinecap="round" strokeLinejoin="round" d="M17.982 18.725A7.488 7.488 0 0 0 12 15.75a7.488 7.488 0 0 0-5.982 2.975m11.963 0a9 9 0 1 0-11.963 0m11.963 0A8.966 8.966 0 0 1 12 21a8.966 8.966 0 0 1-5.982-2.275M15 9.75a3 3 0 1 1-6 0 3 3 0 0 1 6 0Z" />
                        </svg>
                        <input
                            className="pl-2"
                            type="text"
                            name="username"
                            placeholder={translations.username}
                            value={username}
                            onChange={(e) => { setUsername(e.target.value) }} />
                    </div>
                </div>
            </div>
            <div className="w-full flex flex-col space-y-3 h-1/3 flex items-center justify-center">
                <button className="rounded-lg bg-orange-600 w-1/2 h-1/3 hover:bg-orange-400 text-white">{translations.button}</button>
                <p>{translations.account}<Link className="text-orange-600 hover:text-orange-700" href="/login">{translations["sign in"]}</Link></p>
            </div>
        </form>


    )
}
