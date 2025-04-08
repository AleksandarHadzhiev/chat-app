import { FormEvent, Key, KeyboardEvent, useEffect, useState } from "react"
import UsersHandler from "@/ApiCalls/UsersHandler"
import { VerifyDTO } from "@/ApiCalls/DTOs/User/VerifyDTO"

//@ts-expect-error
// Providing a function and can not specify the type
export default function ProvdeCode({ registration, translations }) {
    const length = process.env.codeLength
    const codeLength = [...Array(Number(length)).keys()]
    const [code, setCode] = useState('')
    const [className, setClassName] = useState('')
    const usersAPI = new UsersHandler()

    useEffect(() => {
        let className = "cursor-not-allowed rounded-lg bg-gray-600 w-1/2 h-1/3 text-black"
        let button = document.getElementById('submit');
        if (code == '') {
            const inputElement = document.getElementById('0');
            inputElement?.focus()
        }
        if (code.length < Number(length)) {
            button?.setAttribute('disabled', '')
        }
        if (code.length == Number(length)) {
            className = "rounded-lg bg-orange-600 w-1/2 h-1/3 hover:bg-orange-400 text-white cursort-pointer"
            button?.removeAttribute('disabled')
        }
        setClassName(className)

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

    function goBack(e: KeyboardEvent<HTMLInputElement>) {
        e.preventDefault()
        const key = e.key;
        const id = e.currentTarget.id
        const index = Number(id)
        let next = String(index)
        let _code = code
        const isLetter = (/[a-zA-Z]/).test(key) && key.length == 1
        if (isLetter) {
            next = String(index + 1)
            if (code.length == Number(length)) {
                _code = code.slice(0, -1)
            }
            _code += key
        }
        else if (key == "Backspace") {
            next = String(index - 1)
            _code = code.slice(0, -1)
        }
        setCode(_code)
        const inputElement = document.getElementById(next);
        inputElement?.focus()
    }

    return (
        <form onSubmit={(e) => { verify(e) }} className="bg-white border-1 border-gray-200 w-82 h-82 rounded-lg drop-shadow-md">
            <div className="w-full h-1/2 flex flex-col items-center justify-center">
                <div className="flex flex-col space-y-3 mt-12">
                    <label>{translations.code}</label>
                    <div id="code" className="flex w-full space-x-3">
                        {
                            codeLength.map((index: Key) => (
                                <input
                                    key={index}
                                    id={String(index)}
                                    className="w-12 h-12 bg-white border-2 border-black text-center text-orange-600"
                                    type="text"
                                    name="digit"
                                    value={code[Number(index)] ? code[Number(index)] : ""}
                                    onKeyDown={(e) => { goBack(e) }} />
                            ))}
                    </div>
                </div>
            </div>
            <div className="w-full flex flex-col space-y-3 h-1/3 flex items-center justify-center">
                <button id="submit" className={className}>{translations.button}</button>
            </div>
        </form>

    )
}