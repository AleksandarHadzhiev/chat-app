export default function Login() {
    return (
        <div className="bg-white w-full h-full flex flex-col items-center justify-center text-black">
            <h1 className="text-3xl text-orange-600">Welcome back</h1>
            <form className="bg-gray-200 w-82 h-82 rounded-lg">
                <div className="w-full h-1/2 flex flex-col space-y-3 items-center justify-center">
                    <div className="flex flex-col">
                        <label htmlFor="email">Email</label>
                        <div className="flex w-full border-2 border-solid">
                            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth="1.5" stroke="currentColor" className="size-6 border-r-2 border-black bg-orange-600 text-white">
                                <path strokeLinecap="round" strokeLinejoin="round" d="M21.75 6.75v10.5a2.25 2.25 0 0 1-2.25 2.25h-15a2.25 2.25 0 0 1-2.25-2.25V6.75m19.5 0A2.25 2.25 0 0 0 19.5 4.5h-15a2.25 2.25 0 0 0-2.25 2.25m19.5 0v.243a2.25 2.25 0 0 1-1.07 1.916l-7.5 4.615a2.25 2.25 0 0 1-2.36 0L3.32 8.91a2.25 2.25 0 0 1-1.07-1.916V6.75" />
                            </svg>
                            <input className="" type="email" name="email" placeholder="example@gmail.com" />
                        </div>
                    </div>
                    <div className="flex flex-col">
                        <label htmlFor="password">Password</label>
                        <div className="flex w-full border-2 border-solid">
                            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth="1.5" stroke="currentColor" className="size-6 border-r-2 border-black bg-orange-600 text-white">
                                <path strokeLinecap="round" strokeLinejoin="round" d="M16.5 10.5V6.75a4.5 4.5 0 1 0-9 0v3.75m-.75 11.25h10.5a2.25 2.25 0 0 0 2.25-2.25v-6.75a2.25 2.25 0 0 0-2.25-2.25H6.75a2.25 2.25 0 0 0-2.25 2.25v6.75a2.25 2.25 0 0 0 2.25 2.25Z" />
                            </svg>
                            <input className="" type="password" name="password" placeholder="Password..." />
                        </div>
                    </div>
                    <div className="flex">
                        <p>Forgot password? <a className="text-orange-600 hover:text-orange-700" href="/forgotPassword">Here</a></p>
                    </div>
                </div>
                <div className="w-full flex flex-col space-y-3 h-1/2 flex items-center justify-center">
                    <button className="rounded-lg bg-orange-600 w-1/2 h-1/3 hover:bg-orange-400 text-white">Sign in</button>
                    <p>You don't have an account? <a className="text-orange-600 hover:text-orange-700" href="/register">Sign up</a></p>
                </div>
            </form>
        </div>
    )
}