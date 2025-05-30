import GroupsHandler from "@/ApiCalls/GroupsHandler"
import { Key, MouseEvent } from "react"

//@ts-expect-error
// Providing a function and can not specify the type
export default function MembersDialog({ trigerUpdate, closeDialog, getAllGroups, group, user, translations, setNotificaiton, setResponse }) {
    const handler = new GroupsHandler()
    async function kickMemberOut(e: MouseEvent<HTMLButtonElement, globalThis.MouseEvent>, member: Number) {
        e.preventDefault()
        const response = await handler.kickMemberFromGroup(group.id, user.id, member, translations)
        if ("tag" in response) {
            setNotificaiton(response.message)
            setResponse(response.tag)
            trigerUpdate(group.id)

        }
        await getAllGroups()
        closeDialog()
        const adminMenu = document.getElementById(`${group.id}`)
        if (adminMenu) adminMenu.className = "hidden"
    }

    function disaplyRole(adminId: Number, memberId: Number) {
        if (adminId == memberId)
            return "Admin"
        return "Member"
    }

    return (
        <div className="flex flex-col z-999 relative overflow-x-auto border-2 border-black bg-white">
            <div onClick={() => { closeDialog() }} id="close-button" className="w-full h-6 flex justify-end text-red-600 hover:text-black">
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth="1.5" stroke="currentColor" className="size-6 border-l-2 border-black">
                    <path strokeLinecap="round" strokeLinejoin="round" d="m9.75 9.75 4.5 4.5m0-4.5-4.5 4.5M21 12a9 9 0 1 1-18 0 9 9 0 0 1 18 0Z" />
                </svg>
            </div>
            <table className="w-full text-sm text-left rtl:text-right text-gray-500">
                <thead className="text-xs text-orange-600 uppercase bg-white border-t-2 border-black">
                    <tr>
                        <th scope="col" className="px-6 py-3 border-r-2 border-gray-500 border-b-2">
                            Nr.
                        </th>
                        <th scope="col" className="px-6 py-3 border-r-2 border-gray-500 border-b-2">
                            {translations.role}
                        </th>
                        <th scope="col" className="px-6 py-3 border-r-2 border-gray-500 border-b-2">
                            {translations.name}
                        </th>
                        <th scope="col" className="px-6 py-3 border-b-2 border-gray-500">
                            {translations.actions}
                        </th>
                    </tr>
                </thead>
                <tbody>
                    {group && group.members != 0 ? group.members.map((member: any, key: Key) => {
                        return (
                            <tr key={key} className="bg-white border-b border-gray-400 hover:bg-gray-300">
                                <th scope="row" className="px-6 py-4 font-medium text-gray-900 whitespace-nowrap border-gray-400 border-r">
                                    {Number(key.toString()) + 1}
                                </th>
                                <th scope="row" className="px-6 py-4 border-gray-400 border-r">
                                    {disaplyRole(group.admin_id, member.id)}
                                </th>
                                <td className="px-6 py-4 border-gray-400 border-r">
                                    {member.name}
                                </td>
                                <td className="px-6 py-4">
                                    <button
                                        onClick={(e) => { kickMemberOut(e, member.id) }}
                                        className="hover:text-orange-600">
                                        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth="1.5" stroke="currentColor" className="size-6">
                                            <path strokeLinecap="round" strokeLinejoin="round" d="M22 10.5h-6m-2.25-4.125a3.375 3.375 0 1 1-6.75 0 3.375 3.375 0 0 1 6.75 0ZM4 19.235v-.11a6.375 6.375 0 0 1 12.75 0v.109A12.318 12.318 0 0 1 10.374 21c-2.331 0-4.512-.645-6.374-1.766Z" />
                                        </svg>
                                    </button>
                                </td>
                            </tr>
                        )
                    }) : (<p>Loading...</p>)}
                </tbody>
            </table>
        </div>
    )
}