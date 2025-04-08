'use client'

import { Key, MouseEvent, useEffect, useState } from "react"

import axios from "axios"

async function getLanguages() {
    return await axios.get("http://localhost:8000/languages")
}

//@ts-expect-error
// Providing a function and can not specify the type
export default function LanguageDropDown({ setLn, setLanguage }) {
    const [languages, setLanguages] = useState([])
    const [isFetched, setIsFetched] = useState(false)
    useEffect(() => {
        async function load() {
            const response = await getLanguages()
            const incoming_data = JSON.parse(response.data)
            setIsFetched(true)
            setLanguages(incoming_data.languages)
            setLn(incoming_data.languages[0])
        }

        load()
    }, [isFetched])
    function pickLanguage(e: MouseEvent<HTMLDivElement, globalThis.MouseEvent>) {
        const language = e.currentTarget.children[1].textContent
        setLanguage(language)
        setLn(e.currentTarget.innerHTML)
    }
    return (
        <div className="w-full h-full flex flex-col rounded-lg" id="languages">
            {
                languages.map((language: string, index: Key) => (
                    <div key={index} className="w-full h-full flex-col">
                        <div className="w-full h-full text-black flex items-center justify-center hover:bg-gray-400" onClick={(e) => { pickLanguage(e) }} dangerouslySetInnerHTML={{ __html: language }}></div>
                        <div className="w-full h-[2px] bg-gray-700"></div>
                    </div>
                ))}
        </div>
    )
}