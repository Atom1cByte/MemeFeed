var add = document.getElementById("add");
var count = 0;

add.onclick = () => {
    if (count === 8) {
        var main = document.querySelector("div.center");
        main.innerHTML += "<font size='5ch' color='red'>Select limit reached!</font>";
        return;
    }
    const select = `
    <select class="start-select">
        <option value="r/memes">r/memes</option>
        <option value="r/funny">r/funny</option>
        <option value="r/animememes">r/animememes</option>
        <option value="r/AdviceAnimals">r/AdviceAnimals</option>
        <option value="r/MemeEconomy">r/MemeEconomy</option>
        <option value="r/dankmemes">r/dankmemes</option>
        <option value="r/MinecraftMemes">r/MinecraftMemes</option>
        <option value="r/programmingmemes">r/programmingmemes</option>
        <option value="r/softwaregore">r/softwaregore</option>
    </select>
    `;
    var selects = document.getElementById("selects");
    selects.innerHTML += select;
    count++;
    console.log(selects)
}