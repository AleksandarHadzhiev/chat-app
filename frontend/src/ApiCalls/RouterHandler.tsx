import axios, { AxiosError } from "axios";
export default class RoutersHandler {

    async get(url: string) {
        return await axios.get(url)
    }

    async post(url: string, data: { email: string; username?: string; password?: string; code?: string; }) {

        try {
            const response = await axios.post(url, data)
            if (response.status == 201) {
                return response.data
            }
            else if (response.status == 200) {
                return response.data
            }
        } catch (_error: any) {
            let error = _error.data
            if (_error instanceof AxiosError) {
                const reason = _error.response?.data
                if ("fail" in reason)
                    return reason
            }
            return error
        }

    }
}