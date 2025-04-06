import { FormEvent, useState } from "react"
import RegistrationSteps from "./RegistrationSteps"
import ProvdeUserData from "./ProvideUserData"
import ProvdeCode from "./ProvideCode"
import Confirmation from "./Confirmation"
import { redirect } from 'next/navigation'

export default function Register() {
    const [step, setStep] = useState(1)
    function registration(e: FormEvent<HTMLFormElement>) {
        e.preventDefault()
        setStep(step + 1)
    }

    if (step === 3) {
        setTimeout(() => {
            redirect("/")
        }, 1500);
    }
    return (
        <div className="bg-white w-full h-full flex flex-col items-center justify-center text-black space-y-4">
            <RegistrationSteps step={step} />
            {
                step === 1 ? < ProvdeUserData registration={registration} /> :
                    step === 2 ? <ProvdeCode registration={registration} /> : <Confirmation />
            }
        </div>
    )
}