import { FormEvent, MouseEvent, useState } from "react"
import RegistrationSteps from "./RegistrationSteps"
import ProvdeEmail from "./ProvideEmail"
import ProvdeCode from "./ProvideCode"
import ProvdePassword from "./ProvidePassword"
import ProvdeUsername from "./ProvideUsername"
import Confirmation from "./Confirmation"
export default function Register() {
    const [step, setStep] = useState(1)
    function registration(e: FormEvent<HTMLFormElement>) {
        e.preventDefault()
        setStep(step + 1)
    }
    return (
        <div className="bg-white w-full h-full flex flex-col items-center justify-center text-black space-y-4">
            <RegistrationSteps step={step} />
            <form onSubmit={(e) => { registration(e) }} className="bg-gray-200 w-82 h-82 rounded-lg">
                {
                    step === 1 ? < ProvdeEmail /> :
                        step === 2 ? <ProvdeCode /> :
                            step === 3 ? <ProvdePassword /> :
                                step === 4 ? <ProvdeUsername /> : <Confirmation />
                }
                <div className="w-full flex flex-col space-y-3 h-1/2 flex items-center justify-center">
                    <button className="rounded-lg bg-orange-600 w-1/2 h-1/3 hover:bg-orange-400 text-white">Continue</button>
                    <p>You have an account? <a className="text-orange-600 hover:text-orange-700" href="/">Sign in</a></p>
                </div>
            </form>
        </div>
    )
}