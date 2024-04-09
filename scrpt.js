let loadMoreBtn1 = document.querySelector('#load-more-1');
let currentItem1 = 4;

loadMoreBtn1.onclick = () => {
    let boxes = [...document.querySelectorAll(
        '.box-container-1 .box-1'
    )];
    for(var i = currentItem1; i < currentItem1 + 4; i++){
        boxes[i].style.display = 'inline-block';
    }
    currentItem1 += 4;
    if(currentItem1 >= boxes.length){
        loadMoreBtn1.style.display = 'none'
    }
}