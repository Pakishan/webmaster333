document.addEventListener("DOMContentLoaded", () => {
    const registrationForm = document.getElementById("registro-formulario-validacion");

    registrationForm.addEventListener("submit", (e) => {
        e.preventDefault();
        const nombre = document.getElementById("nombre").value;
        const usuario = document.getElementById("usuario").value;
        const email = document.getElementById("email").value;
        const telefono = document.getElementById("telefono").value;
        const password = document.getElementById("password").value;
        const confirmPassword = document.getElementById("confirm-password").value;

        // Validar correo electrónico
        const emailRegex = /\S+@\S+\.\S+/;
        if (!emailRegex.test(email)) {
            alert("Por favor ingrese un correo electrónico válido.");
            return;
        }

        // Validar teléfono (solo números)
        const telefonoRegex = /^[0-9]+$/;
        if (!telefonoRegex.test(telefono)) {
            alert("Por favor ingrese un número de teléfono válido.");
            return;
        }

        // Validar contraseñas coincidentes
        if (password !== confirmPassword) {
            alert("Las contraseñas no coinciden.");
            return;
        }

        // Simulación de registro exitoso
        alert("Registro exitoso!");

        // Limpiar formulario
        registrationForm.reset();
    });

    
});

// Array para almacenar los productos en el carrito
var cart = [];

// Función para agregar un producto al carrito
function addToCart(id, name, price) {
  // Verifica si el producto ya está en el carrito
  let productExists = cart.find(item => item.id === id);

  if (productExists) {
    // Si existe, aumenta la cantidad
    productExists.quantity++;
  } else {
    // Si no existe, lo agrega con cantidad 1
    cart.push({ id, name, price, quantity: 1 });
  }

  // Actualiza la tabla del carrito
  updateCartTable();
}

// Función para actualizar la tabla del carrito
function updateCartTable() {
  const cartBody = document.getElementById('cartBody');
  cartBody.innerHTML = '';

  // Recorre el carrito y actualiza la tabla
  cart.forEach((item, index) => {
    const row = `
      <tr>
        <td>${index + 1}</td>
        <td>${item.name}</td>
        <td>${item.price}</td>
        <td>${item.quantity}</td>
        <td>${item.price * item.quantity}</td>
      </tr>
    `;
    cartBody.innerHTML += row;
  });
}

// Función para manejar el evento click en botones "Agregar al carrito"
document.querySelectorAll('.add-to-cart').forEach(button => {
  button.addEventListener('click', () => {
    const id = button.dataset.id;
    const name = button.dataset.name;
    const price = parseFloat(button.dataset.price);

    addToCart(id, name, price);
  });
});

// Función para manejar el evento click en el botón "Pagar"
const checkoutBtn = document.getElementById('checkoutBtn');
checkoutBtn.addEventListener('click', () => {
  // Aquí se podría implementar la lógica para procesar el pago
  alert('Implementar lógica de pago...');
});

//planes

// Array para almacenar los productos en el carrito
let cart = [];

// Evento para agregar producto al carrito
document.querySelectorAll('.add-to-cart').forEach(button => {
    button.addEventListener('click', function() {
        const name = this.getAttribute('data-name');
        const price = parseFloat(this.getAttribute('data-price'));

        // Verificar si el producto ya está en el carrito
        let existingItem = cart.find(item => item.name === name);
        if (existingItem) {
            existingItem.quantity++;
            existingItem.total = existingItem.quantity * price;
        } else {
            cart.push({
                name: name,
                price: price,
                quantity: 1,
                total: price
            });
        }

        // Actualizar el contenido del carrito
        updateCart();
    });
});

// Función para actualizar el contenido del carrito en el DOM
function updateCart() {
    const cartBody = document.getElementById('cartBody');
    cartBody.innerHTML = '';

    cart.forEach(item => {
        const row = document.createElement('tr');
        row.innerHTML = `
            <td>${item.name}</td>
            <td>$${item.price.toFixed(2)}</td>
            <td>${item.quantity}</td>
            <td>$${item.total.toFixed(2)}</td>
        `;
        cartBody.appendChild(row);
    });

    // Actualizar total del carrito
    const total = cart.reduce((acc, item) => acc + item.total, 0);
    document.getElementById('checkoutBtn').innerHTML = `Pagar $${total.toFixed(2)}`;
}

// Evento para cerrar el carrito
document.getElementById('checkoutBtn').addEventListener('click', function() {
    // Aquí puedes implementar la lógica para procesar el pago
    alert('Implementa tu lógica de pago aquí.');
});


