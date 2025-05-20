"use client"

import { ChangeEvent, MouseEvent, useState } from "react"
import MessagesHandler from "@/ApiCalls/MessagesHandler"
//@ts-expect-error
// Providing a function and can not specify the type
export default function RefactorMessageContent({ code, setEditMessage, message, setTriggerOff, trigger, socket, translations, widthType }) {

    const [content, setContent] = useState(message)
    const handler = new MessagesHandler()
    function updateMessage(e: ChangeEvent<HTMLTextAreaElement>) {
        e.preventDefault()
        setContent(e.target.value)
    }

    async function send(e: MouseEvent<HTMLButtonElement, globalThis.MouseEvent>) {
        e.preventDefault()
        const requestBody = {
            content: content,
            code: code
        }
        const url = `http://localhost:8000/messages/`
        const response = await handler.editAMessage(url, requestBody, translations)
        if ("tag" in response && response.tag == "success") {
            setEditMessage(false)
            const message = document.getElementById(`${code}`)
            if (message)
                message.textContent = content

            setTriggerOff(!trigger)
            const notification = {
                type: "notification",
                data: {
                    action: "updated"
                }
            }
            socket.send(JSON.stringify(notification))
        }
    }

    return (
        <div className={`${widthType == "mobile" ? "text-2xl" : ""} flex w-full h-1/10 drop-shadow-md border-t-2 border-gray-200`}>
            <div className={`${widthType == "mobile" ? 'w-3/30' : "1/30"} h-full flex items-center justify-center text-black hover:text-orange-500 hover:drop-shadow-md`}>
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth="1.5" stroke="currentColor" className={`${widthType == "mobile" ? 'size-12' : "size-6"} ml-1`}>
                    <path strokeLinecap="round" strokeLinejoin="round" d="m18.375 12.739-7.693 7.693a4.5 4.5 0 0 1-6.364-6.364l10.94-10.94A3 3 0 1 1 19.5 7.372L8.552 18.32m.009-.01-.01.01m5.699-9.941-7.81 7.81a1.5 1.5 0 0 0 2.112 2.13" />
                </svg>
            </div>
            <textarea
                id="msg-input"
                className={`w-[90%] flex flex-col h-full pt-6 pl-3`}
                placeholder={translations.write}
                value={String(content).replace("<br/>", "")}
                onChange={(e) => { updateMessage(e) }}
            />
            <button
                onClick={(e) => { send(e) }}
                className={`${widthType == "mobile" ? 'w-3/30' : "1/30"} h-full flex items-center justify-center text-orange-500 hover:text-orange-300 hover:drop-shadow-md`}>
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth="1.5" stroke="currentColor" className={`${widthType == "mobile" ? 'size-12' : "size-6"} ml-1`}>
                    <path strokeLinecap="round" strokeLinejoin="round" d="M6 12 3.269 3.125A59.769 59.769 0 0 1 21.485 12 59.768 59.768 0 0 1 3.27 20.875L5.999 12Zm0 0h7.5" />
                </svg>
            </button>
        </div >
    )
}