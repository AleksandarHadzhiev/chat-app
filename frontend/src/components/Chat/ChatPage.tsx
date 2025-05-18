"use client"

import ChildContext from "../General/Context";
import Panel from "./Panel";
import { SendMessage } from "./SendMessage";
import Sidebar from "./Sidebar";
import React, { useContext, useEffect, useState } from 'react';
import { useRouter } from "next/navigation";
import axios from "axios";
import UpdateMessage from "./UpdateMessage";
export function Chat() {
    const router = useRouter()
    const [group, setGroup] = useState({ id: Number(1), title: String("General Group Chat"), admin_id: Number(1) })
    const [socket, setSocket] = useState<WebSocket>()
    const [actionsOpened, setActionsOpened] = useState(false)
    const [code, setCode] = useState("")
    const [content, setContent] = useState("")
    const [editMessageIsOpen, setEditMessage] = useState(false)
    const [messages, setMessages] = useState([])
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
            setMessages(respnse.data.messages)
        }).catch((error) => {
            console.log(error)
        })
    }

    function displayMessages(messages: [{ id: Number, content: String, author: String, group_id: Number, user_id: Number, code: String }]) {
        const panel = document.getElementById("panel")
        console.log(messages)
        if (panel?.firstChild)
            panel?.replaceChildren()
        for (let index = 0; index < messages.length; index++) {
            const element = messages[index];
            displayMessage(element)
        }
    }

    function displayPossibleActions(data: { id: Number, content: String, author: String, group_id: Number, user_id: Number, code: String }) {
        removeActions()
        const message = document.getElementById(`loaded-message-${data.code}`)
        const container = document.createElement('div')
        container.setAttribute('id', "message-actions")
        container.className = "flex flex-col w-28 bg-white border-2 border-gray-600 mt-1 space-x-3 ml-15 rounded-md"
        const edit = document.createElement('div')
        const remove = document.createElement('div')
        const btnsClass = "w-full space-x-2 space-y-1 flex bg-white hover:border-orange-600 hover:text-orange-600 text-black rounded-md mt-1"
        remove.innerHTML = `
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth="1.5" stroke="currentColor" class="size-6 ml-1">
                <path strokeLinecap="round" strokeLinejoin="round" d="m14.74 9-.346 9m-4.788 0L9.26 9m9.968-3.21c.342.052.682.107 1.022.166m-1.022-.165L18.16 19.673a2.25 2.25 0 0 1-2.244 2.077H8.084a2.25 2.25 0 0 1-2.244-2.077L4.772 5.79m14.456 0a48.108 48.108 0 0 0-3.478-.397m-12 .562c.34-.059.68-.114 1.022-.165m0 0a48.11 48.11 0 0 1 3.478-.397m7.5 0v-.916c0-1.18-.91-2.164-2.09-2.201a51.964 51.964 0 0 0-3.32 0c-1.18.037-2.09 1.022-2.09 2.201v.916m7.5 0a48.667 48.667 0 0 0-7.5 0" />
            </svg>
            <p className="mt-2">Delete</p>
        `
        edit.innerHTML = `
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth="1.5" stroke="currentColor" class="size-6 ml-1">
                <path strokeLinecap="round" strokeLinejoin="round" d="m16.862 4.487 1.687-1.688a1.875 1.875 0 1 1 2.652 2.652L6.832 19.82a4.5 4.5 0 0 1-1.897 1.13l-2.685.8.8-2.685a4.5 4.5 0 0 1 1.13-1.897L16.863 4.487Zm0 0L19.5 7.125" />
            </svg>
            <p className="mt-2">Edit</p>
        `
        remove.addEventListener('mousedown', () => {
            console.log("MEOW")
            deleteMessage(code)
        })
        edit.addEventListener('mousedown', () => {
            console.log("MEOW")
            editMessage(`${data.code}`, `${data.content}`)
        })
        remove.className = btnsClass
        edit.className = btnsClass
        console.log(data.user_id)
        console.log(user.id)
        if (data.user_id == user.id) {
            console.log("OPEN")
            container.appendChild(edit)
            container.appendChild(remove)
            message?.appendChild(container)
        }
    }

    addEventListener("mousedown", (event) => {
        // From NextJS -> 0 means left click
        if (event.button == 0) {
            removeActions()
        }
    })

    function editMessage(_code: string, content: string) {
        setEditMessage(true)
        setContent(content)
        setCode(_code)
        console.log(editMessageIsOpen)
    }

    function deleteMessage(_code: String) {
        // Delete message in DB
        axios.delete(`http://localhost:8000/messages/${_code}`).then((res) => {
            console.log(res)
            const message = document.getElementById(`loaded-message-${_code}`)
            message?.remove()
        }).catch((err) => {
            console.log(err)
        })
    }

    function removeActions() {
        const message = document.getElementById(`message-actions`)
        if (message != null || message != undefined) {
            message.remove()
            setActionsOpened(false)
        }
    }

    function displayMessage(data: { id: Number, content: String, author: String, group_id: Number, user_id: Number, code: String }) {
        console.log(data)
        const panel = document.getElementById(`panel`)
        const container = document.createElement('div')
        container.setAttribute("id", `loaded-message-${data.code}`)
        container.onmousedown = function (event: MouseEvent) {
            event.preventDefault()
            // 2 is from NextJS, it's equal to right click mouse button
            if (event.button == 2 && actionsOpened == false) {
                setActionsOpened(true)
                displayPossibleActions(data)
            }
        }
        container.oncontextmenu = function (event: MouseEvent) {
            event.preventDefault()
        }
        const isOwnMessage = data.author == user.username
        container.className = `flex flex-col w-full pb-2 ${isOwnMessage ? "justify-end pr-2" : "pl-2"}`
        const fullFormatMessage = document.createElement('div')
        fullFormatMessage.className = "flex w-full"
        const author = document.createElement('div')
        author.className = `mr-2 mt-2 flex items-center justify-center w-12 h-12 ${isOwnMessage ? "bg-orange-600 text-white" : "bg-orange-300 text-black"} rounded-full`
        const authorName = document.createElement('p')
        authorName.className = 'w-full h-full text-center p-3'
        authorName.textContent = data.author.charAt(0)
        const content = document.createElement('p')
        content.id = `${data.code}`
        content.className = `flex rounded-2xl w-[400px] bg-oragne-300 text-black p-3 mt-2 ${isOwnMessage ? "bg-orange-600 text-white" : "bg-orange-300 text-black"}`
        content.textContent = `${data.content}`
        author.appendChild(authorName)
        fullFormatMessage.appendChild(author)
        fullFormatMessage.appendChild(content)
        container.appendChild(fullFormatMessage)
        panel?.appendChild(container)
    }

    const { language, isVisible } = useContext(ChildContext)
    const [groupsAreVisible, setIsVisible] = useState(true)

    useEffect(() => {
        console.log(group.id)
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
                    setSocket(new WebSocket(`ws:/127.0.0.1:8000/ws/${user.id}/${user.username}/${group.admin_id}`))
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
                <Panel messages={messages} socket={socket} group={group} displayMessage={displayMessage} />
                {editMessageIsOpen ? <UpdateMessage setEditMessage={setEditMessage} code={code} content={content} /> : <SendMessage socket={socket} user={user} group={group} />}
            </div>) : <p>Loading...</p>}
        </div>
    )
}
