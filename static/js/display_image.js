var im_container = document.getElementById("img-container");
const meme_id = document.currentScript.getAttribute('meme_id');
const meme_list = localStorage.getItem("meme_list");
console.log(typeof(meme_list))
const im_link = JSON.parse(meme_list)[meme_id-1][2];
const img = `<img src="${im_link}"/>`;
im_container.innerHTML = img;