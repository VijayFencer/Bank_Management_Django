document.addEventListener("DOMContentLoaded", function() {
    // Get the navbar
    var navbar = document.querySelector(".navbar");
    
    // Check if the navbar exists to avoid errors
    if (navbar) {
        // Get the offset position of the navbar
        var sticky = navbar.offsetTop;

        // Add the sticky class to the navbar when you reach its scroll position. Remove "sticky" when you leave the scroll position
        function stickyNavbar() {
            if (window.pageYOffset >= sticky) {
                navbar.classList.add("sticky");
            } else {
                navbar.classList.remove("sticky");
            }
        }

        // When the user scrolls the page, execute stickyNavbar
        window.onscroll = function() {
            stickyNavbar();
        };
    } else {
        console.error("Navbar element not found!");
    }
    
    
});
