'use client'
import LanguageDropDown from "./LanguageDropDown"
import { useState } from "react"


//@ts-expect-error
// Providing a function and can not specify the type
export default function LanguagePicker({ setLanguage }) {
    const [isVisible, setIsVisible] = useState(false)
    const [ln, setLn] = useState("<p>Loading...</p>")
    return (
        <div
            onClick={() => { setIsVisible(!isVisible) }}
            className="flex w-28 h-12 flex border-2 border-black rounded-lg hover:bg-gray-400">
            <div className="w-2/3 h-full flex flex-col items-center justify-center text-black">
                <div className="w-full h-full flex pl-2">
                    <div className="w-full h-full text-black flex items-center justify-center" dangerouslySetInnerHTML={{ __html: ln }}></div>
                </div>
                <div className={isVisible ? "visible bg-gray-200 mt-20 border-2 border-black w-full" : "hidden"}>
                    <LanguageDropDown setLn={setLn} setLanguage={setLanguage} />
                </div>
            </div>
            <div className="flex items-center justify-center border-black border-l-2 w-1/3 h-full text-black">
                {isVisible ? (<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth="1.5" stroke="currentColor" className="size-6">
                    <path strokeLinecap="round" strokeLinejoin="round" d="m4.5 15.75 7.5-7.5 7.5 7.5" />
                </svg>
                ) : (
                    < svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth="1.5" stroke="currentColor" className="size-6">
                        <path strokeLinecap="round" strokeLinejoin="round" d="m19.5 8.25-7.5 7.5-7.5-7.5" />
                    </svg>)}
            </div>
        </div >
    )
}





