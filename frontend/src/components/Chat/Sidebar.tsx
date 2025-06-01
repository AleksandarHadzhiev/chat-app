import GroupsHandler from "@/ApiCalls/GroupsHandler"
import { Key, useEffect, useState } from "react"
import Chat from "./Chat"
import { useRouter } from "next/navigation";

//@ts-expect-error
// Providing a function and can not specify the type
export default function Sidebar({ isVisible, setIsVisible, id, setGroup, displayMessages, group, triggerLastMessage, translations, widthType }) {
    const handler = new GroupsHandler()
    const router = useRouter()
    const [groups, setGroups] = useState([])
    useEffect(() => {
        async function getAllGroupsForUser() {
            const groups = await handler.getGroupsWhereUserIsAMember(id)
            if ("tag" in groups)
                router.push("/login")
            else setGroups(groups)
        }
        getAllGroupsForUser()
    }, [id, groups.length])

    function changeChat(_group: any) {
        if (_group.id != group.id) {
            displayMessages(_group.id)
        }
        setGroup(_group)
    }

    function openChatOnMobileDevice(_group: any) {
        if (widthType == "mobile") {
            setGroup(_group)
            setIsVisible(false)
        }

    }

    function setSidebarStyleBasedOnDevice() {
        // Ако е на мобилен, трябва в зависимост isVisible да е Sidebar цярата страница,
        if (widthType == "mobile" && isVisible) {
            return "w-full h-full"
        }
        else if (widthType == "mobile" && !isVisible)
            return 'hidden'
        else return isVisible ? "flex flex-col w-[300px] h-full border-r-2 border-gray-200" : "w-[60px] h-1/20 border-r-2 border-gray=400 h-full"
    }

    return (
        <div className={setSidebarStyleBasedOnDevice()}>
            {
                isVisible ? (
                    <div className="flex flex-col w-full h-full">
                        <div className="flex w-full h-1/15 border-b-2 border-gray-200">
                            {/* Search bar */}
                            <div onClick={() => { setIsVisible(!isVisible) }} className="w-1/6 h-full flex items-center justify-center hover:text-orange-500 hover:drop-shadow-md">
                                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth="1.5" stroke="currentColor" className="size-6">
                                    <path strokeLinecap="round" strokeLinejoin="round" d="M3.75 6.75h16.5M3.75 12h16.5m-16.5 5.25h16.5" />
                                </svg>
                            </div>
                            <div className="w-5/6 h-full flex items-center justify-center pr-2">
                                <input
                                    className={`bg-gray-200 ${widthType == "mobile" ? 'text-2xl' : ''} w-full pl-4 h-4/5 rounded-4xl focus:outline-none text-black`}
                                    placeholder={translations.search}
                                />
                            </div>
                        </div>
                        <div className="w-full h-14/15 flex flex-col space-y-1 overflow-y-auto">
                            {groups && groups.length != 0 ? groups.map((_group: any, key: Key) => {
                                return (
                                    <div onClick={() => { openChatOnMobileDevice(_group) }} key={key}>
                                        <Chat
                                            widthType={widthType}
                                            triggerLastMessage={triggerLastMessage}
                                            key={key}
                                            _group={_group}
                                            changeChat={changeChat}
                                            isVisible={isVisible} />
                                    </div>)
                            }) : (<p>Loading...</p>)}
                        </div>
                    </div >
                ) : (
                    <div className="w-full h-full space-y-2 items-center justify-center">
                        <div onClick={() => { setIsVisible(!isVisible) }} className="w-full h-1/15 flex items-center justify-center hover:text-orange-500 hover:drop-shadow-md border-b-2 border-gray-400">
                            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth="1.5" stroke="currentColor" className="size-6">
                                <path strokeLinecap="round" strokeLinejoin="round" d="M3.75 6.75h16.5M3.75 12h16.5m-16.5 5.25h16.5" />
                            </svg>
                        </div>
                        {
                            groups && groups.length != 0 ? groups.map((_group: any, key: Key) => {
                                return (
                                    <div key={key}>
                                        <Chat
                                            widthType={widthType}
                                            triggerLastMessage={triggerLastMessage}
                                            key={key}
                                            _group={_group}
                                            changeChat={changeChat}
                                            isVisible={isVisible} />
                                    </div>)
                            }) : <p>Loading...</p>
                        }
                    </div>
                )
            }
        </div >
    )
}