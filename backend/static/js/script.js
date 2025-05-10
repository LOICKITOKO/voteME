$(document).ready(function(){
    $.get("/api/categories/", function(data){
        let categoriesHTML = '';
        data.forEach(function(category){
            categoriesHTML += `<h2>${category.name}</h2><ul>`;
            category.nominees.forEach(function(nominee){
                // Assurez-vous que 'nominee' est un objet et que 'nominee.name' contient le nom du nominé
                categoriesHTML += `
                    <li data-nominee="${nominee.name}">
                        ${nominee.name}  <!-- Utilisez nominee.name ou la propriété correcte -->
                        <button class="vote-btn">Vote</button>
                    </li>`;
            });
            categoriesHTML += '</ul>';
        });
        $('#categories').html(categoriesHTML);

        $('.vote-btn').click(function(){
            const nominee = $(this).parent().data('nominee');                                               $.post("/api/vote/", { nominee: nominee }, function(response){
                alert('Votre vote a été pris en compte!');
            });
        });
    });
});
