import RoutersHandler from "./RouterHandler";
import { GeneralGroupDTO } from "./DTOs/Group/GeneralGroupDTO";

export default class GroupsHandler {
    async createGroup(url: string, data: GeneralGroupDTO, translations: any) {
        const handler = new RoutersHandler()
        const response = await handler.post(url, data)
        return this.notificationHandler(response, translations)
    }

    async deleteGroup(url: string) {
        const handler = new RoutersHandler()
        const response = await handler.delete(url)
        console.log(response)
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
        console.log(response)
        if ("groups" in response) return response.groups
        else return []
    }

    async joinGroup(url: string) {
        const handler = new RoutersHandler()
        const response = await handler.post(url, null)
        console.log(response)
    }

    async leaveGroup(url: string, translations: any) {
        const handler = new RoutersHandler()
        const response = await handler.post(url, translations)
        return this.notificationHandler(response, translations)
    }

    kickMemberFromGroup() { }

    private notificationHandler(response: any, translations: any) {
        console.log(response)
        if ("message" in response) {
            console.log(response.message)
            const message = translations[response.message]
            return {
                tag: "success",
                message: message
            }
        } else if ("fail" in response) {
            let errorMessage = translations.fail
            const errrors = response.fail
            errrors.forEach((error: string) => {
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
