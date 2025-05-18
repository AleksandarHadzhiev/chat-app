"use client"
import { Key, useEffect, useState, useContext } from "react"
import CreateGroup from "./CreateGroup"
import ChildContext from "../General/Context"
import axios from "axios"
import Search from "./Search"
import AdminMenu from "./AdminMenu"
import GroupsHandler from "@/ApiCalls/GroupsHandler"
import TranslationLoader from "@/tools/TranslationLoader"
import Notification from "../General/Notification"


export default function Groups() {
    const { language } = useContext(ChildContext)

    const handler = new GroupsHandler()
    const [translations, setTranslations] = useState({
        "join": "Join",
        "leave": "Leave",
        "cancel": "Cancel",
        "submit": "Submit",
        "search": "Search",
        "edit": "Edit",
        "delete": "Delete",
        "kick": "Kick member out",
        "name": "Name",
        "current name": "Current name",
        "new name": "New name",
        "loading": "Loacding...",
        "role": "Role",
        "actions": "Actions",
        "members": "Members",
        "created group": "You have created a group. Make it popular.",
        "edited": "You have changed the name of the group.",
        "deleted": "You have deleted the group.",
        "left": "You have left the group",
        "kicked": "You have kicked the member out of the group."
    })
    const [response, setResponse] = useState("")
    const [notification, setNotificaiton] = useState("")
    const [isFocued, setIsFocused] = useState(false)
    const [menuIsOpened, setMenuIsOpened] = useState(false)
    const [isOpenDialog, setOpenDialog] = useState(false)
    const [groups, setGroups] = useState([])
    const [user, setUser] = useState<{
        id: Number,
        email: String,
        password: String,
        username: String,
        verified: Boolean,
    }>({
        id: Number(0),
        email: String(),
        password: String(),
        username: String(),
        verified: Boolean(),
    })

    function openDialog() {
        setOpenDialog(true)
    }

    function closeDialog() {
        setOpenDialog(false)
    }

    async function loadTranslations() {
        const translationsLoader = new TranslationLoader(language, "groups")
        const response = await translationsLoader.getTranslatiosn()
        const data = JSON.parse(response.data)
        console.log(data)
        setTranslations(data.translations)
    }

    function joinServer(group_id: Number) {
        const url = `http://localhost:8000/groups/${user.id}/join/${group_id}`
        handler.joinGroup(url)
        getAllGroups()
    }

    async function getAllGroups() {
        const url = "http://localhost:8000/groups/"
        const groups = await handler.getAllGroups(url)
        setGroups(groups)
    }

    useEffect(() => {
        const userStringed = localStorage.getItem("user")
        if (userStringed) {
            setUser(JSON.parse(userStringed))
        }
        getAllGroups()
        loadTranslations()
    }, [user.id, groups.length, language, response])

    function isNotAllowedToJoin(group: any) {
        if (isAlreadyAdmin(group)) return true
        else if (isAlreadyAMember(group.members)) return true
        else return false
    }

    function isAlreadyAdmin(group: any) {
        if (group.admin_id === user.id) {
            return true
        }
        return false
    }

    function isAlreadyAMember(members: any) {
        console.log(members)
        members.forEach((member: { id: Number, name: String }) => {
            if (member.id == user.id) {
                return true
            }
        })
        return false
    }

    async function leaveGroup(group: any) {
        const url = `http://localhost:8000/groups/${user.id}/leave/${group.id}`
        const response = await handler.leaveGroup(url, translations)
        if ("tag" in response) {
            setNotificaiton(response.message)
            setResponse(response.tag)
        }
        await getAllGroups()
    }

    function openMenu() {
        setMenuIsOpened(!menuIsOpened)
    }

    return (
        <div className="w-full h-full flex flex-col">
            <Search setIsFocused={setIsFocused} isFocued={isFocued} translations={translations} />
            <Notification response={response} notification={notification} />
            <div className={`${groups ? "w-full h-4/9 flex flex-col space-y-2" : "hidden"}`}>
                {/* Groups */}
                {groups ? groups.map((group: any, key: Key) => {
                    return (
                        <div key={key} className="ml-2 w-1/3 flex h-1/4 border-1 border-gray-400 hover:border-orange-300" id="global-group">
                            < div className="w-2/3 pl-4 pt-2 h-full" >
                                <p className="text-base text-black">{group.title}</p>
                                <p className="text-sm text-gray-400">{translations.members} {group.members.length}</p>
                            </div>
                            <div className="w-1/3 h-full text-sm/6 text-orange-300 mr-1">
                                {
                                    isAlreadyAdmin(group) ? (
                                        <div className="flex flex-row">
                                            <div onClick={() => { openMenu() }} className="flex w-full justify-end hover:text-orange-600">
                                                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth="1.5" stroke="currentColor" className="size-6">
                                                    <path strokeLinecap="round" strokeLinejoin="round" d="M9.594 3.94c.09-.542.56-.94 1.11-.94h2.593c.55 0 1.02.398 1.11.94l.213 1.281c.063.374.313.686.645.87.074.04.147.083.22.127.325.196.72.257 1.075.124l1.217-.456a1.125 1.125 0 0 1 1.37.49l1.296 2.247a1.125 1.125 0 0 1-.26 1.431l-1.003.827c-.293.241-.438.613-.43.992a7.723 7.723 0 0 1 0 .255c-.008.378.137.75.43.991l1.004.827c.424.35.534.955.26 1.43l-1.298 2.247a1.125 1.125 0 0 1-1.369.491l-1.217-.456c-.355-.133-.75-.072-1.076.124a6.47 6.47 0 0 1-.22.128c-.331.183-.581.495-.644.869l-.213 1.281c-.09.543-.56.94-1.11.94h-2.594c-.55 0-1.019-.398-1.11-.94l-.213-1.281c-.062-.374-.312-.686-.644-.87a6.52 6.52 0 0 1-.22-.127c-.325-.196-.72-.257-1.076-.124l-1.217.456a1.125 1.125 0 0 1-1.369-.49l-1.297-2.247a1.125 1.125 0 0 1 .26-1.431l1.004-.827c.292-.24.437-.613.43-.991a6.932 6.932 0 0 1 0-.255c.007-.38-.138-.751-.43-.992l-1.004-.827a1.125 1.125 0 0 1-.26-1.43l1.297-2.247a1.125 1.125 0 0 1 1.37-.491l1.216.456c.356.133.751.072 1.076-.124.072-.044.146-.086.22-.128.332-.183.582-.495.644-.869l.214-1.28Z" />
                                                    <path strokeLinecap="round" strokeLinejoin="round" d="M15 12a3 3 0 1 1-6 0 3 3 0 0 1 6 0Z" />
                                                </svg>
                                            </div>
                                            {menuIsOpened ? (
                                                <AdminMenu setResponse={setResponse} setNotificaiton={setNotificaiton} group={group} user={user} getAllGroups={getAllGroups} setOpenMenu={setMenuIsOpened} translations={translations} />) : null}
                                        </div>
                                    ) : null
                                }
                                {
                                    isNotAllowedToJoin(group) ? (<button
                                        onClick={() => { leaveGroup(group) }}
                                        className={"w-full mt-2 h-1/2 bg-orange-600 text-white rounded-md hover:bg-orange-400"}>{translations.leave}</button>) : (
                                        <button
                                            onClick={() => { joinServer(group.id) }}
                                            className={"w-full mt-2 h-1/2 bg-orange-600 text-white rounded-md hover:bg-orange-400"}>{translations.join}</button>
                                    )
                                }
                            </div>
                        </div>
                    )
                }) : (<p>{translations.loading}</p>)}
            </div>
            <div className={`${isOpenDialog ? 'z-998 fixed flex items-center justify-center inset-0 bg-gray-500/75 ' : "hidden"} `}>
                <div
                    onClick={() => { closeDialog() }}
                    className="absolute top-0 w-screen h-screen transition-opacity flex items-center justify-center">
                </div>
                <CreateGroup getAllGroups={getAllGroups} closeDialog={closeDialog} translations={translations} setResponse={setResponse} setNotificaiton={setNotificaiton} />
            </div>
            {/* <div className="w-full h-3/10 flex items-center justify-center">
                <div className="h-full w-1/4 rounded-4xl drop-shadow-md border-2 border-gray-200 hover:border-orange-300 text-orange-300 hover:text-orange-400">
                    <button className="w-full h-full flex flex items-center justify-center">
                        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth="1.5" stroke="currentColor" className="size-24">
                            <path strokeLinecap="round" strokeLinejoin="round" d="M12 9v6m3-3H9m12 0a9 9 0 1 1-18 0 9 9 0 0 1 18 0Z" />
                        </svg>
                    </button>
                </div>
            </div> */}
            <div className={`${isOpenDialog ? "hidden" : "w-full h-4/9 flex items-center justify-center"}`}>
                <div
                    onClick={() => { openDialog() }}
                    className="h-1/2 w-1/4 rounded-4xl drop-shadow-md border-2 border-gray-200 hover:border-orange-300 text-orange-300 hover:text-orange-400">
                    <button className="w-full h-full flex flex items-center justify-center">
                        <svg
                            xmlns="http://www.w3.org/2000/svg"
                            fill="none"
                            viewBox="0 0 24 24"
                            strokeWidth="1.5"
                            stroke="currentColor"
                            className="size-24">
                            <path
                                strokeLinecap="round"
                                strokeLinejoin="round"
                                d="M12 9v6m3-3H9m12 0a9 9 0 1 1-18 0 9 9 0 0 1 18 0Z" />
                        </svg>
                    </button>
                </div>
            </div>

        </div >
    )
}