import RoutersHandler from "./RouterHandler";
import { GeneralGroupDTO } from "./DTOs/Other/GeneralGroupDTO";

export default class GroupsHandler {
    async createGroup(data: GeneralGroupDTO, translations: any) {
        const handler = new RoutersHandler()
        const endpoint = "groups"
        const response = await handler.post(endpoint, data)
        return this.notificationHandler(response, translations)
    }

    async deleteGroup(id: any, admin: any, translations: any) {
        const handler = new RoutersHandler()
        const endpoint = `groups/${id}/${admin}`
        const response = await handler.delete(endpoint)
        return this.notificationHandler(response, translations)
    }

    async editGroup(id: any, data: GeneralGroupDTO, translations: any) {
        const handler = new RoutersHandler()
        const endpoint = `groups/${id}`
        const response = await handler.put(endpoint, data)
        return this.notificationHandler(response, translations)
    }

    async getAllGroups() {
        const handler = new RoutersHandler()
        const endpoint = "groups"
        const response = await handler.get(endpoint)
        return this.handleGetResponse(response)
    }

    async getGroupsWhereUserIsAMember(id: any) {
        const endpoint = `groups/user/${id}`
        const handler = new RoutersHandler()
        const response = await handler.get(endpoint)
        return this.handleGetResponse(response)
    }

    private handleGetResponse(response: any) {
        if ("groups" in response) return response.groups
        else return []
    }

    async joinGroup(account: any, group: any, translations: any) {
        const handler = new RoutersHandler()
        const endpoint = `groups/${account}/join/${group}`
        const response = await handler.post(endpoint, null)
        return this.notificationHandler(response, translations)

    }

    async leaveGroup(account: any, group: any, translations: any) {
        const handler = new RoutersHandler()
        const endpoint = `groups/${account}/join/${group}`

        const response = await handler.post(endpoint, null)
        return this.notificationHandler(response, translations)
    }

    async kickMemberFromGroup(id: any, admin: any, member: any, tranlations: any) {
        const handler = new RoutersHandler()
        const endpoint = `groups/${id}/kick/${member}/${admin}`

        const response = await handler.delete(endpoint)
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
