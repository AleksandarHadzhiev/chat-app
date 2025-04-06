"use client"

import UsersHandler from "@/ApiCalls/UsersHandler"
import ChildContext from "@/components/General/Context"
import translationLoader from "@/tools/TranslationLoader"
import Dutch from "../../dictionaries/NL/reset-password.json"
import { FormEvent, useContext, useEffect, useState } from "react"

export default function ResetPassword() {
    const [Data, setData] = useState(Dutch)
    let { language } = useContext(ChildContext)
    useEffect(() => {
        async function load() {
            const data = await translationLoader(language, "reset-password.json")
            setData(data)
        }
        load()
    }, [language])


    const usersAPI = new UsersHandler()
    const [password, setPassword] = useState('')
    function login(e: FormEvent<HTMLFormElement>) {
        e.preventDefault()
        const data = {
            password: password
        }
        usersAPI.login("http://localhost:8000/login", data)
    }
    return (
        <div className="bg-white w-full h-ull flex flex-col items-center justify-center text-black">
            <h1 className="text-3xl text-orange-600">{Data.header}</h1>
            <form
                onSubmit={(e) => { login(e) }}
                className="mt-4 bg-white border-1 border-gray-200 w-82 h-82 rounded-lg drop-shadow-md">
                <div className="w-full h-2/3 flex flex-col space-y-6 items-center justify-center">
                    <div className="flex flex-col">
                        <label htmlFor="password">{Data.password}</label>
                        <div className="flex w-full border-2 border-solid">
                            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth="1.5" stroke="currentColor" className="size-6 border-r-2 border-black bg-orange-600 text-white">
                                <path strokeLinecap="round" strokeLinejoin="round" d="M21.75 6.75v10.5a2.25 2.25 0 0 1-2.25 2.25h-15a2.25 2.25 0 0 1-2.25-2.25V6.75m19.5 0A2.25 2.25 0 0 0 19.5 4.5h-15a2.25 2.25 0 0 0-2.25 2.25m19.5 0v.243a2.25 2.25 0 0 1-1.07 1.916l-7.5 4.615a2.25 2.25 0 0 1-2.36 0L3.32 8.91a2.25 2.25 0 0 1-1.07-1.916V6.75" />
                            </svg>
                            <input
                                className="pl-2"
                                type="password"
                                name="password"
                                placeholder={Data.password}
                                value={password}
                                onChange={(e) => { setPassword(e.target.value) }} />
                        </div>
                    </div>
                </div>
                <div className="w-full flex flex-col space-y-3 h-1/3 flex items-center justify-center">
                    <button className="rounded-lg bg-orange-600 w-1/2 h-1/3 hover:bg-orange-400 text-white">{Data.button}</button>
                    <p>{Data.account}<a className="text-orange-600 hover:text-orange-700" href="/register">{Data.signup}</a></p>
                </div>
            </form>
        </div>
    )
}