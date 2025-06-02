import { EditMessageDTO } from "./DTOs/Other/EditMessageDTO";
import { MessageDTO } from "./DTOs/Other/MessageDTO";
import RoutersHandler from "./RouterHandler";

export default class MessagesHandler {

    createMessage(message: {
        type: string,
        data: MessageDTO
    }, socket: WebSocket) {
        if (message && message.type && message.type == "message") {
            message.data.created_at = new Date().toISOString()
            socket.send(JSON.stringify(message))
            return true
        }
        return false
    }


    async editAMessage(data: EditMessageDTO, translations: any) {
        const access_token = localStorage.getItem("access_token")
        const header = {
            "Authorization": access_token
        }
        const handler = new RoutersHandler()
        const endpoint = `messages`
        const response = await handler.put(endpoint, data, header)
        return this.notificationHandler(response, translations)
    }

    async deleteAMessage(code: string, userId: any, groupId: any, translations: any) {
        const access_token = localStorage.getItem("access_token")
        const header = {
            "Authorization": access_token
        }
        const handler = new RoutersHandler()
        const endpoint = `messages?code=${code}&user_id=${userId}&group_id=${groupId}`
        const response = await handler.delete(endpoint, header)
        return this.notificationHandler(response, translations)
    }

    async getAllMessages(groupId: any) {
        const access_token = localStorage.getItem("access_token")
        const header = {
            "Authorization": access_token
        }
        const endpoint = `messages/${groupId}`
        const handler = new RoutersHandler()
        const response = await handler.get(endpoint, header)
        return this.handleGetResponse(response)
    }

    private handleGetResponse(response: any) {
        if ("fail" in response && response.fail === "Unauthorized") {
            return {
                "tag": "redirect"
            }
        }
        else if ("messages" in response) return response.messages
        else return []
    }

    async getLastMessage(groupId: any) {
        const access_token = localStorage.getItem("access_token")
        const header = {
            "Authorization": access_token
        }
        const handler = new RoutersHandler()
        const endpoint = `messages/${groupId}/last-message`
        const response = await handler.get(endpoint, header)
        return this.handleGetResponse(response)
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
            if ("Unauthorized" in errors) {
                return {
                    tag: "redirect"
                }
            }
            else if (typeof errors === "string")
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