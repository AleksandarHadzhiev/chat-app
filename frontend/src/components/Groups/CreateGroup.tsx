import axios from "axios"
import { useRouter } from "next/navigation"
import { FormEvent, useState } from "react"

//@ts-expect-error
// Providing a function and can not specify the type
export default function CreateGroup({ closeDialog }) {
    const [title, setTitle] = useState("")
    const router = useRouter()

    function create(e: FormEvent<HTMLFormElement>) {
        e.preventDefault()
        const userStringed = localStorage.getItem("user")
        if (userStringed) {
            const user = JSON.parse(userStringed)
            axios.post("http://localhost:8000/groups/", { title: title, admin: user.id })
                .then((res) => { console.log(res.status) })
                .catch((error) => { console.log(error) })
            closeDialog()
        }
        else {
            router.push("/")
        }
    }
    return (
        <form onSubmit={(e) => { create(e) }} className="bg-white border-1 border-gray-200 w-62 h-62 rounded-lg drop-shadow-md flex flex-col items-center justify-center space-y-4">
            <div className="flex flex-col space-y-1">
                <label>Name: </label>
                <input
                    className="focus:outline-none border-b-2 border-gray-400 text-center focus:border-b-2 focus:border-orange-600"
                    value={title}
                    type="text"
                    onChange={(e) => { setTitle(e.target.value) }}
                    placeholder="General Chat .." />
            </div>
            <button className="w-42 rounded-md h-10 bg-orange-600 text-white hover:bg-orange-300 hover:text-black">Submit</button>
        </form>
    )
} 