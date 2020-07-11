
'user strict';


// get answer and hint class
let answers = document.querySelectorAll('.answer-btn');
let hints = document.querySelectorAll('.hint-btn');


// show answer, hint
const showText = (elemList, elemClass) => {

  for (let i = 0; i < elemList.length; i++) {
    // click event
    elemList[i].addEventListener('click', () => {
      // get element
      let elem = elemList[i].parentElement.parentElement.parentElement.querySelector(elemClass);
      // add or remove 'display: none'
      if (elem.classList.contains('d-none')) {
        elem.classList.remove('d-none');
      } else {
        elem.classList.add('d-none');
      }
    });
  }
}

showText(answers, '.answer');
showText(hints, '.hint');
