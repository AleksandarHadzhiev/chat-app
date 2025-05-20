import { FormEvent, useState } from "react"
import GroupsHandler from "@/ApiCalls/GroupsHandler"
import { GeneralGroupDTO } from "@/ApiCalls/DTOs/Other/GeneralGroupDTO"
//@ts-expect-error
// Providing a function and can not specify the type
export default function EditGroup({ closeDialog, getAllGroups, group, user, translations, setNotificaiton, setResponse }) {
    const [title, setTitle] = useState(group.title)
    const handler = new GroupsHandler()
    const editGroupDTO: GeneralGroupDTO = {
        admin: user.id,
        title: title
    }
    async function edit(e: FormEvent<HTMLFormElement>) {
        e.preventDefault()
        const url = `http://localhost:8000/groups/${group.id}`
        const response = await handler.editGroup(url, editGroupDTO, translations)
        if ("tag" in response) {
            setNotificaiton(response.message)
            setResponse(response.tag)

        }
        await getAllGroups();
        closeDialog()
        const adminMenu = document.getElementById(`${group.id}`)
        if (adminMenu) adminMenu.className = "hidden"
    }

    return (
        <form onSubmit={(e) => { edit(e) }} className="z-999 bg-white border-1 border-gray-200 w-62 h-62 rounded-lg drop-shadow-md flex flex-col items-center justify-center space-y-4">
            <div className="flex flex-col space-y-2">
                <label className="text-gray-400">{translations["current name"]}</label>
                <p>{group.title}</p>
                <label className="text-gray-400">{translations["new name"]}</label>
                <input
                    className="focus:outline-none border-b-2 border-gray-400 text-center focus:border-b-2 focus:border-orange-600"
                    value={title}
                    type="text"
                    onChange={(e) => { setTitle(e.target.value) }}
                    placeholder="General Chat .." />
            </div>
            <div className="w-full flex space-x-3 items-center justify-center">
                <button onClick={(e) => {
                    e.preventDefault()
                    closeDialog()
                }} className="w-1/3 rounded-md h-10 bg-orange-600 text-white hover:bg-orange-300 hover:text-black">{translations.cancel}</button>
                <button className="w-1/3 rounded-md h-10 bg-orange-600 text-white hover:bg-orange-300 hover:text-black">{translations.submit}</button>
            </div>
        </form>
    )
}