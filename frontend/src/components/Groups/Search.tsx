//@ts-expect-error
// Providing a function and can not specify the type
export default function Search({ isFocued, setIsFocused, translations }) {
    return (
        <div className="w-full h-1/9 flex items-center justify-center pr-2 bg-white">
            <div className={`w-1/3 h-1/2 bg-white border-2 ${isFocued ? "border-orange-300" : "border-gray-200"} flex items-center justify-center rounded-4xl drop-shadow-md`}>
                <input
                    className=" w-4/5 pl-4 h-full rounded-4xl focus:outline-none"
                    placeholder={translations.search}
                    onFocus={() => { setIsFocused(true) }}
                    onBlur={() => { setIsFocused(false) }}
                />
                <svg
                    xmlns="http://www.w3.org/2000/svg"
                    fill="none"
                    viewBox="0 0 24 24"
                    strokeWidth="1.5"
                    stroke="currentColor"
                    className={`size-6 w-1/5 ${isFocued ? "text-orange-300" : ""}`}>
                    <path
                        strokeLinecap="round"
                        strokeLinejoin="round"
                        d="m21 21-5.197-5.197m0 0A7.5 7.5 0 1 0 5.196 5.196a7.5 7.5 0 0 0 10.607 10.607Z" />
                </svg>
            </div>
        </div>
    )
}