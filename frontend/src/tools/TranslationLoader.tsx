import axios from "axios";
export default class TranslationLoader {
    private language: string;
    private file: string;
    constructor(_language: string, _file: string) {
        this.language = _language;
        this.file = _file;
    }

    async getTranslatiosn() {
        return await axios.get("http://localhost:8000/languages/translations/" + this.language + "/" + this.file)
    }

}
