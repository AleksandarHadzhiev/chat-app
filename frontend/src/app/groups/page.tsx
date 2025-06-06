"use client"

import Groups from "@/components/Groups/Groups"
import { useEffect, useState } from "react"

export default function GroupsPage() {
    const [socket, setSocket] = useState<WebSocket>()
    const [_url, setUrl] = useState()
    useEffect(() => {
        const urlFromStorage = localStorage.getItem("ws")
        if (urlFromStorage != undefined && socket == undefined) {
            setUrl(_url)
            const ws = new WebSocket(urlFromStorage)
            setSocket(ws)
        }
    }, [])

    return (
        <div className="flex flex-col w-full h-full">
            {socket && socket != undefined ? <Groups socket={socket} /> : null}
        </div>
    )
}