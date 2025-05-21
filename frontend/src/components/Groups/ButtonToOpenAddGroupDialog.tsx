//@ts-expect-error
// Providing a function and can not specify the type
export default function ButtonToOpenAddGroupDialog({ openDialog, widthType, isOpenDialog }) {
    return (
        <div className={`${isOpenDialog ? "hidden" : `w-full ${widthType == "mobile" ? "h-2/9" : "h-4/9"} flex items-center justify-center`}`}>
            {widthType == "mobile" ? (
                <div
                    onClick={() => { openDialog() }}
                    className="flex flex items-center justify-center w-22 h-22 bg-white text-orange-400 rounded-full border-2 border-orange-600">
                    <div className="animate-ping">
                        <svg
                            xmlns="http://www.w3.org/2000/svg"
                            fill="none"
                            viewBox="0 0 24 24"
                            strokeWidth="1.5"
                            stroke="currentColor"
                            className="size-12">
                            <path
                                strokeLinecap="round"
                                strokeLinejoin="round"
                                d="M12 9v6m3-3H9m12 0a9 9 0 1 1-18 0 9 9 0 0 1 18 0Z" />
                        </svg>
                    </div>
                </div>)
                : (
                    <div
                        onClick={() => { openDialog() }}
                        className="h-1/2 w-1/4 rounded-4xl drop-shadow-md border-2 border-gray-200 hover:border-orange-300 text-orange-300 hover:text-orange-400">
                        <button className="w-full h-full flex flex items-center justify-center">
                            <svg
                                xmlns="http://www.w3.org/2000/svg"
                                fill="none"
                                viewBox="0 0 24 24"
                                strokeWidth="1.5"
                                stroke="currentColor"
                                className="size-12">
                                <path
                                    strokeLinecap="round"
                                    strokeLinejoin="round"
                                    d="M12 9v6m3-3H9m12 0a9 9 0 1 1-18 0 9 9 0 0 1 18 0Z" />
                            </svg>
                        </button>
                    </div>
                )}
        </div>
    )
}