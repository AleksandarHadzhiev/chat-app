import { FormEvent, useContext, useEffect, useState } from "react"
import RegistrationSteps from "./RegistrationSteps"
import ProvdeUserData from "./ProvideUserData"
import ProvdeCode from "./ProvideCode"
import Confirmation from "./Confirmation"
import { redirect } from 'next/navigation'

import ChildContext from "@/components/General/Context"
import TranslationLoader from "@/tools/TranslationLoader"
import Data from "../../../dictionaries/NL/registration.json"

export default function Register() {
    const [step, setStep] = useState(1)
    function registration(e: FormEvent<HTMLFormElement>) {
        e.preventDefault()
        setStep(step + 1)
    }

    const [data, setData] = useState(Data)

    const { language } = useContext(ChildContext)
    useEffect(() => {
        async function load() {
            const loader = new TranslationLoader(language, "registration")
            const response = await loader.getTranslatiosn()
            const incoming_data = JSON.parse(response.data)
            if (incoming_data && incoming_data.translations.accountOne != Data.account)
                setData(incoming_data.translations)
        }
        load()
    }, [language, Data])

    if (step === 3) {
        setTimeout(() => {
            redirect("/")
        }, 1500);
    }
    return (
        <div className="bg-white w-full h-full flex flex-col items-center justify-center text-black space-y-4">
            <RegistrationSteps step={step} translations={data} />
            {
                step === 1 ? < ProvdeUserData registration={registration} translations={data} /> :
                    step === 2 ? <ProvdeCode registration={registration} translations={data} /> : <Confirmation translations={data} />
            }
        </div>
    )
}