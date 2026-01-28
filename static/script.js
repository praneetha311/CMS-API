let editMode = false;
let editId = null;

// CREATE & UPDATE
function saveCustomer() {
    const customer = {
        id: Number(document.getElementById('id').value),
        name: document.getElementById('name').value,
        email: document.getElementById('email').value,
        phone: document.getElementById('phone').value,
        city: document.getElementById('city').value
    };

    const url = editMode ? `/customers/${editId}` : '/customers';
    const method = editMode ? 'PUT' : 'POST';

    fetch(url, {
        method: method,
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(customer)
    }).then(resetForm);
}

// READ
function loadCustomers() {
    fetch('/customers')
        .then(res => res.json())
        .then(data => {
            document.getElementById('customerTable').innerHTML =
                data.map(c => `
                <tr>
                    <td>${c.id}</td>
                    <td>${c.name}</td>
                    <td>${c.email}</td>
                    <td>${c.phone}</td>
                    <td>${c.city}</td>
                    <td>
                        <button class="edit" onclick="editCustomer(${c.id})">Edit</button>
                        <button class="delete" onclick="deleteCustomer(${c.id})">Delete</button>
                    </td>
                </tr>
            `).join('');
        });
}

// LOAD DATA FOR UPDATE
function editCustomer(id) {
    fetch(`/customers/${id}`)
        .then(res => res.json())
        .then(c => {
            document.getElementById('id').value = c.id;
            document.getElementById('name').value = c.name;
            document.getElementById('email').value = c.email;
            document.getElementById('phone').value = c.phone;
            document.getElementById('city').value = c.city;

            editMode = true;
            editId = id;
            document.getElementById('saveBtn').innerText = 'Update Customer';
        });
}

// DELETE
function deleteCustomer(id) {
    fetch(`/customers/${id}`, { method: 'DELETE' })
        .then(loadCustomers);
}

function resetForm() {
    editMode = false;
    editId = null;
    document.getElementById('saveBtn').innerText = 'Add Customer';
    document.querySelectorAll('input').forEach(i => i.value = '');
    loadCustomers();
}

loadCustomers();
