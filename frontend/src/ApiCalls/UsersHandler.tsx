import RoutersHandler from "./RouterHandler";
import { RegisterDTO } from "./DTOs/User/RegisterDTO";
import { VerifyDTO } from "./DTOs/User/VerifyDTO";
import { LoginDTO } from "./DTOs/User/LoginDTO";

export default class UsersHandler {

    async register(url: string, data: RegisterDTO, transitions: any) {
        const handler = new RoutersHandler()
        const response = await handler.post(url, data)
        return this.notificationHandler(response, transitions)
    }

    async verify(url: string, data: VerifyDTO, transitions: any) {
        const handler = new RoutersHandler()
        const response = await handler.post(url, data)
        return this.notificationHandler(response, transitions)
    }

    async login(url: string, data: LoginDTO, transitions: any) {
        const handler = new RoutersHandler()
        const response = await handler.post(url, data)
        return this.notificationHandler(response, transitions)
    }

    private notificationHandler(response: any, transitions: any) {
        if ("message" in response) {
            const message = transitions[response.message]
            return {
                tag: "success",
                message: message
            }
        } else if ("fail" in response) {
            let errorMessage = transitions.fail
            const errrors = response.fail
            errrors.forEach((error: string) => {
                errorMessage += `${transitions[error]}, `
            });
            return {
                tag: "fail",
                message: errorMessage
            }
        } else if ("error" in response) {
            const message = transitions[response.error]
            return {
                tag: "fail",
                message: message
            }
        }
        return response
    }
}