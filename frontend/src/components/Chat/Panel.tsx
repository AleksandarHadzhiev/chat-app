//@ts-expect-error
// Providing a function and can not specify the type
export default function Panel({ socket, group, displayMessage }) {


    const _socket: WebSocket = socket
    _socket.onmessage = (event) => {
        const text = String(event.data)
        console.log(event.data)
        const index = text.indexOf(":")
        console.log(text)
        const messageWithoutAuthor = text.replace(text.substring(0, index + 2), "")
        const author = text.replace(text.substring(index, text.length), "")
        displayMessage(author, messageWithoutAuthor)
    }

    return (
        <div className="flex flex-col w-full h-9/10">
            <div className="flex flex-col space-y-1 w-full h-1/10 border-b border-gray-200 pl-2 pt-1">
                <h1>{group.title}</h1>
            </div>
            <div id={"panel"} className="w-full h-9/10 overflow-y-auto"></div>
        </div >
    )
}