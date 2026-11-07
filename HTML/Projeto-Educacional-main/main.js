
function  comparaTamanhoSapatos(){
    
    if (tamanhoLuisa > tamanhoIsabela)
    {
        return ("Luisa calça mais");
    } 
    else if (tamanhoLuisa < tamanhoIsabela)
    {
        return  ("Isabela calça mais");
    } 
        else if (tamanhoLuisa == tamanhoIsabela)
    {
        return  ("Isabela e Luisa calçam o mesmo tamanho de sapato");
    }
}

function main() {
    const ws = fs.createWriteStream(process.env.OUTPUT_PATH);
    
    const TamanhoHugo = readLine();
    const TamanhoIza = readLine();
     
    const result = comparaTamanhoSapatos(tamanhoLuisa, tamanhoIsabela);
    ws.write(result + '\n');

    ws.end();
}