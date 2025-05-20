"use client"

import RefactorMessageContent from "./RefactorContent"

//@ts-expect-error
// Providing a function and can not specify the type
export default function UpdateMessage({ widthType, code, content, setEditMessage, setTriggerOff, trigger, socket, translations }) {

    function setStyleBasedOnDevice() {
        // 
    }

    return (
        <>
            <div className={`${widthType == "mobile" ? "text-2xl" : ""} flex w-full h-1/10 drop-shadow-md border-t-2 border-gray-200`}>
                <div className={`${widthType == "mobile" ? 'w-3/30' : "1/30"} h-full flex items-center justify-center text-black hover:text-orange-500 hover:drop-shadow-md`}>
                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth="1.5" stroke="currentColor" className={`${widthType == "mobile" ? 'size-12' : "size-6"} ml-1`}>
                        <path strokeLinecap="round" strokeLinejoin="round" d="m16.862 4.487 1.687-1.688a1.875 1.875 0 1 1 2.652 2.652L6.832 19.82a4.5 4.5 0 0 1-1.897 1.13l-2.685.8.8-2.685a4.5 4.5 0 0 1 1.13-1.897L16.863 4.487Zm0 0L19.5 7.125" />
                    </svg>
                </div>
                <div className={`${widthType == "mobile" ? 'w-24/30' : "1/30"} flex flex-col h-full`}>
                    <p className="text-orange-600 pl-2">{translations.refactor}</p>
                    <p
                        id="msg-input"
                        className="w-full h-full pl-2 focus:outline-none overflow-x-auto"
                    >{String(content).replace("<br/>", "")}
                    </p>
                </div>
                <button
                    onClick={() => { setEditMessage(false) }}
                    className={`${widthType == "mobile" ? 'w-3/30' : "1/30"} h-full flex items-center justify-center text-orange-500 hover:text-orange-300 hover:drop-shadow-md`}>
                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth="1.5" stroke="currentColor" className={`${widthType == "mobile" ? 'size-12' : "size-6"}`}>
                        <path strokeLinecap="round" strokeLinejoin="round" d="m9.75 9.75 4.5 4.5m0-4.5-4.5 4.5M21 12a9 9 0 1 1-18 0 9 9 0 0 1 18 0Z" />
                    </svg>
                </button>
            </div >
            <RefactorMessageContent
                widthType={widthType}
                translations={translations}
                socket={socket}
                trigger={trigger}
                setTriggerOff={setTriggerOff}
                setEditMessage={setEditMessage}
                code={code}
                message={content} />
        </>
    )
}

