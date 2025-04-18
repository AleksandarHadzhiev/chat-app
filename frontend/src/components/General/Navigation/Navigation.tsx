'use client'

import { redirect } from "next/navigation"
import SmallNavigation from "./SmallNavigation"
import { useEffect, useState } from "react"
import FullWidthNavigation from "./FullWidthNavigation"
import MobileNavigation from "./MobileNavigation"
import { useRouter } from "next/navigation"

//@ts-expect-error
// Providing a function and can not specify the type
export default function Navigation({ setLanguage, isVisible, setIsVisible, widthType }) {
    const router = useRouter()
    function goBackToHomepage() {
        router.push('/')
    }

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
                            setLanguage={setLanguage} />
                    ) :
                    widthType == "short" ?
                        (
                            <SmallNavigation
                                setLanguage={setLanguage}
                                setIsVisible={setIsVisible}
                                isVisible={isVisible} />
                        ) :
                        (
                            <MobileNavigation />
                        )
            }
        </nav>
    )
}