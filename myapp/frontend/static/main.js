function createUser() {
    var id = document.getElementById('userId').value;
    var points = document.getElementById('points').value;
    var cash = document.getElementById('cash').value;
  
    var data = {
      id: id,
      points: parseInt(points),
      cash: parseFloat(cash)
    };
  
    fetch('/api/user', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(data)
    })
    .then(response => {
      if (response.ok) {
        alert('User created successfully!');
      } else {
        response.json()
        .then(error => {
          alert('Error creating user: ' + error.message);
        });
      }
    })
    .catch(error => {
      alert('Error creating user: ' + error.message);
    });
  }
  
  function getUser() {
    var id = document.getElementById('getUserId').value;
  
    fetch('/api/user/' + id, {
      method: 'GET'
    })
    .then(response => {
      if (response.ok) {
        response.json()
        .then(data => {
          alert('User ID: ' + data.id + '\nPoints: ' + data.points + '\nCash: ' + data.cash);
        });
      } else {
        response.json()
        .then(error => {
          alert('Error getting user: ' + error.message);
        });
      }
    })
    .catch(error => {
      alert('Error getting user: ' + error.message);
    });
  }
  
  function deleteUser() {
    var id = document.getElementById('deleteUserId').value;
  
    fetch('/api/user/' + id, {
      method: 'DELETE'
    })
    .then(response => {
      if (response.ok) {
        alert('User deleted successfully!');
      } else {
        response.json()
        .then(error => {
          alert('Error deleting user: ' + error.message);
        });
      }
    })
    .catch(error => {
      alert('Error deleting user: ' + error.message);
    });
  }
  
  function purchaseProduct() {
    var userId = document.getElementById('purchaseUserId').value;
    var productId = document.getElementById('purchaseProductId').value;
  
    fetch('/api/user/' + userId + '/purchase/' + productId, {
      method: 'POST'
    })
    .then(response => {
      if (response.ok) {
        response.json()
        .then(data => {
          alert('Product purchased successfully!\nUser ID: ' + data.id + '\nPoints: ' + data.points + '\nCash: ' + data.cash);
        });
      } else {
        response.json()
        .then(error => {
          alert('Error purchasing product: ' + error.message);
        });
      }
    })
    .catch(error => {
      alert('Error purchasing product: ' + error.message);
    });
  }  