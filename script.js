document.addEventListener('DOMContentLoaded', () => {
  const obs = new IntersectionObserver((entries) => {
    entries.forEach(e => { if (e.isIntersecting) { e.target.classList.add('vis'); obs.unobserve(e.target); } });
  }, { threshold: 0.08, rootMargin: '0px 0px -30px 0px' });
  document.querySelectorAll('.glass-card,.section-head,.hero-copy,.hero-card,.stat-card,.strategy-block,.pricing-card,.cta-card').forEach(el => {
    el.classList.add('anim');
    obs.observe(el);
  });
});
const s = document.createElement('style');
s.textContent = `.anim{opacity:0;transform:translateY(20px);transition:opacity .65s cubic-bezier(.16,1,.3,1),transform .65s cubic-bezier(.16,1,.3,1)}.anim.vis{opacity:1;transform:translateY(0)}`;
document.head.appendChild(s);
