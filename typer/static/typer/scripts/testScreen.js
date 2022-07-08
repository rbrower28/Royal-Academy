
// gets the output boxes
let title_text = document.querySelector(".title");
let content_text = document.querySelector(".words-box");
let timer_text = document.querySelector(".output-time");
let accuracy_text = document.querySelector(".output-acc");
let error_text = document.querySelector(".output-errors");
let words_text = document.querySelector(".output-wpm");

// gets the input box
let input_box = document.querySelector("textarea");

// gets the wpm section for display toggle
let wpm_group = document.querySelector(".wpm");

// set some starting variables
let total_time = 60;
let time_passed = 0;
let total_errors = 0;
let errors = 0;
let accuracy = 0;
let typed = 0;
let correctCharacters = 0;
let current_content = "";
let timer = null;

let quotes_array = [
  "It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way.",

  "I see in your eyes the same fear that would take the heart of me. A day may come when the courage of men fails, when we forsake our friends and break all bonds of fellowship, but it is not this day. An hour of wolves and shattered shields, when the age of men comes crashing down, but it is not this day! This day we fight! By all that you hold dear on this good Earth, I bid you stand, Men of the West!",

  "The world ain't all sunshine and rainbows. It's a very mean and nasty place and I don't care how tough you are it will beat you to your knees and keep you there permanently if you let it. You, me, or nobody is gonna hit as hard as life. But it ain't about how hard you hit. It's about how hard you can get hit and keep moving forward. How much you can take and keep moving forward. That's how winning is done! Cause if you're willing to go through all the battling you got to go through to get where you want to get, who's got the right to stop you?",

  "We don't read and write poetry because it's cute. We read and write poetry because we are members of the human race, and the human race is filled with passion. Medicine, law, business, engineering, these are noble pursuits and necessary to sustain life. But poetry, beauty, romance, love, these are what we stay alive for. Boys, you must strive to find your own volce. Because the longer you wait to begin, the less likely you are to find it at all."
];


function UpdateWordsBox() {
  content_text.textContent = "";

  let quote_index = Math.floor(Math.random() * quotes_array.length);

  current_content = quotes_array[quote_index];
  
  current_content.split('').forEach(letter => {
    const span = document.createElement('span');
    span.innerText = letter;
    content_text.appendChild(span);
  })
};


function onTextInput() {
  input = input_box.value;

  if (input == current_content) {
    finishGame();
    return
  }

  input_array = input.split('');
  typed++;

  let curr_errors = 0;

  let allSpans = content_text.querySelectorAll('span');
  allSpans.forEach((char, index) => {
    let ctyped = input_array[index]
    if (ctyped == null) {
      char.classList.remove('green');
    } 
    else if (ctyped === char.innerText) {
      char.classList.add('green');
    } 
    else {
      curr_errors++;
    }
  });

  if (curr_errors > errors) {
    total_errors += curr_errors - errors;
  };
  
  errors = curr_errors

  error_text.textContent = total_errors;
  correctCharacters = (typed - (total_errors));
  let accuracy = ((correctCharacters / typed) * 100);
  accuracy_text.textContent = Math.round(accuracy);
};


function updateTimer() {
  if (time_passed < total_time) {
    time_passed++;
    timer_text.textContent = total_time - time_passed;
  }
  else {
    finishGame();
  }
};


function startGame() {
  content_text.style.display="block";
  UpdateWordsBox();

  clearInterval(timer);
  timer = setInterval(updateTimer, 1000);
};


function finishGame() {
  clearInterval(timer)
  input_box.disabled = true;
  content_text.style.display="none";

  // console.log("total inputs counted - " + typed)
  // console.log("total characters - " + correctCharacters)
  // console.log("seconds passed - " + time_passed + " (" + (time_passed / 60) + " minutes)")
  // console.log("you typed " + (correctCharacters / 5) + " words on average")
  
  wpm = Math.round((correctCharacters / 5) / (time_passed / 60));

  // console.log("your wpm - " + wpm)

  words_text.textContent = wpm;
  wpm_group.style.display = "block";
  title_text.textContent = "Finish!"
};

startGame();