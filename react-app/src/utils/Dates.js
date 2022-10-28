


export function getMonthDay(dateString){

    const postMonth = dateString.slice(8, 11);
    const postDay = dateString.slice(5, 7);

    return `${postMonth} ${postDay}`
}