export function testInputStr(testStr, setErr, errFuncArr, errStrArr) {

    for (let i = 0; i < errFuncArr.length; i++) {
        if (errFuncArr[i](testStr)) {
            setErr(errStrArr[i])
            return false
        }
    }

    setErr()
    return true
}

export function minStrLengthFunc(min){

    return (testStr) => {
        if(testStr.length <= min){
            return true
        }
        return false
    }
}

export function maxStrLengthFunc(max){

    return (testStr) => {
        if(testStr.length >= max){
            return true
        }
        return false
    }
}