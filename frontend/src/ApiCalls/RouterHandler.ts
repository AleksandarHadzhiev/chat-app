import axios, { AxiosError } from "axios";
import { GeneralGroupDTO } from "./DTOs/Other/GeneralGroupDTO";
import { LoginDTO } from "./DTOs/User/LoginDTO";
import { RegisterDTO } from "./DTOs/User/RegisterDTO";
import { VerifyDTO } from "./DTOs/User/VerifyDTO";
import { EditMessageDTO } from "./DTOs/Other/EditMessageDTO";
import { ForgotPasswordDTO } from "./DTOs/User/ForgotPasswordDTO";
import { ResetPasswordDTO } from "./DTOs/User/ResetPassword";
export default class RoutersHandler {
    url = process.env.NEXT_PUBLIC_BACKEND_URL
    async get(endpoint: string, headers: any = null) {
        try {
            const response = await axios.get(`${this.url}/${endpoint}`, { headers: headers })
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

    async post(headers: any = null, endpoint: string, data: LoginDTO | ResetPasswordDTO | ForgotPasswordDTO | GeneralGroupDTO | RegisterDTO | VerifyDTO | null) {
        try {
            const response = await axios.post(`${this.url}/${endpoint}`, data, { headers: headers })
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

    async put(endpoint: string, data: GeneralGroupDTO | EditMessageDTO | null, headers: any = null) {
        try {
            const response = await axios.put(`${this.url}/${endpoint}`, data, { headers: headers })
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

    async delete(endpoint: string, headers: any = null) {
        try {
            const response = await axios.delete(`${this.url}/${endpoint}`, { headers: headers })
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