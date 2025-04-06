import ChildContext from "@/components/General/Context"
import translationLoader from "@/tools/TranslationLoader"
import { useContext, useEffect, useState } from "react"
import Data from "../../../dictionaries/NL/registration.json"
//@ts-expect-error
// Providing a function and can not specify the type
export default function RegistrationSteps({ step }) {

    const [data, setData] = useState(Data)

    const { language } = useContext(ChildContext)
    useEffect(() => {
        async function load() {
            const data = await await new translationLoader().translationLoader(language, "registration.json")
            setData(data)
        }
        load()
    }, [language])

    const focus = "w-12 h-1 bg-orange-600"
    const notFocused = "w-12 h-1 bg-orange-300"
    const focusArrow = "size-12 text-orange-600"
    const notFocusedArrow = "size-12 text-orange-300"
    return (
        <div className="flex w-full items-center justify-center space-x-2">
            <div className="text-orange-600">
                <h3>{data.stepOne}</h3>
            </div>
            <div className="flex items-center justify-center">
                <div className={step < 2 ? notFocused : focus}></div>
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth="1.5" stroke="currentColor" className={step < 2 ? notFocusedArrow : focusArrow}>
                    <path strokeLinecap="round" strokeLinejoin="round" d="m8.25 4.5 7.5 7.5-7.5 7.5" />
                </svg>
            </div>
            <div className={step < 2 ? "text-orange-300" : "text-orange-600"}>
                <h3>{data.stepTwo}</h3>
            </div>
            <div className="flex items-center justify-center">
                <div className={step < 3 ? notFocused : focus}></div>
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth="1.5" stroke="currentColor" className={step < 3 ? notFocusedArrow : focusArrow}>
                    <path strokeLinecap="round" strokeLinejoin="round" d="m8.25 4.5 7.5 7.5-7.5 7.5" />
                </svg>
            </div>
            <div className={step < 3 ? "text-orange-300" : "text-orange-600"}>
                <h3>{data.stepThree}</h3>
            </div>
        </div>
    )
}