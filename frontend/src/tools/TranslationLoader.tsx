
export default async function translationLoader(language: any, _path: any) {
    let path = `../dictionaries/${language}/${_path}`
    return await import(path)
}