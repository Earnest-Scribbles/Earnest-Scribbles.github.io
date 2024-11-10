// Select the logo and the audio element
const logo = document.getElementById('logo');
const hoverSound = document.getElementById('hover-sound');

// Play audio when the mouse enters the logo
logo.addEventListener('mouseenter', () => {
  hoverSound.currentTime = 0;  // Ensure the sound starts from the beginning each time
  hoverSound.play();
});