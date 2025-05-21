import { ChangeEvent, MouseEvent, useState } from "react"
import { MessageDTO } from "@/ApiCalls/DTOs/Other/MessageDTO"
import MessagesHandler from "@/ApiCalls/MessagesHandler"
//@ts-expect-error
// Providing a function and can not specify the type
export function SendMessage({ widthType, socket, user, group, setIsWriting, setTriggerOff, trigger, translations }) {

    const handler = new MessagesHandler()

    const [message, setMessage] = useState<{
        type: String,
        data: MessageDTO
    }>()

    async function send(e: MouseEvent<HTMLButtonElement, globalThis.MouseEvent>) {
        e.preventDefault()
        if (message != undefined) {
            const isSend = handler.createMessage(message, socket)
            if (isSend) {
                setTriggerOff(!trigger)
            }
        }
    }

    function updateMessage(e: ChangeEvent<HTMLTextAreaElement>) {
        e.preventDefault()
        setMessage({
            type: "message",
            data: {
                content: e.target.value,
                group_id: group.id,
                author: user.username,
                user_id: user.id,
                code: "1",
                created_at: "",
            }
        })
    }

    function notifyChatMembersThatSomeoneIsWriting() {
        setIsWriting(true)
        const notification = {
            type: "notification",
            data: {
                user: user.username,
                action: "writing",
                group: group.id
            }
        }
        socket.send(JSON.stringify(notification))
    }

    function notifyChatMembersThatSomeoneStoppedWriting() {
        setIsWriting(false)
        const notification = {
            type: "notification",
            data: {
                user: user.username,
                action: "stopped",
                group: group.id
            }
        }
        socket.send(JSON.stringify(notification))
    }

    return (
        <div className={`${widthType == "mobile" ? 'text-2xl' : 'text-base'} flex w-full h-1/10 drop-shadow-md border-t-2 border-gray-200`}>
            <div className={`${widthType == "mobile" ? 'w-3/30' : "1/30"} h-full flex items-center justify-center text-black hover:text-orange-500 hover:drop-shadow-md`}>
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth="1.5" stroke="currentColor" className={`${widthType == "mobile" ? 'size-12' : "size-6"}`}>
                    <path strokeLinecap="round" strokeLinejoin="round" d="m18.375 12.739-7.693 7.693a4.5 4.5 0 0 1-6.364-6.364l10.94-10.94A3 3 0 1 1 19.5 7.372L8.552 18.32m.009-.01-.01.01m5.699-9.941-7.81 7.81a1.5 1.5 0 0 0 2.112 2.13" />
                </svg>
            </div>
            <textarea
                id="msg-input"
                className={`resize-none w-[90%] h-full pt-6 pl-3 focus:outline-none`}
                placeholder={translations.write}
                onFocus={() => { notifyChatMembersThatSomeoneIsWriting() }} // Change to initiate a message via WS -> notify the users that someone is writing in the chat.
                onBlur={() => { notifyChatMembersThatSomeoneStoppedWriting() }} // Change to initiate a message via WS -> notify the users that someone stopped writing
                onChange={(e) => { updateMessage(e) }}
            />
            <button
                onClick={(e) => { send(e) }}
                className={`${widthType == "mobile" ? 'w-3/30' : "1/30"} h-full flex items-center justify-center text-orange-500 hover:text-orange-300 hover:drop-shadow-md`}>
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth="1.5" stroke="currentColor" className={`${widthType == "mobile" ? 'size-12' : "size-6"}`}>
                    <path strokeLinecap="round" strokeLinejoin="round" d="M6 12 3.269 3.125A59.769 59.769 0 0 1 21.485 12 59.768 59.768 0 0 1 3.27 20.875L5.999 12Zm0 0h7.5" />
                </svg>
            </button>
        </div >
    )
}

