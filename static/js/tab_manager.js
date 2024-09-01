const tabs = document.querySelectorAll('[data-tab-target]');

tabs.forEach(tab => {
  tab.addEventListener('click', () => {
    const target = document.querySelector(`#${tab.dataset.tabTarget}`); // Corrected to match the data attribute value with ID selector
    if (target) { // Ensure target is not null
      document.querySelectorAll('[data-tab-content]').forEach(content => {
        content.classList.remove('active');
      });
      target.classList.add('active');
    }
  });
});


function goBack() {
  window.history.back();
};