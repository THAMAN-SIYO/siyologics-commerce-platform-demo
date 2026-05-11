document.addEventListener('DOMContentLoaded', () => {

  // =========================================================
  // Sticky Header Shadow
  // =========================================================
  const header = document.querySelector('header');

  if (header) {
    const onScroll = () => {
      header.classList.toggle('scrolled', window.scrollY > 30);
    };

    window.addEventListener('scroll', onScroll, { passive: true });
    onScroll();
  }

  // =========================================================
  // Active Navigation Link
  // =========================================================
  document.querySelectorAll('nav a').forEach(link => {

    try {
      const linkPath = new URL(link.href, window.location.origin).pathname;

      if (linkPath === window.location.pathname) {
        link.classList.add('active');
      }

    } catch (e) {
      console.warn('Navigation link parsing error:', e);
    }

  });

  // =========================================================
  // Mobile Navigation
  // =========================================================
  const hamburger = document.querySelector('.hamburger');
  const nav = document.querySelector('nav#main-nav');
  const overlay = document.querySelector('.nav-overlay');

  const closeMenu = () => {
    hamburger?.classList.remove('open');
    nav?.classList.remove('open');
    overlay?.classList.remove('open');
    document.body.style.overflow = '';
  };

  const openMenu = () => {
    hamburger?.classList.add('open');
    nav?.classList.add('open');
    overlay?.classList.add('open');
    document.body.style.overflow = 'hidden';
  };

  hamburger?.addEventListener('click', () => {

    hamburger.classList.contains('open')
      ? closeMenu()
      : openMenu();

  });

  overlay?.addEventListener('click', closeMenu);

  nav?.querySelectorAll('a').forEach(anchor => {
    anchor.addEventListener('click', closeMenu);
  });

  // =========================================================
  // Hero Background Load Animation
  // =========================================================
  const hero = document.querySelector('.hero');

  if (hero) {
    requestAnimationFrame(() => {
      requestAnimationFrame(() => {
        hero.classList.add('loaded');
      });
    });
  }

  // =========================================================
  // Fade-Up Scroll Animation
  // =========================================================
  if ('IntersectionObserver' in window) {

    const elements = document.querySelectorAll('.fade-up');

    if (elements.length > 0) {

      const observer = new IntersectionObserver((entries) => {

        entries.forEach(entry => {

          if (entry.isIntersecting) {
            entry.target.classList.add('visible');
            observer.unobserve(entry.target);
          }

        });

      }, {
        threshold: 0.10,
        rootMargin: '0px 0px -40px 0px'
      });

      elements.forEach(element => observer.observe(element));
    }
  }

  // =========================================================
  // Auto Dismiss Flash Messages
  // =========================================================
  document.querySelectorAll('.flash-msg, .success-banner').forEach(element => {

    setTimeout(() => {

      element.style.transition = 'opacity .5s ease, transform .5s ease';
      element.style.opacity = '0';
      element.style.transform = 'translateY(-8px)';

      setTimeout(() => {
        element.closest('.flash-wrap')?.remove();
        element.remove?.();
      }, 520);

    }, 4500);

  });

  // =========================================================
  // Logo Fallback
  // =========================================================
  const logoImg = document.querySelector('.logo img');
  const logoFallback = document.querySelector('.logo-fallback');

  if (logoImg && logoFallback) {

    logoImg.addEventListener('error', () => {

      logoImg.style.display = 'none';
      logoFallback.style.display = 'block';

    });

  }

  // =========================================================
  // Smooth Anchor Scroll
  // =========================================================
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {

    anchor.addEventListener('click', (e) => {

      const id = anchor.getAttribute('href');

      if (id === '#') return;

      const target = document.querySelector(id);

      if (!target) return;

      e.preventDefault();

      const offset = (header?.offsetHeight ?? 0) + 16;

      window.scrollTo({
        top: target.getBoundingClientRect().top + window.scrollY - offset,
        behavior: 'smooth'
      });

    });

  });

});