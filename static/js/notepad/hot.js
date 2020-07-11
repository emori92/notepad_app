
'user strict';


// btn
let wordbook = document.getElementById('wordbook-btn');
let recommender = document.getElementById('recommender-btn');

// add or remove class
const changeDisplay = (id1, id2) => {
  // get element
  let element1 = document.getElementById(id1);
  let element2 = document.getElementById(id2);
  // change display
  element1.classList.remove('d-none');
  element1.classList.add('d-flex');
  element2.classList.remove('d-flex');
  element2.classList.add('d-none');
}

// push btn
wordbook.addEventListener('click', () => { changeDisplay('wordbook', 'recommender') });
recommender.addEventListener('click', () => { changeDisplay('recommender', 'wordbook') });