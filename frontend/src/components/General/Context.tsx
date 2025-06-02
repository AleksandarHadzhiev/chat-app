import { createContext } from "react"

const ChildContext = createContext({ language: "", isVisible: false, widthType: "desktop", trigered: false, setTrigered: function (data: boolean) { this.trigered = data } })
export default ChildContext
