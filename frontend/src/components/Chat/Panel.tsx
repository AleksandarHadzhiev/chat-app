import { useState } from "react"


//@ts-expect-error
// Providing a function and can not specify the type
export default function Panel({ setIsVisible, widthType, socket, group, displayMessage, messages, isWriting, setIsWriting, setTriggerOff, trigger, translations }) {
    const MAXIMU_ALLOWED_VISIBLE_NAMES = 3
    const _socket: WebSocket = socket
    let writingUsers: any[] = []
    const [writers, setWrites] = useState("")

    _socket.onmessage = (event) => {
        const json = JSON.parse(event.data)
        const data = json.data
        if (json.type == "message") {
            handleMessage(data)
            setTriggerOff(!trigger)
        }
        else if (json.type == "notification" && data.action == "updated") {
            setTriggerOff(!trigger)
        }
        else if (json.type == "notification" && data.group == group.id) {
            handleNotification(data)
        }
        else if (json.type == "fail") {
            alert(json.data)
        }
    }
    function handleMessage(data: any) {
        displayMessage(data)
        messages.push(data)
    }

    function handleNotification(data: any) {
        if (data.action == 'writing') {
            handleAddUserToWriters(data)
        }
        else if (data.action == 'stopped') {
            handleRemoveUserFromWriters(data)
        }
    }

    function handleAddUserToWriters(data: any) {
        setIsWriting(true)
        writingUsers.push(data.user)
        displayNamesOnlyIfWritersLessThanMaximumAllowedVisibleNames()
    }

    function handleRemoveUserFromWriters(data: any) {
        setIsWriting(false)
        if (writingUsers.length > 0) {
            const index = writingUsers.findIndex(data.user)
            writingUsers = writingUsers.splice(index, 1)
            displayNamesOnlyIfWritersLessThanMaximumAllowedVisibleNames()
        }
    }

    function displayNamesOnlyIfWritersLessThanMaximumAllowedVisibleNames() {
        if (writingUsers.length < MAXIMU_ALLOWED_VISIBLE_NAMES)
            setWrites(writingUsers.join(', '))
        else
            setWrites("Many people")
    }

    return (
        <div className="flex flex-col w-full h-9/10">
            <div className={`border-b border-gray-200 flex flex-col w-full ${isWriting ? "pb-1" : "pb-4"}`}>
                <div className="flex flex-row w-full h-9/10 space-x-2">
                    {widthType == "mobile" ? (
                        <div className="pl-2 pt-1" onClick={() => { setIsVisible(true) }}>
                            <svg
                                xmlns="http://www.w3.org/2000/svg"
                                fill="none"
                                viewBox="0 0 24 24"
                                strokeWidth="1.5"
                                stroke="currentColor"
                                className="size-6">
                                <path
                                    strokeLinecap="round"
                                    strokeLinejoin="round"
                                    d="M9 15 3 9m0 0 6-6M3 9h12a6 6 0 0 1 0 12h-3" />
                            </svg>
                        </div>) : null}
                    <div className="pl-2 flex flex-col w-full h-8/10 pt-1">
                        <h1 className={widthType == "mobile" ? "text-2xl" : ""}>{group.title}</h1>
                    </div>
                </div>
                {isWriting ? (<p className={`pl-2 text-orange-600 ${widthType == "mobile" ? "text-xl" : ""}`}>{writers} {translations.writing} <span className={widthType == "mobile" ? "text-xl" : ""}>...</span></p>) : null}
            </div>
            <div id={"panel"} className="w-full h-9/10 overflow-y-auto"></div>
        </div >
    )
}
