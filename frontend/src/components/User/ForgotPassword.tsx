"use client"

import { FormEvent, useContext, useEffect, useState } from "react"
import { ForgotPasswordDTO } from "@/ApiCalls/DTOs/User/ForgotPasswordDTO"
import Notification from "../General/Notification"
import UsersHandler from "@/ApiCalls/UsersHandler"
import TranslationLoader from "@/tools/TranslationLoader"
import Link from "next/link"
import ChildContext from "../General/Context"
import { useRouter } from "next/navigation"

export default function ForgotPassword() {
    const [translations, setTranslations] = useState(
        {
            "header": "Forgot Password",
            "email": "Email",
            "example": "example@gmail.com",
            "button": "Submit",
            "account": "You don't have an account?",
            "signup": "Sing up",
            "empty-email": "The email is empty",
            "invalid-email": "The email format is invalid"
        }
    )
    const [email, setEmail] = useState("")
    const [response, setResponse] = useState()
    const [notification, setNotificaiton] = useState()
    const handler = new UsersHandler()
    const router = useRouter()
    const { language } = useContext(ChildContext)

    useEffect(() => {
        async function load() {
            const loader = new TranslationLoader(language, "forgot_password")
            const response = await loader.getTranslatiosn()
            const incoming_data = JSON.parse(response.data)
            setTranslations(incoming_data.translations)
        }
        load()
    }, [language, response])

    async function login(e: FormEvent<HTMLFormElement>) {
        e.preventDefault()
        const data: ForgotPasswordDTO = {
            email: email,
            language: language
        }
        const url = "http://localhost:8000/forgot-password"
        const response = await handler.forgotPassowrd(url, data, translations)
        console.log(response)
        if ("tag" in response) {
            setResponse(response.tag)
            setNotificaiton(response.message)
        }

    }

    return (
        <div className="bg-white w-full h-full flex flex-col items-center justify-center text-black">
            <Notification response={response} notification={notification} />
            <h1 className="text-3xl text-orange-600">{translations?.header}</h1>
            <form
                onSubmit={(e) => { login(e) }}
                className="bg-white border-1 border-gray-200 w-82 h-82 rounded-lg drop-shadow-md">
                <div className="w-full h-2/3 flex flex-col space-y-6 items-center justify-center">
                    <div className="flex flex-col">
                        <label htmlFor="email">{translations.email}</label>
                        <div className="flex w-full border-2 border-solid">
                            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth="1.5" stroke="currentColor" className="size-6 border-r-2 border-black bg-orange-600 text-white">
                                <path strokeLinecap="round" strokeLinejoin="round" d="M21.75 6.75v10.5a2.25 2.25 0 0 1-2.25 2.25h-15a2.25 2.25 0 0 1-2.25-2.25V6.75m19.5 0A2.25 2.25 0 0 0 19.5 4.5h-15a2.25 2.25 0 0 0-2.25 2.25m19.5 0v.243a2.25 2.25 0 0 1-1.07 1.916l-7.5 4.615a2.25 2.25 0 0 1-2.36 0L3.32 8.91a2.25 2.25 0 0 1-1.07-1.916V6.75" />
                            </svg>
                            <input
                                className="pl-2"
                                type="email"
                                name="email"
                                placeholder={translations.example}
                                value={email}
                                onChange={(e) => { setEmail(e.target.value) }} />
                        </div>
                    </div>
                </div>
                <div className="w-full flex flex-col space-y-3 h-1/3 flex items-center justify-center">
                    <button className="rounded-lg bg-orange-600 w-1/2 h-1/3 hover:bg-orange-400 text-white">{translations.button}</button>
                    <p>{translations.account} <Link className="text-orange-600 hover:text-orange-700" href="/register">{translations.signup}</Link></p>
                </div>
            </form>
        </div>
    )
}