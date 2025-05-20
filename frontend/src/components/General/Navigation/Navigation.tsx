'use client'

import SmallNavigation from "./SmallNavigation"
import { useEffect, useState } from "react"
import FullWidthNavigation from "./FullWidthNavigation"
import MobileNavigation from "./MobileNavigation"
import { useRouter } from "next/navigation"
import TranslationLoader from "@/tools/TranslationLoader"

//@ts-expect-error
// Providing a function and can not specify the type
export default function Navigation({ setLanguage, isVisible, setIsVisible, widthType, _language }) {
    const router = useRouter()
    const [translations, setTranslations] = useState({
        home: "Home",
        account: "Account",
        groups: "Groups",
        login: "Login"
    })
    function goBackToHomepage() {
        router.push('/')
    }
    useEffect(() => {
        async function load() {
            const ln = _language
            const loader = new TranslationLoader(ln, "navigation")
            const response = await loader.getTranslatiosn()
            const incoming_data = JSON.parse(response.data)
            setTranslations(incoming_data.translations)
        }
        load()
    }, [_language])

    function goToLogin() {
        router.push('/login')
    }

    return (
        <nav className="flex space-x-3 w-full bg-white h-1/10 border-1 border-gray-400 hover:text-orange-300 text-orange-600">
            {
                widthType == "desktop" ?
                    (
                        <FullWidthNavigation
                            goBackToHomepage={goBackToHomepage}
                            goToLogin={goToLogin}
                            setLanguage={setLanguage}
                            translations={translations} />
                    ) :
                    widthType == "short" ?
                        (
                            <SmallNavigation
                                setLanguage={setLanguage}
                                setIsVisible={setIsVisible}
                                isVisible={isVisible}
                                translations={translations} />
                        ) :
                        (
                            <MobileNavigation
                                setIsVisible={setIsVisible}
                                isVisible={isVisible} />
                        )
            }
        </nav>
    )
}