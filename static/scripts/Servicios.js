document.querySelectorAll('.card-product').forEach(function(productCard) {
  let selectedRating = 0;
  const stars = productCard.querySelectorAll('.star');

  stars.forEach(function(star) {
      star.addEventListener('mouseover', function() {
          const rating = parseFloat(star.getAttribute('data-value'));
          highlightStars(rating, stars);
      });

      star.addEventListener('click', function() {
          selectedRating = parseFloat(star.getAttribute('data-value'));
          highlightStars(selectedRating, stars);
      });

      star.addEventListener('mouseleave', function() {
          highlightStars(selectedRating, stars);
      });
  });

  function highlightStars(rating, stars) {
      stars.forEach(function(star) {
          const starValue = parseFloat(star.getAttribute('data-value'));
          if (starValue <= rating) {
              star.classList.add('checked');
          } else {
              star.classList.remove('checked');
          }
      });
  }
});
document.querySelectorAll('.card-product').forEach(function(productCard) {
  const shareButton = productCard.querySelector('.share');
  if (shareButton) {
    shareButton.addEventListener('click', function() {
      const productName = productCard.querySelector('h3').innerText;
      const productDescription = productCard.querySelector('p').innerText;
      const productUrl = "https://tuweb.com/producto/123";
      const productImage = productCard.querySelector('img').src;
      const productPrice = productCard.querySelector('.price').innerText;

      openShareModal(productName, productDescription, productUrl, productImage, productPrice);
    });
  }
});
function openShareModal(productName, productDescription, productUrl, productImage, productPrice) {
  const modalContent = `
    <div id="share-modal" class="modal">
      <div class="modal-content">
        <h4>Compartir ${productName}</h4>
        <p>${productDescription}</p>
        <p><strong>Precio: ${productPrice}</strong></p>
        <img src="${productImage}" alt="${productName}" style="width: 100%; max-width: 300px;">
        <p>Selecciona una red social para compartir:</p>
        <div class="share-buttons">
          <a href="https://www.facebook.com/sharer/sharer.php?u=${encodeURIComponent(productUrl)}&quote=${encodeURIComponent(productName + ' - ' + productDescription + ' Precio: ' + productPrice)}" target="_blank">
            <i class="fa-brands fa-facebook"></i> Facebook
          </a>
          <a href="https://twitter.com/intent/tweet?url=${encodeURIComponent(productUrl)}&text=${encodeURIComponent(productName + ' - ' + productDescription + ' Precio: ' + productPrice)}" target="_blank">
            <i class="fa-brands fa-twitter"></i> Twitter
          </a>
          <a href="https://api.whatsapp.com/send?text=${encodeURIComponent(productName + ' - ' + productDescription + ' Precio: ' + productPrice + ' ' + productUrl)}" target="_blank">
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

