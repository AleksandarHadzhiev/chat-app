"use client"
import { Key, useEffect, useState, useContext } from "react"
import CreateGroup from "./CreateGroup"
import ChildContext from "../General/Context"
import Search from "./Search"
import GroupsHandler from "@/ApiCalls/GroupsHandler"
import TranslationLoader from "@/tools/TranslationLoader"
import Notification from "../General/Notification"
import GroupBox from "./GroupBox"
import ButtonToOpenAddGroupDialog from "./ButtonToOpenAddGroupDialog"
import { useRouter } from "next/navigation";


//@ts-expect-error
// Providing a function and can not specify the type
export default function Groups({ socket }) {
    const _socket: WebSocket = socket
    const router = useRouter()
    const [switcher, setSwitcher] = useState(false)
    _socket.onmessage = (event) => {
        const json = JSON.parse(event.data)
        const data = json.data
        if (json.type == "notification" && data.action == "groups") {
            setSwitcher(!switcher)
        }

    }

    const { language, widthType } = useContext(ChildContext)
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
        "kicked": "You have kicked the member out of the group.",
        "joined": "You have joined a group.",
        "already a member": "You are already a member of the group."
    })
    const [response, setResponse] = useState("")
    const [notification, setNotificaiton] = useState("")
    const [isFocued, setIsFocused] = useState(false)
    const [isOpenDialog, setOpenDialog] = useState(false)
    const [groups, setGroups] = useState([])
    const [user, setUser] = useState<{
        id: number,
        email: string,
        name: string,
        verified: boolean,
    }>({
        id: Number(0),
        email: String(),
        name: String(),
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
        setTranslations(data.translations)
    }

    async function getAllGroups() {
        const groups = await handler.getAllGroups()
        if ("tag" in groups) { router.push("/login") }
        else setGroups(groups)
    }

    useEffect(() => {
        const userstringed = localStorage.getItem("user")
        if (userstringed) {
            setUser(JSON.parse(userstringed))
        }
        getAllGroups()
        loadTranslations()
    }, [user.id, groups.length, language, response, switcher])

    function triggerUpdate(group_id: any) {
        const notification = {
            type: "notification",
            data: {
                action: "groups",
                group: group_id ? group_id : 0
            }
        }
        socket?.send(JSON.stringify(notification))
    }

    return (
        <div className="w-full h-full flex flex-col">
            <Search widthType={widthType} setIsFocused={setIsFocused} isFocued={isFocued} translations={translations} />
            <Notification response={response} notification={notification} />
            <div className={`${groups ? `w-full ${widthType == "mobile" ? "h-7/9 flex items-center justify-center" : "h-4/9"} flex flex-col space-y-2` : "hidden"}`}>

                {/* Groups */}
                <div className="overflow-y-auto w-full h-full flex flex-col items-center">
                    {groups ? groups.map((group: any, key: Key) => {
                        return (
                            <div key={key} className={`mt-2 ${widthType == "mobile" ? "w-[95%]" : "w-1/3 ml-2 "} min-h-20 max-h-20 flex h-1/4 border-1 border-gray-400 hover:border-orange-300`} id="global-group">
                                <GroupBox widthType={widthType} getAllGroups={getAllGroups} setResponse={setResponse} setNotificaiton={setNotificaiton} triggerUpdate={triggerUpdate} groups={groups} user={user} group={group} translations={translations} />
                            </div>
                        )
                    }) : (<p>{translations.loading}</p>)}
                </div>
            </div>
            <div className={`${isOpenDialog ? 'z-998 fixed flex items-center justify-center inset-0 bg-gray-500/75 ' : "hidden"} `}>
                <div
                    onClick={() => { closeDialog() }}
                    className="absolute top-0 w-screen h-screen transition-opacity flex items-center justify-center">
                </div>
                <CreateGroup triggerUpdate={triggerUpdate} getAllGroups={getAllGroups} closeDialog={closeDialog} translations={translations} setResponse={setResponse} setNotificaiton={setNotificaiton} />
            </div>
            <ButtonToOpenAddGroupDialog widthType={widthType} isOpenDialog={isOpenDialog} openDialog={openDialog} />
        </div >
    )
}