'use client'

import Login from '@/components/Login';

export default function Home() {
  // const myuuid = uuidv4();
  // const socket = new WebSocket("ws:/127.0.0.1:8000/ws/" + myuuid)

  // socket.addEventListener('open', (event) => {
  //   console.log("Connected to server");
  // })

  // socket.addEventListener('close', (event) => {
  //   console.log("Connected to server");
  // })

  // socket.onmessage = (event) => {
  //   console.log(event.data)
  // }

  return (
    <div className="w-full h-screen bg-white">
      <Login />
    </div>
  );
}
