(function() {
  'use strict';
  
  function init() {
    const hamburger = document.querySelector('#mobile-menu-toggle');
    const panel = document.querySelector('#mobile-nav-panel');
    const body = document.body;
    
    if (!hamburger || !panel) {
      setTimeout(init, 100);
      return;
    }
    
    // Hamburger pysyy paneelin päällä
    hamburger.style.zIndex = '1000';
    
    function openMenu() {
      panel.classList.add('is-active');
      hamburger.classList.add('is-open');
      body.classList.add('nav-open');
      hamburger.setAttribute('aria-expanded', 'true');
      hamburger.setAttribute('aria-label', 'Sulje valikko');
    }
    
    function closeMenu() {
      panel.classList.remove('is-active');
      hamburger.classList.remove('is-open');
      body.classList.remove('nav-open');
      hamburger.setAttribute('aria-expanded', 'false');
      hamburger.setAttribute('aria-label', 'Avaa valikko');
    }
    
    hamburger.addEventListener('click', function(e) {
      e.preventDefault();
      e.stopPropagation();
      if (panel.classList.contains('is-active')) {
        closeMenu();
      } else {
        openMenu();
      }
    });

    // Sulje ESC-näppäimellä
    document.addEventListener('keydown', function(e) {
      if (e.key === 'Escape' && panel.classList.contains('is-active')) {
        closeMenu();
      }
    });

    // Sulje jos klikataan linkkiä paneelissa
    panel.querySelectorAll('a').forEach(function(link) {
      link.addEventListener('click', function() {
        closeMenu();
      });
    });
  }
  
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    setTimeout(init, 50);
  }
})();
