import UsersHandler from "@/ApiCalls/UsersHandler"
import { FormEvent, useContext, useEffect, useState } from "react"
import ChildContext from "../General/Context"
import TranslationLoader from "@/tools/TranslationLoader"
import Notification from "../General/Notification"
import { useSearchParams } from "next/navigation"
import { useRouter } from "next/navigation"
import Link from "next/link"
import { ResetPasswordDTO } from "@/ApiCalls/DTOs/User/ResetPassword"

export default function ResetPassword() {
    const params = useSearchParams()
    const router = useRouter()
    const [translations, setTranslations] = useState({
        "header": "Reset Password",
        "password": "Password",
        "button": "Submit",
        "account": "You don't have an account?",
        "signup": "Sing up",
    })

    const { language } = useContext(ChildContext)
    const [code, setCode] = useState('')
    const [email, setEmail] = useState('')

    const [response, setResponse] = useState("")
    const [notification, setNotificaiton] = useState("")
    const usersAPI = new UsersHandler()

    useEffect(() => {
        const code = params.get("code")
        const email = params.get("email")
        if (email) setEmail(email)
        if (code) setCode(code)
        async function load() {
            const loader = new TranslationLoader(language, "reset_password")
            const response = await loader.getTranslatiosn()
            const incoming_translations = JSON.parse(response.data)
            setTranslations(incoming_translations.translations)
        }

        async function checkIfAuthorized() {
            const url = `http://localhost:8000/${code}/${email}`
            const response = await usersAPI.checkIfAuthorized(url, translations)
            if ("tag" in response) {
                setResponse(response.tag)
                setNotificaiton(response.message)
            }
            else {
                router.push('/login')
            }
        }
        checkIfAuthorized()
        load()
    }, [language, response])
    const [password, setPassword] = useState('')
    async function login(e: FormEvent<HTMLFormElement>) {
        e.preventDefault()
        const data: ResetPasswordDTO = {
            email: email,
            code: code,
            password: password,

        }
        const url = "http://localhost:8000/reset-password"
        const response = await usersAPI.resetPassword(url, data, translations)
        if ("tag" in response) {
            setResponse(response.tag)
            setNotificaiton(response.message)
        }
        else {
            router.push('/login')
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
                    <div className="flex flex-col">
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
                                onChange={(e) => { setPassword(e.target.value) }} />
                        </div>
                    </div>
                    <div className="flex">
                        <p>{translations["forgot-password"]} <Link className="text-orange-600 hover:text-orange-700" href="/forgot-password">{translations.here}</Link></p>
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