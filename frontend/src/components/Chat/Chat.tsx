import axios from "axios"
import { useEffect, useState } from "react"
import MessagesHandler from "@/ApiCalls/MessagesHandler"

//@ts-expect-error
// Providing a function and can not specify the type
export default function Chat({ widthType, _group, changeChat, isVisible, triggerLastMessage }) {
    const [lastMessage, setLastMesage] = useState({ content: String("Last message"), created_at: String("Date") })
    const [date, setDate] = useState("")
    const handler = new MessagesHandler()
    async function getLastMessage() {
        const message = await handler.getLastMessage(_group.id)
        if (message && message.length > 0) {
            setFormatForDate(message[0].created_at)
            setLastMesage(message[0])
        }
    }

    function setFormatForDate(unformatedDate: string) {
        const date = new Date(unformatedDate)
        const timeElapsed = Date.now();
        const today = new Date(timeElapsed);
        let formatedDate = ""
        const difference = calculateDayDifference(date, today)
        if (difference > 0) {
            formatedDate = `${date.toLocaleDateString()}`
        }
        else {
            const unformatedMinutes = date.getMinutes()
            const minutes = unformatedMinutes < 10 ? `0${unformatedMinutes}` : unformatedMinutes
            formatedDate = `${date.getHours()}:${minutes}`
        }
        setDate(formatedDate)
    }

    function calculateDayDifference(dateSend: any, today: any) {
        let timeDifference = today - dateSend;
        let daysDifference = timeDifference / (1000 * 3600 * 24);
        return Math.round(daysDifference);
    }

    useEffect(() => {
        getLastMessage()
    }, [triggerLastMessage])

    function formatLastMessage() {
        const content = lastMessage.content
        const length = content.length
        if (length > 20 && !content.includes(" ")) {
            return `${content.substring(0, 15)} ...`
        }
        return content
    }

    return (
        <>
            {widthType == "mobile" && isVisible ? (
                <div className="flex w-full h-full border-1 border-black">
                    < div className="w-2/3 pl-4 pt-2 h-full" >
                        <p className="text-2xl text-black">{_group.title}</p>
                        <p className="text-xl text-gray-400">{formatLastMessage()}</p>
                    </div>
                    <div className="w-1/3 h-full pt-2 text-xl text-orange-300">
                        <p>{date}</p>
                    </div>
                </div>
            )
                : isVisible ? (<div onClick={() => { changeChat(_group) }} className="w-full flex h-full border-1 border-gray-400 hover:border-orange-300" id="global-group">
                    < div className="w-2/3 pl-4 pt-2 h-full" >
                        <p className="text-base text-black">{_group.title}</p>
                        <p className="overflow-hidden text-sm text-gray-400">{lastMessage.content}</p>
                    </div>
                    <div className="w-1/3 h-full pt-2 text-sm/6 text-orange-300">
                        <p>{date}</p>
                    </div>
                </div>) : (
                    <div className="w-full h-full space-y-2 items-center justify-center">
                        <div onClick={() => { changeChat(_group) }} className="flex items-center justify-center ">
                            <div className="w-[40px] h-[40px] border-2 border-gray-400 flex items-center justify-center hover:text-white hover:bg-orange-600 rounded-full">
                                <p>{_group.title.charAt(0)}</p>
                            </div>
                        </div>
                    </div>
                )}
        </>
    )
}