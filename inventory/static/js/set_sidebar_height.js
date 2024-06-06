function setElementWidth() {
  const dashBoardBody = document.getElementById('dashboard_body'); // Assuming 'dashboard_body' is the ID for the sidebar
  const navbarElement = document.getElementById('navbar'); // Assuming 'navbar' is the ID for the navbar

  console.log(dashBoardBody)
  console.log(navbarElement)


  if (dashBoardBody && navbarElement) {
    const viewportHeight = window.innerHeight; 
    const elementHeight = navbarElement.offsetHeight;
    const newHeight = viewportHeight - elementHeight; 

    dashBoardBody.style.height = `${newHeight}px`; 
  } else {
    console.error('Elements with IDs "dashboard_body" and "navbar" not found.');
  }
}

window.addEventListener('load', setElementWidth); 
window.addEventListener('resize', setElementWidth);
