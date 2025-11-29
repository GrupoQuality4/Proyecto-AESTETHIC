let swiper = new Swiper(".mySwiper", {
  slidesPerView: 3,
  spaceBetween: 30,
  grabCursor: true,
  loop: true,
  autoplay: {
    delay: 1800,
    disableOnInteraction: false,
  },
  breakpoints: {
    991: {
      slidesPerView: 3,
    },
    768: {
      slidesPerView: 2,
    },
    0: {
      slidesPerView: 1,
    },
  },
});

const suggestionsData = [
  { nombre: 'Tratamientos Faciales', ruta: '/tratamientos_facial' },
  { nombre: 'Tratamientos Corporales', ruta: '/tratamientos_corporales' },
  { nombre: 'Depilación', ruta: '/tratamientos_depilacion' },
  { nombre: 'Masajes', ruta: '/tratamientos_masajes' },
  { nombre: 'Spa de Manos', ruta: '/tratamientos_spa_de_manos' },
  { nombre: 'Gift Card', ruta: '/gif_card' }

];

function showSuggestions(query) {
  const suggestionsContainer = document.getElementById('suggestions');
  suggestionsContainer.innerHTML = '';

  if (query.length === 0) {
    suggestionsContainer.style.display = 'none';
    return;
  }
  const filteredSuggestions = suggestionsData.filter(item => item.nombre.toLowerCase().includes(query.toLowerCase()));
  filteredSuggestions.forEach(suggestion => {
    const suggestionItem = document.createElement('div');
    suggestionItem.textContent = suggestion.nombre;
    suggestionItem.classList.add('suggestion-item');
    suggestionItem.onclick = () => {
      document.getElementById('search-input').value = suggestion.nombre;
      window.location.href = suggestion.ruta;
    };
    suggestionsContainer.appendChild(suggestionItem);
  });

  suggestionsContainer.style.display = 'block';
}

function searchService(event) {
  if (event.key === 'Enter') {
    const query = document.getElementById('search-input').value.toLowerCase();

    const match = suggestionsData.find(item => item.nombre.toLowerCase().includes(query));
    if (match) {
      window.location.href = match.ruta;
    } else {
      alert('Servicio no encontrado. Intente con términos como: facial, corporal, depilacion, masajes, manos, o gift card.');
    }
  }
}

document.addEventListener('click', function (event) {
  if (!event.target.closest('.search-container')) {
    document.getElementById('suggestions').style.display = 'none';
  }
});

function openShareModal(pageTitle, pageDescription, pageUrl, pageImage) {
  const modalContent = `
    <div id="share-modal" class="modal">
      <div class="modal-content">
        <h4>Compartir ${pageTitle}</h4>
        <p>${pageDescription}</p>
        <img src="${pageImage}" alt="${pageTitle}" style="width: 100%; max-width: 300px;">

        <p>Selecciona una red social para compartir:</p>
        <div class="share-buttons">
          <a href="https://www.facebook.com/sharer/sharer.php?u=${encodeURIComponent(pageUrl)}&quote=${encodeURIComponent(pageTitle + ' - ' + pageDescription)}" target="_blank">
            <i class="fa-brands fa-facebook"></i> Facebook
          </a>
          <a href="https://twitter.com/intent/tweet?url=${encodeURIComponent(pageUrl)}&text=${encodeURIComponent(pageTitle + ' - ' + pageDescription)}" target="_blank">
            <i class="fa-brands fa-twitter"></i> Twitter
          </a>
          <a href="https://api.whatsapp.com/send?text=${encodeURIComponent(pageTitle + ' - ' + pageDescription + ' ' + pageUrl)}" target="_blank">
            <i class="fa-brands fa-whatsapp"></i> WhatsApp
          </a>
        </div>
        <button id="close-modal-btn">Cerrar</button>
      </div>
    </div>
  `;

  document.body.insertAdjacentHTML('beforeend', modalContent);
  document.getElementById('close-modal-btn').addEventListener('click', closeModal);
}

function closeModal() {
  const modal = document.getElementById('share-modal');
  if (modal) {
    modal.remove();
  }
}
setTimeout(function () {
  const flashMessages = document.querySelectorAll('.flash-message');
  flashMessages.forEach(function (message) {
    message.style.opacity = '0';
    setTimeout(() => { message.remove(); }, 500);
  });
}, 3000);
function showFlash(messageText, type = 'info', duration = 3000) {
  const flashContainer = document.querySelector('.flash-container') || document.body;
  const container = document.createElement('div');
  container.className = `flash-message flash-${type}`;
  container.innerText = messageText;
  flashContainer.appendChild(container);
  container.style.opacity = '1';
  setTimeout(() => {
    container.style.opacity = '0';
    setTimeout(() => container.remove(), 500);
  }, duration);
}
document.addEventListener('DOMContentLoaded', () => {
  document.querySelectorAll('.flash-message').forEach(msg => {
    setTimeout(() => {
      msg.style.opacity = '0';
      setTimeout(() => msg.remove(), 500);
    }, 3000);
  });
  const sessionTimeout = 3 * 60 * 1000;
  setTimeout(() => {
    showFlash('¡Tu sesión ha expirado!', 'expire');
  }, sessionTimeout);
});











