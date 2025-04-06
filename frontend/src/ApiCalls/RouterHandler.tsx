import axios from "axios";

export default class RoutersHandler {

    get(url: string) {
        axios.get(url).then(async (response) => {
            console.log(await response.data)
            return await response.data
        }).catch((error) => {
            console.log(error)
        })
    }

    post(url: string, data: any) {
        axios.post(url, data).then(async (response) => {
            console.log(await response.data)
            const data = response.data
            if (data != "null") {
                alert("Success")
            }
            return await response.data
        }).catch((error) => {
            console.log(error)
            return error
        })
    }
}