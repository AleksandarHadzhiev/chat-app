"use client"

import { useState } from "react";
import Navigation from "./Navigation";
import React from "react";
import ChildContext from "./Context";



//@ts-expect-error
// Providing a function and can not specify the type
export function Layout({ children }) {
    const [ln, setLanguage] = useState('NL')
    return (
        <main className="w-full h-screen bg-white">
            <Navigation setLanguage={setLanguage} />
            <div className="w-full h-9/10 flex flex-col items-center justify-center text-black">
                {
                    <ChildContext.Provider value={{ language: ln }}>
                        {children}
                    </ChildContext.Provider>
                }
            </div>
        </main>
    )
}