const allConstruct = (target,wordBank) => {
    if (target == "") return [[]];
    const result=[]
    for(let word of wordBank){
        if(target.indexOf(word) === 0){
            const suffix = target.slice(word.length);
            const suffixWays = allConstruct(suffix, wordBank);
            const targetWays = suffixWays.map(way => [word, ...way]);
            console.log("targetWays  : ",targetWays)

            // console.log("targetways  : ",targetWays)

            // // targetWays=[word]
            // console.log(targetWays)
            result.push(...targetWays)
        }
    }
    // console.log("result after end loop: ",result)
    // console.log("result  : ",result)
    return result;
}
// console.log(allConstruct('purple',['purp','le','pur','ple']))

console.log(allConstruct('abcdef',['ab','abc','cd','def','abcd','ef','c']))