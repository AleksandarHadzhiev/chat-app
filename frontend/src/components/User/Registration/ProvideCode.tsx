import { ChangeEvent, FormEvent, Key, useContext, useEffect, useState } from "react"
import UsersHandler from "@/ApiCalls/UsersHandler"
import ChildContext from "@/components/General/Context"
import translationLoader from "@/tools/TranslationLoader"
import Data from "../../../dictionaries/NL/registration.json"
import { VerifyDTO } from "@/ApiCalls/DTOs/User/VerifyDTO"

//@ts-expect-error
// Providing a function and can not specify the type
export default function ProvdeCode({ registration }) {

    const [data, setData] = useState(Data)

    const { language } = useContext(ChildContext)
    useEffect(() => {
        async function load() {
            const data = await await new translationLoader().translationLoader(language, "registration.json")
            setData(data)
        }
        load()
    }, [language])
    const codeLength = [...Array(Number(process.env.codeLength))]
    const [code, setCode] = useState('')
    const [className, setClassName] = useState('')
    const usersAPI = new UsersHandler()

    useEffect(() => {
        if (code.length === 0) {
            const inputElement = document.getElementById('0');
            inputElement?.focus()
        }
        if (code.length < 4) {
            const button = document.getElementById('submit');
            const newClassName = "cursor-not-allowed rounded-lg bg-gray-600 w-1/2 h-1/3 text-black"
            setClassName(newClassName)
            button?.setAttribute('disabled', '')
        }
        if (code.length == 4) {
            const button = document.getElementById('submit');
            const newClassName = "rounded-lg bg-orange-600 w-1/2 h-1/3 hover:bg-orange-400 text-white cursort-pointer"
            setClassName(newClassName)
            button?.removeAttribute('disabled')
        }

    }, [code])


    function verify(e: FormEvent<HTMLFormElement>) {
        e.preventDefault()
        const email = localStorage.getItem("email")
        if (email) {
            const data: VerifyDTO = {
                email: email,
                code: code
            }
            usersAPI.verify("http://localhost:8000/verification", data)
            registration(e)
        }

    }

    function updateValue(e: ChangeEvent<HTMLInputElement>) {
        e.preventDefault()
        const id = e.target.id
        const index = Number(id)
        codeLength[Number(index)] = e.target.value
        setCode(code + e.target.value)
        const next = String(index + 1)
        const inputElement = document.getElementById(next);
        inputElement?.focus()
    }

    return (
        <form onSubmit={(e) => { verify(e) }} className="bg-white border-1 border-gray-200 w-82 h-82 rounded-lg drop-shadow-md">
            <div className="w-full h-1/2 flex flex-col items-center justify-center">
                <div className="flex flex-col space-y-3 mt-12">
                    <label>{data.code}</label>
                    <div className="flex w-full space-x-3">
                        {
                            codeLength.map((index: Key) => (
                                <input
                                    key={index}
                                    id={String(index)}
                                    className="w-12 h-12 bg-white border-2 border-black text-center text-orange-600"
                                    type="text"
                                    name="digit"
                                    value={codeLength[Number(index)]}
                                    onChange={(e) => { updateValue(e) }} />
                            ))}
                    </div>
                </div>
            </div>
            <div className="w-full flex flex-col space-y-3 h-1/3 flex items-center justify-center">
                <button id="submit" className={className}>{data.button}</button>
            </div>
        </form>

    )
}