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
    const [ln, setLanguage] = useState('NL')
    const [socket, setSocket] = useState<WebSocket | null>()

    useEffect(() => {

        function setSize() {
            if (window.innerWidth < 600) {
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
    }, [ln])

    return (
        <main className="w-full h-screen bg-white">
            <Navigation _language={ln} widthType={widthType} setLanguage={setLanguage} isVisible={isVisible} setIsVisible={setIsVisible} />
            {
                widthType == "desktop" ? (
                    <div className="w-full h-9/10 flex flex-col items-center justify-center text-black">
                        {
                            <ChildContext.Provider value={{ language: ln, isVisible: isVisible, widthType: widthType, socket: socket }}>
                                {children}
                            </ChildContext.Provider>
                        }
                    </div>
                ) : widthType == "short" ? (
                    <div className="w-full h-9/10 flex">
                        <div className={isVisible ? "w-1/3 h-full bg-white border-r-2 border-gray-400" : "hidden"}>
                            <Dropdown _language={ln} setIsVisible={setIsVisible} />
                        </div>
                        <div className={isVisible ? "w-2/3 h-full " : "w-full h-full text-black"}>
                            <ChildContext.Provider value={{ language: ln, isVisible: isVisible, widthType: widthType }}>
                                {children}
                            </ChildContext.Provider>
                        </div>
                    </div>
                ) :
                    (
                        <div className="w-full h-9/10 flex">
                            <div className={isVisible ? "w-2/3 h-full bg-white border-r-2 border-gray-400" : "hidden"}>
                                <Dropdown _language={ln} setIsVisible={setIsVisible} />
                            </div>
                            <div className={isVisible ? "hidden " : "w-full h-full text-black"}>
                                <ChildContext.Provider value={{ language: ln, isVisible: isVisible, widthType: widthType }}>
                                    {children}
                                </ChildContext.Provider>
                            </div>
                        </div>
                    )
            }
        </main>
    )
}
