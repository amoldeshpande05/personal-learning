const canConstruct=(target,wordBank,memo={}) =>{
    console.log(memo)
    if(target in memo) return memo[target]
    if(target === ''){
        return true;
    }
    for(let word of wordBank){
        if(target.indexOf(word) === 0){
            const suffix = target.slice(word.length);
            if(canConstruct(suffix,wordBank,memo) === true){
                memo[suffix] = true
                return true;
            }
        }
    }
    memo[target] = false
    return false;
}

console.log(canConstruct("enterapotentpots",["a","p","ent","enter","ot","o","t"]))
