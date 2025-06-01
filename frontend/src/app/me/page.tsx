"use client"

import UsersHandler from "@/ApiCalls/UsersHandler"
import { useRouter } from "next/navigation"
import { useEffect } from "react"

export default function AccountPage() {
    const router = useRouter()
    useEffect(() => {
        async function getUser() {
            const handler = new UsersHandler()
            const data = await handler.getIdentity()
            if ("tag" in data) {
                router.push("/login")
            }
            localStorage.setItem("user", JSON.stringify(data))
        }
        getUser()
    }, [])
    return (
        <div className="w-full h-full bg-white">
            <p>Account page</p>
        </div>
    )
}