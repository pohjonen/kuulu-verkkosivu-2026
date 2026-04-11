(function() {
  const selector = '.hero-section-divider-wave-1';

  // Function to remove the element
  const removeElement = () => {
    const element = document.querySelector(selector);
    if (element) {
      element.parentNode.removeChild(element);
      return true; // Element was found and removed
    }
    return false; // Element was not found
  };

  // --- Strategy 1: MutationObserver ---
  // This is the most efficient method. It waits for the element to be added to the DOM.
  const observer = new MutationObserver((mutations, obs) => {
    if (removeElement()) {
      obs.disconnect(); // Stop observing once the element is removed
    }
  });

  observer.observe(document.body, {
    childList: true,
    subtree: true
  });

  // --- Strategy 2: Interval Fallback ---
  // This is an aggressive fallback for stubborn scripts that might run very late.
  let attempts = 0;
  const maxAttempts = 50; // Try for 5 seconds (50 * 100ms)
  const intervalId = setInterval(() => {
    if (removeElement() || attempts >= maxAttempts) {
      clearInterval(intervalId); // Stop the interval if element is removed or we've tried enough
    }
    attempts++;
  }, 100);

  // --- Strategy 3: Run on load ---
  // Final check when the window is fully loaded
  window.addEventListener('load', removeElement);
})();

// Poista tyhjä väli-elementti moduulista 10
(function() {
  const selector = '#hs_cos_wrapper_dnd_area-module-10 .span1.dnd-column.column-flex';

  // Function to remove the element
  const removeSpacerElement = () => {
    const element = document.querySelector(selector);
    if (element) {
      element.parentNode.removeChild(element);
      return true; // Element was found and removed
    }
    return false; // Element was not found
  };

  // --- Strategy 1: MutationObserver ---
  const observer = new MutationObserver((mutations, obs) => {
    if (removeSpacerElement()) {
      obs.disconnect(); // Stop observing once the element is removed
    }
  });

  observer.observe(document.body, {
    childList: true,
    subtree: true
  });

  // --- Strategy 2: Interval Fallback ---
  let attempts = 0;
  const maxAttempts = 50; // Try for 5 seconds (50 * 100ms)
  const intervalId = setInterval(() => {
    if (removeSpacerElement() || attempts >= maxAttempts) {
      clearInterval(intervalId); // Stop the interval if element is removed or we've tried enough
    }
    attempts++;
  }, 100);

  // --- Strategy 3: Run on load ---
  window.addEventListener('load', removeSpacerElement);
})();

// Poista sininen tausta moduulista 14 - JavaScript-ratkaisu
(function() {
  const removeBlueBackground = () => {
    const module = document.getElementById('dnd_area-module-14');
    if (!module) return false;
    
    // Etsi kaikki dnd_area-row-7 luokat
    const rows = document.querySelectorAll('[class*="dnd_area-row-7"]');
    
    // Poista inline-tyylit ja aseta Kuulu tummanvihreä tausta
    rows.forEach(row => {
      row.style.background = '#002E27';
      row.style.backgroundColor = '#002E27';
      row.style.backgroundImage = 'none';
    });
    
    // Muuta moduulin tausta
    module.style.background = '#002E27';
    module.style.backgroundImage = 'none';
    
    // Etsi kaikki lapset ja korjaa siniset taustat
    const children = module.querySelectorAll('*');
    children.forEach(child => {
      const styles = window.getComputedStyle(child);
      const bgColor = styles.backgroundColor;
      
      // Tarkista onko sininen tausta
      if (bgColor.includes('rgb(0, 123, 255)') || 
          bgColor.includes('rgb(67, 157, 240)') ||
          bgColor.includes('rgb(34, 99, 238)') ||
          bgColor.includes('blue')) {
        child.style.backgroundColor = '#002E27';
        child.style.background = '#002E27';
        child.style.backgroundImage = 'none';
      }
    });
    
    // Muuta taustakuva
    const bgImage = module.querySelector('.img-parallax-horiz');
    if (bgImage) {
      bgImage.style.filter = 'hue-rotate(120deg) brightness(0.7) grayscale(100%)';
      bgImage.style.opacity = '0.3';
    }
    
    return true;
  };

  // --- Strategy 1: MutationObserver ---
  const observer = new MutationObserver((mutations, obs) => {
    if (removeBlueBackground()) {
      obs.disconnect();
    }
  });

  observer.observe(document.body, {
    childList: true,
    subtree: true
  });

  // --- Strategy 2: Interval Fallback ---
  let attempts = 0;
  const maxAttempts = 30;
  const intervalId = setInterval(() => {
    if (removeBlueBackground() || attempts >= maxAttempts) {
      clearInterval(intervalId);
    }
    attempts++;
  }, 200);

  // --- Strategy 3: Run on load ---
  window.addEventListener('load', removeBlueBackground);
})();
