import { useState } from "react"
import EditGroup from "./EditGroup"
import MembersDialog from "./Members"
import GroupsHandler from "@/ApiCalls/GroupsHandler"
//@ts-expect-error
// Providing a function and can not specify the type
export default function AdminMenu({ widthType, trigerUpdate, group, user, getAllGroups, translations, setNotificaiton, setResponse }) {
    const handler = new GroupsHandler()
    const [editDialog, setOpenEditDialog] = useState(false)
    const [membersDialog, setOpenMembersDialog] = useState(false)

    function openEditDialog() {
        setOpenEditDialog(true)
    }

    function closeEditDialog() {
        setOpenEditDialog(false)
        const adminMenu = document.getElementById(`${group.id}`)
        if (adminMenu) adminMenu.className = "hidden"
    }

    function closeMembersDialog() {
        setOpenMembersDialog(false)
        const adminMenu = document.getElementById(`${group.id}`)
        if (adminMenu) adminMenu.className = "hidden"
    }

    async function deleteGroup() {
        const response = await handler.deleteGroup(group.id, user.id, translations)
        if ("tag" in response) {
            setNotificaiton(response.message)
            setResponse(response.tag)
            trigerUpdate(group.id)
        }
        await getAllGroups()
        const adminMenu = document.getElementById(`${group.id}`)
        if (adminMenu) adminMenu.className = "hidden"
    }

    return (
        <div className="w-full h-full flex flex-col space-y-2">
            <div onClick={() => { setOpenMembersDialog(!membersDialog) }} className={`${widthType == "mobile" ? "border-b-2 border-white" : ''} flex flex-row w-full hover:text-orange-600 space-x-2`}>
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth="1.5" stroke="currentColor" className="size-6 ml-1">
                    <path strokeLinecap="round" strokeLinejoin="round" d="M22 10.5h-6m-2.25-4.125a3.375 3.375 0 1 1-6.75 0 3.375 3.375 0 0 1 6.75 0ZM4 19.235v-.11a6.375 6.375 0 0 1 12.75 0v.109A12.318 12.318 0 0 1 10.374 21c-2.331 0-4.512-.645-6.374-1.766Z" />
                </svg>
                <p>{translations.kick}</p>
            </div>
            <div onClick={() => { openEditDialog() }} className={`${widthType == "mobile" ? "border-b-2 border-white" : ''} flex flex-row w-full hover:text-orange-600 space-x-2`}>
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth="1.5" stroke="currentColor" className="size-6 ml-1">
                    <path strokeLinecap="round" strokeLinejoin="round" d="m16.862 4.487 1.687-1.688a1.875 1.875 0 1 1 2.652 2.652L6.832 19.82a4.5 4.5 0 0 1-1.897 1.13l-2.685.8.8-2.685a4.5 4.5 0 0 1 1.13-1.897L16.863 4.487Zm0 0L19.5 7.125" />
                </svg>
                <p>{translations.edit}</p>
            </div>
            <div onClick={() => { deleteGroup() }} className="flex flex-row w-full hover:text-orange-600 space-x-2">
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth="1.5" stroke="currentColor" className="size-6 ml-1">
                    <path strokeLinecap="round" strokeLinejoin="round" d="m14.74 9-.346 9m-4.788 0L9.26 9m9.968-3.21c.342.052.682.107 1.022.166m-1.022-.165L18.16 19.673a2.25 2.25 0 0 1-2.244 2.077H8.084a2.25 2.25 0 0 1-2.244-2.077L4.772 5.79m14.456 0a48.108 48.108 0 0 0-3.478-.397m-12 .562c.34-.059.68-.114 1.022-.165m0 0a48.11 48.11 0 0 1 3.478-.397m7.5 0v-.916c0-1.18-.91-2.164-2.09-2.201a51.964 51.964 0 0 0-3.32 0c-1.18.037-2.09 1.022-2.09 2.201v.916m7.5 0a48.667 48.667 0 0 0-7.5 0" />
                </svg>
                <p>{translations.delete}</p>
            </div>
            <div className={`${editDialog ? 'z-998 fixed flex items-center justify-center inset-0 bg-gray-500/75 ' : "hidden"} `}>
                <div
                    onClick={() => { closeEditDialog() }}
                    className="absolute top-0 w-screen h-screen transition-opacity flex items-center justify-center">
                </div>
                <EditGroup trigerUpdate={trigerUpdate} setNotificaiton={setNotificaiton} setResponse={setResponse} group={group} user={user} getAllGroups={getAllGroups} closeDialog={closeEditDialog} translations={translations} />
            </div>
            <div className={`${membersDialog ? 'z-998 fixed flex items-center justify-center inset-0 bg-gray-500/75 ' : "hidden"} `}>
                <div
                    onClick={() => { setOpenMembersDialog(false) }}
                    className="absolute top-0 w-screen h-screen transition-opacity flex items-center justify-center">
                </div>
                <MembersDialog trigerUpdate={trigerUpdate} setNotificaiton={setNotificaiton} setResponse={setResponse} group={group} user={user} getAllGroups={getAllGroups} closeDialog={closeMembersDialog} translations={translations} />
            </div>
        </div>
    )
}