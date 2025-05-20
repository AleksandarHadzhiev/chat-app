import RoutersHandler from "./RouterHandler";
import { GeneralGroupDTO } from "./DTOs/Other/GeneralGroupDTO";

export default class GroupsHandler {
    async createGroup(url: string, data: GeneralGroupDTO, translations: any) {
        const handler = new RoutersHandler()
        const response = await handler.post(url, data)
        return this.notificationHandler(response, translations)
    }

    async deleteGroup(url: string, translations: any) {
        const handler = new RoutersHandler()
        const response = await handler.delete(url)
        return this.notificationHandler(response, translations)
    }

    async editGroup(url: string, data: GeneralGroupDTO, translations: any) {
        const handler = new RoutersHandler()
        const response = await handler.put(url, data)
        return this.notificationHandler(response, translations)
    }

    async getAllGroups(url: string) {
        const handler = new RoutersHandler()
        const response = await handler.get(url)
        return this.handleGetResponse(response)
    }

    async getGroupsWhereUserIsAMember(url: string) {
        const handler = new RoutersHandler()
        const response = await handler.get(url)
        return this.handleGetResponse(response)
    }

    private handleGetResponse(response: any) {
        if ("groups" in response) return response.groups
        else return []
    }

    async joinGroup(url: string, translations: any) {
        const handler = new RoutersHandler()
        const response = await handler.post(url, null)
        return this.notificationHandler(response, translations)

    }

    async leaveGroup(url: string, translations: any) {
        const handler = new RoutersHandler()
        const response = await handler.post(url, null)
        return this.notificationHandler(response, translations)
    }

    async kickMemberFromGroup(url: string, tranlations: any) {
        const handler = new RoutersHandler()
        const response = await handler.delete(url)
        return this.notificationHandler(response, tranlations)
    }

    private notificationHandler(response: any, translations: any) {
        if ("message" in response) {
            const message = translations[response.message]
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
