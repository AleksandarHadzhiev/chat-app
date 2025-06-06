import LanguagePicker from "../LanguagePicker"
import Link from "next/link"

//@ts-expect-error
// Providing a function and can not specify the type
export default function FullWidthNavigation({ goBackToHomepage, setLanguage, goToLogin, translations }) {
    return (
        <div className="flex w-full h-full">
            <div
                onClick={() => { goBackToHomepage() }}
                className="flex w-2/10 h-full items-center justify-center space-x-2">
                <p>Some Icon</p>
                <p>TheMedium</p>
            </div>
            <div className="w-6/10 h-full flex items-center justify-center space-x-3 text-black">
                <Link className="w-1/5 pb-2 border-b-2 text-center hover:text-orange-300" href="/">{translations.home}</Link>
                <Link className="w-1/5 pb-2 border-b-2 text-center hover:text-orange-300" href="/groups">{translations.groups}</Link>
                <Link className="w-1/5 pb-2 border-b-2 text-center hover:text-orange-300" href="/me">{translations.account}</Link>
            </div>
            <div className="w-2/10 h-full flex items-center justify-center">
                <LanguagePicker setLanguage={setLanguage} />
                <div
                    onClick={goToLogin}
                    className="flex w-1/2 items-center justify-center hover:text-orange-300 text-black">
                    <svg
                        xmlns="http://www.w3.org/2000/svg"
                        fill="none"
                        viewBox="0 0 24 24"
                        strokeWidth="1.5"
                        stroke="currentColor"
                        className="h-12 w-1/2">
                        <path
                            strokeLinecap="round"
                            strokeLinejoin="round"
                            d="M17.982 18.725A7.488 7.488 0 0 0 12 15.75a7.488 7.488 0 0 0-5.982 2.975m11.963 0a9 9 0 1 0-11.963 0m11.963 0A8.966 8.966 0 0 1 12 21a8.966 8.966 0 0 1-5.982-2.275M15 9.75a3 3 0 1 1-6 0 3 3 0 0 1 6 0Z" />
                    </svg>
                    <p className="w-1/2 border-b-2 text-center">{translations.login}</p>
                </div>
            </div>
        </div>
    )
}