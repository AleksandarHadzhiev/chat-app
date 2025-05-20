import axios, { AxiosError } from "axios";
import { GeneralGroupDTO } from "./DTOs/Other/GeneralGroupDTO";
import { LoginDTO } from "./DTOs/User/LoginDTO";
import { RegisterDTO } from "./DTOs/User/RegisterDTO";
import { VerifyDTO } from "./DTOs/User/VerifyDTO";
import { MessageDTO } from "./DTOs/Other/MessageDTO";
import { EditMessageDTO } from "./DTOs/Other/EditMessageDTO";
export default class RoutersHandler {

    async get(url: string) {
        try {
            const response = await axios.get(url)
            if (response.status == 200) return response.data
            else if (response.data == 204) return response.data
            else return { "fail": "Unknown reason" }
        } catch (_error: any) {
            const error = _error.data
            if (_error instanceof AxiosError) {
                const reason = _error.response?.data
                if ("fail" in reason)
                    return reason
            }
            return error
        }
    }

    async post(url: string, data: LoginDTO | GeneralGroupDTO | RegisterDTO | VerifyDTO | null) {
        try {
            const response = await axios.post(url, data)
            if (response.status == 201) {
                return response.data
            }
            else if (response.status == 200) {
                return response.data
            }
        } catch (_error: any) {
            const error = _error.data
            if (_error instanceof AxiosError) {
                const reason = _error.response?.data
                if ("fail" in reason)
                    return reason
            }
            return error
        }

    }

    async put(url: string, data: GeneralGroupDTO | EditMessageDTO | null) {
        try {
            const response = await axios.put(url, data)
            if (response.status == 201) {
                return response.data
            }
            else if (response.status == 200) {
                return response.data
            }
        } catch (_error: any) {
            const error = _error.data
            if (_error instanceof AxiosError) {
                const reason = _error.response?.data
                if ("fail" in reason)
                    return reason
            }
            return error
        }
    }

    async delete(url: string) {
        try {
            const response = await axios.delete(url)
            if (response.status == 200) return response.data
            else {
                return {
                    "fail": "Status not 200"
                }
            }
        } catch (_error: any) {
            const error = _error.data
            if (_error instanceof AxiosError) {
                const reason = _error.response?.data
                if ("fail" in reason)
                    return reason
            }
            return error
        }
    }
}