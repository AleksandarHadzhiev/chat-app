//@ts-expect-error
// Providing a function and can not specify the type
export default function MobileNavigation({ setIsVisible, isVisible }) {
    return (
        <div className="w-full h-full flex bg-white items-center justify-center">
            <button onClick={() => { setIsVisible(!isVisible) }} className="w-5/7 h-full text-orange-300">
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth="1.5" stroke="currentColor" className="size-6">
                    <path strokeLinecap="round" strokeLinejoin="round" d="M3.75 6.75h16.5M3.75 12h16.5m-16.5 5.25h16.5" />
                </svg>
            </button>
        </div>
    )
}