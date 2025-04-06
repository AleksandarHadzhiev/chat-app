import English from "./Languages/English"
import Dutch from "./Languages/Dutch"
import { MouseEvent } from "react"

//@ts-ignore
export default function LanguageDropDown({ setLn, setLanguage }) {
    function pickLanguage(e: MouseEvent<HTMLDivElement, globalThis.MouseEvent>) {

        const target = e.currentTarget.children[0].children[1].textContent
        if (target == "EN") {
            setLn(English)
            setLanguage(target)
        }
        else if (target == "NL") {
            setLn(Dutch)
            setLanguage(target)
        }

    }
    return (
        <div className="w-full h-full flex flex-col rounded-lg" id="languages">
            <div onClick={(e) => { pickLanguage(e) }} className="w-full h-full flex hover:bg-gray-400">
                <Dutch />
            </div>
            <div className="w-full h-1 bg-black"></div>
            <div onClick={(e) => { pickLanguage(e) }} className="w-full h-full flex hover:bg-gray-400">
                <English />
            </div>
        </div>
    )
}