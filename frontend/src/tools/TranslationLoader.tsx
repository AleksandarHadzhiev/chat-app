
export default class TranslationLoader {
    async translationLoader(language: string, _path: string) {
        const path = `../dictionaries/${language}/${_path}`
        return await import(path)
    }
}