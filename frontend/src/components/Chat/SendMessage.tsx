import { ChangeEvent, MouseEvent, useState } from "react"

//@ts-expect-error
// Providing a function and can not specify the type
export function SendMessage({ socket, user, group }) {

    const [message, setMessage] = useState<{
        content: String,
        groupId: Number,
        author: String,
        userId: Number
    }>()

    function send(e: MouseEvent<HTMLButtonElement, globalThis.MouseEvent>) {
        e.preventDefault()
        socket.send(JSON.stringify(message))
    }

    function updateMessage(e: ChangeEvent<HTMLInputElement>) {
        e.preventDefault()
        setMessage({
            content: e.target.value,
            groupId: group.id,
            author: user.username,
            userId: user.id,
        })
    }

    return (
        <div className="flex w-full h-1/10 drop-shadow-md border-t-2 border-gray-200">
            <div className="w-1/30 h-full flex items-center justify-center text-black hover:text-orange-500 hover:drop-shadow-md">
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth="1.5" stroke="currentColor" className="size-6">
                    <path strokeLinecap="round" strokeLinejoin="round" d="m18.375 12.739-7.693 7.693a4.5 4.5 0 0 1-6.364-6.364l10.94-10.94A3 3 0 1 1 19.5 7.372L8.552 18.32m.009-.01-.01.01m5.699-9.941-7.81 7.81a1.5 1.5 0 0 0 2.112 2.13" />
                </svg>
            </div>
            <input
                className="w-28/30 h-full pl-2 focus:outline-none"
                placeholder="Write a message..."
                onChange={(e) => { updateMessage(e) }}
            />
            <button
                onClick={(e) => { send(e) }}
                className="w-1/30 h-full flex items-center justify-center text-orange-500 hover:text-orange-300 hover:drop-shadow-md">
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth="1.5" stroke="currentColor" className="size-6">
                    <path strokeLinecap="round" strokeLinejoin="round" d="M6 12 3.269 3.125A59.769 59.769 0 0 1 21.485 12 59.768 59.768 0 0 1 3.27 20.875L5.999 12Zm0 0h7.5" />
                </svg>
            </button>
        </div >
    )
}