export default function ProvdePassword() {
    return (
        <div className="w-full h-1/2 flex flex-col items-center justify-center">
            <div className="flex flex-col space-y-3">
                <label htmlFor="password">Password</label>
                <div className="flex w-full border-2 border-solid">
                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth="1.5" stroke="currentColor" className="size-6 border-r-2 border-black bg-orange-600 text-white">
                        <path strokeLinecap="round" strokeLinejoin="round" d="M16.5 10.5V6.75a4.5 4.5 0 1 0-9 0v3.75m-.75 11.25h10.5a2.25 2.25 0 0 0 2.25-2.25v-6.75a2.25 2.25 0 0 0-2.25-2.25H6.75a2.25 2.25 0 0 0-2.25 2.25v6.75a2.25 2.25 0 0 0 2.25 2.25Z" />
                    </svg>
                    <input className="" type="password" name="password" placeholder="Password" />
                </div>
            </div>
        </div>
    )
}