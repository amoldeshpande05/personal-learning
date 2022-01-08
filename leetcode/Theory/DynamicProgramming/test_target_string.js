const canConstruct=(target,wordBank) =>{
    if(target === ''){
        return true;
    }

    for(let word of wordBank){
        if(target.indexOf(word) === 0){
            const suffix = target.slice(word.length);
            console.log(suffix)
            if(canConstruct(suffix,wordBank) === true){
                return true;
            }
        }
    }

    return false;
}

console.log(canConstruct("skateboard",["bo","rd","ate","t","ska","sk","boar"]))
