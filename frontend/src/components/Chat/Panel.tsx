//@ts-expect-error
// Providing a function and can not specify the type
export default function Panel({ socket, group, displayMessage, messages }) {
    const _socket: WebSocket = socket
    _socket.onmessage = (event) => {
        console.log(event.data)
        const data = JSON.parse(event.data)
        console.log(data)
        // // insert message into the list of messages for the group
        displayMessage(data)
        messages.push(event.data)
        console.log(messages)
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
