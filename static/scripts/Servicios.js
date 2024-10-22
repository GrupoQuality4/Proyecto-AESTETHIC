document.querySelectorAll('.card-product').forEach(function(productCard) {
  const stars = productCard.querySelectorAll('.star');
  stars.forEach(function(star, index) {
    star.addEventListener('click', function() {
      for (let i = 0; i <= index; i++) {
        stars[i].classList.add('checked');
      }
      for (let i = index + 1; i < stars.length; i++) {
        stars[i].classList.remove('checked');
      }
    });
  });
  const shareButton = productCard.querySelector('.share');
  shareButton.addEventListener('click', function() {
    const productName = productCard.querySelector('h3').innerText;
    const productDescription = productCard.querySelector('p').innerText;
    const productUrl = "https://tuweb.com/producto/123";
    const productImage = productCard.querySelector('img').src;
    const productPrice = productCard.querySelector('.price').innerText;

    openShareModal(productName, productDescription, productUrl, productImage, productPrice);
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
});

