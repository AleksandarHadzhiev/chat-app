
//@ts-ignore
export default function RegistrationSteps({ step }) {
    const focus = "w-12 h-1 bg-orange-600"
    const notFocused = "w-12 h-1 bg-orange-300"
    const focusArrow = "size-12 text-orange-600"
    const notFocusedArrow = "size-12 text-orange-300"
    return (
        <div className="flex w-full items-center justify-center space-x-2">
            <div className="text-orange-600">
                <h3>Email</h3>
            </div>
            <div className="flex items-center justify-center">
                <div className={step < 2 ? notFocused : focus}></div>
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth="1.5" stroke="currentColor" className={step < 2 ? notFocusedArrow : focusArrow}>
                    <path strokeLinecap="round" strokeLinejoin="round" d="m8.25 4.5 7.5 7.5-7.5 7.5" />
                </svg>
            </div>
            <div className={step < 2 ? "text-orange-300" : "text-orange-600"}>
                <h3>Verification</h3>
            </div>
            <div className="flex items-center justify-center">
                <div className={step < 3 ? notFocused : focus}></div>
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth="1.5" stroke="currentColor" className={step < 3 ? notFocusedArrow : focusArrow}>
                    <path strokeLinecap="round" strokeLinejoin="round" d="m8.25 4.5 7.5 7.5-7.5 7.5" />
                </svg>
            </div>
            <div className={step < 3 ? "text-orange-300" : "text-orange-600"}>
                <h3>Password</h3>
            </div>
            <div className="flex items-center justify-center">
                <div className={step < 4 ? notFocused : focus}></div>
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth="1.5" stroke="currentColor" className={step < 4 ? notFocusedArrow : focusArrow}>
                    <path strokeLinecap="round" strokeLinejoin="round" d="m8.25 4.5 7.5 7.5-7.5 7.5" />
                </svg>
            </div>
            <div className={step < 4 ? "text-orange-300" : "text-orange-600"}>
                <h3>Username</h3>
            </div>
            <div className="flex items-center justify-center">
                <div className={step < 5 ? notFocused : focus}></div>
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth="1.5" stroke="currentColor" className={step < 5 ? notFocusedArrow : focusArrow}>
                    <path strokeLinecap="round" strokeLinejoin="round" d="m8.25 4.5 7.5 7.5-7.5 7.5" />
                </svg>
            </div>
            <div className={step < 5 ? "text-orange-300" : "text-orange-600"}>
                <h3>Confirmation</h3>
            </div>
        </div>
    )
}