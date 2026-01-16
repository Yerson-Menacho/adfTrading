// script.js - toggle menu en móvil
document.addEventListener('DOMContentLoaded', function () {
  const toggle = document.querySelector('.menu-toggle');
  const nav = document.querySelector('.nav-links');
  const links = document.querySelectorAll('.nav-links a');

  if (!toggle || !nav) return;

  // Abrir / cerrar menú
  toggle.addEventListener('click', () => {
    nav.classList.toggle('active');
  });

  // Cerrar menú al hacer click en un enlace
  links.forEach(link => {
    link.addEventListener('click', () => {
      nav.classList.remove('active');
    });
  });
});




