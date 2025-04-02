export default function ProvdeCode() {
    return (
        <div className="w-full h-1/2 flex flex-col items-center justify-center">
            <div className="flex flex-col space-y-3">
                <label>Code</label>
                <div className="flex w-full space-x-3">
                    <input className="w-12 h-12 bg-white border-2 border-black text-center text-orange-600" type="text" name="firstDigit" placeholder="0" />
                    <input className="w-12 h-12 bg-white border-2 border-black text-center text-orange-600" type="text" name="secondDigit" placeholder="1" />
                    <input className="w-12 h-12 bg-white border-2 border-black text-center text-orange-600" type="text" name="thirdDigit" placeholder="2" />
                    <input className="w-12 h-12 bg-white border-2 border-black text-center text-orange-600" type="text" name="fourthDigit" placeholder="3" />
                </div>
            </div>
        </div>

    )
}