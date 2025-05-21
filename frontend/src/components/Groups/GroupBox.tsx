import GroupsHandler from "@/ApiCalls/GroupsHandler"
import AdminMenu from "./AdminMenu"
//@ts-expect-error
// Providing a function and can not specify the type
export default function GroupBox({ widthType, groups, user, group, translations, setResponse, setNotificaiton, triggerUpdate, getAllGroups }) {

    const handler = new GroupsHandler()

    function isNotAllowedToJoin(group: any) {
        if (isAlreadyAdmin(group)) return true
        else if (isAlreadyAMember(group)) return true
        else return false
    }

    function isAlreadyAdmin(group: any) {
        if (group.admin_id === user.id) {
            return true
        }
        return false
    }

    function isAlreadyAMember(group: any) {
        let isMember = false
        group.members.forEach((member: { id: Number, name: String }) => {
            if (member.id == user.id) {
                isMember = true
            }
        })
        return isMember
    }

    async function joinGroup(group_id: Number) {
        const url = `http://localhost:8000/groups/${user.id}/join/${group_id}`
        const response = await handler.joinGroup(url, translations)
        triggerUpdate(group_id)

        if ("tag" in response) {
            setNotificaiton(response.message)
            setResponse(response.tag)
        }
        await getAllGroups()
    }

    async function leaveGroup(group: any) {
        const url = `http://localhost:8000/groups/${user.id}/leave/${group.id}`
        const response = await handler.leaveGroup(url, translations)
        if ("tag" in response) {
            setNotificaiton(response.message)
            setResponse(response.tag)
            triggerUpdate(group.id)
        }
        await getAllGroups()
    }

    async function adminMenuSwitcher(group: any) {
        const adminMenu = document.getElementById(`${group.id}`)
        if (adminMenu && adminMenu.className == "hidden") {
            closeAdminMenuForOtherGroups()
            adminMenu.className = `${widthType == "mobile" ? "absolute left-35 bg-orange-600 text-white border-2 border-black rounded-md" : "absolute ml-[12%] border-solid border-2 border-black text-black"} w-42 h-26`
        }
        else if (adminMenu) adminMenu.className = "hidden"
    }

    async function closeAdminMenuForOtherGroups() {
        groups.forEach((group: any) => {
            const adminMenu = document.getElementById(`${group.id}`)
            if (adminMenu && adminMenu.className != "hidden")
                adminMenu.className = 'hidden'
        })
    }

    return (
        <>
            <div className={`${widthType == "mobile" ? "w-full" : "w-2/3"} pl-1 pt-2 h-full`} >
                <p className={`${widthType == "mobile" ? "text-xl" : "text-base "} text-base text-black`}>{group.title}</p>
                <p className={`${widthType == "mobile" ? "text-md" : "text-base "} text-base text-gray-400`}>{translations.members} {group.members.length}</p>
            </div>
            <div className={` ${widthType == "mobile" ? "w-[70%]" : "w-1/3"} h-full text-sm/6 text-orange-300 mr-1`}>
                {
                    isAlreadyAdmin(group) ? (
                        <div className="flex flex-row">
                            <div onClick={() => { adminMenuSwitcher(group) }} className="flex w-full justify-end hover:text-orange-600 pt-1">
                                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth="1.5" stroke="currentColor" className="size-6">
                                    <path strokeLinecap="round" strokeLinejoin="round" d="M9.594 3.94c.09-.542.56-.94 1.11-.94h2.593c.55 0 1.02.398 1.11.94l.213 1.281c.063.374.313.686.645.87.074.04.147.083.22.127.325.196.72.257 1.075.124l1.217-.456a1.125 1.125 0 0 1 1.37.49l1.296 2.247a1.125 1.125 0 0 1-.26 1.431l-1.003.827c-.293.241-.438.613-.43.992a7.723 7.723 0 0 1 0 .255c-.008.378.137.75.43.991l1.004.827c.424.35.534.955.26 1.43l-1.298 2.247a1.125 1.125 0 0 1-1.369.491l-1.217-.456c-.355-.133-.75-.072-1.076.124a6.47 6.47 0 0 1-.22.128c-.331.183-.581.495-.644.869l-.213 1.281c-.09.543-.56.94-1.11.94h-2.594c-.55 0-1.019-.398-1.11-.94l-.213-1.281c-.062-.374-.312-.686-.644-.87a6.52 6.52 0 0 1-.22-.127c-.325-.196-.72-.257-1.076-.124l-1.217.456a1.125 1.125 0 0 1-1.369-.49l-1.297-2.247a1.125 1.125 0 0 1 .26-1.431l1.004-.827c.292-.24.437-.613.43-.991a6.932 6.932 0 0 1 0-.255c.007-.38-.138-.751-.43-.992l-1.004-.827a1.125 1.125 0 0 1-.26-1.43l1.297-2.247a1.125 1.125 0 0 1 1.37-.491l1.216.456c.356.133.751.072 1.076-.124.072-.044.146-.086.22-.128.332-.183.582-.495.644-.869l.214-1.28Z" />
                                    <path strokeLinecap="round" strokeLinejoin="round" d="M15 12a3 3 0 1 1-6 0 3 3 0 0 1 6 0Z" />
                                </svg>
                            </div>
                            <div
                                id={`${group.id}`}
                                className="hidden">
                                <AdminMenu
                                    widthType={widthType}
                                    trigerUpdate={triggerUpdate}
                                    setResponse={setResponse}
                                    setNotificaiton={setNotificaiton}
                                    group={group}
                                    user={user}
                                    getAllGroups={getAllGroups}
                                    translations={translations} />
                            </div>
                        </div>
                    ) : null
                }
                {
                    isNotAllowedToJoin(group) ? (<button
                        onClick={() => { leaveGroup(group) }}
                        className={` ${widthType == "mobile" ? "text-xl" : " "} w-full mt-2 h-1/2 bg-orange-600 text-white rounded-md hover:bg-orange-400`}>{translations.leave}</button>) : (
                        <button
                            onClick={() => { joinGroup(group.id) }}
                            className={"w-full mt-2 h-1/2 bg-orange-600 text-white rounded-md hover:bg-orange-400"}>{translations.join}</button>
                    )
                }
            </div>
        </>
    )
}