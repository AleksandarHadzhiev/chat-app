"use client"

import ResetPassword from "@/components/User/ResetPassword"
import { Suspense } from "react"

export default function ResetPasswordPage() {

    return (
        <div className="bg-white w-full h-ull flex flex-col items-center justify-center text-black">
            <Suspense>
                <ResetPassword />
            </Suspense>
        </div>
    )
}