import { FormEvent, useContext, useEffect, useState } from "react"
import RegistrationSteps from "./RegistrationSteps"
import ProvdeUserData from "./ProvideUserData"
import ProvdeCode from "./ProvideCode"
import Confirmation from "./Confirmation"
import { useRouter } from "next/navigation"

import ChildContext from "@/components/General/Context"
import TranslationLoader from "@/tools/TranslationLoader"
import Notification from "@/components/General/Notification"

export default function Register() {
    const router = useRouter()
    const [step, setStep] = useState(1)
    const [response, setResponse] = useState("")
    const [notification, setNotificaiton] = useState("")
    function registration(e: FormEvent<HTMLFormElement>, response: string, notification: string) {
        e.preventDefault()
        setNotificaiton(notification)
        setResponse(response)

        if (response != "") {
            if (response == "success")
                setStep(step + 1)
            setTimeout(() => {
                setResponse('')
            }, 3000);
        }
    }

    const [data, setData] = useState({
        stepOne: "",
        stepTwo: "",
        stepThree: "",
    })

    const { language, widthType } = useContext(ChildContext)
    useEffect(() => {
        async function load() {
            const loader = new TranslationLoader(language, "registration")
            const response = await loader.getTranslatiosn()
            const incoming_data = JSON.parse(response.data)
            setData(incoming_data.translations)
        }
        load()
    }, [language, response])

    if (step === 3) {
        setTimeout(() => {
            router.push('/login')
        }, 1500);
    }
    return (
        <div className="bg-white w-full h-full flex flex-col items-center justify-center text-black space-y-4">
            <Notification notification={notification} response={response} />
            <RegistrationSteps step={step} translations={data} widthType={widthType} />
            {
                step === 1 ? < ProvdeUserData language={language} registration={registration} translations={data} /> :
                    step === 2 ? <ProvdeCode registration={registration} translations={data} /> : <Confirmation translations={data} />
            }
        </div>
    )
}