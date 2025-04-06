import { Key, MouseEvent } from "react"
import Language from "./Languages/Language"

//@ts-expect-error
// Providing a function and can not specify the type
export default function LanguageDropDown({ setLn, setLanguage }) {
    const supportedLanguages = ["English", "Dutch"]
    function pickLanguage(e: MouseEvent<HTMLDivElement, globalThis.MouseEvent>) {
        const language = e.currentTarget.children[0].children[1].textContent
        setLanguage(language)
    }
    return (
        <div className="w-full h-full flex flex-col rounded-lg" id="languages">
            {
                supportedLanguages.map((language: string, index: Key) => (
                    <div key={index} className="w-full h-full flex">
                        <Language language={language} pickLanguage={pickLanguage} setLn={setLn} />
                    </div>
                ))}
        </div>
    )
}