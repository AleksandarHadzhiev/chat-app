import RoutersHandler from "./RouterHandler";
import { RegisterDTO } from "./DTOs/User/RegisterDTO";
import { VerifyDTO } from "./DTOs/User/VerifyDTO";
import { LoginDTO } from "./DTOs/User/LoginDTO";

export default class UsersHandler {
    register(url: string, data: RegisterDTO) {
        const handler = new RoutersHandler()
        return handler.post(url, data)
    }

    verify(url: string, data: VerifyDTO) {
        const handler = new RoutersHandler()
        return handler.post(url, data)
    }

    login(url: string, data: LoginDTO) {
        const handler = new RoutersHandler()
        return handler.post(url, data)
    }
}