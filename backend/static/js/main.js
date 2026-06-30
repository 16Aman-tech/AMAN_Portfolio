// =====================================
// GSAP Animation
// =====================================

console.log("MAIN JS LOADED");

gsap.registerPlugin(ScrollTrigger);

/* Hero Left */

gsap.from(".hero-left",{

    opacity:0,
    x:-120,
    duration:1.2,
    ease:"power3.out"

});

/* Hero Right */

gsap.from(".hero-right",{

    opacity:0,
    x:120,
    duration:1.2,
    delay:.3,
    ease:"power3.out"

});

/* All Sections */

gsap.utils.toArray("section").forEach((section)=>{

    gsap.from(section,{

        opacity:0,
        y:80,
        duration:1,
        ease:"power3.out",

        scrollTrigger:{
            trigger:section,
            start:"top 80%",
            toggleActions:"play none none none"
        }

    });

});


/* =====================================
   ACTIVE NAVBAR
===================================== */

const sections = document.querySelectorAll("section");
const navLinks = document.querySelectorAll(".nav-link");

window.addEventListener("scroll", () => {

    let current = "";

    sections.forEach(section => {

        const sectionTop = section.offsetTop - 150;

        if (window.scrollY >= sectionTop) {
            current = section.getAttribute("id");
        }

    });

    navLinks.forEach(link => {

        link.classList.remove("active");

        if (link.getAttribute("href") === "#" + current) {
            link.classList.add("active");
        }

    });

});

// ==============================
// Typing Animation
// ==============================

window.onload = function () {

    var typed = new Typed("#typing", {

        strings: [
            "Python Developer",
            "Backend Developer",
            "Django Developer",
            "AI Enthusiast"
        ],

        typeSpeed: 70,
        backSpeed: 40,
        backDelay: 1500,
        smartBackspace: true,
        loop: true,
        showCursor: true,
        cursorChar: "|"

    });

};

// Floating Glow

gsap.to(".image-box",{

    y:-15,

    duration:2.2,

    repeat:-1,

    yoyo:true,

    ease:"power1.inOut"

});

// About Image Floating

// About Image Floating

gsap.to(".about-image img",{

    y:-15,

    duration:2.5,

    repeat:-1,

    yoyo:true,

    ease:"power1.inOut"

});