"use client"

import LanguagePicker from "../LanguagePicker"

//@ts-expect-error
// Providing a function and can not specify the type
export default function SmallNavigation({ setLanguage, setIsVisible, isVisible }) {
    return (
        <div className="w-full h-full flex bg-white items-center justify-center">
            <div className="w-5/7 h-full flex flex-col">
                <button onClick={() => { setIsVisible(!isVisible) }} className="w-1/20 h-full text-black hover:text-orange-600">
                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth="1.5" stroke="currentColor" className="size-6">
                        <path strokeLinecap="round" strokeLinejoin="round" d="M3.75 6.75h16.5M3.75 12h16.5m-16.5 5.25h16.5" />
                    </svg>
                </button>
            </div>
            <div className="h-full w-2/7 mt-4 mr-2">
                <LanguagePicker setLanguage={setLanguage} />
            </div>
        </div>
    )
}