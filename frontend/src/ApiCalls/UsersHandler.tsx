import RoutersHandler from "./RouterHandler";

export default class UsersHandler {
    register(url: string, data: any) {
        const handler = new RoutersHandler()
        return handler.post(url, data)
    }

    verify(url: string, data: any) {
        const handler = new RoutersHandler()
        return handler.post(url, data)
    }

    login(url: string, data: any) {
        const handler = new RoutersHandler()
        return handler.post(url, data)
    }
}