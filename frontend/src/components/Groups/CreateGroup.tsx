import { useRouter } from "next/navigation"
import { FormEvent, useState } from "react"
import { GeneralGroupDTO } from "@/ApiCalls/DTOs/Other/GeneralGroupDTO"
import GroupsHandler from "@/ApiCalls/GroupsHandler"
//@ts-expect-error
// Providing a function and can not specify the type
export default function CreateGroup({ triggerUpdate, closeDialog, getAllGroups, translations, setNotificaiton, setResponse }) {
    // For the elements of translations 
    const [title, setTitle] = useState("")
    const router = useRouter()
    const handler = new GroupsHandler()
    async function create(e: FormEvent<HTMLFormElement>) {
        e.preventDefault()
        const userStringed = localStorage.getItem("user")
        if (userStringed) {
            const user = JSON.parse(userStringed)
            const createGroupDTO: GeneralGroupDTO = {
                title: title,
                admin: user.id
            }
            const response = await handler.createGroup(createGroupDTO, translations)
            if ("tag" in response) {
                setNotificaiton(response.message)
                setResponse(response.tag)
                triggerUpdate(null)
            }
            await getAllGroups();
            closeDialog()
        }
        else {
            router.push("/")
        }
    }

    return (
        <form onSubmit={(e) => { create(e) }} className="z-999 bg-white border-1 border-gray-200 w-62 h-62 rounded-lg drop-shadow-md flex flex-col items-center justify-center space-y-4">
            <div className="flex flex-col space-y-2">
                <label className="text-gray-400">{translations.name} </label>
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