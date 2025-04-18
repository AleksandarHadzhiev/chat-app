"use client"
import { Key, useEffect, useState } from "react"
import CreateGroup from "./CreateGroup"
import axios from "axios"
import Search from "./Search"

export default function Groups() {
    const [isFocued, setIsFocused] = useState(false)
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
        console.log(isOpenDialog)
    }

    function closeDialog() {
        setOpenDialog(false)
        console.log(isOpenDialog)
    }

    function joinServer(group_id: Number) {
        axios.post(`http://localhost:8000/groups/${user.id}/join/${group_id}`)
            .then((res) => {
                console.log(res.status)
                console.log(res)
            })
            .catch((err) => {
                console.log(err)
            })
    }

    function getAllGroups() {
        axios.get("http://localhost:8000/groups/").then((response) => {
            setGroups(response.data.groups)
        }).catch((error) => {
            console.log(error)
        })
    }

    useEffect(() => {
        const userStringed = localStorage.getItem("user")
        if (userStringed) {
            setUser(JSON.parse(userStringed))
        }
        getAllGroups()
    }, [user.id, groups.length])

    return (
        <div className="w-full h-full flex flex-col">
            <Search setIsFocused={setIsFocused} isFocued={isFocued} />
            <div className={`${groups ? "w-full h-4/9 flex flex-col space-y-2" : "hidden"}`}>
                {/* Groups */}
                {groups && groups.length != 0 ? groups.map((group: any, key: Key) => {
                    return (
                        <div key={key} className="ml-2 w-1/3 flex h-1/4 border-1 border-gray-400 hover:border-orange-300" id="global-group">
                            < div className="w-2/3 pl-4 pt-2 h-full" >
                                <p className="text-base text-black">{group.title}</p>
                                <p className="text-sm text-gray-400">Last message</p>
                            </div>
                            <div className="w-1/3 h-full pt-2 text-sm/6 text-orange-300 mr-1 mt-2">
                                <button
                                    onClick={() => { joinServer(group.id) }}
                                    className="w-full h-1/2 bg-orange-600 text-white rounded-md hover:bg-orange-400">Join</button>
                            </div>
                        </div>
                    )
                }) : (<p>Loading...</p>)}
            </div>
            <div className={`${isOpenDialog ? 'fixed flex items-center justify-center inset-0 bg-gray-500/75 ' : "hidden"} `}>
                <div onClick={() => { closeDialog() }} className="absolute top-0 w-screen h-screen transition-opacity flex items-center justify-center">
                </div>
                <CreateGroup closeDialog={closeDialog} />
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
                <div onClick={() => { openDialog() }} className="h-1/2 w-1/4 rounded-4xl drop-shadow-md border-2 border-gray-200 hover:border-orange-300 text-orange-300 hover:text-orange-400">
                    <button className="w-full h-full flex flex items-center justify-center">
                        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth="1.5" stroke="currentColor" className="size-24">
                            <path strokeLinecap="round" strokeLinejoin="round" d="M12 9v6m3-3H9m12 0a9 9 0 1 1-18 0 9 9 0 0 1 18 0Z" />
                        </svg>
                    </button>
                </div>
            </div>

        </div>
    )
}