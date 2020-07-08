document.getElementById("formBusquedaGeneral").addEventListener('submit', function () {
    notificacion("Búsqueda General");
});

document.getElementById('formBusquedaBibcode').addEventListener('submit', function () {
    notificacion("Búsqueda por bibcode");
});

document.getElementById('formBusquedaOrcid').addEventListener('submit', function () {
    notificacion("Búsqueda por ORCID");
});

document.getElementById("autor").addEventListener('click', function () {
    document.getElementById('busquedaGeneral').value = (document.getElementById('busquedaGeneral').value + 'author:"" ')
    

});

document.getElementById("primer_autor").addEventListener('click', function () {
    document.getElementById('busquedaGeneral').value = (document.getElementById('busquedaGeneral').value  + 'author:"^" ')
    
});

document.getElementById("año").addEventListener('click', function () {
    document.getElementById('busquedaGeneral').value = (document.getElementById('busquedaGeneral').value  + 'year:')
    
});

document.getElementById("abstract").addEventListener('click', function () {
    document.getElementById('busquedaGeneral').value = (document.getElementById('busquedaGeneral').value  + 'abs:"" ')
    
});

document.getElementById("title").addEventListener('click', function () {
    document.getElementById('busquedaGeneral').value = (document.getElementById('busquedaGeneral').value  + 'title:"" ')
    
});

document.getElementById("database").addEventListener('click', function () {
    document.getElementById('busquedaGeneral').value = (document.getElementById('busquedaGeneral').value  + 'database:"astronomy" ')
    
});

function notificacion(name){
    Swal.fire({
        title: name,
        allowOutsideClick: false,
        allowEscapeKey: false,
        text: 'espere un momento, por favor',
        onBeforeOpen: () => {
            Swal.showLoading()
        },
    });
}