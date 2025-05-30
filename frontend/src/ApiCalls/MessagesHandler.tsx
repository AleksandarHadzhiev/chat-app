import { EditMessageDTO } from "./DTOs/Other/EditMessageDTO";
import { MessageDTO } from "./DTOs/Other/MessageDTO";
import RoutersHandler from "./RouterHandler";

export default class MessagesHandler {

    createMessage(message: {
        type: String,
        data: MessageDTO
    }, socket: WebSocket) {
        if (message && message.type && message.type == "message" && message.data.code) {
            message.data.code = this.generateSpecialCode(message.data)
            message.data.created_at = new Date().toISOString()
            socket.send(JSON.stringify(message))
            return true
        }
        return false
    }

    private generateSpecialCode(data: MessageDTO) {
        const date = new Date()
        const spesialElement = date.toISOString().replace(":", "-")

        const customeCode = `${data.user_id}-${data.group_id}-${spesialElement}`
        return customeCode
    }

    async editAMessage(data: EditMessageDTO, translations: any) {
        const handler = new RoutersHandler()
        const endpoint = `messages`
        const response = await handler.put(endpoint, data)
        return this.notificationHandler(response, translations)
    }

    async deleteAMessage(code: string, userId: any, groupId: any, translations: any) {

        const handler = new RoutersHandler()
        const endpoint = `messages?code=${code}&user_id=${userId}&group_id=${groupId}`
        const response = await handler.delete(endpoint)
        return this.notificationHandler(response, translations)
    }

    async getAllMessages(groupId: any) {
        const endpoint = `messages/${groupId}`
        const handler = new RoutersHandler()
        const response = await handler.get(endpoint)
        console.log(response)
        if ("messages" in response) return response.messages
        else return []
    }

    async getLastMessage(groupId: any) {
        const handler = new RoutersHandler()
        const endpoint = `messages/${groupId}/last-message`
        const response = await handler.get(endpoint)
        if ("message" in response) return response.message
        else return []
    }

    private notificationHandler(response: any, translations: any) {
        if ("message" in response) {
            const message = response.message // FOR NOW
            return {
                tag: "success",
                message: message
            }
        } else if ("fail" in response) {
            let errorMessage = translations.fail
            const errors = response.fail
            if (typeof errors === "string")
                return {
                    tag: "fail",
                    message: translations[errors]
                }
            errors.forEach((error: string) => {
                errorMessage += `${translations[error]}, `
            });
            return {
                tag: "fail",
                message: errorMessage
            }
        } else if ("error" in response) {
            const message = translations[response.error]
            return {
                tag: "fail",
                message: message
            }
        }
        return response
    }
}