// Clears the screen on click of C button.
const clearScreen = async () => {
    document.getElementById("result").value = "";
}

// Displays entered value on screen.
const setScreenValue = async (value) => {
  document.getElementById("result").value += value;
}
