const image = document.getElementById('image');
const inputBox = document.getElementById('input-box');
const inputText = document.getElementById('input-text');
const submitButton = document.getElementById('submit-button');
//π実行
/* <script src="https://pyscript.net/pyscript.min.js"></script> */


let isDragging = false;
let startX, startY;

image.addEventListener('mousedown', (event) => {
  isDragging = true;
  startX = event.clientX - image.offsetLeft;
  startY = event.clientY - image.offsetTop;
});

document.addEventListener('mousemove', (event) => {
  if (isDragging) {
    image.style.left = event.clientX - startX + 'px';
    image.style.top = event.clientY - startY + 'px';
  }
});

document.addEventListener('mouseup', () => {
  isDragging = false;
});

image.addEventListener('click', () => {
  inputBox.style.display = 'block';
});

submitButton.addEventListener('click', () => {
  const text = inputText.value;
  // post() 関数の実装
  const socket = new WebSocket("ws://localhost:8000");

socket.onopen = function(event) {
    console.log("Connected to Python server!");

    socket.send(text);
};

socket.onmessage = function(event) {
    console.log("Received from Python:", event.data);
    const balloon = document.getElementById('balloon');
const text = event.data; // textに表示したいテキストを代入

// 5秒後に非表示にする関数
function hideBalloon() {
  balloon.style.display = 'none';
}

// 吹き出しを表示
balloon.textContent = text;
balloon.style.display = 'block';

// 20秒後に非表示
setTimeout(hideBalloon, 20000); 
};

socket.onerror = function(event) {
    console.error("Error:", event.message);
};

socket.onclose = function(event) {
    console.log("Disconnected from Python server.");
}; 

  // 入力内容をクリア
  inputText.value = '';

  // inputBox を非表示
  inputBox.style.display = 'none';
});
