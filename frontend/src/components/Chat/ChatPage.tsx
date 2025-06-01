"use client"

import ChildContext from "../General/Context";
import Panel from "./Panel";
import { SendMessage } from "./SendMessage";
import Sidebar from "./Sidebar";
import React, { useContext, useEffect, useState } from 'react';
import { useRouter } from "next/navigation";
import UpdateMessage from "./UpdateMessage";
import TranslationLoader from "@/tools/TranslationLoader";
import MessagesHandler from "@/ApiCalls/MessagesHandler";
export function ChatPage() {
    const router = useRouter()

    const handler = new MessagesHandler()
    const LEGNTH_ROW_FOR_READABLE_MESSAGE = 20
    const [touchStart, setTouchStart] = useState(0)
    const [triggerGettingLastMessage, setTriggerGettingLastMessage] = useState(false)
    const [group, setGroup] = useState({ id: Number(1), title: String("General Group Chat"), admin_id: Number(1) })
    const [socket, setSocket] = useState<WebSocket>()
    const [actionsOpened, setActionsOpened] = useState(false)
    const [code, setCode] = useState("")
    const [content, setContent] = useState("")
    const [editMessageIsOpen, setEditMessage] = useState(false)
    const [messages, setMessages] = useState([])
    const { language, isVisible, widthType } = useContext(ChildContext)
    const [isWriting, setIsWriting] = useState(false)
    const [translations, setTranslations] = useState({
        search: "Search ...",
        write: "Write a message ...",
        writing: "is/are writing",
        refactor: "Edit message",
        delete: "Delete",
        edit: "Edit"
    })
    const [user, setUser] = useState({
        id: Number(),
        email: String(),
        name: String(),
        verified: Boolean(),
    })

    async function loadTranslations() {
        const translationsLoader = new TranslationLoader(language, "messages")
        const response = await translationsLoader.getTranslatiosn()
        const data = JSON.parse(response.data)
        setTranslations(data.translations)
    }

    async function getMessages(id: any) {
        const _messages = await handler.getAllMessages(id)
        if ("tag" in _messages) {
            router.push("/login")
        }
        setMessages(_messages)
        displayMessages(_messages)
    }

    function displayMessages(messages: [{ id: number, content: string, author: string, group_id: number, user_id: number, code: string }]) {
        const panel = document.getElementById("panel")
        if (panel?.firstChild)
            panel?.replaceChildren()
        for (let index = 0; index < messages.length; index++) {
            const element = messages[index];
            displayMessage(element)
        }
    }

    function displayPossibleActions(data: { id: number, content: string, author: string, group_id: number, user_id: number, code: string }) {
        removeActions()
        const message = document.getElementById(`loaded-message-${data.code}`)
        const container = document.createElement('div')
        container.setAttribute('id', "message-actions")
        container.className = "flex flex-col w-28 bg-white border-2 border-gray-600 mt-1 space-x-3 ml-15 rounded-md"
        const edit = document.createElement('div')
        const remove = document.createElement('div')
        const btnsClass = `w-full space-x-2 space-y-1 flex bg-white hover:border-orange-600 hover:text-orange-600 text-black rounded-md mt-1`
        remove.innerHTML = `
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth="1.5" stroke="currentColor" class="size-6 ml-1">
                <path strokeLinecap="round" strokeLinejoin="round" d="m14.74 9-.346 9m-4.788 0L9.26 9m9.968-3.21c.342.052.682.107 1.022.166m-1.022-.165L18.16 19.673a2.25 2.25 0 0 1-2.244 2.077H8.084a2.25 2.25 0 0 1-2.244-2.077L4.772 5.79m14.456 0a48.108 48.108 0 0 0-3.478-.397m-12 .562c.34-.059.68-.114 1.022-.165m0 0a48.11 48.11 0 0 1 3.478-.397m7.5 0v-.916c0-1.18-.91-2.164-2.09-2.201a51.964 51.964 0 0 0-3.32 0c-1.18.037-2.09 1.022-2.09 2.201v.916m7.5 0a48.667 48.667 0 0 0-7.5 0" />
            </svg>
            <p className="mt-2">${translations.delete}</p>
        `
        edit.innerHTML = `
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth="1.5" stroke="currentColor" class="size-6 ml-1">
                <path strokeLinecap="round" strokeLinejoin="round" d="m16.862 4.487 1.687-1.688a1.875 1.875 0 1 1 2.652 2.652L6.832 19.82a4.5 4.5 0 0 1-1.897 1.13l-2.685.8.8-2.685a4.5 4.5 0 0 1 1.13-1.897L16.863 4.487Zm0 0L19.5 7.125" />
            </svg>
            <p className="mt-2">${translations.edit}</p>
        `
        remove.addEventListener('mousedown', () => {
            deleteMessage(data.code)
        })
        edit.addEventListener('mousedown', () => {
            editMessage(`${data.code}`, `${data.content}`)
        })
        remove.className = btnsClass
        edit.className = btnsClass
        if (data.user_id == user.id) {
            container.appendChild(edit)
            container.appendChild(remove)
            message?.appendChild(container)
        }
    }

    function editMessage(_code: string, content: string) {
        setEditMessage(true)
        setContent(content)
        setCode(_code)
    }

    async function deleteMessage(_code: string) {
        // Delete message in DB
        const response = await handler.deleteAMessage(_code, user.id, group.id, translations)
        if ("tag" in response && response.tag == "success") {
            const message = document.getElementById(`loaded-message-${_code}`)
            message?.remove()
        }
        else if ("tag" in response && response.tag == "redirect")
            router.push("/login")
    }

    function removeActions() {
        const message = document.getElementById(`message-actions`)
        if (message != null || message != undefined) {
            message.remove()
            setActionsOpened(false)
        }
    }

    function displayMessage(data: { id: number, content: string, author: string, group_id: number, user_id: number, code: string }) {
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
        container.ontouchstart = function (event: TouchEvent) {
            event.preventDefault()
            setTouchStart(Date.now())
        }

        container.ontouchend = function (event: TouchEvent) {
            event.preventDefault()
            const ms = Date.now() - touchStart
            const difference = Math.floor(ms / 1000)
            if (difference > 1) {
                setActionsOpened(true)
                displayPossibleActions(data)
            }
        }

        container.oncontextmenu = function (event: MouseEvent) {
            event.preventDefault()
        }
        const isOwnMessage = data.author == user.name
        container.className = `overflow-hidden flex flex-col w-full pb-2 ${isOwnMessage ? "justify-end pr-2" : "pl-2"}`
        const fullFormatMessage = document.createElement('div')
        fullFormatMessage.className = "flex w-full"
        const author = document.createElement('div')
        author.className = `mr-2 mt-2 flex items-center justify-center w-12 h-12 ${isOwnMessage ? "bg-orange-600 text-white" : "bg-orange-300 text-black"} rounded-full`
        const authorName = document.createElement('p')
        authorName.className = 'w-full h-full text-center p-3'
        authorName.textContent = data.author.charAt(0)
        const content = document.createElement('p')
        content.id = `${data.code}`
        content.className = `${widthType == "mobile" ? "text-2xl" : ""} overflow-hidden h-auto flex rounded-2xl w-[400px] bg-oragne-300 text-black p-3 mt-2 ${isOwnMessage ? "bg-orange-600 text-white" : "bg-orange-300 text-black"}`
        content.innerHTML = displayReadableMessage(data.content)
        author.appendChild(authorName)
        fullFormatMessage.appendChild(author)
        fullFormatMessage.appendChild(content)
        container.appendChild(fullFormatMessage)
        panel?.appendChild(container)
    }

    function displayReadableMessage(content: string) {
        if (content.length > LEGNTH_ROW_FOR_READABLE_MESSAGE && !content.includes(" ")) {
            const breakingPoints = Math.round(content.length / LEGNTH_ROW_FOR_READABLE_MESSAGE)
            let message = ``
            for (let index = 1; index <= breakingPoints; index++) {
                if (index == 1) {
                    message += `${content.substring(0, LEGNTH_ROW_FOR_READABLE_MESSAGE)}<br/>`
                }
                else if (index == breakingPoints) {
                    message += `${content.substring(LEGNTH_ROW_FOR_READABLE_MESSAGE * (index - 1), LEGNTH_ROW_FOR_READABLE_MESSAGE * index)}<br/`
                }
                else {
                    message += `${content.substring(LEGNTH_ROW_FOR_READABLE_MESSAGE * index, LEGNTH_ROW_FOR_READABLE_MESSAGE * Number(index + 1))}<br/>`
                }
            }
            return message

        } else return `${content}`
    }

    const [groupsAreVisible, setIsVisible] = useState(true)

    useEffect(() => {
        addEventListener("mousedown", (event) => {
            // From NextJS -> 0 means left click
            if (event.button == 0) {
                removeActions()
            }
        })
        loadTranslations()
        getMessages(group.id)
        if (localStorage) {
            if (localStorage.getItem("access_token") == null) {
                router.push("/login")
            }
            const accessToken = localStorage.getItem("access_token")
            const userData = localStorage.getItem("user")
            if (userData) {
                setUser(JSON.parse(userData))
            }
            if (socket == undefined) {
                const url = `http://localhost:8000/ws/${accessToken}/${group.admin_id}`
                localStorage.setItem("ws", url)
                const socket = new WebSocket(url)
                setSocket(socket)
            }
        }

    }, [user.id, group, language])


    function setPanelStyleBasedOnDevice() {
        if (widthType == "mobile" && groupsAreVisible) return 'hidden'
        else return `flex flex-col ${isVisible ? "w-full" : groupsAreVisible == false ? "w-full" : " w-5/6"} h-full`
    }

    return (
        <div className="w-full h-full flex">
            {isVisible ? null : <Sidebar
                widthType={widthType}
                translations={translations}
                triggerLastMessage={triggerGettingLastMessage}
                setIsVisible={setIsVisible} isVisible={groupsAreVisible}
                id={user.id}
                setGroup={setGroup}
                displayMessages={displayMessages}
                group={group} />}
            {socket ? (<div
                className={setPanelStyleBasedOnDevice()}>
                <Panel
                    setIsVisible={setIsVisible}
                    widthType={widthType}
                    translations={translations}
                    trigger={triggerGettingLastMessage}
                    setTriggerOff={setTriggerGettingLastMessage}
                    messages={messages}
                    socket={socket}
                    group={group}
                    displayMessage={displayMessage}
                    isWriting={isWriting}
                    setIsWriting={setIsWriting} />
                {editMessageIsOpen ? <UpdateMessage
                    widthType={widthType}
                    translations={translations}
                    socket={socket}
                    user={user}
                    group={group}
                    trigger={triggerGettingLastMessage}
                    setTriggerOff={setTriggerGettingLastMessage}
                    setEditMessage={setEditMessage}
                    code={code}
                    content={content} /> : <SendMessage
                    widthType={widthType}
                    translations={translations}
                    trigger={triggerGettingLastMessage}
                    setTriggerOff={setTriggerGettingLastMessage}
                    socket={socket}
                    group={group}
                    setIsWriting={setIsWriting} />}
            </div>) : <p>Loading...</p>}
        </div>
    )
}
