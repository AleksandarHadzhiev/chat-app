import { createContext } from "react"

const ChildContext = createContext({ language: "", isVisible: false, widthType: "desktop", socket: null })
export default ChildContext
