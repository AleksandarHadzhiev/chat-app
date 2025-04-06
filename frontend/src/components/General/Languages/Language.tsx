import languageLoader from "@/tools/languages"
import { MouseEvent } from "react"

//@ts-expect-error
// Providing a function and can not specify the type
export default function Language({ language, pickLanguage, setLn }) {
    const Element = languageLoader(language)
    function pick(e: MouseEvent<HTMLDivElement, globalThis.MouseEvent>) {
        setLn(Element)
        pickLanguage(e)
    }
    return (
        <div onClick={(e) => { pick(e) }} className="w-full h-full text-black flex flex-col items-center justify-center hover:bg-gray-400">
            <Element />
            <div className="w-full h-[2px] bg-gray-700"></div>
        </div >
    )
}