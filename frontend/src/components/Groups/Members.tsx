import axios from "axios"
import { FormEvent, Key, MouseEvent } from "react"

//@ts-expect-error
// Providing a function and can not specify the type
export default function MembersDialog({ closeDialog, getAllGroups, group, user, translations }) {

    function kickMemberOut(e: MouseEvent<HTMLButtonElement, globalThis.MouseEvent>, member: Number) {
        e.preventDefault()
        axios.delete(`http://localhost:8000/groups/${group.id}/kick/${member}/${user.id}`)
            .then((res) => { console.log(res.status); getAllGroups(); })
            .catch((error) => { console.log(error) })
        closeDialog()
    }

    function disaplyRole(adminId: Number, memberId: Number) {
        if (adminId == memberId)
            return "Admin"
        return "Member"
    }

    return (
        <div className="z-999 relative overflow-x-auto border-2 border-black">
            <table className="w-full text-sm text-left rtl:text-right text-gray-500 ">
                <thead className="text-xs text-orange-600 uppercase bg-white">
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