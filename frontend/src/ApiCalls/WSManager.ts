export class WebSocketManager {
    private static instance: WebSocketManager;
    private socket: WebSocket | null;
    private constructor() {
        this.socket = null
    }
    static getInstance(user: any, group: any) {
        if (WebSocketManager.instance) {
            return this.instance
        }
        this.instance = new WebSocketManager()
        this.instance.socket = new WebSocket(`ws:/127.0.0.1:8000/ws/${user.id}/${user.username}/${group.admin_id}`)
        return this.instance
    }

    getSocket() {
        return this.socket
    }
}