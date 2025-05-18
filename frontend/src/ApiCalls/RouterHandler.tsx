import axios, { AxiosError } from "axios";
import { GeneralGroupDTO } from "./DTOs/Group/GeneralGroupDTO";
import { LoginDTO } from "./DTOs/User/LoginDTO";
import { RegisterDTO } from "./DTOs/User/RegisterDTO";
import { VerifyDTO } from "./DTOs/User/VerifyDTO";
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

    async put(url: string, data: any) {
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
            return await axios.delete(url)
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