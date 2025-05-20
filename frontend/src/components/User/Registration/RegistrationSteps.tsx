//@ts-expect-error
// Providing a function and can not specify the type
export default function RegistrationSteps({ step, translations, widthType }) {

    let focus = "w-12 h-1 bg-orange-600"
    let notFocused = "w-12 h-1 bg-orange-300"
    let focusArrow = "size-12 text-orange-600"
    let notFocusedArrow = "size-12 text-orange-300"
    if (widthType == "mobile") {
        focus = "w-6 h-1 bg-orange-600"
        notFocused = "w-6 h-1 bg-orange-300"
        focusArrow = "size-6 text-orange-600"
        notFocusedArrow = "size-6 text-orange-300"
    }

    function getStleForStepName(_step: number) {
        if (step != _step && widthType == "mobile")
            return 'hidden'
        else if (step != _step && widthType == "mobile")
            return 'text-orange-600'
        else if (step < _step)
            return 'text-orange-300'
        else
            return 'text-orange-600'

    }

    function getStyleForArrows(partOfArrow: string, _step: number) {
        if (widthType == "mobile")
            return 'hidden'
        else if (step < _step && partOfArrow == "body")
            return notFocused
        else if (step > _step && partOfArrow == "body")
            return focus
        else if (step < _step && partOfArrow == "arrow")
            return notFocusedArrow
        else
            return focusArrow
    }
    // Based on steps and width
    // if width is bigger than mobile -> default (all steps visible at the same time)
    // else two steps visible at a time.

    return (
        <div className="flex w-full items-center justify-center space-x-2">
            <div className={getStleForStepName(1)}>
                <h3>{translations.stepOne}</h3>
            </div>
            <div className="flex items-center justify-center">
                <div className={getStyleForArrows("body", 2)}></div>
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth="1.5" stroke="currentColor" className={getStyleForArrows("arrow", 2)}>
                    <path strokeLinecap="round" strokeLinejoin="round" d="m8.25 4.5 7.5 7.5-7.5 7.5" />
                </svg>
            </div>
            <div className={getStleForStepName(2)}>
                <h3>{translations.stepTwo}</h3>
            </div>
            <div className="flex items-center justify-center">
                <div className={getStyleForArrows("body", 3)}></div>
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth="1.5" stroke="currentColor" className={getStyleForArrows("arrow", 3)}>
                    <path strokeLinecap="round" strokeLinejoin="round" d="m8.25 4.5 7.5 7.5-7.5 7.5" />
                </svg>
            </div>
            <div className={getStleForStepName(3)}>
                <h3>{translations.stepThree}</h3>
            </div>
        </div>
    )
}