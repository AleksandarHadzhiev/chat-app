import axios from "axios";
export default class TranslationLoader {
    private language: string;
    private file: string;
    constructor(_language: string, _file: string) {
        this.language = _language;
        this.file = _file;
    }

    async getTranslatiosn() {
        const BACKEND_BASE_URL = process.env.NEXT_PUBLIC_BACKEND_URL
        return await axios.get(`${BACKEND_BASE_URL}/languages/translations/` + this.language + "/" + this.file)
    }

}
