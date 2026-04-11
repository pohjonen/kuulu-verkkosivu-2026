// No header scroll behavior - keeping transparent style at all times
document.addEventListener('DOMContentLoaded', function() {
    // Header stays transparent regardless of scroll position
    console.log('Header initialized with permanent transparent style');

    // Mega-menu functionality - hover and click/touch support
    const navItems = document.querySelectorAll('.custom-header__navigation > ul > li');
    navItems.forEach(item => {
        const megaMenu = item.querySelector('.mega-menu');
        const navLink = item.querySelector('a');
        
        if (megaMenu) {
            let isOpen = false;
            
            // Function to show menu
            function showMenu() {
                if (!isOpen) {
                    item.classList.add('has-open-menu');
                    megaMenu.style.display = 'block';
                    setTimeout(() => {
                        megaMenu.style.opacity = '1';
                        megaMenu.style.visibility = 'visible';
                    }, 10);
                    isOpen = true;
                }
            }
            
            // Function to hide menu
            function hideMenu() {
                if (isOpen) {
                    item.classList.remove('has-open-menu');
                    megaMenu.style.opacity = '0';
                    megaMenu.style.visibility = 'hidden';
                    setTimeout(() => {
                        megaMenu.style.display = 'none';
                    }, 300);
                    isOpen = false;
                }
            }
            
            // Hover support (desktop)
            item.addEventListener('mouseenter', showMenu);
            item.addEventListener('mouseleave', hideMenu);
            
            // Click/touch support
            // Desktop: click navigates to page (menu opens on hover)
            // Touch: first tap opens menu, second tap navigates
            navLink.addEventListener('click', function(e) {
                var isTouchDevice = window.matchMedia('(hover: none) and (pointer: coarse)').matches;
                if (isTouchDevice && megaMenu.querySelector('.mega-menu-list').children.length > 0) {
                    if (!isOpen) {
                        e.preventDefault();
                        showMenu();
                        // Close other menus
                        navItems.forEach(otherItem => {
                            if (otherItem !== item) {
                                var otherMenu = otherItem.querySelector('.mega-menu');
                                if (otherMenu) {
                                    otherItem.classList.remove('has-open-menu');
                                    otherMenu.style.opacity = '0';
                                    otherMenu.style.visibility = 'hidden';
                                    setTimeout(() => {
                                        otherMenu.style.display = 'none';
                                    }, 300);
                                }
                            }
                        });
                    }
                    // If already open on touch, let the click navigate normally
                }
                // On desktop (hover available), always let click navigate
            });
            
            // Close menu when clicking outside
            document.addEventListener('click', function(e) {
                if (!item.contains(e.target) && isOpen) {
                    hideMenu();
                }
            });
        }
    });

    // Mobile menu toggle
    var toggle = document.getElementById('mobile-menu-toggle');
    var panel = document.getElementById('mobile-nav-panel');
    if (toggle && panel) {
        function openMenu(){
            toggle.classList.add('is-open');
            panel.classList.add('is-active');
            toggle.setAttribute('aria-expanded', 'true');
            document.body.classList.add('nav-open');
        }
        function closeMenu(){
            toggle.classList.remove('is-open');
            panel.classList.remove('is-active');
            toggle.setAttribute('aria-expanded', 'false');
            document.body.classList.remove('nav-open');
        }
        function toggleMenu(){
            panel.classList.contains('is-active') ? closeMenu() : openMenu();
        }
        toggle.addEventListener('click', toggleMenu);
        toggle.addEventListener('keydown', function(e){ if(e.key==='Enter' || e.key===' '){ e.preventDefault(); toggleMenu(); }});
        document.addEventListener('keydown', function(e){ if(e.key==='Escape'){ closeMenu(); }});
        panel.querySelectorAll('a').forEach(function(a){ a.addEventListener('click', closeMenu); });

        // Sulje ulkopuolelta klikkaamalla
        document.addEventListener('click', function(e){
          if (panel.classList.contains('is-active')){
            if (!panel.contains(e.target) && !toggle.contains(e.target)){
              closeMenu();
            }
          }
        });
    }
});
