"use client"

import { useEffect, useState } from "react";
import Navigation from "./Navigation/Navigation";
import React from "react";
import ChildContext from "./Context";
import Dropdown from "./Navigation/Dropdown";



//@ts-expect-error
// Providing a function and can not specify the type
export function Layout({ children }) {

    const [isVisible, setIsVisible] = useState(false)
    const [widthType, setWidthType] = useState("desktop")


    useEffect(() => {

        function setSize() {
            if (window.innerWidth < 450) {
                setWidthType("mobile")
            }
            else if (window.innerWidth < 850) {
                setWidthType("short")
            }
            else {
                setWidthType("desktop")
            }
        }

        window.addEventListener('resize', () => {
            setSize()
        })

        setSize()
    }, [])


    const [ln, setLanguage] = useState('NL')
    return (
        <main className="w-full h-screen bg-white">
            <Navigation widthType={widthType} setLanguage={setLanguage} isVisible={isVisible} setIsVisible={setIsVisible} />
            {
                widthType == "desktop" ? (
                    <div className="w-full h-9/10 flex flex-col items-center justify-center text-black">
                        {
                            <ChildContext.Provider value={{ language: ln, isVisible: isVisible }}>
                                {children}
                            </ChildContext.Provider>
                        }
                    </div>
                ) :
                    (
                        <div className="w-full h-9/10 flex">
                            <div className={isVisible ? "w-1/3 h-full bg-white border-r-2 border-gray-400" : "hidden"}>
                                <Dropdown setIsVisible={setIsVisible} />
                            </div>
                            <div className={isVisible ? "w-2/3 h-full " : "w-full h-full text-black"}>
                                <ChildContext.Provider value={{ language: ln, isVisible: isVisible }}>
                                    {children}
                                </ChildContext.Provider>
                            </div>
                        </div>
                    )
            }
        </main>
    )
}
