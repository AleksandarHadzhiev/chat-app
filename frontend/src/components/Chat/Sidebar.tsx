import GroupsHandler from "@/ApiCalls/GroupsHandler"
import { Key, useEffect, useState } from "react"
//@ts-expect-error
// Providing a function and can not specify the type
export default function Sidebar({ isvisible, setIsVisible, id, setGroup, displayMessages, group }) {
    const handler = new GroupsHandler()
    const [groups, setGroups] = useState([])
    useEffect(() => {
        async function getAllGroupsForUser(id: Number) {
            const url = `http://localhost:8000/groups/user/${id}`
            const groups = await handler.getGroupsWhereUserIsAMember(url)
            setGroups(groups)
        }
        getAllGroupsForUser(id)
    }, [id, groups.length])

    function changeChat(_group: any) {
        if (_group.id != group.id) {
            displayMessages(_group.id)
        }
        setGroup(_group)
    }


    return (
        <div className={isvisible ? "flex flex-col w-[300px] h-full border-r-2 border-gray-200" : "w-[60px] h-1/20 border-r-2 border-gray=400 h-full"}>
            {
                isvisible ? (
                    <div className="flex flex-col w-full h-full">
                        <div className="flex w-full h-1/15 border-b-2 border-gray-200">
                            {/* Search bar */}
                            <div onClick={() => { setIsVisible(!isvisible) }} className="w-1/6 h-full flex items-center justify-center hover:text-orange-500 hover:drop-shadow-md">
                                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth="1.5" stroke="currentColor" className="size-6">
                                    <path strokeLinecap="round" strokeLinejoin="round" d="M3.75 6.75h16.5M3.75 12h16.5m-16.5 5.25h16.5" />
                                </svg>
                            </div>
                            <div className="w-5/6 h-full flex items-center justify-center pr-2">
                                <input
                                    className="bg-gray-200 w-full pl-4 h-4/5 rounded-4xl focus:outline-none text-black"
                                    placeholder="Search..."
                                />
                            </div>
                        </div>
                        <div className="w-full h-14/15 flex flex-col space-y-1 overflow-y-auto">
                            {groups && groups.length != 0 ? groups.map((_group: any, key: Key) => {
                                return (
                                    <div onClick={() => { changeChat(_group) }} key={key} className="w-full flex h-1/10 border-1 border-gray-400 hover:border-orange-300" id="global-group">
                                        < div className="w-2/3 pl-4 pt-2 h-full" >
                                            <p className="text-base text-black">{_group.title}</p>
                                            <p className="text-sm text-gray-400">Last message</p>
                                        </div>
                                        <div className="w-1/3 h-full pt-2 text-sm/6 text-orange-300">
                                            <p>22:01</p>
                                        </div>
                                    </div>
                                )
                            }) : (<p>Loading...</p>)}
                        </div>
                    </div >
                ) : (
                    <div onClick={() => { setGroup(1) }} className="w-full h-full space-y-2 items-center justify-center">
                        {/* {
                            groups && groups.length != 0 ? groups.map((group: any, key: Key) => {
                                return (
                                    <div key={key} className="w-full h-full space-y-2 items-center justify-center">
                                        <div onClick={() => { setIsVisible(!isvisible) }} className="w-full h-1/15 flex items-center justify-center hover:text-orange-500 hover:drop-shadow-md border-b-2 border-gray-400">
                                            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth="1.5" stroke="currentColor" className="size-6">
                                                <path strokeLinecap="round" strokeLinejoin="round" d="M3.75 6.75h16.5M3.75 12h16.5m-16.5 5.25h16.5" />
                                            </svg>
                                        </div>
                                        <div className="flex items-center justify-center ">
                                            <div className="w-[40px] h-[40px] border-2 border-gray-400 flex items-center justify-center hover:text-white hover:bg-orange-600 rounded-full">
                                                <p>{group.title.charAt(0)}</p>
                                            </div>
                                        </div>
                                    </div>
                                )
                            }) : <p>Loading...</p>
                        } */}
                    </div>
                )
            }
        </div >
    )
}