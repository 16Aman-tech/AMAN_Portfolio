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

// ABOUT

gsap.from("#about .about-image",{
    scrollTrigger:"#about",
    x:-100,
    opacity:0,
    duration:1
});

gsap.from("#about .about-content",{
    scrollTrigger:"#about",
    x:100,
    opacity:0,
    duration:1
});


// =====================================
// Skills Progress Animation
// =====================================

gsap.utils.toArray(".progress-fill").forEach((bar)=>{

    gsap.to(bar,{

        width:bar.dataset.width+"%",

        duration:1.5,

        ease:"power3.out",

        scrollTrigger:{

            trigger:bar,

            start:"top 85%"

        }

    });

});


// =====================================
// PROJECT ANIMATION
// =====================================

gsap.from(".project-card",{

    scrollTrigger:{

        trigger:"#projects",

        start:"top 75%"

    },

    y:80,

    opacity:0,

    duration:1,

    stagger:.2,

    ease:"power3.out"

});


// EXPERIENCE

gsap.from(".experience-card",{

    scrollTrigger:"#experience",

    y:80,

    opacity:0,

    stagger:.2,

    duration:1,

    ease:"power3.out"

});



// EDUCATION

gsap.from(".education-card",{

    scrollTrigger:"#education",

    y:80,

    opacity:0,

    stagger:.2,

    duration:1,

    ease:"power3.out"

});


// =====================================
// CERTIFICATES
// =====================================

gsap.from(".certificate-card",{

    scrollTrigger:"#certificates",

    y:80,

    opacity:0,

    stagger:.2,

    duration:1,

    ease:"power3.out"

});



// =====================================
// CODING
// =====================================

gsap.from(".coding-card",{

    scrollTrigger:"#coding",

    y:80,

    opacity:0,

    stagger:.2,

    duration:1,

    ease:"power3.out"

});


// =====================================
// CONTACT
// =====================================

gsap.from(".contact-card",{

    scrollTrigger:"#contact",

    x:-80,

    opacity:0,

    duration:1

});

gsap.from(".contact-form",{

    scrollTrigger:"#contact",

    x:80,

    opacity:0,

    duration:1

});