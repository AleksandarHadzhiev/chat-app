"use client"

import ChildContext from "../General/Context";
import Panel from "./Panel";
import { SendMessage } from "./SendMessage";
import Sidebar from "./Sidebar";
import React, { use, useContext, useEffect, useState } from 'react';
import { useRouter } from "next/navigation";
import axios from "axios";
export function Chat() {
    const router = useRouter()
    const [group, setGroup] = useState({ id: Number(1), title: String("General Group Chat") })
    const [socket, setSocket] = useState<WebSocket>()
    const [user, setUser] = useState({
        id: Number(),
        email: String(),
        password: String(),
        username: String(),
        verified: Boolean(),
    })

    function getMessages(id: any) {
        console.log(id)
        axios.get(`http://localhost:8000/messages/${id}`).then((respnse) => {
            displayMessages(respnse.data.messages)
        }).catch((error) => {
            console.log(error)
        })
    }

    function displayMessages(messages: [{ id: Number, content: String, author: String, group_id: Number, user_id: Number }]) {
        const panel = document.getElementById("panel")
        if (panel?.firstChild)
            panel?.replaceChildren()
        for (let index = 0; index < messages.length; index++) {
            const element = messages[index];
            const text = String(element.content)
            displayMessage(element.author, text)
        }
    }

    function displayMessage(sender: String, message: string) {
        const panel = document.getElementById(`panel`)
        const container = document.createElement('div')
        container.setAttribute("id", "loaded-message")
        const isOwnMessage = sender == user.username
        container.className = `flex  w-full pb-2 ${isOwnMessage ? "justify-end pr-2" : "pl-2"}`
        const author = document.createElement('div')
        author.className = `mr-2 mt-2 flex tems-center justify-center w-12 h-12 ${isOwnMessage ? "bg-orange-600 text-white" : "bg-orange-300 text-black"} rounded-full`
        const authorName = document.createElement('p')
        authorName.className = 'w-full h-full text-center p-3'
        authorName.textContent = sender.charAt(0)
        const content = document.createElement('p')
        content.className = `flex rounded-2xl w-[400px] bg-oragne-300 text-black p-3 mt-2 ${isOwnMessage ? "bg-orange-600 text-white" : "bg-orange-300 text-black"}`
        content.textContent = message
        author.appendChild(authorName)
        container.appendChild(author)
        container.appendChild(content)
        panel?.appendChild(container)
    }

    const { language, isVisible } = useContext(ChildContext)
    const [groupsAreVisible, setIsVisible] = useState(true)

    useEffect(() => {
        getMessages(group.id)
        if (localStorage) {
            const userStringed = localStorage.getItem("user")
            if (userStringed)
                setUser(JSON.parse(userStringed))
            else {
                router.push("/login")
            }
            if (user.username != '') {
                if (socket == undefined)
                    setSocket(new WebSocket(`ws:/127.0.0.1:8000/ws/${user.id}/${user.username}`))
            }
        }
    }, [user.id, group])

    socket?.addEventListener('open', (event) => {
        console.log(event)
    })

    socket?.addEventListener('close', (event) => {
        console.log(event.reason)
    })

    return (
        <div className="w-full h-full flex">
            {isVisible ? null : <Sidebar setIsVisible={setIsVisible} isvisible={groupsAreVisible} id={user.id} setGroup={setGroup} displayMessages={displayMessages} group={group} />}
            {socket ? (<div className={`flex flex-col ${isVisible ? "w-full" : groupsAreVisible == false ? "w-full" : " w-5/6"} h-full`}>
                <Panel socket={socket} group={group} displayMessage={displayMessage} />
                <SendMessage socket={socket} user={user} group={group} />
            </div>) : <p>Loading...</p>}
        </div>
    )
}