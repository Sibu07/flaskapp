const toggleThemeButton = document.getElementById('toggle-theme');
const iconElement = toggleThemeButton.querySelector('i'); // Select the icon element

toggleThemeButton.addEventListener('click', () => {
  const bodyElement = document.querySelector('body');
  const iconName = iconElement.classList.contains('fa-moon') ? 'fa-moon' : 'fa-sun';

  bodyElement.classList.toggle('dark-mode');
  
  if (iconName === 'fa-moon') {
    iconElement.classList.replace('fa-moon', 'fa-sun');
    // Additional code for dark mode
  } else if (iconName === 'fa-sun') {
    iconElement.classList.replace('fa-sun', 'fa-moon');
    // Additional code for light mode
  }
});
