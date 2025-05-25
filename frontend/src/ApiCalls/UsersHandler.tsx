import RoutersHandler from "./RouterHandler";
import { RegisterDTO } from "./DTOs/User/RegisterDTO";
import { VerifyDTO } from "./DTOs/User/VerifyDTO";
import { LoginDTO } from "./DTOs/User/LoginDTO";
import { ForgotPasswordDTO } from "./DTOs/User/ForgotPasswordDTO";
import { ResetPasswordDTO } from "./DTOs/User/ResetPassword";

export default class UsersHandler {

    async register(url: string, data: RegisterDTO, translations: any) {
        const handler = new RoutersHandler()
        const response = await handler.post(url, data)
        return this.notificationHandler(response, translations)
    }

    async checkIfAuthorized(url: string, data: VerifyDTO, translations: any) {
        const handler = new RoutersHandler()
        const response = await handler.post(url, data)
        return this.notificationHandler(response, translations)
    }

    async resetPassword(url: string, data: ResetPasswordDTO, translations: any) {
        const handler = new RoutersHandler()
        const response = await handler.post(url, data)
        return this.notificationHandler(response, translations)
    }

    async verify(url: string, data: VerifyDTO, translations: any) {
        const handler = new RoutersHandler()
        const response = await handler.post(url, data)
        return this.notificationHandler(response, translations)
    }

    async login(url: string, data: LoginDTO, translations: any) {
        const handler = new RoutersHandler()
        const response = await handler.post(url, data)
        return this.notificationHandler(response, translations)
    }

    async forgotPassowrd(url: string, data: ForgotPasswordDTO, translations: any) {
        const handler = new RoutersHandler()
        const response = await handler.post(url, data)
        console.log(response)
        return this.notificationHandler(response, translations)
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