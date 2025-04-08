//@ts-expect-error
// Providing a function and can not specify the type
export default function Notification({ notification, response }) {
    return (
        <div className={response == "" ? "hidden" : `w-fill h-[5%] flex flex-col bg-white border-2 ${response == "success" ? "border-green-700" : "border-red-700"} absolute top-20 right-5 drop-shadow-md transition duration-2000`}>
            <div className="h-full w-full flex">
                <div className="w-fill flex items-center justify-center h-full">
                    {response == "success" ? (
                        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth="1.5" stroke="currentColor" className="size-6 text-green-700">
                            <path strokeLinecap="round" strokeLinejoin="round" d="M9 12.75 11.25 15 15 9.75M21 12a9 9 0 1 1-18 0 9 9 0 0 1 18 0Z" />
                        </svg>

                    ) : (
                        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth="1.5" stroke="currentColor" className="size-6 text-red-600">
                            <path strokeLinecap="round" strokeLinejoin="round" d="M12 9v3.75m9-.75a9 9 0 1 1-18 0 9 9 0 0 1 18 0Zm-9 3.75h.008v.008H12v-.008Z" />
                        </svg>

                    )}
                </div>
                <p className="pl-1 pr-1 pt-1 w-full h-5/6">{notification}</p>
            </div>
            <div className={`h-1/6 w-full ${response == "success" ? "bg-green-700" : "bg-red-700"}`}></div>
        </div>
    )
}