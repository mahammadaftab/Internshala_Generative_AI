const number1Input = document.getElementById('number1');
const number2Input = document.getElementById('number2');
const calculateBtn = document.getElementById('calculateBtn');
const resultOutput = document.getElementById('resultOutput');
const fetchOutput = document.getElementById('fetchOutput');
const previewImage = document.getElementById('previewImage');

function displayResult(sum) {
  resultOutput.textContent = `Sum: ${sum}`;
}

function displayFetchData(data) {
  fetchOutput.textContent = JSON.stringify(data, null, 2);
}

function resetOutput(target) {
  target.textContent = '';
}

function showImage(url) {
  if (!url) {
    previewImage.style.display = 'none';
    previewImage.src = '';
    return;
  }

  previewImage.src = url;
  previewImage.style.display = 'block';
}

function fetchApiData(id) {
  const apiUrl = `https://jsonplaceholder.typicode.com/todos/${id}`;

  fetch(apiUrl)
    .then((response) => {
      if (!response.ok) {
        throw new Error('Data could not be loaded.');
      }
      return response.json();
    })
    .then((data) => {
      displayFetchData(data);
    })
    .catch((error) => {
      fetchOutput.textContent = `Error: ${error.message}`;
    });
}

calculateBtn.addEventListener('click', () => {
  const firstValue = number1Input.value.trim();
  const secondValue = number2Input.value.trim();

  if (firstValue === '' || secondValue === '') {
    alert('Please enter both numbers.');
    return;
  }

  const firstNumber = Number(firstValue);
  const secondNumber = Number(secondValue);
  const sum = firstNumber + secondNumber;

  displayResult(sum);
});

number1Input.addEventListener('input', () => {
  const imageUrl = number1Input.value.trim();
  if (imageUrl === '') {
    showImage('');
    return;
  }

  const safeUrl = imageUrl.match(/^https?:\/\//) ? imageUrl : `https://${imageUrl}`;
  showImage(safeUrl);
});

number2Input.addEventListener('input', () => {
  const fetchId = number2Input.value.trim();

  if (fetchId === '') {
    resetOutput(fetchOutput);
    return;
  }

  const numericId = Number(fetchId);
  if (Number.isNaN(numericId) || numericId <= 0) {
    fetchOutput.textContent = 'Enter a positive numeric ID to fetch data.';
    return;
  }

  fetchApiData(Math.floor(numericId));
});
