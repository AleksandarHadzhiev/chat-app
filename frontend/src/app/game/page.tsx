"use client"

export default function GamePage() {

    const charachter = document.getElementById("character")
    if (charachter) {
        charachter.className = "text-white"
        charachter.textContent = `
           |^^^^^^|    
          <|--<>--|>                
           |__--__|         
         ____|  |____
        | |   __   | |
        | |   __   | |
        | |   __   | |
        |_|  ____  |_|
           | |   | |
           | |   | |
           | |   | |
           |_|   |_|
        `
    }

    return (
        <div id="board" className="w-full h-full bg-black flex flex-col items-center justify-center">
            <div id="charachter" className="text-white">|^^^^|</div>
            <div className="text-white">{"   <|-<>-|>"}</div>
            <div className="text-white">{"    |_--_|"}</div>
            <div className="text-white">{"   __|  |__"}</div>
            <div className="text-white">{"|_|   __   |_|"}</div>
            <div className="text-white">{"|_|   __   |_|"}</div>
            <div className="text-white">{"|_|   __   |_|"}</div>
            <div className="text-white">{"|_|   __  |_|"}</div>
            <div className="text-white">{"|_|   |_|"}</div>
            <div className="text-white">{"|_|   |_|"}</div>
            <div className="text-white">{"|_|   |_|"}</div>
            <div className="text-white">{"|_|   |_|"}</div>
            <div className="text-white">{"|_|   |_|"}</div>
        </div>
    )
}